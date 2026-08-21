"""MOD_INCHIDERE_EX — închiderea exercițiului: cls.6 → 121 ← cls.7, impozit, report 117.

Acoperă F-37.

Contul 121 are rol de **colectare rezultat**: adună clasele 6 și 7, ține rezultatul cât
timp e nevoie de el, apoi se golește prin report pe 117. Starea terminală e sold zero pe
121 — dacă rămâne ceva acolo după 31.12, reportul n-a fost făcut.

Ordinea blocurilor nu e arbitrară: impozitul se calculează pe rezultatul de DINAINTE de
impozit, apoi cheltuiala cu impozitul se închide și ea în 121, și abia soldul rămas se
reportează. Blocul 3 are deci două rânduri, nu unul — 691 nu poate rămâne deschis.

## Gol cunoscut, păstrat ca atare

Tabelul A din Reguli enumeră șase pași, printre care „B4 Repartizare (opțional) —
129 = 106/457…”. Jurnalele au patru blocuri și NU includ repartizarea: câmpul „Repartizare
la rezerve / dividende” din Declarații se scade din rezultatul reportat, dar nicio
înregistrare nu mută suma aceea nicăieri. Cu valoarea implicită 0 nu se vede; pusă pe
5.000, nota ar ieși cu 5.000 lei care dispar.

Golul vine din sămânță și e lăsat aici NESCHIMBAT, ca portarea să rămână portare. Cine
are de repartizat efectiv folosește MOD_CAPITALURI, care face exact asta (rezervă legală,
dividende, 1171) și e construit pentru ea.
"""
from .comun import formula_activ

COD = "MOD_INCHIDERE_EX"

CATALOG = dict(
    fluxuri="F-37",
    tip="Anual",
    variabile="Rulaje cls.6, Rulaje cls.7, Impozit/IMCA",
    porti="—",
    blocuri="B1 Închidere 6xx; B2 Închidere 7xx; B3 Impozit; B4 Report 117",
    ce_face="Închidere cls.6/7 pe 121; impozit; report 117",
    cand="La 31.12",
    activ="NU",
)

#: pas, bloc, cont Dr, cont Cr, sumă, observație
SECVENTA = [
    (1, "B1 Închidere cheltuieli", "121", "6xx (total)", "Rulaj D cls.6",
     "Neutralizare rezultat — cheltuieli"),
    (2, "B2 Închidere venituri", "7xx (total)", "121", "Rulaj C cls.7",
     "Neutralizare rezultat — venituri"),
    (3, "B3 Impozit", "691/697", "441/4417", "Impozit calculat",
     "Cheltuială cu impozitul → datorie"),
    (4, "B3b Închidere 691", "121", "691", "Impozit",
     "Impozitul intră în rezultatul net"),
    (5, "B4 Repartizare (opțional)", "129", "106/457…", "Sumă repartizată",
     "Doar dacă AGA / decizie există"),
    (6, "B5 Report", "121", "117", "Sold final 121",
     "Dacă profit; invers dacă pierdere"),
]

