"""MOD_CAPITALURI — repartizarea rezultatului și corecția erorilor din anii anteriori.

Acoperă F-46 și F-47. Nu dublează MOD_INCHIDERE_EX: acela închide clasele 6 și 7
pe 121, acesta repartizează rezultatul obținut.

Particularitatea modulului: rezerva legală are DOUĂ plafoane care se aplică
simultan — 5% din profitul contabil brut (limita fiscală, art. 26 alin. 1 lit. a CF)
și 20% din capitalul social subscris ȘI VĂRSAT (limita juridică, art. 183 L. 31/1990).
Se ia minimul, ținând cont de rezerva deja constituită.
"""

COD = "MOD_CAPITALURI"

CATALOG = dict(
    fluxuri="F-46, F-47",
    tip="Anual (31.12 + ianuarie)",
    variabile="Sold 121, rulaj 691, capital vărsat 1012, sold 1061, pierdere reportată",
    porti="Dublu plafon rezervă legală; pierdere reportată de acoperit înainte de dividende",
    blocuri="B1 Rezervă legală; B2 Închidere 121; B3 Dividende; B4 Corecție 1174",
    activ="NU",
)


from .comun import formula_activ  # noqa: E402


def construieste(F, P):
    """F = fabrica de foi, P = dict cu referințele parametrilor globali."""
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_CAPITALURI", {"A": 46, "B": 22, "C": 58})
    d.titlu("MOD_CAPITALURI — Declarații (input)")
    d.nota("Completează doar celulele galbene cu scris albastru. Restul sunt formule sau text fix.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    an = d.kv("Exercițiu financiar (anul N)", 2026)
    data_rep = d.kv("Data notei de repartizare (31.12.N)", "2026-12-31")
    data_inc = d.kv("Data notei de închidere (ianuarie N+1)", "2027-01-05")
    d.gol()

    d.sectiune("2. Date din balanță")
    sold121 = d.kv("Sold creditor 121 (după închiderea cls. 6 și 7)", 2500)
    rulaj691 = d.kv("Rulaj 691 (cheltuiala cu impozitul pe profit)", 0)
    capital = d.kv("Capital social subscris ȘI VĂRSAT (1012)", 5000,
                   nota="Partea nevărsată din 1011 NU intră în plafon")
    rez_ex = d.kv("Sold 1061 deja constituit", 0)
    pierdere = d.kv("Pierdere contabilă reportată de acoperit (1171 sold D)", 0)
    activ_net = d.kv("Capitaluri proprii (activ net) din bilanț", 5000,
                     nota="Se ia din bilanț, nu din balanță — vezi C-20")
    d.gol()

    d.sectiune("3. Rezerva legală — dublul plafon (nu edita)")
    brut = d.kv("Profit contabil brut (121 + 691)", f"={sold121}+{rulaj691}", tip="calc")
    cota = d.kv("Limita fiscală: 5% din profitul brut", f"={brut}*{P['proc_rezerva']}", tip="calc",
                nota="art. 26 alin. (1) lit. a) Cod fiscal")
    plafon = d.kv("Limita juridică: 20% din capitalul vărsat",
                  f"={capital}*{P['plafon_rezerva']}", tip="calc",
                  nota="art. 183 Legea 31/1990")
    spatiu = d.kv("Spațiu rămas până la plafon", f"=MAX(0,{plafon}-{rez_ex})", tip="calc")
    rezerva = d.kv("Rezervă legală de constituit", f"=MIN({cota},{spatiu})", tip="calc")
    d.check("Check plafon rezervă",
            f"={rez_ex}+{rezerva}",
            f'=IF({rez_ex}+{rezerva}<={plafon}+0.001,"OK — sub plafonul de 20%",'
            f'"EROARE — depășire plafon")')
    d.gol()

    d.sectiune("4. Repartizare")
    ramas = d.kv("Profit rămas după rezerva legală", f"={sold121}-{rezerva}", tip="calc")
    divid = d.kv("Disponibil de distribuit ca dividende", f"=MAX(0,{ramas}-{pierdere})", tip="calc")
    d.check("Check pierdere reportată",
            f"={pierdere}",
            f'=IF({pierdere}>0,"ATENȚIE — acoperă întâi pierderea reportată (L. 239/2025)",'
            f'"OK — fără pierdere reportată")')
    d.check("Check activ net ≥ ½ capital social (C-20)",
            f"={activ_net}",
            f'=IF({activ_net}>={capital}/2,"OK — activ net ≥ ½ capital social",'
            f'"BLOCAJ — L. 239/2025: fără dividende și fără restituiri de împrumuturi '
            f'de la asociați până la reîntregire")')
    d.gol()

    d.sectiune("5. Corecție erori exerciții anterioare (1174)")
    baza_cor = d.kv("Bază corecție, fără TVA (0 dacă nu e cazul)", 0)
    tva_cor = d.kv("TVA aferentă corecției", 0)
    d.check("Check 1174",
            f"={baza_cor}",
            f'=IF({baza_cor}=0,"— fără corecție în această perioadă",'
            f'"1174 se închide obligatoriu în 1171 până la 31.12 (C-18) + D101 rectificativ")')
    d.gol()

    d.sectiune("6. Conturi (din planul pe rol)")
    c121 = d.kv("Cont rezultat", 121)
    c129 = d.kv("Cont repartizarea profitului", 129)
    c1061 = d.kv("Cont rezervă legală", 1061)
    c1171 = d.kv("Cont rezultat reportat (analitic pe an)", "1171.2026")
    c457 = d.kv("Cont dividende de plată", 457)
    c1174 = d.kv("Cont corecții exerciții anterioare", 1174)
    c401 = d.kv("Cont furnizor", "401.RO")
    c4426 = d.kv("Cont TVA deductibilă", 4426)
    d.gol()

    d.sectiune("7. Sufix generat")
    sufix = d.kv("Sufix", f'="— repartizare rezultat " & {an}', tip="calc")
    d.gol()
    d.kv("Modul activ în CatalogModule?",
         formula_activ(COD, "ACTIV — jurnalele se generează",
                       "INACTIV — jurnalele rămân goale"), tip="calc")

    # -------------------------------------------------------------------- Reguli
    g = F("Reguli_CAPITALURI", {"A": 10, "B": 14, "C": 14, "D": 34, "E": 26, "F": 56})
    g.titlu("MOD_CAPITALURI — Reguli (tabele fixe)")
    g.nota("Regula juridică/fiscală e dată, nu formulă. Se editează doar când se schimbă legea.")
    g.gol()
    g.sectiune("Tabel A — Secvența de repartizare")
    g.cap(["Pas", "Cont Dr", "Cont Cr", "Sumă (sursă)", "Condiție", "Temei / observație"])
    for row in [
        ("1", "129", "1061", "MIN(5% × profit brut; 20% × capital vărsat − rezerva existentă)",
         "La 31.12.N", "art. 183 L. 31/1990 + art. 26 alin. (1) lit. a) CF"),
        ("2", "121", "129", "cât rezerva constituită", "În ianuarie N+1",
         "129 are sold DEBITOR → se închide prin creditare. NU `129 = 1171`"),
        ("3", "121", "1171", "profit rămas nerepartizat", "În ianuarie N+1",
         "1171 cu analitic PE AN (C-21)"),
        ("4", "1171", "457", "dividende aprobate", "După hotărârea AGA",
         "Impozit 16% pentru distribuiri de la 01.01.2026 (L. 141/2025); "
         "cota urmează data DISTRIBUIRII, nu a plății"),
        ("5", "1174", "401", "corecție eroare semnificativă an anterior", "Dacă e cazul",
         "Nu prin 628. Obligatoriu D101 rectificativ"),
        ("6", "1171", "1174", "cât baza corecției", "După AGA",
         "1174 e tranzitoriu — nu poate rămâne cu sold (C-18)"),
    ]:
        g.rand(list(row))
    g.gol()
    g.sectiune("Tabel B — Ordinea condițiilor înainte de dividende")
    g.cap(["#", "Condiție", "Efect dacă nu e îndeplinită", "", "", "Temei"])
    for row in [
        ("1", "Rezerva legală constituită", "Nu se pot distribui dividende", "", "", "art. 183 L. 31/1990"),
        ("2", "Pierderea contabilă reportată acoperită integral", "Nu se pot distribui dividende",
         "", "", "art. 67 L. 31/1990"),
        ("3", "Activ net ≥ ½ din capitalul social subscris",
         "Blocaj dividende ȘI blocaj restituire împrumuturi de la asociați; "
         "amenzi 10.000–300.000 lei; răspundere solidară pentru obligațiile fiscale",
         "", "", "L. 239/2025 (modifică L. 31/1990)"),
    ]:
        g.rand(list(row))
    g.gol()
    g.sectiune("Tabel C — Porți de calitate")
    for t in [
        "• ΣDr = ΣCr pe fiecare bloc",
        "• După înregistrare: sold 121 = 0 și sold 129 = 0 (C-16)",
        "• Sold 1061 ≤ 20% × capital vărsat (C-17)",
        "• Sold 1174 = 0 la 31.12 (C-18)",
        "• 1171 are analitic pe an, cu sens D/C explicit (C-21)",
        "• Modulul nu creează conturi noi — folosește conturile din Declarații",
    ]:
        g.rand([t])

    # ------------------------------------------------------------------- Jurnale
    j = F("Jurnale_CAPITALURI", {"A": 8, "B": 14, "C": 14, "D": 48, "E": 14, "F": 14, "G": 48})
    j.titlu("MOD_CAPITALURI — Jurnale (generate automat)")
    j.nota("Nu se scrie nimic manual. Toate sumele și descrierile derivă din Declarații_CAPITALURI.")
    j.gol()

    D = d.ref
    j.sectiune("Bloc 1 — Constituirea rezervei legale (31.12.N)")
    j.kv("Data jurnal:", f"={D(data_rep)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b1 = j.rand([1, f"={D(c129)}", f"={D(rezerva)}",
                 f'="Repartizare profit la rezerva legală " & {D(sufix)}',
                 f"={D(c1061)}", f"={D(rezerva)}",
                 f'="Rezervă legală constituită " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 2 — Închiderea contului 121 (ianuarie N+1)")
    j.kv("Data jurnal:", f"={D(data_inc)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b2a = j.rand([1, f"={D(c121)}", f"={D(rezerva)}",
                  f'="Închidere 121 — partea repartizată " & {D(sufix)}',
                  f"={D(c129)}", f"={D(rezerva)}",
                  f'="Stingere repartizare " & {D(sufix)}'])
    b2b = j.rand([2, f"={D(c121)}", f"={D(ramas)}",
                  f'="Închidere 121 — profit reportat " & {D(sufix)}',
                  f"={D(c1171)}", f"={D(ramas)}",
                  f'="Report rezultat pe an " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 3 — Dividende (după hotărârea AGA)")
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b3 = j.rand([1, f"={D(c1171)}", f"={D(divid)}",
                 f'="Dividende aprobate AGA " & {D(sufix)}',
                 f"={D(c457)}", f"={D(divid)}",
                 f'="Dividende de plată " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 4 — Corecție eroare exercițiu anterior (1174)")
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b4a = j.rand([1, f"={D(c1174)}", f"={D(baza_cor)}",
                  f'="Corecție eroare exercițiu anterior " & {D(sufix)}',
                  f"={D(c401)}", f"={D(baza_cor)}",
                  f'="Datorie furnizor din corecție " & {D(sufix)}'])
    b4b = j.rand([2, f"={D(c4426)}", f"={D(tva_cor)}",
                  f'="TVA din corecție — se deduce în decontul curent " & {D(sufix)}',
                  f"={D(c401)}", f"={D(tva_cor)}",
                  f'="Datorie furnizor — TVA " & {D(sufix)}'])
    b4c = j.rand([3, f"={D(c1171)}", f"={D(baza_cor)}",
                  f'="Închiderea contului tranzitoriu 1174 " & {D(sufix)}',
                  f"={D(c1174)}", f"={D(baza_cor)}",
                  f'="Stingere 1174 " & {D(sufix)}'])
    j.gol()

    j.sectiune("Sumar și controale")
    toate_dr = "+".join(x["C"] for x in (b1, b2a, b2b, b3, b4a, b4b, b4c))
    toate_cr = "+".join(x["F"] for x in (b1, b2a, b2b, b3, b4a, b4b, b4c))
    tdr = j.kv("Total Dr", f"={toate_dr}", tip="calc")
    tcr = j.kv("Total Cr", f"={toate_cr}", tip="calc")
    j.check("Check Σ (structural)", f"={tdr}-{tcr}",
            f'=IF(ABS({tdr}-{tcr})<0.01,"OK — notele se închid","EROARE")')
    j.check("Check închidere 121 (C-16)",
            f"={D(sold121)}-({b2a['C']}+{b2b['C']})",
            f'=IF(ABS({D(sold121)}-({b2a["C"]}+{b2b["C"]}))<0.01,'
            f'"OK — 121 se închide integral","EROARE — 121 rămâne cu sold")')
    j.check("Check plafon rezervă (C-17)",
            f"={D(rez_ex)}+{b1['C']}",
            f'=IF({D(rez_ex)}+{b1["C"]}<={D(plafon)}+0.001,"OK — sub 20% din capitalul vărsat",'
            f'"EROARE — depășire plafon")')
    j.check("Check 1174 (C-18)",
            f"={b4a['C']}-{b4c['C']}",
            f'=IF(ABS({b4a["C"]}-{b4c["C"]})<0.01,"OK — 1174 se închide în 1171",'
            f'"EROARE — 1174 rămâne cu sold")')
    j.nota("Stare terminală așteptată: sold 121 = 0, sold 129 = 0, sold 1174 = 0, "
           "sold 1061 ≤ 20% × capital vărsat, 1171 cu analitic pe an.")

    # ---------------------------------------------------------------- NotaExport
    n = F("NotaExport_CAPITALURI", {"A": 6, "B": 34, "C": 12, "D": 14, "E": 14, "F": 14,
                                    "G": 50, "H": 30, "I": 10})
    n.titlu("MOD_CAPITALURI — Notă pentru import (1 rând = 1 înregistrare)")
    n.nota("Filtrează pe coloana Include = DA înainte de import. Echilibrul se verifică pe bloc "
           "în Jurnale, nu pe totalul listei.")
    n.gol()
    n.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document", "Include"])
    J = j.ref
    linii = [
        ("Bloc 1 — Rezervă legală", D(data_rep), b1, "Notă contabilă 31.12"),
        ("Bloc 2 — Închidere 121", D(data_inc), b2a, "Notă de închidere"),
        ("Bloc 2 — Închidere 121", D(data_inc), b2b, "Notă de închidere"),
        ("Bloc 3 — Dividende", D(data_inc), b3, "Hotărâre AGA"),
        ("Bloc 4 — Corecție 1174", D(data_inc), b4a, "Factură an anterior"),
        ("Bloc 4 — Corecție 1174", D(data_inc), b4b, "Factură an anterior"),
        ("Bloc 4 — Corecție 1174", D(data_inc), b4c, "Notă contabilă"),
    ]
    refs_suma = []
    for i, (bloc, data_ref, b, doc) in enumerate(linii, start=1):
        r = n.rand([i, bloc, f"={data_ref}", f"={J(b['B'])}", f"={J(b['E'])}",
                    f"={J(b['C'])}", f"={J(b['D'])}", doc, None])
        n.ws.cell(row=n.r - 1, column=9, value=f'=IF({r["F"]}>0,"DA","NU")')
        refs_suma.append(r["F"])
    n.gol()
    prima, ultima = refs_suma[0].replace("F", "I"), refs_suma[-1].replace("F", "I")
    n.kv("Rânduri de importat (Include=DA)", f'=COUNTIF({prima}:{ultima},"DA")', tip="calc")
    n.check("Check global (trebuie 0)", f"={J(tdr)}-{J(tcr)}",
            f'=IF(ABS({J(tdr)}-{J(tcr)})<0.01,"OK","EROARE")')
