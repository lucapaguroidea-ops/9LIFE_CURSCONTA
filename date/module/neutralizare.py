"""MOD_NEUTRALIZARE — 711 / 712 / 722: costul intră în cls.6, venitul îl neutralizează.

Acoperă F-05 (bunuri), F-07 (servicii), F-28 (imobilizări în regie proprie).

Conturile 711, 712 și 722 au rol de **neutralizare rezultat**: țin 121 la zero cât timp
bunul nu e livrat sau finalizat. Costurile lovesc clasa 6 în luna în care se fac; dacă
n-ar exista contrapartida de venit din producție, firma ar raporta pierdere în luna
producției și profit în luna vânzării, deși economic nu s-a întâmplat nimic în plus.

Cele trei tipuri sunt același principiu cu trei destinații:

| Tip | Stoc intermediar | Venit neut. | Stoc final |
|---|---|---|---|
| BUNURI | 331 | 711 | 345 |
| SERVICII | 332 | 712 | — (se stinge la livrare) |
| MF | 231 | 722 | 213 |

## Cele patru erori pe care le apără Tabelul C

Sunt scrise acolo pentru că fiecare a fost făcută în notițe și corectată:

- **345 creditat de două ori** fără un debit de obținere. La bunuri, 711 se debitează la
  reluarea producției neterminate ȘI se creditează la obținerea produsului finit — două
  mișcări, nu una.
- **722 = 231**, care ar stinge activul. Corect e invers: `231 = 722`.
- **607 la descărcarea produselor finite.** 607 e cont de mărfuri. Produsul finit se
  descarcă prin `711 = 345`.
- **„711 sau 712” la servicii.** Pentru servicii e strict 712.

## Observație lăsată neschimbată

Formula de pe contul de credit al blocului 3 e `IF(Tip="MF", stoc_interm, stoc_interm)` —
ambele ramuri identice, deci condiția nu decide nimic. E din sămânță, nu schimbă nicio
valoare, și rămâne ca atare: portarea reproduce, nu rescrie.

Modulul era una din cele șapte foi rămase din sămânța de 14.08.2026.
"""

from .comun import sectiune_temei

COD = "MOD_NEUTRALIZARE"

CATALOG = dict(
    fluxuri="F-05, F-07, F-28",
    tip="Pe stadiu producție",
    variabile="Cost acumulat, Cont stoc (331/332/231), Cont venit (711/712/722)",
    porti="—",
    blocuri="B1 Costuri→stoc; B2 Neutralizare; B3 Finalizare/livrare",
    ce_face="711/712/722: lanț complet producție / servicii / MF",
    cand="La producție / servicii în curs",
    activ="NU",
)

#: tip, cost →, stoc intermediar, venit neut., stoc final / livrare, descărcare
LANT = [
    ("BUNURI", "601=301", "331=711", "711=331 apoi 345=711", "345", "711=345 (NU 607)"),
    ("SERVICII", "641/601=…", "332=712", "712=332", "(nu e stoc final)",
     "712 stins la livrare"),
    ("MF", "601=301, 641=421", "231=722", "—", "213=231", "(nu e vânzare — e activ)"),
]


