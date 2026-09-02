# Salarii, contribuții și rețineri
### Sursă: training 21.08.2026 — de la statul de plată la balanță, cu verificările care se fac în secunda doi

---

## Cum citești acest document

| Marcaj | Semnificație |
|---|---|
| ✅ | Notița originală era corectă — doar reformulată/completată |
| ⚠️ | **Eroare în notița originală** — corectată aici, cu explicație |
| ➕ | Completare (lucru care lipsea, dar era necesar ca raționamentul să stea în picioare) |
| ❓ | Rămas deschis — de clarificat cu formatorul (vezi Anexa D) |

---

## 1. Înainte de înregistrare: de unde vine statul de plată
Contabilitatea primește statul de plată gata făcut. Asta e și riscul: dacă statul e
greșit, nota contabilă e greșită, iar eroarea se vede abia la control.


### 1.1 Salariul minim și norma parțială


✅ Salariul minim brut pe economie este **4.325 lei**, de la **1 iulie 2026** (anterior 4.050 lei) — HG 146/2026. Tot de atunci și până la 31.12.2026, suma neimpozabilă lunară scade de la 300 la **200 lei**. Verificarea care se face lunar,
și obligatoriu la fiecare modificare a minimului: fiecare salariat trebuie să fie plătit
cel puțin la nivelul lui, **proporțional cu norma**.

| Normă | Ore | Minim pe stat |
|---|---|---|
| Întreagă | 8 | 4.325 lei |
| Jumătate | 4 | 50% din 4.325 = 2.162,50 lei |
| Un sfert | 2 | 25% din 4.325 = 1.081,25 lei |

➕ Notița rotunjea la 2.163 și 1.081. Cifra exactă contează: sub minimul proporțional,
contractul e neconform, indiferent cu cât.

Greșeala frecventă în practică nu e reaua-credință, ci **neactualizarea**: la creșterea
minimului se ajustează salariații cu normă întreagă și se uită cei cu normă parțială.
De aceea statul se cere, nu se presupune — cel puțin la fiecare modificare a minimului.


### 1.2 REGES, D112 și pontajul


Trei surse care trebuie să spună același lucru:

- **REGES** (fostul Revisal) — registrul în care se înregistrează contractele de muncă,
  modificările și **fiecare concediu medical în parte**. De acolo iese, la plecarea
  salariatului, cât a fost angajat, cât în medical, cât în concediu plătit — necesar
  pentru vechimea în muncă. Responsabilitatea e a HR-ului, dar consecința e a tuturor.
- **D112** — declarația în baza căreia se plătesc contribuțiile. Un `.xml` întocmit de
  HR, cu toate contractele și fluctuațiile lunii.
- **Pontajul** — documentul justificativ pentru întocmirea statului. Fără el, statul nu
  are bază.

➕ **Verificarea minimă:** la fiecare modificare a salariului minim, se confruntă ce e pe
stat cu ce e în REGES. Și se verifică CNP-urile — o cifră greșită înseamnă un salariat
care, pentru stat, nu există.


### 1.3 Fișa de plătitor din SPV


Cu acces la Spațiul Privat Virtual se ia **fișa pe plătitor** și se confruntă cu nota
contabilă. Cazul care apare lunar: HR-ul a uitat un concediu medical, procesează o
**rectificativă pe mai**, iar contabilitatea e deja la nota pe iunie.

Dacă statul s-a modificat și s-a depus un D112 nou, **trebuie înregistrată o notă
rectificativă** — altfel fișa de plătitor și balanța nu se mai potrivesc. Lanțul e:

> statul de plată → D112 → fișa de plătitor ANAF → balanță

Nu e opțional ca HR să comunice ce s-a modificat. Fără asta, corelația se rupe și nu se
vede până la control.

---

## 2. Monografia salariilor
### 2.1 Salariul brut și reținerile


Se pornește de la **brutul realizat de pe stat** — salariul de încadrare plus sporuri și
prime, nu salariul de încadrare.

Exemplu, salariu brut realizat 50.000 lei:

```
641  = 421    ·  50.000     (cheltuiala cu salariile — brutul realizat)
```

Din brut, statul reține trei lucruri, toate din banii salariatului:

```
421  = 4315   ·  12.500     (CAS — contribuția de asigurări sociale, pensii)
421  = 4316   ·   5.000     (CASS — asigurări sociale de sănătate)
421  = 444    ·   3.250     (impozit pe venituri de natura salariilor)
```

