"""Închide invariantul cont → flux → modul, în ambele sensuri.

Sistemul își declară singur regula: din orice cont Tier A ajungi la fluxurile
relevante, iar de acolo la modulul care produce nota contabilă. Ultimul pas lipsea
pentru modulele adăugate ulterior: fluxurile, corelațiile și matricea știau de fluxuri,
dar nu și de motoarele care le execută.

Ancorele NU se scriu de mână. Fiecare modul declară în `CATALOG["fluxuri"]` ce acoperă,
iar corelațiile și matricea au deja liste de fluxuri — deci legătura se DEDUCE. O hartă
scrisă separat ar fi al doilea adevăr, care diverge la primul modul nou.

Modulele preexistente (cele din workbook-ul-sămânță) nu sunt în `date/module`, deci
maparea lor se citește din foaia `Index module` a semințelor.
"""
import re

RE_FLUX = re.compile(r"F-\d+")
RE_MOD = re.compile(r"MOD_[A-Z_]+")

COL_FLUX_NOTA = 8        # Fluxuri: „Note / Declarativ legat”
COL_COREL_MODUL = 6      # Corelații de control: „Flux / modul legat”
COL_MATRICE_NOTA = 5     # Matrice acoperire: „Pas revelator / note”


def harta_flux_modul(module, ws_index_seed, harta_renumerotare):
    """{flux nou: [MOD_…]} — din modulele proprii + cele preexistente din sămânță."""
    out = {}

    def adauga(flux, cod):
        f = harta_renumerotare.get(flux, flux)
        if cod not in out.setdefault(f, []):
            out[f].append(cod)

    for m in module:
        for f in RE_FLUX.findall(m.CATALOG["fluxuri"]):
            adauga(f, m.COD)

    # modulele care existau deja în sămânță: maparea lor stă în „Index module”
    if ws_index_seed is not None:
        for r in range(1, ws_index_seed.max_row + 1):
            cod = str(ws_index_seed.cell(row=r, column=1).value or "").strip()
            if not cod.startswith("MOD_"):
                continue
            for f in RE_FLUX.findall(str(ws_index_seed.cell(row=r, column=2).value or "")):
                adauga(f, cod)
    return out


def _adauga_in_celula(ws, rand, col, module, sablon):
    """Adaugă ancorele lipsă, păstrând ce era în celulă. Întoarce 1 dacă a scris."""
    cell = ws.cell(row=rand, column=col)
    vechi = str(cell.value or "").strip()
    lipsa = [m for m in module if m not in RE_MOD.findall(vechi)]
    if not lipsa:
        return 0
    ancora = sablon.format(module=" / ".join(lipsa))
    cell.value = ancora if vechi in ("", "—") else f"{vechi} | {ancora}"
    return 1


def _module_pentru(text, harta):
    """Modulele care acoperă fluxurile menționate într-o celulă, fără duplicate."""
    out = []
    for f in RE_FLUX.findall(str(text or "")):
        for m in harta.get(f, []):
            if m not in out:
                out.append(m)
    return out


def adauga(wb, harta, *, didactic=("nu", "★ DA")):
    """Scrie ancorele în Fluxuri, Corelații de control și Matrice acoperire."""
    scrise = {"fluxuri": 0, "corelatii": 0, "matrice": 0}

    # --- catalogul de fluxuri: fluxul își numește modulul
    ws = wb["Fluxuri"]
    for r in range(1, ws.max_row + 1):
        fid = str(ws.cell(row=r, column=1).value or "").strip()
        if not RE_FLUX.fullmatch(fid):
            continue
        if str(ws.cell(row=r, column=4).value or "").strip() not in didactic:
            continue
        module = harta.get(fid, [])
        if module:
            scrise["fluxuri"] += _adauga_in_celula(
                ws, r, COL_FLUX_NOTA, module, "modul: {module}")

    # --- corelații: de la fluxurile pe care le verifică, la motoarele lor
    wc = wb["Corelații de control"]
    for r in range(1, wc.max_row + 1):
        if not re.fullmatch(r"C-\d+", str(wc.cell(row=r, column=1).value or "").strip()):
            continue
        module = _module_pentru(wc.cell(row=r, column=COL_COREL_MODUL).value, harta)
        if module:
            scrise["corelatii"] += _adauga_in_celula(
                wc, r, COL_COREL_MODUL, module,
                "Module_Declarative_Fluxuri.xlsx → {module}")

    # --- matrice: contul → fluxurile lui → modulele lor
    wm = wb["Matrice acoperire"]
    for r in range(1, wm.max_row + 1):
        simbol = str(wm.cell(row=r, column=1).value or "").strip()
        if not simbol or simbol in ("Simbol",):
            continue
        module = _module_pentru(wm.cell(row=r, column=4).value, harta)
        if module:
            scrise["matrice"] += _adauga_in_celula(
                wm, r, COL_MATRICE_NOTA, module, "modul: {module}")

    return scrise
