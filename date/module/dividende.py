"""MOD_DIVIDENDE — repartizarea rezultatului către asociați, de la AGA la D710.

Acoperă F-109 (dividende certe din rezultatul reportat) și F-110 (dividende interimare).

Cazul se repetă la fiecare AGA și are aritmetică de greșit la fiecare pas: cotele de
participare, impozitul de 16%, plafonul interimarelor, stornarea de la 31.12. Nimic din
ce face modulul nu e greu — dar toate patru trebuie să iasă, iar cine le face o dată pe
an le face de fiecare dată de la zero.

## Ce apără modulul

**Cotele vin din 1012, nu din AGA.** Hotărârea AGA e DOCUMENTUL repartizării, nu sursa
cotelor. Ordinea de lucru e: mai întâi balanța, unde 1012 e spart pe asociați cu
procentul în denumire, apoi contraverificarea cu ce scrie în hotărâre. Invers, ajungi să
înregistrezi o repartizare pe procente care nu există nicăieri în contabilitate — cazul
ajuns la comisia de disciplină la ANAF.

**Plafonul interimarelor e soldul lui 121, nu disponibilul din bancă.** Administratorul
vede bani în cont și cere să ridice. Modulul spune cu CÂT se depășește, nu doar că se
depășește: diferența e chiar suma care va trebui stornată și returnată.

**Impozitul se datorează la DISTRIBUIRE.** Termenul e 25.01 a anului următor
repartizării, chiar dacă asociatul n-a ridicat nimic. Obligația e față de buget, nu față
de asociat, iar un 457 cu sold creditor la 31.12 nu amână nimic.

## Exemplul din notițe nu se leagă, și e instructiv că nu se leagă

Notițele scriu analiticele lui 1012 ca „Ionescu 33,3%”, „Popescu 33,3%”, „Xulescu 33,3%”
— care însumează 99,9%, nu 100% — și repartizează apoi exact 10.000 lei fiecare dintr-un
total de 30.000. Cele două nu pot fi amândouă adevărate: 33,3% din 30.000 e 9.990.

Nu e o greșeală de calcul a formatorului, e felul în care se scrie o cotă în practică.
De aceea modulul folosește 33,33 / 33,33 / 33,34 — care chiar însumează 100% — iar garda
pe sume acceptă abaterea de rotunjire, cu o toleranță DERIVATĂ din total (o sutime de
procent), nu aleasă. Peste banda aia, hotărârea chiar repartizează altfel decât spun
cotele din balanță, și atunci garda are ce spune.

## De ce sumele pe asociat sunt INTRARE, nu calcul

Modulul ar putea calcula singur `cotă × total` și ar ieși mereu corect — dar atunci n-ar
verifica nimic: o gardă care compară o valoare cu ea însăși e verde întotdeauna. Sumele
pe asociat se introduc așa cum apar în hotărârea AGA, iar modulul le recalculează alături
și compară. Același tipar ca la MOD_TAXARE_INVERSA, unde TVA-ul vine de pe autofactură.

Impozitul are două căi independente: pe asociat (16% × brutul lui) și pe total (16% ×
totalul din AGA). Cele două se calculează din intrări diferite, deci pot să nu se
potrivească — și exact atunci garda are ce spune.
"""
from .comun import formula_activ, sectiune_temei

COD = "MOD_DIVIDENDE"

CATALOG = dict(
    fluxuri="F-109, F-110",
    tip="La fiecare hotărâre AGA de repartizare",
    variabile="Total repartizat, cotele din 1012, sold 121, profit final la 31.12",
    porti="Σ cote = 100%; sume = cotă × total; interimare ≤ sold 121; impozit pe două căi",
    blocuri="A Repartizare pe asociați; B Impozitul de 16%; C Interimare cu plafon; "
            "D Storno la 31.12 + D710",
    ce_face="Repartizarea rezultatului către asociați, cu impozit și regularizare",
    cand="La AGA de repartizare și la 31.12",
    activ="NU",
)

#: tip de dividend, cont, când se acordă, ce document cere în plus
TIPURI = [
    ("Certe", "457", "Din rezultatul unui exercițiu ÎNCHEIAT (1171)",
     "Hotărâre AGA. Condiție: 1171 fără sold debitor pe niciun an"),
    ("Interimare", "463 → 456", "Din profitul anului CURENT, doar trimestrial",
     "Hotărâre AGA + INVENTARIERE + bilanț interimar"),
]

