"""MOD_IMOBILIZARI — intrarea unui mijloc fix și planul de amortizare.

Acoperă F-54, F-55, F-57 și controlul din F-61.

Particularități:
- cele trei regimuri de TVA la intrare (intern cu TVA / taxare inversă / import
  cu plată în vamă) se aleg dintr-un singur câmp, iar blocurile se activează singure;
- taxele vamale și transportul se CAPITALIZEAZĂ (OMFP 1802/2014), nu se trec pe 635;
- testul prag mijloc fix vs. obiect de inventar (5.000 lei, OUG 8/2026);
- oglinda 21x ↔ 28x se propune automat, ca să se poată verifica în prima lună (C-14).
"""

COD = "MOD_IMOBILIZARI"

CATALOG = dict(
    fluxuri="F-54, F-55, F-57, F-61",
    tip="Pe mijloc fix + lunar",
    variabile="Valoare, regim TVA, cod clasificare, durată, dată PIF, taxe vamale, transport",
    porti="Prag 5.000 lei (MF vs. obiect de inventar); tranzit 223/224 dacă nu e recepționat",
    blocuri="B1 Intrare; B2 TVA pe regim; B3 Costuri capitalizate; B4 Amortizare lunară",
)

REGIMURI = "INTERN / TAXARE_INVERSA / IMPORT"


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_IMOBILIZARI", {"A": 46, "B": 22, "C": 58})
    d.titlu("MOD_IMOBILIZARI — Declarații (input)")
    d.nota("Completează doar celulele galbene. Regimul de TVA activează singur blocul potrivit.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    denumire = d.kv("Denumire mijloc fix", "Echipament tehnologic")
    luna = d.kv("Luna", "2026-07")
    data_f = d.kv("Data facturii", "2026-07-05")
    data_pif = d.kv("Data punerii în funcțiune", "2026-07-20")
    d.gol()

    d.sectiune("2. Valori")
    valoare = d.kv("Valoare din factură / DVI (fără TVA)", 100000)
    vamale = d.kv("Taxe vamale (0 dacă nu e import)", 0,
                  nota="Se CAPITALIZEAZĂ, nu se trec pe 635")
    transport = d.kv("Transport și manipulare până la recepție", 0,
                     nota="Intră tot în costul de achiziție")
    cota = d.kv("Cotă TVA", "=Parametri!B10", tip="calc")
    d.gol()

    d.sectiune("3. Regim și clasificare")
    regim = d.kv("Regim TVA (INTERN / TAXARE_INVERSA / IMPORT)", "INTERN")
    receptionat = d.kv("Bunul a fost recepționat? (DA / NU)", "DA",
                       nota="NU → intrarea se face pe 223/224 (tranzit), vezi F-57")
    cod_clas = d.kv("Cod de clasificare din catalog", "2.1.16.4.1")
    durata = d.kv("Durată de amortizare (luni)", 120,
                  nota="Din catalogul de clasificare; merge în D406/SAF-T")
    d.gol()

    d.sectiune("4. Calcul automat (nu edita)")
    cost = d.kv("Valoare de intrare (cost complet)",
                f"={valoare}+{vamale}+{transport}", tip="calc")
    tva = d.kv("TVA aferentă", f"={valoare}*{cota}", tip="calc")
    amort = d.kv("Amortizare lunară", f"=ROUND({cost}/{durata},2)", tip="calc")
    d.check("Test prag mijloc fix",
            f"={cost}",
            f'=IF({cost}>={P["prag_mf"]},"OK — mijloc fix, se amortizează",'
            f'"ATENȚIE — sub prag: obiect de inventar (303), nu mijloc fix")')
    d.check("Test recepție",
            f"={receptionat}",
            f'=IF({receptionat}="DA","OK — intrare directă în contul de imobilizare",'
            f'"TRANZIT — se înregistrează pe 223/224 până la recepție (F-57)")')
    d.check("Test regim TVA",
            f"={regim}",
            f'=IF(OR({regim}="INTERN",{regim}="TAXARE_INVERSA",{regim}="IMPORT"),'
            f'"OK — regim recunoscut","EROARE — regim necunoscut")')
    d.gol()

    d.sectiune("5. Conturi")
    c_imo = d.kv("Cont imobilizare (21x)", "2131")
    c_amo = d.kv("Cont amortizare (28x) — oglinda", "2813",
                 nota="C-14: 212↔2812, 213x↔2813, 214↔2814, 215↔2815")
    c_tranzit = d.kv("Cont tranzit dacă nerecepționat", "223")
    c_furn = d.kv("Cont furnizor de imobilizări", "404")
    c_4426 = d.kv("Cont TVA deductibilă", 4426)
    c_4427 = d.kv("Cont TVA colectată (taxare inversă)", 4427)
    c_vama = d.kv("Cont taxe vamale", "446.VAMA")
    c_banca = d.kv("Cont bancă", "5121")
    c_chelt = d.kv("Cont cheltuială cu amortizarea", 6811)
    d.gol()

    d.sectiune("6. Sufix generat")
    sufix = d.kv("Sufix", f'="— " & {denumire} & " " & {luna}', tip="calc")
    d.gol()
    d.kv("Modul activ în CatalogModule?",
         '=IF(INDEX(CatalogModule!A:A,MATCH("MOD_IMOBILIZARI",CatalogModule!B:B,0))="DA",'
         '"ACTIV — jurnalele se generează","INACTIV — jurnalele rămân goale")', tip="calc")

    # -------------------------------------------------------------------- Reguli
    g = F("Reguli_IMOBILIZARI", {"A": 10, "B": 16, "C": 16, "D": 34, "E": 26, "F": 56})
    g.titlu("MOD_IMOBILIZARI — Reguli (tabele fixe)")
    g.nota("Se editează doar când se schimbă legea sau catalogul de clasificare.")
    g.gol()
    g.sectiune("Tabel A — Regimuri de TVA la intrare")
    g.cap(["Regim", "Cont Dr", "Cont Cr", "Sumă", "Condiție", "Temei / observație"])
    for row in [
        ("INTERN", "4426", "404", "valoare × cotă", "Furnizor român plătitor",
         "TVA deductibilă normală"),
        ("TAXARE_INVERSA", "4426", "4427", "valoare × cota din România",
         "Achiziție intracomunitară SAU art. 331 intern",
         "IC: cere VIES valid + dovada transportului. Clădiri: cod 27 în D394, altfel "
         "decontul nu recunoaște operațiunea"),
        ("IMPORT", "4426", "5121", "TVA plătit efectiv în vamă", "Import din afara UE",
         "Document de bază: DVI, nu factura furnizorului. Cu certificat de amânare: 4426 = 4427"),
    ]:
        g.rand(list(row))
    g.gol()
    g.sectiune("Tabel B — Ce intră în costul de achiziție")
    g.cap(["Element", "Tratament", "", "", "", "Temei"])
    for row in [
        ("Preț din factură / DVI", "capitalizat", "", "", "", "OMFP 1802/2014"),
        ("Taxe vamale nerecuperabile", "CAPITALIZAT — nu pe 635", "", "", "", "OMFP 1802/2014"),
        ("Transport și manipulare până la recepție", "capitalizat", "", "", "", "OMFP 1802/2014"),
        ("TVA nedeductibilă (ex. 50% vehicule)", "capitalizată sau pe cheltuială",
         "", "", "", "vezi MOD_LEASING_FIN"),
        ("Dobânzi de finanțare", "de regulă pe cheltuială", "", "", "", "OMFP 1802/2014"),
    ]:
        g.rand(list(row))
    g.gol()
    g.sectiune("Tabel C — Oglinda cont activ ↔ cont amortizare (C-14)")
    g.cap(["Activ", "Amortizare", "", "Activ", "Amortizare", "Observație"])
    for row in [
        ("205", "2805", "", "212", "2812", ""),
        ("208", "2808", "", "2131/2132/2133", "2813", "2813 deservește mai multe conturi"),
        ("2111", "— nu se amortizează", "", "214", "2814", "„2114” din notițe este 214"),
        ("2112", "2811", "", "215", "2815", ""),
    ]:
        g.rand(list(row))
    g.gol()
    g.sectiune("Tabel D — Porți de calitate")
    for t in [
        "• ΣDr = ΣCr pe fiecare bloc",
        "• Amortizarea începe cu luna următoare punerii în funcțiune",
        "• Sold 28x ≤ sold 21x, pe fiecare mijloc (C-13)",
        "• Analitic 21x din balanță = registrul mijloacelor fixe, LUNAR (C-15)",
        "• Verifică în PRIMA lună că nota de amortizare postează perechea corectă (C-14)",
        "• Sub pragul de 5.000 lei: obiect de inventar (303 + 8035), nu mijloc fix",
        "• Declarație la primărie în 30 de zile de la achiziție",
    ]:
        g.rand([t])

    # ------------------------------------------------------------------- Jurnale
    j = F("Jurnale_IMOBILIZARI", {"A": 8, "B": 14, "C": 14, "D": 48, "E": 14, "F": 14, "G": 48})
    j.titlu("MOD_IMOBILIZARI — Jurnale (generate automat)")
    j.nota("Blocurile inactive rămân pe zero — sumele sunt condiționate de regimul declarat.")
    j.gol()
    D = d.ref

    j.sectiune("Bloc 1 — Intrarea în patrimoniu")
    j.kv("Data jurnal:", f"={D(data_f)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    cont_intrare = f'IF({D(receptionat)}="DA",{D(c_imo)},{D(c_tranzit)})'
    b1 = j.rand([1, f"={cont_intrare}", f"={D(valoare)}",
                 f'="Intrare imobilizare " & {D(sufix)}',
                 f"={D(c_furn)}", f"={D(valoare)}",
                 f'="Datorie furnizor de imobilizări " & {D(sufix)}'])
    b1b = j.rand([2, f"={cont_intrare}", f"={D(vamale)}+{D(transport)}",
                  f'="Taxe vamale și transport capitalizate " & {D(sufix)}',
                  f"={D(c_vama)}", f"={D(vamale)}+{D(transport)}",
                  f'="Taxe vamale / transport de plată " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 2 — TVA, pe regimul declarat")
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b2a = j.rand([1, f"={D(c_4426)}", f'=IF({D(regim)}="INTERN",{D(tva)},0)',
                  f'="TVA deductibilă — achiziție internă " & {D(sufix)}',
                  f"={D(c_furn)}", f'=IF({D(regim)}="INTERN",{D(tva)},0)',
                  f'="TVA pe factura furnizorului " & {D(sufix)}'])
    b2b = j.rand([2, f"={D(c_4426)}", f'=IF({D(regim)}="TAXARE_INVERSA",{D(tva)},0)',
                  f'="TVA deductibilă — taxare inversă " & {D(sufix)}',
                  f"={D(c_4427)}", f'=IF({D(regim)}="TAXARE_INVERSA",{D(tva)},0)',
                  f'="TVA colectată — autolichidare " & {D(sufix)}'])
    b2c = j.rand([3, f"={D(c_4426)}", f'=IF({D(regim)}="IMPORT",{D(tva)},0)',
                  f'="TVA deductibilă plătită în vamă " & {D(sufix)}',
                  f"={D(c_banca)}", f'=IF({D(regim)}="IMPORT",{D(tva)},0)',
                  f'="Plată TVA în vamă " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 3 — Recepția, dacă intrarea a fost pe tranzit (F-57)")
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b3 = j.rand([1, f"={D(c_imo)}", f'=IF({D(receptionat)}="NU",{D(cost)},0)',
                 f'="Recepție — stingere tranzit " & {D(sufix)}',
                 f"={D(c_tranzit)}", f'=IF({D(receptionat)}="NU",{D(cost)},0)',
                 f'="Stingere 223/224 la recepție " & {D(sufix)}'])
    j.gol()

    j.sectiune("Bloc 4 — Amortizarea lunară (din luna următoare punerii în funcțiune)")
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b4 = j.rand([1, f"={D(c_chelt)}", f"={D(amort)}",
                 f'="Amortizare lunară " & {D(sufix)}',
                 f"={D(c_amo)}", f"={D(amort)}",
                 f'="Amortizare cumulată " & {D(sufix)}'])
    j.gol()

    j.sectiune("Sumar și controale")
    grupuri = (b1, b1b, b2a, b2b, b2c, b3, b4)
    tdr = j.kv("Total Dr", "=" + "+".join(x["C"] for x in grupuri), tip="calc")
    tcr = j.kv("Total Cr", "=" + "+".join(x["F"] for x in grupuri), tip="calc")
    j.check("Check Σ (structural)", f"={tdr}-{tcr}",
            f'=IF(ABS({tdr}-{tcr})<0.01,"OK — notele se închid","EROARE")')
    j.check("Check exclusivitate regim TVA",
            f"=COUNTIF({b2a['C']}:{b2c['C']},\">0.001\")",
            f'=IF(COUNTIF({b2a["C"]}:{b2c["C"]},">0.001")<=1,"OK — un singur regim activ",'
            f'"EROARE — mai multe regimuri simultan")')
    j.check("Check valoare de intrare",
            f"={b1['C']}+{b1b['C']}-{D(cost)}",
            f'=IF(ABS({b1["C"]}+{b1b["C"]}-{D(cost)})<0.01,'
            f'"OK — cost complet capitalizat","EROARE — taxe sau transport pierdute")')
    j.check("Check amortizare vs. durată",
            f"={D(amort)}*{D(durata)}-{D(cost)}",
            f'=IF(ABS({D(amort)}*{D(durata)}-{D(cost)})<1,'
            f'"OK — planul acoperă valoarea de intrare","ATENȚIE — diferență din rotunjire, '
            f'se regularizează la ultima rată")')
    j.nota("Stare terminală așteptată: 21x = valoarea de intrare completă, sold 223/224 = 0, "
           "28x crește lunar și nu depășește niciodată 21x.")

    # ---------------------------------------------------------------- NotaExport
    n = F("NotaExport_IMOBILIZARI", {"A": 6, "B": 34, "C": 12, "D": 14, "E": 14, "F": 14,
                                     "G": 50, "H": 30, "I": 10})
    n.titlu("MOD_IMOBILIZARI — Notă pentru import (1 rând = 1 înregistrare)")
    n.nota("Filtrează pe Include = DA. Rândurile cu sumă zero sunt blocuri inactive pe regimul ales.")
    n.gol()
    n.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document", "Include"])
    J = j.ref
    linii = [
        ("Bloc 1 — Intrare", b1, "Factură / DVI"),
        ("Bloc 1 — Costuri capitalizate", b1b, "DVI + factură transport"),
        ("Bloc 2 — TVA intern", b2a, "Factură furnizor"),
        ("Bloc 2 — TVA taxare inversă", b2b, "Autofactură / factură IC"),
        ("Bloc 2 — TVA în vamă", b2c, "DVI + extras"),
        ("Bloc 3 — Recepție", b3, "Proces-verbal de recepție"),
        ("Bloc 4 — Amortizare", b4, "Notă de amortizare"),
    ]
    refs = []
    for i, (bloc, b, doc) in enumerate(linii, start=1):
        data_ref = D(data_pif) if "Amortizare" in bloc else D(data_f)
        r = n.rand([i, bloc, f"={data_ref}", f"={J(b['B'])}", f"={J(b['E'])}",
                    f"={J(b['C'])}", f"={J(b['D'])}", doc, None])
        n.ws.cell(row=n.r - 1, column=9, value=f'=IF({r["F"]}>0.001,"DA","NU")')
        refs.append(r["F"])
    n.gol()
    n.kv("Rânduri de importat (Include=DA)",
         f'=COUNTIF({refs[0].replace("F", "I")}:{refs[-1].replace("F", "I")},"DA")', tip="calc")
    n.check("Check global (trebuie 0)", f"={J(tdr)}-{J(tcr)}",
            f'=IF(ABS({J(tdr)}-{J(tcr)})<0.01,"OK","EROARE")')
