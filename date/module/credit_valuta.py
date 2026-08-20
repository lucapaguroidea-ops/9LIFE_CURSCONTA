"""MOD_CREDIT_VALUTA — credit bancar în valută, cu ambele momente de curs.

Acoperă F-49.

Greșeala pe care o previne modulul: se înregistrează diferența de curs LA PLATĂ și se
uită reevaluarea lunară a soldului rămas. Sunt două momente distincte, iar al doilea e
obligatoriu lunar (OMFP 1802/2014) — „la 3 luni”, cum apărea în notițe, e insuficient.

A doua capcană, la fel de costisitoare: extrasul bancar arată deseori rata de capital și
dobânda CUMULAT. Cine le înregistrează așa ajunge fie cu 1621 pe debit, fie cu sold rămas
la finalul creditului — adică a trecut pe cheltuială mai mult decât trebuia, cu efect pe
impozitul pe profit și pe dividende. Modulul le cere separat, din scadențar.

Verificarea finală e cea care contează: soldul în lei trebuie să fie EXACT soldul în
valută înmulțit cu cursul BNR de la închidere. Dacă nu e, una dintre cele două diferențe
lipsește.
"""

COD = "MOD_CREDIT_VALUTA"

CATALOG = dict(
    fluxuri="F-49",
    tip="Lunar, pe contract",
    variabile="Sold valută, curs inițial, rată, dobândă, comision, curs plată, curs BNR",
    porti="Reevaluare lunară obligatorie; rata și dobânda se iau din scadențar, nu din extras",
    blocuri="B1 Rata + diferența la plată; B2 Dobânda; B3 Comisioane; B4 Reevaluarea soldului",
)


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_CREDIT_VALUTA", {"A": 46, "B": 20, "C": 62})
    d.titlu("MOD_CREDIT_VALUTA — Declarații (input)")
    d.nota("Valorile implicite reproduc monografia din F-49. Rata și dobânda se iau din "
           "SCADENȚAR, nu din extras — extrasul le arată deseori cumulat.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    contract = d.kv("Număr contract de credit", "CR-2026-001",
                    nota="1621 se ține analitic pe contract și pe valută")
    luna = d.kv("Luna (AAAA-LL)", "2026-07")
    data_plata = d.kv("Data plății ratei", "2026-07-15")
    data_reeval = d.kv("Data reevaluării (ultima zi bancară a lunii)", "2026-07-31")
    valuta = d.kv("Valuta", "EUR")
    d.gol()

    d.sectiune("2. Soldul de la care pornim")
    sold_val = d.kv("Sold inițial, în valută", 20000)
    curs_ini = d.kv("Cursul la care e înregistrat soldul", 4.97)
    sold_lei = d.kv("Sold inițial, în lei", f"=ROUND({sold_val}*{curs_ini},2)", tip="calc")
    d.gol()

    d.sectiune("3. Mișcările lunii (din SCADENȚAR)")
    rata_val = d.kv("Rata de capital, în valută", 5000)
    dob_val = d.kv("Dobânda, în valută", 200)
    curs_plata = d.kv("Cursul de la data plății", 4.99)
    comision = d.kv("Comisioane bancare, în lei", 50)
    d.gol()

    d.sectiune("4. Reevaluarea de la finalul lunii")
    curs_bnr = d.kv("Curs BNR la data reevaluării", 5.01)
    d.gol()

    d.sectiune("5. Calcul automat (nu edita)")
    rata_ini = d.kv("Rata, la cursul de înregistrare", f"=ROUND({rata_val}*{curs_ini},2)",
                    tip="calc")
    rata_plata = d.kv("Rata, la cursul de plată", f"=ROUND({rata_val}*{curs_plata},2)",
                      tip="calc")
    dif1 = d.kv("MOMENTUL 1 — diferența la plată", f"={rata_plata}-{rata_ini}", tip="calc",
                nota="Pozitiv = nefavorabil (665); negativ = favorabil (765)")
    dob_lei = d.kv("Dobânda, în lei", f"=ROUND({dob_val}*{curs_plata},2)", tip="calc")
    rest_val = d.kv("Sold rămas, în valută", f"={sold_val}-{rata_val}", tip="calc")
    rest_ini = d.kv("Sold rămas, la cursul de înregistrare",
                    f"=ROUND({rest_val}*{curs_ini},2)", tip="calc")
    rest_bnr = d.kv("Sold rămas, la cursul BNR", f"=ROUND({rest_val}*{curs_bnr},2)",
                    tip="calc")
    dif2 = d.kv("MOMENTUL 2 — diferența din reevaluare", f"={rest_bnr}-{rest_ini}",
                tip="calc", nota="Pozitiv = datoria crește = nefavorabil (665)")
    d.gol()

    d.sectiune("6. Conturi")
    c_credit = d.kv("Cont credit (162x)", "1621",
                    nota="1621…1627 sunt sintetice DISTINCTE, nu analitice ale aceluiași cont")
    c_dob_neajunsa = d.kv("Cont dobândă neajunsă la scadență", 1682)
    c_banca_val = d.kv("Cont trezorerie în valută", "5124")
    c_banca_lei = d.kv("Cont trezorerie în lei", "5121")
    c_dob = d.kv("Cont cheltuială cu dobânda", 666)
    c_com = d.kv("Cont cheltuială cu serviciile bancare", 627)
    c_nefav = d.kv("Cont diferențe nefavorabile", 665)
    c_fav = d.kv("Cont diferențe favorabile", 765)
    d.gol()

    d.sectiune("7. Controale")
    d.check("Check FINAL: sold lei = sold valută × curs BNR",
            f"={rest_ini}+{dif2}-{rest_bnr}",
            f'=IF(ABS(B{d.r})<0.01,"OK — soldul în lei corespunde soldului în valută",'
            f'"EROARE — una dintre cele două diferențe de curs lipsește")')
    d.check("Check cele două momente sunt distincte",
            f"={dif1}+{dif2}",
            f'="Momentul 1 (la plată): " & TEXT({dif1},"0.00") & " lei · Momentul 2 '
            f'(reevaluare): " & TEXT({dif2},"0.00") & " lei"')
    d.check("Reminder: rata și dobânda vin din scadențar",
            f"={rata_val}+{dob_val}",
            f'="Extrasul arată deseori {rata_val}+{dob_val} cumulat. Dacă le înregistrezi '
            f'așa, ajungi cu 1621 pe debit sau cu sold rămas la finalul creditului."')
    d.check("Reminder: reevaluarea e LUNARĂ",
            f"={data_reeval}",
            '="Obligatorie lunar (OMFP 1802/2014), nu trimestrial. Verifică și soldul ÎN '
            'VALUTĂ, nu doar în lei."')
    d.check("Reminder bilanț",
            f"={rest_val}",
            '="Reclasifică porțiunea scadentă în ≤ 12 luni pentru bilanț, prin analitic sau '
            'cont dedicat. Dobânda calculată și neajunsă la scadență stă pe 1682."')
    d.gol()

    d.sectiune("8. Sufix generat")
    sufix = d.kv("Sufix", f'=" - " & {contract} & " - " & {luna}', tip="calc")

    # -------------------------------------------------------------------- Reguli
    g = F("Reguli_CREDIT_VALUTA", {"A": 24, "B": 34, "C": 16, "D": 34, "E": 20, "F": 54})
    g.titlu("MOD_CREDIT_VALUTA — Reguli (tabele fixe)")
    g.gol()
    g.sectiune("Tabel A — Cele două momente de diferență de curs")
    g.cap(["Moment", "Când apare", "Bază", "Formula", "Cont", "Temei / observație"])
    for row in [
        ("1. La plată", "la fiecare rambursare de rată",
         "rata în valută", "(curs plată − curs înregistrare) × rată", "665 / 765",
         "Diferența dintre cursul la care e înregistrată datoria și cel la care se stinge"),
        ("2. La reevaluare", "ultima zi bancară a FIECĂREI luni",
         "soldul rămas în valută", "(curs BNR − curs înregistrare) × sold rămas", "665 / 765",
         "OMFP 1802/2014 — obligatoriu lunar; „la 3 luni” e insuficient"),
    ]:
        g.rand(list(row))
    g.gol()

    g.sectiune("Tabel B — Ce se ia din scadențar, nu din extras")
    g.cap(["Element", "Cont", "", "", "", "De ce contează"])
    for row in [
        ("Rata de capital", "1621", "", "", "",
         "Stinge datoria. Dacă o umfli cu dobânda, 1621 ajunge pe debit"),
        ("Dobânda", "666", "", "", "",
         "Cheltuială financiară. Dacă o pui pe 1621, rămâi cu sold la finalul creditului"),
        ("Comisioane", "627", "", "", "",
         "Cheltuială cu serviciile bancare, separată de dobândă"),
        ("Dobânda neajunsă la scadență", "1682", "", "", "",
         "Se calculează, nu se plătește încă"),
    ]:
        g.rand(list(row))
    g.gol()

    g.sectiune("Tabel C — LIMITĂRI DECLARATE ale modulului")
    g.cap(["Ce NU tratează", "De ce", "Ce faci", "", "", "Efect dacă îl ignori"])
    for row in [
        ("Linii de credit revolving", "Soldul fluctuează în ambele sensuri în cursul lunii, "
         "deci nu există o „rată” unică.",
         "Reevaluează soldul la finalul lunii; tratează tragerile separat.", "", "",
         "Diferențele de curs pe trageri intermediare rămân neînregistrate"),
        ("Instrumente de acoperire a riscului valutar (hedging)",
         "Contabilitatea de acoperire are reguli proprii (OMFP 1802, cap. dedicat).",
         "Tratează separat; nu compensa în 665/765.", "", "",
         "Rezultatul financiar apare volatil fără motiv"),
        ("Credite cu dobândă variabilă recalculată retroactiv", "Recalculul schimbă "
         "scadențarul pe perioade deja înregistrate.",
         "Reia scadențarul nou și corectează perioadele afectate.", "", "",
         "Dobânda înregistrată nu corespunde cu cea datorată"),
        ("Costuri de tranzacție amortizate (metoda dobânzii efective)",
         "Comisioanele inițiale se pot amortiza pe durata creditului.",
         "Dacă politica firmei o cere, tratează prin 471.", "", "",
         "Cheltuiala e recunoscută integral în prima lună"),
    ]:
        g.rand(list(row))

    # ------------------------------------------------------------------- Jurnale
    j = F("Jurnale_CREDIT_VALUTA", {"A": 8, "B": 14, "C": 14, "D": 46, "E": 14, "F": 14,
                                    "G": 46})
    j.titlu("MOD_CREDIT_VALUTA — Jurnale (generate automat)")
    j.nota("Blocurile de diferență se activează după semn: nefavorabilă pe 665, favorabilă "
           "pe 765. Doar unul dintre ele are sumă.")
    j.gol()
    D = d.ref

    j.sectiune("Bloc 1 — Rata de capital și diferența la plată")
    j.kv("Data jurnal:", f"={D(data_plata)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b1 = j.r
    j.rand([1, f"={D(c_credit)}", f"={D(rata_ini)}",
            f'="Rambursare rată de capital" & {D(sufix)}',
            f"={D(c_banca_val)}", f"={D(rata_plata)}",
            f'="Plata ratei din contul în valută" & {D(sufix)}'])
    j.rand([2, f"={D(c_nefav)}", f"=MAX(0,{D(dif1)})",
            f'="Diferență de curs nefavorabilă la plată" & {D(sufix)}', None, None, None])
    j.rand([3, None, None, None, f"={D(c_fav)}", f"=MAX(0,-{D(dif1)})",
            f'="Diferență de curs favorabilă la plată" & {D(sufix)}'])
    sf1 = j.r - 1
    j.gol()
    j.check("Check Σ (structural)", f"=SUM(C{b1}:C{sf1})-SUM(F{b1}:F{sf1})",
            f'=IF(ABS(B{j.r})<0.01,"OK — nota se închide","EROARE")')
    j.check("Check exclusivitate 665/665", f"=IF(AND(C{b1+1}>0.005,F{b1+2}>0.005),1,0)",
            f'=IF(B{j.r}=0,"OK — o singură diferență, într-un singur sens",'
            f'"EROARE — 665 și 765 nu pot avea ambele sumă")')
    j.gol()

    j.sectiune("Bloc 2 — Dobânda")
    j.kv("Data jurnal:", f"={D(data_plata)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b2 = j.r
    j.rand([1, f"={D(c_dob)}", f"={D(dob_lei)}",
            f'="Dobândă aferentă creditului" & {D(sufix)}',
            f"={D(c_banca_val)}", f"={D(dob_lei)}",
            f'="Plata dobânzii din contul în valută" & {D(sufix)}'])
    j.gol()
    j.check("Check Σ (structural)", f"=C{b2}-F{b2}",
            f'=IF(ABS(B{j.r})<0.01,"OK — nota se închide","EROARE")')
    j.gol()

    j.sectiune("Bloc 3 — Comisioane bancare")
    j.kv("Data jurnal:", f"={D(data_plata)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b3 = j.r
    j.rand([1, f"={D(c_com)}", f"={D(comision)}",
            f'="Comisioane bancare aferente creditului" & {D(sufix)}',
            f"={D(c_banca_lei)}", f"={D(comision)}",
            f'="Plata comisioanelor" & {D(sufix)}'])
    j.gol()
    j.check("Check Σ (structural)", f"=C{b3}-F{b3}",
            f'=IF(ABS(B{j.r})<0.01,"OK — nota se închide","EROARE")')
    j.gol()

    j.sectiune("Bloc 4 — Reevaluarea soldului (PASUL CARE SE UITĂ)")
    j.kv("Data jurnal:", f"={D(data_reeval)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b4 = j.r
    j.rand([1, f"={D(c_nefav)}", f"=MAX(0,{D(dif2)})",
            f'="Reevaluare sold credit — diferență nefavorabilă" & {D(sufix)}',
            f"={D(c_credit)}", f"=MAX(0,{D(dif2)})",
            f'="Creșterea datoriei din reevaluare" & {D(sufix)}'])
    j.rand([2, f"={D(c_credit)}", f"=MAX(0,-{D(dif2)})",
            f'="Diminuarea datoriei din reevaluare" & {D(sufix)}',
            f"={D(c_fav)}", f"=MAX(0,-{D(dif2)})",
            f'="Reevaluare sold credit — diferență favorabilă" & {D(sufix)}'])
    sf4 = j.r - 1
    j.gol()
    j.check("Check Σ (structural)", f"=SUM(C{b4}:C{sf4})-SUM(F{b4}:F{sf4})",
            f'=IF(ABS(B{j.r})<0.01,"OK — nota se închide","EROARE")')
    j.check("Check sold final", f"={D(rest_bnr)}",
            f'="Sold 1621 după reevaluare = " & TEXT(B{j.r},"0.00") & " lei = " & '
            f'TEXT({D(rest_val)},"0") & " " & {D(valuta)} & " × " & TEXT({D(curs_bnr)},"0.0000")')
    j.gol()
    j.nota("Stare terminală: soldul lui 1621 în lei = soldul în valută × cursul BNR de la "
           "data reevaluării. Dacă nu ține, unul dintre cele două momente lipsește.")

    # ---------------------------------------------------------------- NotaExport
    n = F("NotaExport_CREDIT_VALUTA", {"A": 6, "B": 30, "C": 12, "D": 12, "E": 12, "F": 14,
                                       "G": 46, "H": 20, "I": 9})
    n.titlu("MOD_CREDIT_VALUTA — Notă pentru import (1 rând = 1 înregistrare)")
    n.nota("Filtrează pe Include = DA. Rândurile de diferență cu sumă zero ies singure.")
    n.gol()
    n.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    J = j.ref
    prima_n = n.r
    linii = ([("Bloc 1 — Rata + diferență", data_plata, r) for r in range(b1, sf1 + 1)]
             + [("Bloc 2 — Dobânda", data_plata, b2)]
             + [("Bloc 3 — Comisioane", data_plata, b3)]
             + [("Bloc 4 — Reevaluare", data_reeval, r) for r in range(b4, sf4 + 1)])
    for i, (bloc, data, r) in enumerate(linii, start=1):
        rn = n.r
        n.rand([i, bloc, f"={D(data)}", f"={J(f'B{r}')}", f"={J(f'E{r}')}",
                f"=MAX(N({J(f'C{r}')}),N({J(f'F{r}')}))", f"={J(f'D{r}')}",
                "Scadențar + extras", f'=IF(N(F{rn})>0.005,"DA","NU")'])
    ultim_n = n.r - 1
    n.gol()
    n.kv("Rânduri de importat (Include=DA)", f'=COUNTIF(I{prima_n}:I{ultim_n},"DA")',
         tip="calc")