#: declarație, cadență, ce conține
DECLARATII = [
    ("D100", "Ori de câte ori e impozit de plată",
     "Impozitul pe dividende. Atenție la rubrica separată pentru persoane fizice — "
     "nu se confundă cu impozitul datorat de persoane juridice"),
    ("D205", "Anual, cumulativ",
     "Declarație informativă. Două rubrici distincte: dividende DISTRIBUITE și "
     "dividende RIDICATE. Se confruntă cu D100 și cu fișa contului 446"),
    ("Declarația Unică", "Anual, de către asociat",
     "CASS. ❓ Notițele spun că se datorează la dividendele RIDICATE, nu la cele "
     "distribuite — de confirmat cu formatorul"),
    ("D710", "La regularizarea de la 31.12",
     "Rectificativa lui D100. Apare suma plătită inițial și cea corectată; diferența "
     "plătită în plus se compensează sau se restituie la cerere"),
]

#: momentul, ce se întâmplă — calendarul interimarelor, care nu e intuitiv
CALENDAR = [
    ("30.06", "Închiderea a șase luni. Soldul lui 121 la data asta E plafonul"),
    ("iunie", "LUNA în care se face înregistrarea contabilă — bilanțul interimar are "
              "rubrică separată pentru 463, deci acolo vede ANAF ce s-a repartizat"),
    ("iulie", "LUNA în care se ia hotărârea AGA: are nevoie de balanța închisă"),
    ("31.07", "Termenul de depunere a bilanțului interimar"),
    ("31.12", "Comparația cu profitul realizat. Dacă e mai mic, se stornează diferența"),
    ("25.01", "Termenul de plată a impozitului, indiferent dacă s-a ridicat sau nu"),
]


