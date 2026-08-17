"""Generează dist/Module_Declarative_Fluxuri.xlsx.

Extindere pe bază de seed: se încarcă workbook-ul original din
`surse/training-4-2026-08-14/` și se adaugă modulele noi din `date/module/`,
fiecare cu setul complet de patru foi, pe tiparul lui MOD_INCHIDERE_TVA:

    Declarații_<COD>   input galben (font albastru) + calcule auto
    Reguli_<COD>       tabele fixe — se editează doar când se schimbă legea
    Jurnale_<COD>      blocuri de înregistrări, prin formulă, cu celule Check
    NotaExport_<COD>   1 rând = 1 înregistrare, cu coloana Include

`Parametri` primește pragurile noi ÎNAINTE de construirea modulelor, ca acestea
să poată referi celulele reale (nu coordonate ghicite).

Rulare:  python build/build_module.py
"""
import os
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from build import stil  # noqa: E402
from build.foaie import Foaie  # noqa: E402
from build.recalc import recalc  # noqa: E402
from date.module import MODULE, PARAMETRI_NOI  # noqa: E402

RADACINA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = os.path.join(RADACINA, "surse", "training-4-2026-08-14", "Module_Declarative_Fluxuri.xlsx")
IESIRE = os.path.join(RADACINA, "dist", "Module_Declarative_Fluxuri.xlsx")


def extinde_parametri(wb):
    """Scrie parametrii noi și întoarce {cheie: 'Parametri!Bxx'}."""
    ws = wb["Parametri"]
    rand = ws.max_row + 2
    stil.scrie(ws, rand, 1, "Parametri adăugați în Etapa 4 (capitaluri și imobilizări)",
               font=stil.F_TITLU_BLOC)
    rand += 1
    if ws.column_dimensions["C"].width is None or ws.column_dimensions["C"].width < 50:
        ws.column_dimensions["C"].width = 56

    refs = {}
    for cheie, eticheta, valoare, nota in PARAMETRI_NOI:
        stil.scrie(ws, rand, 1, eticheta, font=stil.F_NORMAL, align=stil.A_WRAP)
        stil.scrie(ws, rand, 2, valoare, font=stil.F_INPUT, fill=stil.FILL_INPUT)
        stil.scrie(ws, rand, 3, nota, font=stil.F_NOTA, align=stil.A_WRAP)
        refs[cheie] = f"Parametri!B{rand}"
        rand += 1
    return refs


def insereaza_randuri(ws, rand, n):
    """`insert_rows` care deplasează ȘI celulele îmbinate.

    openpyxl mută valorile la inserare, dar lasă `merged_cells` pe loc. Pe o foaie
    cu îmbinări (CatalogModule are A1:H1, A17:H17 …) rândurile noi cad peste un
    merge rămas nedeplasat, iar tot ce se scrie în afara colțului stânga-sus se
    pierde tăcut la salvare. De aceea îmbinările se desfac, se inserează, apoi se
    refac deplasate.
    """
    afectate = [m for m in list(ws.merged_cells.ranges) if m.min_row >= rand]
    for m in afectate:
        ws.unmerge_cells(str(m))
    ws.insert_rows(rand, amount=n)
    for m in afectate:
        ws.merge_cells(start_row=m.min_row + n, start_column=m.min_col,
                       end_row=m.max_row + n, end_column=m.max_col)


def extinde_catalog(wb, module):
    ws = wb["CatalogModule"]
    rand = None
    for r in range(1, ws.max_row + 1):
        v = ws.cell(row=r, column=1).value
        if v and str(v).strip().startswith("REGULĂ DE SUMONARE"):
            rand = r
            break
    if rand is None:
        raise SystemExit("Nu găsesc blocul „REGULĂ DE SUMONARE” în CatalogModule")

    insereaza_randuri(ws, rand, len(module) + 1)
    for i, m in enumerate(module):
        r = rand + i
        cat = m.CATALOG
        stil.scrie(ws, r, 1, "NU", font=stil.F_INPUT, fill=stil.FILL_NU, align=stil.A_CENTER)
        for col, val in enumerate([m.COD, cat["fluxuri"], cat["tip"], cat["variabile"],
                                   cat["porti"], cat["blocuri"], "IMPLEMENTAT"], start=2):
            stil.scrie(ws, r, col, val, font=stil.F_NORMAL, fill=stil.FILL_DA,
                       align=stil.A_WRAP)


def marcheaza_leasing_implementat(wb):
    """MOD_LEASING_FIN era „EXEMPLU EXTERN” în catalogul original."""
    ws = wb["CatalogModule"]
    for r in range(1, ws.max_row + 1):
        if str(ws.cell(row=r, column=2).value or "").strip() == "MOD_LEASING_FIN":
            if str(ws.cell(row=r, column=8).value or "").strip() == "EXEMPLU EXTERN":
                ws.cell(row=r, column=8,
                        value="ÎNLOCUIT — vezi rândul MOD_LEASING_FIN implementat mai jos")
                return
    # rândul vechi poate lipsi; nu e o eroare


def main():
    if not os.path.exists(SEED):
        raise SystemExit(f"Lipsește fișierul-sămânță: {SEED}")
    wb = openpyxl.load_workbook(SEED)

    P = extinde_parametri(wb)

    def fabrica(nume, latimi=None):
        return Foaie(wb, nume, latimi)

    for m in MODULE:
        m.construieste(fabrica, P)

    marcheaza_leasing_implementat(wb)
    extinde_catalog(wb, MODULE)

    os.makedirs(os.path.dirname(IESIRE), exist_ok=True)
    wb.save(IESIRE)
    recalc(IESIRE)
    print(f"scris: {os.path.relpath(IESIRE, RADACINA)}  "
          f"({len(MODULE)} module noi × 4 foi = {len(MODULE) * 4} foi adăugate)")


if __name__ == "__main__":
    main()
