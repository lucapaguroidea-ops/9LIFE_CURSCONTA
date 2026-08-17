"""MOD_LEASING_FIN — leasing financiar autoturism, cu regimul fiscal complet.

Acoperă F-50. Trece din „EXEMPLU EXTERN” în IMPLEMENTAT.

Aici sunt concentrate cele TREI limitări fiscale ale autoturismelor, care se aplică
simultan dar pe BAZE DIFERITE — motivul pentru care modulul e cel mai greu din set:

  1. TVA deductibilă 50%              — art. 298 CF, pe TVA de pe toate facturile
  2. Cheltuieli deductibile 50%       — art. 25 alin. (3) lit. l) CF, pe dobânzi,
                                        comisioane, asigurări, diferențe de curs,
                                        INCLUSIV TVA nedeductibilă trecută pe cheltuială
  3. Amortizare max. 1.500 lei/lună   — art. 28 alin. (14) CF

⚠ Amortizarea NU intră sub limitarea de 50% — are propria plafonare. Cele două nu
se cumulează. Aceasta era piesa lipsă din notițele brute, cu cel mai mare impact
pe impozitul pe profit.

Cifrele implicite sunt exact cele din monografia revizuită a trainingului 2, ca
modulul să poată fi verificat contra ei.
"""

COD = "MOD_LEASING_FIN"

