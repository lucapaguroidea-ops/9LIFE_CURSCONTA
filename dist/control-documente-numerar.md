# Control, documente și numerar
### Surse: training 19.08.2026 · adâncit cu 21.08.2026, 26.08.2026 și 28.08.2026 — cum se citește un cont, ce cere legea de la un document și unde se rupe disciplina de casă

---

## Cum citești acest document

| Marcaj | Semnificație |
|---|---|
| ✅ | Notița originală era corectă — doar reformulată/completată |
| ⚠️ | **Eroare în notița originală** — corectată aici, cu explicație |
| ➕ | Completare (lucru care lipsea, dar era necesar ca raționamentul să stea în picioare) |
| ❓ | Rămas deschis — de clarificat cu formatorul (vezi Anexa D) |

---

## Convenția de notare
*Material de studiu structurat pe baza notițelor de training din 19.08.2026.*

Convenție de notare folosită peste tot în ghid:

> `cont debitor = cont creditor · sumă`

## 1. Cum se citește un cont
Înainte de orice înregistrare, două lucruri fixe, care nu se schimbă niciodată:

- **Debitul este partea stângă** a contului.
- **Creditul este partea dreaptă** a contului.

Restul decurge din natura contului:

| | Cont de **ACTIV** | Cont de **PASIV** |
|---|---|---|
| Ce reprezintă | Ce **deține** societatea (bunuri, creanțe, bani) | Ce **datorează** societatea (datorii, capital) |
| Prima funcțiune | Începe prin a se **debita** | Începe prin a se **credita** |
| Crește | pe **debit** (stânga) | pe **credit** (dreapta) |
| Scade | pe **credit** (dreapta) | pe **debit** (stânga) |
| Sold final | **debitor** | **creditor** |

Exemple: 371 Mărfuri, 4111 Clienți, 5121 Conturi la bănci → **activ**.
401 Furnizori, 419 Clienți-creditori, 4423 TVA de plată → **pasiv**.

**Conturi bifuncționale.** Câteva conturi pot avea, după caz, sold debitor sau creditor: **408**, **418**, **4428**, **473**, **481**. Exact acestea sunt cele care cer atenție și analitice — vezi secțiunile 4 și 5.

**Semnal de eroare:** un cont de activ cu sold creditor (sau invers) înseamnă aproape întotdeauna o înregistrare greșită. Un 4111 cu sold creditor = ai încasat mai mult decât ai facturat (vezi 7.3).

---

## 2. Operațiuni speciale
### 2.1 Prețul din contract fără mențiune de TVA


Când un contract menționează sec o sumă — „100.000 lei", punct, fără nicio precizare — acea sumă se consideră că este **cu tot cu TVA**.

De aceea este esențial ca în contract să se menționeze explicit: prețul **cu sau fără TVA**, și tranșele în care se primesc banii.

Principiul este consacrat de jurisprudența CJUE (cauzele conexate C-249/12 și C-250/12, *Tulică și Plavoșin*).


### 2.2 Încasare mai mare decât factura


Ai emis o factură de 10.000 lei și ai încasat 15.000 lei.

Diferența de 5.000 lei este un **avans**, nu un venit — deci **nu** poate merge pe 472. Merge pe **419**, iar din ea trebuie extras TVA-ul și colectat, chiar dacă banii se returnează partenerului luna următoare.

Suma încasată în plus este TVA-inclusivă:
- baza: 5.000 ÷ 1,21 = **4.132,23**
- TVA: **867,77**

```
4111 = 419    ·   4.132,23
4111 = 4427   ·     867,77
```

Impactul fiscal apare doar când încasarea și restituirea **nu se închid în aceeași lună**. Dacă returnezi banii în aceeași lună, situația se neutralizează.

Practic: soldul lui 4111 poate apărea ca debit cu minus sau ca sold creditor — de aceea se ia **fișa pe plătitor** și se verifică. Trebuie contraverificat **4427**, ca să confirmi că softul chiar a extras TVA-ul pentru tranzacția respectivă.

Legiuitorul nu impune corecții când **tu** plătești în plus, dar impune corecția atunci când **tu încasezi** în plus.


### 2.3 Note despre 455


Contul **455** Sume datorate acționarilor/asociaților are restricții privind operațiunile în numerar: plățile din 455 prin casierie nu mai sunt permise în condițiile anterioare. ❓ Punct de verificat în textul legal în vigoare — vezi Anexa D.

---

