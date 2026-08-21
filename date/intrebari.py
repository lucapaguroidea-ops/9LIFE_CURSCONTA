"""Cele 21 de întrebări deschise, grupate pe temă contabilă.

Provin din secțiunile „rămase deschise” ale celor trei documente revizuite. Erau
împrăștiate în trei fișiere, în trei formate, numerotate independent — imposibil de
trimis cuiva așa.

Grupate pe TEMĂ, nu pe training: formatorul răspunde o dată la „446 vs. 462 la
comisionarul vamal”, nu de trei ori în trei contexte diferite.

Fiecare întrebare poartă:
  sursa       — de unde vine, ca să se poată urmări înapoi
  intrebare   — formularea trimisibilă, fără jargon intern
  context     — ce spuneau notițele, ca formatorul să nu recitească
  conteaza    — ce anume din sistem depinde de răspuns (flux / modul / corelație)
  presupunere — ce am ales între timp, unde a trebuit să aleg. Lipsește când nu a
                fost nevoie de nicio presupunere.

Documentul pe care îl privește o întrebare NU e un câmp: se DEDUCE din data din `sursa`,
pentru că trainingurile 2, 3 și 4 au fiecare documentul lor. Sursa din 19.08 alimentează
patru documente deodată, deci acolo nu e nimic de dedus — cele cinci excepții sunt
scrise o singură dată, în `DOC_EXPLICIT` de mai jos.
"""


def q(sursa, intrebare, context, conteaza, presupunere=None,
      raspuns=None, temei=None, verificat=None, decizie=False):
    """O întrebare deschisă, eventual cu răspuns verificat pe surse publice.

    `raspuns`   — formulat ca fapt, nu ca opinie
    `temei`     — actul normativ și articolul. FĂRĂ TEMEI NU EXISTĂ RĂSPUNS: o părere
                  care arată ca un fapt e mai rea decât o întrebare deschisă
    `verificat` — data confruntării cu sursele; praguri ca salariul minim se schimbă
    `decizie`   — nu e o întrebare de drept, ci o alegere a cabinetului. Nicio sursă
                  nu poate răspunde la „ce standard folosim noi”, deci nu se caută
    """
    return dict(sursa=sursa, intrebare=intrebare, context=context,
                conteaza=conteaza, presupunere=presupunere,
                raspuns=raspuns, temei=temei, verificat=verificat, decizie=decizie)


