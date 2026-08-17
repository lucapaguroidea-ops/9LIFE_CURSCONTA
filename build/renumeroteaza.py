"""Renumerotarea fluxurilor: o singură trecere peste toate celulele.

`date/` continuă să folosească ID-urile vechi (F-01…F-62). Trecerea asta le schimbă
în cele noi, pe clase (F-101…F-802), în FIECARE celulă din FIECARE foaie a ambelor
workbook-uri. Așa nicio referință încrucișată nu poate fi ratată — nici cele din
`Plan de conturi!Flux (pas)`, nici cele din `Matrice acoperire`, nici cele din
textele de corelații sau din notele modulelor.

Tiparul e strict `F-` urmat de EXACT două cifre, delimitat. Deci:
  - `F-14` se înlocuiește;
  - `F-316` (deja renumerotat) rămâne neatins, pentru că are trei cifre;
  - `F-1` sau `F-140` nu se potrivesc.
Nu există lanțuri de înlocuire: sursele au două cifre, țintele au trei.
"""
import re

#: `(?<!fost )` protejează etichetele de tip „[fost F-27]”, care trebuie să rămână în
#: numerotarea VECHE — ele spun tocmai de unde vine fluxul. Restul se renumerotează.
RE_VECHI = re.compile(r"(?<!fost )\bF-(\d{2})\b")


def in_text(text, harta):
    """Înlocuiește ID-urile vechi dintr-un text. Textele fără ID rămân identice."""
    if not isinstance(text, str) or "F-" not in text:
        return text
    return RE_VECHI.sub(lambda m: harta.get(m.group(0), m.group(0)), text)


def in_workbook(wb, harta, *, exclude=()):
    """Renumerotează toate celulele de text. Întoarce numărul de celule schimbate.

    `exclude`: foi care NU se renumerotează. Foaia `Istoric` intră aici obligatoriu —
    ea ține tabelul de echivalență vechi → nou, iar renumerotarea coloanei „ID vechi”
    ar distruge exact informația pentru care există foaia.
    """
    schimbate = 0
    for ws in wb.worksheets:
        if ws.title in exclude:
            continue
        for row in ws.iter_rows():
            for cell in row:
                v = cell.value
                if not isinstance(v, str):
                    continue
                nou = in_text(v, harta)
                if nou != v:
                    cell.value = nou
                    schimbate += 1
    return schimbate


def ramase(wb, cunoscute, *, exclude=()):
    """ID-uri vechi care au supraviețuit trecerii — semn că harta e incompletă.

    `cunoscute` sunt ID-urile vechi din hartă. Orice `F-<2 cifre>` rămas în fișier
    e ori o scăpare a hărții, ori un ID inventat pe undeva; ambele sunt erori.

    `exclude` trebuie să conțină aceleași foi ca la `in_workbook` — în `Istoric`,
    ID-urile vechi sunt conținut intenționat, nu scăpări.
    """
    gasite = {}
    for ws in wb.worksheets:
        if ws.title in exclude:
            continue
        for row in ws.iter_rows():
            for cell in row:
                if not isinstance(cell.value, str):
                    continue
                for m in RE_VECHI.finditer(cell.value):
                    if m.group(0) in cunoscute:
                        gasite.setdefault(m.group(0), []).append(f"{ws.title}!{cell.coordinate}")
    return gasite