## 3. Numerar și plafoane (Legea 70/2015)
Plafoanele reținute la training:

| Tip operațiune | Plafon |
|---|---|
| Între persoane juridice (B2B) | **5.000 lei** |
| Încasări de la persoane fizice (B2C) | **10.000 lei** |
| Între persoane fizice (C2C) | **50.000 lei** |

**Cum se citesc plafoanele — răspuns la întrebarea din notițe:**

- Sunt **plafoane zilnice**, **per persoană** — nu per contract și nu per document izolat. Adică: de la același partener, într-o zi, nu poți încasa în numerar peste plafon, indiferent câte documente emiți.
- Pentru operațiunile între persoane juridice există și un **plafon total zilnic**, peste limita per persoană.
- **Fragmentarea este interzisă expres.** Nu poți sparge o factură de 12.000 lei în trei tranșe de 4.000 lei, nici în aceeași zi, nici pe zile consecutive, dacă scopul este eludarea plafonului. Aceasta este și logica pentru care plafonul e „pe zi": altfel ar fi trivial de ocolit.
- Există și un plafon pentru **soldul casieriei** la sfârșitul zilei.

Restul, peste plafon, se decontează obligatoriu prin bancă.

> Cifrele exacte au fost modificate prin Legea 296/2023. Înainte de a le aplica la un client, confirmă valorile în textul Legii 70/2015 în vigoare la data operațiunii ❓ — vezi Anexa D.

---

## 4. Documente, contracte și riscuri la control
### 4.1 „Prestări servicii conform contract"


Când pe documentul de intrare scrie doar atât, ai o problemă: legea obligă la descrierea **naturii serviciului prestat** (art. 319 Cod fiscal — denumirea și cantitatea bunurilor livrate, denumirea serviciilor prestate).

Prestările de servicii sunt foarte diverse, iar încadrarea contează:
- dacă factura menționează **numărul contractului**, ești norocos — te uiți în contract;
- o factură de 628 de 100.000 lei cere o cu totul altă abordare decât una de 500 lei;
- cazul fericit: servicii de arhitectură / proiectare → nu e cheltuială, e **imobilizare în curs**.


### 4.2 Contractul la prestările de servicii


La prestări de servicii trebuie să existe **contract**. Factura este documentul fiscal; contractul detaliază **cum interacționezi cu partenerul**.

> Nuanță: cerința expresă de a avea contract pentru servicii de management și consultanță, din vechiul Cod fiscal, a fost abrogată. Codul fiscal actual (art. 25 alin. 1) cere ca o cheltuială să fie efectuată **în scopul desfășurării activității economice** și susținută cu documente justificative. Contractul rămâne principalul mijloc de probă la control — deci, practic, indispensabil.


### 4.3 Cazul penalităților — de reținut


O firmă de construcții a avut contract de livrare cu un client. Clientul nu a mai achitat. În contract, la capitolul penalități, erau trecute sume foarte mari — pe care firma nu le-a mai facturat și nu le-a trecut la venituri.

ANAF a constatat că firma **nu și-a respectat propriul contract**, a calculat venituri și majorări pentru soldurile neîncasate, iar firma a rămas și fără venit, și cu bani dați la stat.

**Concluzie:** în contracte se trec **penalități realiste**. O clauză de penalitate exagerată nu te protejează — te expune.


### 4.4 Sistemele informatice


Programele au ecrane cu o structură în spate care generează notele contabile fără ca tu să le vezi. Dacă ceva pare suspect, instrumentul de verificare este **fișa de cont**. Nu te baza pe faptul că softul „știe" — mai ales pe conturile bifuncționale.

---

## 6. Răspunsuri la întrebările din notițe
### 6.1 Ce alte corelații se pot face din balanță


Sunt în secțiunea 5. Tiparul e același de fiecare dată și se poate aplica oricărui cont
nou: **întreabă ce document extern conține aceeași informație**, apoi compară.

| Cont | Documentul care îl confirmă |
|---|---|
| 421 + 423 | statul de plată |
| 444, 4315, 4316, 436 | D112 și fișa de plătitor |
| 427 | adresa de înființare a popririi |
| 4423 / 4424 | decontul de TVA și fișa de rol |
| 4426 / 4427 | jurnalele de cumpărări și vânzări |
| 5121 | extrasul de cont |
| 5311 | registrul de casă |

Un cont fără document extern care să-l confirme e un cont pe care nu îl poți verifica
decât intern — și de aceea conturile de tranzit (473, 581) trebuie să ajungă la zero, nu
verificate: ele n-au corespondent afară.