Cotele și baza:

- CAS: 25% × 50.000 = 12.500
- CASS: 10% × 50.000 = 5.000
- impozit: 10% din baza rămasă, adică 10% × 32.500 = 3.250

⚠️ **Notița inversa acronimele.** Scria „4315 = CASS (pensia) = 25%” și „4316 = CAS
(sănătate) = 10%”. Conturile erau corecte, denumirile schimbate între ele — iar notița se
contrazicea singură, pentru că într-un bloc anterior le avea corect. Corect este:

| Cont | Acronim | Ce este | Cotă |
|---|---|---|---|
| **4315** | **CAS** | contribuția de asigurări sociale — **pensii** | 25% |
| **4316** | **CASS** | contribuția de asigurări sociale de **sănătate** | 10% |


### 2.2 Singura contribuție a angajatorului


```
646  = 436    ·   1.125     (CAM — contribuția asiguratorie pentru muncă)
```

Cota este 2,25% aplicată la fondul de salarii: 2,25% × 50.000 = 1.125.

⚠️ **Notița scria `436 - 646`, adică invers.** În convenția ei proprie — `debit -
credit` — asta ar însemna debit 436 și credit 646: o datorie care scade și un venit care
apare. CAM este o **cheltuială** a angajatorului: debit 646, credit 436.

Contul 646 este „Cheltuieli privind contribuția asiguratorie pentru muncă”, 436 este
datoria. Toate celelalte contribuții sunt reținute din salariul angajatului; asta e
singura suportată de firmă.


### 2.3 Restul de plată


```
421  = 5121   ·  29.250     (plata prin bancă)
```

50.000 − 12.500 − 5.000 − 3.250 = 29.250.

Iar obligațiile create pe credit se sting la termen, tot prin bancă:

```
%      = 5121        20.750
4315               12.500
4316                5.000
444                 3.250
```

Plus CAM, separat: `436 = 5121 · 1.125`.


### 2.4 Tichetele de masă


⚠️ Notița pusese tichetele de masă sub contul **423**. Nu acolo stau: 423 este „Personal
— ajutoare materiale datorate”, corect pentru concediile medicale din secțiunea
următoare, dar nu pentru tichete.

Tichetele de masă merg pe **642** — „Cheltuieli cu avantajele în natură și tichetele
acordate salariaților”.

---

## 3. Concediile medicale
Indemnizația de concediu medical se împarte între doi plătitori: primele zile le suportă
**angajatorul**, restul **casa de sănătate** (fondul FNUASS).

Regulile de calcul, care nu sunt cele ale salariului:

- numărul de zile suportate de angajator **depinde de codul de boală**;
- baza de calcul este **media ultimelor 6 luni**, nu ultimul salariu;
- la un angajat nou se ia media de la locul de muncă anterior;
- indemnizațiile de risc maternal și cele asimilate vin integral de la casă.

Exemplu, indemnizație totală 1.000 lei, din care 250 lei suportați de angajator:

```
6458 = 423    ·     250     (partea suportată de angajator — cheltuială)
4382 = 423    ·     750     (partea de recuperat de la casa de sănătate — creanță)
```

Contul **4382** „Alte creanțe sociale” este o **creanță**: banii urmează să vină de la
FNUASS. Contul **6458** este cheltuiala proprie.

✅ **Reținerile din indemnizație.** Se rețin **CAS 25%** și **impozit 10%**. **CASS 10% se datorează începând cu veniturile lunii august 2026** (Legea 170/2026) — până atunci nu se datora; fac excepție indemnizațiile pentru accidente de muncă și boli profesionale. **CAM 2,25% NU se datorează** pe partea suportată din FNUASS (art. 220^5 Cod fiscal): angajatorul datorează CAM doar pe zilele pe care le suportă el. Baza de calcul e media veniturilor brute din ultimele 6 luni, plafonată la 12 salarii minime brute pe lună. *(art. 139 alin. (1) lit. o) și art. 144 Cod fiscal; OUG 158/2005 — verificat 21.08.2026)*

---

## 4. Rețineri, avansuri și datorii reciproce
### 4.1 Popriri — contul 427


Când un executor judecătoresc instituie poprire pe salariu, firma devine **intermediar**:
reține din salariul angajatului și plătește terțului.