CATALOG = dict(
    fluxuri="F-50",
    tip="Pe contract + lunar",
    variabile="Valoare contract, avans, rată, dobândă, comision, CASCO, regim vehicul, durată",
    porti="MIXT 50% / EXCLUSIV 100% / EXCEPTAT; capitalizare vs. cheltuială pentru TVA nededusă",
    blocuri="B1 Avans; B2 TVA avans; B3 Intrare + 167; B4 Stingere avans; "
            "B5 Factura lunară; B6 Corecție TVA 50%; B7 Limitare 50% cheltuieli; B8 Amortizare",
)


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_LEASING_FIN", {"A": 52, "B": 22, "C": 62})
    d.titlu("MOD_LEASING_FIN — Declarații (input)")
    d.nota("Valorile implicite reproduc monografia din trainingul 07.08.2026 "
           "(contract 150.000, avans 50.000, rată 2.000, dobândă 500, comision 100, CASCO 20).")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    contract = d.kv("Număr contract de leasing", "LF-2026-001",
                    nota="167 este 1-la-1 cu contractul (C-19)")
    luna = d.kv("Luna", "2026-07")
    data_av = d.kv("Data facturii de avans", "2026-07-01")
    data_rec = d.kv("Data recepției bunului", "2026-07-10")
    data_rata = d.kv("Data facturii lunare", "2026-07-31")
    d.gol()

    d.sectiune("2. Contract")
    valoare = d.kv("Valoare de intrare din contract (fără TVA)", 150000)
    avans = d.kv("Avans (fără TVA)", 50000)
    durata = d.kv("Durata de amortizare (luni)", 60)
    cota = d.kv("Cotă TVA", "=Parametri!B10", tip="calc")
    d.gol()

    d.sectiune("3. Regim fiscal al vehiculului")
    regim = d.kv("Regim (MIXT / EXCLUSIV / EXCEPTAT)", "MIXT",
                 nota="MIXT = 50%. EXCLUSIV/EXCEPTAT = 100%, dar cere documentație "
                      "(foi de parcurs, decizie internă)")
    proc = d.kv("Procent de deducere aplicat",
                f'=IF({regim}="MIXT",{P["proc_vehicul"]},1)', tip="calc")
    capitalizare = d.kv("TVA nededusă pe rata de capital: CAPITALIZEAZA / CHELTUIALA",
                        "CAPITALIZEAZA",
                        nota="❓ De clarificat cu formatorul — practica e împărțită. "
                             "Capitalizarea e coerentă cu tratamentul avansului (pct. 75 OMFP 1802)")
    d.gol()

    d.sectiune("4. Factura lunară de leasing")
    rata = d.kv("Rata de capital", 2000)
    dobanda = d.kv("Dobândă", 500)
    comision = d.kv("Comision de administrare", 100)
    casco = d.kv("CASCO (fără TVA)", 20)
    d.gol()

    d.sectiune("5. Calcul — intrarea bunului (nu edita)")
    tva_avans = d.kv("TVA pe avans", f"={avans}*{cota}", tip="calc")
    tva_av_ned = d.kv("TVA nedeductibilă pe avans (capitalizată)",
                      f"=ROUND({tva_avans}*(1-{proc}),2)", tip="calc")
    cost = d.kv("Valoare de intrare a mijlocului fix",
                f"={valoare}+{tva_av_ned}", tip="calc",
                nota="150.000 + 5.250 = 155.250 în exemplul din training")
    amo_cont = d.kv("Amortizare contabilă lunară", f"=ROUND({cost}/{durata},2)", tip="calc")
    amo_fisc = d.kv("Amortizare deductibilă fiscal",
                    f"=MIN({amo_cont},{P['plafon_amo_auto']})", tip="calc",
                    nota="Plafon 1.500 lei/lună, art. 28 alin. (14) CF")
    amo_ned = d.kv("Amortizare NEdeductibilă lunară", f"={amo_cont}-{amo_fisc}", tip="calc")
    d.gol()

    d.sectiune("6. Calcul — factura lunară (nu edita)")
    tva_rata = d.kv("TVA pe rata de capital", f"={rata}*{cota}", tip="calc")
    tva_dob = d.kv("TVA pe dobândă", f"={dobanda}*{cota}", tip="calc")
    tva_com = d.kv("TVA pe comision", f"={comision}*{cota}", tip="calc")
    tva_tot = d.kv("TVA total pe factură", f"={tva_rata}+{tva_dob}+{tva_com}", tip="calc",
                   nota="CASCO e fără TVA")
    total_f = d.kv("Total factură",
                   f"={rata}+{dobanda}+{comision}+{casco}+{tva_tot}", tip="calc")
    d.gol()

    d.sectiune("7. Calcul — corecția TVA nedeductibilă (limitarea 1)")
    ned_rata = d.kv("TVA nededusă — rată", f"=ROUND({tva_rata}*(1-{proc}),2)", tip="calc")
    ned_dob = d.kv("TVA nededusă — dobândă", f"=ROUND({tva_dob}*(1-{proc}),2)", tip="calc")
    ned_com = d.kv("TVA nededusă — comision", f"=ROUND({tva_com}*(1-{proc}),2)", tip="calc")
    ned_tot = d.kv("TVA nededusă total", f"={ned_rata}+{ned_dob}+{ned_com}", tip="calc")
    d.gol()

    d.sectiune("8. Calcul — limitarea de 50% a cheltuielilor (limitarea 2)")
    d.nota("Baza include TVA nedeductibilă deja trecută pe cheltuială. "
           "Amortizarea NU intră aici — are propria plafonare (limitarea 3).")
    baza_dob = d.kv("Bază dobândă (dobândă + TVA nededusă)",
                    f"={dobanda}+{ned_dob}", tip="calc")
    baza_com = d.kv("Bază comision (comision + TVA nededusă)",
                    f"={comision}+{ned_com}", tip="calc")
    baza_casco = d.kv("Bază CASCO", f"={casco}", tip="calc")
    ch_dob = d.kv("Dobândă nedeductibilă", f"=ROUND({baza_dob}*(1-{proc}),2)", tip="calc")
    ch_com = d.kv("Comision nedeductibil", f"=ROUND({baza_com}*(1-{proc}),2)", tip="calc")
    ch_casco = d.kv("CASCO nedeductibil", f"=ROUND({baza_casco}*(1-{proc}),2)", tip="calc")
    d.gol()

    d.sectiune("9. Controale")
    d.check("Check valoare de intrare",
            f"={cost}",
            f'=IF({regim}="MIXT",IF(ABS({cost}-({valoare}+{tva_avans}*0.5))<0.01,'
            f'"OK — include TVA nedeductibilă pe avans","EROARE"),'
            f'"OK — regim cu deducere integrală, fără TVA capitalizată")')
    d.check("Check cele trei limitări",
            f"={amo_ned}+{ned_tot}+{ch_dob}+{ch_com}+{ch_casco}",
            f'="Nedeductibil lunar total: " & TEXT({amo_ned}+{ch_dob}+{ch_com}+{ch_casco},'
            f'"0.00") & " lei (din care amortizare " & TEXT({amo_ned},"0.00") & ")"')
    d.check("Check plafon amortizare",
            f"={amo_cont}",
            f'=IF({amo_cont}>{P["plafon_amo_auto"]},'
            f'"ATENȚIE — amortizarea contabilă depășește plafonul de 1.500 lei/lună; '
            f'diferența e nedeductibilă","OK — sub plafon")')
    d.check("Reminder: amortizarea NU se limitează cu 50%",
            '="regulă"',
            '="Amortizarea are propria plafonare (1.500 lei/lună). Nu se aplică și 50% peste ea — '
            'ar fi dublă limitare."')
    d.check("Reminder impozit local",
            f"={contract}",
            '="Declarație la primărie în 30 de zile. La leasing financiar, impozitul pe mijlocul de '
            'transport e datorat de LOCATAR pe toată durata contractului."')
    d.gol()

    d.sectiune("10. Conturi")
    c_avans = d.kv("Cont avans imobilizări", 4093)
    c_mf = d.kv("Cont mijloc fix", 2133)
    c_amo_c = d.kv("Cont amortizare", 2813)
    c_167 = d.kv("Cont datorie leasing (analitic pe contract)", "167.LF-2026-001")
    c_furn = d.kv("Cont furnizor de imobilizări", 404)
    c_4426 = d.kv("Cont TVA deductibilă", 4426)
    c_dob = d.kv("Cont dobândă", 666)
    c_com = d.kv("Cont comision", 628, nota="Poate fi și 627 — fii consecvent cu politica firmei")
    c_casco = d.kv("Cont primă de asigurare", 613)
    c_dob_n = d.kv("Cont dobândă nedeductibilă", "666.NED")
    c_com_n = d.kv("Cont comision nedeductibil", "628.NED")
    c_casco_n = d.kv("Cont CASCO nedeductibil", "613.NED",
                     nota="⚠ NU 615 — acela e cheltuieli cu pregătirea personalului")
    c_tva_ned = d.kv("Cont cheltuială pentru TVA nededusă pe rată", 6588)
    c_chelt_amo = d.kv("Cont cheltuială cu amortizarea", 6811)
    d.gol()

    d.sectiune("11. Sufix generat")
    sufix = d.kv("Sufix", f'="— leasing " & {contract} & " " & {luna}', tip="calc")
    d.gol()
    d.kv("Modul activ în CatalogModule?",
         '=IF(INDEX(CatalogModule!A:A,MATCH("MOD_LEASING_FIN",CatalogModule!B:B,0))="DA",'
         '"ACTIV — jurnalele se generează","INACTIV — jurnalele rămân goale")', tip="calc")

    # -------------------------------------------------------------------- Reguli
    g = F("Reguli_LEASING_FIN", {"A": 10, "B": 18, "C": 18, "D": 36, "E": 26, "F": 60})
    g.titlu("MOD_LEASING_FIN — Reguli (tabele fixe)")
    g.nota("Se editează doar când se schimbă legea.")
    g.gol()
    g.sectiune("Tabel A — Cele trei limitări fiscale (se aplică simultan, pe baze diferite)")
    g.cap(["#", "Limitare", "Bază de aplicare", "Procent / plafon", "Temei", "Observație"])
    for row in [
        ("1", "TVA deductibilă", "TVA de pe TOATE facturile aferente vehiculului", "50%",
         "art. 298 CF", "Inclusiv avansul și factura lunară"),
        ("2", "Cheltuieli deductibile",
         "combustibil, întreținere, piese, chirii, asigurări, dobânzi, comisioane, "
         "diferențe de curs, INCLUSIV TVA nedeductibilă trecută pe cheltuială", "50%",
         "art. 25 alin. (3) lit. l) CF",
         "Deductibilitate limitată la UN SINGUR autoturism per persoană cu funcție de conducere "
         "(art. 25 alin. 3 lit. m)"),
        ("3", "Amortizare", "amortizarea contabilă a fiecărui autoturism", "max. 1.500 lei/lună",
         "art. 28 alin. (14) CF",
         "⚠ NU intră sub limitarea de 50% — cele două nu se cumulează"),
    ]:
        g.rand(list(row))
    g.gol()
    g.sectiune("Tabel B — Operațional vs. financiar")
    g.cap(["Criteriu", "Operațional", "Financiar", "", "", "Observație"])
    for row in [
        ("Bunul în bilanț", "NU — rămâne la locator", "DA — 2133", "", "", ""),
        ("Datoria", "nu se înregistrează", "167", "", "", "167 e 1:1 cu contractul (C-19)"),
        ("Cheltuiala lunară", "612 chirie", "666 dobândă + amortizare", "", "", ""),
        ("Evidență extrabilanțieră", "8036", "—", "", "", ""),
        ("Impozit local", "plătit de locator", "plătit de LOCATAR, pe toată durata", "", "",
         "Declarație la primărie în 30 de zile"),
        ("Valoarea reziduală", "achiziție nouă la final", "deja capitalizată", "", "",
         "La operațional, mijlocul fix apare abia la final"),
    ]:
        g.rand(list(row))
    g.gol()
    g.sectiune("Tabel C — Excepții de la regimul de 50%")
    for t in [
        "Urgență / pază / curierat · agenți de vânzări și achiziții · taxi · închiriere · "
        "școli de șoferi · transport de persoane cu plată.",
        "Fără documentație (foi de parcurs, decizie internă), regimul prudent și conform este MIXT (50%).",
    ]:
        g.rand([t])
    g.gol()
    g.sectiune("Tabel D — Porți de calitate")
    for t in [
        "• ΣDr = ΣCr pe fiecare bloc",
        "• Valoarea de intrare include TVA nedeductibilă pe avans (taxe nerecuperabile în cost)",
        "• Sold 167 pe contract = sold din scadențar, în valuta contractului (C-19)",
        "• Avansul 4093 se închide integral în 167 la recepție",
        "• Amortizarea contabilă se calculează pe valoarea de intrare COMPLETĂ, nu pe cea din contract",
        "• Nedeductibilul lunar = amortizare peste plafon + 50% din dobândă/comision/CASCO",
        "• Verifică rata de schimb de pe factură față de scadențar (altfel reevaluarea e greșită)",
    ]:
        g.rand([t])

    # ------------------------------------------------------------------- Jurnale
    j = F("Jurnale_LEASING_FIN", {"A": 8, "B": 16, "C": 14, "D": 50, "E": 16, "F": 14, "G": 50})
    j.titlu("MOD_LEASING_FIN — Jurnale (generate automat)")
    j.nota("Blocurile 1–4 se rulează o singură dată, la deschiderea contractului. "
           "Blocurile 5–8 se rulează lunar.")
    j.gol()
    D = d.ref

    j.sectiune("Bloc 1 — Factura de avans")
    j.kv("Data jurnal:", f"={D(data_av)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b1a = j.rand([1, f"={D(c_avans)}", f"={D(avans)}",
                  f'="Avans leasing " & {D(sufix)}',
                  f"={D(c_furn)}", f"={D(avans)}",
                  f'="Datorie societate de leasing — avans " & {D(sufix)}'])
    b1b = j.rand([2, f"={D(c_4426)}", f"={D(tva_avans)}",
                  f'="TVA pe avans " & {D(sufix)}',
                  f"={D(c_furn)}", f"={D(tva_avans)}",
                  f'="Datorie — TVA avans " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 2 — TVA nedeductibilă pe avans, capitalizată")
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b2 = j.rand([1, f"={D(c_mf)}", f"={D(tva_av_ned)}",
                 f'="TVA nedeductibilă capitalizată în cost " & {D(sufix)}',
                 f"={D(c_4426)}", f"={D(tva_av_ned)}",
                 f'="Stingere TVA nedeductibilă " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 3 — Recepția bunului și nașterea datoriei")
    j.kv("Data jurnal:", f"={D(data_rec)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b3 = j.rand([1, f"={D(c_mf)}", f"={D(valoare)}",
                 f'="Intrare autoturism în patrimoniu " & {D(sufix)}',
                 f"={D(c_167)}", f"={D(valoare)}",
                 f'="Datorie leasing financiar " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 4 — Închiderea avansului")
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b4 = j.rand([1, f"={D(c_167)}", f"={D(avans)}",
                 f'="Închidere avans în datoria de leasing " & {D(sufix)}',
                 f"={D(c_avans)}", f"={D(avans)}",
                 f'="Stingere avans 4093 " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 5 — Factura lunară de leasing (la valoarea ei, fără split)")
    j.kv("Data jurnal:", f"={D(data_rata)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b5a = j.rand([1, f"={D(c_167)}", f"={D(rata)}",
                  f'="Rata de capital " & {D(sufix)}',
                  f"={D(c_furn)}", f"={D(rata)}", f'="Factura lunară — capital " & {D(sufix)}'])
    b5b = j.rand([2, f"={D(c_dob)}", f"={D(dobanda)}",
                  f'="Dobândă de leasing " & {D(sufix)}',
                  f"={D(c_furn)}", f"={D(dobanda)}", f'="Factura lunară — dobândă " & {D(sufix)}'])
    b5c = j.rand([3, f"={D(c_com)}", f"={D(comision)}",
                  f'="Comision de administrare " & {D(sufix)}',
                  f"={D(c_furn)}", f"={D(comision)}", f'="Factura lunară — comision " & {D(sufix)}'])
    b5d = j.rand([4, f"={D(c_casco)}", f"={D(casco)}",
                  f'="Primă CASCO " & {D(sufix)}',
                  f"={D(c_furn)}", f"={D(casco)}", f'="Factura lunară — CASCO " & {D(sufix)}'])
    b5e = j.rand([5, f"={D(c_4426)}", f"={D(tva_tot)}",
                  f'="TVA pe factura de leasing " & {D(sufix)}',
                  f"={D(c_furn)}", f"={D(tva_tot)}", f'="Factura lunară — TVA " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 6 — Corecția TVA nedeductibilă (limitarea 1: 50%)")
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    dest_rata = f'IF({D(capitalizare)}="CAPITALIZEAZA",{D(c_mf)},{D(c_tva_ned)})'
    b6a = j.rand([1, f"={dest_rata}", f"={D(ned_rata)}",
                  f'="TVA nededusă pe rata de capital — " & '
                  f'IF({D(capitalizare)}="CAPITALIZEAZA","capitalizată","pe cheltuială") & '
                  f'" " & {D(sufix)}',
                  f"={D(c_4426)}", f"={D(ned_rata)}",
                  f'="Stingere TVA nededusă — rată " & {D(sufix)}'])
    b6b = j.rand([2, f"={D(c_dob)}", f"={D(ned_dob)}",
                  f'="TVA nededusă pe dobândă " & {D(sufix)}',
                  f"={D(c_4426)}", f"={D(ned_dob)}",
                  f'="Stingere TVA nededusă — dobândă " & {D(sufix)}'])
    b6c = j.rand([3, f"={D(c_com)}", f"={D(ned_com)}",
                  f'="TVA nededusă pe comision " & {D(sufix)}',
                  f"={D(c_4426)}", f"={D(ned_com)}",
                  f'="Stingere TVA nededusă — comision " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 7 — Limitarea de 50% a cheltuielilor (limitarea 2)")
    j.nota("Reclasificare pe analitice nedeductibile. Amortizarea NU apare aici.")
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b7a = j.rand([1, f"={D(c_dob_n)}", f"={D(ch_dob)}",
                  f'="Dobândă nedeductibilă 50% " & {D(sufix)}',
                  f"={D(c_dob)}", f"={D(ch_dob)}",
                  f'="Reclasificare din 666 " & {D(sufix)}'])
    b7b = j.rand([2, f"={D(c_com_n)}", f"={D(ch_com)}",
                  f'="Comision nedeductibil 50% " & {D(sufix)}',
                  f"={D(c_com)}", f"={D(ch_com)}",
                  f'="Reclasificare din 628 " & {D(sufix)}'])
    b7c = j.rand([3, f"={D(c_casco_n)}", f"={D(ch_casco)}",
                  f'="CASCO nedeductibil 50% " & {D(sufix)}',
                  f"={D(c_casco)}", f"={D(ch_casco)}",
                  f'="Reclasificare din 613 (NU 615) " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 8 — Amortizarea lunară (limitarea 3: plafon 1.500 lei/lună)")
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b8 = j.rand([1, f"={D(c_chelt_amo)}", f"={D(amo_cont)}",
                 f'="Amortizare contabilă (din care nedeductibil " & '
                 f'TEXT({D(amo_ned)},"0.00") & " lei) " & {D(sufix)}',
                 f"={D(c_amo_c)}", f"={D(amo_cont)}",
                 f'="Amortizare cumulată " & {D(sufix)}'])
    j.gol()

    j.sectiune("Sumar și controale")
    grupuri = (b1a, b1b, b2, b3, b4, b5a, b5b, b5c, b5d, b5e,
               b6a, b6b, b6c, b7a, b7b, b7c, b8)
    tdr = j.kv("Total Dr", "=" + "+".join(x["C"] for x in grupuri), tip="calc")
    tcr = j.kv("Total Cr", "=" + "+".join(x["F"] for x in grupuri), tip="calc")
    j.check("Check Σ (structural)", f"={tdr}-{tcr}",
            f'=IF(ABS({tdr}-{tcr})<0.01,"OK — notele se închid","EROARE")')
    j.check("Check valoare de intrare a mijlocului fix",
            f"={b2['C']}+{b3['C']}-{D(cost)}",
            f'=IF(ABS({b2["C"]}+{b3["C"]}-{D(cost)})<0.01,'
            f'"OK — 2133 = valoare contract + TVA nedeductibilă pe avans","EROARE")')
    j.check("Check stingere avans (C-19)",
            f"={b1a['C']}-{b4['C']}",
            f'=IF(ABS({b1a["C"]}-{b4["C"]})<0.01,"OK — 4093 se închide integral în 167",'
            f'"EROARE — avansul rămâne cu sold")')
    j.check("Check TVA de pe factura lunară",
            f"={b6a['C']}+{b6b['C']}+{b6c['C']}-{D(ned_tot)}",
            f'=IF(ABS({b6a["C"]}+{b6b["C"]}+{b6c["C"]}-{D(ned_tot)})<0.01,'
            f'"OK — corecția acoperă exact TVA nedeductibilă","EROARE")')
    j.check("Check limitarea 2 nu atinge amortizarea",
            f"={b8['C']}",
            f'=IF(ABS({b7a["C"]}+{b7b["C"]}+{b7c["C"]})<{b8["C"]},'
            f'"OK — amortizarea are propria plafonare, nu se limitează cu 50%",'
            f'"VERIFICĂ — sume neobișnuite")')
    j.check("Nedeductibil lunar total (informativ)",
            f"={D(amo_ned)}+{b7a['C']}+{b7b['C']}+{b7c['C']}",
            f'="Din care amortizare peste plafon: " & TEXT({D(amo_ned)},"0.00") & " lei"')
    j.nota("Stare terminală așteptată: sold 4093 = 0; sold 167 pe contract = soldul din scadențar; "
           "2133 = valoarea de intrare completă; nedeductibilul lunar urmărit pentru D101.")

    # ---------------------------------------------------------------- NotaExport
    n = F("NotaExport_LEASING_FIN", {"A": 6, "B": 36, "C": 12, "D": 16, "E": 16, "F": 14,
                                     "G": 52, "H": 30, "I": 10})
    n.titlu("MOD_LEASING_FIN — Notă pentru import (1 rând = 1 înregistrare)")
    n.nota("Blocurile 1–4 se importă o singură dată, la deschiderea contractului. "
           "Blocurile 5–8, lunar. Filtrează pe Include = DA.")
    n.gol()
    n.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document", "Include"])
    J = j.ref
    linii = [
        ("Bloc 1 — Avans", data_av, b1a, "Factură de avans"),
        ("Bloc 1 — TVA avans", data_av, b1b, "Factură de avans"),
        ("Bloc 2 — TVA nededusă capitalizată", data_av, b2, "Notă contabilă"),
        ("Bloc 3 — Intrare + 167", data_rec, b3, "Proces-verbal de recepție"),
        ("Bloc 4 — Stingere avans", data_rec, b4, "Notă contabilă"),
        ("Bloc 5 — Rata de capital", data_rata, b5a, "Factură lunară"),
        ("Bloc 5 — Dobândă", data_rata, b5b, "Factură lunară"),
        ("Bloc 5 — Comision", data_rata, b5c, "Factură lunară"),
        ("Bloc 5 — CASCO", data_rata, b5d, "Factură lunară"),
        ("Bloc 5 — TVA", data_rata, b5e, "Factură lunară"),
        ("Bloc 6 — TVA nededusă rată", data_rata, b6a, "Notă contabilă"),
        ("Bloc 6 — TVA nededusă dobândă", data_rata, b6b, "Notă contabilă"),
        ("Bloc 6 — TVA nededusă comision", data_rata, b6c, "Notă contabilă"),
        ("Bloc 7 — Dobândă nedeductibilă", data_rata, b7a, "Notă contabilă"),
        ("Bloc 7 — Comision nedeductibil", data_rata, b7b, "Notă contabilă"),
        ("Bloc 7 — CASCO nedeductibil", data_rata, b7c, "Notă contabilă"),
        ("Bloc 8 — Amortizare", data_rata, b8, "Notă de amortizare"),
    ]
    refs = []
    for i, (bloc, data_ref, b, doc) in enumerate(linii, start=1):
        r = n.rand([i, bloc, f"={D(data_ref)}", f"={J(b['B'])}", f"={J(b['E'])}",
                    f"={J(b['C'])}", f"={J(b['D'])}", doc, None])
        n.ws.cell(row=n.r - 1, column=9, value=f'=IF({r["F"]}>0.001,"DA","NU")')
        refs.append(r["F"])
    n.gol()
    n.kv("Rânduri de importat (Include=DA)",
         f'=COUNTIF({refs[0].replace("F", "I")}:{refs[-1].replace("F", "I")},"DA")', tip="calc")
    n.check("Check global (trebuie 0)", f"={J(tdr)}-{J(tcr)}",
            f'=IF(ABS({J(tdr)}-{J(tcr)})<0.01,"OK","EROARE")')
