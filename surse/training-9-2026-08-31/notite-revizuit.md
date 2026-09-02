# Declarații, fișa pe plătitor și bilanțul — notițe training 31.08.2026

*Versiune revizuită. Sursa: notițele brute din 31.08.2026.*

## 0. Ce e deja în sistem

Primul pas al revizuirii, înaintea oricărei linii de material nou: fiecare temă din
notițe se pune lângă fluxul, modulul sau corelația care o acoperă deja. Ce rămâne e
material nou; restul e **adâncire**, și se scrie ca adâncire — cu trimitere la ce
adâncește.

| Tema din notițe | Ce o acoperă deja |
|---|---|
| Reduceri comerciale `609 / 709` | F-409 |
| `711` ca venit al producției stocate | F-311, F-314 — și scutirea de cadență din `date/inchideri.py` |
| Închiderea exercițiului `121 / 129 / 117 + 691` | F-104, MOD_INCHIDERE_EX |
| Repartizarea rezultatului → `1171` | F-103 |
| Dividende din rezultatul reportat | F-109, F-110, MOD_DIVIDENDE |
| Închiderea lunară a obligațiilor salariale | F-422, MOD_INCHIDERE_LUNARA |
| Fișa pe plătitor confruntată cu balanța | MOD_CONTROL_BALANTA, C-29 |
| Amortizare liniară; plafonul auto de 50% | F-204, F-108, MOD_IMOBILIZARI, MOD_LEASING_FIN |
| Amortizarea accelerată vs. profitul reinvestit | întrebarea 12.08 î2 — **deja cu răspuns verificat** |
| Pragul fiscal de 5.000 lei al mijloacelor fixe | întrebarea 12.08 î1 — **deja cu răspuns verificat** |
| SAF-T pe mijloace fixe (D406) | MOD_IMOBILIZARI |
| Taxare inversă internă / intracomunitară | F-402, F-303, MOD_TAXARE_INVERSA |
| Codurile din nomenclatorul D394 | F-203 |
| Piese de schimb `3024`, valorificate din casare | F-212 (`3024 → 371`) |
| Scutirea de impozit pentru handicap accentuat | **limitare DECLARATĂ** în MOD_SALARII, tabelul C |
| Corecție după D300 depusă | F-407 |
| Debitori diverși `461` | F-425 |
| Sold contrar naturii contului | C-23 |
| Bon de consum la ieșirea din gestiune | F-321, §9.5 din sursa 28.08 |

⚠️ Rândul cu **scutirea pentru handicap accentuat** e cel care justifică tabelul. MOD_SALARII
o declară explicit ca limitare — „Scutiri (handicap, studenți): regim special, pe document
justificativ” — deci nu e material nou, e o limitare cunoscută care acum primește conținut.
Ce e nou e **cealaltă** față a subiectului: fondul de handicap datorat de angajator, care
n-are nicio legătură cu scutirea salariatului în afară de cuvânt.

➕ Ce rămâne **cu adevărat nou** după tabel: fondul de handicap (`635 = 447`), chiriile de la
persoane fizice (`462`), vocabularul balanței (sold inițial / rulaje / total sume), impozitul
pe profit calculat **cumulat**, plafonul de 1.500 lei la amortizarea autoturismelor, structura
bilanțului (F10/F20/F30/F40), regimul de redepunere pe fiecare declarație, extrasele
înregistrate necronologic, `622` / `628`, locuința de serviciu și codul fiscal al salariatului
de la punctul de lucru.

## 1. Clasele 6 și 7 se verifică în fiecare lună

### 1.1 De ce tocmai ele

Formatorul le pune primele: **ridică cel mai des întrebări**. Motivul e structural — clasele
6 și 7 nu au sold care să se reporteze, deci o eroare acolo nu se autodenunță luna următoare
printr-un sold ciudat. Se vede doar dacă te uiți la rulaj în luna în care s-a produs.

### 1.2 Reducerile care se citesc invers

| Cont | Perechea | Ce e |
|---|---|---|
| `609` Reduceri comerciale primite | cu `401` | cheltuială cu semn **inversat** |
| `709` Reduceri comerciale acordate | cu `411` | venit cu semn **inversat** |

