"""Foaia „Întrebări deschise” — ce anume din workbook e încă provizoriu.

Workbook-ul prezintă regulile ca tranșate. O parte nu sunt: unde notițele erau ambigue
sau unde practica diferă, a trebuit să aleg ca să pot merge mai departe. Alegerile alea
existau doar în documentele `.md` și în celulele `Check` ale modulelor — deci cine
deschidea Excel-ul nu avea de unde ști ce e sigur și ce e presupus.

Foaia se generează din `date/intrebari.py`, aceeași sursă ca documentul trimisibil și
ca pagina publicată. Trei formate, un singur adevăr.

În plus, fluxurile și corelațiile atinse de o întrebare primesc un marcaj `❓ Î-nn`, ca
semnalul să apară acolo unde te uiți, nu doar într-o foaie separată.
"""
import re

from build import stil
from date import intrebari as I

RE_TOKEN = re.compile(r"\b(F-\d{3}|MOD_[A-Z_]+|C-\d{2})\b")

NUME = "Întrebări deschise"
LATIMI = {"A": 7, "B": 30, "C": 54, "D": 22, "E": 58, "F": 56, "G": 24}


def _tokenuri(q):
    """Ce atinge întrebarea, în ordinea apariției, fără duplicate."""
    out = []
    for camp in ("conteaza", "presupunere"):
        for t in RE_TOKEN.findall(str(q.get(camp) or "")):
            if t not in out:
                out.append(t)
    return out


def _scrie_rand(ws, r, valori, fill=None):
    for c, v in enumerate(valori, start=1):
        stil.scrie(ws, r, c, v, font=stil.F_NORMAL, fill=fill, align=stil.A_WRAP_TOP)


def construieste(wb, dupa="Matrice acoperire"):
    """Creează foaia și întoarce {token: [„Î-01”, …]} pentru marcajele din restul foilor."""
    index = wb.sheetnames.index(dupa) + 1 if dupa in wb.sheetnames else len(wb.sheetnames)
    ws = wb.create_sheet(NUME, index)
    for col, lat in LATIMI.items():
        ws.column_dimensions[col].width = lat

    r = 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
    stil.scrie(ws, r, 1, "ÎNTREBĂRI DESCHISE — ce e încă provizoriu în acest workbook",
               font=stil.F_TITLU)
    r += 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
    stil.scrie(ws, r, 1,
               "Restul foilor prezintă regulile ca tranșate. Cele de mai jos nu sunt: "
               "notițele erau ambigue sau practica diferă, iar coloana „Ce am presupus” "
               "spune ce am ales ca să pot merge mai departe. Un răspuns diferit schimbă "
               "exact ce scrie acolo. Fluxurile și corelațiile atinse poartă marcajul ❓.",
               font=stil.F_NOTA, align=stil.A_WRAP_TOP)
    r += 2

    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
    stil.scrie(ws, r, 1, "Cele trei care blochează cel mai mult", font=stil.F_TITLU_BLOC)
    r += 1
    for cheie, motiv in _prioritare():
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
        stil.scrie(ws, r, 1, f"❓  {cheie}  —  {motiv}", font=stil.F_AVERTISMENT,
                   align=stil.A_WRAP_TOP)
        r += 1
    r += 1

    for c, h in enumerate(["Nr.", "Temă", "Întrebare", "Atinge",
                           "Ce depinde de răspuns", "Ce am presupus", "Sursa"], start=1):
        stil.scrie(ws, r, c, h, font=stil.F_CAP_TABEL_ALB, fill=stil.FILL_ANTET,
                   align=stil.A_CENTER)
    r += 1

    marcaje = {}
    nr = 0
    for tema, qs in I.TEME:
        for q in qs:
            nr += 1
            eticheta = f"Î-{nr:02d}"
            toks = _tokenuri(q)
            for t in toks:
                marcaje.setdefault(t, []).append(eticheta)
            _scrie_rand(ws, r, [
                eticheta, tema, q["intrebare"], "\n".join(toks) or "—",
                q["conteaza"], q["presupunere"] or "— nu a fost nevoie de o presupunere",
                q["sursa"],
            ])
            r += 1

    r += 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
    stil.scrie(ws, r, 1,
               f"{I.TOTAL} de întrebări, {len(I.TEME)} teme. Aceeași sursă cu "
               "dist/intrebari-formator.md și cu pagina publicată — nu pot diverge.",
               font=stil.F_NOTA, align=stil.A_WRAP_TOP)

    ws.freeze_panes = "A9"
    return marcaje


def _prioritare():
    """Cele trei scoase în față, cu formularea scurtă a întrebării."""
    from build.intrebari import PRIORITARE, _gaseste
    return [(_gaseste(k)["intrebare"], motiv) for k, motiv in PRIORITARE]


def marcheaza(wb, marcaje):
    """Pune `❓ Î-nn` pe fluxurile și corelațiile atinse. Întoarce câte a scris."""
    scrise = 0

    ws = wb["Fluxuri"]
    for r in range(1, ws.max_row + 1):
        fid = str(ws.cell(row=r, column=1).value or "").strip()
        if not re.fullmatch(r"F-\d{3}", fid):
            continue
        if str(ws.cell(row=r, column=4).value or "").strip() not in ("nu", "★ DA"):
            continue
        scrise += _marc(ws, r, 8, marcaje.get(fid))

    wc = wb["Corelații de control"]
    for r in range(1, wc.max_row + 1):
        cid = str(wc.cell(row=r, column=1).value or "").strip()
        if re.fullmatch(r"C-\d{2}", cid):
            scrise += _marc(wc, r, 6, marcaje.get(cid))
    return scrise


def _marc(ws, rand, col, etichete):
    if not etichete:
        return 0
    cell = ws.cell(row=rand, column=col)
    vechi = str(cell.value or "").strip()
    marcaj = "❓ " + ", ".join(etichete)
    if marcaj in vechi:
        return 0
    cell.value = marcaj if vechi in ("", "—") else f"{vechi} | {marcaj}"
    return 1