```
421  = 427    ·   9.749,03  (reținerea din net)
427  = 5121   ·   9.749,03  (plata către executor)
```

Limita reținerii este de o treime din **salariul net** — 33,33% din 29.250 = 9.749,03.
Se calculează din net, nu din brut, pentru că banii merg la executor, nu la stat.

✅ **Sunt trei reguli, nu una** (art. 729 Cod procedură civilă): **1/2** din venitul net pentru obligații de întreținere sau alocații pentru copii · **1/3** pentru orice alte datorii · la mai multe popriri pe aceeași sumă, reținerea totală nu poate depăși **1/2**, indiferent de natura creanțelor. Iar dacă venitul e sub salariul minim net, se poate urmări doar partea care depășește **jumătate din salariul minim net** — prag de protecție pe care notițele nu-l aveau deloc. *(verificat 21.08.2026)*

**427 este contul cu cel mai mare risc penal din grupă.** Banii reținuți nu sunt ai
firmei: sunt ai angajatului, opriți în beneficiul altcuiva. Dacă firma nu îi virează,
nu are ce explica — trebuia fie să îi vireze, fie să nu îi rețină.


### 4.2 Drepturi de personal neridicate — contul 426


Dacă salariul nu ajunge la salariat, datoria nu dispare, doar își schimbă natura:

```
421  = 426                  (drepturi neridicate)
```

426 rămâne un cont de pasiv: datoria există în continuare, doar că nu mai e „salariu de
plătit luna asta”, ci „bani pe care îi datorăm cuiva care nu i-a luat”.

Cazul practic din notițe: soldul lui 421 este mai mare decât restul de plată de pe stat.
Se scot statele lună de lună, se compară cu soldul, și se găsește luna în care s-a rupt.
Dacă explicația e „doi salariați nu și-au luat banii”, suma trece la 426.

**Situația inversă e mai gravă:** dacă s-a plătit mai mult decât e pe stat, diferența e
un venit neimpozitat. Motivele nu contează contabil — tratamentul, da.


### 4.3 Creanțe față de personal la plecare — contul 4282


Când un salariat pleacă și rămâne dator firmei — un echipament de protecție nepredat, un
avans nejustificat — firma are o **creanță**:

```
4282 = 7588   ·     400     (creanța față de fostul salariat)
5311 = 4282   ·     400     (încasarea)
```

⚠️ **Notița scria `4428`.** Contul 4428 este *TVA neexigibilă* și n-are nicio legătură cu
personalul. Contul corect este **4282**, „Alte creanțe în legătură cu personalul”.


### 4.4 Avansul


Dacă s-a plătit avans în cursul lunii, el se scade din restul de plată de pe statul
final. Avansul stă pe **425** „Avansuri acordate personalului”, iar la statul de lichidare
se închide `421 = 425`. Fără pasul ăsta, restul de plată din balanță nu se potrivește cu
statul.

---

## 5. Corelațiile de balanță pe salarii
Aici e miezul practic al trainingului. Conturile de salarii se pot verifica **în secunda
doi**, pentru că documentul de control există deja: statul de plată.


### 5.1 Regula generală: rulaj creditor = sold creditor


Pentru orice datorie **constituită lunar și achitată în luna următoare**, la sfârșitul
lunii:

> **sold creditor = rulaj creditor al lunii**

Motivul e mecanic. În iulie se înregistrează obligația lunii iulie (pe credit) și se
plătește, pe 25, obligația lunii iunie (pe debit). Ce rămâne pe credit la 31 iulie este
exact obligația lunii iulie — adică rulajul creditor al lunii.

**Dacă soldul creditor este mai mare decât rulajul creditor, există restanță.** Firma nu
și-a plătit obligațiile la zi, iar diferența arată de cât timp.

Regula se aplică la:

| Cont | Ce verifică | Ce înseamnă abaterea |
|---|---|---|
| **444** | impozitul pe salarii | stopaj la sursă nevirat |
| **4315 / 4316** (prin 431) | CAS și CASS | contribuții restante |
| **436** | CAM | contribuție restantă |
| **427** | rețineri către terți | **risc penal** — bani opriți și nevirați |
| **4423** | TVA de plată | TVA restantă |

➕ **Stopajul la sursă nevirat în 30 de zile atrage răspundere penală.** Angajatorul
trebuie să știe asta, iar contabilul trebuie să i-o spună — corelația de mai sus e
instrumentul prin care se vede la timp.