`609` stă în clasa 6, dar economic e un **venit**: reduce cheltuiala. De aceea rulajul lui
normal e **creditor**, iar dacă apare „cu +” — adică debitor, ca o cheltuială obișnuită — e
semn de operare greșită.

➕ Instrumentul de verificat, numit în notiță: **fișa de cont / cartea mare**. Nu balanța:
balanța dă soldul net, care poate ascunde un rulaj pe sensul greșit compensat de altul pe
sensul bun. Fișa arată fiecare mișcare cu sensul ei.

↳ adâncește F-409, care are deja monografia celor două conturi.

### 1.3 `711` — singurul venit care se închide prin sold

Regula, cuvânt cu cuvânt din notiță: **`711` e singurul venit care se închide prin sold, nu
prin rulaje; restul se închid prin rulaje.**

Motivul: `711` „Venituri aferente costurilor stocurilor de produse” e un **cont intermediar
de venituri**, care oglindește variația stocului de produse. În cursul anului se mișcă în
ambele sensuri — crește când producția intră în stoc, scade când iese — iar ce contează la
închidere e **variația netă**, adică soldul. Închiderea pe rulaje ar dubla mișcarea.

↳ e chiar motivul pentru care `711` figurează în `FARA_CADENTA`: „Se închide la 31.12
împreună cu variația stocurilor (F-314). Sold în cursul anului e starea normală, nu o eroare.”
Notița de acum confirmă regula scrisă acolo cu un training în urmă.

## 2. Vocabularul balanței

### 2.1 Cele cinci mărimi

Material nou, și e fundația pe care stă orice verificare de balanță:

| Mărimea | Definiția |
|---|---|
| **Sold inițial** | tot timpul la **începutul anului** — nu al lunii |
| **Rulaje** | mișcările **din luna** curentă |
| **Total sume** | sold inițial + rulaje |
| **Total sume precedente** | sold inițial + rulajele până la începutul lunii curente |
| **Sold** | diferența dintre totalurile de sume — **întotdeauna** |

➕ Precizarea care lipsea și care e sursa celor mai multe confuzii: soldul **nu** se citește
din rulaje, ci din totalurile de sume. Un cont poate avea rulaj pe ambele sensuri într-o lună
și totuși sold neschimbat; și invers, poate avea sold fără niciun rulaj în luna curentă.

### 2.2 Exemplul din notițe, verificat

Notița dă un exemplu pe `121`. Îl reiau cu cifrele ei:

- sold inițial: `121` creditor **10.000**
- rulaj ianuarie: debitor **7.000**, creditor **5.000**
- total sume: debitor **7.000**, creditor **15.000**
- sold: creditor **8.000**

Verificarea: creditor `10.000 + 5.000 = 15.000`; debitor `0 + 7.000 = 7.000`; soldul
`15.000 − 7.000 = 8.000` creditor.

⚠️ Notița scrie, pe rândul de mijloc, „pe rulaje la 121 Dr 2k”. Cifra e corectă ca **diferență
de rulaje** (`7.000 − 5.000 = 2.000` debitor), dar nu e soldul; e mișcarea netă a lunii.
Soldul rămâne 8.000 creditor. Confuzia dintre „diferența rulajelor” și „sold” e exact ce
previne tabelul de la §2.1.

## 3. Impozitul pe profit și D101

### 3.1 Se calculează cumulat, nu pe trimestru

Capcana, descrisă în notiță: profit în trimestrul 1, pierdere în trimestrul 2 — declari 0 —
iar în trimestrul 3 **impozitul se calculează cumulat de la începutul anului**, nu pe
trimestrul izolat. Cine declară trimestru cu trimestru, ca și cum ar fi exerciții separate,
ajunge la altă sumă.

➕ De aceea `691` poate avea rulaj în **ambele sensuri**: regularizarea cumulată poate cere o
diminuare a cheltuielii cu impozitul înregistrate anterior.

### 3.2 Soldul din D101 trebuie să iasă cu `441`

Regula de contraverificare, luată ca atare: **tot timpul soldul din D101 trebuie să iasă cu
`441`.** Dacă nu iese, declarația e greșită, nu balanța.

➕ Practica numită de formator: **listat din fișa pe plătitor, caseta de impozit pe profit** —
ca să nu te încurci în ce ai declarat. Fișa pe plătitor e adevărul ANAF; balanța e adevărul
tău; corelația dintre ele e singura care prinde divergența.

