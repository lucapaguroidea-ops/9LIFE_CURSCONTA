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
]