**Ce o rupe LEGITIM:** un decalaj de scadență (obligația lunii se plătește în luna
următoare — asta *este* corelația), o plată în avans, o rectificativă care schimbă
obligația unei luni anterioare.

**Ce o rupe SUSPECT:** sold creditor mai mare decât rulajul, constant, pe mai multe luni.


### 5.2 Corelația cu statul de plată


> **sold creditor 421 + sold creditor 423 = restul de plată din statul de plată**

Se verifică lună de lună, și e cea mai ieftină verificare din toată contabilitatea:
statul există, soldul există, comparația durează secunde.

Când nu se potrivește, se caută luna în care s-a rupt, scoțând statele pe rând. Cazul
tipic: o plată înregistrată pe alt cont decât 421 — `627 = 5121` în loc de `421 = 5121`.


### 5.3 Verificarea CAM pe cifre


> **2,25% × rulaj creditor 421 (brut) = rulaj creditor 436**

Dacă nu se potrivește, ori baza de calcul e greșită, ori s-a omis o parte din fondul de
salarii.


### 5.4 Solduri cu semn contrar naturii contului


Un cont de activ cu sold creditor — sau invers — este aproape întotdeauna o eroare.

- **4282** (creanță față de personal) cu sold creditor: ori s-a încasat de două ori, ori
  înregistrarea inițială era pe partea greșită.
- **421** cu sold debitor: s-a plătit mai mult decât s-a datorat.

De aceea soldurile se verifică **lunar**, nu la bilanț. Verificarea lunară e picătura
chinezească: puțin, des, și cu analiticul confruntat cu sinteticul. Alternativa e să
contraverifici în martie conturi din ianuarie, când nimeni nu mai ține minte ce s-a
întâmplat.

---

## 6. Răspunsuri la întrebările din notițe
Întrebările de mai jos erau notate în text ca lucruri de lămurit. Nu sunt întrebări
pentru formator — sunt lucruri care se pot răspunde din logica înregistrării.


### 6.1 Cum se leagă rulajul debit/credit cu soldul, la 421 și 423


Rulajul este **mișcarea perioadei**; soldul este **ce a rămas**. Pe un cont de pasiv:

> sold creditor final = sold inițial + rulaj creditor − rulaj debitor

La 421, rulajul creditor al lunii este brutul datorat, iar rulajul debitor conține
reținerile și plata. Ce rămâne pe credit este exact ce mai ai de dat — deci se compară cu
restul de plată de pe stat.

Diferența față de regula „rulaj = sold” de la 444 sau 436 este că acolo soldul inițial e
zero la începutul fiecărei luni, pentru că obligația lunii precedente s-a stins. La 421,
dacă soldul inițial nu e zero, ai deja o restanță din trecut — și corelația îți spune
asta înainte să o caute altcineva.


### 6.2 De ce creanța față de un fost salariat e cont de activ


Un **activ** este ceva ce ai sau ai de primit. O **datorie** este ceva ce ai de dat.

Când fostul salariat îți datorează bani, tu ai *de primit* — deci creanță, deci activ:
4282. La încasare, nu îți trebuie un cont de pasiv „opus băncii”: pur și simplu **crește
un activ și scade altul**.

```
5311 = 4282   ·     400
```

Banca crește pe debit (activ care crește), creanța scade pe credit (activ care scade).
Bilanțul rămâne echilibrat pentru că totalul activelor nu s-a schimbat — doar forma lor.

Regula generală, care rezolvă toate cazurile de genul: **întreabă întâi ce s-a întâmplat
economic**, apoi caută conturile. Nu invers.


### 6.3 De ce nu trebuie solduri creditoare pe conturi de activ


Pentru că ar afirma ceva imposibil: „am o creanță negativă”. În practică înseamnă
întotdeauna una din trei — s-a înregistrat pe partea greșită, s-a încasat de două ori,
sau s-a încasat ceva ce nu era înregistrat ca datorat.

Bilanțul prezintă activele pe o parte și pasivele pe alta. Un activ cu sold creditor ori
se prezintă greșit, ori trebuie reclasificat ca datorie — și atunci nu mai e ce spune
numele contului.

## 9. Fondul de handicap
**Material integral nou.**


### 9.1 Când se datorează


Din momentul în care societatea are **peste 50 de angajați ca număr mediu**. Formatorul spune
că formula legală e greoaie și dă una simplă, cu abatere neglijabilă.

