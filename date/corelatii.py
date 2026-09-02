"""Corelațiile de control C-13…C-22 (capitaluri și imobilizări).

Același format ca C-01…C-12 din workbook-ul original: formulă · unde se verifică ·
ce o rupe LEGITIM · ce o rupe SUSPECT · flux/modul legat · severitate.

Scopul coloanei „LEGITIM” e să deosebești „nu ține pentru că am greșit” de
„nu ține pentru că s-a întâmplat X, și e normal”.
"""

CORELATII = [
    dict(
        id="C-13",
        formula="sold 28x ≤ sold 21x\n(pe fiecare mijloc fix, nu pe total)",
        unde="Balanță analitică 21x vs. 28x, pe mijloc",
        legitim="Nimic — amortizarea cumulată nu poate depăși valoarea de intrare.\n"
                "Bun integral amortizat: sold 28x = sold 21x (egalitate, nu depășire).",
        suspect="Amortizare calculată peste durata normală\n"
                "Mijloc ieșit din gestiune fără descărcarea lui 28x\n"
                "Cont 28x fără analitic pe mijloc\n"
                "Cont setat greșit în planul societății (bifuncțional sau pe sens invers)",
        flux="F-59, F-60, F-61",
        severitate="Înaltă — valoare netă și rezultat denaturate",
    ),
    dict(
        id="C-14",
        formula="oglinda cont activ ↔ cont amortizare:\n"
                "205↔2805 · 208↔2808 · 2112↔2811\n"
                "212↔2812 · 213x↔2813 · 214↔2814 · 215↔2815",
        unde="Nota de amortizare din PRIMA lună + balanța analitică",
        legitim="2813 deservește mai multe conturi (2131, 2132, 2133, 2134) —\n"
                "e normal ca soldul lui să acopere mai multe analitice de 213.\n"
                "2111 Terenuri nu are pereche: nu se amortizează.",
        suspect="Amortizare postată pe alt cont decât perechea\n"
                "Softul nu face automat corespondența și nimeni nu a verificat\n"
                "Analitic de 213 fără corespondent în 2813",
        flux="F-53, F-54, F-61",
        severitate="Medie — se propagă lunar dacă nu e prinsă în prima lună",
    ),
    dict(
        id="C-15",
        formula="analitic 21x din balanța contabilă =\nregistrul mijloacelor fixe / modulul de imobilizări\n(LUNAR)",
        unde="Listing modul imobilizări vs. balanță analitică",
        legitim="Intrare la sfârșit de lună, încă neintrodusă în modul (se reglează în luna următoare, cu notă)\n"
                "Mijloc în 223/224, facturat dar nerecepționat (nu e încă în modul)",
        suspect="Mijloc fix neintrodus în modulul de imobilizări → amortizare neînregistrată →\n"
                "impozit pe profit plătit în plus\n"
                "Ieșire operată în modul dar nu în contabilitate (sau invers)",
        flux="F-57, F-61",
        severitate="Înaltă — impozit pe profit supraevaluat",
    ),
    dict(
        id="C-16",
        formula="Σ rulaj clasa 7 − Σ rulaj clasa 6 = sold 121\n(înainte de închidere)\nsold 121 = 0 după închidere",
        unde="Balanță + nota de închidere a exercițiului",
        legitim="Repartizarea pe 129 făcută la 31.12, înainte de închiderea lui 121\n"
                "711/712/722 cu sold creditor înainte de închidere = variația stocului / producția "
                "capitalizată, normal",
        suspect="121 din anul precedent NEÎNCHIS — cauza #1 când corelația nu ține\n"
                "Cont de cheltuială sau venit rămas neînchis după notă\n"
                "331 închis greșit pe 121",
        flux="F-37, F-41, F-46",
        severitate="Critică — bilanț, D101 și baza de dividende",
    ),
    dict(
        id="C-17",
        formula="sold 1061 ≤ 20% × capital social subscris ȘI VĂRSAT\nrulaj anual 1061 ≤ 5% × (sold 121 + rulaj 691)",
        unde="Balanță 1061 vs. 1012 + nota de repartizare",
        legitim="Plafonul de 20% atins → nu se mai constituie rezervă (rulaj 0, sold la plafon)\n"
                "Majorare de capital social în cursul anului → plafonul crește",
        suspect="Plafonul calculat pe capital SUBSCRIS, ignorând partea nevărsată din 1011\n"
                "Rezerva constituită peste 5% din profitul contabil brut → partea în plus nedeductibilă\n"
                "Rezerva constituită pe profit net, nu pe profit brut",
        flux="F-45, F-46",
        severitate="Medie — deductibilitate și conformare L. 31/1990",
    ),
    dict(
        id="C-18",
        formula="sold 1174 = 0 la 31.12",
        unde="Balanță 1174 la închidere",
        legitim="Corecție înregistrată în decembrie, transferată în 1171 după hotărârea AGA din anul următor\n"
                "(cu notă explicativă la dosarul de închidere)",
        suspect="1174 lăsat cu sold pe termen lung — cont TRANZITORIU, nu de sold\n"
                "Corecție făcută pe 1174 fără D101 rectificativ depus\n"
                "Corecție trecută prin 628 în loc de 1174 (denaturează rezultatul curent)",
        flux="F-47",
        severitate="Înaltă — D101 și trasabilitatea corecției",
    ),
    dict(
        id="C-19",
        formula="sold 167 pe contract = sold din scadențar\n(în valuta contractului)",
        unde="Balanță analitică 167 vs. scadențarul de la firma de leasing",
        legitim="Factură de rată emisă la un curs diferit de cel din scadențar (se explică prin diferența de curs)\n"
                "Rate restante sau reeșalonare comunicată de finanțator",
        suspect="167 fără analitic pe contract → nu poți ști la ce rată te raportezi la reevaluare\n"
                "Mai multe contracte amestecate pe același analitic\n"
                "Avansul (4093) neînchis în 167",
        flux="F-50",
        severitate="Înaltă — reevaluare la curs greșit, valoare de intrare greșită",
    ),
    dict(
        id="C-20",
        formula="capitaluri proprii (activ net) ≥ ½ × capital social subscris",
        unde="Bilanț — nu balanță de cont",
        legitim="Pierdere din primul an de activitate, în curs de reconstituire în termenul legal\n"
                "(până la încheierea exercițiului financiar ULTERIOR celui în care s-a constatat)",
        suspect="Activ net sub ½ și totuși s-au distribuit dividende (inclusiv interimare)\n"
                "S-au restituit împrumuturi de la asociați / afiliați\n"
                "Corecție 1174 → 1171 care duce rezultatul reportat pe debitor, după distribuire",
        flux="F-46, F-47",
        severitate="Critică — L. 239/2025: amenzi 10.000–300.000 lei, răspundere solidară, "
                   "risc de dizolvare judiciară",
    ),
    dict(
        id="C-21",
        formula="1171 cu analitic PE AN, cu sens Debitor/Creditor explicit",
        unde="Balanță analitică 1171 vs. rândurile de pierdere din D101",
        legitim="Analitic pe an cu solduri mixte (unii ani profit, alții pierdere) — e chiar scopul",
        suspect="1171 agregat, fără analitic pe an → nu poți urmări recuperarea pierderii\n"
                "(70% din profitul impozabil, în 5 ani consecutivi, pentru pierderi din 2024 încolo)\n"
                "1171 nu reflectă pierderea care apare în D101 → baza impozitului e greșită și\n"
                "plafonul de dividende distribuibile e SUPRAEVALUAT",
        flux="F-46, F-47",
        severitate="Înaltă — impozit pe profit și plafon de dividende",
    ),
    dict(
        id="C-22",
        formula="sold 231/233 = lista obiectivelor în curs\n(pe analitic de obiectiv)",
        unde="Balanță 231/233 + situațiile de lucrări + PV de punere în funcțiune",
        legitim="Obiectiv real în execuție la 31.12, care continuă în anul următor\n"
                "Recepție în ianuarie pentru lucrări din decembrie",
        suspect="Obiectiv pus în funcțiune fără PV → rămâne în 231 și nu se amortizează\n"
                "Sold 231 mare, fără listă pe obiectiv (administratorul întreabă ce e acolo)\n"
                "Prestații de terți trecute pe 628 în loc de 231\n"
                "Salarii capitalizate prin 711 în loc de 722 (sau deloc)",
        flux="F-52, F-58",
        severitate="Înaltă — amortizare neînregistrată, bilanț denaturat",
    ),
    dict(
        id="C-23",
        formula="sensul soldului = natura contului\n"
                "401, 404 → creditor · 4111, 409 → debitor\n"
                "(pe analitic de partener, NU pe total)",
        unde="Balanța analitică de terți + fișa pe plătitor",
        legitim="Avans plătit unui furnizor, ținut pe 401 în loc de 4091 —\n"
                "sold debitor real, dar pus pe contul greșit (se reclasifică, nu se ignoră)\n"
                "Storno de factură înregistrat înaintea facturii pe care o anulează\n"
                "Notă de credit primită și neînchisă încă",
        suspect="Încasare mai mare decât factura, nereclasificată pe 419 —\n"
                "  TVA-ul din diferență rămâne necolectat (F-415)\n"
                "Plată dublă către același furnizor\n"
                "Factură înregistrată de două ori și stornată o singură dată\n"
                "Analitic de partener greșit: soldul se compensează pe total și\n"
                "  dispare din vedere, deși pe partener e contrar naturii",
        flux="F-415, F-410",
        severitate="Înaltă — TVA necolectat și creanțe/datorii raportate eronat",
    ),

    # ======================================================================
    # Familia „rulaj creditor = sold creditor” (sursa 21.08)
    #
    # Notițele numesc regula o singură dată, pe conturile de salarii. Ea e însă
    # generală: se aplică oricărei datorii CONSTITUITE lunar și ACHITATE în luna
    # următoare. În iulie se creditează obligația lui iulie și se debitează plata lui
    # iunie; ce rămâne pe credit la 31 iulie e exact obligația lunii — adică rulajul.
    #
    # De aceea corelațiile de mai jos au aceeași formulă și diferă doar prin ce
    # înseamnă abaterea. Sunt scrise separat, nu ca un rând cu „444/4315/4316/436”,
    # pentru că SUSPECT-ul e altul la fiecare: la 427 e penal, la 444 e stopaj
    # nevărsat, la 4423 e TVA restant.
    # ======================================================================
    dict(
        id="C-24",
        formula="sold creditor 421 + sold creditor 423\n= restul de plată din statul de plată",
        unde="Balanța la 31 ale lunii vs. statul de plată al lunii",
        legitim="Avans acordat în cursul lunii, ținut pe 425 și nescăzut încă\n"
                "Drepturi neridicate reclasificate pe 426 (F-418) —\n"
                "  suma iese din 421, dar rămâne datorată\n"
                "Indemnizații de concediu medical decontate parțial (F-416)",
        suspect="Plată înregistrată pe alt cont decât 421 (ex. 627 = 5121)\n"
                "Salarii neplătite din luni anterioare, nereclasificate pe 426\n"
                "Plată mai mare decât statul — venit neimpozitat la salariat\n"
                "Stat rectificat de HR fără notă rectificativă în contabilitate",
        flux="F-413, F-416, F-418",
        severitate="Înaltă — cea mai ieftină verificare din contabilitate: "
                   "documentul de control există deja",
    ),
    dict(
        id="C-25",
        formula="rulaj creditor 444 = sold creditor 444\n(la sfârșitul fiecărei luni)",
        unde="Balanța lunii + fișa pe plătitor din SPV",
        legitim="Luna în care s-a depus o rectificativă: obligația unei luni\n"
                "  anterioare se modifică, deci soldul conține și diferența\n"
                "Plată în avans a impozitului",
        suspect="Sold > rulaj, constant pe mai multe luni = stopaj la sursă nevirat.\n"
                "  Nevirat peste 30 de zile → răspundere penală\n"
                "Fișa pe plătitor nu se potrivește cu balanța: D112 depus pe alte sume",
        flux="F-413",
        severitate="Înaltă — stopajul la sursă nevirat e infracțiune, nu întârziere",
    ),
    dict(
        id="C-26",
        formula="rulaj creditor 431 (4315 + 4316) = sold creditor 431\n"
                "și rulaj creditor 436 = sold creditor 436",
        unde="Balanța lunii + D112 + fișa pe plătitor",
        legitim="Rectificativă pe o lună anterioară\n"
                "Eșalonare la plată aprobată de ANAF — soldul rămâne legitim mai mare",
        suspect="Contribuții restante acumulate\n"
                "Bază de calcul greșită: rulajul nu corespunde cu brutul din 421",
        flux="F-413",
        severitate="Înaltă — contribuții restante blochează certificatul fiscal",
    ),
    dict(
        id="C-27",
        formula="2,25% × rulaj creditor 421 (brut realizat)\n= rulaj creditor 436",
        unde="Balanța lunii: rulajele 421 și 436",
        legitim="Luni cu concedii medicale: CAM NU se datorează pe partea suportată\n"
                "  din FNUASS (art. 220^5 Cod fiscal), deci rulajul 436 e mai mic decât\n"
                "  2,25% din rulajul 421. Diferența trebuie să fie exact 2,25% ×\n"
                "  indemnizația din fond\n"
                "Categorii cu cotă redusă sau scutire, dacă societatea are astfel de\n"
                "  salariați — verificat pe D112, nu presupus",
        suspect="Bază de calcul incompletă: sporuri sau prime omise din fondul de salarii\n"
                "Cotă aplicată greșit\n"
                "CAM înregistrat invers (436 = 646) — cheltuiala lipsește din rezultat",
        flux="F-413",
        severitate="Medie — se corectează ușor, dar denaturează rezultatul lunii",
    ),
    dict(
        id="C-28",
        formula="rulaj creditor 427 = sold creditor 427\n(la sfârșitul fiecărei luni)",
        unde="Balanța lunii + adresa de înființare a popririi",
        legitim="Poprire înființată la finalul lunii, cu termen de virare în luna\n"
                "  următoare — decalajul normal de scadență",
        suspect="Sold care persistă = bani opriți din salariul altcuiva și nevirați.\n"
                "  Firma nu are ce explica: trebuia fie să vireze, fie să nu rețină\n"
                "Reținere peste limita legală, fără temei pentru cota majorată",
        flux="F-417",
        severitate="Înaltă — singura din grupa 42x care trece din contabil în penal",
    ),
    dict(
        id="C-29",
        formula="sold 4423 / 4424 din balanță\n= soldul din decontul de TVA (NU rulajul lunii)",
        unde="Decontul D300 + balanța + fișa de rol",
        legitim="Sume din decizii de impunere, ținute pe analitic distinct (F-421) —\n"
                "  ele nu intră în decont, deci diferența e prin construcție\n"
                "Facturi înregistrate după depunere, regularizate în decontul următor",
        suspect="TVA neachitat din perioade precedente, omis din decont: la finanțe\n"
                "  soldul pare corect, dar decontul e greșit\n"
                "Sumă din decizie de impunere trecută pe 4423 fără analitic\n"
                "Sold de rambursare pornit dintr-un sold inițial greșit — tot ce\n"
                "  urmează e greșit",
        flux="F-405, F-407, F-421",
        severitate="Înaltă — decontul nu are variantă rectificativă; corecția se face "
                   "doar pe regularizări",
    ),
    # ======================================================================
    # Sursa 26.08.2026 — dividende, creditare, conturile în așteptare
    #
    # Cele cinci au un tipar comun cu C-23 (sold contrar naturii), dar merg mai
    # departe: nu întreabă doar „ce semn are soldul”, ci „ce document extern trebuie
    # să spună același lucru”. Hotărârea AGA, certificatul ONRC și decizia de impunere
    # sunt a doua sursă — iar o corelație fără a doua sursă e doar o preferință.
    # ======================================================================
    dict(
        id="C-30",
        formula="sold 4551 NICIODATĂ debitor\n(pe fiecare analitic de asociat, nu pe total)",
        unde="Balanța analitică a lui 455, la orice moment",
        legitim="Nimic. 4551 e cont de pasiv: sold debitor nu are variantă legitimă.\n"
                "Sold ZERO e starea normală de final, nu o abatere.",
        suspect="Asociatul a ridicat mai mult decât a pus — creditare inexistentă\n"
                "Înregistrare pe sensul greșit\n"
                "Compensare între doi asociați, fără act notarial: soldul total\n"
                "  pare curat, analiticele nu\n"
                "Ridicări puse pe 461 după ce 4551 a ajuns la zero (vezi C-33)",
        flux="F-111, F-112, F-113",
        severitate="Înaltă — la control apare drept bani scoși fără temei, cu efect "
                   "și asupra persoanei, nu doar a firmei",
    ),
    dict(
        id="C-31",
        formula="Σ analitice 1012 = sold 1012\nȘI Σ procentelor din denumiri = 100%",
        unde="Balanța analitică + certificatul constatator ONRC",
        legitim="Firmă nouă preluată cu 1012 „la grămadă”, înainte de spargerea pe\n"
                "  analitice — dar atunci corelația e o SARCINĂ, nu o excepție (F-114)\n"
                "Majorare de capital în curs, cu mențiunea nedepusă încă la ONRC:\n"
                "  partea nouă stă pe 1011, nu pe 1012",
        suspect="Fuziune sau cedare de părți sociale operată în acte și nu în analitice\n"
                "Hotărâre AGA care repartizează pe procente inexistente în balanță\n"
                "Analitice cu procente care nu însumează 100% — cineva a fost uitat",
        flux="F-114, F-109, F-112",
        severitate="Înaltă — cazurile ajunse la comisia de disciplină la ANAF au "
                   "pornit exact de aici",
    ),
    dict(
        id="C-32",
        formula="sold debitor 463 ≤ sold creditor 121\n(la orice moment, nu doar la 31.12)",
        unde="Balanța la data bilanțului interimar și la 31.12",
        legitim="Egalitate: s-a repartizat exact profitul realizat — plafonul atins,\n"
                "  nu depășit\n"
                "Sold 463 = 0 după regularizarea de la 31.12 și trecerea prin 1171",
        suspect="Dividende interimare peste profitul realizat: la 31.12 se stornează,\n"
                "  se depune D710, iar asociatul trebuie să aducă banii înapoi\n"
                "Repartizare făcută pe disponibilul din bancă, nu pe soldul lui 121\n"
                "Lipsa bilanțului interimar sau a inventarierii — condiții legale,\n"
                "  nu formalități",
        flux="F-110",
        severitate="Înaltă — corecția e un proces lung, cu bani de restituit și "
                   "rectificativă printr-un formular separat (D710), pentru că "
                   "decontul nu are variantă rectificativă",
    ),
    dict(
        id="C-33",
        formula="4481 și 4482 se sting până la finalul exercițiului\n(sold reportat = 0)",
        unde="Balanța la 31.12, pe fiecare analitic de decizie sau de plată",
        legitim="Decizie de impunere contestată, cu suspendarea executării — soldul\n"
                "  rămâne, dar are dosar\n"
                "Plată eronată descoperită în decembrie, returnată în ianuarie",
        suspect="Sold purtat de la un an la altul: decizia n-a fost achitată sau\n"
                "  nimeni n-a mai urmărit-o\n"
                "4482 folosit ca depozit pentru diferențe pe care nu le-a disecat\n"
                "  nimeni — devine coș, ca 461\n"
                "Sume din decizii trecute prin 4423: soldul lui 4481 pare curat,\n"
                "  dar decontul de TVA e cel stricat (vezi C-29)",
        flux="F-421, F-424",
        severitate="Medie — conturile există tocmai ca să protejeze corelațiile pe "
                   "care ANAF le contraverifică; nefolosite corect, le strică",
    ),
    dict(
        id="C-34",
        formula="Σ analitice 457 = dividendele din hotărârea AGA\nȘI 457 se stinge doar prin 446 sau 5121",
        unde="Hotărârea AGA + balanța analitică a lui 457 + fișa contului 446",
        legitim="Dividende repartizate și neridicate: 457 rămâne cu sold creditor,\n"
                "  chiar dacă impozitul e deja plătit (termenul e 25.01, indiferent\n"
                "  de ridicare)\n"
                "Renunțare la dividend, documentată prin hotărâre",
        suspect="Sold 457 fără hotărâre AGA în spate — cea mai frecventă cauză de\n"
                "  ajungere la comisia de disciplină\n"
                "457 stins prin 4551 sau 461: dividendul nu se compensează cu\n"
                "  creditarea decât documentat\n"
                "D205 care nu se potrivește cu D100 și cu fișa lui 446 — se caută\n"
                "  o plată făcută fără declarație",
        flux="F-109",
        severitate="Înaltă — impozitul se datorează la data DISTRIBUIRII, nu a plății",
    ),
    # ======================================================================
    # Sursa 28.08.2026 — trezoreria și verificarea balanței
    #
    # C-37 e altfel decât toate celelalte 26: nu verifică un cont anume, verifică o
    # PROPRIETATE a balanței. E corelația pe care formatorul a repetat-o toată ședința
    # și singura care se aplică la orice cont cu analitic, indiferent de subiect. Tot
    # ea e motorul lui MOD_CONTROL_BALANTA.
    # ======================================================================
    dict(
        id="C-35",
        formula="sold 5191 NICIODATĂ debitor\nȘI sold 5191 = soldul confirmat de bancă,\npe fiecare analitic de linie",
        unde="Extrasul de LINIE DE CREDIT (separat de extrasul de cont), la sfârșit de lună",
        legitim="Sold zero: linia e disponibilă și netrasă — starea normală între trageri.",
        suspect="Sold debitor: s-a restituit mai mult decât s-a tras, deci o înregistrare\n"
                "  pe sensul greșit\n"
                "Dobânda operată prin 5191 în loc de 666, pentru că extrasul de linie\n"
                "  n-a fost cerut clientului — cheltuiala dispare, iar impozitul pe\n"
                "  profit se plătește în plus\n"
                "Două linii pe același analitic: totalul poate ieși, liniile nu",
        flux="F-507",
        severitate="Înaltă — la linie NU există scadențar, deci soldul confirmat de "
                   "bancă e singura verificare independentă disponibilă",
    ),
    dict(
        id="C-36",
        formula="sold 581 = 0 la sfârșit de lună\nȘI diferența de curs valutar NU trece prin 581",
        unde="Balanța la sfârșit de lună + jurnalul de bancă",
        legitim="Transfer inițiat la sfârșitul lunii și primit la începutul lunii\n"
                "  următoare: soldul e chiar realitatea, banii sunt pe drum.",
        suspect="Diferența de curs de la transferul valută → lei lăsată în 581: contul\n"
                "  nu se mai închide, iar soldul rămas devine imposibil de citit —\n"
                "  transfer în curs sau diferență necontabilizată?\n"
                "Transfer înregistrat pe o singură parte",
        flux="F-501",
        severitate="Medie — 581 e cont de tranzit PUR: trebuie să iasă cu exact cât a "
                   "intrat, iar diferența de curs aparține contului în valută, unde s-a "
                   "și produs",
    ),
    dict(
        id="C-37",
        formula="Σ analitice = sold sintetic,\npe FIECARE cont cu analitic obligatoriu\n"
                "(4111 · 401 · 512x · 542 · 446 · 455 · 1012)",
        unde="Balanța analitică vs. balanța sintetică; la bancă, și extrasul de cont",
        legitim="Nimic. Nu există motiv legitim pentru care suma analiticelor să difere\n"
                "  de sintetic — e o identitate, nu o estimare.",
        suspect="Operațiune făcută DUPĂ închiderea de lună, fără refacerea închiderii —\n"
                "  cauza cea mai frecventă, și nu se anunță singură\n"
                "Sume nealocate lăsate pe 4111 sau 401 fără analitic de partener\n"
                "Cont pornit fără analitic și spart ulterior: istoricul rămâne pe\n"
                "  sintetic\n"
                "La bancă: jurnalul dă cu extrasul, dar nu dă cu balanța — semn că\n"
                "  diferența e între analitic și sintetic, nu în operare",
        flux="F-214, F-503, F-507",
        severitate="Înaltă — e verificarea pe care formatorul o cere la preluarea "
                   "oricărei societăți, înaintea oricărei alte analize",
    ),
    dict(
        id="C-38",
        formula="sold 5311 ≤ 50.000 lei la sfârșitul FIECĂREI ZILE",
        unde="Registrul de casă, pe fiecare casierie",
        legitim="Depășirea cu sumele aferente plății salariilor și altor drepturi de\n"
                "  personal, pentru perioada scurtă prevăzută de lege.",
        suspect="Sold peste plafon purtat de la o zi la alta: ce depășește trebuie\n"
                "  depus în cont\n"
                "Casierie deschisă special ca să se multiplice plafonul ❓\n"
                "Sold de casă mare și constant, fără numerar real în casă — cazul pe\n"
                "  care controlul îl cere arătat efectiv",
        flux="F-502",
        severitate="Înaltă — plafonul a fost introdus relativ recent; cine lucrează "
                   "după obiceiul vechi, când soldul era nelimitat, îl încalcă fără să știe",
    ),
    dict(
        id="C-39",
        formula="la preluarea unei balanțe ÎN CURSUL ANULUI\nse preiau TOTAL SUME debitoare și creditoare,\nnu soldurile",
        unde="Balanța de preluare vs. balanța lunii următoare",
        legitim="Preluare la 1 ianuarie: acolo soldurile CHIAR sunt punctul de plecare,\n"
                "  iar rulajele anului pornesc de la zero pe bună dreptate.",
        suspect="Preluare la mijloc de an cu soldurile puse ca sold inițial: rulajele\n"
                "  anului pornesc de la zero din luna preluării, iar ORICE verificare\n"
                "  pe rulaj devine falsă — corelația cu fișa de rol la TVA, CAM-ul ca\n"
                "  procent din brut, rulajul creditor al obligațiilor salariale\n"
                "Total sume care nu cresc monoton de la o lună la alta",
        flux="F-422, F-405",
        severitate="Înaltă — eroarea nu se vede în luna preluării, ci la prima "
                   "verificare pe rulaj, când nu mai știe nimeni de unde vine",
    ),

    # ---- sursa 31.08: declarațiile confruntate cu contabilitatea -----------
    dict(
        id="C-40",
        formula="sold 441 din balanță = impozitul pe profit din D101\n"
                "  și = caseta de impozit pe profit din FIȘA PE PLĂTITOR",
        unde="Balanța la 31.12 vs. D101 depusă vs. fișa pe plătitor de la ANAF",
        legitim="Diferență de rotunjire între lei și lei fără subdiviziuni, dacă\n"
                "  declarația se completează rotunjit.\n"
                "Sold debitor pe 4411 în cursul anului: e plata în plus rămasă după\n"
                "  un trimestru cu pierdere, care se absoarbe la regularizare (F-429).",
        suspect="Impozit declarat trimestru cu trimestru, ca și cum fiecare trimestru\n"
                "  ar fi un exercițiu separat: în T3 impozitul se calculează CUMULAT,\n"
                "  iar cine adună trimestrele plătește pe un profit pe care nu l-a avut.\n"
                "Sold 441 care nu iese cu D101: declarația e greșită, nu balanța.\n"
                "Cheltuiala 691 fără rulaj creditor într-un an cu trimestru pierdut:\n"
                "  semn că diminuarea cumulată n-a fost înregistrată deloc.",
        flux="F-429, F-104",
        severitate="Înaltă — se descoperă la control, cu accesorii pe toată perioada, "
                   "iar reconstituirea cere refacerea tuturor trimestrelor",
    ),
    dict(
        id="C-41",
        formula="609 și 709 au rulaj pe sensul INVERS clasei lor:\n"
                "  609 (clasa 6) rulează în CREDIT · 709 (clasa 7) rulează în DEBIT",
        unde="Fișa de cont / cartea mare, nu balanța",
        legitim="Storno de reducere acordată din greșeală, care readuce contul pe\n"
                "  sensul propriu clasei pentru o singură operațiune.",
        suspect="609 cu rulaj debitor, ca o cheltuială obișnuită: reducerea primită a\n"
                "  fost operată ca achiziție, deci cheltuiala e umflată de două ori.\n"
                "709 cu rulaj creditor: reducerea acordată a fost operată ca vânzare,\n"
                "  deci cifra de afaceri e umflată.",
        flux="F-409",
        severitate="Medie — nu rupe balanța și nu se vede în sold, pentru că soldul "
                   "net poate ascunde un rulaj greșit compensat de altul corect; de "
                   "aceea verificarea se face pe fișă, unde fiecare mișcare are sensul ei",
    ),
    dict(
        id="C-42",
        formula="ACTIV NET din F10 = CAPITALURI PROPRII din F10\n"
                "  și imobilizările din F10 = imobilizările din F40",
        unde="Bilanț: F10 (solduri) · F20 (cheltuieli, venituri, 121) · F30 (salariați) "
             "· F40 (imobilizări)",
        legitim="Nimic. Corelația e o identitate: dacă nu iese, e eroare, nu situație "
                "particulară.",
        suspect="Conturi cu soldul pe invers: în cazul ăsta bilanțul nu se generează\n"
                "  deloc — se repară întâi balanța (vezi C-23).\n"
                "Balanța modificată DUPĂ depunerea bilanțului: nu există bilant\n"
                "  rectificativ, iar diferența se explică în notele bilanțului următor.\n"
                "  La bănci se vede imediat: la creditare confruntă bilanțul cu balanța.",
        flux="F-104",
        severitate="Înaltă — bilanțul depus nu se mai poate corecta, deci eroarea "
                   "rămâne în evidența publică a firmei până la exercițiul următor",
    ),
]
