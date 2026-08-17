"""Actualizări pe foaia `Plan de conturi` + conturi sintetice lipsă + rânduri de matrice.

Planul original e SINTETIC (conturi de 3 cifre); analiticele stau în coloana
„Analitice recomandate”. Deci pentru trainingurile 2 și 3 nu se adaugă rânduri noi
de 4 cifre — se completează coloanele G (Analitice), H (Factor), I (Flux pas) și
J (Tier) pe rândurile care există deja.
"""

# --------------------------------------------------------------------------
# 1. Actualizări în loc, pe conturile existente: simbol -> câmpurile de completat
#    (se scriu doar câmpurile date; restul rândului rămâne neatins)
# --------------------------------------------------------------------------
ACTUALIZARI = {
    # ---- clasa 1 -----------------------------------------------------------
    "101":  dict(analitice="1011 subscris nevărsat / 1012 subscris vărsat [N]", factor="N C",
                 flux="F-45, F-46", tier="A"),
    "105":  dict(analitice="105 pe activ / pe reevaluare", factor="C F", flux="F-48", tier="A"),
    "106":  dict(analitice="1061 rezerve legale / 1063 statutare / 1068 alte rezerve [N]", factor="N F",
                 flux="F-46", tier="A"),
    "117":  dict(analitice="1171 PE AN (sens D/C) / 1174 corecții / 1175 surplus reevaluare [N]",
                 factor="N F B", flux="F-46, F-47, F-48, F-37", tier="A"),
    "121":  dict(flux="F-37 (pas revelator), F-46, F-41"),
    "129":  dict(analitice="129 (sintetic)", factor="C", flux="F-46", tier="A"),
    "151":  dict(analitice="1511 litigii / 1512 garanții / 1514 restructurare / 1516 impozite / "
                           "1518 alte [N]", factor="N F", flux="F-51", tier="A"),
    "162":  dict(analitice="1621…1627 sintetice distincte + analitic pe contract și VALUTĂ",
                 factor="V B", flux="F-49", tier="A"),
    "168":  dict(analitice="1682 dobânzi credite pe termen lung", factor="V", flux="F-49", tier="B"),
    "167":  dict(analitice="167 PE CONTRACT (1:1) și pe tip de valută", factor="C V O",
                 flux="F-50", tier="A"),
    # ---- clasa 2 -----------------------------------------------------------
    "203":  dict(analitice="203 pe proiect de dezvoltare", factor="O", flux="F-52", tier="B"),
    "205":  dict(analitice="205 pe titlu (marcă, licență, brevet)", factor="O", flux="F-52", tier="A"),
    "208":  dict(analitice="208 pe program", factor="O", flux="F-52", tier="A"),
    "211":  dict(analitice="2111 terenuri pe categorie de folosință / 2112 amenajări [N]",
                 factor="N F O", flux="F-53", tier="A"),
    "212":  dict(analitice="analitic pe mijloc fix + cod de clasificare + durată", factor="N C D O",
                 flux="F-54, F-58, F-59, F-61", tier="A"),
    "213":  dict(analitice="2131 / 2132 / 2133 / 2134, analitic pe mijloc fix + cod clasificare",
                 factor="N C D O", flux="F-55, F-57, F-60, F-61", tier="A"),
    "214":  dict(analitice="analitic pe mijloc fix + cod de clasificare", factor="N C O",
                 flux="F-57, F-61", tier="A"),
    "215":  dict(analitice="analitic pe imobil, cu defalcare teren / construcție", factor="N C O",
                 flux="F-56", tier="A"),
    "223":  dict(analitice="223 (tranzit) → 213 la recepție", factor="O", flux="F-57", tier="A"),
    "224":  dict(analitice="224 (tranzit) → 214 la recepție", factor="O", flux="F-57", tier="A"),
    "231":  dict(analitice="analitic PE OBIECTIV de investiții", factor="C O B",
                 flux="F-58, F-27", tier="A"),
    "235":  dict(analitice="analitic pe obiectiv", factor="O", flux="F-27", tier="B"),
    "261":  dict(analitice="261 pe entitate", factor="O B", flux="F-62", tier="A"),
    "267":  dict(analitice="267 pe PARTENER și CONTRACT", factor="O B", flux="F-62", tier="A"),
    "280":  dict(analitice="2803 / 2805 / 2808, în oglindă cu contul de activ", factor="C N",
                 flux="F-52, F-61", tier="A"),
    "281":  dict(analitice="2811 / 2812 / 2813 / 2814 / 2815, analitic pe mijloc fix",
                 factor="C N", flux="F-53, F-54, F-59, F-60, F-61", tier="A"),
    # ---- clasa 4 -----------------------------------------------------------
    "409":  dict(analitice="4093 avansuri imobilizări corporale / 4094 necorporale [N]", factor="C O",
                 flux="F-25, F-50", tier="A"),
    "404":  dict(analitice="404.RO / 404.UE / 404.EXT (alimentează D394 / D390)", factor="D",
                 flux="F-52, F-54, F-55, F-57, F-58", tier="A"),
    "456":  dict(analitice="456 pe fiecare ASOCIAT", factor="O", flux="F-45", tier="A"),
    "457":  dict(analitice="457 pe asociat", factor="D F", flux="F-46", tier="B"),
    "461":  dict(analitice="461 pe debitor", factor="O", flux="F-59", tier="B"),
    # ---- clasele 6 și 7 ----------------------------------------------------
    "613":  dict(analitice="613 / 613.NED (partea nedeductibilă la vehicule)", factor="F",
                 flux="F-50", tier="B"),
    "628":  dict(analitice="628 / 628.NED (partea nedeductibilă la vehicule)", factor="F",
                 flux="F-50, F-51, F-58", tier="B"),
    "658":  dict(analitice="6583 cedarea activelor / 6588 alte cheltuieli de exploatare", factor="F",
                 flux="F-59, F-60, F-50", tier="A"),
    "665":  dict(analitice="665 pe tip de element (credite, furnizori, clienți)", factor="V F",
                 flux="F-49, F-50", tier="A"),
    "666":  dict(analitice="666 / 666.NED (partea nedeductibilă la vehicule)", factor="V F",
                 flux="F-49, F-50", tier="A"),
    "681":  dict(analitice="6811 amortizare / 6812 provizioane", factor="F C",
                 flux="F-26, F-50, F-52, F-53, F-54, F-61", tier="A"),
    "721":  dict(analitice="721 (necorporale)", factor="C F", flux="F-52", tier="A"),
    "722":  dict(analitice="722 (corporale)", factor="C F", flux="F-28, F-58", tier="A"),
    "758":  dict(analitice="7583 cedarea activelor / 7588 alte venituri din exploatare", factor="F",
                 flux="F-59, F-60", tier="A"),
    "765":  dict(analitice="765 pe tip de element", factor="V F", flux="F-49", tier="A"),
    "781":  dict(analitice="7812 reluări de provizioane / 7813 reluări de ajustări", factor="F",
                 flux="F-51", tier="A"),
}