↳ e aceeași mecanică pe care MOD_CONTROL_BALANTA o aplică la TVA și la salarii. Impozitul pe
profit e a treia instanță a aceleiași reguli.

### 3.3 `1171` are nevoie de analitic

**Material nou, cu motiv fiscal:** `1171` trebuie ținut pe analitic ca să știi **cât poți să
compensezi**. Pierderea fiscală se recuperează pe ani, în ordine, cu termen limită — iar dacă
toate exercițiile stau grămadă într-un singur sold, nu mai poți spune ce parte din el mai e
recuperabilă și ce parte s-a prescris.

### 3.4 Pierderea nedeductibilă

La D101, dacă rezultatul e pierdere, **trebuie calculată partea nedeductibilă fiscal**.
Pierderea contabilă și cea fiscală nu sunt același lucru: cheltuielile nedeductibile se adaugă
înapoi, iar ce rămâne recuperabil e pierderea **fiscală**.

## 4. Amortizarea contabilă față de cea fiscală

### 4.1 Se țin separat

Regula: amortizarea fiscală se face **conform catalogului**; cea contabilă poate diferi.
Trebuie ținute **separat, inclusiv în Excel**, pentru că — spune notița — sistemele contabile
rareori le țin pe amândouă în paralel.

### 4.2 Plafonul de 1.500 lei la autoturisme

**Material nou.** Pentru autoturismele a căror amortizare depășește 1.500 lei pe lună, statul
lasă amortizarea **contabilă** să meargă conform catalogului, dar recunoaște **fiscal** doar
1.500 lei pe lună. Diferența e cheltuială nedeductibilă și se urmărește ca atare la D101.

Temeiul: **Codul fiscal, art. 28 alin. (14)** — pentru vehiculele de transport persoane cu cel
mult **9 locuri** (categoria M1), amortizarea e deductibilă în limita a 1.500 lei/lună, pe
fiecare vehicul.

↳ e a doua limitare pe autoturisme din sistem, lângă deductibilitatea de 50% de la F-108. Sunt
reguli diferite, care se aplică simultan și se confundă des: 50% privește **TVA și
cheltuielile de exploatare**, plafonul de 1.500 lei privește **amortizarea**.

➕ Nuanța care decide corect cazurile de graniță: folosirea **exclusivă** în activitatea economică
ridică limitarea de 50% de pe cheltuielile de exploatare, dar **nu** ridică plafonul de 1.500 lei
de pe amortizare. Plafonul se aplică oricărui vehicul M1, indiferent cât de mult e folosit în
firmă. Excepțiile sunt pe **destinație** — taxi, transport de persoane cu plată, curierat, agenți
de vânzări, școli de șoferi, intervenție și pază — nu pe intensitatea utilizării.

### 4.3 Amortizarea accelerată

Recomandarea formatorului, pentru **utilaje**: amortizare accelerată — jumătate din valoare în
primul an, restul eșalonat pe durata rămasă, exact cât e fiscal. Se aplică atunci când clientul
cere o amortizare contabilă diferită de cea fiscală.

⚠️ Regula care nu trebuie ratată: **o metodă de amortizare, o dată implementată, rămâne așa pe
toată durata de viață a mijlocului fix.** Nu se schimbă în mijlocul drumului pentru că într-un
an ar fi mai convenabil altfel.

↳ atenție la interacțiunea deja documentată: cine aplică scutirea pentru profit reinvestit **nu**
poate opta pentru accelerată pe acele active, cu excepția din 2026 pentru subgrupa 2.1 și pentru
calculatoare. Vezi răspunsul verificat la întrebarea 12.08 î2.

## 5. SAF-T

### 5.1 Ce se depune și când

| SAF-T | Când |
|---|---|
| Balanță, furnizori, clienți, plăți | **lunar / trimestrial**, după vector |
| Mijloace fixe | **o dată pe an, cu depunerea bilanțului** |
| Stocuri | **doar la cererea organelor de control** |

➕ Situația mijloacelor fixe se depune ca **SAF-T separat**, la sfârșit de an, odată cu bilanțul —
nu în declarația lunară.

### 5.2 Stocurile și evidența primară