---

## 7. Conturile care țin rulajele curate
### 7.1 Taxele locale prin 446, nu direct pe cheltuială


```
446 = 5121                  plata taxei
471 = 446                   dacă acoperă o perioadă mai lungă
635 = 471                   eșalonat, pe luni
635 = 446                   direct, dacă suma e mică
```

➕ Rostul lui 446 ca punct de trecere: taxa plătită anticipat pentru un an întreg nu e
cheltuiala lunii în care s-a plătit. Pentru sume mici nu merită mecanismul cu 471.


### 7.2 Contul 4481 — datorii din acte de control


**4481 este cont de pasiv**: dobânzi, penalități și sume stabilite prin acte de control,
inclusiv cele aferente perioadelor anterioare.

Când ANAF vine în control și întocmește o decizie de impunere — să zicem 10.000 lei TVA
suplimentar — suma **nu se înregistrează în 4423**, pentru că ar denatura rulajul curent
și ar produce diferență la decont.

```
6588 = 4481       cheltuială nedeductibilă fiscal
```

❓ **Contradicție de rezolvat cu formatorul.** Notițele din 21.08.2026 spun că sumele din
decizii de impunere se înregistrează „în 4423 cu analitic distinct, tocmai ca să nu ajungă
din greșeală în decontul lunii următoare". Notițele din 26.08.2026 spun exact invers: nu
prin 4423, ci prin 4481, „pentru că denaturează rulajul curent".

Ambele afirmații vin de la același formator, la cinci zile distanță. Am adoptat varianta
din 26.08 pentru că e cea care dă motivul, iar motivul e verificabil: un analitic al lui
4423 rămâne totuși în soldul lui 4423, adică fix contul pe care decontul îl reconciliază.
Dar decizia îi aparține formatorului, nu mie.


### 7.3 Contul 4482 — plăți eronate către buget


**4482 este cont de activ**: ține sumele plătite eronat, până la lămurire.

Exemplu: impozit pe salarii de plată 715 lei, în soldul creditor al lui 444. Din bancă a
ieșit o plată de 751 lei (cifre inversate):

```
444  = 5121       715        cât se datora
4482 = 5121        36        diferența plătită în plus
```

Luna următoare, soldul lui 4482 diminuează plata datorată.

Al doilea caz, frecvent la cei cu mai multe firme: ordinul de plată pleacă din contul
firmei, dar cu **alt CUI de plătitor**. Banii sting datoria altei firme, iar firma plătitoare
rămâne cu datoria neachitată la ANAF. Plata se înregistrează pe 4482 — sold în așteptare,
care se disecă — până când cealaltă firmă returnează sumele.

➕ Rostul ambelor conturi e același: **să nu altereze rulajele conturilor curente**. ANAF
contraverifică exact corelațiile pe care ele le protejează.


### 7.4 Conturile 461 / 462 — coșul firmei


461 și 462 sunt printre primele conturi la care se uită **și ANAF, și băncile**. Sunt și
cele mai ușor de transformat în coș: sume decontate care n-au corespondent prin 401, 419
sau alt cont dedicat ajung acolo și rămân.

⚠️ Cazul concret: nu mai există sold pe 4551, dar asociatul continuă să ia bani din bancă
— iar sumele se pun pe 461. La control apare o creditare de societate inexistentă și bani
scoși fără temei.

**Utilizări corecte:**

Vânzarea unui mijloc fix se face prin 461, nu prin cont de client — cumpărătorul nu e
client pentru activitatea curentă:

```
461 = 7583        venit din active cedate
461 = 4427        TVA colectată
```

Imputația către un salariat care a produs pagube — nu e client, deci nu 4111:

```
461 = 7588        826,45     venit din exploatare
461 = 4427        173,55     TVA colectată
```

pentru o pagubă de 1.000 lei cu TVA (1.000 ÷ 1,21 = 826,45).

⚠️ Notița scria debitul ca `121`. Contul corect este **461**; sumele erau bune.

➕ 7588 se folosește când nu există un cont de venit asociat direct, cum e 707 pentru
marfă. Dacă bunul deteriorat a fost dedus, TVA se colectează.

❓ Imputația nu se poate face fără ca salariatul să fie informat și de acord — Codul
muncii. Notița menționează un plafon „la nivelul a 5 salarii medii", cu observația
formatorului „de verificat suma".