TEME = [
    ("Repartizarea rezultatului și rezultatul reportat", [
        q("training 07.08.2026, întrebarea 1",
          "Care este temeiul legal al termenului de 3 ani pentru a decide ce se face cu "
          "soldul rămas în 1171?",
          "Notițele spuneau: „1171 → decis, în curs de 3 ani, ce face cu diferența dintre "
          "250 și 125 lei” — deci profitul reportat ar trebui repartizat într-un interval "
          "de trei ani. Nu am găsit termenul ăsta în Legea 31/1990 și nici în Codul fiscal.",
          "F-103 (repartizarea rezultatului) și MOD_CAPITALURI. Dacă termenul există, "
          "modulul ar trebui să semnaleze soldurile 1171 mai vechi de 3 ani; dacă nu, "
          "semnalarea ar fi un fals pozitiv la fiecare client cu profit nerepartizat.",
          "Nu l-am implementat. MOD_CAPITALURI raportează soldul 1171 pe an, prin C-21, "
          "fără să-l judece după vechime."),

        q("training 07.08.2026, întrebarea 2",
          "În exemplul cu rezerva legală, profitul era 250 sau 2.500 lei?",
          "Notițele au „121 = 250 lei” și imediat „129 - 1061 = 125 lei”. Dar 5% din 250 "
          "înseamnă 12,50 lei, nu 125. Cifrele se leagă doar dacă profitul era 2.500.",
          "F-103 și MOD_CAPITALURI folosesc exemplul ca test. Am nevoie să știu dacă a fost "
          "o scăpare de notare sau dacă mi-a scăpat mie o regulă de calcul.",
          "Am folosit 2.500 lei, singura variantă în care 5% dau 125. Dacă profitul chiar "
          "era 250, atunci procentul aplicat nu era 5% și trebuie relămurit."),

        q("training 07.08.2026, întrebarea 4",
          "Pierderile nedeductibile fiscal se urmăresc pe analitic al lui 1171 sau pe alt cont?",
          "Notițele: „sunt anumite pierderi care nu sunt deductibile fiscal — astea se "
          "înregistrează într-un cont separat”. Nu s-a spus care.",
          "C-21 cere ca 1171 să aibă analitic pe an, cu sensul debitor/creditor explicit. "
          "Dacă pierderea nedeductibilă are cont propriu, corelația trebuie extinsă, iar "
          "recuperarea în 5 ani (70% din profitul impozabil) se urmărește altfel.",
          "Am lăsat 1171 cu analitic pe an, fără separare a pierderii nedeductibile."),

        q("training 07.08.2026, întrebarea 6",
          "Care este actul normativ care a permanentizat termenul de 25 iunie pentru D101?",
          "Notițele anunțau pentru 2027 „101 în Martie, bilanț în mai”. Termenul s-a mutat "
          "însă la 25 iunie, iar în documentul revizuit am marcat asta ca schimbare — dar "
          "fără să pot cita actul care o face permanentă, nu doar valabilă pentru un an.",
          "Checklistul de închidere din documentele revizuite și calendarul din foaia "
          "Legendă. Un termen greșit aici se propagă la toți clienții.",
          "Am scris 25 iunie, marcat ca „de reconfirmat”.",
          raspuns='Termenul de 25 iunie **nu a fost de la început permanent**: a venit prin **OUG 153/2020**, care l-a prelungit pentru perioada 2021–2025, odată cu bonificațiile pentru capital propriu pozitiv și în creștere. 2025 a fost ultimul an de aplicare a acelui mecanism, iar termenul uniform de 25 iunie a anului următor se aplică de la 2026. ❓ Actul care l-a permanentizat nu l-am putut identifica cu certitudine — surse îl descriu ca măsură adoptată în 2026, dar fără să-l numească. De confirmat înainte de a-l cita unui client.',
          temei='OUG 153/2020, art. I — aplicabil 2021–2025. Permanentizarea: act neidentificat.',
          verificat="21.08.2026"),
    ]),

    ("Corectarea erorilor din exerciții anterioare", [
        q("training 07.08.2026, întrebarea 5",
          "Cum se tratează o factură a exercițiului anterior, descoperită neînregistrată "
          "în anul curent — și când se folosește 1174 în loc de 628 cu semn schimbat?",
          "Notițele conțineau întrebarea ca atare, fără răspuns, plus observația că 1174 "
          "„a fost introdus ca să nu mai denaturăm profitul anilor” și că „lucrurile se "
          "complică atunci când nu mai am sold în 1171, pentru că proprietarul a decis să "
          "ia dividende”.",
          "F-105 (corecția erorilor prin 1174) și MOD_CAPITALURI. Pragul de semnificație "
          "din politicile contabile decide între cele două căi, dar nu știu ce prag "
          "folosește cabinetul.",
          "Am construit arborele de decizie pe pragul de semnificație, cu 1174 pentru "
          "erorile semnificative din exerciții închise și corecția pe cheltuiala curentă "
          "sub prag. C-18 cere ca 1174 să ajungă la zero la 31.12."),
    ]),

    ("Capital social și activ net", [
        q("training 07.08.2026, întrebarea 7",
          "Cum se documentează reîntregirea activului net cerută de Legea 239/2025 — prin "
          "conversia creanței asociatului în capital sau prin aport nou?",
          "Legea condiționează dividendele și restituirile de împrumuturi de un activ net "
          "de cel puțin jumătate din capitalul social. Notițele semnalau problema, fără "
          "procedura de ieșire din blocaj.",
          "C-20 (testul de activ net) și MOD_CAPITALURI, care azi doar semnalează blocajul. "
          "Ca să propună o cale de rezolvare, are nevoie de varianta preferată a cabinetului.",
          "Modulul semnalează blocajul și se oprește acolo — nu propune nicio soluție."),

        q("training 07.08.2026, întrebarea 8",
          "Verificăm sistematic pragul de capital social minim (500 / 5.000 lei) pe tot "
          "portofoliul de clienți, sau doar la firmele noi?",
          "Pragurile noi din 2026: 500 lei la înființare, 5.000 lei la cifră de afaceri "
          "netă peste 400.000 lei. Al doilea prag prinde firme existente, nu doar noi.",
          "F-101 (constituirea capitalului) și checklistul de deschidere de dosar. Dacă "
          "verificarea e sistematică, intră în checklistul lunar, nu în cel de deschidere.",
          "Am pus-o în checklistul de deschidere a dosarului.",
          decizie=True),
    ]),

    ("Leasing și vehicule", [
        q("training 07.08.2026, întrebarea 3",
          "TVA nedeductibilă de pe rata de capital la leasingul financiar: se capitalizează "
          "în valoarea mijlocului fix (2133) sau se trece pe cheltuială (635 / 6588)?",
          "Notițele arătau capitalizarea TVA nededuse de pe AVANS în valoarea de intrare "
          "(150.000 + 5.250 = 155.250), dar pentru ratele lunare foloseau 6588. Practica e "
          "împărțită și în literatură.",
          "F-108 și MOD_LEASING_FIN. E singura variabilă a modulului care schimbă valoarea "
          "de intrare a mijlocului fix, deci și amortizarea, deci și impozitul pe profit pe "
          "toată durata contractului.",
          "Am făcut din ea o OPȚIUNE DE CONFIGURARE în modul (CAPITALIZEAZA / CHELTUIALA), "
          "cu implicit „capitalizează”, coerent cu tratamentul avansului. Nu am tranșat-o "
          "ca regulă.",
          raspuns='**Cheltuială, nu capitalizare.** La leasing, tratamentul diferă de achiziția directă: la cumpărarea internă a unui autoturism, TVA-ul nedeductibil de 50% intră în costul de achiziție, dar la leasing **nu** intră în valoarea mijlocului fix. Se înregistrează pe cheltuială, defalcat după componenta ratei: `635 = 4426` pentru 50% din TVA aferent ratei de capital, `666 = 4426` pentru cel aferent dobânzii, `628 = 4426` pentru cel aferent comisionului.',
          temei='Cod fiscal art. 298 (limitarea la 50%) coroborat cu OMFP 1802/2014 privind costul de achiziție; tratamentul distinct al leasingului față de achiziția directă.',
          verificat="21.08.2026"),
    ]),

    ("Imobilizări — prag și amortizare", [
        q("training 12.08.2026, întrebarea 1",
          "Recomandați alinierea pragului contabil de recunoaștere la cel fiscal (5.000 lei), "
          "sau menținerea unui prag intern mai mic pentru control de gestiune?",
          "OUG 8/2026 a urcat pragul fiscal la 5.000 lei. Pragul contabil rămâne la "
          "latitudinea entității, prin politici contabile.",
          "MOD_IMOBILIZARI face un test de prag la intrare. Dacă cele două praguri diferă, "
          "apar diferențe temporare de urmărit în registrul de evidență fiscală — un lucru "
          "pe care modulul nu îl tratează azi.",
          "Am folosit un singur prag, cel fiscal, și am semnalat în notițe că divergența "
          "produce diferențe temporare.",
          decizie=True),

        q("training 12.08.2026, întrebarea 2",
          "Excepția de la cumulul cu profitul reinvestit (art. 22 alin. 9) acoperă doar "
          "amortizarea accelerată, sau și pe cea superaccelerată de 65%?",
          "Notițele spuneau despre amortizarea accelerată că „nu poate să mai fie aplicată "
          "o altă facilitate fiscală = reducere pentru profitul reinvestit”, cu recomandarea "
          "de a calcula ce e mai avantajos.",
          "F-204 și MOD_IMOBILIZARI, la alegerea metodei de amortizare. Dacă excepția nu "
          "acoperă superaccelerata, calculul comparativ are altă concluzie.",
          "Nu am implementat comparația. Modulul propune metoda, fără să optimizeze fiscal.",
          raspuns="Regula: cine aplică scutirea de impozit a profitului reinvestit **nu poate opta pentru amortizarea accelerată** pentru activele respective — se amortizează liniar sau degresiv. Există însă o **excepție pentru 2026**: dacă scutirea se aplică pentru subgrupa 2.1 (echipamente tehnologice — mașini, utilaje și instalații de lucru) și pentru calculatoare și echipamente periferice, contribuabilul **poate** opta pentru amortizare accelerată.",
          temei="Cod fiscal art. 22 alin. (9), cu trimitere la art. 28 alin. (5) lit. b) pentru excepția din 2026.",
          verificat="21.08.2026"),
    ]),

    ("Imobilizări — ieșiri din gestiune", [
        q("training 12.08.2026, întrebarea 3",
          "Care este baza legală exactă pentru a trata ca nedeductibilă diferența dintre "
          "valoarea rămasă și prețul de vânzare, față de art. 28 alin. (17)?",
          "Notițele: la vânzarea cu 50.000 a unei clădiri cu valoare rămasă 70.000, "
          "„50k cheltuieli deductibile, 20k cheltuieli nedeductibile”, cu excepția cazului "
          "în care există dovezi (clădire avariată, deviz de service). Citit strict, "
          "art. 28 alin. (17) include pierderea în rezultatul fiscal.",
          "F-211 și MOD_IESIRE_MF. E testul central al modulului: azi calculează diferența "
          "și cere documentul justificativ, dar nu poate cita articolul pe care se sprijină.",
          "Modulul semnalează riscul și cere documentarea prețului, invocând art. 11 "
          "(reîncadrare) și art. 25 alin. (1) (scopul activității economice) — nu art. 28.",
          raspuns="**Nu există un asemenea temei — presupunerea din notițe e inversă.** La vânzarea unui mijloc fix la prețul pieței, valoarea rămasă neamortizată e cheltuială **deductibilă**, chiar dacă prețul e sub ea. Limitarea reală e alta și privește doar **autoturismele din categoria M1**: acolo valoarea rămasă e deductibilă în limita a **1.500 lei × numărul de luni rămase** de amortizat din durata normală de funcționare.",
          temei="Cod fiscal art. 28 alin. (17) și normele metodologice aferente (limitarea M1).",
          verificat="21.08.2026"),

        q("training 12.08.2026, întrebarea 5",
          "La o casare din care nu rezultă nici deșeuri, nici piese reutilizabile, cum se "
          "justifică deductibilitatea valorii rămase neamortizate?",
          "Notițele tratau cazul cu valorificare (piese pe 3024, venit pe 7588), dar nu și "
          "pe cel fără nicio recuperare.",
          "F-212 (casarea) și MOD_IESIRE_MF, unde valoarea pieselor recuperate poate fi "
          "zero. Fără răspuns, modulul nu poate spune dacă procesul-verbal de scoatere din "
          "funcțiune e suficient singur.",
          "Modulul acceptă valoarea zero a recuperărilor și lasă deductibilitatea "
          "nejudecată, cu procesul-verbal ca singur document.",
          raspuns="**Nu se cere nici deșeu, nici piesă reutilizabilă.** Cheltuielile înregistrate ca urmare a casării unui mijloc fix cu valoare fiscală incomplet amortizată sunt, prin lege, cheltuieli efectuate în scopul desfășurării activității economice — deci deductibile. Documentația de casare rămâne necesară ca probă a operațiunii, nu ca o condiție de deductibilitate.",
          temei="Cod fiscal art. 28 alin. (17).",
          verificat="21.08.2026"),
    ]),

    ("Imobilizări — control și raportare", [
        q("training 12.08.2026, întrebarea 4",
          "În secțiunea Active din D406 (SAF-T) se raportează și 231 (investiții "
          "neterminate), și 261 (imobilizări financiare)?",
          "Notițele menționau că informația din modulul de imobilizări „merge în 406”, fără "
          "să delimiteze ce anume intră.",
          "Coloana Declarativ a fluxurilor F-208 (imobilizări în curs) și F-213 "
          "(imobilizări financiare). Azi nu marchez D406 pe ele, ca să nu afirm ceva greșit.",
          "Le-am lăsat nemarcate în coloana Declarativ."),

        q("training 12.08.2026, întrebarea 6 — PUNCTUL CEL MAI IMPORTANT",
          "Ne puteți da procedura scrisă de reconciliere, pentru cazul în care analiticul "
          "din balanța contabilă nu corespunde cu registrul mijloacelor fixe?",
          "Ultimul punct al trainingului 3, rămas nefinalizat: „am verificat analiticul cu "
          "sinteticul → am verificat firma X, avem în 212 x lei, dar în balanța contabilă / "
          "imobilizări am x, y, z → să vedem o procedură, ce e de făcut.” Formatorul a "
          "promis-o și sesiunea s-a încheiat înainte.",
          "F-214 este singurul flux de PROCEDURĂ din tot sistemul — nu produce note "
          "contabile, descrie un control lunar. Azi se oprește la „dacă soldurile nu "
          "corespund”, fără pașii de rezolvare. C-15 depinde de aceeași procedură.",
          "Am scris pașii de identificare (listing, comparare pe perechi 21x↔28x, fișă de "
          "cont), dar NU și pașii de corecție — aceia sunt procedura promisă.",
          decizie=True),
    ]),

    ("Stocuri și producție", [
        q("training 14.08.2026, întrebarea 1",
          "Care sunt celelalte metode de calculație a costurilor acceptate de OMFP "
          "1802/2014, și în ce situații se alege fiecare?",
          "Notițele menționau metoda pe comenzi ca fiind cea mai utilizată, în contextul "
          "producției de termopane. Celelalte (pe faze, pe produs, standard-cost) au rămas "
          "doar enumerate.",
          "F-311 (producția multi-stadiu) ține gestiunea lui 331 analitic pe comandă. Pe "
          "faze, structura analitică e alta, deci și fluxul.",
          "Am implementat doar metoda pe comenzi."),
    ]),

    ("TVA — import, vamă, taxare inversă", [
        q("training 14.08.2026, întrebarea 3",
          "La decontarea cu comisionarul vamal folosiți 446 sau 462? Care e standardul "
          "cabinetului și de ce?",
          "Notițele foloseau 446, cu observația proprie că „e o înregistrare puțin forțată, "
          "pentru că e un cont de pasiv”. Unele cabinete folosesc 461/462.",
          "F-319 (import prin comisionar) și analiticul 446.VAMA din foaia Analitice. "
          "Contul ales determină unde apare soldul în bilanț: datorie la buget vs. datorie "
          "către un terț.",
          "Am păstrat 446.VAMA, ca în notițe, și am notat 461/462 ca alternativă.",
          decizie=True),

        q("training 14.08.2026, întrebarea 4",
          "Verificăm sistematic dacă clienții importatori îndeplinesc condițiile pentru "
          "certificatul de amânare de la plata TVA în vamă?",
          "Certificatul înlocuiește plata efectivă a TVA în vamă cu taxare inversă "
          "(4426 = 4427) — avantaj mare de cash-flow. Notițele nu îl menționau deloc; l-am "
          "adăugat eu la revizuire.",
          "F-320 (import cu plată directă) capătă o a treia variantă dacă certificatul "
          "există. Ar trebui să intre în checklistul de deschidere a dosarului.",
          "L-am adăugat ca variantă în documentul revizuit, dar nu în checklist.",
          decizie=True),

        q("training 14.08.2026, întrebarea 7",
          "Derogarea UE pentru taxarea inversă la cereale și electronice avea termen "
          "31.12.2026 — a fost prelungită?",
          "Art. 331 alin. (6) limitează în timp o parte din categorii, iar Consiliul UE a "
          "prelungit derogarea succesiv. Nu se poate presupune prelungirea automată.",
          "F-402 (taxare inversă internă) și lista de categorii din documentul revizuit. "
          "Aplicarea taxării inverse după expirare înseamnă factură greșit întocmită.",
          "Am marcat termenul în document cu avertisment de reverificare.",
          raspuns="Derogarea e prelungită până la **31 decembrie 2026** și acoperă opt operațiuni: cereale și plante tehnice, certificate de emisii de gaze cu efect de seră, energie electrică și gaze naturale către comercianți persoane impozabile, certificate verzi, telefoane mobile, dispozitive cu circuite integrate, console de jocuri, tablete și laptopuri. Pentru ultimele patru categorii, taxarea inversă se aplică **doar dacă valoarea fără TVA de pe factură e cel puțin 22.500 lei**. La data verificării **nu e publicată o prelungire dincolo de 31.12.2026** — deci expiră peste patru luni dacă nu intervine una.",
          temei="Cod fiscal art. 331; decizie a Consiliului UE de prelungire până la 31.12.2026. Reverificat la 21.08.2026.",
          verificat="21.08.2026"),
    ]),

    ("TVA — ajustări fără document", [
        q("training 14.08.2026, întrebarea 2",
          "La lipsa la inventar, practica implicită a cabinetului este colectarea de TVA "
          "sau ajustarea dreptului de deducere? Ce set de documente se cere clientului?",
          "Notițele spuneau simplu „trebuie să colectez și TVA”. La revizuire am găsit că "
          "tratamentul diferă: lipsă imputabilă → colectare; neimputabilă nejustificată → "
          "ajustare; bunuri distruse cu documente → fără ajustare.",
          "F-406 (înregistrări fără document) și corelațiile C-03 / C-04, unde ajustările "
          "care nu vin din facturi trebuie să apară în jurnale cu semnul corect. Cele două "
          "tratamente ating conturi diferite, deci și jurnale diferite.",
          "Am descris toate patru situațiile, fără să declar una ca implicită.",
          decizie=True),
    ]),

    ("Obligații de mediu", [
        q("training 14.08.2026, întrebarea 5",
          "Care este termenul curent de depunere a declarației la Fondul pentru Mediu — "
          "lunar sau trimestrial?",
          "Notițele nu dădeau termenul, iar acesta s-a modificat de mai multe ori. La "
          "revizuire am scris „verifică termenul curent pe afm.ro”, ceea ce nu e un răspuns.",
          "F-310 (ambalaje și taxa AFM) și checklistul lunar. Un termen greșit produce "
          "penalități direct.",
          "Am lăsat termenul nespecificat, cu trimitere la sursa oficială.",
          raspuns="**Lunar sau trimestrial**, după tipul de obligație, cu termen **25 a lunii următoare** perioadei de raportare. Depunerea se face exclusiv electronic, prin platforma AFM-Online, cu semnătură electronică calificată — de la 1 iulie 2022 nu se mai acceptă depunerea pe hârtie.",
          temei="Procedura de declarare la Fondul pentru mediu; depunere electronică obligatorie din 1.07.2022.",
          verificat="21.08.2026"),
    ]),

    ("Material lipsă din notițe", [
        q("training 14.08.2026, întrebarea 6",
          "Ce fișier și ce sarcină erau în spatele notițelor „Fișierul atașat arată "
          "corelații importante între conturi” și „task”?",
          "Ambele au rămas fără conținut în notițele originale — un rând care trimite la un "
          "atașament și un rând cu un singur cuvânt, „task”.",
          "Fișierul cu corelații ar putea conține exact materialul din foaia „Corelații de "
          "control”, care azi are 22 de corelații construite de mine. Dacă există o listă a "
          "formatorului, merită confruntată cu a mea.",
          "Am construit corelațiile din notițe și din practică, fără fișierul original."),
    ]),

    ("Plafoane de numerar și contul 455", [
        q("training 19.08.2026, punctul 1",
          "Care sunt valorile exacte ale plafoanelor din Legea 70/2015 în forma modificată "
          "prin Legea 296/2023, la data operațiunii?",
          "Notițele rețin 5.000 lei B2B, 10.000 lei încasări de la persoane fizice și "
          "50.000 lei între persoane fizice, plus un plafon separat pentru soldul casieriei "
          "la sfârșitul zilei. Sunt și plafoane totale zilnice, peste cele per persoană.",
          "Documentul „Control, documente și numerar”, secțiunea de plafoane. Un plafon "
          "greșit produce amendă direct, iar fragmentarea e interzisă expres — deci nici "
          "împărțirea pe tranșe nu e o ieșire.",
          "Am păstrat cifrele din notițe, cu mențiunea explicită că trebuie confirmate în "
          "textul în vigoare la data operațiunii.",
          raspuns="Între persoane juridice: **5.000 lei/zi și de persoană**. Magazine cash & carry: 5.000 lei de persoană, dar maximum **10.000 lei total pe zi**; plăți către ele, maximum 10.000 lei/zi. Avansuri spre decontare: **5.000 lei/zi** pentru fiecare persoană care a primit avansul. **Fragmentarea e interzisă expres** pentru facturi peste 5.000 lei, respectiv 10.000 la cash & carry. Legea 239/2025 **nu a modificat plafoanele** de la 1.01.2026, dar a eliminat pragul de 50.000 lei de la care era obligatorie acceptarea cardului și a introdus obligația unui cont de plăți deschis în România.",
          temei="Legea 70/2015, art. 3 și art. 4, în forma modificată prin Legea 296/2023 și Legea 239/2025.",
          verificat="21.08.2026"),
        q("training 19.08.2026, punctul 2",
          "Care sunt exact operațiunile în numerar interzise pe contul 455 și care e "
          "temeiul legal?",
          "Notițele spun doar că „plățile din 455 prin casierie nu mai sunt permise în "
          "condițiile anterioare”, fără să precizeze care condiții și din ce text.",
          "Foaia „Închideri periodice”, unde 455 e urmărit trimestrial fără flux în spate. "
          "Fără regula exactă, rândul rămâne gol declarat — nu se poate scrie o monografie "
          "pentru o restricție pe care n-o cunosc.",
          "Am lăsat 455 fără flux, cu golul marcat ca atare în foaie.",
          raspuns="Nu e un plafon, e o **interdicție**. Din **11 noiembrie 2023**, încasările și plățile reprezentând împrumuturi — indiferent de sumă — de la sau către asociați, acționari, administratori și alte persoane fizice **nu se mai pot face în numerar**, ci doar prin instrumente de plată fără numerar. Înalta Curte a stabilit că amenda de 25% se calculează la **totalul operațiunilor**, nu la depășirea unui plafon.",
          temei="Legea 70/2015 modificată prin Legea 296/2023, în vigoare din 11.11.2023. Cuantumul amenzii — jurisprudența ÎCCJ.",
          verificat="21.08.2026"),
    ]),

    ("Comportamentul softului la încasarea în plus", [
        q("training 19.08.2026, punctul 3",
          "Programul de contabilitate extrage automat TVA-ul din diferența trecută pe 419 "
          "la o încasare mai mare decât factura, sau trebuie forțat manual?",
          "Suma încasată în plus e TVA-inclusivă: din 5.000 lei ies 4.132,23 bază și 867,77 "
          "TVA. Dacă softul nu face extragerea, TVA-ul rămâne necolectat fără ca nimic "
          "să semnaleze.",
          "F-415 (încasare peste factură) și C-23. Notițele cer explicit contraverificarea "
          "lui 4427 după simulare — deci nici formatorul nu presupune că softul o face.",
          "Am scris fluxul cu extragerea explicită a TVA-ului, ca pas separat, tocmai ca "
          "să nu depindă de comportamentul softului.",
          decizie=True),
    ]),

    ("Convenții de analitic rămase de fixat", [
        q("training 19.08.2026, punctul 4",
          "Care e structura analitică exactă pe 4428 — pe situație și pe cotă?",
          "4428 apare în trei situații cu sensuri diferite: debitor la achiziția pe aviz "
          "(4428 = 408), creditor la livrarea pe aviz (418 = 4428) și creditor la mărfuri "
          "la preț cu amănuntul (371 = 4428). Notițele cer analitice pe fiecare situație "
          "ȘI pe fiecare cotă, dar nu dau nomenclatorul.",
          "F-316, F-408 și analiticul Tier A al lui 4428. Workbook-ul folosește azi "
          "4428.AM (amănunt) și 4428.INC (la încasare); pentru avizul de intrare nu există "
          "convenție scrisă.",
          "Am folosit convenția existentă din training 4 și am lăsat avizul de intrare fără "
          "analitic propriu — vizibil ca gol în foaia „Închideri periodice”.",
          decizie=True),
        q("training 19.08.2026, punctul 5",
          "Facturile nesosite pentru imobilizări se țin pe 408 cu analitic sau direct pe "
          "404 cu analitic?",
          "Exemplul din notițe folosește 231 = 408, dar furnizorul de imobilizări e 404. "
          "Notițele semnalează singure problema și cer stabilirea unei convenții "
          "consecvente.",
          "F-408 și F-207. Alegerea decide dacă furnizorii de exploatare se amestecă sau nu "
          "cu cei de imobilizări în balanța analitică — adică dacă 401/404 mai pot fi "
          "verificate separat.",
          "Am păstrat 408 cu analitic, ca în exemplul din notițe, semnalând alternativa în "
          "observația contului.",
          decizie=True),
    ]),

    ("Salarii — praguri și baze de calcul", [
        q("training 21.08.2026, punctul 1",
          "Care este salariul minim brut pe economie în vigoare, și de la ce dată?",
          "Notițele rețin 4.325 lei. Valoarea se schimbă prin hotărâre de guvern, uneori "
          "de mai multe ori pe an, iar verificarea normei parțiale se face contra ei.",
          "Verificarea lunară a statului de plată și corelația „minim proporțional cu "
          "norma”. Un prag depășit înseamnă contracte neconforme la toți salariații cu "
          "normă parțială, nu doar la unul.",
          "Am folosit 4.325 lei ca în notițe, marcat ❓ peste tot unde apare.",
          raspuns="**4.325 lei** brut, de la **1 iulie 2026** (anterior 4.050 lei). Minimul se aplică proporțional cu norma: 2.162,50 lei la jumătate de normă, 1.081,25 la un sfert. Tot de la 1 iulie 2026 și până la 31.12.2026, suma neimpozabilă scade de la 300 la 200 lei/lună.",
          temei="HG 146/2026 (salariul minim). Suma neimpozabilă — Cod fiscal, cu aplicare 1.07–31.12.2026.",
          verificat="21.08.2026"),

        q("training 21.08.2026, punctul 3",
          "Ce contribuții se datorează pentru indemnizația de concediu medical, și pe "
          "ce parte se rețin?",
          "Notițele acoperă împărțirea indemnizației între angajator și FNUASS "
          "(6458 / 4382 = 423), dar nu și reținerile din ea. Regulile diferă de cele "
          "ale salariului.",
          "Fluxul de concedii medicale și MOD_SALARII. Fără regulă, monografia se "
          "oprește la împărțire și nu ajunge la restul de plată.",
          "N-am afirmat nimic: documentul spune explicit că tratamentul reținerilor nu "
          "era în notițe.",
          raspuns="Din indemnizație se rețin **CAS 25%** și **impozit 10%**. **CASS 10% se datorează începând cu veniturile lunii august 2026** — până atunci nu se datora. Fac excepție indemnizațiile pentru accidente de muncă și boli profesionale, care rămân scutite de CASS. **CAM 2,25% NU se datorează** pe partea suportată din FNUASS: angajatorul datorează CAM doar pe zilele pe care le suportă el. Baza de calcul e media veniturilor brute din ultimele 6 luni, plafonată la 12 salarii minime brute pe lună.",
          temei="CAS: Cod fiscal art. 139 alin. (1) lit. o) și art. 144. CASS: Legea 170/2026, aplicabilă veniturilor din august 2026. CAM: Cod fiscal art. 220^5. Baza: OUG 158/2005.",
          verificat="21.08.2026"),

        q("training 21.08.2026, punctul 4",
          "Care e limita de reținere prin poprire pentru obligațiile de întreținere, "
          "față de treimea aplicabilă datoriilor obișnuite?",
          "Notițele rețin 33,33% din salariul net. Codul de procedură civilă prevede o "
          "limită mai mare pentru pensii de întreținere, și reguli de cumul când există "
          "mai multe popriri.",
          "Fluxul de popriri (427). Un procent greșit înseamnă ori reținere insuficientă "
          "— firma răspunde față de executor — ori excesivă, față de salariat.",
          "Am folosit treimea, marcând limita specială ca deschisă.",
          raspuns="Sunt **trei** reguli, nu una. **1/2** din venitul net lunar pentru obligații de întreținere sau alocații pentru copii; **1/3** pentru orice alte datorii. Când există mai multe popriri pe aceeași sumă, reținerea totală nu poate depăși **1/2**, indiferent de natura creanțelor. Iar dacă venitul e sub salariul minim net pe economie, se poate urmări doar partea care depășește **jumătate din salariul minim net** — prag de protecție pe care notițele nu-l aveau deloc.",
          temei="Codul de procedură civilă, art. 729 — Limitele urmăririi veniturilor bănești.",
          verificat="21.08.2026"),
    ]),

    ("Microîntreprindere — prag și cotă", [
        q("training 21.08.2026, punctul 2",
          "Care sunt pragul de venituri și cota de impozit pentru microîntreprinderi, "
          "în vigoare la data operațiunii?",
          "Notițele rețin 100.000 EUR și 1%. Pragul a fost coborât în trepte în anii "
          "anteriori, iar cota a avut două paliere. Ambele sunt din Codul fiscal, deci "
          "se pot schimba prin ordonanță.",
          "Fluxul de impozit micro (698 = 4418) și avertizarea clientului care se apropie "
          "de prag. Trecerea se face din trimestrul depășirii, deci un prag greșit "
          "înseamnă o declarație greșită, nu doar o estimare.",
          "Am folosit 100.000 EUR și 1% ca în notițe, marcate ❓.",
          raspuns="Prag **100.000 EUR** venituri totale, din 2026 (era 250.000 în 2025 și 500.000 până în 2024). Cotă unică **1%** — cota de 3% pentru firmele fără salariat a fost **eliminată** de la 1 ianuarie 2026. Echivalentul în lei se determină la cursul de la închiderea exercițiului financiar anterior.",
          temei="Cod fiscal, Titlul IV — Impozitul pe veniturile microîntreprinderilor.",
          verificat="21.08.2026"),
    ]),

    ("Decontul de TVA și fișa de rol", [
        q("training 21.08.2026, punctul 5",
          "Ce rânduri din D300 sunt preluate în fișa de rol: 36 și 37, sau 44 și 45?",
          "Notițele afirmă amândouă variantele, în două locuri diferite. Numerele de "
          "rând se schimbă între versiunile formularului, deci una dintre ele e dintr-o "
          "versiune anterioară.",
          "Corelația decont ↔ fișă de rol ↔ balanță. Fără numerele corecte, corelația "
          "nu se poate scrie ca formulă, ci doar descrie.",
          "Am scris corelația pe SOLD, care nu depinde de numerotarea rândurilor, și am "
          "marcat rândurile ca deschise."),

        q("training 21.08.2026, punctul 6",
          "La declarațiile care admit rectificare, contează ordinea cronologică a "
          "înregistrării facturilor la redepunere?",
          "Întrebarea era notată ca presupunere: dacă facturile nu sunt înregistrate "
          "cronologic, poate că redepunerea nu mai e posibilă și ar trebui altă metodă "
          "de corecție.",
          "Procedura de corecție după depunere, pe toate declarațiile care admit "
          "rectificativă. Decontul de TVA nu admite, deci acolo întrebarea nu se pune — "
          "dar la celelalte, da.",
          "N-am implementat nimic pe presupunerea asta."),

        q("training 21.08.2026, punctul 7",
          "Care sunt corelațiile complete între D300 și fișa de rol la TVA?",
          "Temă lăsată explicit la training. Notițele dau două fragmente: fișa preia "
          "rulajul lunii, nu soldul; și ANAF încarcă doar suma lunii, de unde greșeala "
          "de a omite TVA-ul neachitat din perioadele precedente.",
          "Corelațiile de control pe TVA. Ce avem acum se verifică pe sold; corelația pe "
          "rulaj, rând cu rând, are nevoie de structura exactă a fișei de rol.",
          "Am scris corelația pe sold și am lăsat-o pe cea pe rulaj ca gol declarat — "
          "n-am fișă de rol de citit."),
    ]),
]

