"""Fluxurile F-45…F-51 — capitaluri, credite, leasing, provizioane.

Sursa: surse/training-2-2026-08-07/notite-revizuit.md (trainingul din 07.08.2026).
Cifrele sunt cele din monografiile corectate din documentul revizuit, nu din
notițele brute (unde exemplul rezervei legale nu se lega, iar la leasing apăreau
typo-urile 1067, 4424 și 615).
"""
from .comun import flux, pas

FLUXURI = [
    # ------------------------------------------------------------------ F-45
    flux(
        "F-45", "Constituire / majorare capital social (456 → 1011 → 1012)",
        roluri="Creanță + Capital propriu",
        conturi="456, 1011, 1012, 5121",
        note="Prag minim: 500 lei firme noi / 5.000 lei la CA netă > 400.000 lei (L. 239/2025)",
        principiu="Momentul 1011 → 1012 este VĂRSAREA EFECTIVĂ, nu înregistrarea la ONRC. "
                  "ONRC validează juridic (naște creanța pe 456); banii o transformă în „vărsat”.",
        pasi=[
            pas(1, "Act constitutiv / Hotărâre AGA + ONRC",
                "Subscrierea capitalului de către asociați. 456 se ține pe ANALITIC PE FIECARE ASOCIAT — "
                "altfel nu poți justifica cine ce datorează.",
                dr=[("456.asociat", 5000)], cr=[("1011", 5000)],
                rol="Creanță față de asociați + Capital subscris nevărsat"),
            pas(2, "Extras de cont",
                "Vărsarea efectivă a aportului în contul societății.",
                dr=[("5121", 5000)], cr=[("456.asociat", 5000)],
                rol="Trezorerie + Stingere creanță"),
            pas(3, "Notă contabilă",
                "Trecerea la „subscris și vărsat”. Se face la vărsare, nu la data înregistrării la ONRC.",
                dr=[("1011", 5000)], cr=[("1012", 5000)],
                rol="Capital nevărsat → capital vărsat (pas revelator)", revelator=True),
            pas(4, "Verificare",
                "Sold 456 = 0 (toți asociații au vărsat). Sold 1011 = 0, sold 1012 = 5.000. "
                "Doar capitalul VĂRSAT (1012) intră în plafonul de 20% al rezervei legale — vezi F-46.",
                rol="Stare terminală: 456 = 0, capital integral pe 1012"),
        ],
    ),
    # ------------------------------------------------------------------ F-46
    flux(
        "F-46", "Repartizarea rezultatului: 121 → 129/1061 → 1171", didactic=True,
        roluri="Colectare / repartizare rezultat",
        conturi="121, 129, 1061, 1171, 457",
        note="Pas revelator: 121 = 129 (NU 129 = 1171). D101",
        principiu="129 are sold DEBITOR, deci se închide prin CREDITARE: `121 = 129`. "
                  "Închiderea lui 121 se face la începutul exercițiului următor, fără să aștepți AGA; "
                  "AGA decide doar ce se întâmplă ulterior cu soldul lui 1171.",
        pasi=[
            pas(1, "Balanță la 31.12.N",
                "După închiderea claselor 6 și 7 (vezi F-37), 121 are sold creditor 2.500 lei = "
                "profitul contabil brut (121 + rulaj 691).",
                rol="121 colectează rezultatul"),
            pas(2, "Notă 31.12.N — rezerva legală",
                "5% din profitul contabil brut = 125 lei. Plafon: 20% din capitalul social subscris "
                "ȘI VĂRSAT (art. 183 L. 31/1990; deductibilă fiscal art. 26 alin. 1 lit. a CF).",
                dr=[("129", 125)], cr=[("1061", 125)],
                rol="Repartizare rezultat → Rezervă legală", declarativ="D101"),
            pas(3, "Notă ianuarie N+1",
                "Închiderea părții repartizate. ⚠ Sensul e `121 = 129`, NU `129 = 1171`: "
                "129 are sold debitor și se stinge prin creditare.",
                dr=[("121", 125)], cr=[("129", 125)],
                rol="Pas revelator: 121 se închide pe 129, nu invers", revelator=True),
            pas(4, "Notă ianuarie N+1",
                "Închiderea profitului rămas nerepartizat în rezultatul reportat. "
                "1171 se ține cu ANALITIC PE AN — condiție pentru urmărirea recuperării pierderii.",
                dr=[("121", 2375)], cr=[("1171.N", 2375)],
                rol="Report rezultat pe an"),
            pas(5, "Hotărâre AGA",
                "Distribuire de dividende din soldul lui 1171. Impozit pe dividende 16% pentru "
                "distribuirile de la 01.01.2026 (L. 141/2025) — cota urmează DATA DISTRIBUIRII, nu a plății. "
                "Se poate distribui doar după rezerva legală și acoperirea integrală a pierderii reportate.",
                dr=[("1171.N", 2375)], cr=[("457", 2375)],
                rol="Repartizare către asociați", declarativ="D100 (impozit dividende)"),
            pas(6, "Verificare",
                "Sold 121 = 0, sold 129 = 0, sold 1061 = 125, sold 1171.N = 0. "
                "Control periodic: Σ rulaj clasa 7 − Σ rulaj clasa 6 = sold 121; dacă nu ține, "
                "cel mai probabil nu ai închis 121 din anul precedent. Nu există automatism ca la TVA.",
                rol="Stare terminală: 121 = 0, 129 = 0, rezultatul e pe 1061 / 1171"),
        ],
    ),
    # ------------------------------------------------------------------ F-47
    flux(
        "F-47", "Corecția erorilor din exerciții anterioare (1174)", didactic=True,
        roluri="Corecție rezultat reportat (ocolește 121)",
        conturi="1174, 1171, 401, 4426, 628",
        note="Pas revelator: cheltuiala nu atinge niciodată 121. D101 rectificativ",
        principiu="1174 NU protejează „profitul anilor precedenți”, ci (1) rezultatul anului CURENT — "
                  "o cheltuială din 2025 nu are ce căuta în P&L-ul lui 2026 — și (2) trasabilitatea: "
                  "arată cât din capitalurile proprii vine dintr-o corecție, nu din profit realizat. "
                  "Transferul ulterior în 1171 nu re-denaturează nimic; denaturarea ar fi fost trecerea prin 121.",
        pasi=[
            pas(1, "Politici contabile — pragul de semnificație",
                "Factură din exercițiul anterior (2025), descoperită în 2026, PESTE pragul de semnificație "
                "definit expres în politicile contabile. Sub prag → se corectează pe 6xx curent (vezi pasul 5).",
                rol="Testul de prag decide contul"),
            pas(2, "Factura + notă contabilă",
                "Eroare semnificativă din exercițiul anterior: cheltuiala merge pe 1174, NU pe 628. "
                "TVA se deduce în decontul CURENT (drept de deducere păstrat 5 ani).",
                dr=[("1174", 10000), ("4426", 2100)], cr=[("401", 12100)],
                rol="Pas revelator: corecția ocolește complet contul 121",
                declarativ="D300 (rând de regularizări)", revelator=True),
            pas(3, "D101 rectificativ",
                "OBLIGATORIU pentru anul afectat — formularul 101 ARE bifă de „Declarație rectificativă” "
                "(spre deosebire de D100, unde se folosește formularul 710). "
                "Situațiile financiare ale anilor trecuți NU se retratează.",
                rol="Declarativ: corecția contabilă fără rectificativă lasă evidența deconectată",
                declarativ="D101 rectificativ"),
            pas(4, "Hotărâre AGA",
                "Închiderea contului tranzitoriu în rezultatul reportat.",
                dr=[("1171.2025", 10000)], cr=[("1174", 10000)],
                rol="1174 = cont tranzitoriu, nu poate rămâne cu sold"),
            pas(5, "Contrast — celelalte trei cazuri",
                "A) Factură a exercițiului CURENT descoperită în același an → înregistrare normală pe 6xx, "
                "nicio rectificare. B) Factură care nu era a mea → storno `628 = 401` și `4426 = 401` cu minus; "
                "efect net 0 pe cheltuială, furnizor și TVA. D) Eroare NEsemnificativă → 6xx curent, cu risc "
                "de nedeductibilitate; documentează decizia de prag.",
                rol="Arborele de decizie complet"),
            pas(6, "Verificare",
                "Sold 1174 = 0 la 31.12. Rezultatul anului curent (121) neatins de corecție. "
                "⚠ Partea sensibilă: dacă 1171 nu mai are sold (dividendele au fost deja luate), transferul îl "
                "duce pe DEBITOR → pierdere reportată neacoperită → restricțiile L. 239/2025 (blocaj dividende, "
                "blocaj restituire împrumuturi asociați). Ordinea corectă: corectezi întâi, distribui după.",
                rol="Stare terminală: 1174 = 0, 121 neatins"),
        ],
    ),
    # ------------------------------------------------------------------ F-48
    flux(
        "F-48", "Rezerve din reevaluare: 105 → 1175 pe măsura amortizării",
        roluri="Capital propriu + Regularizare pe măsura amortizării",
        conturi="105, 1175, 212, 2812, 6811",
        note="1175 a înlocuit 1065 de la 01.01.2015 (OMFP 1802/2014)",
        principiu="Surplusul din reevaluare se consideră realizat fie integral la scoaterea din evidență, "
                  "fie TREPTAT pe măsura amortizării — cu suma = amortizarea pe valoarea reevaluată minus "
                  "amortizarea pe costul inițial. Sumele din 1175 NU pot majora capitalul social "
                  "(art. 210 alin. 3 L. 31/1990), dar pot acoperi pierderi contabile.",
        pasi=[
            pas(1, "Raport de evaluare",
                "Reevaluarea unei clădiri: plus de valoare 12.000 lei, durată rămasă 60 luni.",
                dr=[("212", 12000)], cr=[("105", 12000)],
                rol="Activ imobilizat + Capital propriu (rezervă din reevaluare)"),
            pas(2, "Notă de amortizare lunară",
                "Amortizarea se calculează acum pe valoarea REEVALUATĂ. Diferența față de amortizarea "
                "pe costul inițial = 12.000 / 60 = 200 lei/lună.",
                dr=[("6811", 200)], cr=[("2812", 200)],
                rol="Cheltuială + Rectificativ (doar partea aferentă reevaluării)"),
            pas(3, "Notă concomitentă — transferul surplusului realizat",
                "Se transferă la rezultat reportat exact cât s-a amortizat din plusul de valoare. "
                "1175 se ține cu ANALITIC pe fiecare activ / fiecare reevaluare.",
                dr=[("105", 200)], cr=[("1175", 200)],
                rol="Pas revelator: rezerva devine realizată pe măsura amortizării", revelator=True),
            pas(4, "Verificare + tratament fiscal",
                "Amortizarea aferentă reevaluării ESTE deductibilă, dar rezerva din reevaluare "
                "se impozitează CONCOMITENT cu deducerea — operațiune practic neutră, care însă trebuie "
                "urmărită, altfel apar diferențe la D101. Fără analitic pe 1175 nu poți proba nici "
                "impozitarea corelată, nici ce sumă e distribuibilă.",
                rol="Stare terminală: 105 scade, 1175 crește, efect fiscal neutru",
                declarativ="D101"),
        ],
    ),
    # ------------------------------------------------------------------ F-49
    flux(
        "F-49", "Credit bancar în valută (162x) — cele două momente de diferență de curs", didactic=True,
        roluri="Datorie + Valută (factor V)",
        conturi="1621, 1682, 5124, 666, 627, 665, 765",
        note="Pas revelator: reevaluarea LUNARĂ a soldului, nu doar diferența la plată",
        principiu="Sunt DOUĂ momente de diferență de curs, nu unul: la plată și la reevaluarea lunară a "
                  "soldului. Reevaluarea e LUNARĂ și obligatorie (OMFP 1802/2014) — „la 3 luni” e insuficient. "
                  "Verifică soldul ÎN VALUTĂ, nu doar în lei: sold valută × curs BNR = sold lei.",
        pasi=[
            pas(1, "Scadențar + extras de cont",
                "Sold inițial 1621: 20.000 EUR înregistrat la cursul de 4,9700 = 99.400 lei. "
                "Rata de capital a lunii: 5.000 EUR (înregistrată la 4,9700 = 24.850), plătită la cursul "
                "de 4,9900 = 24.950 lei. Diferența nefavorabilă de 100 lei este primul moment de curs.",
                dr=[("1621", 24850), ("665", 100)], cr=[("5124", 24950)],
                rol="Stingere datorie + Diferență de curs la plată (momentul 1)"),
            pas(2, "Scadențar + extras",
                "Dobânda lunii: 200 EUR × 4,9900 = 998 lei. ⚠ Extrasul arată deseori rata și dobânda "
                "CUMULAT — mergi la scadențar și desparte-le, altfel ajungi cu 1621 pe debit sau cu sold "
                "rămas la finalul creditului, adică ai trecut pe cheltuială mai mult decât trebuia.",
                dr=[("666", 998)], cr=[("5124", 998)],
                rol="Cheltuială financiară (dobândă)"),
            pas(3, "Extras de cont",
                "Comisioane bancare aferente creditului.",
                dr=[("627", 50)], cr=[("5121", 50)],
                rol="Cheltuială cu serviciile bancare"),
            pas(4, "Notă de reevaluare la ultima zi bancară a lunii",
                "Sold rămas 15.000 EUR, înregistrat la 4,9700 = 74.550 lei. Curs BNR la 31: 5,0100 → "
                "75.150 lei. Datoria crește cu 600 lei = diferență nefavorabilă.",
                dr=[("665", 600)], cr=[("1621", 600)],
                rol="Pas revelator: al doilea moment de curs — reevaluarea lunară a soldului",
                revelator=True),
            pas(5, "Verificare",
                "Sold 1621 = 74.550 + 600 = 75.150 lei = 15.000 EUR × 5,0100. ✔ "
                "Reclasifică porțiunea scadentă în ≤ 12 luni pentru bilanț (prin analitic sau cont dedicat). "
                "1621…1627 sunt sintetice DISTINCTE, nu analitice ale aceluiași cont; dobânda calculată și "
                "neajunsă la scadență stă pe 1682.",
                rol="Stare terminală: sold în lei = sold în valută × curs BNR",
                declarativ="Situații financiare (scadență <1an / >1an)"),
        ],
    ),
    # ------------------------------------------------------------------ F-50
    flux(
        "F-50", "Leasing financiar autoturism cu deductibilitate 50%", didactic=True,
        roluri="Datorie 167 + Activ imobilizat + Fiscal (trei limitări simultane)",
        conturi="4093, 167, 2133, 2813, 6811, 666, 628, 613, 4426, 6588, 404",
        note="Pas revelator: 167 este 1-la-1 cu contractul. D300, D101",
        principiu="167 este 1-la-1 cu CONTRACTUL de leasing — indiferent câte bunuri conține — și pe tip de "
                  "valută; fără analitic pe contract nu poți reevalua soldul la rata corectă din scadențar. "
                  "Cele trei limitări fiscale se aplică simultan dar pe BAZE DIFERITE: TVA 50%, cheltuieli 50%, "
                  "amortizare plafonată la 1.500 lei/lună. ⚠ Amortizarea NU intră sub limitarea de 50% — "
                  "are propria plafonare; cele două nu se cumulează.",
        pasi=[
            pas(1, "Factura de avans",
                "Contract 150.000 lei valoare de intrare, avans 50.000 lei, TVA 21%.",
                dr=[("4093", 50000), ("4426", 10500)], cr=[("404", 60500)],
                rol="Avans pentru imobilizări + TVA deductibilă", declarativ="D300"),
            pas(2, "Notă contabilă",
                "TVA nedeductibilă pe avans (50% × 10.500), CAPITALIZATĂ în valoarea bunului: taxele "
                "nerecuperabile intră în costul de achiziție (OMFP 1802/2014). Varianta din notiță "
                "(`4426 = 404` de roșu + `2133 = 404` de negru) dă exact același rezultat.",
                dr=[("2133", 5250)], cr=[("4426", 5250)],
                rol="TVA nerecuperabilă → cost de achiziție"),
            pas(3, "Proces-verbal de recepție",
                "Intrarea bunului în patrimoniu și nașterea datoriei față de societatea de leasing.",
                dr=[("2133", 150000)], cr=[("167.contract", 150000)],
                rol="Activ imobilizat + Datorie pe contract"),
            pas(4, "Notă contabilă",
                "Închiderea avansului în datoria de leasing.",
                dr=[("167.contract", 50000)], cr=[("4093", 50000)],
                rol="Stingere avans"),
            pas(5, "Plan de amortizare",
                "Valoare de intrare = 150.000 + 5.250 = 155.250 lei. Amortizare contabilă pe 60 luni = "
                "2.587,50 lei/lună. Deductibil fiscal DOAR 1.500 lei/lună (art. 28 alin. 14 CF) → "
                "nedeductibil 1.087,50 lei/lună. Acesta e elementul cu cel mai mare impact pe impozitul pe profit.",
                dr=[("6811", 2587.50)], cr=[("2813", 2587.50)],
                rol="Pas revelator: plafonul de 1.500 lei/lună e SEPARAT de limitarea de 50%",
                declarativ="D101", revelator=True),
            pas(6, "Factura lunară de leasing",
                "Se înregistrează la valoarea ei, fără split. Comisionul poate fi și pe 627 — "
                "aliniază-te la politica firmei și fii consecvent.",
                dr=[("167.contract", 2000), ("666", 500), ("628", 100), ("613", 20), ("4426", 546)],
                cr=[("404", 3166)],
                rol="Rată capital + dobândă + comision + CASCO + TVA", declarativ="D300"),
            pas(7, "Notă — corecția TVA nedeductibilă (50%)",
                "Din TVA total 546 lei (420 rată + 105 dobândă + 21 comision), 273 lei sunt nedeductibili. "
                "⚠ În notiță apărea `4426 = 4424` — typo; contrapartida corectă e 4426. "
                "❓ De clarificat cu formatorul: TVA nedeductibilă pe RATA DE CAPITAL (210 lei) se "
                "capitalizează în 2133 (coerent cu tratamentul avansului) sau se trece pe cheltuială (6588/635)? "
                "Practica e împărțită. Dacă merge pe cheltuială, e integral nedeductibilă — nu se mai aplică "
                "încă o dată 50%, ar fi dublă limitare.",
                dr=[("6588", 210), ("666", 52.50), ("628", 10.50)], cr=[("4426", 273)],
                rol="TVA nedeductibilă pe destinația finală", declarativ="D300, D101"),
            pas(8, "Notă — limitarea de 50% a cheltuielilor",
                "Baza include TVA nedeductibilă deja trecută pe cheltuială: 666 = 500 + 52,50 = 552,50 → "
                "nedeductibil 276,25. 628 = 100 + 10,50 = 110,50 → 55,25. 613 = 20 → 10,00. "
                "⚠ Contul de contrapartidă nedeductibil pentru CASCO este 613.NED, NU 615 "
                "(615 = cheltuieli cu pregătirea personalului). Dacă leasingul e în EUR, diferențele de curs "
                "intră și ele în baza limitării.",
                dr=[("666.NED", 276.25), ("628.NED", 55.25), ("613.NED", 10.00)],
                cr=[("666", 276.25), ("628", 55.25), ("613", 10.00)],
                rol="Reclasificare pe analitice nedeductibile (art. 25 alin. 3 lit. l CF)",
                declarativ="D101"),
            pas(9, "Verificare",
                "Sold 167 pe contract = soldul din scadențar, în valuta contractului (C-19). "
                "Valoare 2133 = 155.250. Impozit local pe mijlocul de transport: declarație la primărie în "
                "30 de zile, datorat de LOCATAR pe toată durata contractului. Verifică pe fiecare factură "
                "rata de schimb comunicată de firma de leasing față de scadențar.",
                rol="Stare terminală: 167 = scadențar, 4093 = 0, valoare de intrare completă"),
        ],
    ),
    # ------------------------------------------------------------------ F-51
    flux(
        "F-51", "Provizioane pentru litigii (151x) — constituire și reluare",
        roluri="Provizion (datorie estimată)",
        conturi="1511, 6812, 7812, 628, 401",
        note="Nedeductibil fiscal — nu e optimizare, e imagine fidelă",
        principiu="Factura NU se înregistrează „pe 151”. Provizionul nu e o datorie față de furnizor. "
                  "Constituirea și reluarea sunt operațiuni INDEPENDENTE de factura propriu-zisă; "
                  "efectul net pe rezultatul anului următor este ~zero, ceea ce e chiar scopul provizionului.",
        pasi=[
            pas(1, "Hotărâre + estimare (31.12.2026)",
                "Litigiu în curs; obligația s-a născut în exercițiul curent, chiar dacă plata vine anul "
                "următor. Condiții: obligație actuală din eveniment trecut, ieșire probabilă de resurse, "
                "sumă estimabilă credibil.",
                dr=[("6812", 8000)], cr=[("1511", 8000)],
                rol="Cheltuială de exploatare + Provizion", declarativ="D101 (nedeductibil)"),
            pas(2, "Factura de la avocat (2027)",
                "Înregistrare NORMALĂ pe cheltuială. Nu atinge contul 1511.",
                dr=[("628", 8000), ("4426", 1680)], cr=[("401", 9680)],
                rol="Cheltuială efectivă + TVA deductibilă", declarativ="D300"),
            pas(3, "Notă contabilă (2027) — reluarea provizionului",
                "Operațiune SEPARATĂ de factură. Provizionul se revizuiește la fiecare dată a bilanțului și "
                "nu poate fi utilizat pentru altă cheltuială decât cea pentru care a fost constituit.",
                dr=[("1511", 8000)], cr=[("7812", 8000)],
                rol="Pas revelator: reluarea e independentă de factură", revelator=True),
            pas(4, "Verificare + tratament fiscal",
                "Sold 1511 = 0; efectul net pe rezultatul lui 2027 ≈ 0. "
                "⚠ Provizioanele pentru LITIGII sunt NEDEDUCTIBILE (art. 26 CF enumeră limitativ ce e "
                "deductibil — litigiile nu sunt pe listă). Prin simetrie, reluarea pe 7812 este venit "
                "neimpozabil. Nu-l vinde clientului ca optimizare fiscală.",
                rol="Stare terminală: 1511 = 0, efect fiscal neutru", declarativ="D101"),
        ],
    ),
    # ==================================================================
    # Trainingul 26.08.2026 — dividende și creditarea de societate
    #
    # Toate șase pleacă din același loc: ce se întâmplă cu rezultatul DUPĂ ce F-104
    # l-a închis, și cu banii pe care asociatul îi bagă sau îi scoate. Sunt clasa 1
    # pentru că patrimoniul lor e capitalul propriu, chiar dacă decontarea trece
    # prin conturi de clasa 4 (455, 456, 457, 463).
    # ==================================================================
    # ------------------------------------------------------------------ F-71
    flux(
        "F-71", "Dividende certe din rezultatul reportat (1171 → 457)", didactic=True,
        roluri="Capital propriu → Datorie față de asociați",
        conturi="1171, 457, 446, 1012, 5121",
        note="Impozit 16%. Termen de plată: 25.01 a anului următor repartizării, CHIAR "
             "DACĂ dividendele nu au fost ridicate. D100 + D205",
        principiu="Hotărârea AGA e documentul repartizării, nu SURSA cotelor. Cotele "
                  "vin din analiticele lui 1012, iar ordinea de lucru e: mai întâi "
                  "balanța, apoi actul. Fără hotărâre AGA nu se înregistrează nimic — "
                  "e cel mai frecvent caz ajuns la comisia de disciplină.",
        pasi=[
            pas(1, "Balanță la 31.12 + certificat constatator ONRC",
                "1171.2025 are sold creditor 30.000 lei, iar 1012 e spart pe trei "
                "analitice de câte 33,33%. Condiție prealabilă: 1171 NU are sold "
                "debitor pe niciun an — cu pierdere neacoperită nu se distribuie nimic, "
                "nici cert, nici interimar.",
                rol="Verificarea prealabilă: sursa există și e repartizabilă"),
            pas(2, "Hotărâre AGA",
                "Repartizarea a câte 10.000 lei către fiecare asociat, în cotele din "
                "1012. 457 se ține pe analitic pe persoană, în oglindă cu 1012 — altfel "
                "nu poți spune cui i-ai plătit și cui nu.",
                dr=[("1171.2025", 30000)],
                cr=[("457.1", 10000), ("457.2", 10000), ("457.3", 10000)],
                rol="Pas revelator: cotele se citesc din 1012, nu se inventează în AGA",
                revelator=True, declarativ="D100 (impozit dividende)"),
            pas(3, "Notă contabilă — reținerea impozitului",
                "16% × 10.000 = 1.600 lei pe fiecare asociat. Pe fiecare analitic de "
                "457 rămâne un rest de plată de 8.400 lei.",
                dr=[("457.1", 1600), ("457.2", 1600), ("457.3", 1600)],
                cr=[("446.dividende", 4800)],
                rol="Datorie față de asociat → datorie față de buget"),
            pas(4, "Ordin de plată — impozitul",
                "Se plătește până la 25.01 a anului următor, indiferent dacă asociatul "
                "a ridicat sau nu banii. Obligația e față de buget, nu față de asociat.",
                dr=[("446.dividende", 4800)], cr=[("5121", 4800)],
                rol="Stingerea datoriei fiscale", declarativ="D100"),
            pas(5, "Ordin de plată — dividendele nete",
                "8.400 lei × 3. Poate rămâne neridicat: atunci soldul lui 457 persistă, "
                "iar impozitul e deja plătit.",
                dr=[("457.1", 8400), ("457.2", 8400), ("457.3", 8400)],
                cr=[("5121", 25200)],
                rol="Plata către asociați"),
            pas(6, "Verificare",
                "Sold 1171.2025 = 0, sold 446.dividende = 0, sold 457 = 0 pe fiecare "
                "analitic (dacă s-a ridicat tot). Verificarea încrucișată de la sfârșit "
                "de an: D205 se confruntă cu D100 și cu fișa contului 446 din balanță — "
                "cazul căutat e o plată făcută fără declarație.",
                rol="Stare terminală: 1171 repartizat integral, 446 = 0, 457 = 0",
                declarativ="D205 (informativă, anuală)"),
        ],
    ),
    # ------------------------------------------------------------------ F-72
    flux(
        "F-72", "Dividende interimare (463) cu plafonul soldului lui 121", didactic=True,
        roluri="Creanță temporară față de asociat + Colectare rezultat",
        conturi="463, 456, 446, 121, 1171, 5121",
        note="Cer inventariere ȘI bilanț interimar; se acordă doar trimestrial. "
             "Bilanțul interimar se depune până la 31 iulie.",
        principiu="Soldul debitor al lui 463 e o CREANȚĂ până la 31.12, nu o cheltuială "
                  "consumată: banii au plecat pe seama unui profit care încă nu s-a "
                  "realizat. Plafonul nu e o recomandare — e soldul lui 121 la data "
                  "bilanțului interimar, iar în practică se stă sub el, pentru că "
                  "nimeni nu știe cum arată decembrie.",
        pasi=[
            pas(1, "Inventariere + bilanț interimar la 30.06",
                "După închiderea a șase luni și după înregistrarea impozitului, 121 are "
                "sold creditor 80.000 lei. Administratorul vrea să ridice 100.000 — nu "
                "poate: plafonul e profitul realizat, nu disponibilul din bancă.",
                rol="Sursa plafonului: soldul lui 121, nu extrasul de cont"),
            pas(2, "Hotărâre AGA (iulie) — înregistrare în iunie",
                "Calendarul care nu e intuitiv: hotărârea se ia în iulie, pentru că are "
                "nevoie de balanța închisă, dar înregistrarea se face în IUNIE, luna "
                "bilanțului interimar — acolo are bilanțul rubrică separată pentru 463, "
                "deci acolo vede ANAF ce s-a repartizat.",
                dr=[("463", 80000)], cr=[("456.administrator", 80000)],
                rol="Pas revelator: maximul repartizabil e soldul lui 121",
                revelator=True),
            pas(3, "Notă contabilă — impozitul",
                "16% × 80.000 = 12.800 lei.",
                dr=[("456.administrator", 12800)], cr=[("446.dividende", 12800)],
                rol="Datorie fiscală", declarativ="D100"),
            pas(4, "Ordin de plată",
                "Din 100.000 pe care îi vedea în bancă, administratorul ridică 67.200.",
                dr=[("456.administrator", 67200)], cr=[("5121", 67200)],
                rol="Plata efectivă"),
            pas(5, "Verificare",
                "Sold 456 = 0. Sold 463 = 80.000 DEBITOR și rămâne așa până la 31.12, "
                "când se compară cu 121 — vezi pașii de regularizare din același flux la "
                "F-110 în varianta cu profit mai mic. Corelația de urmărit: sold 463 ≤ "
                "sold 121 la orice moment.",
                rol="Stare terminală: 456 = 0, 463 = 80.000 D în așteptarea lui 31.12"),
        ],
    ),
    # ------------------------------------------------------------------ F-73
    flux(
        "F-73", "Creditarea de societate (4551) — analitic pe asociat", didactic=True,
        roluri="Datorie față de asociat",
        conturi="4551, 5121",
        note="Contract pentru fiecare creditare (sau unul pe lună, pe totalul fișei). "
             "Restricții de numerar: vezi plafoanele din L. 70/2015.",
        principiu="4551 e cont de PASIV și trebuie să apară doar pe credit. Un sold "
                  "debitor înseamnă ori înregistrare greșită, ori că asociatul a ridicat "
                  "mai mult decât a pus. Analiticele nu se compensează între ele: "
                  "creditarea unui asociat nu poate stinge ridicarea altuia decât prin "
                  "act notarial — nu pe cuvânt și nu pe mesaj.",
        pasi=[
            pas(1, "Contract de creditare + extras de cont",
                "Asociatul A creditează societatea cu 20.000 lei. Contractul nu trebuie "
                "să fie complicat, dar trebuie să existe: înregistrarea din bancă nu e "
                "document justificativ. Se poate genera din soft și doar semnat.",
                dr=[("5121", 20000)], cr=[("4551.A", 20000)],
                rol="Naște datoria față de asociat"),
            pas(2, "Extras de cont",
                "Asociatul B ridică 15.000 lei, deși 4551.B are sold zero. Contul lui "
                "trece pe DEBIT — un cont de pasiv cu sold contrar naturii, adică "
                "semnalul din C-23 aplicat aici.",
                dr=[("4551.B", 15000)], cr=[("5121", 15000)],
                rol="Sold debitor pe un cont de pasiv: semnal, nu curiozitate"),
            pas(3, "Notă contabilă RESPINSĂ",
                "Tentația e `4551.B = 4551.A` pe 15.000, ca soldul debitor să dispară. "
                "Nu se poate: sunt doi asociați diferiți, iar compensarea are nevoie de "
                "o înțelegere notarială. Fără ea, soldul debitor rămâne la vedere și se "
                "lămurește — ori B restituie, ori suma se documentează ca dividend, "
                "avans de trezorerie sau împrumut, fiecare cu contul lui.",
                rol="Pas revelator: analiticele nu se compensează între ele",
                revelator=True),
            pas(4, "Extras de cont",
                "B restituie. Administratorul nu ține minte cât a creditat și cât a "
                "ridicat — de aceea contul se urmărește pe analitic, în ambele sensuri.",
                dr=[("5121", 15000)], cr=[("4551.B", 15000)],
                rol="Stingerea soldului debitor"),
            pas(5, "Verificare",
                "Sold 4551.A = 20.000 creditor, sold 4551.B = 0. Niciun analitic cu sold "
                "debitor. Ținta finală a contului e soldul 0 pe fiecare asociat.",
                rol="Stare terminală: 4551 fără sold debitor pe niciun analitic"),
        ],
    ),
    # ------------------------------------------------------------------ F-74
    flux(
        "F-74", "Majorarea capitalului social din creditare (4551 → 456 → 1011 → 1012)",
        didactic=True,
        roluri="Datorie față de asociat → Capital propriu",
        conturi="4551, 456, 1011, 1012",
        note="Două documente obligatorii: hotărârea AGA și expertiza contabilă care "
             "atestă că sumele sunt certe, lichide și exigibile.",
        principiu="Trecerea 1011 → 1012 se face DUPĂ înregistrarea la ONRC, nu la data "
                  "hotărârii: până atunci capitalul e subscris, nu vărsat. Expertiza "
                  "contabilă nu e formalitate — ea atestă că banii au existat cu "
                  "adevărat, au fost virați și au contract în spate.",
        pasi=[
            pas(1, "Hotărâre AGA + expertiză contabilă",
                "Asociatul renunță la 5.000 lei din creditare, care devin aport. "
                "Expertiza atestă că sumele sunt certe, lichide și exigibile — adică "
                "exact ce demonstrează contractele cerute la F-73.",
                dr=[("4551.A", 5000)], cr=[("456.A", 5000)],
                rol="Datoria față de asociat devine aport subscris"),
            pas(2, "Notă contabilă",
                "Constituirea capitalului subscris nevărsat.",
                dr=[("456.A", 5000)], cr=[("1011", 5000)],
                rol="Capital subscris nevărsat"),
            pas(3, "Certificat de înregistrare a mențiunii la ONRC",
                "Abia acum capitalul e „vărsat”. Distincția pe care formatorul o "
                "subliniază: ACȚIONARII creditează societatea, ASOCIAȚII constituie "
                "capitalul social.",
                dr=[("1011", 5000)], cr=[("1012.A", 5000)],
                rol="Pas revelator: 1011 → 1012 la ONRC, nu la hotărâre",
                revelator=True),
            pas(4, "Verificare",
                "Sold 456 = 0, sold 1011 = 0, 1012.A crescut cu 5.000, iar 4551.A scăzut "
                "cu aceeași sumă. Cotele din denumirile analiticelor lui 1012 se "
                "recalculează — altfel F-114 pică la prima hotărâre AGA.",
                rol="Stare terminală: 456 = 0, 1011 = 0, cotele din 1012 recalculate"),
        ],
    ),
    # ------------------------------------------------------------------ F-75
    flux(
        "F-75", "Remiterea de datorie (4551 → 7582)", didactic=True,
        roluri="Datorie față de asociat → Venit",
        conturi="4551, 7582, 121",
        note="Act notarial, în baza acelorași două documente ca la majorarea de capital: "
             "hotărârea AGA și expertiza contabilă.",
        principiu="Din două înregistrări, o societate în pierdere trece pe profit. "
                  "Rezultatul e real și impozabil, dar SUBSTANȚA lui nu e activitatea: "
                  "vine dintr-o renunțare. Formal, 7582 e venit din exploatare — grupa "
                  "758 stă în partea de exploatare a contului de profit și pierdere — "
                  "deci cine citește doar linia „rezultat din exploatare” nu vede "
                  "diferența. De aceea contul se ține pe analitic pe asociat.",
        pasi=[
            pas(1, "Balanță",
                "Societatea are pierdere de 100.000 lei și o creditare de 120.000 lei de "
                "la asociat. Sugestia care circulă la firmele în impas: renunțarea la "
                "creditare.",
                rol="Starea inițială: pierdere și datorie față de asociat"),
            pas(2, "Act de remitere de datorie (notarial) + AGA + expertiză",
                "Suma la care asociatul renunță devine venit. Actul se face prin "
                "notariat — nu printr-o declarație pe proprie răspundere.",
                dr=[("4551.A", 120000)], cr=[("7582", 120000)],
                rol="Pas revelator: datoria stinsă fără plată este venit",
                revelator=True),
            pas(3, "Notă de închidere (F-104)",
                "Venitul se închide în rezultat, ca orice cont de clasa 7.",
                dr=[("7582", 120000)], cr=[("121", 120000)],
                rol="Colectare rezultat"),
            pas(4, "Verificare",
                "Sold 4551.A = 0, sold 7582 = 0 după închidere, iar 121 trece de la "
                "−100.000 la +20.000. Profit de 20.000 lei fără nicio operațiune de "
                "exploatare — de citit ca atare la analiza rezultatului și la calculul "
                "impozitului.",
                rol="Stare terminală: 4551 = 0, rezultatul pe profit din remitere"),
        ],
    ),
    # ------------------------------------------------------------------ F-76
    flux(
        "F-76", "Analiticele pe 1012 = cotele de participare (procedură de control)",
        didactic=True,
        roluri="Procedură de control — balanța ca sursă unică",
        conturi="1012, 457, 456",
        note="Fără sume: e o procedură de verificare, ca F-214. Se rulează înainte de "
             "ORICE hotărâre AGA de repartizare.",
        principiu="Balanța trebuie să vorbească de la sine. Când vine hotărârea AGA, "
                  "verifici direct în balanță ce cotă are fiecare asociat, fără să "
                  "deschizi actul constitutiv — iar dacă cele două nu spun același "
                  "lucru, afli înainte de a înregistra, nu după.",
        pasi=[
            pas(1, "Sursa 1 — certificat constatator ONRC / act constitutiv",
                "Cotele de participare, așa cum sunt înregistrate juridic. La firmele "
                "noi luate în lucru, ele sunt singura sursă disponibilă.",
                rol="Sursa juridică a cotelor"),
            pas(2, "Sursa 2 — balanța, contul 1012",
                "1012 se ține pe analitic PE ASOCIAT, iar denumirea analiticului poartă "
                "procentul: `1012.1 = Ionescu 33,3%`, `1012.2 = Popescu 33,3%`, "
                "`1012.3 = Xulescu 33,3%`.",
                rol="Sursa contabilă a cotelor"),
            pas(3, "Confruntarea",
                "Σ analitice 1012 = soldul sintetic al lui 1012, iar Σ procente din "
                "denumiri = 100%. Amândouă trebuie să țină simultan: prima spune că nu "
                "s-a pierdut nimic, a doua că nu s-a inventat nimic.",
                rol="Pas revelator: balanța răspunde singură la „cine cât deține”",
                revelator=True),
            pas(4, "Firma nouă cu 1012 „la grămadă”",
                "Procedura de spargere: se ia cota de la ONRC și se creează analiticele, "
                "înainte de prima repartizare. Nu se amână până la AGA — atunci e prea "
                "târziu ca să mai fie o verificare.",
                rol="Procedura de remediere"),
            pas(5, "Ce rupe corelația",
                "Fuziunile și cedările de părți sociale: cotele se schimbă, analiticele "
                "rămân. Exact cazurile ajunse la comisia de disciplină la ANAF, pentru "
                "că experții contabili nu obținuseră procentele pe analitice. "
                "Consecința nu e doar a firmei — afectează și persoana, la ce poate "
                "ridica din societate.",
                rol="Momentele în care corelația cedează"),
            pas(6, "Verificare",
                "1012 spart pe asociați, Σ analitice = sintetic, Σ procente = 100%, iar "
                "repartizarea din orice hotărâre AGA se poate contraverifica din balanță "
                "în două minute.",
                rol="Stare terminală: cotele sunt citibile din balanță, fără acte"),
        ],
    ),
    # ------------------------------------------------------------------ F-91
    # Cifrele NU vin din notițe: notița din 28.08 spunea doar „se cumpără la un preț,
    # se răscumpără la un preț + cheltuieli la un curs valutar”, cu „de detaliat”
    # adresat mie. Exemplul de mai jos e construit de mine ca să fie autoconsistent și
    # să treacă poarta 1 — e ilustrativ, nu dictat de formator. Rămâne de confirmat cu
    # el (întrebarea „training 28.08.2026, punctul 9”).
    flux(
        "F-91", "Emisiune și răscumpărare de obligațiuni proprii (161 / 169 / 505)",
        didactic=True,
        roluri="Împrumut obligatar + Primă de rambursare + Răscumpărare de titluri proprii",
        conturi="161, 169, 1681, 505, 461, 512, 666, 686, 668, 768, 665",
        note="Emitentul, nu investitorul: 161 e datoria, 505 sunt propriile obligațiuni "
             "răscumpărate. Investitorul care CUMPĂRĂ obligațiunile altcuiva le ține pe "
             "506 — alt cont, altă poveste (vezi §2.2 din documentul de trezorerie).",
        principiu="Prețul de EMISIUNE și cel de RAMBURSARE sunt două lucruri diferite, "
                  "iar diferența dintre ele — prima de rambursare (169) — nu e nici "
                  "cheltuială la emisiune, nici venit: e un cost al finanțării, întins "
                  "pe toată durata împrumutului prin 686. Răscumpărarea propriilor "
                  "obligațiuni înainte de scadență nu stinge datoria la preț de piață, "
                  "ci ANULEAZĂ nominalul (161) contra prețului plătit (505) și a primei "
                  "neamortizate aferente (169) — iar ce rămâne e câștig (768) sau "
                  "pierdere (668), nu o simplă plată.",
        pasi=[
            pas(1, "Prospect de emisiune + subscriere",
                "1.000 de obligațiuni, valoare nominală (= de rambursare) 100 lei, "
                "emise la 95 lei. Se încasează prețul de emisiune (95.000), dar datoria "
                "se naște la valoarea de RAMBURSARE (100.000). Diferența de 5.000 e "
                "prima de rambursare, un activ care se va amortiza.",
                dr=[("461.subscriitori", 95000), ("169", 5000)],
                cr=[("161.emisiune", 100000)],
                rol="Creanță subscriere + Primă (169) + Datoria la valoarea de rambursare"),
            pas(2, "Extras de cont — încasarea subscrierii",
                "Banii intră la prețul de emisiune, nu la nominal.",
                dr=[("512", 95000)], cr=[("461.subscriitori", 95000)],
                rol="Trezorerie + stingerea creanței de subscriere"),
            pas(3, "Nota anuală — cuponul și amortizarea primei",
                "Cuponul de 10% pe an se calculează pe NOMINAL (100.000), deci 10.000 "
                "lei, recunoscut și plătit. În paralel, prima se amortizează liniar pe "
                "cei 5 ani: 5.000 ÷ 5 = 1.000 lei/an, pe cheltuială financiară (686). "
                "Cuponul e remunerația; amortizarea primei e costul emisiunii sub par.",
                dr=[("666", 10000), ("1681", 10000), ("686", 1000)],
                cr=[("1681", 10000), ("512", 10000), ("169", 1000)],
                rol="Cheltuială cu dobânda + amortizarea primei de rambursare"),
            pas(4, "Răscumpărarea și anularea a 200 de obligațiuni proprii (anul 3)",
                "După doi ani de amortizare, societatea cumpără de pe piață 200 din "
                "propriile obligațiuni la 98 lei = 19.600 lei (pe 505). Apoi le "
                "ANULEAZĂ: stinge nominalul de 20.000 (161) și scoate prima neamortizată "
                "aferentă — 3.000 rămas × 200/1.000 = 600 (169). Datoria netă anulată e "
                "20.000 − 600 = 19.400; s-au plătit 19.600, deci o pierdere de 200 (668).",
                dr=[("161.emisiune", 20000), ("668", 200)],
                cr=[("505", 19600), ("169", 600)],
                rol="Pas revelator: răscumpărarea nu e plată, e anulare cu rezultat",
                revelator=True),
            pas(5, "Scadența finală — rambursarea celor 800 rămase, emise în valută",
                "Dacă emisiunea fusese în valută, la rambursare apare și diferența de "
                "curs. Ilustrativ, pe un tranșon de 100 de obligațiuni EUR (nominal 100 "
                "EUR, curs emisiune 4,95 → 49.500 lei), rambursate la curs 5,05 = 50.500 "
                "lei: diferența de 1.000 lei e nefavorabilă și merge pe 665 (nu pe 668 — "
                "e diferență de curs pe un element monetar).",
                dr=[("161.emisiune.EUR", 49500), ("665", 1000)],
                cr=[("512", 50500)],
                rol="Rambursarea la scadență, cu diferența de curs pe 665"),
            pas(6, "Verificare",
                "Sold 161 = 0 după rambursarea integrală, sold 169 = 0 (amortizat plus "
                "porțiunea anulată la răscumpărare), sold 505 = 0 (obligațiunile proprii "
                "s-au anulat, nu se păstrează în portofoliu), sold 1681 = 0 după fiecare "
                "cupon plătit. 505 cu sold la sfârșit de an = obligațiuni proprii "
                "răscumpărate și neanulate — un titlu care se ține pe sine, semnal de "
                "anulare uitată.",
                rol="Stare terminală: 161 = 0, 169 = 0, 505 = 0"),
        ],
    ),

    # ------------------------------------------------------------------ F-94
    # Capcana descrisă în notițele 31.08: profit în T1, pierdere în T2, „declar 0”, iar
    # în T3 impozitul se calculează CUMULAT. Fluxul o arată cu cifre, pentru că pe cifre
    # se vede ce nu se vede în vorbe: contul 691 trebuie să scadă, iar 4411 trece prin
    # sold debitor — adică prin exact semnalul pe care C-23 îl tratează ca eroare.
    flux(
        "F-94", "Impozitul pe profit se calculează cumulat, nu pe trimestru "
                "(691 / 4411)", didactic=True,
        roluri="Datorie fiscală recalculată de la începutul anului, nu adunată pe bucăți",
        conturi="691, 4411, 5121",
        note="Profit cumulat: 100.000 la 31.03, 60.000 la 30.06, 150.000 la 30.09. "
             "Cota de impozit pe profit 16%.",
        principiu="Impozitul pe profit e datorat pe REZULTATUL CUMULAT de la începutul "
                  "anului, nu pe rezultatul fiecărui trimestru luat separat. De aceea "
                  "691 e singurul cont de cheltuială din sistem care are rulaj normal pe "
                  "ambele sensuri: când profitul cumulat scade, cheltuiala înregistrată "
                  "anterior trebuie diminuată. Cine adună trimestrele ca pe niște "
                  "exerciții separate plătește impozit pe un profit pe care nu l-a avut.",
        pasi=[
            pas(1, "Declarația D100 — trimestrul I",
                "Profit cumulat la 31.03: 100.000 lei. Impozit: 16% × 100.000 = 16.000 lei.",
                dr=[("691", 16000)], cr=[("4411", 16000)],
                rol="Constituirea datoriei pe rezultatul cumulat al T1"),
            pas(2, "Ordin de plată — trimestrul I",
                "Se plătește tot, pentru că nu s-a plătit nimic înainte.",
                dr=[("4411", 16000)], cr=[("5121", 16000)],
                rol="Stingerea datoriei T1"),
            pas(3, "Declarația D100 — trimestrul II",
                "Trimestrul II aduce pierdere, iar profitul CUMULAT scade la 60.000 lei. "
                "Impozitul cumulat datorat devine 16% × 60.000 = 9.600 lei, dar în "
                "contabilitate e deja înregistrat 16.000. Diferența de "
                "16.000 − 9.600 = 6.400 lei se STORNEAZĂ: cheltuiala cu impozitul scade. "
                "4411 rămâne cu sold DEBITOR de 6.400 — nu e o eroare de tipul C-23, e o "
                "plată în plus, reală, care se va regulariza.",
                dr=[("4411", 6400)], cr=[("691", 6400)],
                rol="Pas revelator: cheltuiala cu impozitul poate să scadă",
                revelator=True),
            pas(4, "Declarația D100 — trimestrul III",
                "Profit cumulat la 30.09: 150.000 lei. Impozit cumulat: "
                "16% × 150.000 = 24.000 lei. Înregistrat până acum, net: 9.600 lei. "
                "Diferența de completat: 24.000 − 9.600 = 14.400 lei.",
                dr=[("691", 14400)], cr=[("4411", 14400)],
                rol="Completarea până la impozitul cumulat"),
            pas(5, "Ordin de plată — trimestrul III",
                "Datorat cumulat 24.000, plătit deja 16.000, deci se virează "
                "24.000 − 16.000 = 8.000 lei. Soldul debitor de 6.400 din T2 se absoarbe "
                "aici, fără să fi fost vreodată cerut înapoi de la buget.",
                dr=[("4411", 8000)], cr=[("5121", 8000)],
                rol="Stingerea prin diferență, nu prin sumă nouă"),
            pas(6, "Verificare",
                "Σ691 = 16.000 − 6.400 + 14.400 = 24.000, adică exact 16% din profitul "
                "cumulat de 150.000. Sold 4411 = 0 după plata din T3. Regula de "
                "contraverificare a formatorului: soldul din D101 trebuie să iasă cu 441 — "
                "dacă nu iese, declarația e greșită, nu balanța. Instrumentul e caseta de "
                "impozit pe profit din fișa pe plătitor, listată și confruntată cu balanța.",
                rol="Stare terminală: 4411 = 0, Σ691 = impozitul pe rezultatul cumulat"),
        ],
    ),
]