## 8. Verificarea care încheie ședința
Regula generală, formulată de formator ca temă: **să verificăm activul și pasivul —
conturile care stau pe invers.** Un cont de activ cu sold creditor sau un cont de pasiv
cu sold debitor nu e o curiozitate de balanță; e o eroare care încă n-a fost căutată.

Conturile din ședința asta care se verifică așa: 455 (niciodată debitor), 461/462, 4482,
463 față de 121.

➕ Tema dată: identificarea în balanță a lucrurilor care pot fi rezolvate — pentru că, o
dată ce li se stabilește cursul, nu mai sunt erori.

## 9. Ce e deja în sistem
Primul pas al revizuirii, înaintea oricărei linii de material nou: fiecare temă din
notițe se pune lângă fluxul, modulul sau corelația care o acoperă deja. Ce rămâne e
material nou; restul e **adâncire**, și se scrie ca adâncire — cu trimitere la ce
adâncește.

| Tema din notițe | Ce o acoperă deja |
|---|---|
| Taxare inversă internă, `4426 = 4427` | F-402, MOD_TAXARE_INVERSA |
| Taxare inversă intracomunitară | F-303, MOD_TAXARE_INVERSA |
| Codul de operațiune din nomenclatorul D394 | **F-203** — cod 27 la clădiri |
| Închiderea lunară de TVA | F-405, MOD_INCHIDERE_TVA |
| Decontul de TVA ↔ soldul din balanță | C-29, MOD_INCHIDERE_LUNARA (blocul V4) |
| Sumă neidentificată din extras → 473 | F-411, MOD_INTERMEDIAR |
| Viramente interne 581 | F-501, MOD_INTERMEDIAR |
| Avansuri de trezorerie 542 | F-502, MOD_DECONT |
| Reevaluarea lunară a valutei | F-107, MOD_CREDIT_VALUTA |
| Obiecte de inventar `603 ↔ 303` + 8035 | F-305, F-802 |
| Reduceri comerciale ulterioare `609 / 709` | F-409 |
| Control analitic ↔ sintetic la imobilizări | F-214, C-15 |
| Sold contrar naturii contului | C-23 |

⚠️ Rândul cu **codul D394** e cel care justifică tot tabelul. La prima revizuire a
notițelor ăstora, mecanismul „fără cod, declarația nu recunoaște operațiunea” a fost
scris ca material nou. Nu era: e pasul revelator al lui F-203, scris cu cinci
traininguri în urmă, cu exemplul codului 27 la clădiri. Duplicarea s-a descoperit abia
la comparația cu o a doua revizuire.

➕ Ce rămâne **cu adevărat nou** după tabel: scontarea (5114, 667), liniile de credit
(5191), dobânzile pe 5186/5187, plafonul de sold al casei, tichetele ca stoc de
trezorerie (5328), perechile clasă 6 ↔ clasă 3, și verificarea analitic ↔ sintetic ca
procedură generală.

## 10. Casa și plafoanele de numerar
### 10.1 Plafonul soldului de casă


Soldul de casă nu poate depăși **50.000 lei la sfârșitul zilei**, pe fiecare punct de
lucru. Ce depășește se depune în cont.

➕ Istoric: soldul **a fost** nelimitat, cu singura cerință ca banii să existe efectiv și
să poată fi arătați la control. Plafonul e o restricție relativ nouă, iar cine lucrează
după obiceiul vechi îl încalcă fără să știe.

❓ **Per societate sau per casierie?** Notițele povestesc un client care, aflând de
plafon, „a mai făcut rost de o casierie cu 50.000 lei” — deci a înțeles că limita e per
casierie. Dacă e așa, orice societate poate multiplica plafonul deschizând puncte de
lucru, ceea ce ar goli restricția de sens. De confirmat cu formatorul care e textul exact
și dacă practica clientului rezistă la control — mai ales pentru un punct de lucru fără
activitate reală de încasări.

❓ **Plafon separat la magazinele mari?** O a doua lectură a acelorași notițe indică un
plafon de **500.000 lei** pentru magazinele de tip cash & carry, supermagazine și
hipermagazine, în locul celui de 50.000. Cifra e plauzibilă — un hipermarket depășește
50.000 lei într-o oră de vârf, iar depunerea zilnică a excedentului ar fi impracticabilă —
dar **nu era în notițele de la curs și n-am putut-o confirma pe textul legii**. Rămâne
întrebare, nu afirmație: dacă se confirmă, C-38 are nevoie de un al doilea prag, după
tipul unității.