SAF-T pentru stocuri include **materiile prime**, iar întrebarea practică e la ce preț se ține
gestiunea: **cu ridicata sau cu amănuntul**.

Dacă `301` se operează „la grămadă” în loc de bucată cu bucată, evidența primară trebuie cerută
de la cine o ține, iar la stocuri trebuie atașat SAF-T-ul de stocuri. Notița semnalează că
SmartBill și SAGA au dezvoltat partea de gestiune tocmai pentru asta.

### 5.3 Consumabilele nu ocolesc gestiunea

⚠️ Eroarea numită explicit de formator, cu trei motive: **`6024 = 401` și `6028 = 401` nu sunt
corecte** — nici din punctul de vedere al corelațiilor, nici al auditului, nici al
contabilității.

Traseul corect trece prin gestiune, chiar când consumul e imediat:

```
3024 = 401     piese de schimb intrate în gestiune
6024 = 3024    consumul, pe bon de consum
```

`3024` și `3028` sunt conturi de stoc „cu posibilitate de consum imediat” — dar *posibilitatea*
consumului imediat nu desființează intrarea în gestiune. Fără ea nu există bon de consum, deci
nu există document justificativ pentru cheltuială.

↳ e aceeași regulă ca la §9.5 din sursa 28.08 („orice ieșire din gestiune se face pe bon de
consum”) și ca la F-321, unde marfa devenită materie primă trece tot prin gestiune.

## 6. Fondul de handicap

**Material integral nou.**

### 6.1 Când se datorează

Din momentul în care societatea are **peste 50 de angajați ca număr mediu**. Formatorul spune
că formula legală e greoaie și dă una simplă, cu abatere neglijabilă.

Temeiul: **Legea 448/2006, art. 78** — angajatorii cu **cel puțin 50 de angajați** au obligația
de a angaja persoane cu handicap în proporție de **cel puțin 4%** din numărul total de angajați.

### 6.2 Numărul mediu de angajați — metoda

Se însumează **orele lucrate** și se împart la norma lunii:

- 5 angajați × 20 zile × 8 h = **800** ore
- 2 angajați × 20 zile × 4 h = **160** ore
- total = **960** ore
- norma lunii = 20 zile × 8 h = **160** ore
- `960 / 160` = **6** angajați medii

Rezultatul e 6, nu 7 — și asta e toată ideea: doi oameni cu normă de 4 ore fac un singur
angajat mediu, nu doi.

⚠️ Notița scrie norma lunii ca „(20 zile × 8h) = 180 ore”. **`20 × 8 = 160`, nu 180.** Cifra
180 e o scăpare de scris: cu 180 rezultatul ar fi 5,33, nu 6. Restul exemplului confirmă că
norma folosită efectiv a fost 160.

➕ Ce intră în orele lucrate, din enumerarea formatorului: orele **lucrate** (nu lucrătoare),
fără concedii, **plus** liberul plătit prevăzut de Codul muncii (căsătorie 5 zile, deces 3 zile
etc.) **plus** orele suplimentare. Sursa e pontajul.

### 6.3 Cota și calculul obligației

⚠️ Aici notița rulează două exemple ca și cum ar fi unul singur. Numărul mediu calculat mai sus
e 6, dar pasul următor înmulțește cu 4% și obține 2,4 — ceea ce cere un număr mediu de **60**,
nu 6. Le separ, pentru că un exemplu cu 6 angajați n-ar declanșa oricum obligația: pragul e 50.

Exemplul coerent, cu media de **60** de angajați:

- locuri rezervate: `4% × 60` = **2,4**
- se scade cel cu handicap **accentuat** deja angajat: `2,4 − 1` = **1,4**
- obligația: `1,4 × 4.325` = **6.055** lei

✅ Salariul minim de **4.325** lei folosit de formator e cel corect **la data trainingului**:
a crescut de la 4.050 la 4.325 începând cu **1 iulie 2026**. Cifra e însă un **parametru**, nu o
constantă — se schimbă cel puțin anual, iar obligația se recalculează la fiecare modificare.
Cine reia exemplul peste un an trebuie să înlocuiască întâi salariul minim, apoi să recalculeze.

Distincția care contează:

| Gradul de handicap | Efectul |
|---|---|
| **Accentuat** | salariatul **nu plătește impozit pe salarii**; ocupă un loc rezervat |
| **Ușor / mediu** | intră la fondul de handicap, fără scutirea de impozit |

