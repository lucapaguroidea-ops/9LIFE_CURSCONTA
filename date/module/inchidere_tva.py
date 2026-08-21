"""MOD_INCHIDERE_TVA — închiderea lunară 4426 / 4427 → 4423 / 4424.

Acoperă F-21.

Rolul lui 4426 și 4427 e de TRANZIT: adună rulajul lunii și se golesc la închidere.
Un sold rămas pe ele după notă nu e o nuanță, e o eroare — de-asta starea terminală e
scrisă explicit, iar jurnalul o verifică prin trei celule `Check` distincte.

Cele trei verificări nu sunt redundante, și merită spus de ce:

- **Check Σ (structural)** — ΣDr = ΣCr pe notă. Trece și dacă sumele sunt greșite, cât
  timp sunt greșite simetric. Singur, nu dovedește nimic despre corectitudine.
- **Check net (REAL)** — netul repartizat pe 4423/4424 e chiar |4427 − 4426|. Asta prinde
  cazul în care nota se echilibrează frumos pe cifre care nu vin din balanță.
- **Check exclusivitate** — nu pot fi ambele conturi cu sold. TVA e ori de plată, ori de
  recuperat, niciodată amândouă în aceeași lună.

Modulul era una din cele șapte foi rămase din sămânța de 14.08.2026.
"""
from .comun import formula_activ

COD = "MOD_INCHIDERE_TVA"

CATALOG = dict(
    fluxuri="F-21",
    tip="Lunar (fără linii)",
    variabile="Rulaj 4426, Rulaj 4427, Luna",
    porti="—",
    blocuri="B1 Închidere 4426/4427 → 4423/4424",
    ce_face="Închidere 4426/4427 → 4423/4424",
    cand="La fiecare lună, după rulaje TVA",
    activ="DA",
)

#: pas, cont Dr, cont Cr, sumă (sursă), condiție, temei / observație
SECVENTA = [
    (1, "4427", "4426", "MIN(rulaj 4426, rulaj 4427)", "Întotdeauna",
     "Stingere reciprocă a rulajelor — fără sold intermediar"),
    (2, "4427", "4423", "MAX(0, 4427−4426)", "Dacă 4427 > 4426",
     "Sold net = TVA de plată către buget"),
    (3, "4424", "4426", "MAX(0, 4426−4427)", "Dacă 4426 > 4427",
     "Sold net = TVA de recuperat / de rambursat"),
]