### 10.2 Ce plăți sunt plafonate și ce plăți nu


**Fără plafon**, oricât de mare e suma:

- salariile și alte drepturi de personal
- plățile către bugetul statului și alte instituții publice

**Cu plafon:**

| Operațiunea | Plafonul |
|---|---|
| Încasări de la o persoană juridică | 5.000 lei / persoană / zi |
| Plăți către o persoană juridică | 5.000 lei / persoană / zi, **dar maximum 10.000 lei/zi în total** |
| Încasări și plăți față de o persoană fizică | 10.000 lei / persoană / zi |
| Avansuri spre decontare (plăți din 542) | 5.000 lei / persoană |

⚠️ Notița reține doar „5.000 la juridice, 10.000 la fizice”. Direcția e corectă, dar
plafonul pe persoană **nu e singurul**: la plățile către persoane juridice există și un
plafon TOTAL de 10.000 lei pe zi. Cinci furnizori × 5.000 lei într-o zi respectă primul
plafon și îl încalcă pe al doilea.

➕ Plafoanele și interdicțiile complete — inclusiv interdicția totală a operațiunilor în
numerar pe contul 455 — sunt verificate pe surse și consemnate separat. Aici rămâne doar
ce a adăugat trainingul ăsta: plafonul de sold și regula punctelor de lucru.


### 10.3 Plăți fragmentate și contractul cu plata în rate


Fragmentarea unei plăți ca să încapă sub plafon e **interzisă expres**.

Există însă o cale legitimă: **contractul cu plata în rate**. Dacă există contract, cu
scadențar și date fixe, încasarea în tranșe nu mai e fragmentare — e executarea
contractului. Din 20.000 lei se poate încasa de la o persoană fizică toată suma, în ratele
prevăzute.

➕ Condiția nu e formalitatea contractului, ci **respectarea lui**: dacă ratele se încasează
la alte date sau în alte sume decât scrie în scadențar, apărarea cade.

## 11. Verificarea analitic ↔ sintetic
### 11.1 De ce se rupe


Programul te lasă să mai faci o operațiune **după** ce ai dat închiderea de lună. Dacă nu
te întorci să refaci închiderea, apare o diferență între analitic și sintetic — care nu se
anunță singură.


### 11.2 Conturile la care se rupe cel mai des


**Banca.** Extrasul de cont trebuie să se potrivească cu balanța. Cazul tipic: jurnalul de
bancă dă cu extrasul, dar nu dă cu balanța — semn că diferența e între analitic și
sintetic, nu în operare.

**Clienții și furnizorii.** Nu se lasă solduri nealocate pe 4111 sau 401: denaturează și
fișa partenerului, și corelația analitic ↔ sintetic.

➕ Regula formatorului, repetată: **niciodată nu pleci fără analitic.** Chiar și acolo unde
pare inutil — 446 se ține pe `446.1` de la bun început, nu pe sintetic, pentru că a doua
taxă apare întotdeauna, iar despărțirea retroactivă e mult mai scumpă decât analiticul
făcut din prima.


### 11.3 Sumele nealocate și contul 473


Când o încasare nu se poate aloca înainte de închiderea lunii, se pune în **473**, cu
notiță despre proveniență:

```
473  = 4111       la închiderea lunii, dacă nu se știe alocarea
4111 = 473        luna următoare, la stornare și alocare corectă
```

➕ Importantul nu e contul, e **să fie într-un cont de care să-ți mai amintești**. Nu e o
problemă să stornezi luna viitoare și să pui pe clientul corect. Problema e să ratezi
alocarea cu totul.


### 11.4 Compensările 4091 ↔ 419


Notița cerea analiza. Cazul: același partener e și furnizor, și client. I-ai plătit un
avans (4091) și el ți-a plătit un avans (419). Tentația e să le stingi unul cu altul.

Se poate, dar cu două condiții pe care notița nu le spune:

1. **Compensarea are nevoie de document** — acord scris între părți, nu decizie
   unilaterală. Soldurile sunt față de aceeași persoană, dar din raporturi juridice
   diferite;
2. **TVA-ul nu se compensează odată cu avansurile.** La avansul plătit ai dedus TVA, la
   cel încasat ai colectat. Regularizarea se face la facturile finale, prin stornarea
   fiecărui avans în parte — nu prin compensare.

❓ Ce document folosește cabinetul pentru compensare, și dacă se aplică pragul de la care
compensarea trebuie făcută prin sistemul reglementat — de confirmat.


