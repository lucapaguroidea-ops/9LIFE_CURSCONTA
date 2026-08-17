"""Porțile de calitate ale sistemului. Cod de ieșire ≠ 0 la orice eșec.

Porțile (din foaia Legendă a workbook-ului original, plus cele adăugate în Etapa 4):

  1. ΣDebit = ΣCredit pe fiecare pas de flux care are sume
  2. fiecare flux se închide cu un pas de verificare și o stare terminală declarată
  3. fiecare flux didactic ★ are exact un pas revelator
  4. fiecare cont Tier A apare în cel puțin un flux (matricea fără goluri)
  5. fiecare analitic recomandat are un factor din D/N/C/F/B/V/O
  6. fiecare token MOD_* referit există în CatalogModule (verificare între fișiere)
  7. corelațiile se verifică pe cifrele fluxurilor, nu declarativ
  8. după recalc: zero erori de formulă, toate celulele Check = OK
  9. conținutul original din training 4 e păstrat neatins în fișierele generate

Rulare:  python build/verifica.py
"""
import os
import re
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from date import ANALITICE, CORELATII, FLUXURI, plan as dplan  # noqa: E402
from date import module as dmod  # noqa: E402

RADACINA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SURSE = os.path.join(RADACINA, "surse", "training-4-2026-08-14")
DIST = os.path.join(RADACINA, "dist")
PLAN = os.path.join(DIST, "Plan_de_conturi_ROL_Analitice_Fluxuri_SAGA.xlsx")
MODULE = os.path.join(DIST, "Module_Declarative_Fluxuri.xlsx")

FACTORI = set("DNCFBVO")
ERORI_EXCEL = ("#REF!", "#VALUE!", "#DIV/0!", "#NAME?", "#N/A", "#NULL!", "#NUM!")

esecuri = []
note = []


def _echilibru(formula):
    """(adâncime_paranteze, șir_rămas_deschis) pentru o formulă Excel.

    Parantezele din interiorul șirurilor nu se numără, iar `""` este ghilimeaua
    scăpată din Excel, nu un sfârșit de șir.
    """
    adanc, in_sir, i = 0, False, 0
    while i < len(formula):
        ch = formula[i]
        if ch == '"':
            if in_sir and i + 1 < len(formula) and formula[i + 1] == '"':
                i += 2
                continue
            in_sir = not in_sir
        elif not in_sir:
            if ch == "(":
                adanc += 1
            elif ch == ")":
                adanc -= 1
        i += 1
    return adanc, in_sir


def cade(poarta, mesaj):
    esecuri.append(f"[{poarta}] {mesaj}")


def ok(poarta, mesaj):
    note.append(f"  ✔ {poarta}: {mesaj}")


# ---------------------------------------------------------------- porțile 1, 2, 3
def poarta_fluxuri():
    dezechilibrate = 0
    for f in FLUXURI:
        pasi_cu_sume = 0
        revelatori = 0
        for p in f["pasi"]:
            if p["revelator"]:
                revelatori += 1
            if not p["dr"] and not p["cr"]:
                continue
            pasi_cu_sume += 1
            sd = round(sum(s for _, s in p["dr"]), 2)
            sc = round(sum(s for _, s in p["cr"]), 2)
            if abs(sd - sc) > 0.005:
                cade("1", f"{f['id']} pas {p['nr']}: ΣD={sd} ≠ ΣC={sc}")
                dezechilibrate += 1
            if not p["dr"] or not p["cr"]:
                cade("1", f"{f['id']} pas {p['nr']}: are sume doar pe o parte")

        # poarta 2 — ultimul pas trebuie să fie verificare cu stare terminală
        ultim = f["pasi"][-1]
        rol = (ultim["rol"] or "").lower()
        if "stare terminală" not in rol and "stare terminala" not in rol:
            cade("2", f"{f['id']}: ultimul pas nu declară o stare terminală (rol={ultim['rol']!r})")
        if ultim["dr"] or ultim["cr"]:
            cade("2", f"{f['id']}: ultimul pas are sume — ar trebui să fie pas de verificare")

        # poarta 3 — fluxurile didactice au exact un pas revelator
        if f["didactic"].startswith("★"):
            if revelatori != 1:
                cade("3", f"{f['id']} (didactic): are {revelatori} pași revelatori, se cere exact 1")
        elif revelatori > 1:
            cade("3", f"{f['id']}: are {revelatori} pași revelatori pe un flux nedidactic")

        if not f["principiu"]:
            cade("2", f"{f['id']}: nu are „Principiul:” la finalul blocului")

    if not esecuri:
        ok("1", f"ΣD = ΣC pe toți pașii cu sume din {len(FLUXURI)} fluxuri")
        ok("2", "toate fluxurile se închid cu stare terminală și principiu")
        ok("3", "fluxurile didactice au exact un pas revelator")
    return dezechilibrate