#: cont, denumire, rol, observație din Plan de conturi
CONTURI = [
    ("4426", "TVA deductibilă", "Tranzit / reflectare",
     "Jurnal cumpărări; se închide lunar; fără sold"),
    ("4427", "TVA colectată", "Tranzit / reflectare",
     "Jurnal vânzări; se închide lunar; fără sold"),
    ("4423", "TVA de plată", "Patrimonial — Datorie",
     "Sold datorie lunară către buget"),
    ("4424", "TVA de recuperat", "Patrimonial — Creanță",
     "Sold creanță / de rambursat"),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_INCHIDERE_TVA", {"A": 48, "B": 30, "C": 54})
    d.titlu("MOD_INCHIDERE_TVA — Declarații (input)")
    d.nota("Completează doar celulele galbene cu scris albastru. Restul sunt formule "
           "sau text fix.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    d.kv("CUI", "=Parametri!B6", tip="calc")
    luna = d.kv("Luna (AAAA-LL)", "2026-07")
    data_j = d.kv("Data jurnal (ultima zi a lunii)", "2026-07-31")
    d.gol()

    d.sectiune("2. Rulaje TVA din jurnale (introducere manuală din balanță / "
               "jurnale SAGA)")
    rd = d.kv("Rulaj debitor 4426 (TVA deductibilă)", 10500)
    rc = d.kv("Rulaj creditor 4427 (TVA colectată)", 15750)
    d.gol()

    d.sectiune("3. Politică de conturi (din planul pe rol)")
    c_ded = d.kv("Cont TVA deductibilă", "4426")
    c_col = d.kv("Cont TVA colectată", "4427")
    c_plata = d.kv("Cont TVA de plată", "4423")
    c_recup = d.kv("Cont TVA de recuperat", "4424")
    d.gol()

    d.sectiune("4. Calcul automat (nu edita)")
    net = d.kv("Sold net (4427 − 4426)", f"={rc}-{rd}", tip="calc")
    d.kv("Direcție",
         f'=IF({net}>0,"TVA de plată (4423)","TVA de recuperat (4424)")', tip="calc")
    s_plata = d.kv("Sumă pe 4423", f"=IF({net}>0,{net},0)", tip="calc")
    s_recup = d.kv("Sumă pe 4424", f"=IF({net}<0,-{net},0)", tip="calc")
    d.gol()

    d.sectiune("5. Sufix descriere (generat)")
    sufix = d.kv("Sufix", f'="— închidere TVA " & {luna}', tip="calc")
    d.gol()

    d.sectiune("6. Control")
    d.kv("Check: 4426 și 4427 trebuie să aibă sold 0 după notă",
         "OK dacă nota e înregistrată integral", tip="calc")
    d.kv("Modul activ în CatalogModule?",
         formula_activ(COD, "ACTIV — jurnalele se generează",
                       "INACTIV — jurnalele rămân goale"), tip="calc")

    # ------------------------------------------------------------------- Reguli
    g = F("Reguli_INCHIDERE_TVA",
          {"A": 8, "B": 22, "C": 22, "D": 28, "E": 22, "F": 52})
    g.titlu("MOD_INCHIDERE_TVA — Reguli (tabele fixe)")
    g.nota("Regula fiscală/contabilă este dată, nu formulă. Se editează doar când se "
           "schimbă legea sau politica firmei.")
    g.gol()

    g.sectiune("Tabel A — Secvența de închidere")
    g.cap(["Pas", "Cont Dr", "Cont Cr", "Sumă (sursă)", "Condiție",
           "Temei / observație"])
    for rand in SECVENTA:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel B — Conturi din planul pe rol (referință)")
    g.cap(["Cont", "Denumire", "Rol", "Observație din Plan de conturi"])
    for rand in CONTURI:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel C — Porți de calitate")
    for linie in [
        "• ΣDr = ΣCr pe notă",
        "• După înregistrare: sold 4426 = 0 și sold 4427 = 0",
        "• Sold 4423 sau 4424 = |4427 − 4426|",
        "• Descrierile conțin sufixul generat (luna)",
        "• Modulul nu creează analitice noi — folosește conturile din Declarații",
    ]:
        g.nota(linie)

    # ------------------------------------------------------------------ Jurnale
    j = F("Jurnale_INCHIDERE_TVA",
          {"A": 30, "B": 16, "C": 14, "D": 46, "E": 16, "F": 14, "G": 46})
    j.titlu("MOD_INCHIDERE_TVA — Jurnale (generate automat)")
    j.nota("Nu se scrie nimic manual. Toate sumele și descrierile derivă din "
           "Declarații_INCHIDERE_TVA.")
    j.gol()

    D = d.ref
    minim = f"=MIN({D(rd)},{D(rc)})"

    j.sectiune("Bloc 1 — Închiderea lunară 4426 / 4427")
    j.kv("Data jurnal:", f"={D(data_j)}", tip="calc")
    j.gol()
    j.sectiune("Înregistrări")
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr",
           "Descriere Cr"])
    r1 = j.rand([1, f"={D(c_col)}", minim,
                 f'="Stingere TVA colectată " & {D(sufix)}',
                 f"={D(c_ded)}", minim,
                 f'="Stingere TVA deductibilă " & {D(sufix)}'])
    r2 = j.rand([2, f"={D(c_col)}", f"={D(s_plata)}",
                 f'="TVA de plată (sold net) " & {D(sufix)}',
                 f"={D(c_plata)}", f"={D(s_plata)}",
                 f'="Datorie TVA buget " & {D(sufix)}'])
    r3 = j.rand([3, f"={D(c_recup)}", f"={D(s_recup)}",
                 f'="TVA de recuperat (sold net) " & {D(sufix)}',
                 f"={D(c_ded)}", f"={D(s_recup)}",
                 f'="Stingere rest TVA deductibilă " & {D(sufix)}'])
    j.gol()

    j.sectiune("Sumar")
    t_dr = j.kv("Total Dr", f"={r1['C']}+{r2['C']}+{r3['C']}", tip="calc")
    t_cr = j.kv("Total Cr", f"={r1['F']}+{r2['F']}+{r3['F']}", tip="calc")

    # Cele trei verificări prind lucruri diferite; vezi docstringul modulului.
    structural = j.check("Check Σ (structural)", f"={t_dr}-{t_cr}",
                         f'=IF(ABS(B{j.r})<0.01,"OK — notă se închide","EROARE")')
    j.check("Check net (REAL)",
            f"=ABS({D(rc)}-{D(rd)})-({r2['C']}+{r3['C']})",
            f'=IF(ABS(B{j.r})<0.01,"OK — net repartizat pe 4423/4424",'
            f'"EROARE — net ≠ |4427−4426|")')
    j.check("Check exclusivitate 4423/4424",
            f"=IF(AND({r2['C']}>0.01,{r3['C']}>0.01),1,0)",
            f'=IF(B{j.r}=0,"OK — un singur cont de sold",'
            f'"EROARE — 4423 și 4424 ambele >0")')
    j.nota("Stare terminală așteptată: sold 4426=0, sold 4427=0, sold 4423 sau "
           "4424 = |4427−4426|")

    # --------------------------------------------------------------- NotaExport
    e = F("NotaExport_INCHIDERE_TVA",
          {"A": 6, "B": 26, "C": 14, "D": 12, "E": 12, "F": 14, "G": 46, "H": 26,
           "I": 10})
    e.titlu("MOD_INCHIDERE_TVA — Notă pentru import (1 rând = 1 înregistrare)")
    e.nota("Filtrează pe coloana Include = DA înainte de import în SAGA / alt program. "
           "Echilibrul se verifică pe bloc în Jurnale, nu pe totalul listei.")
    e.gol()
    e.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    primul = e.r
    for i, r in enumerate([r1, r2, r3], start=1):
        e.rand([i, "Bloc 1 — Închidere TVA", f"={D(data_j)}",
                f"={j.ref(r['B'])}", f"={j.ref(r['E'])}", f"={j.ref(r['C'])}",
                f"={j.ref(r['D'])}", "Închidere lunară TVA",
                f'=IF(F{e.r}>0,"DA","NU")'])
    ultim = e.r - 1
    e.gol()
    e.kv("Rânduri de importat (Include=DA)", f'=COUNTIF(I{primul}:I{ultim},"DA")',
         tip="calc")
    e.check("Check global (trebuie 0)", f"={j.ref(structural)}",
            f'=IF(ABS(B{e.r})<0.01,"OK","EROARE")')
