"""Fluxurile documentului de control — conturile la care se vede că ceva e greșit.

Sursele: `surse/training-5-2026-08-19/ghid-contabilitate.md` §7.3 (F-63) și
`surse/training-7-2026-08-26/notite-revizuit.md` §4 (F-79…F-82) și §8 (F-90).

Fișierul a pornit cu un singur flux și a rămas coerent crescând: toate șase sunt
locuri unde o sumă se așază CORECT ca să nu denatureze un cont pe care altcineva îl
reconciliază — decontul de TVA, fișa de rol, soldul clienților, balanța de la bancă.
Numele fișierului e „control” în ambele sensuri ale cuvântului: controlul intern care
prinde eroarea, și controlul fiscal care o găsește dacă nu e prinsă.

F-63 (→ F-415) — încasare mai mare decât factura:

E singurul material din 19.08 care naște un flux propriu în loc să adâncească unul
existent. Restul secțiunilor „noi” — plafoane de numerar, cerințe de document,
practică de control — nu produc articole contabile, deci n-au ce monografie să aibă.

Cifrele sunt cele din sursă: factură 10.000, încasat 15.000, diferența de 5.000 e
TVA-inclusivă și se sparge în 4.132,23 bază + 867,77 TVA. Factura se modelează tot cu
total 10.000, ca cele două sume să fie comparabile — sursa nu spune dacă e cu sau fără
TVA, iar §7.2 din același material stabilește chiar regula că o sumă fără mențiune se
consideră cu tot cu TVA.
"""
from .comun import flux, pas