TOTAL = sum(len(qs) for _, qs in TEME)


# ---------------------------------------------------------------------------
# Legătura întrebare → document
#
# Poarta 19 o folosește în ambele sensuri: un document pe care o întrebare îl privește
# trebuie să poarte marcajul ❓, iar un ❓ într-un document fără întrebări deschise nu
# are ce semnala.
# ---------------------------------------------------------------------------

#: dată din `sursa` → cheia documentului. Trainingurile cu document propriu.
ZI_DOCUMENT = {
    "07.08.2026": "doc:capitaluri",
    "12.08.2026": "doc:imobilizari",
    "14.08.2026": "doc:stocuri-tva",
}

#: Excepțiile: sursa din 19.08 s-a împărțit la patru documente, deci data nu mai spune
#: nimic despre destinație. Fiecare punct își numește documentul.
DOC_EXPLICIT = {
    "training 19.08.2026, punctul 1": "doc:control",     # plafoanele de numerar
    "training 19.08.2026, punctul 2": "doc:control",     # restricțiile pe 455
    "training 19.08.2026, punctul 3": "doc:control",     # simularea încasării în plus
    "training 19.08.2026, punctul 4": "doc:stocuri-tva",  # analiticele pe 4428
    "training 19.08.2026, punctul 5": "doc:stocuri-tva",  # 408 vs. 404 la imobilizări
    # 21.08 se împarte la fel: salariile la documentul nou, impozitarea rezultatului la
    # capitaluri, decontul la stocuri-TVA.
    "training 21.08.2026, punctul 1": "doc:salarii",      # salariul minim
    "training 21.08.2026, punctul 2": "doc:capitaluri",   # pragul micro
    "training 21.08.2026, punctul 3": "doc:salarii",      # rețineri pe medicale
    "training 21.08.2026, punctul 4": "doc:salarii",      # limita popririi
    "training 21.08.2026, punctul 5": "doc:stocuri-tva",  # rândurile D300
    "training 21.08.2026, punctul 6": "doc:stocuri-tva",  # ordinea la redepunere
    "training 21.08.2026, punctul 7": "doc:stocuri-tva",  # corelațiile D300 ↔ fișă rol
}


