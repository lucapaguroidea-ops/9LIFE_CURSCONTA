"""MOD_IESIRE_MF — vânzarea sau casarea unui mijloc fix.

Acoperă F-59 și F-60.

Particularitatea modulului este testul de deductibilitate: cheltuiala cu valoarea
rămasă neamortizată este deductibilă în limita venitului din vânzare, iar diferența
rămâne nedeductibilă dacă prețul nu e documentat. Modulul calculează diferența și
cere explicit documentul justificativ — nu o trece tăcut pe deductibil.
"""

COD = "MOD_IESIRE_MF"

CATALOG = dict(
    fluxuri="F-59, F-60",
    tip="Pe eveniment de ieșire",
    variabile="Valoare de intrare, amortizare cumulată, preț de vânzare, tip ieșire, documente",
    porti="Test deductibilitate (valoare rămasă vs. venit); documentarea prețului",
    blocuri="B1 Descărcare amortizare; B2 Valoare rămasă; B3 Vânzare; B4 Piese recuperate",
)


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_IESIRE_MF", {"A": 48, "B": 22, "C": 60})
    d.titlu("MOD_IESIRE_MF — Declarații (input)")
    d.nota("Completează doar celulele galbene. Tipul ieșirii (VANZARE / CASARE) comandă blocurile.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    denumire = d.kv("Denumire mijloc fix", "Clădire administrativă")
    data_i = d.kv("Data ieșirii", "2026-07-31")
    tip = d.kv("Tip ieșire (VANZARE / CASARE)", "VANZARE")
    d.gol()

    d.sectiune("2. Date din evidență")
    intrare = d.kv("Valoare de intrare (sold 21x)", 100000)
    amortizat = d.kv("Amortizare cumulată (sold 28x)", 30000)
    pret = d.kv("Preț de vânzare, fără TVA (0 la casare)", 50000)
    cota = d.kv("Cotă TVA", "=Parametri!B10", tip="calc")
    piese = d.kv("Valoare piese recuperate din casare", 0,
                 nota="Evaluate de comisia tehnică, pe listă")
    documentat = d.kv("Prețul este documentat? (DA / NU)", "NU",
                      nota="Raport de evaluare / referință de piață / deviz de service")
    d.gol()

    d.sectiune("3. Calcul automat (nu edita)")
    ramasa = d.kv("Valoare rămasă neamortizată", f"={intrare}-{amortizat}", tip="calc")
    tva = d.kv("TVA colectată", f"={pret}*{cota}", tip="calc")
    total = d.kv("Total de încasat", f"={pret}+{tva}", tip="calc")
    ded = d.kv("Cheltuială deductibilă (în limita venitului)",
               f"=MIN({ramasa},{pret})", tip="calc")
    neded = d.kv("Cheltuială NEdeductibilă", f"=MAX(0,{ramasa}-{pret})", tip="calc")
    rezultat = d.kv("Rezultat din cedare (venit − valoare rămasă)",
                    f"={pret}-{ramasa}", tip="calc")
    d.gol()

    d.sectiune("4. Controale")
    d.check("Check C-13: amortizarea nu poate depăși valoarea de intrare",
            f"={intrare}-{amortizat}",
            f'=IF({amortizat}<={intrare}+0.001,"OK — 28x ≤ 21x",'
            f'"EROARE — amortizare mai mare decât valoarea de intrare")')
    d.check("Test deductibilitate",
            f"={neded}",
            f'=IF({neded}<0.001,"OK — valoarea rămasă e integral acoperită de venit",'
            f'IF({documentat}="DA","ATENȚIE — diferență nedeductibilă, dar prețul e documentat: '
            f'susține poziția în scris","RISC — vânzare sub valoarea rămasă, fără document. '
            f'Comunică riscul clientului ÎN SCRIS"))')
    d.check("Test preț minim",
            f"={pret}",
            f'=IF({documentat}="DA","OK — preț documentat",'
            f'"ATENȚIE — reperul minim e valoarea de piață (Autovit/OLX) sau valoarea de fier vechi; '
            f'nu se vinde cu 100 EUR doar pentru că e amortizat")')
    d.check("Reminder modul de imobilizări",
            f"={tip}",
            f'="Schimbă STAREA mijlocului fix în modul: " & IF({tip}="VANZARE","vândut","casat") & '
            f'" — altfel softul continuă să calculeze amortizare"')
    d.gol()

    d.sectiune("5. Conturi")
    c_imo = d.kv("Cont imobilizare (21x)", "212")
    c_amo = d.kv("Cont amortizare (28x)", "2812")
    c_chelt = d.kv("Cont cheltuială din cedare", 6583)
    c_venit = d.kv("Cont venit din cedare", 7583)
    c_client = d.kv("Cont creanță", "461")
    c_4427 = d.kv("Cont TVA colectată", 4427)
    c_stoc = d.kv("Cont stoc piese recuperate", 3024)
    c_venit_alt = d.kv("Cont venit din piese recuperate", 7588)
    d.gol()

    d.sectiune("6. Sufix generat")
    sufix = d.kv("Sufix", f'="— " & {denumire} & " " & {data_i}', tip="calc")
    d.gol()
    d.kv("Modul activ în CatalogModule?",
         '=IF(INDEX(CatalogModule!A:A,MATCH("MOD_IESIRE_MF",CatalogModule!B:B,0))="DA",'
         '"ACTIV — jurnalele se generează","INACTIV — jurnalele rămân goale")', tip="calc")

    # -------------------------------------------------------------------- Reguli
    g = F("Reguli_IESIRE_MF", {"A": 10, "B": 16, "C": 16, "D": 34, "E": 26, "F": 58})
    g.titlu("MOD_IESIRE_MF — Reguli (tabele fixe)")
    g.nota("Se editează doar când se schimbă legea sau practica documentată a cabinetului.")
    g.gol()
    g.sectiune("Tabel A — Secvența de ieșire")
    g.cap(["Pas", "Cont Dr", "Cont Cr", "Sumă (sursă)", "Condiție", "Temei / observație"])
    for row in [
        ("1", "28x", "21x", "amortizarea cumulată", "Întotdeauna",
         "28x e pur rectificativ — nu ține nimic real"),
        ("2", "6583", "21x", "valoarea rămasă neamortizată", "Dacă valoarea rămasă > 0",
         "La bun integral amortizat, pasul lipsește"),
        ("3", "461/411", "7583 + 4427", "preț + TVA", "Doar la VANZARE",
         "La casare nu există venit din cedare"),
        ("4", "3024", "7588", "valoarea pieselor recuperate", "Doar la CASARE cu recuperări",
         "Lista vine de la comisia tehnică; dacă se revând, transfer în 371 (F-10)"),
    ]:
        g.rand(list(row))
    g.gol()
    g.sectiune("Tabel B — Testul de deductibilitate")
    g.cap(["Situație", "Tratament", "", "", "", "Observație"])
    for row in [
        ("Preț ≥ valoarea rămasă", "6583 integral deductibil", "", "", "",
         "Rezultatul din cedare e câștig"),
        ("Preț < valoarea rămasă, preț DOCUMENTAT",
         "deductibil în limita venitului; diferența e discutabilă", "", "", "",
         "❓ De cerut formatorului baza legală exactă. Art. 28 alin. (17) CF, citit strict, "
         "include pierderea în rezultatul fiscal"),
        ("Preț < valoarea rămasă, preț NEdocumentat",
         "diferența — nedeductibilă; risc de reîncadrare", "", "", "",
         "art. 11 CF (reîncadrare) + art. 25 alin. (1) CF (scopul activității economice)"),
        ("Bun integral amortizat, vândut sub piață", "risc de reîncadrare", "", "", "",
         "Reper minim: valoare de piață sau valoare de fier vechi, documentat"),
    ]:
        g.rand(list(row))
    g.gol()
    g.sectiune("Tabel C — Porți de calitate")
    for t in [
        "• ΣDr = ΣCr pe fiecare bloc",
        "• Sold 21x = 0 și sold 28x = 0 pentru bunul ieșit",
        "• Amortizarea descărcată = soldul 28x din evidență, nu o estimare (C-13)",
        "• Starea mijlocului fix schimbată în modul: vândut / casat",
        "• Ieșirea din nota contabilă corelată cu modulul de imobilizări (C-15)",
        "• Diferența nedeductibilă comunicată clientului în scris",
    ]:
        g.rand([t])

    # ------------------------------------------------------------------- Jurnale
    j = F("Jurnale_IESIRE_MF", {"A": 8, "B": 14, "C": 14, "D": 48, "E": 14, "F": 14, "G": 48})
    j.titlu("MOD_IESIRE_MF — Jurnale (generate automat)")
    j.nota("Blocul de vânzare rămâne pe zero la casare, și invers pentru piesele recuperate.")
    j.gol()
    D = d.ref

    j.sectiune("Bloc 1 — Descărcarea amortizării cumulate")
    j.kv("Data jurnal:", f"={D(data_i)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b1 = j.rand([1, f"={D(c_amo)}", f"={D(amortizat)}",
                 f'="Descărcare amortizare cumulată " & {D(sufix)}',
                 f"={D(c_imo)}", f"={D(amortizat)}",
                 f'="Scoatere din evidență — partea amortizată " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 2 — Valoarea rămasă pe cheltuială")
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b2 = j.rand([1, f"={D(c_chelt)}", f"={D(ramasa)}",
                 f'="Valoare rămasă neamortizată " & {D(sufix)}',
                 f"={D(c_imo)}", f"={D(ramasa)}",
                 f'="Scoatere din evidență — partea neamortizată " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 3 — Vânzarea (doar la tip = VANZARE)")
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b3a = j.rand([1, f"={D(c_client)}", f'=IF({D(tip)}="VANZARE",{D(pret)},0)',
                  f'="Creanță din vânzare mijloc fix " & {D(sufix)}',
                  f"={D(c_venit)}", f'=IF({D(tip)}="VANZARE",{D(pret)},0)',
                  f'="Venit din cedarea activelor " & {D(sufix)}'])
    b3b = j.rand([2, f"={D(c_client)}", f'=IF({D(tip)}="VANZARE",{D(tva)},0)',
                  f'="Creanță — TVA " & {D(sufix)}',
                  f"={D(c_4427)}", f'=IF({D(tip)}="VANZARE",{D(tva)},0)',
                  f'="TVA colectată " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 4 — Piese recuperate din casare")
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b4 = j.rand([1, f"={D(c_stoc)}", f"={D(piese)}",
                 f'="Piese recuperate, evaluate de comisia tehnică " & {D(sufix)}',
                 f"={D(c_venit_alt)}", f"={D(piese)}",
                 f'="Venit din piese recuperate " & {D(sufix)}'])
    j.gol()

    j.sectiune("Sumar și controale")
    grupuri = (b1, b2, b3a, b3b, b4)
    tdr = j.kv("Total Dr", "=" + "+".join(x["C"] for x in grupuri), tip="calc")
    tcr = j.kv("Total Cr", "=" + "+".join(x["F"] for x in grupuri), tip="calc")
    j.check("Check Σ (structural)", f"={tdr}-{tcr}",
            f'=IF(ABS({tdr}-{tcr})<0.01,"OK — notele se închid","EROARE")')
    j.check("Check stingere integrală 21x",
            f"={b1['F']}+{b2['F']}-{D(intrare)}",
            f'=IF(ABS({b1["F"]}+{b2["F"]}-{D(intrare)})<0.01,'
            f'"OK — 21x se stinge integral","EROARE — rămâne sold pe mijlocul ieșit")')
    j.check("Check deductibilitate (informativ, nu blochează)",
            f"={D(neded)}",
            f'=IF({D(neded)}<0.001,"OK — integral deductibil",'
            f'"ATENȚIE — " & TEXT({D(neded)},"0.00") & " lei nedeductibili fără document")')
    j.nota("Stare terminală așteptată: sold 21x = 0, sold 28x = 0 pentru bunul ieșit; "
           "starea în modulul de imobilizări schimbată în vândut / casat.")

    # ---------------------------------------------------------------- NotaExport
    n = F("NotaExport_IESIRE_MF", {"A": 6, "B": 34, "C": 12, "D": 14, "E": 14, "F": 14,
                                   "G": 50, "H": 32, "I": 10})
    n.titlu("MOD_IESIRE_MF — Notă pentru import (1 rând = 1 înregistrare)")
    n.nota("Filtrează pe Include = DA. Rândurile pe zero corespund blocului inactiv "
           "pentru tipul de ieșire ales.")
    n.gol()
    n.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document", "Include"])
    J = j.ref
    linii = [
        ("Bloc 1 — Descărcare amortizare", b1, "Notă de scoatere din evidență"),
        ("Bloc 2 — Valoare rămasă", b2, "Notă de scoatere din evidență"),
        ("Bloc 3 — Vânzare", b3a, "Factură de vânzare"),
        ("Bloc 3 — TVA", b3b, "Factură de vânzare"),
        ("Bloc 4 — Piese recuperate", b4, "PV scoatere din funcțiune + listă comisie"),
    ]
    refs = []
    for i, (bloc, b, doc) in enumerate(linii, start=1):
        r = n.rand([i, bloc, f"={D(data_i)}", f"={J(b['B'])}", f"={J(b['E'])}",
                    f"={J(b['C'])}", f"={J(b['D'])}", doc, None])
        n.ws.cell(row=n.r - 1, column=9, value=f'=IF({r["F"]}>0.001,"DA","NU")')
        refs.append(r["F"])
    n.gol()
    n.kv("Rânduri de importat (Include=DA)",
         f'=COUNTIF({refs[0].replace("F", "I")}:{refs[-1].replace("F", "I")},"DA")', tip="calc")
    n.check("Check global (trebuie 0)", f"={J(tdr)}-{J(tcr)}",
            f'=IF(ABS({J(tdr)}-{J(tcr)})<0.01,"OK","EROARE")')