### 11.5 Preluarea unei balanțe în cursul anului


⚠️ La preluarea unei societăți **în cursul anului** nu se preiau soldurile, ci **totalul
sumelor** debitoare și creditoare.

Motivul: balanța trebuie să aibă **continuitate**. Cu soldurile preluate ca sold inițial,
rulajele anului pornesc de la zero în luna preluării — iar orice verificare care se face pe
rulaj, nu pe sold, devine falsă: corelația cu fișa de rol la TVA, verificarea CAM-ului ca
procent din brut, rulajul creditor al obligațiilor salariale.

➕ Distincția e chiar întrebarea pusă pentru sesiunea următoare:

- **soldul** — diferența, la un moment dat, între ce a intrat și ce a ieșit;
- **rulajul** — mișcarea unei perioade, pe fiecare sens;
- **totalul sumelor** — rulajul CUMULAT de la începutul anului, pe fiecare sens.

Numai al treilea permite reconstituirea anului întreg dintr-o balanță de mijloc de an.


### 11.6 Cele trei verificări din softul formatorului


Formatorul a descris trei „căsuțe care se înverzesc” din programul lui — și ele sunt exact
modelul de verificare pe care îl urmărim:

| Verificarea | Ce compară | Când e verde |
|---|---|---|
| **Decontul de TVA** | 4426 și 4427 din balanță vs. ce se duce în decont | ce se declară = ce e în balanță |
| **Balanța pe furnizor** | analiticul furnizorilor vs. sinteticul lui 401 | analitic = sintetic |
| **Contul 121** | rulajul claselor 6 și 7 vs. 121 | 6 și 7 s-au închis complet în 121 |

A treia se vede cel mai bine la bilanț: dacă 6 și 7 nu s-au închis, cifrele nu se leagă.

➕ Notă legată, din aceeași secțiune: **comisioanele bancare se înregistrează `627 = 5121`**
chiar dacă linia din extras apare la încasări. Contul urmează natura operațiunii, nu poziția
ei în extras.

## 12. Ce s-a cerut pentru sesiunile următoare
**Lista corelațiilor de verificat pe balanță**, cu precizarea formatorului că fiecare
balanță e unică — fiecare firmă are alt obiect de activitate. Se cer: conturile cele mai
comune, cele mai esențiale, și **în ce ordine** se verifică.

**O aplicație care rulează verificările analitic ↔ sintetic pe balanță**, cerută explicit
sub titlul „Later”:

- mijloacele fixe și celelalte corelații de analitic;
- 121 cu clasele 6 și 7;
- TVA.

**Întrebări pentru sesiunea următoare:**

1. La preluarea unei societăți, ce se disecă analitic ↔ sintetic — mai multe exemple decât
   4111 / 401 și 512x;
2. Diferența dintre sold, rulaje și total sume (răspuns propus la §9.5, de confirmat).

---

## Anexa B — Checklist practic

1. **Confuzia 5121 / 5311 / 5112.** 5121 = bancă, 5311 = casa în lei, 5112 = *cecuri de încasat*. Orice plată bancară — inclusiv prin ordin de plată — trece prin **5121**.

2. **Impozitul pe profit calculat pe baza greșită.** Soldul creditor al lui 121 este **baza**, nu impozitul. Impozitul este 16% din el.

3. **Sensul lui 4428.** Debitor la achiziții pe aviz (`4428 = 408`), creditor la livrări pe aviz (`418 = 4428`) și la mărfuri la preț cu amănuntul (`371 = 4428`). Fără analitice, softul le amestecă.

4. **Uitarea pasului `408 = 4428`.** Fără el, ambele conturi rămân umflate reciproc la infinit.

5. **Dublarea gestiunii prin 408.** Factura care nu menționează numărul avizului este cauza clasică. Se verifică împerecherea aviz–factură.

6. **TVA neexigibilă calculată pe bază greșită** la mărfuri: se aplică la **cost + adaos**, nu la cost.

7. **Ajustările pentru deprecierea stocurilor tratate ca deductibile.** Sunt nedeductibile; reluarea lor e neimpozabilă. Nu confunda cu ajustările pentru creanțe.

8. **Uitarea scoaterii din evidență la vânzarea unui mijloc fix.** Facturarea (7583) nu e suficientă — trebuie și `2813 = 213` plus `6583 = 213`.

9. **Diferențe de curs pe avansuri.** Nu se calculează. Stornarea se face la cursul de la data avansului.