Temeiul: **Legea 448/2006, art. 78** — angajatorii cu **cel puțin 50 de angajați** au obligația
de a angaja persoane cu handicap în proporție de **cel puțin 4%** din numărul total de angajați.


### 9.2 Numărul mediu de angajați — metoda


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


### 9.3 Cota și calculul obligației


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


### 9.4 Înregistrarea și declararea


```
635 = 447    6.055
```

Se declară în **D100, rândul 810**. Nu e obligatoriu să treacă prin D700 și **nu apare pe
vector**.


### 9.5 Reducerea prin achiziții de la unități protejate


Varianta pe care formatorul o recomandă de explorat: contract cu o societate **acreditată**,
de la care se fac achiziții direct pe `401`, se scad din `447`, și se declară doar diferența.

⚠️ Plafonul: **nu se poate depăși 50%** din valoarea obligației. Restul se plătește oricum.

✅ Temeiul confirmă și structura, și plafonul: **Legea 448/2006, art. 78** dă angajatorului care
nu ocupă cota de 4% două variante — (a) plata integrală a **salariului de bază minim brut pe
țară × numărul de locuri de muncă neocupate**, sau (b) plata a **cel puțin 50%** din această
sumă la bugetul de stat, diferența fiind folosită pentru **achiziția de produse sau servicii
de la unități protejate autorizate**. Varianta (b) e exact ce descrie notița, iar „maximum 50%”
e reversul lui „cel puțin 50% la buget”.

## 10. Două chestiuni de personal
### 10.1 Codul fiscal al salariatului de la punctul de lucru


**Material nou.** Dacă ai punct de lucru și ai salariat acolo, trebuie **cerut cod fiscal pentru
acel salariat**. Se aplică și la **sectoare**, pentru că sunt primării diferite: raportarea se
face la primăria de care ține punctul de lucru.


### 10.2 Locuința de serviciu


Societățile pot acorda **locuință de serviciu** salariaților care îndeplinesc condițiile din
Codul fiscal. Deductibilitatea e **20% din salariul minim**, calculată **pe salariat** — nu pe
firmă. Este un **avantaj de natură salarială neimpozabil**, încadrat ca atare în Codul fiscal.

❓ Ultima propoziție a notiței — că în zona de salarii se calculează un avantaj **net**, pentru
care se determină apoi un **brut impozabil** — e marcată de formator „{de contraverificat}”. O
las deschisă: dacă avantajul e neimpozabil, brutarea lui nu se justifică; dacă se depășește
plafonul de 20%, doar **excedentul** ar trebui brutat. Cele două afirmații nu se pot împăca fără
confirmare.

---

## Anexa B — Checklist practic

1. Statul de plată primit de la HR, cu pontajul în spate.
2. Salariații cu normă parțială — verificat minimul proporțional.
3. `sold 421 + sold 423` = restul de plată de pe stat.
4. `rulaj creditor = sold creditor` pe 444, 431, 436, 427.
5. `2,25% × brut = rulaj creditor 436`.
6. Fișa de plătitor din SPV confruntată cu balanța.
7. Rectificativele de la HR — nota rectificativă înregistrată în aceeași lună.
8. Conturi de activ cu sold creditor, sau invers — investigate, nu reportate.
9. `sold 4423 / 4424` din balanță = soldul din decontul de TVA.
10. Sumele din decizii de impunere — pe analitic distinct, în afara decontului.

---

---

## Anexa C — Ce am corectat față de notițele originale

| Notița | Corect | Unde |
|---|---|---|
| `436 - 646` pentru CAM | `646 = 436` | 2.2 |
| `4428` pentru datoria fostului salariat | `4282` | 4.3 |
| `6918` pentru impozitul micro | `698` | 6.2 |
| `4315 = CASS (pensia)`, `4316 = CAS (sănătate)` | 4315 = CAS = pensii · 4316 = CASS = sănătate | 2.1 |
| Tichetele de masă sub 423 | 642 | 2.4 |
| Minimul proporțional rotunjit la 2.163 / 1.081 | 2.162,50 / 1.081,25 | 1.1 |

---

---

## Anexa D — Rămase deschise

Ce e încă provizoriu în documentul ăsta. Lista nu e scrisă aici: vine din `date/intrebari.py`, aceeași sursă cu foaia „Întrebări deschise” a workbook-ului și cu lista trimisibilă formatorului.