# ------------------------------------------------------------------------ poarta 5
def poarta_factori():
    for a in ANALITICE:
        f = (a["factor"] or "").replace(" ", "")
        if not f or f == "—":
            cade("5", f"analitic {a['simbol']}: fără factor")
        elif not set(f) <= FACTORI:
            cade("5", f"analitic {a['simbol']}: factor necunoscut {a['factor']!r}")
        if not a["rupe"]:
            cade("5", f"analitic {a['simbol']}: nu spune ce se rupe dacă lipsește")
    ok("5", f"toate cele {len(ANALITICE)} analitice Tier A au factor din D/N/C/F/B/V/O")


# ------------------------------------------------------------------------ poarta 4
def poarta_acoperire(wb):
    ids = {f["id"] for f in FLUXURI}
    ws = wb["Matrice acoperire"]
    goluri = []
    referite = set()
    for r in range(1, ws.max_row + 1):
        gol = ws.cell(row=r, column=6).value
        simbol = ws.cell(row=r, column=1).value
        fluxuri = ws.cell(row=r, column=4).value
        if simbol and gol and str(gol).strip() not in ("Gol?", "NU"):
            s = str(simbol).strip()
            if s not in dplan.GOLURI_ACCEPTATE:
                goluri.append(f"{simbol} = {gol}")
        if fluxuri:
            referite |= set(re.findall(r"F-\d+", str(fluxuri)))
    if goluri:
        cade("4", "goluri nedeclarate în matrice: " + "; ".join(goluri))
    else:
        ok("4", f"fără goluri nedeclarate; {len(dplan.GOLURI_ACCEPTATE)} goluri preexistente "
                f"rămân marcate onest (salarii — vezi GOLURI_ACCEPTATE)")

    # marcajele pe care extinderea s-a angajat să le rezolve trebuie chiar rezolvate
    for s in dplan.PARTIAL_REZOLVATE:
        for r in range(1, ws.max_row + 1):
            if str(ws.cell(row=r, column=1).value or "").strip() == s:
                if str(ws.cell(row=r, column=6).value or "").strip() != "NU":
                    cade("4", f"{s}: promis rezolvat, dar marcajul nu e „NU”")
                break

    nereferite = ids - referite
    if nereferite:
        cade("4", f"fluxuri noi neapărute în matrice: {sorted(nereferite)}")
    else:
        ok("4", f"toate cele {len(ids)} fluxuri noi sunt referite în matrice")


# ------------------------------------------------------------------------ poarta 7
def poarta_corelatii():
    """Corelațiile se verifică pe cifrele fluxurilor, nu declarativ."""
    ids = {f["id"] for f in FLUXURI}
    sume = {}
    for f in FLUXURI:
        for p in f["pasi"]:
            for cont, s in p["dr"]:
                sume.setdefault((f["id"], "D", cont.split(".")[0]), 0)
                sume[(f["id"], "D", cont.split(".")[0])] += s
            for cont, s in p["cr"]:
                sume.setdefault((f["id"], "C", cont.split(".")[0]), 0)
                sume[(f["id"], "C", cont.split(".")[0])] += s

    def rulaj(flux, sens, cont):
        return round(sume.get((flux, sens, cont), 0), 2)

    # C-13 pe F-59: amortizarea descărcată nu poate depăși valoarea de intrare
    if rulaj("F-59", "D", "2812") > rulaj("F-59", "C", "212"):
        cade("7", "C-13 pe F-59: amortizarea descărcată depășește valoarea activului")

    # F-59: 212 se stinge integral (30.000 + 70.000 = 100.000)
    if rulaj("F-59", "C", "212") != 100000:
        cade("7", f"F-59: 212 nu se stinge integral (credit {rulaj('F-59', 'C', '212')})")

    # F-50: valoarea de intrare a mijlocului fix = 150.000 + 5.250 = 155.250
    val_2133 = rulaj("F-50", "D", "2133")
    if val_2133 != 155250:
        cade("7", f"F-50: valoarea de intrare 2133 = {val_2133}, se aștepta 155.250")
    # F-50: 4093 se deschide și se închide integral
    if rulaj("F-50", "D", "4093") != rulaj("F-50", "C", "4093"):
        cade("7", "F-50: avansul 4093 nu se închide integral în 167")
    # F-50: amortizarea contabilă = 155.250 / 60
    amo = rulaj("F-50", "D", "6811")
    if abs(amo - round(155250 / 60, 2)) > 0.01:
        cade("7", f"F-50: amortizarea lunară {amo} ≠ 155.250/60")

    # F-49: soldul în lei după reevaluare = sold valută × curs BNR
    # 20.000 EUR @4,97 = 99.400 iniţial; rată 5.000 @4,97 = 24.850; reevaluare +600
    sold_1621 = 99400 - rulaj("F-49", "D", "1621") + rulaj("F-49", "C", "1621")
    if abs(sold_1621 - 15000 * 5.01) > 0.01:
        cade("7", f"F-49: sold 1621 = {sold_1621}, se aștepta 15.000 × 5,0100 = 75.150")

    # F-46: repartizarea acoperă integral profitul de 2.500
    if rulaj("F-46", "D", "121") != 2500:
        cade("7", f"F-46: 121 nu se închide integral (debit {rulaj('F-46', 'D', '121')})")
    # F-46: rezerva legală = 5% din 2.500
    if rulaj("F-46", "C", "1061") != 125:
        cade("7", "F-46: rezerva legală ≠ 5% din profitul contabil brut")

    # F-47 / F-51: conturile tranzitorii se închid integral
    for flux, cont in (("F-47", "1174"), ("F-51", "1511"), ("F-52", "233"),
                       ("F-58", "231"), ("F-57", "223"), ("F-45", "456")):
        d, c = rulaj(flux, "D", cont), rulaj(flux, "C", cont)
        if d != c:
            cade("7", f"{flux}: contul {cont} nu se închide (D={d}, C={c})")

    # F-52 / F-58: capitalizarea neutralizează integral cheltuiala cu salariile
    for flux, venit in (("F-52", "721"), ("F-58", "722")):
        if rulaj(flux, "C", venit) != rulaj(flux, "D", "641"):
            cade("7", f"{flux}: {venit} nu neutralizează integral cheltuiala 641")

    if not any(e.startswith("[7]") for e in esecuri):
        ok("7", f"corelațiile se verifică pe cifrele din {len(ids)} fluxuri")


