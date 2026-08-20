"""Foaia „Închideri periodice” — disciplina de închidere, derivată din fluxuri.

Aserțiunile nu se scriu aici. Sunt deja în monografii, în pașii de verificare:

    F-405  „Sold 4426 = 0; sold 4427 = 0; sold 4423 = 5.250”
    F-501  „Sold 581 = 0. Fără 581: dacă se face 531=512 direct înainte…”
    F-502  „Sold 542 = 0 după decont. Dacă rămâne sold → angajatul are…”

Foaia le CITEȘTE de acolo, la fel cum `build/parcurs.py` citește harta documentelor de
referință din tabelul de structură al Legendei în loc s-o rescrie. O listă scrisă
separat ar începe să diveargă de monografii din prima zi în care cineva schimbă un flux.

Din `date/inchideri.py` vine doar cadența — cât de des te uiți. Un flux spune ce stare
atinge contul, nu la ce interval trebuie verificat; asta e judecată, nu derivare.

Conturile fără aserțiune apar cu ancora goală și cu motivul din `GOLURI`. Un checklist
care afirmă ceva ce sistemul nu demonstrează e mai rău decât unul incomplet — de aceea
golul se vede, nu se ascunde.
"""
import re

from build import stil
from date import inchideri as I

NUME = "Închideri periodice"
LATIMI = {"A": 26, "B": 22, "C": 46, "D": 15, "E": 62, "F": 34}

#: „Sold 4426 = 0”, „soldul 581”, „Sold 471/472 scade”. Primul grup e lista de conturi.
RE_SOLD = re.compile(r"[Ss]old(?:ul)?\s+([0-9][0-9x./]{1,9}(?:\s*/\s*[0-9][0-9x./]{1,9})*)")
RE_SIMBOL = re.compile(r"\d{3,4}")


def simboluri(text):
    """Simbolurile de cont dintr-o descriere de cadență: „408 / 418” → [408, 418]."""
    out = []
    for m in RE_SIMBOL.finditer(str(text or "")):
        if m.group(0) not in out:
            out.append(m.group(0))
    return out


def asertiuni(wb):
    """{simbol: [(flux, pas, text)]} — stările terminale declarate în monografii.

    Se filtrează contra simbolurilor din `Plan de conturi`: fără filtru, regexul ia
    drept cont și numerele care urmează cuvântului „sold” („sold 12.000”).
    """
    ws_plan = wb["Plan de conturi"]
    cunoscute = set()
    for r in range(1, ws_plan.max_row + 1):
        v = str(ws_plan.cell(row=r, column=1).value or "").strip()
        if re.fullmatch(r"\d{3,4}([./]\d+)?", v):
            cunoscute.add(v.split(".")[0].split("/")[0])

    ws = wb["Fluxuri"]
    out = {}
    for r in range(1, ws.max_row + 1):
        fid = str(ws.cell(row=r, column=1).value or "").strip()
        if not re.fullmatch(r"F-\d+", fid):
            continue
        pas = str(ws.cell(row=r, column=3).value or "").strip()
        txt = str(ws.cell(row=r, column=4).value or "").strip()
        for m in RE_SOLD.finditer(txt):
            for bucata in re.split(r"\s*/\s*", m.group(1)):
                cont = bucata.strip(" .")
                baza = cont.split(".")[0]
                # Planul ține sinteticele de 3 cifre; 1621 și 5187 sunt analitice de
                # gradul II sub 162 și 518. Fără prefix, ele ar apărea drept goluri
                # deși fluxul lor chiar declară starea terminală.
                if baza not in cunoscute and baza[:3] not in cunoscute:
                    continue
                out.setdefault(baza, []).append((fid, pas, txt))
    return out


def construieste(wb, dupa="Corelații de control"):
    """Creează foaia. Întoarce (nr_rânduri, nr_goluri) pentru raportul de build."""
    index = wb.sheetnames.index(dupa) + 1 if dupa in wb.sheetnames else len(wb.sheetnames)
    ws = wb.create_sheet(NUME, index)
    for col, lat in LATIMI.items():
        ws.column_dimensions[col].width = lat

    harta = asertiuni(wb)

    r = 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=6)
    stil.scrie(ws, r, 1, I.TITLU, font=stil.F_TITLU)
    r += 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=6)
    stil.scrie(ws, r, 1, I.NOTA, font=stil.F_NOTA, align=stil.A_WRAP_TOP)
    r += 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=6)
    stil.scrie(ws, r, 1,
               "Coloana „Stare terminală declarată” nu e scrisă aici: e citită din pașii "
               "de verificare ai fluxurilor. Dacă se schimbă o monografie, se schimbă și "
               "rândul de mai jos. Un rând fără flux e un gol cunoscut — checklistul cere "
               "ceva ce sistemul nu demonstrează încă, iar coloana din dreapta spune ce "
               "lipsește.", font=stil.F_NOTA, align=stil.A_WRAP_TOP)
    r += 2

    goluri = 0
    randuri = 0
    for cadenta in I.CADENTE:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=6)
        stil.scrie(ws, r, 1, cadenta, font=stil.F_TITLU_BLOC)
        r += 1
        for cap, col in zip(["Cont", "Cadență", "De ce se urmărește",
                             "Flux", "Stare terminală declarată", "Gol cunoscut"],
                            range(1, 7)):
            stil.scrie(ws, r, col, cap, font=stil.F_CAP_TABEL_ALB,
                       fill=stil.FILL_ANTET, align=stil.A_WRAP)
        r += 1

        for cont, cad, dece in I.CADENTA:
            if cad != cadenta:
                continue
            simb = simboluri(cont)
            fluxuri, stari, lipsuri = [], [], []
            for s in simb:
                if s in harta:
                    for fid, pas, txt in harta[s][:2]:
                        if fid not in fluxuri:
                            fluxuri.append(fid)
                        # tăierea la prima propoziție, nu la primul punct:
                        # „Sold 473 la 31.12” nu e două propoziții.
                        scurt = re.split(r"\.\s", txt)[0].strip().rstrip(".")
                        if scurt not in stari:
                            stari.append(scurt)
                elif s in I.GOLURI:
                    lipsuri.append(f"{s}: {I.GOLURI[s]}")
                else:
                    lipsuri.append(f"{s}: niciun flux nu declară starea lui terminală.")

            fill = stil.FILL_NU if lipsuri and not fluxuri else None
            for col, val in enumerate(
                    [cont, cad, dece, " · ".join(fluxuri) or "—",
                     " · ".join(stari) or "—", " ".join(lipsuri) or "—"], start=1):
                stil.scrie(ws, r, col, val, font=stil.F_NORMAL,
                           fill=fill, align=stil.A_WRAP_TOP)
            if lipsuri:
                goluri += 1
            randuri += 1
            r += 1
        r += 1

    ws.freeze_panes = "A6"
    return randuri, goluri
