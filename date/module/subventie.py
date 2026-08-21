"""MOD_SUBVENTIE — subvenție pentru investiții, eliberată pe măsura amortizării.

Acoperă F-29.

Ideea pe care o apără modulul: subvenția NU e venit la încasare. Ea stă în 475 și se
trece la venit **pe măsura amortizării activului finanțat**, ca cele două să se anuleze
reciproc în fiecare lună. Cine o trece la venit la încasare umflă rezultatul anului 1 și
îl sărăcește pe următorii, cu efect direct pe impozitul pe profit și pe dividende.

Cazul general, pe care monografia nu-l acoperea: **subvenția poate finanța doar o parte
din activ.** Atunci eliberarea e proporțională — cota de finanțare aplicată amortizării
lunare. Modulul calculează cota și arată explicit cât din amortizare rămâne pe cheltuiala
proprie a firmei.
"""

COD = "MOD_SUBVENTIE"

CATALOG = dict(
    fluxuri="F-29",
    tip="Lunar, pe activ subvenționat",
    variabile="Valoare subvenție, valoare activ, durata de amortizare, luna curentă",
    porti="Cota de finanțare — eliberarea e proporțională dacă subvenția acoperă parțial",
    blocuri="B1 Încasarea subvenției; B2 Achiziția activului; B3 Amortizare + eliberare",
    activ="NU",
)


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_SUBVENTIE", {"A": 48, "B": 20, "C": 62})
    d.titlu("MOD_SUBVENTIE — Declarații (input)")
    d.nota("Valorile implicite reproduc monografia din F-29 (utilaj 50.000, subvenție "
           "integrală, 60 de luni). Schimbă valoarea subvenției ca să vezi cazul parțial.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    obiect = d.kv("Activul finanțat", "Utilaj tehnologic")
    contract = d.kv("Contract / program de finanțare", "AFIR 2026-114")
    data_inc = d.kv("Data încasării subvenției", "2026-03-10")
    data_pif = d.kv("Data punerii în funcțiune", "2026-04-01")
    luna = d.kv("Luna curentă (AAAA-LL)", "2026-07")
    data_nota = d.kv("Data notei lunare (ultima zi a lunii)", "2026-07-31")
    d.gol()

    d.sectiune("2. Sumele")
    subventie = d.kv("Valoarea subvenției încasate", 50000)
    activ = d.kv("Valoarea de intrare a activului", 50000)
    durata = d.kv("Durata de amortizare (luni)", 60)
    luni_scurse = d.kv("Luni de amortizare deja înregistrate", 3,
                       nota="Fără luna curentă; se folosește la calculul soldului rămas")
    d.gol()

    d.sectiune("3. Calcul automat (nu edita)")
    cota = d.kv("Cota de finanțare din subvenție",
                f"=IF({activ}=0,0,MIN(1,{subventie}/{activ}))", tip="calc",
                nota="1 = subvenția acoperă integral activul; sub 1 = finanțare parțială")
    amo = d.kv("Amortizare lunară", f"=ROUND({activ}/{durata},2)", tip="calc")
    eliberare = d.kv("Subvenție eliberată lunar la venit",
                     f"=ROUND({amo}*{cota},2)", tip="calc",
                     nota="Amortizarea × cota de finanțare — nu amortizarea întreagă")
    propriu = d.kv("Amortizare rămasă pe cheltuiala firmei", f"={amo}-{eliberare}",
                   tip="calc")
    sold_475 = d.kv("Sold 475 după luna curentă",
                    f"=ROUND({subventie}-{eliberare}*({luni_scurse}+1),2)", tip="calc")
    efect = d.kv("Efect net pe rezultatul lunii", f"={eliberare}-{amo}", tip="calc",
                 nota="Zero doar la finanțare integrală; altfel = partea proprie, cu minus")
    d.gol()

    d.sectiune("4. Conturi")
    c_subv = d.kv("Cont subvenții pentru investiții", 475)
    c_creanta = d.kv("Cont creanță din subvenție", "445",
                     nota="Dacă subvenția e aprobată dar neîncasată încă")
    c_banca = d.kv("Cont trezorerie", "5121")
    c_activ = d.kv("Cont imobilizare", "2131")
    c_furnizor = d.kv("Cont furnizor de imobilizări", "404")
    c_amo = d.kv("Cont amortizare", 2813)
    c_chelt = d.kv("Cont cheltuială cu amortizarea", 6811)
    c_venit = d.kv("Cont venit din subvenții pentru investiții", 7584)
    d.gol()

    d.sectiune("5. Controale")
    d.check("Check cota de finanțare", f"={cota}",
            f'=IF({cota}>=1,"Finanțare INTEGRALĂ — efectul net pe rezultat e zero în '
            f'fiecare lună","Finanțare PARȚIALĂ (" & TEXT({cota}*100,"0.0") & "%) — restul '
            f'de " & TEXT({propriu},"0.00") & " lei/lună rămâne cheltuiala firmei")')
    d.check("Check efect net pe rezultat", f"={efect}",
            f'=IF(ABS({efect})<0.01,"OK — amortizarea și venitul se anulează reciproc",'
            f'"Rezultatul lunii scade cu " & TEXT(-{efect},"0.00") & " lei — corect la '
            f'finanțare parțială")')
    d.check("Check sold 475 nu devine negativ", f"={sold_475}",
            f'=IF({sold_475}>=-0.01,"OK — mai sunt " & TEXT({sold_475},"0.00") & '
            f'" lei de eliberat","EROARE — s-a eliberat mai mult decât s-a încasat; '
            f'verifică numărul de luni")')
    d.check("Check durata eliberării = durata amortizării",
            f"=IF({eliberare}=0,0,ROUND({subventie}/{eliberare},0))",
            f'=IF(ABS(B{d.r}-{durata})<1.5,"OK — subvenția se epuizează odată cu '
            f'amortizarea","ATENȚIE — eliberarea nu se sincronizează cu amortizarea")')
    d.check("Reminder: NU e venit la încasare", f"={subventie}",
            '="La încasare, subvenția intră în 475 (regularizare temporală), nu în clasa 7. '
            'Trecerea la venit se face lunar, pe măsura amortizării."')
    d.gol()

    d.sectiune("6. Sufix generat")
    sufix = d.kv("Sufix", f'=" - " & {obiect} & " - " & {luna}', tip="calc")

    # -------------------------------------------------------------------- Reguli
    g = F("Reguli_SUBVENTIE", {"A": 26, "B": 40, "C": 14, "D": 32, "E": 20, "F": 54})
    g.titlu("MOD_SUBVENTIE — Reguli (tabele fixe)")
    g.gol()
    g.sectiune("Tabel A — Secvența")
    g.cap(["Moment", "Înregistrare", "Cont", "Sumă", "Condiție", "Observație"])
    for row in [
        ("Aprobarea", "445 = 475", "445", "valoarea aprobată", "dacă e aprobată neîncasată",
         "Creanța față de finanțator; pasul se sare dacă încasarea e simultană"),
        ("Încasarea", "5121 = 475 (sau 445)", "475", "valoarea încasată", "întotdeauna",
         "475 e cont de REGULARIZARE TEMPORALĂ, nu de venit"),
        ("Achiziția activului", "21x = 404", "21x", "valoarea de intrare", "întotdeauna",
         "Independentă de subvenție; activul se înregistrează la valoarea lui completă"),
        ("Amortizarea lunară", "6811 = 28x", "6811", "valoare / durată", "lunar",
         "Pe valoarea INTEGRALĂ a activului, nu pe partea nesubvenționată"),
        ("Eliberarea subvenției", "475 = 7584", "475", "amortizare × cota", "lunar, CONCOMITENT",
         "Pas revelator: eliberarea urmează amortizarea, nu calendarul"),
    ]:
        g.rand(list(row))
    g.gol()

    g.sectiune("Tabel B — Cota de finanțare")
    g.cap(["Situație", "Cota", "Eliberare lunară", "Efect net pe rezultat", "", "Observație"])
    for row in [
        ("Subvenția acoperă integral activul", "1", "cât amortizarea lunară", "zero", "",
         "Cazul din monografia F-29"),
        ("Subvenția acoperă parțial", "subvenție / activ", "amortizare × cota",
         "negativ, egal cu partea proprie", "",
         "Cazul frecvent în practică — cofinanțare"),
        ("Subvenția depășește valoarea activului", "plafonat la 1", "cât amortizarea lunară",
         "zero", "", "Verifică încadrarea: excedentul nu e subvenție pentru investiții"),
    ]:
        g.rand(list(row))
    g.gol()

    g.sectiune("Tabel C — LIMITĂRI DECLARATE ale modulului")
    g.cap(["Ce NU tratează", "De ce", "Ce faci", "", "", "Efect dacă îl ignori"])
    for row in [
        ("Subvenții pentru exploatare (741)", "Acelea sunt venit în perioada în care se "
         "produce cheltuiala acoperită, nu se eșalonează pe amortizare.",
         "Folosește 741, nu 475/7584.", "", "",
         "Venitul e amânat pe ani, când ar trebui recunoscut imediat"),
        ("Restituirea subvenției", "Neîndeplinirea condițiilor din contract obligă la "
         "restituire, cu tratament propriu.",
         "Stornează partea neeliberată din 475 și tratează restul pe cheltuială.", "", "",
         "475 rămâne cu sold pentru o subvenție care nu mai există"),
        ("Cedarea activului înainte de finalul amortizării",
         "Soldul rămas din 475 se reia integral la venit la data ieșirii.",
         "Reia soldul 475 în 7584 odată cu descărcarea activului (vezi MOD_IESIRE_MF).",
         "", "", "475 rămâne cu sold pentru un activ care nu mai e în patrimoniu"),
        ("Ajustarea planului de amortizare", "O modificare de durată schimbă și ritmul "
         "eliberării subvenției.",
         "Recalculează ambele; cota rămâne aceeași, amortizarea lunară se schimbă.", "", "",
         "Subvenția se epuizează înainte sau după activ"),
    ]:
        g.rand(list(row))

    # ------------------------------------------------------------------- Jurnale
    j = F("Jurnale_SUBVENTIE", {"A": 8, "B": 14, "C": 14, "D": 48, "E": 14, "F": 14,
                                "G": 48})
    j.titlu("MOD_SUBVENTIE — Jurnale (generate automat)")
    j.nota("Blocul 3 se repetă lunar, pe toată durata de amortizare. Cele două înregistrări "
           "din el se fac CONCOMITENT — asta e tot mecanismul.")
    j.gol()
    D = d.ref

    j.sectiune("Bloc 1 — Încasarea subvenției")
    j.kv("Data jurnal:", f"={D(data_inc)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b1 = j.r
    j.rand([1, f"={D(c_banca)}", f"={D(subventie)}",
            f'="Încasarea subvenției pentru investiții" & {D(sufix)}',
            f"={D(c_subv)}", f"={D(subventie)}",
            f'="Subvenție pentru investiții, de eliberat pe măsura amortizării" & {D(sufix)}'])
    j.gol()
    j.check("Check Σ (structural)", f"=C{b1}-F{b1}",
            f'=IF(ABS(B{j.r})<0.01,"OK — nota se închide","EROARE")')
    j.check("Check: nu atinge clasa 7", f"={D(c_subv)}",
            '="Corect — 475 e regularizare temporală. Venitul apare abia în blocul 3, '
            'lunar."')
    j.gol()

    j.sectiune("Bloc 2 — Achiziția activului")
    j.kv("Data jurnal:", f"={D(data_pif)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b2 = j.r
    j.rand([1, f"={D(c_activ)}", f"={D(activ)}",
            f'="Achiziția activului finanțat, la valoarea integrală" & {D(sufix)}',
            f"={D(c_furnizor)}", f"={D(activ)}",
            f'="Datorie față de furnizorul de imobilizări" & {D(sufix)}'])
    j.gol()
    j.check("Check Σ (structural)", f"=C{b2}-F{b2}",
            f'=IF(ABS(B{j.r})<0.01,"OK — nota se închide","EROARE")')
    j.gol()

    j.sectiune("Bloc 3 — Amortizare + eliberare (LUNAR, concomitent)")
    j.kv("Data jurnal:", f"={D(data_nota)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b3 = j.r
    j.rand([1, f"={D(c_chelt)}", f"={D(amo)}",
            f'="Amortizarea lunară a activului" & {D(sufix)}',
            f"={D(c_amo)}", f"={D(amo)}",
            f'="Amortizare cumulată" & {D(sufix)}'])
    j.rand([2, f"={D(c_subv)}", f"={D(eliberare)}",
            f'="Eliberarea subvenției pe măsura amortizării" & {D(sufix)}',
            f"={D(c_venit)}", f"={D(eliberare)}",
            f'="Venit din subvenții pentru investiții" & {D(sufix)}'])
    sf3 = j.r - 1
    j.gol()
    j.check("Total Dr", f"=SUM(C{b3}:C{sf3})", "")
    j.check("Total Cr", f"=SUM(F{b3}:F{sf3})", "")
    j.check("Check Σ (structural)", f"=SUM(C{b3}:C{sf3})-SUM(F{b3}:F{sf3})",
            f'=IF(ABS(B{j.r})<0.01,"OK — notele se închid","EROARE")')
    j.check("Check efect pe rezultat", f"={D(efect)}",
            f'=IF(ABS({D(efect)})<0.01,"OK — amortizarea și venitul se anulează: '
            f'rezultatul lunii nu e afectat de activul subvenționat",'
            f'"Rezultatul scade cu " & TEXT(-{D(efect)},"0.00") & " lei — partea '
            f'nesubvenționată a amortizării")')
    j.gol()
    j.nota("Stare terminală, la finalul duratei: sold 475 = 0, activ complet amortizat, "
           "iar suma veniturilor din 7584 = valoarea subvenției încasate.")

    # ---------------------------------------------------------------- NotaExport
    n = F("NotaExport_SUBVENTIE", {"A": 6, "B": 34, "C": 12, "D": 12, "E": 12, "F": 14,
                                   "G": 48, "H": 22, "I": 9})
    n.titlu("MOD_SUBVENTIE — Notă pentru import (1 rând = 1 înregistrare)")
    n.nota("Blocurile 1 și 2 se importă o singură dată; blocul 3 se repetă lunar.")
    n.gol()
    n.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    J = j.ref
    prima_n = n.r
    linii = [("Bloc 1 — Încasare (o dată)", data_inc, b1, "Contract + extras"),
             ("Bloc 2 — Achiziție (o dată)", data_pif, b2, "Factură + PV recepție")]
    linii += [("Bloc 3 — Lunar", data_nota, r, "Notă contabilă lunară")
              for r in range(b3, sf3 + 1)]
    for i, (bloc, data, r, doc) in enumerate(linii, start=1):
        rn = n.r
        n.rand([i, bloc, f"={D(data)}", f"={J(f'B{r}')}", f"={J(f'E{r}')}",
                f"=MAX(N({J(f'C{r}')}),N({J(f'F{r}')}))", f"={J(f'D{r}')}", doc,
                f'=IF(N(F{rn})>0.005,"DA","NU")'])
    ultim_n = n.r - 1
    n.gol()
    n.kv("Rânduri de importat (Include=DA)", f'=COUNTIF(I{prima_n}:I{ultim_n},"DA")',
         tip="calc")