# --------------------------------------------------------------------- porțile 6, 8
def poarta_module():
    if not os.path.exists(MODULE):
        note.append("  – 6/8: Module_Declarative_Fluxuri.xlsx încă negenerat, porți sărite")
        return
    wb = openpyxl.load_workbook(MODULE)
    catalog = set()
    ws = wb["CatalogModule"]
    for r in range(1, ws.max_row + 1):
        v = ws.cell(row=r, column=2).value
        if v and str(v).startswith("MOD_"):
            catalog.add(str(v).strip())

    referite = set()
    wbp = openpyxl.load_workbook(PLAN)
    for foaie in ("Corelații de control", "Index module"):
        w = wbp[foaie]
        for row in w.iter_rows(values_only=True):
            for cell in row:
                if isinstance(cell, str):
                    referite |= set(re.findall(r"MOD_[A-Z_]+", cell))
    lipsa = referite - catalog
    if lipsa:
        cade("6", f"module referite dar absente din CatalogModule: {sorted(lipsa)}")
    else:
        ok("6", f"toate cele {len(referite)} module referite există în CatalogModule")

    # poarta 8a — formule sintactic valide (paranteze și ghilimele echilibrate).
    # Fără asta, o formulă stricată e prinsă abia de recalc, cu un traceback opac.
    stricate = 0
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith("="):
                    adanc, in_sir = _echilibru(c.value)
                    if adanc != 0 or in_sir:
                        cade("8", f"{ws.title}!{c.coordinate}: formulă dezechilibrată "
                                  f"(paranteze={adanc}, șir deschis={in_sir})")
                        stricate += 1
    if stricate == 0:
        ok("8", "toate formulele au paranteze și ghilimele echilibrate")

    # poarta 8b — valori de formulă
    wbv = openpyxl.load_workbook(MODULE, data_only=True)
    erori, checkuri, checkuri_ok = 0, 0, 0
    for ws in wbv.worksheets:
        for row in ws.iter_rows():
            for c in row:
                v = c.value
                if isinstance(v, str):
                    if v.strip() in ERORI_EXCEL:
                        cade("8", f"{ws.title}!{c.coordinate}: {v}")
                        erori += 1
                    if v.startswith("OK") or v.startswith("EROARE"):
                        checkuri += 1
                        if v.startswith("OK"):
                            checkuri_ok += 1
                        else:
                            cade("8", f"{ws.title}!{c.coordinate}: {v}")
    if erori == 0:
        ok("8", f"zero erori de formulă; {checkuri_ok}/{checkuri} celule Check = OK")