### 6.4 Înregistrarea și declararea

```
635 = 447    6.055
```

Se declară în **D100, rândul 810**. Nu e obligatoriu să treacă prin D700 și **nu apare pe
vector**.

### 6.5 Reducerea prin achiziții de la unități protejate

Varianta pe care formatorul o recomandă de explorat: contract cu o societate **acreditată**,
de la care se fac achiziții direct pe `401`, se scad din `447`, și se declară doar diferența.

⚠️ Plafonul: **nu se poate depăși 50%** din valoarea obligației. Restul se plătește oricum.

✅ Temeiul confirmă și structura, și plafonul: **Legea 448/2006, art. 78** dă angajatorului care
nu ocupă cota de 4% două variante — (a) plata integrală a **salariului de bază minim brut pe
țară × numărul de locuri de muncă neocupate**, sau (b) plata a **cel puțin 50%** din această
sumă la bugetul de stat, diferența fiind folosită pentru **achiziția de produse sau servicii
de la unități protejate autorizate**. Varianta (b) e exact ce descrie notița, iar „maximum 50%”
e reversul lui „cel puțin 50% la buget”.

## 7. Chiriile de la persoane fizice

**Material nou.** Societatea plătește chirie către o persoană fizică, iar cheltuiala e a ei.

### 7.1 Câți proprietari are contractul

De sesizat **pe contract**: câți proprietari sunt. Soț și soție înseamnă **două** persoane, iar
în contabilitate trebuie înregistrat **CNP-ul fiecăruia** — pentru că D205 se depune anul viitor
pe CNP, iar informația nu se mai poate reconstitui atunci.

### 7.2 Impozitul

⚠️ Notița dă două variante de calcul, ca și cum ar fi echivalente:

> valoarea din brut (10.000) − 40%, × 10% — **sau** — valoarea din brut (10.000) × 8%

Cele două **nu** dau același rezultat: prima dă 600, a doua dă 800. Cota forfetară de cheltuieli
la cedarea folosinței bunurilor este **20%**, nu 40%, iar cu ea cele două variante coincid:

- `10.000 − 20%` = 8.000 venit net; `8.000 × 10%` = **800**
- scurtătura: `10.000 × 8%` = **800**

Tocmai de aceea circulă „8%”: e produsul `80% × 10%`. Cota de 40% e cea **veche**, dinaintea
reducerii la 20%; cu ea, scurtătura de 8% n-ar mai fi validă.

✅ Temeiul: **Codul fiscal, art. 84** — venitul net din cedarea folosinței bunurilor se stabilește
scăzând din venitul brut o cotă forfetară de cheltuieli de **20%**, iar impozitul de **10%** se
reține **la sursă** de plătitorul de venit, la momentul plății, și este **final**. Coerența internă
a notiței a fost cea care a dat semnalul: două variante prezentate ca echivalente care nu dădeau
același număr.

### 7.3 Obligația se urmărește lunar

Regula, cu accentul formatorului: **te interesează, lună de lună, obligația de plată — nu când
se plătește.** Consecința practică: fișă **pe analitic la `462`**, din care se vede ce s-a
plătit și care e soldul.

↳ `462` era până acum un **gol declarat** în disciplina de închidere: „Nu există flux pe
debitori/creditori diverși”. Chiriile de la persoane fizice sunt exact cazul care îl umple.

### 7.4 Declarațiile

| Declarația | Ce |
|---|---|
| **D100** | codul **628** — impozitul pe chiria plătită persoanei fizice |
| **D205** | informativă, pe CNP, se depune **în ultima zi a lui februarie** |
| **D394** | cod **34** la chirii, cod **35** la prestări servicii |

⚠️ Fără codurile 34/35 atașate, **D394 nu se validează** — e refuz la depunere, nu eroare
descoperită târziu. Regula privește tot ce înseamnă achiziții de la persoane **neplătitoare
de TVA**.

➕ Procedura pentru D205, ca să nu ajungi la rectificativă: **scoți din fișa pe plătitor ce ai
declarat în D100** și compari, pentru că D205 se confruntă cu D100 — la dividende, la impozitul
pe venituri din alte surse și la chirii — chiar dacă D205 e doar informativă.