**❓ Dacă avantajul locuinței de serviciu e neimpozabil în limita a 20% din salariul minim, ce se brutează — tot avantajul, sau doar excedentul?**

*Declarații informative și avantaje salariale · training 31.08.2026, punctul 2*

Notița spune întâi că e „avantaj de natură salarială neimpozabil”, apoi că „în zona de salarii se calculează un avantaj salariat NET, pentru care se calculează un brut impozabil”. Formatorul a marcat exact ultima propoziție „{de contraverificat}”.

**Ce am presupus între timp:** Nu am implementat brutarea. Am consemnat plafonul de 20% pe salariat și presupunerea cea mai probabilă — că se brutează DOAR excedentul peste plafon, cum se procedează la celelalte avantaje plafonate — dar am lăsat-o marcată, pentru că e o presupunere, nu o regulă citită.


---

## Anexa E — Baza legală citată

Extrasă automat din textul documentului: sunt listate actele și articolele care apar efectiv citate mai sus. Contextul fiecărei citări e în secțiunea unde apare.

**Acte normative citate**

- Legea 448/2006
- Codul muncii
- Codul fiscal

**Articole citate**

art. 78


---

## Anexa G — Răspunsuri verificate pe surse publice

Întrebări care erau deschise și la care am găsit răspuns în lege. Fiecare poartă actul normativ pe care se sprijină și data la care a fost confruntat cu sursele. **De confirmat cu formatorul** — nu pentru că răspunsul ar fi nesigur, ci pentru că practica poate adăuga ceva ce textul nu spune.

**✅ Care este salariul minim brut pe economie în vigoare, și de la ce dată?**

**4.325 lei** brut, de la **1 iulie 2026** (anterior 4.050 lei). Minimul se aplică proporțional cu norma: 2.162,50 lei la jumătate de normă, 1.081,25 la un sfert. Tot de la 1 iulie 2026 și până la 31.12.2026, suma neimpozabilă scade de la 300 la 200 lei/lună.

*Temei:* HG 146/2026 (salariul minim). Suma neimpozabilă — Cod fiscal, cu aplicare 1.07–31.12.2026.

*Salarii — praguri și baze de calcul · training 21.08.2026, punctul 1 · verificat 21.08.2026*

**✅ Ce contribuții se datorează pentru indemnizația de concediu medical, și pe ce parte se rețin?**

Din indemnizație se rețin **CAS 25%** și **impozit 10%**. **CASS 10% se datorează începând cu veniturile lunii august 2026** — până atunci nu se datora. Fac excepție indemnizațiile pentru accidente de muncă și boli profesionale, care rămân scutite de CASS. **CAM 2,25% NU se datorează** pe partea suportată din FNUASS: angajatorul datorează CAM doar pe zilele pe care le suportă el. Baza de calcul e media veniturilor brute din ultimele 6 luni, plafonată la 12 salarii minime brute pe lună.

*Temei:* CAS: Cod fiscal art. 139 alin. (1) lit. o) și art. 144. CASS: Legea 170/2026, aplicabilă veniturilor din august 2026. CAM: Cod fiscal art. 220^5. Baza: OUG 158/2005.

*Salarii — praguri și baze de calcul · training 21.08.2026, punctul 3 · verificat 21.08.2026*

**✅ Care e limita de reținere prin poprire pentru obligațiile de întreținere, față de treimea aplicabilă datoriilor obișnuite?**

Sunt **trei** reguli, nu una. **1/2** din venitul net lunar pentru obligații de întreținere sau alocații pentru copii; **1/3** pentru orice alte datorii. Când există mai multe popriri pe aceeași sumă, reținerea totală nu poate depăși **1/2**, indiferent de natura creanțelor. Iar dacă venitul e sub salariul minim net pe economie, se poate urmări doar partea care depășește **jumătate din salariul minim net** — prag de protecție pe care notițele nu-l aveau deloc.

*Temei:* Codul de procedură civilă, art. 729 — Limitele urmăririi veniturilor bănești.

*Salarii — praguri și baze de calcul · training 21.08.2026, punctul 4 · verificat 21.08.2026*


---

*Al cincilea document. Salariile sunt clasa 4, dar un document intitulat „Stocuri, TVA și corelații de balanță” nu le putea găzdui fără să mintă — iar materialul e coerent și mare cât să stea singur.*