def documentul(intrebare):
    """Cheia documentului pe care îl privește întrebarea, sau None."""
    sursa = intrebare["sursa"]
    if sursa in DOC_EXPLICIT:
        return DOC_EXPLICIT[sursa]
    import re
    m = re.search(r"(\d\d\.\d\d\.\d{4})", sursa)
    return ZI_DOCUMENT.get(m.group(1)) if m else None


def toate():
    """[(temă, întrebare)] — plate, în ordinea din fișier."""
    return [(tema, q) for tema, qs in TEME for q in qs]


def deschise():
    """Ce se trimite formatorului: fără răspuns verificat."""
    return [(t, q) for t, q in toate() if not q["raspuns"]]


def verificate():
    """Ce am rezolvat singur, cu temei — formatorul confirmă sau infirmă."""
    return [(t, q) for t, q in toate() if q["raspuns"]]


def decizii():
    """Alegeri de cabinet. Rămân deschise, dar nu pentru că n-am căutat."""
    return [(t, q) for t, q in toate() if q["decizie"] and not q["raspuns"]]


# Fără temei nu există răspuns — verificat la import, ca titlurile repetate din
# `date/repartizare.py`. O regulă care se verifică singură nu se poate uita.
_fara_temei = [q["sursa"] for _, q in toate() if q["raspuns"] and not q["temei"]]
if _fara_temei:
    raise SystemExit(f"date/intrebari.py: răspuns fără temei legal — {_fara_temei}")