FLUXURI = [
    # ------------------------------------------------------------------ F-63
    flux(
        "F-63", "Încasare mai mare decât factura (supraîncasare → 419 + TVA)",
        didactic=True,
        roluri="Creanță + Datorie din avans + Colectare TVA",
        conturi="4111, 419, 4427, 707, 5121",
        note="Diferența e TVA-inclusivă (§7.2: sumă fără mențiune = cu tot cu TVA). "
             "Legiuitorul nu cere corecție când TU plătești în plus, dar o cere când "
             "TU încasezi în plus.",
        principiu="Un sold creditor pe 4111 nu e o curiozitate de balanță, e un avans "
                  "neînregistrat. Banii primiți peste factură sunt o datorie față de "
                  "partener, nu un venit — deci merg pe 419, nu pe 472, iar TVA-ul din "
                  "ei se colectează chiar dacă banii se returnează luna următoare.",
        pasi=[
            pas(1, "Factură emisă",
                "Factura de 10.000 lei, total cu TVA 21%: bază 8.264,46 + TVA 1.735,54.",
                dr=[("4111.partener", 10000)],
                cr=[("707", 8264.46), ("4427", 1735.54)],
                rol="Creanță + Venit + TVA colectată"),
            pas(2, "Extras de cont",
                "Partenerul virează 15.000 lei — cu 5.000 mai mult decât factura. "
                "Creanța se stinge și trece pe credit: 4111 ajunge cu sold creditor 5.000, "
                "adică un cont de activ cu sold contrar naturii lui.",
                dr=[("5121", 15000)], cr=[("4111.partener", 15000)],
                rol="Trezorerie + Creanță stinsă și depășită"),
            pas(3, "Notă contabilă — reclasificarea diferenței",
                "Diferența nu e venit, deci nu poate merge pe 472. E avans: 419. Iar din "
                "ea se extrage TVA-ul, pentru că suma încasată e TVA-inclusivă: "
                "5.000 ÷ 1,21 = 4.132,23 bază, 867,77 TVA. Fără pasul ăsta, TVA-ul rămâne "
                "necolectat și nimic nu semnalează.",
                dr=[("4111.partener", 5000)],
                cr=[("419.partener", 4132.23), ("4427", 867.77)],
                rol="Pas revelator: soldul creditor de pe 4111 se dovedește a fi avans "
                    "purtător de TVA, nu o eroare de încasare",
                revelator=True),
            pas(4, "Verificare",
                "Sold 4111 = 0 pe partenerul respectiv; sold 419 = 4.132,23; TVA colectată "
                "suplimentar 867,77. Se ia fișa pe plătitor și se contraverifică 4427, ca "
                "să confirmi că softul chiar a extras TVA-ul — vezi întrebarea deschisă. "
                "Dacă încasarea și restituirea se închid în aceeași lună, situația se "
                "neutralizează și impactul fiscal dispare.",
                rol="Stare terminală: sold 4111 = 0, avansul identificat pe 419 cu TVA "
                    "colectat"),
        ],
    ),
    # ==================================================================
    # Trainingul 26.08.2026 — conturile care țin rulajele curate
    #
    # 446, 4481, 4482 și 461 par patru subiecte fără legătură. Sunt patru răspunsuri
    # la aceeași întrebare: **cum ții rulajele curente curate**. Fiecare e un loc unde
    # se așază o sumă care ALTFEL ar denatura un cont pe care cineva îl reconciliază —
    # decontul de TVA, fișa de rol de la ANAF, soldul clienților. De aia stau împreună
    # și de aia sunt în documentul de control: sunt despre cum se vede că un cont
    # arată greșit.
    #
    # F-427 (participația) intră tot aici, deși nu e un cont-coș: e tot un cont de
    # decontare care ține impozitul fiecărei societăți pe activitatea ei.
    # ==================================================================
    # ------------------------------------------------------------------ F-79
    flux(
        "F-79", "Taxe locale prin 446, cu 471 la perioade lungi", didactic=True,
        roluri="Punct de trecere + Regularizare temporală",
        conturi="446, 471, 635, 5121",
        note="Pragul sub care nu merită mecanismul cu 471 e o decizie de disciplină "
             "internă, nu o regulă fiscală — dar odată aleasă, se respectă consecvent.",
        principiu="Taxa nu intră direct pe cheltuială. O taxă plătită anticipat pentru "
                  "un an întreg nu e cheltuiala lunii în care s-a plătit — 446 o ține "
                  "cât e doar plătită, 471 o ține cât e plătită dar neconsumată, și "
                  "abia 635 o consumă, lună de lună.",
        pasi=[
            pas(1, "Decizie de impunere de la primărie + ordin de plată",
                "Impozitul pe clădiri de 12.000 lei pe an, plătit integral în martie. "
                "446 rămâne cu sold DEBITOR: taxa e plătită, dar nu e încă cheltuiala "
                "nimănui.",
                dr=[("446.taxe-locale", 12000)], cr=[("5121", 12000)],
                rol="Plata: 446 ca punct de trecere, cu sold debitor temporar"),
            pas(2, "Notă contabilă",
                "Suma se așază în 471, de unde va curge lună de lună. 446 se stinge — "
                "soldul lui debitor era tranzitoriu, nu o creanță față de primărie.",
                dr=[("471.impozit-cladiri", 12000)], cr=[("446.taxe-locale", 12000)],
                rol="Pas revelator: taxa nu intră direct pe cheltuială",
                revelator=True),
            pas(3, "Notă contabilă lunară",
                "12.000 ÷ 12 = 1.000 lei pe lună, din martie până în februarie anul "
                "următor — sau pe lunile calendaristice pe care le acoperă decizia.",
                dr=[("635", 1000)], cr=[("471.impozit-cladiri", 1000)],
                rol="Consumul eșalonat al cheltuielii"),
            pas(4, "Varianta sumei mici",
                "Taxa de firmă de 240 lei pe an: se plătește la fel prin 446, dar trece "
                "direct pe cheltuială. Mecanismul cu 471 costă mai mult decât "
                "denaturarea pe care o previne.",
                dr=[("635", 240)], cr=[("446.taxe-locale", 240)],
                rol="Trecerea directă, sub pragul de eșalonare"),
            pas(5, "Verificare",
                "La capătul perioadei: sold 471 = 0, sold 446 = 0, Σ635 = 12.240. "
                "Sold rămas pe 471 după ce perioada s-a scurs = eșalonarea s-a oprit pe "
                "drum; sold debitor pe 446 la sfârșit de an = o plată care n-a fost "
                "niciodată repartizată.",
                rol="Stare terminală: 446 = 0, 471 = 0, cheltuiala pe lunile ei"),
        ],
    ),
    # ------------------------------------------------------------------ F-80
    flux(
        "F-80", "Plată eronată către buget (4482)", didactic=True,
        roluri="Intermediar / clarificare — sold în așteptare",
        conturi="4482, 444, 5121",
        note="Cifrele sunt cele din notițe: datorat 715, plătit 751 (cifre inversate).",
        principiu="Diferența plătită în plus nu se lasă pe contul de datorie — acolo ar "
                  "produce un sold debitor pe un cont de pasiv, adică semnalul din C-23 "
                  "declanșat de o eroare care nu e a înregistrării, ci a plății. 4482 o "
                  "ține la vedere ca sold în AȘTEPTARE, care se disecă până la lămurire.",
        pasi=[
            pas(1, "Balanță + ordin de plată",
                "Impozitul pe salarii de plată e 715 lei, în soldul creditor al lui 444. "
                "Din bancă a ieșit o plată de 751 lei — cifre inversate la tastare.",
                dr=[("444", 715), ("4482.plata-in-plus", 36)], cr=[("5121", 751)],
                rol="Pas revelator: diferența se așază în așteptare, nu pe 444",
                revelator=True),
            pas(2, "Luna următoare",
                "Datoria lunii e 700 lei. Soldul lui 4482 diminuează plata: se virează "
                "664 lei, iar cei 36 din luna trecută sting restul.",
                dr=[("444", 700)],
                cr=[("5121", 664), ("4482.plata-in-plus", 36)],
                rol="Stingerea soldului în așteptare"),
            pas(3, "Al doilea caz — plata cu alt CUI de plătitor",
                "Frecvent la cei cu mai multe firme: ordinul de plată pleacă din contul "
                "firmei, dar cu CUI-ul alteia. Banii sting datoria celeilalte firme, iar "
                "firma plătitoare rămâne cu datoria neachitată la ANAF. Plata nu are ce "
                "datorie proprie să stingă, deci merge tot pe 4482.",
                dr=[("4482.cui-gresit", 5000)], cr=[("5121", 5000)],
                rol="Bani ieșiți fără datorie proprie stinsă"),
            pas(4, "Extras de cont",
                "Cealaltă firmă returnează sumele. Până atunci, 4482 ține la vedere o "
                "creanță reală față de ea — nu față de buget.",
                dr=[("5121", 5000)], cr=[("4482.cui-gresit", 5000)],
                rol="Recuperarea de la firma beneficiară"),
            pas(5, "Verificare",
                "Sold 4482 = 0 pe ambele analitice. 444 nu are niciodată sold debitor. "
                "Rostul, comun cu 4481: să nu altereze rulajele conturilor curente — "
                "ANAF contraverifică exact corelațiile pe care ele le protejează. Sold "
                "4482 rămas de la un an la altul = o lămurire care n-a mai avut loc.",
                rol="Stare terminală: 4482 = 0, 444 fără sold contrar naturii"),
        ],
    ),
    # ------------------------------------------------------------------ F-81
    flux(
        "F-81", "Debitori diverși 461 — mijloc fix vândut și imputație", didactic=True,
        roluri="Creanță care nu vine din activitatea curentă",
        conturi="461, 7583, 7588, 4427, 6583, 2813, 213, 421, 5121",
        note="⚠ Notițele scriau imputația ca `121 − 826,45 / 4427 − 173,55`. Debitul e "
             "461; sumele erau bune (1.000 ÷ 1,21 = 826,45).",
        principiu="461 și 462 sunt printre primele conturi la care se uită și ANAF, și "
                  "băncile — și cele mai ușor de transformat în coș. Regula care le ține "
                  "curate: pe 461 intră doar creanțe care NU vin din activitatea "
                  "curentă, fiecare cu documentul ei. O sumă pusă acolo pentru că n-avea "
                  "unde altundeva e, prin definiție, o sumă nejustificată.",
        pasi=[
            pas(1, "Factură de vânzare a unui mijloc fix",
                "Cumpărătorul unui utilaj nu e client pentru activitatea curentă, deci "
                "nu 4111. Preț 20.000 lei + TVA 21%.",
                dr=[("461.cumparator", 24200)],
                cr=[("7583", 20000), ("4427", 4200)],
                rol="Pas revelator: nu e client, deci nu 4111 — e 461",
                revelator=True),
            pas(2, "Proces-verbal de scoatere din evidență",
                "Facturarea singură nu scoate activul din patrimoniu. Valoare de intrare "
                "30.000, amortizat 26.000, rămas 4.000.",
                dr=[("2813", 26000), ("6583", 4000)], cr=[("213", 30000)],
                rol="Scoaterea din evidență (vezi F-211)"),
            pas(3, "Extras de cont",
                "Încasarea prețului.",
                dr=[("5121", 24200)], cr=[("461.cumparator", 24200)],
                rol="Stingerea creanței"),
            pas(4, "Decizie de imputare + acordul salariatului",
                "Pagubă de 1.000 lei cu TVA produsă de un salariat. Nu e client, deci nu "
                "4111; și nu e cheltuiala firmei, deci nu se stinge în 121. 7588 se "
                "folosește pentru că nu există un cont de venit asociat direct, cum e "
                "707 pentru marfă. Dacă bunul deteriorat a fost dedus, TVA se colectează.",
                dr=[("461.salariat", 1000)],
                cr=[("7588", 826.45), ("4427", 173.55)],
                rol="Creanță față de salariat + venit + TVA colectată"),
            pas(5, "Stat de plată",
                "Reținerea din drepturile salariale. Imputația nu se poate face fără ca "
                "salariatul să fie informat și de acord (Codul muncii art. 254). "
                "Plafonul recuperării de comun acord e 5 salarii MINIME brute pe "
                "economie — verificat pe Codul muncii art. 254; notița spunea „5 salarii "
                "medii”, ceea ce era greșit. Peste plafon sau fără acord, doar prin "
                "instanță; reținerea efectivă e limitată la o treime din net (art. 169).",
                dr=[("421", 1000)], cr=[("461.salariat", 1000)],
                rol="Recuperarea prin reținere"),
            pas(6, "Verificare",
                "Sold 461 = 0 pe ambele analitice. Testul care contează la 31.12: orice "
                "sold rămas pe 461 trebuie să aibă un document care spune cine datorează "
                "ce și de ce. Cazul concret din notițe — nu mai există sold pe 4551, dar "
                "asociatul continuă să ia bani din bancă, iar sumele se pun pe 461 — "
                "apare la control drept creditare de societate inexistentă și bani scoși "
                "fără temei.",
                rol="Stare terminală: 461 = 0, sau sold cu document pe fiecare analitic"),
        ],
    ),
    # ------------------------------------------------------------------ F-82
    flux(
        "F-82", "Decontări din operațiuni în participație (458)", didactic=True,
        roluri="Cont de decontare între societăți asociate în participație",
        conturi="458, 704, 628, 4111, 4427, 5121",
        note="Entități afiliate (peste 25% acționari comuni, contul 451) sunt altceva: "
             "acolo se decontează împrumuturi, aici se împart venituri și cheltuieli.",
        principiu="Fiecare societate plătește impozit pe profit DOAR pe activitatea ei. "
                  "Una vine cu utilajele, alta cu angajații, dar facturarea o face una "
                  "singură — deci fără decont, ea ar plăti impozit și pe partea "
                  "partenerului. Transferul prin 458 nu e o plată, e o redistribuire de "
                  "venituri și cheltuieli, în oglindă la cele două societăți.",
        pasi=[
            pas(1, "Contract de participațiune",
                "Două societăți, un obiectiv comun, cote de 50/50. Contractul stabilește "
                "cine facturează și cum se împart rezultatele. Nu produce înregistrare "
                "contabilă — dar fără el, decontul de mai jos n-are temei.",
                rol="Documentul care stabilește cotele"),
            pas(2, "Factură către beneficiar",
                "Societatea A facturează întreaga lucrare: 100.000 lei + TVA 21%. "
                "Cheltuielile proprii ale lui A sunt de 20.000, ale lui B de 40.000.",
                dr=[("4111.beneficiar", 121000)],
                cr=[("704", 100000), ("4427", 21000)],
                rol="Venitul intră integral la societatea care facturează"),
            pas(3, "Decont de participație — partea de venit",
                "Cota de venit care îi revine lui B iese din veniturile lui A. Fără "
                "pasul ăsta, A ar plăti impozit pe profit pe activitatea partenerului.",
                dr=[("704", 50000)], cr=[("458.B", 50000)],
                rol="Pas revelator: venitul se redistribuie, nu se plătește",
                revelator=True),
            pas(4, "Decont de participație — partea de cheltuială",
                "A are cheltuieli proprii de 20.000, dar îi revine jumătate din cele "
                "60.000 comune, adică 30.000. Preia de la B diferența de 10.000.",
                dr=[("628", 10000)], cr=[("458.B", 10000)],
                rol="Cheltuielile se redistribuie în aceeași cotă"),
            pas(5, "Ordin de plată",
                "Decontarea soldului: A îi datorează lui B 60.000 lei. Înregistrările "
                "sunt în OGLINDĂ la B, pe analiticul 458.A.",
                dr=[("458.B", 60000)], cr=[("5121", 60000)],
                rol="Stingerea decontului"),
            pas(6, "Verificare",
                "Sold 458 = 0 după decontare. Testul care spune că decontul e corect: "
                "rezultatul lui A din operațiune = 100.000 − 50.000 − 20.000 − 10.000 = "
                "20.000 lei, adică exact jumătate din profitul comun de 40.000 "
                "(100.000 − 60.000). La B iese aceeași cifră, pe drumul invers.",
                rol="Stare terminală: 458 = 0, profitul împărțit în cotele contractuale"),
        ],
    ),
    # ------------------------------------------------------------------ F-90
    # Clasa 3, nu 4 — dar stă aici pentru că e despre același lucru ca restul
    # fișierului: cum se vede, dintr-o balanță, că ceva e greșit. Întrebarea
    # „de ce am rulaj pe 601 dacă n-am rulaj pe 301?” e o verificare de control,
    # iar răspunsul ei e o monografie.
    flux(
        "F-90", "Marfa devenită materie primă (301 = 371) și consumul din gestiune",
        didactic=True,
        roluri="Transfer între gestiuni + Consum documentat",
        conturi="301, 371, 601, 401, 4426",
        note="⚠ Notițele scriau perechea lui 608 ca `308`. E transpoziție de cifre: 381 "
             "e contul de ambalaje, iar 308 e „Diferențe de preț la materii prime” — un "
             "cont rectificativ, nu o gestiune de consumat.",
        principiu="Consumul trece PRIN GESTIUNE. Un bun trecut direct pe cheltuială "
                  "n-a intrat niciodată în evidență, deci nu poate fi scos din ea: n-ai "
                  "ce inventaria, n-ai ce justifica, și nu poți răspunde la întrebarea "
                  "„unde e”. Verificarea inversă, pe care o face și controlul: de ce am "
                  "rulaj pe 601 dacă n-am rulaj pe 301?",
        pasi=[
            pas(1, "Factură + notă de recepție",
                "Bunul intră ca MARFĂ, pentru că la recepție se credea că se revinde. "
                "10.000 lei + TVA 21%.",
                dr=[("371", 10000), ("4426", 2100)], cr=[("401.furnizor", 12100)],
                rol="Intrare în gestiunea de mărfuri"),
            pas(2, "Bon de transfer între gestiuni",
                "Se dovedește că bunul se consumă într-o lucrare, nu se revinde. Se mută "
                "în gestiunea de materii prime — pe bon de transfer, nu prin cheltuială.",
                dr=[("301", 10000)], cr=[("371", 10000)],
                rol="Pas revelator: gestiunea se schimbă înaintea consumului",
                revelator=True),
            pas(3, "Bon de consum",
                "Abia acum bunul devine cheltuială. ⚠ `601 = 371` ar fi asociat o "
                "cheltuială cu materii prime unei gestiuni de mărfuri, iar contul de "
                "cheltuială și-ar fi pierdut înțelesul. Formatorul e explicit: "
                "niciodată 601 la 371, nici dacă programul îl propune prestabilit.",
                dr=[("601", 10000)], cr=[("301", 10000)],
                rol="Consumul, cu document justificativ"),
            pas(4, "Verificare",
                "Sold 371 = 0 pe bunul transferat, sold 301 = 0 după consum, iar "
                "cheltuiala e pe contul care corespunde gestiunii din care a ieșit. "
                "Testul de coerență pe rulaje: rulaj 601 ≠ 0 cere rulaj 301 ≠ 0. De când "
                "s-a implementat SAF-T, modulul de stocuri se cere la control — nu "
                "ajunge să existe, trebuie să fie deja gestionat.",
                rol="Stare terminală: gestiunile golite, cheltuiala pe contul potrivit"),
        ],
    ),
]