10. **Încasarea în plus pusă pe 472.** Nu este venit — este avans (419) și cere colectare de TVA.

11. **Conturi cu sold contrar naturii lor** (401 debitor, 4111 creditor) — aproape întotdeauna semn de eroare sau de avans neînregistrat corect.

12. **473 și 581 cu sold la închidere.** Ambele trebuie golite; un sold acolo ascunde o operațiune neterminată.

13. **Penalități contractuale nerealiste.** Dacă nu le facturezi, ANAF le poate impune ca venit. Vezi 9.3.

---

---

## Anexa D — Rămase deschise

Ce e încă provizoriu în documentul ăsta. Lista nu e scrisă aici: vine din `date/intrebari.py`, aceeași sursă cu foaia „Întrebări deschise” a workbook-ului și cu lista trimisibilă formatorului.

**❓ Programul de contabilitate extrage automat TVA-ul din diferența trecută pe 419 la o încasare mai mare decât factura, sau trebuie forțat manual?**

*Comportamentul softului la încasarea în plus · training 19.08.2026, punctul 3*

Suma încasată în plus e TVA-inclusivă: din 5.000 lei ies 4.132,23 bază și 867,77 TVA. Dacă softul nu face extragerea, TVA-ul rămâne necolectat fără ca nimic să semnaleze.

**Ce am presupus între timp:** Am scris fluxul cu extragerea explicită a TVA-ului, ca pas separat, tocmai ca să nu depindă de comportamentul softului.

**❓ Care e plafonul legal al sumei care se poate imputa unui salariat pentru o pagubă produsă, și în ce ritm se poate reține din salariu?**

*Salarii — praguri și baze de calcul · training 26.08.2026, punctul 1*

Notițele din 26.08 menționează un plafon „la nivelul a 5 salarii medii”, cu observația formatorului însuși: „de verificat suma”. Separat, notițele spun că imputația nu se poate face fără ca salariatul să fie informat și de acord — Codul muncii.

**Ce am presupus între timp:** Am modelat imputația integrală, cu reținere într-o singură lună, pentru că exemplul din notițe e de 1.000 lei — sub orice plafon plauzibil. Pasul poartă ❓. De verificat art. 254 (răspunderea patrimonială) și art. 169 (reținerile din salariu) din Codul muncii.

**❓ Există un plafon de sold de casă separat, de 500.000 lei, pentru magazinele de tip cash & carry, supermagazine și hipermagazine?**

*Trezorerie — diferențe de curs și plafoane · training 28.08.2026, punctul 8*

Nu era în notițele de la curs. O a doua revizuire a acelorași notițe îl afirmă, alături de plafonul general de 50.000 lei.

**Ce am presupus între timp:** Cifra e plauzibilă: un hipermarket trece de 50.000 lei într-o oră de vârf, iar depunerea zilnică a excedentului ar fi impracticabilă. Dar plauzibil nu e verificat, iar eu n-am confirmat-o pe textul legii — deci C-38 a rămas cu un singur prag și cu întrebarea marcată.

**❓ Plafonul de 50.000 lei la soldul de casă e per societate sau per casierie / punct de lucru?**

*Trezorerie — diferențe de curs și plafoane · training 28.08.2026, punctul 2*

Notițele spun „50.000 lei pe fiecare punct de lucru” și povestesc un client care, aflând de plafon, „a mai făcut rost de o casierie cu 50.000 lei”. Notițele nu spun dacă practica aceea rezistă la control.

**Ce am presupus între timp:** Am formulat C-38 pe casierie, cum spun notițele, dar cu semnalul „casierie deschisă special ca să se multiplice plafonul” trecut la SUSPECT — pentru că intenția se vede, indiferent cum e textul. De confirmat art. 4 din Legea 70/2015 în forma în vigoare.

**❓ Ce documentație face diferența, la un control, între „rate contractuale” și fragmentarea unei plăți?**

*Trezorerie — convenții de înregistrare · training 28.08.2026, punctul 6*

Notițele spun că un contract cu plata în rate scoate operațiunea de sub acuzația de fragmentare: „am scadențar, am o dată fixă pe care încasez ratele”. Nu spun ce se prezintă efectiv.

**Ce am presupus între timp:** Am scris în document că apărarea cade dacă ratele se încasează la alte date sau în alte sume decât scadențarul. Ce nu știu e dacă se cere contract cu dată certă, sau dacă e de ajuns unul sub semnătură privată.

**❓ Ce document susține compensarea 4091 ↔ 419 la același partener, și de la ce prag trebuie făcută prin sistemul reglementat?**

