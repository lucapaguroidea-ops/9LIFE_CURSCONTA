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
]