#: (ce se sprijină pe el, temei) — secțiunea finală din `Reguli`.
TEMEI_LEGAL = [
    ('Producția de imobilizări în regie proprie se evidențiază prin 722',
     'OMFP 1802/2014 — funcțiunea contului 722'),
    ('Variația stocurilor de produse și producție în curs, prin 711',
     'OMFP 1802/2014 — funcțiunea contului 711'),
    ('Costul de producție cuprinde materiile, manopera și cota de cheltuieli indirecte',
     'OMFP 1802/2014, pct. 9'),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_NEUTRALIZARE", {"A": 40, "B": 42, "C": 52})
    d.titlu("MOD_NEUTRALIZARE — Declarații (input)")
    d.nota("Acoperă F-05 (bunuri/711), F-07 (servicii/712), F-28 (imobilizări/722). "
           "Alege tipul — conturile și lanțul se adaptează. Principiu: costurile lovesc "
           "cls.6, apoi contul de venit de producție capitalizează și neutralizează.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    d.kv("CUI", "=Parametri!B6", tip="calc")
    proiect = d.kv("Luna / proiect", "2026-07")
    data_c = d.kv("Data costuri (B1)", "2026-07-05")
    data_f = d.kv("Data finalizare stoc (B2-B3)", "2026-07-20")
    data_v = d.kv("Data vânzare / recepție MF (B4)", "2026-07-25")
    d.gol()

    d.sectiune("2. Tip producție (poartă principală)")
    tip = d.kv("Tip (BUNURI / SERVICII / MF)", "BUNURI")
    c_venit_n = d.kv("Cont venit neutralizare (auto)",
                     f'=IF({tip}="BUNURI",711,IF({tip}="SERVICII",712,'
                     f'IF({tip}="MF",722,"?")))', tip="calc")
    c_interm = d.kv("Cont stoc intermediar (auto)",
                    f'=IF({tip}="BUNURI",331,IF({tip}="SERVICII",332,'
                    f'IF({tip}="MF",231,"?")))', tip="calc")
    c_final = d.kv("Cont stoc final (auto)",
                   f'=IF({tip}="BUNURI",345,IF({tip}="SERVICII",'
                   f'"(nu e cazul — se stinge la livrare)",IF({tip}="MF",213,"?")))',
                   tip="calc")
    c_venit_v = d.kv("Cont venit vânzare (auto)",
                     f'=IF({tip}="BUNURI",701,IF({tip}="SERVICII",704,'
                     f'IF({tip}="MF","(nu e vânzare — e activ)","?")))', tip="calc")
    d.gol()

    d.sectiune("3. Costuri (cls.6)")
    cost_mat = d.kv("Cost materiale (→ 601)", 4500)
    cost_man = d.kv("Cost manoperă (→ 641)", 0)
    cost_alte = d.kv("Alte costuri (→ 6xx)", 0)
    cost_tot = d.kv("Cost total", f"={cost_mat}+{cost_man}+{cost_alte}", tip="calc")
    d.gol()

    d.sectiune("4. Vânzare (doar BUNURI / SERVICII)")
    pret = d.kv("Preț vânzare (fără TVA)", 7000)
    cota = d.kv("Cota TVA", 0.21)
    tva = d.kv("TVA",
               f'=IF(OR({tip}="BUNURI",{tip}="SERVICII"),{pret}*{cota},0)', tip="calc")
    total = d.kv("Total factură", f"={pret}+{tva}", tip="calc")
    d.gol()

    d.sectiune("5. Conturi suplimentare")
    c_materii = d.kv("Cont materii prime", "301")
    c_client = d.kv("Cont client", "411.RO")
    c_4427 = d.kv("Cont TVA colectată", "4427")
    d.gol()

    d.sectiune("6. Sufix")
    sufix = d.kv("Sufix", f'="— " & {proiect} & " — " & {tip} & " — " & {c_venit_n}',
                 tip="calc")
    d.gol()

    d.sectiune("7. Control")
    d.kv("Marjă (vânzare − cost)",
         f'=IF(OR({tip}="BUNURI",{tip}="SERVICII"),{pret}-{cost_tot},"n/a (MF)")',
         tip="calc")
    d.kv("Notă principiu",
         "Costurile lovesc cls.6; contul de venit de producție (711/712/722) "
         "capitalizează și neutralizează. Descărcarea la vânzare (bunuri) e prin "
         "711=345, nu prin 607.", tip="calc")

    # ------------------------------------------------------------------- Reguli
    g = F("Reguli_NEUTRALIZARE",
          {"A": 12, "B": 20, "C": 20, "D": 26, "E": 30, "F": 26})
    g.titlu("MOD_NEUTRALIZARE — Reguli (tabele fixe)")
    g.nota("Principiul comun F-05 / F-07 / F-28: cost → cls.6 → stoc intermediar = venit "
           "neutralizare → stoc final / livrare. 711/712/722 nu se stinge greșit în "
           "stocul final fără pasul de obținere.")
    g.gol()

    g.sectiune("Tabel A — Lanț pe tip")
    g.cap(["Tip", "Cost →", "Stoc intermediar", "Venit neut.", "Stoc final / livrare",
           "Descărcare la vânzare"])
    for rand in LANT:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel B — Porți de calitate")
    for linie in [
        "• ΣD=ΣC pe fiecare bloc",
        "• Cont venit neutralizare: rulaj D = rulaj C la final (sold 0)",
        "• Stoc intermediar sold 0 după finalizare",
        "• Pentru BUNURI: 345 un singur D și un singur C; descărcare prin 711, nu 607",
        "• Pentru MF: impact net pe 121 din capitalizare = 0 (cheltuieli = 722)",
    ]:
        g.nota(linie)
    g.gol()

    g.sectiune("Tabel C — Ce NU se face")
    for linie in [
        "• 345 creditat de două ori fără un debit de obținere (eroarea F-05 veche)",
        "• 722 = 231 (ar stinge activul — eroare F-28 veche); corect e 231 = 722",
        "• 607 la descărcarea produselor finite (607 e doar mărfuri)",
        "• „711 sau 712” la servicii — pentru servicii e strict 712",
    ]:
        g.nota(linie)

    sectiune_temei(g, TEMEI_LEGAL)

    # ------------------------------------------------------------------ Jurnale
    j = F("Jurnale_NEUTRALIZARE",
          {"A": 14, "B": 20, "C": 14, "D": 52, "E": 20, "F": 14, "G": 52})
    j.titlu("MOD_NEUTRALIZARE — Jurnale (generate automat)")
    j.nota("Lanțul se adaptează după Tip. Pentru MF, blocul de vânzare rămâne 0. Pentru "
           "SERVICII, stocul final e gol.")
    j.gol()

    D = d.ref
    T = D(tip)
    #: Cele două condiții care comandă tot lanțul. Scrise o dată, folosite peste tot.
    bunuri = f'{T}="BUNURI"'
    vandabil = f'OR({T}="BUNURI",{T}="SERVICII")'

    def daca_bunuri(a, altfel=0):
        return f"=IF({bunuri},{a},{altfel})"

    def daca_vandabil(a, altfel=0):
        return f"=IF({vandabil},{a},{altfel})"

    antet = ["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr",
             "Descriere Cr"]

    j.sectiune("Bloc 1 — Costuri pe cls.6")
    j.kv("Data:", f"={D(data_c)}", tip="calc")
    j.cap(antet)
    b1a = j.rand([1, "601", f"={D(cost_mat)}",
                  f'="Consum materiale " & {D(sufix)}',
                  f"={D(c_materii)}", f"={D(cost_mat)}",
                  f'="Stingere stoc materii " & {D(sufix)}'])
    b1b = j.rand([2, "641", f"={D(cost_man)}",
                  f'="Manoperă pe proiect " & {D(sufix)}',
                  "421", f"={D(cost_man)}",
                  f'="Datorie salarii " & {D(sufix)}'])
    c1 = j.check("Check B1",
                 f"=({b1a['C']}+{b1b['C']})-({b1a['F']}+{b1b['F']})",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Bloc 2 — Stoc intermediar = venit neutralizare (pas revelator)")
    j.kv("Data:", f"={D(data_f)}", tip="calc")
    j.cap(antet)
    b2 = j.rand([1, f"={D(c_interm)}", f"={D(cost_tot)}",
                 f'="Stoc intermediar (PN/servicii/MF în curs) " & {D(sufix)}',
                 f"={D(c_venit_n)}", f"={D(cost_tot)}",
                 f'="Venit producție / neutralizare " & {D(sufix)}'])
    c2 = j.check("Check B2", f"={b2['C']}-{b2['F']}",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Bloc 3 — Finalizare (obținere stoc final / stingere intermediar)")
    j.kv("Data:", f"={D(data_f)}", tip="calc")
    j.cap(antet)
    b3a = j.rand([
        1,
        f'=IF({bunuri},{D(c_venit_n)},IF({T}="SERVICII",{D(c_venit_n)},{D(c_final)}))',
        f"={D(cost_tot)}",
        f'=IF({bunuri},"Reluare PN (711 debitat #1) ",IF({T}="SERVICII",'
        f'"Stingere servicii în curs ","Transfer MF final ")) & {D(sufix)}',
        # Ambele ramuri sunt contul de stoc intermediar — condiția nu decide nimic.
        # Din sămânță; reprodusă ca atare, vezi docstringul modulului.
        f'=IF({T}="MF",{D(c_interm)},{D(c_interm)})',
        f"={D(cost_tot)}",
        f'="Stingere stoc intermediar " & {D(sufix)}'])
    b3b = j.rand([
        2,
        daca_bunuri(D(c_final)),
        daca_bunuri(D(cost_tot)),
        f'=IF({bunuri},"Obținere produs finit (345=711) " & {D(sufix)},"")',
        daca_bunuri(D(c_venit_n)),
        daca_bunuri(D(cost_tot)),
        f'=IF({bunuri},"Neutralizare (711 creditat #2) " & {D(sufix)},"")'])
    c3 = j.check("Check B3",
                 f"=({b3a['C']}+{b3b['C']})-({b3a['F']}+{b3b['F']})",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Bloc 4 — Vânzare + descărcare (BUNURI/SERVICII; 0 pentru MF)")
    j.kv("Data:", f"={D(data_v)}", tip="calc")
    j.cap(antet)
    b4a = j.rand([1, daca_vandabil(D(c_client)), daca_vandabil(D(total)),
                  f'="Creanță client " & {D(sufix)}',
                  daca_vandabil(D(c_venit_v)), daca_vandabil(D(pret)),
                  f'="Venit din vânzare " & {D(sufix)}'])
    b4b = j.rand([2, 0, 0, None,
                  daca_vandabil(D(c_4427)), daca_vandabil(D(tva)),
                  f'="TVA colectată " & {D(sufix)}'])
    b4c = j.rand([
        3,
        f'=IF({bunuri},{D(c_venit_n)},IF({T}="SERVICII",{D(c_venit_n)},0))',
        daca_vandabil(D(cost_tot)),
        f'=IF({bunuri},"Descărcare PF prin 711 (NU 607) ",IF({T}="SERVICII",'
        f'"Stingere 712 la livrare ","")) & {D(sufix)}',
        daca_bunuri(D(c_final)),
        daca_bunuri(D(cost_tot)),
        f'=IF({bunuri},"Stingere stoc PF " & {D(sufix)},"")'])
    c4 = j.check("Check B4",
                 f"=({b4a['C']}+{b4b['C']}+{b4c['C']})-"
                 f"({b4a['F']}+{b4b['F']}+{b4c['F']})",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    glob = j.check("Check global",
                   f"=ABS({c1})+ABS({c2})+ABS({c3})+ABS({c4})",
                   f'=IF(B{j.r}<0.01,"OK — toate blocurile se închid",'
                   f'"EROARE — cel puțin un bloc dezechilibrat")')
    j.gol()
    j.sectiune("Stare terminală")
    j.nota("Cont venit neut. sold 0 | Stoc intermediar 0 | Pentru BUNURI: 345 sold 0, "
           "descărcare prin 711 | Pentru MF: 213=cost, impact 121 din capitalizare = 0")

    # --------------------------------------------------------------- NotaExport
    e = F("NotaExport_NEUTRALIZARE",
          {"A": 6, "B": 18, "C": 14, "D": 16, "E": 16, "F": 14, "G": 52, "H": 24,
           "I": 10})
    e.titlu("MOD_NEUTRALIZARE — Notă pentru import")
    e.nota("Filtrează Include=DA. Rândurile cu sumă 0 (ex. manoperă 0, sau blocuri MF "
           "fără vânzare) apar ca NU.")
    e.gol()
    e.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    primul = e.r
    # (bloc, data, cont Dr, cont Cr, sumă, descriere)
    linii = [
        ("B1 Costuri", data_c, b1a["B"], b1a["E"], b1a["C"], b1a["D"]),
        ("B1 Costuri", data_c, b1b["B"], b1b["E"], b1b["C"], b1b["D"]),
        ("B2 Neutralizare", data_f, b2["B"], b2["E"], b2["C"], b2["D"]),
        ("B3 Finalizare", data_f, b3a["B"], b3a["E"], b3a["C"], b3a["D"]),
        ("B3 Finalizare", data_f, b3b["B"], b3b["E"], b3b["C"], b3b["D"]),
        ("B4 Vânzare", data_v, b4a["B"], b4a["E"], b4a["F"], b4a["D"]),
        ("B4 TVA", data_v, b4a["B"], b4b["E"], b4b["F"], b4b["G"]),
        ("B4 Descărcare", data_v, b4c["B"], b4c["E"], b4c["C"], b4c["D"]),
    ]
    for i, (bloc, data, cd, cc, suma, desc) in enumerate(linii, start=1):
        e.rand([i, bloc, f"={D(data)}", f"={j.ref(cd)}", f"={j.ref(cc)}",
                f"={j.ref(suma)}", f"={j.ref(desc)}", "Producție / neutralizare",
                f'=IF(AND(ISNUMBER(F{e.r}),F{e.r}>0),"DA","NU")'])
    ultim = e.r - 1
    e.gol()
    e.kv("Rânduri de importat", f'=COUNTIF(I{primul}:I{ultim},"DA")', tip="calc")
    e.check("Check global", f"={j.ref(glob)}",
            f'=IF(ABS(B{e.r})<0.01,"OK","EROARE")')
