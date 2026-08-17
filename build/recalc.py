"""Recalc pur-Python, fără LibreOffice.

openpyxl scrie formule dar nu le evaluează, deci fișierul livrat nu are valori
cache-uite. LibreOffice headless nu funcționează în acest mediu (filtrele de
conversie nu se încarcă), așa că recalc-ul se face cu biblioteca `formulas`:

1. Setează `fullCalcOnLoad=True` — orice aplicație reală (Excel, LibreOffice,
   Google Sheets, Numbers) recalculează la deschidere.
2. Evaluează workbook-ul cu `formulas` și injectează valorile în XML-ul foilor
   (adaugă `<v>` la celulele cu `<f>`), fără să atingă stilurile scrise de openpyxl.
   Astfel `data_only=True` citește valorile și fișierul arată complet și în vizualizatoare
   care nu recalculează.

Întoarce dicționarul {(SHEET_UPPER, COORD): valoare} — folosit și de verifica.py.
"""
import os
import re
import shutil
import sys
import warnings
import zipfile
from xml.sax.saxutils import escape

import numpy as np
import xml.etree.ElementTree as ET

import openpyxl

warnings.filterwarnings("ignore")

_KEY = re.compile(r"\](.+?)'?!\$?([A-Z]+)\$?(\d+)$")
# O celulă goală e auto-închisă: `<c r="B10" s="81"/>`. Dacă tiparul o tratează ca
# deschizător, `(.*?)</c>` sare peste ea și înghite CELULA URMĂTOARE — iar injectarea
# scrie atributul în mijlocul lui `/>`, producând XML invalid. De aceea alternativa
# auto-închisă e recunoscută explicit, prima, și lăsată neatinsă.
_CELL = re.compile(
    r'(?P<sing><c\b[^>]*\br="[A-Z]+\d+"[^>]*/>)'
    r'|(?P<open><c\b[^>]*\br="(?P<coord>[A-Z]+\d+)"[^>]*>)(?P<inner>.*?)(?P<close></c>)',
    re.DOTALL)
_V = re.compile(r"<v\b[^>]*/>|<v\b[^>]*>.*?</v>", re.DOTALL)


def _scalar(v):
    x = getattr(v, "value", v)
    try:
        arr = np.asarray(x)
        if arr.size >= 1:
            return arr.flatten()[0]
    except Exception:
        pass
    return x


def evalueaza(path: str) -> dict:
    """Evaluează formulele cu `formulas`; întoarce {(SHEET_UPPER, COORD): valoare}."""
    import formulas

    xl = formulas.ExcelModel().loads(path).finish()
    sol = xl.calculate()
    vals = {}
    for k, v in sol.items():
        m = _KEY.search(k)
        if not m:
            continue
        sheet = m.group(1).strip("'").upper()
        coord = f"{m.group(2)}{m.group(3)}"
        vals[(sheet, coord)] = _scalar(v)
    return vals


def _attr(elem: str, name: str) -> str:
    m = re.search(rf'\b{name}="([^"]+)"', elem)
    return m.group(1) if m else ""


def _norm_target(target: str) -> str:
    """Normalizează Target-ul din rels la o cale de arhivă (xl/worksheets/sheetN.xml)."""
    if target.startswith("/"):
        return target.lstrip("/")            # cale absolută: /xl/worksheets/... -> xl/...
    if target.startswith("xl/"):
        return target
    return "xl/" + target                    # cale relativă la xl/: worksheets/... -> xl/worksheets/...


def _sheet_file_map(zf: zipfile.ZipFile):
    """{ SHEET_NAME_UPPER : 'xl/worksheets/sheetN.xml' } din workbook.xml + rels."""
    wbxml = zf.read("xl/workbook.xml").decode("utf-8")
    rels = zf.read("xl/_rels/workbook.xml.rels").decode("utf-8")
    rid2target = {}
    for rel in re.findall(r"<Relationship\b[^>]*/>", rels):
        rid2target[_attr(rel, "Id")] = _norm_target(_attr(rel, "Target"))
    out = {}
    for sheet in re.findall(r"<sheet\b[^>]*/>", wbxml):
        name = _attr(sheet, "name")
        rid = _attr(sheet, "r:id")
        target = rid2target.get(rid, "")
        if name and target:
            out[name.upper()] = target
    return out


def _fmt(value) -> tuple:
    """Întoarce (text_xml, tip) pentru un `<v>`; tip='str' pentru text."""
    if value is None:
        return None
    if isinstance(value, str):
        if value == "" or value.startswith("#"):
            # celulă goală sau eroare — nu injectăm valoare cache
            return None
        return escape(value), "str"
    if isinstance(value, bool):
        return ("1" if value else "0"), "b"
    if isinstance(value, (int, np.integer)):
        return str(int(value)), None
    if isinstance(value, (float, np.floating)):
        if np.isnan(value):
            return None
        f = float(value)
        return (str(int(f)) if f.is_integer() else repr(f)), None
    return escape(str(value)), "str"


def injecteaza(path: str, vals: dict) -> None:
    """Adaugă valori cache în celulele cu formulă, păstrând tot restul XML-ului."""
    tmp = path + ".tmp"
    with zipfile.ZipFile(path, "r") as zin:
        smap = _sheet_file_map(zin)
        file2sheet = {v: k for k, v in smap.items()}
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename in file2sheet:
                    sheet = file2sheet[item.filename]
                    data = _patch_sheet(data.decode("utf-8"), sheet, vals).encode("utf-8")
                zout.writestr(item, data)
    shutil.move(tmp, path)


def _patch_sheet(xml: str, sheet_upper: str, vals: dict) -> str:
    def repl(m):
        if m.group("sing") is not None:
            return m.group(0)                     # celulă goală, auto-închisă
        open_tag, coord = m.group("open"), m.group("coord")
        inner, close = m.group("inner"), m.group("close")
        if "<f" not in inner:
            return m.group(0)                    # nu e celulă cu formulă
        got = vals.get((sheet_upper, coord))
        fmt = _fmt(got)
        if fmt is None:
            return m.group(0)
        text, typ = fmt
        inner = _V.sub("", inner)                 # scoate orice <v> gol lăsat de openpyxl
        # tipul curent al celulei (t="...") trebuie să reflecte valoarea injectată
        new_open = re.sub(r'\s+t="[^"]*"', "", open_tag)
        if typ:
            new_open = new_open[:-1].rstrip() + f' t="{typ}">'
        return f"{new_open}{inner}<v>{text}</v>{close}"

    nou = _CELL.sub(repl, xml)
    # Gardă: o injectare care strică XML-ul trebuie să pice aici, nu la citirea de peste
    # trei pași, cu un traceback de parser care nu spune nimic despre cauză.
    try:
        ET.fromstring(nou)
    except ET.ParseError as e:
        raise SystemExit(
            f"recalc: injectarea a produs XML invalid în foaia {sheet_upper}: {e}") from e
    return nou


def recalc(path: str) -> dict:
    wb = openpyxl.load_workbook(path)
    try:
        wb.calculation.fullCalcOnLoad = True
    except Exception:
        pass
    wb.save(path)
    vals = evalueaza(path)
    injecteaza(path, vals)
    return vals


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    for p in sys.argv[1:]:
        print(f"recalc: {p}")
        recalc(os.path.abspath(p))
    print("gata.")