# ------------------------------------------------------------------------ poarta 9
def poarta_neatins():
    """Conținutul original din training 4 trebuie păstrat identic în fișierele generate."""
    perechi = [
        (os.path.join(SURSE, "Plan_de_conturi_ROL_Analitice_Fluxuri_SAGA.xlsx"), PLAN),
        (os.path.join(SURSE, "Module_Declarative_Fluxuri.xlsx"), MODULE),
    ]
    # Celulele pe care extinderea are voie să le schimbe, deduse din `date/`, nu hardcodate:
    #  - coloanele D/E/F ale rândurilor din matrice promise ca PARȚIAL_REZOLVATE
    #  - denumirea și observația conturilor din CORECTII
    permise = set()
    if os.path.exists(PLAN):
        wsm = openpyxl.load_workbook(PLAN)["Matrice acoperire"]
        for r in range(1, wsm.max_row + 1):
            if str(wsm.cell(row=r, column=1).value or "").strip() in dplan.PARTIAL_REZOLVATE:
                for col in ("D", "E", "F"):
                    permise.add(("Matrice acoperire", f"{col}{r}"))
        wsp = openpyxl.load_workbook(PLAN)["Plan de conturi"]
        simboluri = {c["simbol"] for c in dplan.CORECTII}
        for r in range(1, wsp.max_row + 1):
            if str(wsp.cell(row=r, column=1).value or "").strip() in simboluri:
                permise.add(("Plan de conturi", f"B{r}"))
                permise.add(("Plan de conturi", f"F{r}"))

    # coloana Status a modulelor promovate din „EXEMPLU EXTERN” în implementate
    sursa_mod = os.path.join(SURSE, "Module_Declarative_Fluxuri.xlsx")
    if os.path.exists(sursa_mod):
        wsc = openpyxl.load_workbook(sursa_mod)["CatalogModule"]
        for r in range(1, wsc.max_row + 1):
            if str(wsc.cell(row=r, column=2).value or "").strip() in dmod.STATUS_INLOCUIT:
                permise.add(("CatalogModule", f"H{r}"))

    def semnatura(ws, rand, ignora_coloane=()):
        vals = []
        for c in range(1, ws.max_column + 1):
            if c in ignora_coloane:
                continue
            v = ws.cell(row=rand, column=c).value
            vals.append(None if v is None else str(v))
        return tuple(vals)

    for sursa, iesire in perechi:
        if not os.path.exists(iesire):
            continue
        a = openpyxl.load_workbook(sursa)
        b = openpyxl.load_workbook(iesire)
        for nume in a.sheetnames:
            if nume not in b.sheetnames:
                cade("9", f"{os.path.basename(iesire)}: foaia {nume!r} a dispărut")
                continue
            wa, wbs = a[nume], b[nume]
            # actualizările în loc pe coloanele G–J din plan sunt intenționate
            ignora = tuple(range(7, 11)) if nume == "Plan de conturi" else ()

            # Rândurile originale trebuie să apară, în aceeași ordine, în fișierul
            # generat. Inserarea de rânduri noi între ele e permisă (extindere);
            # ștergerea sau rescrierea unui rând nu e.
            noi = [semnatura(wbs, r, ignora) for r in range(1, wbs.max_row + 1)]
            i = 0
            for r in range(1, wa.max_row + 1):
                orig = semnatura(wa, r, ignora)
                if all(v is None for v in orig):
                    continue
                # celulele declarate ca modificabile se neutralizează pe ambele părți
                masca = [j for j in range(len(orig))
                         if (nume, f"{chr(65 + j)}{r}") in permise]
                def aplica(t):
                    t = list(t)
                    for j in masca:
                        if j < len(t):
                            t[j] = "«permis»"
                    return tuple(t)
                tinta = aplica(orig)
                gasit = False
                while i < len(noi):
                    if aplica(noi[i][:len(orig)]) == tinta:
                        gasit = True
                        i += 1
                        break
                    i += 1
                if not gasit:
                    cade("9", f"{nume}: rândul original {r} nu se mai regăsește "
                              f"({str(orig[:3])[:70]})")
                    break
    if not any(e.startswith("[9]") for e in esecuri):
        ok("9", "conținutul original din training 4 e păstrat (rândurile originale, în ordine)")


def main():
    if not os.path.exists(PLAN):
        raise SystemExit("Rulează întâi `make build` — lipsește dist/Plan_de_conturi_...xlsx")
    poarta_fluxuri()
    poarta_factori()
    wb = openpyxl.load_workbook(PLAN)
    poarta_acoperire(wb)
    poarta_corelatii()
    poarta_module()
    poarta_neatins()

    print("\n".join(note))
    if esecuri:
        print(f"\n✘ {len(esecuri)} eșecuri:")
        for e in esecuri:
            print("   " + e)
        sys.exit(1)
    print(f"\n✔ toate porțile trecute ({len(FLUXURI)} fluxuri, {len(CORELATII)} corelații, "
          f"{len(ANALITICE)} analitice)")


if __name__ == "__main__":
    main()