# --------------------------------------------------------------------------
# 2. Conturi sintetice care LIPSEAU din planul original
#    (simbol, denumire, funcție, natura, subtip, observație, analitice, factor, flux, tier)
#    `dupa` = simbolul după care se inserează logic; folosit doar pentru ordonare la raport.
# --------------------------------------------------------------------------
CONTURI_NOI = [
    dict(simbol="233", denumire="Imobilizari necorporale in curs de executie", fct="A",
         natura="Patrimonial (real)", subtip="Activ imobilizat",
         observatie="Costurile de dezvoltare internă se acumulează aici, neutralizate prin 721; "
                    "se stinge în 203/208 la punerea în funcțiune.",
         analitice="analitic PE PROIECT", factor="C O", flux="F-52", tier="A"),
    dict(simbol="232", denumire="Avansuri acordate pentru imobilizari corporale", fct="A",
         natura="Patrimonial (real)", subtip="Creanta",
         observatie="Alternativă la 4093 în unele planuri; a se folosi consecvent una singură.",
         analitice="—", factor="O", flux="—", tier="C"),
]

# --------------------------------------------------------------------------
# 3. Corecții pe rânduri existente (erori găsite în workbook-ul original)
# --------------------------------------------------------------------------
CORECTII = [
    dict(simbol="235",
         camp="denumire",
         vechi="Imobilizari necorporale in curs de executie",
         nou="Investitii imobiliare in curs de executie",
         motiv="Denumirea din fișierul original este a contului 233. Conform OMFP 1802/2014: "
               "231 = imobilizări corporale în curs, 233 = imobilizări necorporale în curs, "
               "235 = investiții imobiliare în curs."),
]

