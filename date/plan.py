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
    # ---- denumiri completate din tabelul recapitulativ al sursei 19.08 -------
    "378":  dict(observatie="Diferențe de preț la mărfuri (adaos). Rectificativ al lui "
                            "371 la preț cu amănuntul, alături de 4428."),
    "419":  dict(observatie="Clienți-creditori (avansuri încasate). TVA se colectează la "
                            "încasarea avansului, iar la factura finală avansul se "
                            "stornează — nu e venit, deci nu poate merge pe 472."),
    "491":  dict(observatie="Ajustări pentru deprecierea creanțelor-clienți. Spre deosebire "
                            "de ajustările de stoc, acestea SUNT deductibile condiționat, "
                            "în limitele art. 26. Nu se confundă cele două regimuri."),
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

    # ------------------------------------------------------------------
    # Analiticele de gradul II pe care sursa 19.08 le numește și planul nu le avea.
    #
    # Planul e ținut la nivel sintetic, de trei cifre — o alegere bună pentru
    # navigare. Dar șapte dintre conturile de mai jos sunt FOLOSITE în monografii
    # (6583 și 7583 în ieșirile de mijloace fixe, 6814/7814 în ajustări, 5121
    # aproape peste tot), fără să existe în plan. Adică navigarea cont → flux se
    # rupea exact pentru ele — unul dintre golurile marcate „verifică tu” în
    # documentul de parcurs.
    #
    # Le-a scos la iveală poarta 16: tabelul recapitulativ al sursei le numea, iar
    # planul n-avea unde să le primească.
    # ------------------------------------------------------------------
    # ---- conturi cerute de fluxurile din 21.08 -------------------------
    dict(simbol="4282", denumire="Alte creanțe în legătură cu personalul", fct="A",
         natura="Patrimonial (real)", subtip="Creanță",
         observatie="Ce datorează salariatul firmei: echipament nepredat, avans "
                    "nejustificat, imputații. ⚠️ Notițele din 21.08 foloseau 4428 — "
                    "acela e TVA neexigibilă. Sold creditor = contrar naturii (C-23).",
         analitice="4282 pe salariat", factor="C", flux="F-419", tier="A"),
    dict(simbol="6458", denumire="Alte cheltuieli privind asigurările și protecția socială",
         fct="A", natura="Patrimonial (real)", subtip="Cheltuială",
         observatie="Partea din indemnizația de concediu medical suportată efectiv de "
                    "angajator. Restul indemnizației NU e cheltuială: e creanță pe 4382.",
         analitice="—", factor="D", flux="F-416", tier="B"),
    dict(simbol="2813", denumire="Amortizarea instalațiilor și mijloacelor de transport",
         fct="P", natura="Rol in flux", subtip="Rectificativ / contra",
         observatie="Rectificativ pasiv al lui 213. La ieșire se debitează cu amortizarea "
                    "cumulată, iar valoarea rămasă trece prin 6583.",
         analitice="2813 pe grupa de mijloc fix", factor="C B", flux="F-211, F-212", tier="A"),
    dict(simbol="5121", denumire="Conturi la bănci în lei", fct="A",
         natura="Patrimonial (real)", subtip="Trezorerie",
         observatie="Contul de bancă, indiferent de instrument (ordin de plată, internet "
                    "banking, mandat). Nu se confundă cu 5311 (casa) sau 5111 "
                    "(cecuri de încasat, cont de ÎNCASĂRI).",
         analitice="5121 pe bancă și pe valută", factor="V O", flux="F-405, F-410", tier="A"),
    dict(simbol="6583", denumire="Cheltuieli privind activele cedate", fct="A",
         natura="Patrimonial (real)", subtip="Cheltuiala",
         observatie="Valoarea rămasă neamortizată la ieșirea unui activ. Perechea lui "
                    "7583 — facturarea singură nu scoate activul din evidență.",
         analitice="6583 pe activ cedat", factor="F C", flux="F-211, F-212", tier="A"),
    dict(simbol="7583", denumire="Venituri din vânzarea activelor și alte operațiuni de capital",
         fct="P", natura="Patrimonial (real)", subtip="Venit",
         observatie="Prețul de vânzare al activului. Se compară cu 6583: diferența e "
                    "rezultatul cedării.",
         analitice="7583 pe activ cedat", factor="F C", flux="F-211, F-212", tier="A"),
    dict(simbol="6814",
         denumire="Cheltuieli de exploatare privind ajustările pentru deprecierea activelor circulante",
         fct="A", natura="Patrimonial (real)", subtip="Cheltuiala",
         observatie="Constituirea ajustării de stoc. NEDEDUCTIBILĂ fiscal — art. 26 Cod "
                    "fiscal enumeră limitativ, iar deprecierea stocurilor nu e acolo. "
                    "Funcționează în oglindă cu 7814.",
         analitice="6814 pe natura stocului ajustat", factor="F N", flux="F-307", tier="A"),
    dict(simbol="7814",
         denumire="Venituri din ajustări pentru deprecierea activelor circulante",
         fct="P", natura="Patrimonial (real)", subtip="Venit",
         observatie="Reluarea ajustării la valorificarea bunului — obligatorie prin lege. "
                    "NEIMPOZABILĂ (art. 23 lit. d), ca să neutralizeze cheltuiala "
                    "nedeductibilă din 6814.",
         analitice="7814 pe natura stocului ajustat", factor="F N", flux="F-307", tier="A"),
    dict(simbol="4091", denumire="Furnizori-debitori (avansuri plătite)", fct="A",
         natura="Patrimonial (real)", subtip="Creanta",
         observatie="Avansurile se analitizează pe DESTINAȚIE: 4091 stocuri, 4092 servicii, "
                    "4093 imobilizări corporale, 4094 imobilizări necorporale. "
                    "4093/4094 au furnizor 404, nu 401. Stornarea la factura finală se "
                    "face și pe 4091, și pe 401, ca efectul net să fie zero.",
         analitice="4091 – 4094 pe destinație", factor="C O", flux="F-410", tier="A"),

    # ------------------------------------------------------------------
    # Conturile cerute de sursa 26.08: subvenții, dividende, conturile-coș
    #
    # Toate cele 17 au sinteticul de trei cifre în plan, deci **poarta 20 nu le-ar fi
    # cerut**: ea acceptă `4481` pe baza rândului lui `448`. Rezerva aia e corectă în
    # principiu — planul se ține sintetic — dar pentru șase dintre ele minte, și minte
    # exact acolo unde e miezul lecției:
    #
    #     448 e A/P, iar 4481 e datorie și 4482 e creanță;
    #     445 e A/P, iar 4451/4452/4458 sunt toate creanțe;
    #     117 e A/P, iar 1171 poate fi în oricare sens.
    #
    # Un cont bifuncțional nu poate răspunde în locul analiticului lui la întrebarea
    # „ce sold trebuie să aibă”. Poarta 29 formalizează exact granița asta.
    #
    # Restul de unsprezece se adaugă din același motiv ca 6583/7583 mai sus: sunt
    # FOLOSITE în monografii, iar navigarea cont → flux se rupea pentru ele.
    # ------------------------------------------------------------------
    # ---- creanțele din subvenții (grupa 445) ---------------------------
    dict(simbol="4451", denumire="Subvenții guvernamentale", fct="A",
         natura="Patrimonial (real)", subtip="Creanță",
         observatie="Creanța față de finanțatorul public, născută la APROBARE, nu la "
                    "încasare. Perechea ei de venit amânat e 4751: separat se țin „de "
                    "la cine am de primit” și „cât din venit nu mi se cuvine încă”.",
         analitice="4451 pe proiect / program de finanțare", factor="C O",
         flux="F-210, F-215", tier="A"),
    dict(simbol="4452", denumire="Împrumuturi nerambursabile cu caracter de subvenții",
         fct="A", natura="Patrimonial (real)", subtip="Creanță",
         observatie="Fondurile europene nerambursabile. Perechea de venit amânat e 4752 "
                    "(sau 4758 la „alte sume”). Valorile din proiect sunt FĂRĂ TVA: "
                    "TVA-ul nu se decontează din proiect.",
         analitice="4452 pe proiect", factor="C O", flux="F-215", tier="A"),
    dict(simbol="4458", denumire="Alte sume primite cu caracter de subvenții", fct="A",
         natura="Patrimonial (real)", subtip="Creanță",
         observatie="Creanța la plusurile de inventar de natura imobilizărilor și la "
                    "celelalte sume asimilate. Perechea: 4753 / 4754 / 4758.",
         analitice="4458 pe sursă", factor="C O", flux="F-215, F-216", tier="A"),
    # ---- veniturile amânate (grupa 475) --------------------------------
    dict(simbol="4751", denumire="Subvenții guvernamentale pentru investiții", fct="P",
         natura="Rol in flux", subtip="Regularizare temporală",
         observatie="Venitul care nu ți se cuvine încă. Se reia la 7584 pe măsura "
                    "amortizării activului finanțat, în COTA de finanțare.",
         analitice="4751 pe proiect", factor="C O", flux="F-210, F-215", tier="A"),
    dict(simbol="4752",
         denumire="Împrumuturi nerambursabile cu caracter de subvenții pentru investiții",
         fct="P", natura="Rol in flux", subtip="Regularizare temporală",
         observatie="Venitul amânat al fondurilor europene. Poate sta „latent” oricât "
                    "între aprobare și prima cheltuială cu activul: nimic nu se reia la "
                    "venit până nu începe amortizarea.",
         analitice="4752 pe proiect", factor="C O", flux="F-215", tier="A"),
    dict(simbol="4753", denumire="Donații pentru investiții", fct="P",
         natura="Rol in flux", subtip="Regularizare temporală",
         observatie="Aceeași mecanică, altă sursă: donația de imobilizare nu e venit al "
                    "lunii primirii.",
         analitice="4753 pe donator", factor="C O", flux="F-215", tier="B"),
    dict(simbol="4754", denumire="Plusuri de inventar de natura imobilizărilor", fct="P",
         natura="Rol in flux", subtip="Regularizare temporală",
         observatie="Plusul constatat la inventar la imobilizări NU se recunoaște direct "
                    "la venit: o imobilizare are drept cheltuială amortizarea, iar "
                    "venitul trebuie să apară în același ritm.",
         analitice="4754 pe mijloc fix", factor="C O", flux="F-216", tier="A"),
    dict(simbol="4758", denumire="Alte sume primite cu caracter de subvenții pentru investiții",
         fct="P", natura="Rol in flux", subtip="Regularizare temporală",
         observatie="Perechea folosită în monografia proiectului european din 26.08 "
                    "(4452 = 4758, apoi 4758 = 7584 lunar).",
         analitice="4758 pe proiect", factor="C O", flux="F-215", tier="A"),
    # ---- veniturile din reluare (grupa 758) ----------------------------
    dict(simbol="7584", denumire="Venituri din subvenții pentru investiții", fct="P",
         natura="Patrimonial (real)", subtip="Venit",
         observatie="Reluarea subvenției la venit, lună de lună, în cota de finanțare. "
                    "Regula de verificare a formatorului: dacă am o cheltuială din "
                    "proiect, trebuie să am și un venit în aceeași lună.",
         analitice="7584 pe proiect", factor="C O", flux="F-210, F-215, F-216", tier="A"),
    dict(simbol="7582", denumire="Venituri din donații primite", fct="P",
         natura="Patrimonial (real)", subtip="Venit",
         observatie="Contul pe care îl primește remiterea de datorie: creditarea la care "
                    "asociatul renunță prin act notarial devine venit. ⚠️ Formal E venit "
                    "din exploatare — grupa 758 stă în partea de exploatare a contului "
                    "de profit. Ce nu e „din exploatare” e SUBSTANȚA: profitul vine "
                    "dintr-o renunțare, nu din activitate.",
         analitice="7582 pe asociat", factor="F O", flux="F-113", tier="A"),
    dict(simbol="7588", denumire="Alte venituri din exploatare", fct="P",
         natura="Patrimonial (real)", subtip="Venit",
         observatie="Contul de venit folosit când nu există unul asociat direct — cum e "
                    "707 pentru marfă. La imputația către salariat: 461 = 7588 pentru "
                    "bază și 461 = 4427 pentru TVA.",
         analitice="7588 pe natura operațiunii", factor="F", flux="F-426", tier="B"),
    # ---- asociați și capital -------------------------------------------
    dict(simbol="4551", denumire="Acționari/asociați — conturi curente", fct="P",
         natura="Patrimonial (real)", subtip="Datorie",
         observatie="Creditarea de societate. **Nu are niciodată sold debitor**: dacă "
                    "are, ori înregistrarea e greșită, ori asociatul a ridicat mai mult "
                    "decât a pus. Analitic pe fiecare asociat, fără compensare între ei "
                    "decât prin act notarial. Contract pentru fiecare creditare.",
         analitice="4551 pe fiecare ASOCIAT", factor="O", flux="F-111, F-112, F-113",
         tier="A"),
    dict(simbol="1011", denumire="Capital subscris nevărsat", fct="P",
         natura="Rol in flux", subtip="Regularizare temporală",
         observatie="Etapa dintre subscriere și vărsare. Trece în 1012 abia DUPĂ "
                    "înregistrarea la ONRC — nu la virarea banilor.",
         analitice="1011 pe asociat", factor="O", flux="F-101, F-112", tier="A"),
    dict(simbol="1012", denumire="Capital subscris vărsat", fct="P",
         natura="Patrimonial (real)", subtip="Capital propriu",
         observatie="Se ține pe analitic PE ASOCIAT, iar denumirea analiticului poartă "
                    "procentul de participare. Rostul: balanța spune singură cine cât "
                    "deține, fără actul constitutiv, în ziua în care vine hotărârea AGA.",
         analitice="1012 pe fiecare ASOCIAT, cu procentul în denumire", factor="O",
         flux="F-101, F-112, F-114", tier="A"),
    dict(simbol="1171",
         denumire="Rezultatul reportat reprezentând profitul nerepartizat sau pierderea neacoperită",
         fct="A/P", natura="Patrimonial (real)", subtip="Capital propriu",
         observatie="Profitul nerepartizat al anilor anteriori, pe analitic PE AN. Sold "
                    "creditor = profit repartizabil; sold debitor = pierdere. Cât timp "
                    "are sold debitor NU se pot acorda dividende, nici certe, nici "
                    "interimare.",
         analitice="1171 PE AN (sens D/C)", factor="N F", flux="F-104, F-109, F-110",
         tier="A"),
    # ---- conturile care țin rulajele curate ----------------------------
    dict(simbol="4481", denumire="Alte datorii față de bugetul statului", fct="P",
         natura="Rol in flux", subtip="Intermediar / clarificare",
         observatie="Dobânzi, penalități și sume stabilite prin acte de control, "
                    "inclusiv pentru perioade anterioare. Ține impunerea ÎN AFARA "
                    "rulajului curent: trecută prin 4423, ar denatura decontul lunii. "
                    "Cheltuiala corespondentă (6588) e nedeductibilă. ❓ Notițele din "
                    "21.08 spun invers — 4423 cu analitic distinct; contradicția e "
                    "deschisă cu formatorul.",
         analitice="4481 pe decizie de impunere", factor="F", flux="F-424", tier="A"),
    dict(simbol="4482", denumire="Alte creanțe privind bugetul statului", fct="A",
         natura="Rol in flux", subtip="Intermediar / clarificare",
         observatie="Sumele plătite eronat către buget, până la lămurire: cifre "
                    "inversate pe ordinul de plată, sau plată făcută cu alt CUI de "
                    "plătitor. Sold în așteptare care se disecă — nu se lasă de la un an "
                    "la altul.",
         analitice="4482 pe plată în așteptare", factor="O", flux="F-425", tier="A"),
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
    # ---- subvenții, dividende, conturile-coș (sursa 26.08) -----------------
    ("1012", "Capital subscris vărsat — analitice pe asociat", "A", "F-76, F-74",
     "F-76 pas 3: cotele se citesc din balanță, fără actul constitutiv", "NU"),
    ("1171", "Rezultat reportat — analitic pe an", "A", "F-71, F-72",
     "F-71 pas 1: cu sold debitor pe 1171 nu se distribuie dividende", "NU"),
    ("457", "Dividende de plată — analitic pe asociat", "A", "F-71",
     "F-71 pas 2: repartizarea urmează cotele din 1012, nu invers", "NU"),
    ("463", "Creanțe din dividende interimare", "A", "F-72",
     "F-72 pas 2: plafonul e soldul lui 121, nu disponibilul din bancă", "NU"),
    ("4551", "Acționari/asociați — conturi curente", "A", "F-73, F-74, F-75",
     "F-73 pas 3: analiticele nu se compensează între asociați", "NU"),
    ("7582", "Venituri din donații primite (remitere de datorie)", "A", "F-75",
     "F-75 pas 2: datoria stinsă fără plată e venit, dar nu din activitate", "NU"),
    ("4452 / 4758", "Fonduri europene — creanță și venit amânat", "A", "F-77",
     "F-77 pas 4: amortizarea și reluarea la venit, în aceeași notă", "NU"),
    ("7584", "Venituri din subvenții pentru investiții", "A", "F-77, F-78",
     "F-77 pas 5: lună cu amortizare din proiect și fără reluare = eroare", "NU"),
    ("4754", "Plusuri de inventar de natura imobilizărilor", "A", "F-78",
     "F-78 pas 3: reluarea urmează ritmul amortizării, nu luna constatării", "NU"),
    ("446", "Alte impozite și taxe — punct de trecere", "A", "F-79",
     "F-79 pas 2: taxa nu intră direct pe cheltuială", "NU"),
    ("4482", "Alte creanțe privind bugetul statului", "A", "F-80",
     "F-80 pas 1: diferența plătită în plus stă în așteptare, nu pe 444", "NU"),
    ("461 / 462", "Debitori și creditori diverși", "A", "F-81",
     "F-81 pas 1: cumpărătorul unui mijloc fix nu e client", "NU"),
    ("458", "Decontări din operațiuni în participație", "A", "F-82",
     "F-82 pas 3: venitul se redistribuie, ca impozitul să urmeze activitatea", "NU"),

    # ---- salarii și rețineri (sursa 21.08) ---------------------------------
    ("423", "Personal — ajutoare materiale datorate", "A", "F-64",
     "F-64 pas 3: indemnizația trece prin datorie, dar numai o parte e cheltuială", "NU"),
    ("4382", "Alte creanțe sociale (FNUASS)", "A", "F-64",
     "F-64 pas 3: creanță, nu cheltuială — firma a avansat banii casei", "NU"),
    ("6458", "Alte cheltuieli privind asigurările și protecția socială", "A", "F-64",
     "F-64 pas 1: partea de indemnizație suportată efectiv de angajator", "NU"),
    ("427", "Rețineri din salarii datorate terților", "A", "F-65",
     "F-65 pas 2: firma e conductă — intră și iese cu aceeași sumă", "NU"),
    ("426", "Drepturi de personal neridicate", "A", "F-66",
     "F-66 pas 3: datoria nu dispare, se reclasifică — corelația cu statul revine", "NU"),
    ("4282", "Alte creanțe în legătură cu personalul", "A", "F-67",
     "F-67 pas 2: la încasare crește un activ și scade altul", "NU"),
    ("4418", "Impozitul pe venit (microîntreprindere)", "A", "F-68",
     "F-68 pas 3: sold creditor = obligația trimestrului curent", "NU"),
    ("698", "Cheltuieli cu impozitul pe venit", "A", "F-68",
     "F-68 pas 1: baza e VENITUL, nu profitul — de aceea 698, nu 691", "NU"),
    ("444 / 4315 / 4316 / 436", "Obligații salariale ale lunii", "A", "F-70",
     "F-70 pas 3: rulajul creditor al lunii = soldul creditor la finalul ei", "NU"),
    ("4481", "Datorii din acte de control (decizii de impunere)", "A", "F-69",
     "F-69 pas 4: decizia stă în afara contului pe care îl reconciliază decontul", "NU"),

    # ---- supraîncasare (sursa 19.08) ---------------------------------------
    ("419", "Clienți-creditori (avansuri încasate)", "A", "F-25, F-63",
     "F-63 pas 3: soldul creditor de pe 4111 se dovedește avans cu TVA", "NU"),
    ("4111", "Clienți", "A", "F-63",
     "F-63 pas 2: cont de activ ajuns cu sold creditor = avans neînregistrat", "NU"),
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
PARTIAL_REZOLVATE = ["28x", "681/781", "167", "421/431/444/436", "641/642/646"]

# Goluri PARȚIAL din matricea originală pe care extinderea NU le rezolvă.
# Sunt lăsate marcate onest, nu trecute pe „NU”. Poarta 4 le acceptă doar pentru că
# sunt enumerate aici cu motiv — orice gol nou, nedeclarat, pică verificarea.
#
# Salariile au ieșit din listă odată cu MOD_SALARII: modulul acoperă lanțul complet
# (brut → CAS/CASS/impozit → net → CAM → tichete → plăți), cu cifre verificate contra
# statului real din 31.07.2026. Ce rămâne neacoperit e declarat în Reguli_SALARII,
# tabelul C — deducere personală, facilități sectoriale, scutiri, Pilon II, concedii
# medicale — și e o limitare a MODULULUI, nu un gol al matricei.
GOLURI_ACCEPTATE = {}
