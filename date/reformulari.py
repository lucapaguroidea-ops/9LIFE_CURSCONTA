"""Textele din originalul training 4 care au voie să dispară, fiecare cu motiv.

Poarta de conservare (build/conservare.py) verifică faptul că nimic din conținutul
original nu se pierde. Când un text chiar TREBUIE înlocuit — pentru că era greșit
sau pentru că a devenit fals — se trece aici, explicit. Fără intrare în lista asta,
build-ul pică.

Regula: se declară doar CORECȚII și STATUSURI DEVENITE FALSE. Dacă textul original
era pur și simplu mai scurt decât cel nou, nu se declară — se contopesc (vezi
auto-merge-ul din build/build_plan.py, care păstrează originalul și adaugă la el).
"""

INLOCUIRI = [
    # ---- notații de cont greșite în coloana „Analitice recomandate” ----------
    dict(
        text="101.1 nevarsat / 101.2 varsat",
        motiv="Notație inexistentă. OMFP 1802/2014 definește conturile 1011 „Capital "
              "subscris nevărsat” și 1012 „Capital subscris vărsat” — nu analitice "
              "„101.1 / 101.2” ale lui 101.",
        devine="1011 subscris nevărsat / 1012 subscris vărsat [N]",
    ),
    dict(
        text="151.1 litigii / 151.2 garanții / 151.8 alte [N]",
        motiv="Aceeași problemă de notație: conturile sunt 1511, 1512, 1514, 1516, 1518. "
              "În plus, lista originală omitea restructurarea (1514) și impozitele (1516).",
        devine="1511 litigii / 1512 garanții / 1514 restructurare / 1516 impozite / 1518 alte [N]",
    ),
    dict(
        text="280.x pe tip imobilizare",
        motiv="„280.x” nu e o notație de cont. Conturile sunt 2803, 2805, 2808, iar "
              "regula reală e oglinda cu contul de activ (vezi C-14).",
        devine="2803 / 2805 / 2808, în oglindă cu contul de activ",
    ),
    # ---- statusuri devenite false -------------------------------------------
    dict(
        text="- (modul extern Leasing)",
        motiv="MOD_LEASING_FIN nu mai e extern: e implementat în "
              "Module_Declarative_Fluxuri.xlsx și acoperit de flux propriu.",
        devine="F-50",
    ),
    dict(
        text="Template_leasing_financiar_auto, nu în Fluxuri",
        motiv="Idem — afirmația „nu în Fluxuri” a devenit falsă odată cu F-50.",
        devine="F-50 pas 9: 167 = scadențar, 1:1 cu contractul",
    ),
    # ---- MOD_LEASING_FIN: din „exemplu extern” în modul implementat ----------
    # Rândul din CatalogModule / Index module se ACTUALIZEAZĂ în loc, ca modulul să
    # aibă un singur rând. Metadatele vechi descriau un fișier separat care nu mai e
    # sursa adevărului, deci nu se contopesc — se înlocuiesc.
    *[
        dict(text=t, devine=d,
             motiv="MOD_LEASING_FIN a devenit modul intern, cu foile "
                   "Declarații/Reguli/Jurnale/NotaExport în acest workbook. Metadatele "
                   "vechi trimiteau la un fișier separat și la un status „EXEMPLU "
                   "EXTERN” care nu mai sunt adevărate.")
        for t, d in [
            ("Leasing financiar auto (limitări TVA/amortizare)",
             "Leasing financiar auto: avans, intrare, rate, corecții TVA 50%, "
             "amortizare plafonată"),
            ("Template_leasing_financiar_auto.xlsx",
             "Declarații_LEASING_FIN, Reguli_, Jurnale_, NotaExport_"),
            ("Pe contract + lună — fișier separat", "Pe contract + lunar"),
            ("Pe contract + lună", "Pe contract + lunar"),
            ("F-26 + F-28 + reeval", "F-50"),
            ("Contract, Scadențar, Regim vehicul, Curs BNR — vezi "
             "Template_leasing_financiar_auto",
             "Valoare contract, avans, rată, dobândă, comision, CASCO, regim vehicul, durată"),
            ("MIXT/EXCLUSIV/EXCEPTAT; Capitalizare vs Cheltuială TVA neded.",
             "MIXT 50% / EXCLUSIV 100% / EXCEPTAT; capitalizare vs. cheltuială pentru "
             "TVA nededusă"),
            ("B1–B7 pe momente — EXEMPLU EXTERN complet",
             "B1 Avans; B2 TVA avans; B3 Intrare + 167; B4 Stingere avans; "
             "B5 Factura lunară; B6 Corecție TVA 50%; B7 Limitare 50% cheltuieli; "
             "B8 Amortizare"),
        ]
    ],

    # ---- MOD_SALARII și MOD_DECONT: din „exemplu extern” în module interne ---
    # Fișierele-sursă rămân în surse/module-externe/ ca referință de verificare, dar
    # nu mai sunt LOCUL unde se face treaba, deci metadatele care trimiteau la ele au
    # devenit false.
    *[
        dict(text=t, devine=d,
             motiv="Modulul a devenit intern, cu foile Declarații/Reguli/(Registru)/"
                   "Jurnale/NotaExport în acest workbook. Cifrele lui sunt verificate "
                   "contra fișierului extern, care rămâne în surse/module-externe/ "
                   "doar ca referință.")
        for t, d in [
            ("Salarii complete (exemplu extern cifrat)",
             "B1 Plata avansului; B2 Costurile lunii; B3 Plăți (net, taxe, CAM)"),
            ("Salarii AS Kids - 31.07.2026.xlsx",
             "Declarații_SALARII, Reguli_SALARII, Jurnale_SALARII, NotaExport_SALARII"),
            ("Brut, Tichete, Avans, Angajat, Luna — vezi fișierul Salarii AS Kids",
             "Brut, tichete, avans, pe angajat; cotele CAS/CASS/impozit/CAM"),
            ("B1 Costuri; B2 Plăți net+taxe; B3 Tichete — EXEMPLU EXTERN complet",
             "B1 Plata avansului; B2 Costurile lunii; B3 Plăți (net, taxe, CAM)"),
            ("Lunar — fișier separat", "Lunar, pe registru de angajați"),
            ("Lunar + plăți", "Lunar, pe registru de angajați"),
            ("Deconturi cheltuieli + avansuri",
             "B1 Avans; B2 Cheltuieli + TVA; B3 Regularizare avans; B4 Plată / restituire"),
            ("Deconturi AS Kids - ….xlsx",
             "Declarații_DECONT, Reguli_DECONT, Registru_DECONT, Jurnale_DECONT, "
             "NotaExport_DECONT"),
            ("Linii decont, Titular, Avans, Cotă TVA — vezi Deconturi AS Kids",
             "Linii de decont (furnizor, sumă, natură, tip document, CUI), avans, cote"),
            ("B1 Avans; B2 Cheltuieli; B3 Regularizare; B4 Plată — EXEMPLU EXTERN complet",
             "B1 Avans; B2 Cheltuieli + TVA; B3 Regularizare avans; B4 Plată / restituire"),
            ("La deconturi — fișier separat", "Pe decont"),
            ("F-35 + deplasări", "F-35"),
            ("Platitor TVA, % ded. vehicule",
             "Plătitor de TVA; % deducere vehicule; matricea document × CUI"),
        ]
    ],

    # ---- marcaje PARȚIAL pe salarii, rezolvate de MOD_SALARII ---------------
    *[
        dict(text=t, devine=d,
             motiv="Marcajul PARȚIAL era corect cât timp salariile existau doar ca "
                   "exemplu extern cifrat. MOD_SALARII acoperă acum lanțul complet "
                   "(brut → CAS/CASS/impozit → net → CAM → tichete → plăți), cu cifre "
                   "verificate contra statului real din 31.07.2026. Limitările rămase "
                   "sunt declarate în Reguli_SALARII, tabelul C.")
        for t, d in [
            ("F-32 ilustrativ; modul extern Salarii e cifrat",
             "Lanțul complet în MOD_SALARII, cu cifre verificate contra statului real "
             "din 31.07.2026; F-52/F-58 acoperă ipostaza de cost capitalizat"),
            ("Idem F-32 / modul extern",
             "MOD_SALARII acoperă 641 salarii, 642 tichete și 646 CAM; limitările "
             "rămase sunt declarate în Reguli_SALARII, tabelul C"),
        ]
    ],

    # ---- retitulări care elimină concurența semantică între fluxuri ----------
    dict(
        text="Achiziție MF + amortizare",
        motiv="Titlu prea generic: concura cu fluxul de achiziție intracomunitară / import "
              "de mijloc fix, care tratează alt regim. Precizarea „intern” le separă.",
        devine="Achiziție mijloc fix intern + amortizare liniară",
    ),
    dict(
        text="F-26 - Achiziție mijloc fix + amortizare",
        motiv="Idem, pe titlul blocului de monografie.",
        devine="F-204 — Achiziție mijloc fix intern + amortizare liniară",
    ),

    # ---- cifre care descriau starea veche a fișierului -----------------------
    dict(
        text="Fluxuri: 38/38 detaliate. Matrice Tier A: acoperire completă.",
        motiv="Numărătoare depășită: sunt 60 de fluxuri după trainingurile 2 și 3 și "
              "după cele două contopiri. Textul original e păstrat în foaia Istoric.",
        devine="Fluxuri: 60/60 detaliate. Matrice Tier A: acoperire completă.",
    ),
    dict(
        text="~38 fluxuri × pași, tabelar cu note complete + coloană Declarativ",
        motiv="Idem — descrierea structurii workbook-ului anunța 38 de fluxuri.",
        devine="60 fluxuri × pași, tabelar cu note complete + coloană Declarativ",
    ),
    dict(
        text="245+ rânduri, cu 3 coloane noi: Analitice recomandate · Factor · Flux (pas)",
        motiv="Planul are acum 270+ rânduri, după adăugarea conturilor care lipseau "
              "(1011, 1012, 1171, 1174, 2812, 6583 ș.a.).",
        devine="270+ rânduri, cu 3 coloane noi: Analitice recomandate · Factor · Flux (pas)",
    ),
    # ---- cifre care se derivă acum, deci nu mai pot fi scrise de mână ---------
    #
    # Cele cinci de mai jos au aceeași poveste: erau aproximări scrise în sămânță și
    # rămase acolo. Nu se mai înlocuiesc cu alte numere fixe — `build/cifre.py` le
    # numără din workbook la fiecare build, iar `devine` de aici arată doar valoarea
    # din momentul declarării, ca motivul să fie citibil.
    dict(
        text="LISTA FLUXURILOR (~38) — structură + status implementare",
        motiv="Titlul catalogului anunța 38 de fluxuri, la trei rânduri deasupra celor "
              "68 pe care le lista. Înlocuirea exista în cod din prima curățare, dar "
              "rula numai pe Legendă, niciodată pe foaia Fluxuri.",
        devine="LISTA FLUXURILOR (68) — structură + status implementare",
    ),
    dict(
        text="81 conturi de serviciu, grupate pe rol",
        motiv="Foaia „Doar rol în flux” are 80 de conturi. Se numără la build.",
        devine="80 conturi de serviciu, grupate pe rol",
    ),
    dict(
        text="Tier A (~55) — tratate individual, cu analitice justificate rând cu rând",
        motiv="Sunt 87 de conturi clasificate Tier A, din care 39 au rând detaliat în "
              "foaia de analitice. Aproximarea „~55” nu era niciuna din cele două.",
        devine="Tier A (87, din care 39 cu rând detaliat de analitice) — tratate "
               "individual, cu analitice justificate rând cu rând",
    ),
    dict(
        text="Tier B (~110) — analitic prin aplicarea unui tipar deja stabilit la Tier A "
             "(ex. toate ajustările urmează același model)",
        motiv="Sunt 134.",
        devine="Tier B (134) — analitic prin aplicarea unui tipar deja stabilit la Tier A "
               "(ex. toate ajustările urmează același model)",
    ),
    dict(
        text="Tier C (~80) — conturi rar folosite în cabinet (consolidare, fiducie, "
             "resurse minerale, clasa 9). Marcate explicit „acoperire minimă”",
        motiv="Sunt 36. Eroarea nu era de rotunjire, era de peste dublu — și se vedea "
              "abia când cele trei tiere s-au numărat: 87 + 134 + 36 = 257, adică fix "
              "planul întreg. Aproximările nu însumau nimic.",
        devine="Tier C (36) — conturi rar folosite în cabinet (consolidare, fiducie, "
               "resurse minerale, clasa 9). Marcate explicit „acoperire minimă”",
    ),
    # ---- portarea modulelor moștenite din sămânță în `date/module/` ----------
    dict(
        text='=IF(B10=473,"Sold 473 la 31.12 = suspect — clarificare obligatorie","—")',
        motiv="Defect viu, găsit la portarea lui MOD_INTERMEDIAR. B10 conține TEXTUL "
              "„473”, iar Excel nu compară text cu număr: „473”=473 e FALSE, mereu. Cu "
              "tipul implicit chiar pe 473, celula afișa „—”. Adică singurul avertisment "
              "serios al modulului — soldul de 473 rămas la 31.12, care în notițe e "
              "SUSPECT, nu LEGITIM — era cod mort. Acum se compară text cu text.",
        devine='=IF(B10="473","Sold 473 la 31.12 = suspect — clarificare '
               'obligatorie","—")',
    ),
    dict(
        text='=IF(CatalogModule!A14="DA","ACTIV","INACTIV")',
        motiv="Rândul din catalog era scris în formulă. Mutai un rând și celula citea "
              "steagul altui modul, tăcut. Se caută pe codul modulului, prin "
              "INDEX/MATCH — vezi `date/module/comun.py:formula_activ`. Intervalul e "
              "mărginit ($A$1:$A$200), pentru că motorul de recalcul nu evaluează "
              "`INDEX(CatalogModule!A:A, …)` pe coloană întreagă; forma pe coloană "
              "întreagă lăsa celula goală în toate cele patru module care o foloseau.",
        devine="vezi date/module/comun.py:formula_activ",
    ),
    dict(
        text="Declarații_INTER, Jurnale_INTER, NotaExport_INTER",
        motiv="Foile nu se numesc așa. Sunt Declarații_INTERMEDIAR, Reguli_INTERMEDIAR, "
              "Jurnale_INTERMEDIAR, NotaExport_INTERMEDIAR — iar `Reguli_` lipsea cu "
              "totul din listă, deși modulul o are. O instrucțiune de navigare greșită "
              "în foaia al cărei singur rost e navigarea. Se generează acum din cod.",
        devine="Declarații_INTERMEDIAR, Reguli_INTERMEDIAR, Jurnale_INTERMEDIAR, "
               "NotaExport_INTERMEDIAR",
    ),
    dict(
        text="F-23, F-34, F-39",
        motiv="Lista de fluxuri a lui MOD_INTERMEDIAR din `Index module` nu coincidea cu "
              "cea din `CatalogModule` („F-23, F-33, F-34”) — două liste scrise de mână "
              "despre același modul, divergente. Rămâne una singură, citită din "
              "`CATALOG['fluxuri']`. F-39 (F-304, intersecția 32x ↔ 408 la același "
              "furnizor) iese: e o stare inițială murdară, pe care tiparul generic "
              "deschidere → stingere de aici nu o modelează.",
        devine="F-23, F-33, F-34",
    ),
    dict(
        text='=IF(CatalogModule!A6="DA","ACTIV — jurnalele se generează",'
             '"INACTIV — jurnalele rămân goale")',
        motiv="Același rând absolut, la MOD_INCHIDERE_TVA. Vezi motivul de la A14.",
        devine="vezi date/module/comun.py:formula_activ",
    ),
    dict(
        text="Declarații_TVA, Jurnale_TVA, NotaExport_TVA",
        motiv="Foile se numesc Declarații_INCHIDERE_TVA ș.a.m.d., iar Reguli_ lipsea "
              "din listă. Se generează acum din codul modulului.",
        devine="Declarații_INCHIDERE_TVA, Reguli_INCHIDERE_TVA, Jurnale_INCHIDERE_TVA, "
               "NotaExport_INCHIDERE_TVA",
    ),
    dict(
        text='=IF(CatalogModule!A7="DA","ACTIV","INACTIV")',
        motiv="Același rând absolut, la MOD_APROV_TRANZIT. Vezi motivul de la A14.",
        devine="vezi date/module/comun.py:formula_activ",
    ),
    dict(
        text="Declarații_APROV, Jurnale_APROV, NotaExport_APROV",
        motiv="Foile se numesc Declarații_APROV_TRANZIT ș.a.m.d., iar Reguli_ lipsea "
              "din listă. Se generează acum din codul modulului.",
        devine="Declarații_APROV_TRANZIT, Reguli_APROV_TRANZIT, Jurnale_APROV_TRANZIT, "
               "NotaExport_APROV_TRANZIT",
    ),
    dict(
        text="F-02 (+408 simetric)",
        motiv="A doua divergență Index ↔ Catalog: `Index module` scria „F-302, F-304”, "
              "`CatalogModule` scria „F-302 (+408 simetric)” — o paranteză în proză "
              "într-un câmp pe care poarta 21 îl citește ca listă de ID-uri. Rămâne "
              "F-302 curat; cazul simetric pe 408 e MOD_INTERMEDIAR și scrie asta în "
              "Tabelul B al Regulilor, unde se și caută.",
        devine="F-02",
    ),
    dict(
        text='=IF(CatalogModule!A13="DA","ACTIV","INACTIV")',
        motiv="Același rând absolut, la MOD_INCHIDERE_EX. Vezi motivul de la A14. Cu "
              "asta se termină cele patru; nicio foaie de modul nu mai citește catalogul "
              "pe rând, deci reordonarea lui devine sigură.",
        devine="vezi date/module/comun.py:formula_activ",
    ),
    dict(
        text="Declarații_EX, Jurnale_EX, NotaExport_EX",
        motiv="Foile se numesc Declarații_INCHIDERE_EX ș.a.m.d., iar Reguli_ lipsea din "
              "listă. Se generează acum din codul modulului.",
        devine="Declarații_INCHIDERE_EX, Reguli_INCHIDERE_EX, Jurnale_INCHIDERE_EX, "
               "NotaExport_INCHIDERE_EX",
    ),
    dict(
        text="B1 Închidere 6xx; B2 Închidere 7xx; B3 Impozit; B4 Repartizare 129; "
             "B5 Report 117",
        motiv="Catalogul anunța cinci blocuri; jurnalele au patru. Blocul de repartizare "
              "nu există și n-a existat niciodată: câmpul „Repartizare la rezerve / "
              "dividende” se scade din rezultatul reportat, dar nicio înregistrare nu "
              "mută suma nicăieri. Cu valoarea implicită 0 nu se vede; pusă pe 5.000, "
              "nota ar ieși cu 5.000 de lei care dispar. Lista spune acum ce emite "
              "modulul. Cine repartizează efectiv are MOD_CAPITALURI, construit pentru "
              "asta (rezervă legală, dividende, 1171).",
        devine="B1 Închidere 6xx; B2 Închidere 7xx; B3 Impozit; B4 Report 117",
    ),
    dict(
        text="Închidere cls.6/7 pe 121; 711 cu PN",
        motiv="A patra și ultima divergență Index ↔ Catalog. `Index module` dădea "
              "MOD_INCHIDERE_EX drept acoperind și F-314 („711 cu PN”), `CatalogModule` "
              "dădea doar F-104. Citit din foile reale, catalogul avea dreptate: modulul "
              "închide totaluri de clasă 6 și 7 și nu atinge 711 nicăieri. Producția "
              "neterminată la granița de exercițiu e MOD_NEUTRALIZARE.",
        devine="Închidere cls.6/7 pe 121; impozit; report 117",
    ),
    dict(
        text="Ilustrativ (sume descriptive)",
        motiv="Marcajul PARȚIAL de la 681/781 era corect când sumele erau descriptive. "
              "Acum 681 și 781 au cifre reale în F-50 (plafonul de 1.500 lei/lună) și "
              "F-51 (reluarea prin 7812), deci nota nu mai descrie realitatea.",
        devine="F-50 plafon 1.500 lei/lună; F-51 reluare 7812",
    ),
]

#: Doar textele, pentru poartă.
DECLARATE = [d["text"] for d in INLOCUIRI]

#: text original -> textul care îl înlocuiește (folosit de auto-merge ca să știe
#: că nu trebuie să contopească, ci să suprascrie).
SUPRASCRIE = {d["text"]: d["devine"] for d in INLOCUIRI}