#: cont, denumire, rol, observație
CONTURI = [
    ("121", "Profit sau pierdere", "Colectare rezultat",
     "Se închide anual; fără sold după report pe 117"),
    ("129", "Repartizarea profitului", "Colectare / tranzit",
     "Se folosește doar la repartizare formală"),
    ("117", "Rezultatul reportat", "Patrimonial — Capital",
     "Sold permanent până la acoperire / repartizare"),
    ("691", "Cheltuieli cu impozitul pe profit", "Neutralizare rezultat",
     "Se închide în 121"),
    ("697", "Cheltuieli cu impozitul pe venit micro", "Neutralizare rezultat",
     "Alternativă la 691"),
    ("441", "Impozit pe profit", "Patrimonial — Datorie", "Datorie către buget"),
    ("4417", "Impozit pe venit micro / alte impozite", "Patrimonial — Datorie",
     "Conform OMF actualizat"),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_INCHIDERE_EX", {"A": 48, "B": 26, "C": 56})
    d.titlu("MOD_INCHIDERE_EX — Declarații (input)")
    d.nota("Modul anual. Completezi rulajele din balanță (sau totaluri din SAGA). "
           "Jurnalele închid cls.6 → 121, cls.7 → 121, calculează impozit / IMCA, "
           "repartizează 129 și reportează 117.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    d.kv("CUI", "=Parametri!B6", tip="calc")
    an = d.kv("An exercițiu", 2026)
    data_j = d.kv("Data jurnal închidere (31.12)", "2026-12-31")
    d.gol()

    d.sectiune("2. Rulaje de închis (din balanță / totaluri SAGA)")
    r6 = d.kv("Total rulaj debitor cls.6 (cheltuieli)", 185000)
    r7 = d.kv("Total rulaj creditor cls.7 (venituri)", 245000)
    d.gol()

    d.sectiune("3. Impozit pe profit / IMCA")
    d.kv("Regim (PROFIT / MICRO / IMCA)", "PROFIT")
    baza = d.kv("Baza impozabilă (sau cifră afaceri IMCA)", 60000)
    cota = d.kv("Cotă (0.16 / 0.01 / 0.03 etc.)", 0.16)
    impozit = d.kv("Impozit calculat", f"={baza}*{cota}", tip="calc")
    c_chelt = d.kv("Cont cheltuială impozit (691 / 697 / 4417)", "691")
    c_datorie = d.kv("Cont datorie impozit (441 / 4417)", "441")
    d.gol()

    d.sectiune("4. Repartizare rezultat")
    brut = d.kv("Rezultat înainte de impozit (7−6)", f"={r7}-{r6}", tip="calc")
    net = d.kv("Rezultat net (după impozit)", f"={brut}-{impozit}", tip="calc")
    repartizat = d.kv("Repartizare la rezerve / dividende etc. (opțional)", 0)
    reportat = d.kv("Reportat pe 117 (sold final 121/129)", f"={net}-{repartizat}",
                    tip="calc")
    d.gol()

    d.sectiune("5. Politică conturi rezultat")
    c_121 = d.kv("Cont profit și pierdere", "121")
    d.kv("Cont repartizare profit", "129")
    c_117 = d.kv("Cont rezultat reportat", "117")
    d.gol()

    d.sectiune("6. Sufix")
    sufix = d.kv("Sufix", f'="— închidere exercițiu " & {an}', tip="calc")
    d.gol()

    d.sectiune("7. Control")
    d.kv("Modul activ?", formula_activ(COD), tip="calc")
    d.kv("Notă",
         "În practică se închid conturile de cheltuieli/venituri pe analitice (sau pe "
         "grupe). Aici se lucrează pe totaluri — un singur rând pe clasă.", tip="calc")

    # ------------------------------------------------------------------- Reguli
    g = F("Reguli_INCHIDERE_EX",
          {"A": 8, "B": 30, "C": 16, "D": 18, "E": 20, "F": 48})
    g.titlu("MOD_INCHIDERE_EX — Reguli (tabele fixe)")
    g.nota("Secvența de închidere e standard OMFP 1802. Detalierea pe conturi analitice "
           "se face în SAGA; modulul lucrează pe totaluri de clasă pentru generarea "
           "notei de principiu.")
    g.gol()

    g.sectiune("Tabel A — Secvența de închidere")
    g.cap(["Pas", "Bloc", "Cont Dr", "Cont Cr", "Sumă", "Observație"])
    for rand in SECVENTA:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel B — Conturi din plan pe rol")
    g.cap(["Cont", "Denumire", "Rol", "Observație"])
    for rand in CONTURI:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel C — Porți de calitate")
    for linie in [
        "• ΣDr = ΣCr pe fiecare bloc",
        "• După B1+B2: sold 6xx = 0, sold 7xx = 0",
        "• Sold 121 înainte de report = rezultat net",
        "• După B5: sold 121 = 0, sold 117 reflectă reportul",
        "• Modulul nu înlocuiește D101 / declarația de impozit — produce doar nota "
        "contabilă",
    ]:
        g.nota(linie)

    # ------------------------------------------------------------------ Jurnale
    j = F("Jurnale_INCHIDERE_EX",
          {"A": 24, "B": 16, "C": 14, "D": 50, "E": 16, "F": 14, "G": 50})
    j.titlu("MOD_INCHIDERE_EX — Jurnale (generate automat)")
    j.nota("Toate sumele derivă din Declarații. În SAGA se detaliază pe conturi "
           "analitice; aici e nota de principiu pe totaluri de clasă.")
    j.gol()

    D = d.ref
    j.kv("Data jurnal:", f"={D(data_j)}", tip="calc")
    j.gol()

    antet = ["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr",
             "Descriere Cr"]

    j.sectiune("Bloc 1 — Închidere cheltuieli (cls.6 → 121)")
    j.cap(antet)
    b1 = j.rand([1, f"={D(c_121)}", f"={D(r6)}",
                 f'="Închidere cheltuieli cls.6 " & {D(sufix)}',
                 "6xx", f"={D(r6)}",
                 f'="Stingere rulaj cheltuieli " & {D(sufix)}'])
    c1 = j.check("Check B1", f"={b1['C']}-{b1['F']}",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Bloc 2 — Închidere venituri (cls.7 → 121)")
    j.cap(antet)
    b2 = j.rand([1, "7xx", f"={D(r7)}",
                 f'="Închidere venituri cls.7 " & {D(sufix)}',
                 f"={D(c_121)}", f"={D(r7)}",
                 f'="Stingere rulaj venituri " & {D(sufix)}'])
    c2 = j.check("Check B2", f"={b2['C']}-{b2['F']}",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    # Două rânduri, nu unul: cheltuiala cu impozitul se naște ȘI se închide în 121.
    # Lăsată doar cu primul rând, 691 ar rămâne cu sold la 31.12.
    j.sectiune("Bloc 3 — Cheltuială cu impozitul + închiderea ei în 121")
    j.cap(antet)
    b3a = j.rand([1, f"={D(c_chelt)}", f"={D(impozit)}",
                  f'="Cheltuială impozit " & {D(sufix)}',
                  f"={D(c_datorie)}", f"={D(impozit)}",
                  f'="Datorie impozit buget " & {D(sufix)}'])
    b3b = j.rand([2, f"={D(c_121)}", f"={D(impozit)}",
                  f'="Închidere cheltuială impozit în rezultat " & {D(sufix)}',
                  f"={D(c_chelt)}", f"={D(impozit)}",
                  f'="Stingere 691 " & {D(sufix)}'])
    c3 = j.check("Check B3",
                 f"=({b3a['C']}+{b3b['C']})-({b3a['F']}+{b3b['F']})",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    # Sensul se inversează la pierdere: 117 se debitează, 121 se creditează.
    profit = f"{D(reportat)}>=0"
    j.sectiune("Bloc 4 — Report rezultat net pe 117")
    j.cap(antet)
    b4 = j.rand([1,
                 f"=IF({profit},{D(c_121)},{D(c_117)})",
                 f"=ABS({D(reportat)})",
                 f'=IF({profit},"Report profit pe 117 ","Report pierdere pe 117 ")'
                 f" & {D(sufix)}",
                 f"=IF({profit},{D(c_117)},{D(c_121)})",
                 f"=ABS({D(reportat)})",
                 f'=IF({profit},"Rezultat reportat (profit) ",'
                 f'"Rezultat reportat (pierdere) ") & {D(sufix)}'])
    c4 = j.check("Check B4", f"={b4['C']}-{b4['F']}",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Stare terminală așteptată")
    j.nota("Sold 6xx=0 | Sold 7xx=0 | Sold 121=0 | Sold 691=0 | 441 = impozit datorat | "
           "117 = rezultat net reportat")
    j.gol()
    glob = j.check("Check global",
                   f"=ABS({c1})+ABS({c2})+ABS({c3})+ABS({c4})",
                   f'=IF(B{j.r}<0.01,"OK — toate blocurile se închid",'
                   f'"EROARE — cel puțin un bloc dezechilibrat")')

    # --------------------------------------------------------------- NotaExport
    e = F("NotaExport_INCHIDERE_EX",
          {"A": 6, "B": 18, "C": 14, "D": 12, "E": 12, "F": 14, "G": 50, "H": 22,
           "I": 10})
    e.titlu("MOD_INCHIDERE_EX — Notă pentru import")
    e.nota("Filtrează Include=DA. În SAGA se detaliază 6xx/7xx pe conturi individuale; "
           "aceste rânduri sunt nota de principiu.")
    e.gol()
    e.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    primul = e.r
    for i, (bloc, r) in enumerate([
        ("B1 Cheltuieli", b1), ("B2 Venituri", b2), ("B3 Impozit", b3a),
        ("B3 Înch.691", b3b), ("B4 Report 117", b4),
    ], start=1):
        e.rand([i, bloc, f"={D(data_j)}", f"={j.ref(r['B'])}", f"={j.ref(r['E'])}",
                f"={j.ref(r['C'])}", f"={j.ref(r['D'])}", "Închidere exercițiu",
                f'=IF(F{e.r}>0,"DA","NU")'])
    ultim = e.r - 1
    e.gol()
    e.kv("Rânduri de importat", f'=COUNTIF(I{primul}:I{ultim},"DA")', tip="calc")
    e.check("Check global", f"={j.ref(glob)}",
            f'=IF(ABS(B{e.r})<0.01,"OK","EROARE")')