# --------------------------------------------------------------------------
# 4. Rânduri noi pentru foaia `Matrice acoperire`
# --------------------------------------------------------------------------
MATRICE = [
    ("101 / 1012", "Capital social", "A", "F-45, F-46", "F-45 pas 3: nevărsat → vărsat", "NU"),
    ("456", "Decontări cu asociații", "A", "F-45", "F-45 stingere la vărsare", "NU"),
    ("117 (1171)", "Rezultat reportat", "A", "F-46, F-47", "F-46 pas 4; analitic pe an (C-21)", "NU"),
    ("1174", "Corecții erori exerciții anterioare", "A", "F-47", "F-47 pas 2: ocolește 121", "NU"),
    ("1175 / 105", "Surplus din reevaluare", "A", "F-48", "F-48 pas 3: realizare pe măsura amortizării", "NU"),
    ("1061 / 129", "Rezervă legală / repartizare", "A", "F-46", "F-46 pași 2–3 (121 = 129)", "NU"),
    ("151x", "Provizioane", "A", "F-51", "F-51 pas 3: reluarea e independentă de factură", "NU"),
    ("162x / 1682", "Credite bancare în valută", "A", "F-49", "F-49 pas 4: reevaluarea lunară", "NU"),
    ("4093", "Avansuri pentru imobilizări", "A", "F-50, F-25", "F-50 pas 4: stingerea avansului în 167", "NU"),
    ("205 / 208 / 233", "Imobilizări necorporale", "A", "F-52", "F-52 pas 5: capitalizare prin 721", "NU"),
    ("211 (2111/2112)", "Terenuri și amenajări", "A", "F-53", "F-53 pas 3: se amortizează doar amenajarea", "NU"),
    ("212", "Construcții", "A", "F-54, F-58, F-59", "F-54 pas 3: taxare inversă + cod 27 în D394", "NU"),
    ("213x", "Instalații și mijloace de transport", "A", "F-55, F-57, F-60", "F-55 pas 4: taxa vamală în cost", "NU"),
    ("214 / 215", "Birotică / Investiții imobiliare", "A", "F-56, F-57", "F-56 pas 3: defalcare teren/construcție", "NU"),
    ("223 / 224", "Imobilizări în curs de aprovizionare", "A", "F-57", "F-57 pas 2: stingere la recepție", "NU"),
    ("231 / 233", "Imobilizări în curs de execuție", "A", "F-58, F-52", "F-58 pas 3: capitalizare prin 722", "NU"),
    ("26x", "Imobilizări financiare", "A", "F-62", "F-62 pas 3: analiticul face garanția identificabilă", "NU"),
    # 28x, 681/781 și 167 nu se repetă aici: rândurile lor din matricea originală
    # sunt actualizate în loc de build_plan.py (marcajul PARȚIAL trece pe NU).
    ("6583 / 7583", "Cedarea activelor", "A", "F-59, F-60", "F-59 pas 5: deductibil în limita venitului", "NU"),
    ("665 / 765", "Diferențe de curs", "A", "F-49, F-50", "F-49 pași 1 și 4: cele două momente", "NU"),
    ("721 / 722", "Producția de imobilizări", "A", "F-52, F-58, F-28", "F-58 pas 3 (era acoperit doar prin F-28)", "NU"),
]

# Conturi din matricea originală marcate PARȚIAL care trec acum pe NU,
# prin fluxurile din tranșa 4. Verificate de build_plan.py.
PARTIAL_REZOLVATE = ["28x", "681/781", "167"]

# Goluri PARȚIAL din matricea originală pe care tranșa 4 NU le rezolvă.
# Sunt lăsate marcate onest, nu trecute pe „NU”. Poarta 4 le acceptă doar pentru că
# sunt enumerate aici cu motiv — orice gol nou, nedeclarat, pică verificarea.
GOLURI_ACCEPTATE = {
    "421/431/444/436": "Salariile apar în F-52 și F-58 doar în ipostaza de cost CAPITALIZAT "
                       "(641 = 421, apoi 231/233 = 722/721). Lanțul complet de salarizare — "
                       "contribuții, rețineri, plăți, D112 — rămâne în MOD_SALARII (exemplu extern, "
                       "cifrat). Trainingul dedicat salariilor nu a fost încă prelucrat.",
    "641/642/646": "Idem: 641 e folosit în F-52 și F-58 ca bază de capitalizare, nu ca monografie "
                   "completă de cheltuieli cu personalul (642 tichete, 646 contribuții nu apar).",
}
