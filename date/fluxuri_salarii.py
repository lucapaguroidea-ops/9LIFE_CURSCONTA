"""Fluxurile din trainingul 21.08.2026 — salarii, rețineri, impozit pe venit.

Grupa 42x în afara salariului propriu-zis: concediile medicale, popririle, drepturile
neridicate, creanțele față de un fost salariat. Plus impozitul micro, care e tot clasa 4
(4418), chiar dacă subiectul lui e rezultatul exercițiului.

`F-413 Salarii complet` NU se dublează: monografia de bază rămâne acolo, iar fluxurile de
aici tratează ce se întâmplă în jurul ei. Un flux nou pentru fiecare situație care are
altă stare terminală — asta e granița, nu volumul de text.

Cifrele continuă exemplul din documentul de salarii: brut 50.000, net 29.250. Un
exemplu care traversează mai multe fluxuri se verifică singur, pentru că sumele trebuie
să se lege între ele.
"""
from .comun import flux, pas

FLUXURI_SALARII = [

    flux("F-64", "Concediu medical (împărțire angajator / FNUASS + rețineri)",
         didactic=True,
         roluri="Cheltuială proprie + Creanță socială + Datorie față de salariat",
         conturi="6458, 4382, 423, 4315, 4316, 444, 646, 436, 5121",
         note="Prima zi de concediu medical pentru boală obișnuită NU se plătește, "
              "februarie 2026 – decembrie 2027; regula nu se aplică urgențelor, "
              "accidentelor de muncă, sarcinii și carantinei. Baza: media veniturilor "
              "brute din ultimele 6 luni, plafonată la 12 salarii minime brute.",
         pasi=[
             pas(1, "Certificat de concediu medical + stat de plată",
                 "Indemnizație brută 1.000 lei. Primele zile le suportă angajatorul — "
                 "aici 250 lei — restul vine de la FNUASS. Numărul de zile suportate de "
                 "angajator depinde de codul de indemnizație.",
                 dr=[("6458", 250), ("4382", 750)], cr=[("423", 1000)],
                 rol="Cheltuială proprie + Creanță de recuperat + Datorie"),
             pas(2, "Stat de plată — reținerile din indemnizație",
                 "Din indemnizația brută se rețin CAS 25% = 250 și, ÎNCEPÂND CU "
                 "VENITURILE LUNII AUGUST 2026, CASS 10% = 100 (Legea 170/2026 — până "
                 "atunci CASS nu se datora). Impozitul de 10% se aplică pe ce rămâne: "
                 "10% × 650 = 65.",
                 dr=[("423", 415)],
                 cr=[("4315", 250), ("4316", 100), ("444", 65)],
                 rol="Contribuții și impozit reținute din indemnizație"),
             pas(3, "Nota de contribuții — partea angajatorului",
                 "ROLUL ÎMPĂRȚIRII se vede aici. CAM se calculează DOAR pe partea "
                 "suportată de angajator: 2,25% × 250 = 5,63. Pe cele 750 de lei care "
                 "vin din FNUASS nu se datorează CAM — nu sunt cheltuiala firmei, sunt "
                 "bani avansați în numele casei.",
                 dr=[("646", 5.63)], cr=[("436", 5.63)],
                 rol="CAM doar pe partea proprie, nu pe indemnizația din fond",
                 revelator=True),
             pas(4, "Extras de cont — plata către salariat",
                 "Netul: 1.000 − 250 − 100 − 65 = 585 lei.",
                 dr=[("423", 585)], cr=[("5121", 585)],
                 rol="Stingerea datoriei față de salariat"),
             pas(5, "Extras de cont — decontarea cu FNUASS",
                 "Casa rambursează partea ei. 4382 e o CREANȚĂ: firma a avansat banii "
                 "casei, nu i-a cheltuit — de aceea cele 750 nu apar niciodată pe "
                 "cheltuieli, oricât ar trece prin datoria față de salariat.",
                 dr=[("5121", 750)], cr=[("4382", 750)],
                 rol="Încasarea creanței sociale"),
             pas(6, "Verificare",
                 "Sold 423 = 0 și sold 4382 = 0 pe indemnizația decontată. Pe rezultat "
                 "au rămas 250 (cheltuiala proprie) + 5,63 (CAM aferent ei). Un sold "
                 "4382 care nu se stinge înseamnă indemnizații nerecuperate de la casă "
                 "— bani ai firmei blocați, adesea din dosare incomplete.",
                 rol="Stare terminală: 423 și 4382 fără sold; pe cheltuieli doar partea "
                     "angajatorului și CAM-ul aferent ei"),
         ],
         principiu="Indemnizația trece integral prin datoria față de salariat, dar numai "
                   "o parte din ea e cheltuiala firmei — iar linia de demarcație "
                   "decide și baza CAM. Reținerile se fac pe TOATĂ indemnizația, "
                   "indiferent cine o suportă; CAM-ul, doar pe partea proprie. Cine "
                   "trece toată indemnizația pe cheltuieli își subestimează rezultatul "
                   "și plătește CAM pe banii altcuiva."),

    flux("F-65", "Poprire pe salariu (rețineri datorate terților)",
         didactic=True,
         roluri="Intermediar / clarificare — firma reține pentru altcineva",
         conturi="421, 427, 5121",
         note="Art. 729 Cod procedură civilă: 1/2 pentru obligații de întreținere sau "
              "alocații pentru copii · 1/3 pentru alte datorii · la mai multe popriri, "
              "maximum 1/2 în total. Sub salariul minim net se urmărește doar partea "
              "care depășește jumătate din el.",
         pasi=[
             pas(1, "Adresă de înființare a popririi + stat de plată",
                 "Datorie obișnuită, deci limita e o treime: 29.250 / 3 = "
                 "9.750,00 lei. Fracția e o TREIME, nu „33,33%” — aproximarea zecimală "
                 "dă alt număr, iar limita e un prag legal, nu o estimare. "
                 "Se calculează din NET, nu din brut — banii merg la "
                 "executor, nu la stat, deci după ce statul și-a luat partea. La "
                 "obligații de întreținere limita ar fi fost 1/2, iar la mai multe "
                 "popriri pe aceeași sumă tot 1/2 e maximul, indiferent de natura "
                 "creanțelor.",
                 dr=[("421", 9750.00)], cr=[("427", 9750.00)],
                 rol="Datoria față de salariat scade, apare o datorie față de terț"),
             pas(2, "Extras de cont — plata către executor",
                 "ROLUL LUI 427 se vede aici: firma nu a câștigat și nu a cheltuit "
                 "nimic. A fost doar conductă între salariat și creditorul lui. Contul "
                 "intră și iese cu aceeași sumă, iar pe rezultat nu apare nimic.",
                 dr=[("427", 9750.00)], cr=[("5121", 9750.00)],
                 rol="Stingerea datoriei față de terț", revelator=True),
             pas(3, "Verificare",
                 "Sold 427 = 0 după virare. Un sold creditor care persistă înseamnă bani "
                 "opriți din salariul cuiva și nevirați — firma nu are ce explica: "
                 "trebuia fie să îi vireze, fie să nu îi rețină. Verificare în amonte: "
                 "dacă venitul salariatului e sub salariul minim NET, se poate urmări "
                 "doar partea care depășește jumătate din el — reținerea peste acest "
                 "prag îl păgubește pe salariat, nu pe debitor.",
                 rol="Stare terminală: sold 427 = 0; rulaj creditor = sold creditor pe "
                     "luna curentă"),
         ],
         principiu="427 e cont de tranzit, nu de rezultat. Banii care trec prin el nu "
                   "sunt ai firmei în niciun moment — sunt ai salariatului, opriți în "
                   "beneficiul creditorului lui. De aceea soldul lui e singurul din "
                   "grupa 42x care, rămas neachitat, trece din problemă contabilă în "
                   "problemă penală."),

    flux("F-66", "Drepturi de personal neridicate (421 → 426)",
         roluri="Datorie care își schimbă natura, nu dispare",
         conturi="421, 426, 5311",
         note="Se identifică prin corelația sold 421 = restul de plată de pe stat. "
              "Diferența se caută pe luni, scoțând statele.",
         pasi=[
             pas(1, "Stat de plată + registru de casă",
                 "Doi salariați nu și-au ridicat salariile: 3.400 lei. Datoria rămâne "
                 "integral, doar că nu mai e „salariu de plătit luna asta”.",
                 dr=[("421", 3400)], cr=[("426", 3400)],
                 rol="Reclasificare în interiorul pasivului"),
             pas(2, "Dispoziție de plată — ridicarea ulterioară",
                 "Salariatul se prezintă și își ia banii.",
                 dr=[("426", 3400)], cr=[("5311", 3400)],
                 rol="Stingerea datoriei"),
             pas(3, "Verificare",
                 "După reclasificare, sold 421 = restul de plată de pe statul curent, "
                 "iar sold 426 = exact sumele nerevendicate. Fără pasul 1, corelația se "
                 "rupe și pare că firma are restanțe de salarii — când de fapt are bani "
                 "nerevendicați.",
                 rol="Stare terminală: sold 421 reconciliat cu statul; sold 426 = doar "
                     "sumele nerevendicate, urmărite până la ridicare"),
         ],
         principiu="Un salariu neridicat nu e o economie și nu e o restanță. E aceeași "
                   "datorie, mutată pe un cont care spune de ce nu s-a plătit — iar "
                   "mutarea e ce face corelația cu statul de plată să funcționeze din "
                   "nou."),

    flux("F-67", "Creanță față de un fost salariat (4282)",
         roluri="Creanță — un activ, nu o reducere de cheltuială",
         conturi="4282, 7588, 5311",
         note="⚠️ Notițele foloseau 4428 (TVA neexigibilă). Contul corect e 4282, "
              "„Alte creanțe în legătură cu personalul”.",
         pasi=[
             pas(1, "Notă de lichidare + proces-verbal de predare-primire",
                 "Salariatul pleacă fără să predea un echipament de protecție de 400 "
                 "lei. Firma are de primit, deci are o creanță.",
                 dr=[("4282", 400)], cr=[("7588", 400)],
                 rol="Creanță față de fostul salariat + Venit din despăgubiri"),
             pas(2, "Chitanță / extras de cont",
                 "Încasarea. Crește un activ (casa) și scade alt activ (creanța) — nu e "
                 "nevoie de niciun cont de pasiv, pentru că firma nu datorează nimic.",
                 dr=[("5311", 400)], cr=[("4282", 400)],
                 rol="Stingerea creanței"),
             pas(3, "Verificare",
                 "Sold 4282 = 0 după încasare. Un sold CREDITOR pe 4282 e contrar "
                 "naturii contului și înseamnă ori încasare dublă, ori înregistrare "
                 "inițială pe partea greșită (C-23).",
                 rol="Stare terminală: sold 4282 = 0, niciodată creditor"),
         ],
         principiu="Ce ai de primit e activ, ce ai de dat e pasiv — iar întrebarea se "
                   "pune despre operațiunea economică, nu despre conturi. La încasare "
                   "nu îți trebuie „opusul băncii”: crește un activ și scade altul, iar "
                   "totalul bilanțului nu se mișcă."),

    flux("F-68", "Impozitul pe venitul microîntreprinderii (698 → 4418)",
         roluri="Cheltuială cu impozitul + Datorie fiscală",
         conturi="698, 4418, 5121",
         note="Condiții cumulative: cel puțin un salariat cu normă întreagă (sau "
              "contract de mandat la nivelul minimului) ȘI venituri sub prag. "
              "❓ Pragul de 100.000 EUR și cota de 1% — de confirmat.",
         pasi=[
             pas(1, "Calcul trimestrial pe veniturile totale",
                 "Venituri trimestriale 240.000 lei, cotă 1%: impozit 2.400 lei. Baza e "
                 "VENITUL, nu profitul — de aceea contul e 698, nu 691.",
                 dr=[("698", 2400)], cr=[("4418", 2400)],
                 rol="Cheltuială cu impozitul pe venit + Datorie"),
             pas(2, "Extras de cont — plata la termen (D100 trimestrial)",
                 "Plata până la data de 25 a lunii următoare trimestrului.",
                 dr=[("4418", 2400)], cr=[("5121", 2400)],
                 rol="Stingerea datoriei fiscale"),
             pas(3, "Verificare",
                 "Sold 4418 creditor = impozitul trimestrului curent, nedatorat încă. "
                 "Un sold DEBITOR înseamnă că s-a plătit mai mult decât se datorează — "
                 "de investigat, nu de reportat.",
                 rol="Stare terminală: sold 4418 creditor, egal cu obligația "
                     "trimestrului curent"),
         ],
         principiu="Microul e impozit pe VENIT, nu pe profit — de aceea nu poate sta pe "
                   "un analitic al lui 691. La depășirea pragului, societatea trece la "
                   "impozit pe profit din TRIMESTRUL depășirii, nu din următorul: "
                   "clientul care se apropie de prag trebuie anunțat înainte, nu după."),

    flux("F-69", "Decizie de impunere ANAF prin 4481 (în afara rulajului curent)",
         didactic=True,
         roluri="Datorie fiscală izolată de circuitul declarativ",
         conturi="4481, 6588, 6581, 5121",
         note="Sumele stabilite prin decizie de impunere NU ajung niciodată în decontul "
              "de TVA. ❓ Notițele din 21.08 spun „4423 cu analitic distinct”, cele din "
              "26.08 spun 4481 — vezi principiul și întrebarea din listă.",
         pasi=[
             pas(1, "Decizie de impunere după inspecție fiscală",
                 "ANAF stabilește TVA suplimentar de plată 18.000 lei, pentru perioade "
                 "anterioare. Suma e o datorie reală, dar nu provine din operațiunile "
                 "lunii — și nici din vreo lună pe care decontul curent o acoperă. "
                 "Cheltuiala e nedeductibilă fiscal.",
                 dr=[("6588", 18000)], cr=[("4481.decizie", 18000)],
                 rol="Cheltuială nedeductibilă + Datorie din act de control"),
             pas(2, "Aceeași decizie — accesoriile",
                 "Dobânzile și penalitățile merg pe același cont de datorie, cu "
                 "cheltuiala lor proprie, tot nedeductibilă.",
                 dr=[("6581", 2700)], cr=[("4481.decizie", 2700)],
                 rol="Accesoriile, pe același analitic de decizie"),
             pas(3, "Extras de cont — plata deciziei",
                 "Se plătește ca orice datorie fiscală.",
                 dr=[("4481.decizie", 20700)], cr=[("5121", 20700)],
                 rol="Stingerea datoriei"),
             pas(4, "Închiderea lunară de TVA",
                 "AICI se vede rostul contului separat: închiderea lunii lucrează pe "
                 "4423 și NU are ce atinge, pentru că decizia n-a intrat niciodată "
                 "acolo. Un ANALITIC al lui 4423 n-ar fi fost de ajuns — rămâne tot în "
                 "soldul lui 4423, adică fix contul pe care decontul îl reconciliază.",
                 rol="Pas revelator: decizia stă în afara contului pe care îl "
                     "reconciliază decontul",
                 revelator=True),
             pas(5, "Verificare",
                 "Sold 4481 = 0 după plată. Rulajele lui 4423, 4426 și 4427 rămân exact "
                 "cele din jurnalele de TVA, deci corelația decont ↔ balanță trece "
                 "nemodificată. Sold 4481 rămas de la un an la altul = decizie "
                 "neachitată sau neurmărită.",
                 rol="Stare terminală: 4481 = 0; corelația decont ↔ balanță intactă"),
         ],
         principiu="Formatorul a dat două reguli incompatibile pentru același caz, la "
                   "cinci zile distanță: 21.08 — „4423 cu analitic distinct, ca să nu "
                   "ajungă în decont”; 26.08 — „nu prin 4423, pentru că denaturează "
                   "rulajul curent, ci prin 4481”. Fluxul urmează varianta din 26.08 "
                   "pentru că e singura care dă un motiv VERIFICABIL: analiticul separă "
                   "evidența, dar nu separă SOLDUL, iar decontul se compară pe soldul "
                   "sintetic. Decizia finală îi aparține însă formatorului, nu "
                   "monografiei — de aceea cazul e și întrebare deschisă."),

    flux("F-70", "Închiderea lunară a obligațiilor salariale (rulaj = sold)",
         didactic=True,
         roluri="Stingerea datoriilor lunii + testul de bun-platnic",
         conturi="444, 4315, 4316, 436, 5121",
         note="Corelația care deosebește o firmă la zi de una cu restanțe, fără să ceri "
              "niciun document în plus: totul e deja în balanță.",
         pasi=[
             pas(1, "Nota de salarii a lunii curente (iulie)",
                 "Obligațiile lunii se creează pe credit: CAS 12.500, CASS 5.000, "
                 "impozit 3.250, CAM 1.125. Total datorat pentru iulie: 21.875.",
                 dr=[("421", 20750), ("646", 1125)],
                 cr=[("4315", 12500), ("4316", 5000), ("444", 3250), ("436", 1125)],
                 rol="Constituirea obligațiilor lunii"),
             pas(2, "Extras de cont — 25 iulie, plata obligațiilor lunii IUNIE",
                 "Pe 25 iulie se plătesc obligațiile lunii iunie, nu ale lui iulie. "
                 "Presupunem că iunie avea aceleași sume.",
                 dr=[("4315", 12500), ("4316", 5000), ("444", 3250), ("436", 1125)],
                 cr=[("5121", 21875)],
                 rol="Stingerea obligațiilor lunii precedente"),
             pas(3, "Verificare la 31 iulie — pasul revelator",
                 "ROLUL DECALAJULUI se vede aici. Rulajul debitor al lunii e plata lui "
                 "iunie; rulajul creditor e obligația lui iulie. Ce rămâne pe credit e "
                 "exact obligația lui iulie — deci sold creditor = rulaj creditor. "
                 "Dacă soldul e MAI MARE, diferența e o restanță din trecut, iar "
                 "mărimea ei spune de cât timp.",
                 rol="Rulajul creditor al lunii = soldul creditor la finalul lunii",
                 revelator=True),
             pas(4, "Verificare",
                 "Sold 444 = rulaj creditor 444; sold 4315 și sold 4316 = rulajele lor; "
                 "sold 436 = rulaj creditor 436. Toate patru se confruntă cu fișa pe "
                 "plătitor din SPV. Egalitatea e testul de bun-platnic (C-25, C-26).",
                 rol="Stare terminală: pe 444, 4315, 4316 și 436, soldul creditor "
                     "egalează rulajul creditor al lunii"),
         ],
         principiu="O datorie constituită lunar și achitată în luna următoare are, la "
                   "sfârșit de lună, sold creditor egal cu rulajul creditor. Nu e o "
                   "coincidență de calendar, e o consecință a decalajului de scadență — "
                   "și de aceea orice depășire e restanță, nu decalaj. Verificarea nu "
                   "cere niciun document în plus: totul e deja în balanță."),
]