*Gestiuni, bonuri de consum și compensări · training 28.08.2026, punctul 4*

Notițele scriu doar „4091 - 419 <=> să faci compensări ulterior”, cu mențiunea „de analizat” adresată mie.

**Ce am presupus între timp:** Analiza e în documentul de control, §9.4: compensarea e posibilă, dar cere acord scris între părți, iar TVA-ul NU se compensează odată cu avansurile — regularizarea lui se face la facturile finale, prin stornarea fiecărui avans în parte. N-am scris flux, pentru că starea inițială depinde de răspuns.

**❓ Sumele stabilite prin decizie de impunere pe TVA se înregistrează în 4423 cu analitic distinct, sau în 4481?**

*Acte de control — 4423 sau 4481 · training 26.08.2026, punctul 3*

Cele două traininguri spun exact invers, la cinci zile distanță. 21.08: „se înregistrează în 4423 cu analitic distinct, tocmai ca să nu ajungă din greșeală în decontul lunii următoare”. 26.08: „nu mă duc prin 4423, pentru că denaturează rulajul curent — și mă duc prin 4481”.

**Ce am presupus între timp:** Am adoptat varianta din 26.08, pentru că e singura care dă un motiv verificabil: un analitic separă EVIDENȚA, dar nu separă SOLDUL, iar decontul se compară pe soldul sintetic al lui 4423. F-421 e rescris pe 4481, cu ❓ pe el. Dacă formatorul confirmă varianta din 21.08, fluxul se întoarce — dar atunci trebuie explicat cum rămâne corelația decont ↔ balanță valabilă, pentru că azi nu văd cum.


---

## Anexa E — Baza legală citată

Extrasă automat din textul documentului: sunt listate actele și articolele care apar efectiv citate mai sus. Contextul fiecărei citări e în secțiunea unde apare.

**Acte normative citate**

- Legea 70/2015
- Legea 296/2023
- Codul fiscal
- Codul muncii

**Articole citate**

art. 25 alin. (1), art. 319


---

## Anexa G — Răspunsuri verificate pe surse publice

Întrebări care erau deschise și la care am găsit răspuns în lege. Fiecare poartă actul normativ pe care se sprijină și data la care a fost confruntat cu sursele. **De confirmat cu formatorul** — nu pentru că răspunsul ar fi nesigur, ci pentru că practica poate adăuga ceva ce textul nu spune.

**✅ Care sunt valorile exacte ale plafoanelor din Legea 70/2015 în forma modificată prin Legea 296/2023, la data operațiunii?**

Între persoane juridice: **5.000 lei/zi și de persoană**. Magazine cash & carry: 5.000 lei de persoană, dar maximum **10.000 lei total pe zi**; plăți către ele, maximum 10.000 lei/zi. Avansuri spre decontare: **5.000 lei/zi** pentru fiecare persoană care a primit avansul. **Fragmentarea e interzisă expres** pentru facturi peste 5.000 lei, respectiv 10.000 la cash & carry. Legea 239/2025 **nu a modificat plafoanele** de la 1.01.2026, dar a eliminat pragul de 50.000 lei de la care era obligatorie acceptarea cardului și a introdus obligația unui cont de plăți deschis în România.

*Temei:* Legea 70/2015, art. 3 și art. 4, în forma modificată prin Legea 296/2023 și Legea 239/2025.

*Plafoane de numerar și contul 455 · training 19.08.2026, punctul 1 · verificat 21.08.2026*

**✅ Care sunt exact operațiunile în numerar interzise pe contul 455 și care e temeiul legal?**

Nu e un plafon, e o **interdicție**. Din **11 noiembrie 2023**, încasările și plățile reprezentând împrumuturi — indiferent de sumă — de la sau către asociați, acționari, administratori și alte persoane fizice **nu se mai pot face în numerar**, ci doar prin instrumente de plată fără numerar. Înalta Curte a stabilit că amenda de 25% se calculează la **totalul operațiunilor**, nu la depășirea unui plafon.

*Temei:* Legea 70/2015 modificată prin Legea 296/2023, în vigoare din 11.11.2023. Cuantumul amenzii — jurisprudența ÎCCJ.

*Plafoane de numerar și contul 455 · training 19.08.2026, punctul 2 · verificat 21.08.2026*


---

*Singurul document care nu vine dintr-o zi de training proprie: e partea din 19.08.2026 care nu adâncea niciun subiect existent.*