#: (ce se sprijină pe el, temei) — secțiunea finală din `Reguli`.
TEMEI_LEGAL = [
    ('Dividendele se repartizează proporțional cu cota de participare la capitalul social',
     'art. 67 alin. (2) Legea 31/1990'),
    ('Cota de impozit pe dividende, 16% pentru distribuirile de la 01.01.2026',
     'art. 43 Cod fiscal, astfel cum a fost modificat prin Legea 141/2025'),
    ('Termenul de plată: 25 ianuarie a anului următor celui în care s-a aprobat '
     'repartizarea, dacă dividendele nu au fost ridicate',
     'art. 43 alin. (3) Cod fiscal'),
    ('Dividendele interimare, trimestrial, pe baza situațiilor financiare interimare',
     'art. 67 alin. (2) și (4) Legea 31/1990 — cu inventariere prealabilă'),
    ('Regularizarea la 31.12 și restituirea diferenței distribuite în plus',
     'art. 67 alin. (4) Legea 31/1990'),
    ('Nu se distribuie dividende cât timp există pierdere contabilă reportată neacoperită',
     'art. 69 Legea 31/1990'),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_DIVIDENDE", {"A": 50, "B": 20, "C": 62})
    d.titlu("MOD_DIVIDENDE — Declarații (input)")
    d.nota("Valorile implicite reproduc monografiile din F-109 (30.000 lei, trei "
           "asociați în cote egale) și F-110 (interimare de 80.000 pe un 121 de "
           "80.000, regularizate la un profit final de 70.000).")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    d.kv("CUI", "=Parametri!B6", tip="calc")
    exercitiu = d.kv("Exercițiul repartizat (AAAA)", "2025")
    nr_aga = d.kv("Hotărârea AGA (număr și dată)", "12 / 2026-04-20")
    data_j = d.kv("Data notei contabile", "2026-04-30")
    d.gol()

    d.sectiune("2. Blocul A — Repartizarea dividendelor certe")
    a_on = d.kv("Se aplică? (DA/NU)", "DA")
    a_sold_1171 = d.kv("Sold 1171 pe exercițiul repartizat (creditor)", 30000,
                       nota="Sold DEBITOR = pierdere neacoperită: nu se distribuie nimic")
    a_total = d.kv("Total repartizat prin hotărârea AGA", 30000)
    d.gol()

    d.nota("Cotele se citesc din DENUMIRILE analiticelor lui 1012, nu din hotărâre. "
           "Sumele se introduc așa cum apar în hotărâre; modulul le recalculează "
           "alături și compară — de-aia sunt intrare, nu formulă.")
    d.sectiune("2.1 Asociatul 1")
    a1_nume = d.kv("Nume (din 1012)", "Ionescu")
    a1_cota = d.kv("Cota de participare (din denumirea analiticului)", 0.3333)
    a1_suma = d.kv("Sumă din hotărârea AGA", 10000)
    a1_calc = d.kv("Recalculat: cotă × total", f"=ROUND({a1_cota}*{a_total},2)",
                   tip="calc")
    d.sectiune("2.2 Asociatul 2")
    a2_nume = d.kv("Nume (din 1012)", "Popescu")
    a2_cota = d.kv("Cota de participare", 0.3333)
    a2_suma = d.kv("Sumă din hotărârea AGA", 10000)
    a2_calc = d.kv("Recalculat: cotă × total", f"=ROUND({a2_cota}*{a_total},2)",
                   tip="calc")
    d.sectiune("2.3 Asociatul 3")
    a3_nume = d.kv("Nume (din 1012)", "Xulescu")
    a3_cota = d.kv("Cota de participare", 0.3334)
    a3_suma = d.kv("Sumă din hotărârea AGA", 10000)
    a3_calc = d.kv("Recalculat: cotă × total", f"=ROUND({a3_cota}*{a_total},2)",
                   tip="calc")
    # Procentele din denumirile analiticelor sunt ROTUNJITE — „33,33%”, nu o treime.
    # Diferența dintre suma din hotărâre și recalcul e legitimă exact cât ține
    # rotunjirea: o sutime de procent aplicată totalului. Peste banda asta, hotărârea
    # chiar repartizează altfel decât spun cotele. Toleranța se derivă din total, nu
    # se alege — la 30.000 lei sunt 3 lei, la 3.000.000 sunt 300.
    toleranta = d.kv("Toleranța de rotunjire a cotelor (auto)",
                     f"=ROUND({a_total}*0.0001,2)", tip="calc",
                     nota="O sutime de procent din total — precizia cu care se scrie "
                          "cota în denumirea analiticului")
    d.gol()

    d.sectiune("3. Blocul B — Impozitul pe dividende")
    b_cota = d.kv("Cota de impozit", f"={P['cota_impozit_dividend']}", tip="calc")
    b_impozit = d.kv("Impozit reținut, din nota contabilă", 4800)
    b_pe_asociat = d.kv(
        "Recalculat, calea 1: Σ (16% × brutul fiecărui asociat)",
        f"=ROUND({a1_suma}*{b_cota},2)+ROUND({a2_suma}*{b_cota},2)"
        f"+ROUND({a3_suma}*{b_cota},2)", tip="calc")
    b_pe_total = d.kv("Recalculat, calea 2: 16% × totalul din hotărâre",
                      f"=ROUND({a_total}*{b_cota},2)", tip="calc")
    b_ridicat = d.kv("S-au ridicat dividendele? (DA/NU)", "DA",
                     nota="NU → 457 rămâne cu sold, dar impozitul se plătește oricum")
    d.gol()

    d.sectiune("4. Blocul C — Dividende interimare")
    c_on = d.kv("Se aplică? (DA/NU)", "DA")
    c_inventariere = d.kv("S-a făcut inventarierea? (DA/NU)", "DA")
    c_bilant = d.kv("S-a întocmit bilanțul interimar? (DA/NU)", "DA")
    c_sold_121 = d.kv("Sold creditor 121 la data bilanțului interimar", 80000,
                      nota="Din BALANȚĂ, după înregistrarea impozitului — nu din extras")
    c_cerut = d.kv("Suma cerută de administrator", 100000)
    c_repartizat = d.kv("Suma efectiv repartizată", 80000)
    c_impozit = d.kv("Impozit pe interimare, din nota contabilă", 12800)
    c_impozit_calc = d.kv("Recalculat: 16% × repartizat",
                          f"=ROUND({c_repartizat}*{b_cota},2)", tip="calc")
    d.gol()

    d.sectiune("5. Blocul D — Regularizarea la 31.12")
    e_on = d.kv("Se aplică? (DA/NU)", "DA")
    e_profit_final = d.kv("Profit realizat la 31.12 (sold 121)", 70000)
    e_diferenta = d.kv("Diferența de stornat (auto)",
                       f"=MAX(0,{c_repartizat}-{e_profit_final})", tip="calc")
    e_storno_imp = d.kv("Storno de impozit (auto)",
                        f"=ROUND({e_diferenta}*{b_cota},2)", tip="calc")
    d.gol()

    d.sectiune("6. Conturi")
    k_1171 = d.kv("Cont rezultat reportat", "1171")
    k_457_1 = d.kv("Cont dividende asociat 1", "457.1")
    k_457_2 = d.kv("Cont dividende asociat 2", "457.2")
    k_457_3 = d.kv("Cont dividende asociat 3", "457.3")
    k_446 = d.kv("Cont impozit pe dividende", "446.dividende")
    k_463 = d.kv("Cont dividende interimare", "463")
    k_456 = d.kv("Cont decontări cu asociații", "456")
    k_banca = d.kv("Cont trezorerie", "5121")
    d.gol()

    d.sectiune("7. Sufix")
    sufix = d.kv("Sufix", f'="— AGA " & {nr_aga} & ", exercițiul " & {exercitiu}',
                 tip="calc")
    d.gol()

    d.sectiune("8. Control")
    d.kv("Modul activ?", formula_activ(COD), tip="calc")

    # Garda 1: cotele. Σ cote = 100% e o condiție PE INTRĂRI — niciuna dintre ele nu e
    # calculată de modul, deci verificarea are ce compara.
    ver_cote = d.kv(
        "Verificare: Σ cotelor de participare = 100%",
        f'=IF(OR({a_on}<>"DA",ABS({a1_cota}+{a2_cota}+{a3_cota}-1)<0.0001),'
        f'"OK — cotele acoperă exact capitalul",'
        f'"EROARE — Σ cote = " & TEXT({a1_cota}+{a2_cota}+{a3_cota},"0.00%") & '
        f'"; un asociat lipsește din 1012 sau un procent e greșit")', tip="calc")

    # Garda 2: sumele din hotărâre vs. recalculul din cote. Ambele părți vin din
    # intrări diferite — suma e transcrisă din AGA, recalculul pleacă din cotă.
    ver_sume = d.kv(
        "Verificare: sumele din AGA = cotă × total",
        f'=IF(OR({a_on}<>"DA",AND(ABS({a1_suma}-{a1_calc})<={toleranta},'
        f'ABS({a2_suma}-{a2_calc})<={toleranta},'
        f'ABS({a3_suma}-{a3_calc})<={toleranta})),'
        f'"OK — repartizarea din hotărâre urmează cotele din 1012, în limita '
        f'rotunjirii procentelor",'
        f'"EROARE — hotărârea repartizează altfel decât spun cotele din balanță: '
        f'abateri de " & TEXT({a1_suma}-{a1_calc},"#,##0.00") & " / " & '
        f'TEXT({a2_suma}-{a2_calc},"#,##0.00") & " / " & '
        f'TEXT({a3_suma}-{a3_calc},"#,##0.00") & " lei, peste toleranța de " & '
        f'TEXT({toleranta},"#,##0.00"))',
        tip="calc")

    ver_total = d.kv(
        "Verificare: Σ sumelor repartizate = totalul din hotărâre",
        f'=IF(OR({a_on}<>"DA",ABS({a1_suma}+{a2_suma}+{a3_suma}-{a_total})<0.01),'
        f'"OK","EROARE — Σ pe asociați diferă de total cu " & '
        f'TEXT({a1_suma}+{a2_suma}+{a3_suma}-{a_total},"#,##0.00") & " lei")', tip="calc")

    ver_sursa = d.kv(
        "Verificare: există sursă în 1171 pentru ce se repartizează",
        f'=IF(OR({a_on}<>"DA",{a_sold_1171}>={a_total}),'
        f'"OK",IF({a_sold_1171}<0,'
        f'"BLOCAT — 1171 are sold debitor: cu pierdere neacoperită nu se distribuie '
        f'nimic (art. 69 L. 31/1990)",'
        f'"EROARE — se repartizează mai mult decât are 1171, lipsă " & '
        f'TEXT({a_total}-{a_sold_1171},"#,##0.00") & " lei"))', tip="calc")

    # Garda 3: impozitul, pe două căi de calcul care pleacă din intrări diferite.
    ver_impozit = d.kv(
        "Verificare: impozitul reținut, pe două căi",
        f'=IF({a_on}<>"DA","—",'
        f'IF(AND(ABS({b_impozit}-{b_pe_asociat})<0.01,'
        f'ABS({b_impozit}-{b_pe_total})<0.02),'
        f'"OK — 16% verificat și pe asociat, și pe total",'
        f'"EROARE — impozit " & TEXT({b_impozit},"#,##0.00") & " vs. " & '
        f'TEXT({b_pe_asociat},"#,##0.00") & " pe asociat și " & '
        f'TEXT({b_pe_total},"#,##0.00") & " pe total"))', tip="calc")

    # Garda 4: plafonul interimarelor. Ambii termeni sunt intrări: soldul lui 121 vine
    # din balanță, suma repartizată din hotărâre. Mesajul spune CU CÂT se depășește,
    # pentru că fix suma aia va trebui stornată și adusă înapoi de asociat.
    ver_plafon = d.kv(
        "Verificare: interimarele nu depășesc soldul lui 121",
        f'=IF({c_on}<>"DA","—",'
        f'IF({c_repartizat}<={c_sold_121},'
        f'"OK — sub plafon, rezervă de " & '
        f'TEXT({c_sold_121}-{c_repartizat},"#,##0.00") & " lei",'
        f'"EROARE — depășire de " & TEXT({c_repartizat}-{c_sold_121},"#,##0.00") & '
        f'" lei, care se va storna la 31.12 și se va restitui"))', tip="calc")

    ver_conditii = d.kv(
        "Verificare: condițiile legale ale interimarelor",
        f'=IF({c_on}<>"DA","—",'
        f'IF(AND({c_inventariere}="DA",{c_bilant}="DA"),'
        f'"OK — inventariere și bilanț interimar făcute",'
        f'"BLOCAT — interimarele cer INVENTARIERE și bilanț interimar; '
        f'sunt condiții legale, nu formalități"))', tip="calc")

    ver_cerut = d.kv(
        "Informativ: cât a cerut administratorul vs. cât poate ridica net",
        f'=IF({c_on}<>"DA","—","Cerut " & TEXT({c_cerut},"#,##0") & " lei; '
        f'repartizabil " & TEXT(MIN({c_cerut},{c_sold_121}),"#,##0") & '
        f'"; ridicat net " & TEXT({c_repartizat}-{c_impozit},"#,##0") & " lei")',
        tip="calc")

    ver_regul = d.kv(
        "Verificare: după storno, 463 rămâne la nivelul profitului realizat",
        f'=IF({e_on}<>"DA","—",'
        f'IF(ABS(({c_repartizat}-{e_diferenta})-MIN({c_repartizat},{e_profit_final}))'
        f'<0.01,"OK — 463 = " & TEXT({c_repartizat}-{e_diferenta},"#,##0.00") & '
        f'" lei, adică profitul realizat","EROARE — stornarea nu aduce 463 la '
        f'profitul realizat"))', tip="calc")

    d.kv("Termenul care surprinde",
         "Impozitul pe dividende se plătește până la 25.01 a anului următor "
         "repartizării, CHIAR DACĂ dividendele nu au fost ridicate. Obligația e față "
         "de buget, nu față de asociat.", tip="calc")

    # ------------------------------------------------------------------- Reguli
    g = F("Reguli_DIVIDENDE", {"A": 26, "B": 18, "C": 42, "D": 52})
    g.titlu("MOD_DIVIDENDE — Reguli (tabele fixe)")
    g.nota("Ce e regulă dată, nu formulă: tipurile de dividend, declarațiile și "
           "calendarul interimarelor.")
    g.gol()

    g.sectiune("Tabel A — Cele două feluri de dividende")
    g.cap(["Tip", "Cont", "Din ce se repartizează", "Ce document cere"])
    for rand in TIPURI:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel B — Declarațiile")
    g.cap(["Declarație", "Cadență", "Ce conține"])
    for rand in DECLARATII:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel C — Calendarul interimarelor")
    g.nota("Nu e intuitiv: hotărârea se ia într-o lună, înregistrarea se face în alta.")
    g.cap(["Momentul", "Ce se întâmplă"])
    for rand in CALENDAR:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel D — Porți de calitate")
    for linie in [
        "• Cotele se citesc din DENUMIRILE analiticelor lui 1012; hotărârea AGA se "
        "contraverifică cu ele, nu invers",
        "• Fără hotărâre AGA nu se înregistrează dividende — nici certe, nici interimare",
        "• Cu sold debitor pe 1171 (pierdere neacoperită) nu se distribuie nimic",
        "• Interimarele cer inventariere ȘI bilanț interimar, și se acordă doar trimestrial",
        "• Plafonul interimarelor e soldul lui 121, nu disponibilul din bancă",
        "• Impozitul se datorează la DISTRIBUIRE; termenul de 25.01 nu depinde de ridicare",
        "• 457 se stinge doar prin 446 sau prin trezorerie — nu prin 4551 sau 461 "
        "(vezi C-34)",
        "• D205 se confruntă cu D100 și cu fișa contului 446: se caută o plată făcută "
        "fără declarație",
    ]:
        g.nota(linie)

    sectiune_temei(g, TEMEI_LEGAL)

    # ------------------------------------------------------------------ Jurnale
    j = F("Jurnale_DIVIDENDE",
          {"A": 30, "B": 18, "C": 14, "D": 52, "E": 18, "F": 14, "G": 52})
    j.titlu("MOD_DIVIDENDE — Jurnale (generate automat)")
    j.nota("Blocurile neactivate ies cu zero. Blocul D produce sume NEGATIVE: e "
           "stornare, nu o înregistrare inversă.")
    j.gol()

    D = d.ref
    antet = ["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr",
             "Descriere Cr"]

    def daca(comutator, valoare):
        return f'=IF({D(comutator)}="DA",{D(valoare)},0)'

    j.sectiune("Bloc A — Repartizarea pe asociați")
    j.kv("Data:", f"={D(data_j)}", tip="calc")
    j.cap(antet)
    randuri_a = []
    for i, (nume, suma, cont) in enumerate([
        (a1_nume, a1_suma, k_457_1), (a2_nume, a2_suma, k_457_2),
        (a3_nume, a3_suma, k_457_3)], start=1):
        randuri_a.append(j.rand([
            i, f"={D(k_1171)}", daca(a_on, suma),
            f'="Repartizare dividende " & {D(nume)} & " " & {D(sufix)}',
            f"={D(cont)}", daca(a_on, suma),
            f'="Dividende de plată " & {D(nume)} & " " & {D(sufix)}']))
    ca = j.check(
        "Check A (Σ pe asociați = totalul din hotărâre)",
        f"={randuri_a[0]['C']}+{randuri_a[1]['C']}+{randuri_a[2]['C']}"
        f'-IF({D(a_on)}="DA",{D(a_total)},0)',
        f'=IF(ABS(B{j.r})<0.01,"OK — repartizarea acoperă exact totalul din AGA",'
        f'"EROARE — Σ pe asociați ≠ total")')
    j.gol()

    j.sectiune("Bloc B — Impozitul de 16%")
    j.cap(antet)
    b_randuri = []
    for i, (nume, suma, cont) in enumerate([
        (a1_nume, a1_suma, k_457_1), (a2_nume, a2_suma, k_457_2),
        (a3_nume, a3_suma, k_457_3)], start=1):
        b_randuri.append(j.rand([
            i, f"={D(cont)}",
            f'=IF({D(a_on)}="DA",ROUND({D(suma)}*{D(b_cota)},2),0)',
            f'="Impozit 16% dividende " & {D(nume)} & " " & {D(sufix)}',
            f"={D(k_446)}",
            f'=IF({D(a_on)}="DA",ROUND({D(suma)}*{D(b_cota)},2),0)',
            f'="Impozit pe dividende de plată " & {D(sufix)}']))
    b_plata = j.rand([
        4, f"={D(k_446)}", daca(a_on, b_impozit),
        f'="Plata impozitului pe dividende (termen 25.01) " & {D(sufix)}',
        f"={D(k_banca)}", daca(a_on, b_impozit),
        f'="Ieșire trezorerie " & {D(sufix)}'])
    cb = j.check(
        "Check B (impozitul din notă = Σ reținerilor pe asociat)",
        f"={D(b_impozit)}*IF({D(a_on)}=\"DA\",1,0)"
        f"-{b_randuri[0]['C']}-{b_randuri[1]['C']}-{b_randuri[2]['C']}",
        f'=IF(ABS(B{j.r})<0.01,"OK — 16% pe fiecare analitic de 457",'
        f'"EROARE — impozitul plătit nu e suma reținerilor")')
    j.gol()

    j.sectiune("Bloc B2 — Plata dividendelor nete")
    j.cap(antet)
    b2_randuri = []
    for i, (nume, suma, cont) in enumerate([
        (a1_nume, a1_suma, k_457_1), (a2_nume, a2_suma, k_457_2),
        (a3_nume, a3_suma, k_457_3)], start=1):
        b2_randuri.append(j.rand([
            i, f"={D(cont)}",
            f'=IF(AND({D(a_on)}="DA",{D(b_ridicat)}="DA"),'
            f'{D(suma)}-ROUND({D(suma)}*{D(b_cota)},2),0)',
            f'="Plată dividend net " & {D(nume)} & " " & {D(sufix)}',
            f"={D(k_banca)}",
            f'=IF(AND({D(a_on)}="DA",{D(b_ridicat)}="DA"),'
            f'{D(suma)}-ROUND({D(suma)}*{D(b_cota)},2),0)',
            f'="Ieșire trezorerie " & {D(sufix)}']))
    cb2 = j.check(
        "Check B2 (457 se stinge integral după plată)",
        f"={randuri_a[0]['C']}+{randuri_a[1]['C']}+{randuri_a[2]['C']}"
        f"-{b_randuri[0]['C']}-{b_randuri[1]['C']}-{b_randuri[2]['C']}"
        f"-{b2_randuri[0]['C']}-{b2_randuri[1]['C']}-{b2_randuri[2]['C']}",
        f'=IF(ABS(B{j.r})<0.01,"OK — 457 = 0 pe fiecare analitic",'
        f'IF({D(b_ridicat)}<>"DA",'
        f'"AȘTEPTARE — dividende neridicate: 457 rămâne cu sold, impozitul e plătit",'
        f'"EROARE — 457 nu se stinge"))')
    j.gol()

    j.sectiune("Bloc C — Dividende interimare")
    j.cap(antet)
    c1 = j.rand([1, f"={D(k_463)}", daca(c_on, c_repartizat),
                 f'="Dividende interimare repartizate " & {D(sufix)}',
                 f"={D(k_456)}", daca(c_on, c_repartizat),
                 f'="Datorie față de asociat, interimar " & {D(sufix)}'])
    c2 = j.rand([2, f"={D(k_456)}", daca(c_on, c_impozit),
                 f'="Impozit 16% pe dividende interimare " & {D(sufix)}',
                 f"={D(k_446)}", daca(c_on, c_impozit),
                 f'="Impozit de plată " & {D(sufix)}'])
    c3 = j.rand([3, f"={D(k_456)}",
                 f'=IF({D(c_on)}="DA",{D(c_repartizat)}-{D(c_impozit)},0)',
                 f'="Plata dividendelor interimare " & {D(sufix)}',
                 f"={D(k_banca)}",
                 f'=IF({D(c_on)}="DA",{D(c_repartizat)}-{D(c_impozit)},0)',
                 f'="Ieșire trezorerie " & {D(sufix)}'])
    cc = j.check(
        "Check C (456 se stinge integral)",
        f"={c1['F']}-{c2['C']}-{c3['C']}",
        f'=IF(ABS(B{j.r})<0.01,"OK — 456 = 0; 463 rămâne creanță până la 31.12",'
        f'"EROARE — 456 nu se stinge")')
    cc_plafon = j.check(
        "Check C2 (repartizat ≤ sold 121)",
        f'=IF({D(c_on)}="DA",MAX(0,{D(c_repartizat)}-{D(c_sold_121)}),0)',
        f'=IF(B{j.r}<0.01,"OK — sub plafonul profitului realizat",'
        f'"EROARE — depășire de " & TEXT(B{j.r},"#,##0.00") & " lei")')
    j.gol()

    j.sectiune("Bloc D — Regularizarea la 31.12 (storno)")
    j.nota("Sumele sunt NEGATIVE: stornarea se face în roșu, nu prin înregistrare "
           "inversă. Cele două rânduri se echilibrează fiecare în parte.")
    j.cap(antet)
    d1 = j.rand([1, f"={D(k_463)}",
                 f'=IF({D(e_on)}="DA",-{D(e_diferenta)},0)',
                 f'="Storno dividende interimare nerealizate " & {D(sufix)}',
                 f"={D(k_456)}",
                 f'=IF({D(e_on)}="DA",-{D(e_diferenta)},0)',
                 f'="Storno datorie față de asociat " & {D(sufix)}'])
    d2 = j.rand([2, f"={D(k_456)}",
                 f'=IF({D(e_on)}="DA",-{D(e_storno_imp)},0)',
                 f'="Storno impozit pe partea nerealizată " & {D(sufix)}',
                 f"={D(k_446)}",
                 f'=IF({D(e_on)}="DA",-{D(e_storno_imp)},0)',
                 f'="Storno impozit de plată (rectificativă D710) " & {D(sufix)}'])
    d3 = j.rand([3, f"={D(k_463)}", 0,
                 '"Anul următor, la AGA: 121 = 1171, apoi 1171 = 463 pe partea rămasă"',
                 f"={D(k_463)}", 0, '"Vezi F-110 pașii de închidere"'])
    cd = j.check(
        "Check D (storno = repartizat − profit realizat)",
        f'=IF({D(e_on)}="DA",'
        f'ABS({d1["C"]})-MAX(0,{D(c_repartizat)}-{D(e_profit_final)}),0)',
        f'=IF(ABS(B{j.r})<0.01,"OK — se stornează exact partea nerealizată",'
        f'"EROARE — stornarea nu corespunde diferenței")')
    j.gol()

    glob = j.check(
        "Check global",
        f"=ABS({ca})+ABS({cb})+ABS({cb2})+ABS({cc})+ABS({cc_plafon})+ABS({cd})",
        f'=IF(B{j.r}<0.01,"OK — toate blocurile se închid",'
        f'"EROARE — cel puțin un bloc nu se închide")')
    j.gol()
    j.sectiune("Stare terminală")
    j.nota("După blocul B2: 1171 repartizat integral, 446 = 0, 457 = 0 pe fiecare "
           "analitic (dacă s-a ridicat). După blocul D: 463 rămâne la nivelul "
           "profitului realizat și se soldează anul următor, prin 1171. Rămâne de "
           "depus D710 și de recuperat de la asociat diferența stornată.")

    # --------------------------------------------------------------- NotaExport
    e = F("NotaExport_DIVIDENDE",
          {"A": 6, "B": 30, "C": 14, "D": 14, "E": 14, "F": 14, "G": 52, "H": 26,
           "I": 10})
    e.titlu("MOD_DIVIDENDE — Notă pentru import")
    e.nota("Filtrează Include=DA. Rândurile de storno au sumă negativă și se importă "
           "ca atare — includerea lor se decide după sumă ≠ 0, nu după semn.")
    e.gol()
    e.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    primul = e.r
    linii = (
        [(f"A Repartizare asociat {i}", r, "Hotărâre AGA")
         for i, r in enumerate(randuri_a, start=1)]
        + [(f"B Impozit asociat {i}", r, "Notă contabilă")
           for i, r in enumerate(b_randuri, start=1)]
        + [("B Plata impozitului", b_plata, "Ordin de plată")]
        + [(f"B2 Plată net asociat {i}", r, "Ordin de plată")
           for i, r in enumerate(b2_randuri, start=1)]
        + [("C Interimare — repartizare", c1, "Hotărâre AGA + bilanț interimar"),
           ("C Interimare — impozit", c2, "Notă contabilă"),
           ("C Interimare — plată", c3, "Ordin de plată"),
           ("D Storno interimare", d1, "Notă contabilă 31.12"),
           ("D Storno impozit", d2, "Notă contabilă + D710"),
           ("D Închidere anul următor", d3, "Hotărâre AGA anul următor")]
    )
    for i, (bloc, r, doc) in enumerate(linii, start=1):
        e.rand([i, bloc, f"={D(data_j)}", f"={j.ref(r['B'])}", f"={j.ref(r['E'])}",
                f"={j.ref(r['C'])}", f"={j.ref(r['D'])}", doc,
                f'=IF(AND(ISNUMBER(F{e.r}),ABS(F{e.r})>0),"DA","NU")'])
    ultim = e.r - 1
    e.gol()
    e.kv("Rânduri de importat", f'=COUNTIF(I{primul}:I{ultim},"DA")', tip="calc")
    e.check("Check global", f"={j.ref(glob)}",
            f'=IF(ABS(B{e.r})<0.01,"OK","EROARE")')