❓ Notița spune „207 = dividende pentru persoane juridice + impozitul pentru nerezidenți”, cu
mențiunea formatorului „{de contraverificat}”. O las marcată: D207 e declarația informativă
pentru **beneficiari nerezidenți**, iar partea cu dividendele către persoane juridice rezidente
pare să aparțină altui formular.

## 8. Două conturi de cheltuieli care se încurcă

| Cont | Ce ține, din notiță |
|---|---|
| `622` | comisioane acordate **nerezidenților**; comisioanele agenților de vânzări cu PFA |
| `628` | **onorariile de notar** |

➕ Nuanța: `622` se cheamă „Cheltuieli privind comisioanele și onorariile”, deci ar părea că
onorariul de notar îi aparține. Practica pe care o dă formatorul îl trimite la `628` — „alte
cheltuieli cu serviciile executate de terți”. Distincția utilă e **cine prestează**: comision
de intermediere pe `622`, taxă notarială pe `628`.

## 9. Taxarea inversă — completările din notiță

### 9.1 Când factura vine din afară cu TVA străin

Situațiile numite: când produsul **pleacă din România**, sau când **nu s-a dat codul de TVA cu
prefix RO**.

Primul lucru de cerut: **AWB / CMR** — documentul de transport care arată că marfa chiar a
plecat din Ungaria și a ajuns în România.

⚠️ Regula care se ratează cel mai des: dacă livrarea e **din România în România**, chiar dacă
furnizorul e o firmă din afara țării, operațiunea se pune pe **scutită** — nu pe taxare inversă.
Criteriul e traseul fizic al bunului, nu naționalitatea furnizorului.

### 9.2 Facturile fără trasabilitate

Procedura, luată ca atare: când ai un document care „nu te duce nicăieri”, o iei **din aproape
în aproape**. La valori mari, discuțiile se poartă **în scris** (mail / WhatsApp) — un cabinet
de contabilitate nu își poate asuma singur o trasabilitate pe care n-o poate proba.

➕ Singurele care **nu se vămuiesc** sunt **serviciile** (coduri de acces etc.); în rest,
bunurile din afara UE se vămuiesc.

## 10. Extrasele bancare înregistrate cu întârziere

**Material nou**, și e o procedură, nu o regulă contabilă.

Dacă extrasele sunt **din anul curent**: se înregistrează **necronologic** — nu ne mai întoarcem
la lunile respective — și rămân **deductibile fiscal**, pentru că nu țin de ani trecuți.

Ce se face în plus, după caz:

- informații vechi de câteva luni, cu **dobânzi mari**, care au produs un impozit pe venit
  eronat: rămâne la latitudinea cabinetului; minimul e să **menționezi în descriere** la ce dată
  se referă („înregistrat pe 01.08, dar era din 15.06”);
- **cheltuieli mari**: se depun rectificative pentru **D394** și **D406**; dacă firma e la **TVA
  la încasare**, se schimbă și TVA-ul.

**Sumar, cuvânt cu cuvânt:** le înregistrezi necronologic, dar să ai informația în descriere.

## 11. Bilanțul

### 11.1 Structura pe formulare

| Formular | Ce preia |
|---|---|
| **F10** | partea de **solduri**, la decembrie |
| **F20** | **cheltuieli și venituri**, `121` |
| **F30** | **numărul de salariați** |
| **F40** | corelațiile de imobilizări, cu F10 |

Corelațiile numite: în **F10**, imobilizările se corelează cu **F40**, iar **activul net =
capitalurile proprii**.

⚠️ „Active − pasive” din notiță nu e egalitatea clasică de bilanț, ci **activul net**, care se
confruntă cu capitalurile proprii. E o corelație de control, nu identitatea contabilă.

### 11.2 Condițiile de pornire

- până la bilanț trebuie să avem **balanța întocmită**;
- dacă avem conturi cu **soldurile pe invers**, nu generăm bilanțul deloc.

↳ a doua condiție e chiar C-23 (sold contrar naturii contului), promovată de la verificare de
lună la **condiție de poartă** pentru bilanț.

### 11.3 Nu există bilanț rectificativ

Regula, tranșant: **nu există bilanț rectificativ.** Consecințele:

- toate modificările făcute în balanță care nu se mai potrivesc cu bilanțul depus **se explică
  în notele bilanțului următor** — asta spune legea;
- singurele lucruri la care se poate interveni sunt **adresa, codul CAEN și numărul de angajați**,
  și sunt informative;
- ⚠️ dacă modificăm balanța după depunere, apare o problemă **la bănci**: la o cerere de credit
  ei confruntă bilanțul cu balanța.

Corelațiile de bilanț le dă softul; ce rămâne în sarcina ta e să fii sigur că ai **activul pe
debit și pasivul pe credit**.

➕ Când bilanțul se face **direct la ANAF**, aplicația te anunță de neconcordanțe. Dacă îl rulezi
din soft, corelațiile trebuie verificate de tine.

### 11.4 Formularul unic

Se urcă „în pliculeț”, cu formularul de contact, pe **SPV**: adresa, codul CAEN și numărul de
salariați.

## 12. Redepunerea declarațiilor

**Material nou**, și e cel mai practic tabel din notițe: fiecare declarație are alt mecanism de
corectare.

| Declarația | Cum se corectează |
|---|---|
| **D100** | bifă de rectificativă; prin **D710** — pui ce ai pus greșit inițial, apoi suma corectă |
| **D101** | bifă de rectificativă |
| **D112** | bifă de rectificativă |
| **D390** | bifă de rectificativă — mai ales pentru sume; un cod de TVA greșit e prins de validare și nu se preia |
| **D205 / D207 / D107** | bifă de rectificativă |
| **D300** | **nu are bifă** — se face **decont de corecții materiale**, manual, prin formularul de contact, cu toate anexele și cu motivul |
| **D394** | **nu are bifă** — se depune **peste** declarația inițială |
| **D406** | **nu are bifă** — se depune **peste** declarația inițială |

### 12.1 Decontul de corecții materiale

Detaliul care contează la D300: decontul de corecții încarcă **doar partea de rulaje din lună**.
Dacă o factură nu a fost înregistrată cronologic, o înregistrezi și vii pe **regularizări luna
viitoare**.

➕ Atenție la `4424` preluat greșit din decontul trecut: sistemul trimite o **atentionare**, nu o
eroare. E o distincție care schimbă reacția — atenționarea nu blochează depunerea.

### 12.2 Unde te uiți când corectezi

Regula scurtă: **la rectificativă te uiți în declarație, nu în balanță.** Declarația depusă e
faptul care se corectează; balanța e doar sursa cifrei corecte.

## 13. Reevaluările făcute cu întârziere

Exemplul din notiță: dacă nu ai făcut reevaluările în februarie și ai depus D100 în martie, faci
reevaluările în **aprilie / luna curentă deschisă** și depui D100 corect în **trimestrul
următor**. Nu se redeschide luna închisă.

## 14. Două chestiuni de personal

### 14.1 Codul fiscal al salariatului de la punctul de lucru

**Material nou.** Dacă ai punct de lucru și ai salariat acolo, trebuie **cerut cod fiscal pentru
acel salariat**. Se aplică și la **sectoare**, pentru că sunt primării diferite: raportarea se
face la primăria de care ține punctul de lucru.

### 14.2 Locuința de serviciu

Societățile pot acorda **locuință de serviciu** salariaților care îndeplinesc condițiile din
Codul fiscal. Deductibilitatea e **20% din salariul minim**, calculată **pe salariat** — nu pe
firmă. Este un **avantaj de natură salarială neimpozabil**, încadrat ca atare în Codul fiscal.

❓ Ultima propoziție a notiței — că în zona de salarii se calculează un avantaj **net**, pentru
care se determină apoi un **brut impozabil** — e marcată de formator „{de contraverificat}”. O
las deschisă: dacă avantajul e neimpozabil, brutarea lui nu se justifică; dacă se depășește
plafonul de 20%, doar **excedentul** ar trebui brutat. Cele două afirmații nu se pot împăca fără
confirmare.

## 15. Handover-ul final

Cele două referințe cu care formatorul închide, ambele de ținut la îndemână:

- **OMFP 1802**, partea a 2-a din secțiunea de contabilitate — **corelațiile la planul de conturi**;
- **catalogul mijloacelor fixe** — pentru încadrarea corectă.

Se predau în ambele forme: **digital și pe hârtie**.
