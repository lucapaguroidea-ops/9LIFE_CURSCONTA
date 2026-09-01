# Trezorerie, efecte de încasat și verificarea balanței — notițe training 28.08.2026

*Versiune revizuită. Sursa: notițele brute din 28.08.2026.*

## 0. Ce e deja în sistem

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

## 1. Recapitulare: taxarea inversă

### 1.1 Ce operațiuni intră

Taxarea inversă e o **măsură fiscală de protecție**: statul mută obligația de plată a
TVA de la furnizor la cumpărător, în domeniile unde frauda e cea mai ușoară.

Din lista discutată la curs:

| Operațiunea | Nuanța care se uită |
|---|---|
| Construcții și terenuri | Se aplică la livrările **taxabile** — construcțiile noi sunt taxabile prin efectul legii, cele vechi doar prin opțiune |
| Cereale și plante tehnice | **Sămânța pentru însămânțat NU intră** — are alt cod tarifar decât cerealele de consum |
| Deșeuri feroase și neferoase | Doar cele din listă, nu orice rebut |
| Masă lemnoasă — cherestea, buștean | Materialele lemnoase din listă |

➕ Precizare la construcții: notița spune „construcții noi (la prima ocupare)”. Criteriul
din lege nu e vechimea, ci **regimul livrării**: taxarea inversă se aplică oriunde
livrarea e taxabilă, fie prin efectul legii (construcție nouă), fie prin **opțiunea**
vânzătorului (construcție veche). O construcție veche vândută cu opțiune de taxare intră
la fel de bine.

### 1.2 Codurile din nomenclatorul D394

Fiecare tip de tranzacție cu taxare inversă are un **cod** pe care D394 îl recunoaște.
Formatorul a dat exemplul deșeurilor — cod **22**.

⚠️ Fără codul asociat, **D394 nu se validează**. Nu e o eroare de conținut care se vede
la control peste doi ani; e un refuz la depunere, în ziua declarației.

➕ Mecanismul nu e nou: e chiar pasul revelator al lui **F-203**, unde apare cu codul
**27** la livrarea de clădiri în regim de taxare inversă. Ce adaugă trainingul ăsta e că
regula e **generală**, nu specifică clădirilor: fiecare categorie din art. 331 are codul
ei, iar deșeurile sunt exemplul al doilea. Regula, formulată o dată pentru toate
categoriile: **codul e condiție de recunoaștere declarativă, nu ornament.**

❓ Nomenclatorul complet de coduri nu era în notițe și nu se poate reconstitui din
memorie. Se ia din instrucțiunile de completare ale formularului D394, în vigoare la data
depunerii, și se atașează configurării programului **înainte** de prima operațiune cu
taxare inversă, nu la depunere.

### 1.3 Ce se înregistrează și ce nu

La **cumpărare**, autolichidarea produce notă contabilă:

```
4426 = 4427        cu aceeași sumă
```

Suma apare în **ambele jurnale** — și de cumpărări, și de vânzări — exact ca la
achizițiile intracomunitare.

La **livrare** de bunuri supuse taxării inverse, situația e alta:

➕ **Nu se face notă contabilă pentru TVA.** Furnizorul nu colectează nimic: factura
poartă mențiunea „taxare inversă”, iar obligația trece la cumpărător. Ce rămâne în sarcina
furnizorului e **mențiunea în jurnalul de vânzări** și **codul de operațiune** pentru
D394. Cine caută nota contabilă la livrare n-o găsește pentru că nu există — nu pentru că
a uitat-o cineva.

Codul se asociază **și la intrare, și la ieșire**.

### 1.4 Rubricile separate din jurnale

Jurnalele trebuie să aibă rubrici distincte, nu o coloană comună:

- taxare inversă România
- taxare inversă intracomunitară
- achiziții scutite (de la neplătitori de TVA)
- importuri

➕ Rostul separării: fiecare rubrică alimentează alt rând din D300 și altă declarație
(D390 doar la intracomunitar). Amestecate, cifrele sunt corecte în total și greșite pe
fiecare rând.

## 2. Investiții pe termen scurt: acțiuni și obligațiuni

### 2.1 Achiziția de acțiuni

```
501 = 5121        achiziția acțiunilor
```

➕ **Analitic pe fiecare societate emitentă.** Dacă firma deține participații la mai
multe societăți, un 501 sintetic nu poate spune care participație s-a apreciat și care
s-a depreciat — iar ajustările pentru pierdere de valoare (591) se constituie pe fiecare
titlu, nu pe total.

⚠️ **501 nu e contul oricăror acțiuni.** El e în clasa 50 — investiții pe termen
**SCURT**, cumpărate ca plasament, cu intenția de a fi revândute. Participația deținută
**durabil** merge în clasa 26 — imobilizări financiare:

| Termen scurt (plasament) | Termen lung (participație) |
|---|---|
| 501 Acțiuni deținute la entitățile afiliate | 261 Acțiuni deținute la entitățile afiliate |
| 506 Obligațiuni | 263 Acțiuni deținute la entități controlate în comun |
| 508 Alte investiții pe termen scurt | 265 Alte titluri imobilizate |

Capcana e că **501 și 261 poartă aceeași denumire în plan**. Ce le deosebește nu e
emitentul, e INTENȚIA de deținere — iar intenția nu se citește din denumire, se
declară la achiziție. Cine ia contul după nume înregistrează o participație de zece ani
ca plasament pe termen scurt.

### 2.2 Acțiuni vs. obligațiuni — ce cumperi de fapt

Notița cerea detalierea distincției. E mai mult decât o diferență de cont:

| | Acțiuni | Obligațiuni |
|---|---|---|
| **Ce sunt** | Drept de **proprietate** — deții o parte din societate | **Împrumut** — ai dat bani societății |
| **Ce primești** | Dividende, dacă se repartizează | Dobândă, contractual, indiferent de profit |
| **Riscul** | Dacă societatea pierde, valoarea scade | Dacă societatea pierde, dobânda se datorează oricum |
| **La lichidare** | Ultimul la împărțire | Înaintea acționarilor — ești creditor |
| **Contul** | 501 (afiliate) / 508 | 506 |

În SA sunt **acțiuni**, în SRL sunt **părți sociale** — nu e o diferență de vocabular:
părțile sociale nu se tranzacționează liber, cesiunea lor cere hotărâre și mențiune la
ONRC.

Obligațiunea se cumpără la un preț și se răscumpără la altul; diferența, plus dobânda și
eventualele diferențe de curs dacă e în valută, formează rezultatul operațiunii.

⚠️ **506 și 505 nu sunt același lucru**, deși ambele au „obligațiuni” în nume:

| Cont | Ce ține | Cine e emitentul |
|---|---|---|
| **506** Obligațiuni | plasamentul TĂU în obligațiunile altcuiva | altă societate |
| **505** Obligațiuni emise și răscumpărate | propriile tale obligațiuni, pe care le-ai răscumpărat | tu |

505 e oglinda lui 161 „Împrumuturi din emisiuni de obligațiuni”: ai împrumutat de la
piață, apoi ți-ai cumpărat înapoi titlurile. 506 e un activ de plasament; 505 e stingerea
unei datorii proprii.

De aceea și ajustările pentru pierdere de valoare au conturi separate pe fiecare fel de
titlu — 591 pentru acțiuni la afiliate, 595 pentru obligațiuni emise și răscumpărate, 596
pentru obligațiuni, 598 pentru alte investiții.

❓ Monografia completă a răscumpărării (preț de emisiune vs. preț de răscumpărare, primă
sau discount, curs valutar dacă emisiunea e în valută) nu era în notițe — formatorul a
marcat subiectul „de detaliat” fără cifre. Rămâne de cerut.

## 3. Efecte de încasat: CEC-uri și bilete la ordin

### 3.1 De la factură la încasare

Punctul de plecare — o vânzare de marfă de 10.000 lei fără TVA:

```
4111 = 707        10.000     venitul din vânzare
4111 = 4427        2.100     TVA colectată, 21%
```

Clientul plătește cu un **CEC de 12.100 lei**:

```
5112 = 4111       12.100     efectul primit stinge creanța
5121 = 5112       12.100     încasarea efectivă, la scadență
```

➕ Aici e nuanța care contează: **primul pas stinge clientul, dar banii nu sunt încă în
bancă.** Efectele se emit la termen — rar se emite factura azi și se primește CEC-ul tot
azi. Între cele două înregistrări, 4111 arată zero, iar riscul de neîncasare stă pe 5112.
Cine se uită doar la soldul clienților crede că a încasat.

**Biletul la ordin** funcționează identic, pe contul 5113:

```
5113 = 4111       12.100     la primirea biletului
5121 = 5113       12.100     la încasare
```

### 3.2 Scontarea biletului la ordin

Dacă biletul are scadență peste două luni, banca poate să-l **sconteze**: îți dă acum un
procent din valoare, și încasează ea efectul la scadență.

Pe biletul de **12.100 lei**, cu 80% avansat de bancă:

```
5114 = 5113       12.100     efectul pleacă spre scontare
5121 = 5114        9.680     lichiditatea primită, 80%
667  = 5114        2.420     costul scontării, restul de 20%
```

⚠️ Notița scria contul de cheltuială ca `6067`. Contul corect este **667 — „Cheltuieli
privind sconturile acordate”**, cu perechea de venit **767 — „Venituri din sconturi
obținute”** (scontul pe care îl obții tu, când plătești un furnizor înainte de scadență).
`6067` nu există în planul de conturi.

⚠️ Notița pornea de la „bilet la ordine de **12k** lei”, dar calcula 80% = 9,68k. 80% din
12.000 dă 9.600. Baza corectă e **12.100** — suma cu TVA din exemplul de mai sus.

➕ De ce trece prin 5114 și nu direct din 5113: mutarea spune că efectul **a plecat din
mâna ta**. Cât timp stă pe 5113, îl mai ai. Din 5114 se închide în trei direcții — bani,
cost, și zero rest — iar dacă rămâne sold acolo, scontarea nu s-a finalizat.

Contul 5114 se închide exact: 9.680 + 2.420 = 12.100.

### 3.3 Când merită scontarea și când nu

Scontarea e un instrument **scump** — cei 20% nu sunt dobândă la an, sunt costul
operațiunii. Banca o acordă societăților cu activitate îndelungată și clienți la fel; nu
e o facilitate pentru firme mici.

Rostul ei e altul decât costul: **contabilitatea românească e de angajamente.** Faci
factura, nu o încasezi, și statul cere TVA-ul și impozitul oricum. Societatea se poate
bloca având vânzări. Scontarea aduce lichiditatea mai devreme decât încasarea, iar analiza
băncii e mult mai rapidă decât la un credit clasic — pentru că se uită la efectul din
mână, nu la indicatorii tăi de profit.

## 4. Conturile la bănci

### 4.1 Conturile în valută și reevaluarea lunară

Conturile în valută se **reevaluează la cursul BNR de la sfârșitul lunii**. Diferența
rezultată se înregistrează, nu se lasă în așteptare.

La decontări în valută apar diferențe pentru că datoria s-a înregistrat la **cursul
istoric** — cel de la data recepției — și se plătește la cursul zilei:

| Situația | Curs istoric | Curs la decontare | Rezultatul |
|---|---|---|---|
| Datorie de 100 EUR către furnizor | 5,00 | 6,00 | **cheltuială** — plătești mai mulți lei |
| Datorie de 100 EUR către furnizor | 5,00 | 4,00 | **venit** |
| Creanță de 100 EUR de la client | 5,00 | 6,00 | **venit** — încasezi mai mulți lei |
| Creanță de 100 EUR de la client | 5,00 | 4,00 | **cheltuială** |

⚠️ Notița inversa sensurile la creanțe: scria „100 eur de la furnizor; istoric era 5, și
la încasare era 6, avem un venit” — dar „de la furnizor” cu „încasare” amestecă cele două
cazuri. Regula unică, din care ies toate patru: **la curs mai mare, elementul de ACTIV
aduce venit, iar elementul de PASIV aduce cheltuială.**

➕ **Avansurile în valută NU se reevaluează.** Regula de reevaluare lunară privește
elementele **monetare** — disponibilul, creanțele și datoriile care se vor stinge în
bani. Un avans plătit sau încasat e **nemonetar**: dă dreptul la un bun sau la un
serviciu, nu la o sumă. Deci rămâne la **cursul de la data plății**, indiferent cum se
mișcă cursul până la factura finală, iar la factură se folosește tot acel curs istoric
pentru partea acoperită de avans. Cine reevaluează avansul umflă sau dezumflă un cont
care n-are ce diferență de curs să producă. ❓ Articolul exact din OMFP 1802/2014 pe
elementele nemonetare — regula e fermă, referința rămâne de confirmat.

### 4.2 Diferențele de curs: 665/765 sau 668/768?

❓ **Divergență de rezolvat cu formatorul.** Notițele spun:

> diferențele de curs valutar, curent, le înregistrăm prin 665 / 765
> diferența de reevaluare la sfârșitul lunii (financiare): 668 / 768

Funcțiunea contului **665** din OMFP 1802/2014 include explicit diferențele nefavorabile
rezultate *„la sfârșitul lunii/exercițiului financiar, din evaluarea disponibilităților
bancare și a numerarului în valută”*. Adică reevaluarea de lună e chiar în funcțiunea lui
665/765, nu în afara ei.

Conturile **668/768** („alte cheltuieli / venituri financiare”) au un rost diferit:
creanțele și datoriile **exprimate în lei, dar decontabile în funcție de cursul unei
valute** — alt caz decât valuta propriu-zisă.

**Scopul formatorului e însă corect** și merită păstrat: el vrea ca diferența din
reevaluare să se vadă separat de cea de la decontare, altfel nu poți explica soldul.
Rezultatul se obține cu **analitic pe 665/765**, nu cu alt sintetic:

```
665.DEC / 765.DEC     diferențe la decontare
665.REV / 765.REV     diferențe din reevaluarea de sfârșit de lună
```

Așa rămân ambele în „diferențe de curs valutar” la raportare, dar se separă acolo unde
contează — la explicat.

Am păstrat 665/765 pentru ambele situații, cu analitic. Dacă formatorul confirmă varianta
cu 668/768, se schimbă — dar atunci trebuie explicat cum se raportează diferențele de
curs care nu mai sunt în contul de diferențe de curs.

### 4.3 Dobânzi de plătit și de încasat

**Dobânda la credit, când e FIXĂ pe toată durata**, se cunoaște din scadențar de la
început, deci se recunoaște în avans:

```
471  = 5186        dobânda totală din scadențar, ca cheltuială în avans
5186 = 5121        la fiecare plată
666  = 471         eșalonat, lună de lună
```

**Dobânda VARIABILĂ**, calculată de bancă la sold, nu se poate anticipa — deci nu are ce
căuta în 471:

```
5186 = 5121        la plată
666  = 5186        recunoașterea cheltuielii
```

sau, mai scurt, `666 = 5121` direct.

➕ Distincția nu e de stil. 471 înseamnă „știu suma și știu perioada”. La dobândă
variabilă nu știi nici una, nici alta, iar o sumă pusă acolo se dovedește greșită la prima
schimbare de indice.

**Dobânzile de încasat** merg în oglindă, prin 5187 (cont de **activ**):

```
5187 = 472         creanța și venitul amânat
472  = 766         recunoașterea venitului
5121 = 5187        încasarea
```

➕ Notițele insistă că primele două se fac **concomitent** — ține de politica fiecărei
societăți când anume, dar nu una fără cealaltă. Al treilea pas lipsea din notițe: fără el,
5187 rămâne cu sold și pare creanță neîncasată.

### 4.4 Linii de credit (5191) vs. credite cu scadențar (1621)

| | Linie de credit | Credit cu scadențar |
|---|---|---|
| **Contul** | 5191 — datorie pe termen scurt | 1621 — datorie pe termen lung |
| **Documentul** | fără scadențar; se reînnoiește anual | scadențar cu rata și dobânda pe fiecare lună |
| **Cum funcționează** | tragi și restitui de câte ori vrei | rate fixe, la date fixe |
| **Ce plătești** | doar ce utilizezi — dar e produs scump | tot ce e în scadențar |

```
5121 = 5191        tragerea din linie
5191 = 5121        restituirea
```

⚠️ **Riscul specific**, subliniat de formator: la linia de credit **nu ai scadențar**.
Extrasele au explicații evazive, diferite de la o bancă la alta, iar unele (exemplul dat —
UniCredit) nu afișează sold intermediar, deci se operează la sfârșit de lună.

Fără extrasul de linie de credit cerut clientului, se ajunge să se opereze totul prin 5121
și să se rateze dobânda (666). Consecința nu e cosmetică: **cheltuiala nedeclarată
înseamnă impozit pe profit plătit în plus.**

La un credit cu scadențar, dacă înregistrezi rata în loc de dobândă te uiți în scadențar
și îți dai seama. La linie nu ai la ce să te uiți — de aceea se cere **soldul de la
sfârșit de lună**, ca verificare independentă.

➕ Analitic pe fiecare linie de credit, ca la 501: două linii pe același cont nu se mai
pot reconcilia cu extrasele.

⚠️ **5191 nu ajunge niciodată cu sold debitor.** E cont de pasiv; un sold debitor
înseamnă că s-a restituit mai mult decât s-a tras, deci o înregistrare greșită.

## 5. Casa și plafoanele de numerar

### 5.1 Plafonul soldului de casă

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

### 5.2 Ce plăți sunt plafonate și ce plăți nu

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

### 5.3 Plăți fragmentate și contractul cu plata în rate

Fragmentarea unei plăți ca să încapă sub plafon e **interzisă expres**.

Există însă o cale legitimă: **contractul cu plata în rate**. Dacă există contract, cu
scadențar și date fixe, încasarea în tranșe nu mai e fragmentare — e executarea
contractului. Din 20.000 lei se poate încasa de la o persoană fizică toată suma, în ratele
prevăzute.

➕ Condiția nu e formalitatea contractului, ci **respectarea lui**: dacă ratele se încasează
la alte date sau în alte sume decât scrie în scadențar, apărarea cade.

## 6. Tichete de masă și alte valori

```
5328 = 401        achiziția tichetelor de la furnizor
6422 = 5328       acordarea, la înregistrarea statului de plată
```

⚠️ Notița scrie contul ca `5238` în două locuri și ca `5328` în altele. Corect e
**5328**; `5238` nu există — grupa 52 nu există deloc în planul de conturi.

➕ Denumirea lui 5328 în OMFP 1802/2014 este **„Alte valori”**, nu „tichete de masă”:
planul nu are un cont dedicat lor. Grupa 532 are conturi proprii pentru timbre (5321),
bilete de tratament (5322) și bilete de călătorie (5323), iar tichetele de masă intră la
5328. De aceea analiticul e util și aici: 5328 poate ține simultan tichete de masă,
tichete cadou și carduri valorice, care au regimuri fiscale diferite.

Fiscalizarea se face pe statul de plată: **impozit 10% și CASS 10%**. Nu se datorează CAS
și nu se datorează CAM.

➕ Tichetele stau pe 5328 ca **stoc de trezorerie** între achiziție și acordare. Contul se
verifică **lunar**, nu trimestrial: un sold acolo înseamnă tichete cumpărate și
neacordate, iar la fiecare lună trecută devine mai greu de spus cui i se cuveneau.

**Regula funcției de bază:** tichetele se acordă doar la locul de muncă de bază — o normă
de 4 ore poate fi funcție de bază, dar dintre două contracte de 8 ore doar unul poate fi.
Se acordă la sfârșitul lunii, când se știe efectiv cine a fost la lucru: nu se dau pentru
zilele de concediu.

## 7. Avansuri de trezorerie (542)

### 7.1 Monografia decontului

Acordarea avansului către salariat:

```
542 = 5121        5.000     (sau 5311, dacă se dă din casă)
```

Salariatul se întoarce cu decontul și documentele. **Fiecare cheltuială cu TVA trece
întâi prin furnizor** — altfel TVA-ul nu se poate deduce:

**Motorină — 2.000 lei, cotă 21%:**

```
6022 = 401        1.652,89
4426 = 401          347,11
401  = 542        2.000,00     plata furnizorului din avans
```

**Cazare — 1.000 lei, cotă 11%:**

```
625  = 401          900,90
4426 = 401           99,10
401  = 542        1.000,00
```

### 7.2 Diurna — partea care lipsea

Notița se opreşte la „part 3 din 3: 2.000 lei decontul = diurna”, fără înregistrare.

➕ Nu e o omisiune de transcriere: **diurna rupe tiparul primelor două.** Nu are furnizor
și nu are TVA de dedus — e o sumă cuvenită salariatului pentru deplasare. Deci nu trece
prin 401:

```
625 = 542         2.000     direct, fără furnizor și fără TVA
```

Decontul se închide exact: 2.000 + 1.000 + 2.000 = **5.000 lei**, cât s-a acordat.

➕ Există și varianta prin **421**, când diurna se plătește odată cu salariul în loc să
se deconteze din avansul de trezorerie: `625 = 421`, iar 542 se închide numai cu ce s-a
cheltuit efectiv. E o alegere de politică de decont, nu de corectitudine — dar trebuie
făcută consecvent, altfel aceeași deplasare apare când pe 542, când pe 421, și niciun
analitic nu mai spune nimic.

❓ **Plafonul de deductibilitate al diurnei** nu era în notițe. Peste plafon, diurna se
asimilează salariului și se impozitează ca atare — deci cifra contează. De confirmat
nivelul în vigoare la data deplasării.

### 7.3 De ce analiticul e obligatoriu aici

Formatorul e categoric: **„542 pe analitic este esențial”**, cu patru semne de exclamare.

Motivul e că soldul poate merge în ambele sensuri, pe același cont, pe persoane diferite:
un șofer a pus bani de la el și firma îi datorează, altul a primit avans mai mare și
trebuie să restituie. Pe un 542 sintetic, cele două se anulează și soldul arată aproape
zero — corect ca total, fals pe fiecare om.

Partea asta e cea mai greu de ținut din toată trezoreria, și fiecare program de
contabilitate o tratează altfel.

## 8. Viramente interne (581)

### 8.1 Când 581 are voie să aibă sold

581 trebuie să ajungă la **zero**. Excepția legitimă: transferul făcut la sfârșitul lunii
și primit la începutul lunii următoare — atunci soldul e chiar realitatea, banii sunt pe
drum.

### 8.2 Diferența de curs la transferul valută → lei

⚠️ La transferul din valută în lei, diferența de curs **se reglează prin bancă, nu prin
581** — notițele subliniază cu șase semne de exclamare.

Motivul: 581 e un cont de **tranzit pur**, care trebuie să iasă cu exact cât a intrat.
Dacă diferența de curs se lasă acolo, contul nu se mai închide și devine imposibil de spus
dacă soldul rămas e un transfer în curs sau o diferență necontabilizată. Diferența
aparține contului de bancă în valută, unde s-a și produs.

## 9. Cheltuielile de clasa 6 și gestiunile de clasa 3

### 9.1 Tabelul corespondențelor

Notița cerea contraverificarea și completarea listei. Fiecare cont de cheltuială are
gestiunea lui:

| Cheltuiala | Gestiunea | Ce cuprinde |
|---|---|---|
| 601 | 301 | Materii prime |
| 6021 | 3021 | Materiale auxiliare |
| 6022 | 3022 | Combustibili |
| 6023 | 3023 | Materiale pentru ambalat |
| 6024 | 3024 | Piese de schimb |
| 6028 | 3028 | Alte materiale consumabile |
| 603 | 303 | Obiecte de inventar — **și 8035**, extrabilanțier |
| 604 | — | Materiale nestocate: direct pe cheltuială, fără gestiune |
| 605 | — | Utilități: energie, apă — direct din factură |
| 607 | 371 | Mărfuri |
| 608 | 381 | Ambalaje |
| 609 / 709 | — | Reduceri comerciale primite / acordate, **ulterioare facturii** |

⚠️ Notița scria perechea lui 608 ca `308`. E o transpoziție de cifre: **381** e contul de
ambalaje, iar `308` e „Diferențe de preț la materii prime și materiale” — un cont
rectificativ, care nu poate fi gestiunea pe care 608 o consumă.

➕ 603 e singurul care are și un pas **extrabilanțier**: obiectele de inventar date în
folosință ies din gestiune, dar rămân pe 8035, ca să știi ce ai pe teren. Fără el, un
obiect dat în folosință dispare din evidență în ziua consumului.

➕ 609/709 nu sunt reducerile de pe factura inițială — alea se scad direct din bază. Sunt
reducerile primite sau acordate **ulterior**, pe o factură separată.

### 9.2 Regula: consumul trece prin gestiune

⚠️ **Nu se recomandă înregistrarea directă `6021 = 401`.** Corect e în doi pași:

```
3021 = 401        intrarea în gestiune
6021 = 3021       consumul, pe bază de bon de consum
```

Motivul: un bun trecut direct pe cheltuială **n-a intrat niciodată în evidență**, deci nu
poate fi scos din ea. Nu ai ce inventaria, nu ai ce justifica, și nu poți răspunde la
întrebarea „unde e”.

Verificarea inversă, pe care o face și controlul: **de ce am rulaj pe 601 dacă n-am rulaj
pe 301?** O cheltuială cu materii prime fără gestiune de materii prime spune că bunurile
n-au trecut niciodată prin depozit.

➕ De când s-a implementat **SAF-T**, modulul de stocuri se cere la control. Nu ajunge să
existe — trebuie să fie **deja gestionat** și prezentabil.

### 9.3 Excepțiile

**Bonul de benzină:** `6022 = 401` direct e acceptabil. Când vine factură sau când
combustibilul se stochează, se aplică regula gestiunii.

**Materialele nestocate (604):** apa pentru angajați, pixurile, hârtia — bunuri cumpărate
și consumate imediat, care nu se stochează.

Criteriul nu e valoarea, ci **dacă bunul stă**: o mie de pixuri cumpărate de o firmă care
le consumă în timp intră în 3028, cu bon de consum la fiecare ieșire. Aceleași o mie de
pixuri duse toate pe șantier în aceeași zi n-au ce căuta în 3028 — se consumă imediat,
deci 604.

➕ Al treilea caz, care lipsea din notiță: dacă firma **revinde** pixurile, ele nu sunt
nici 3028, nici 604 — sunt **marfă, 371**. Criteriul e destinația, nu obiectul.

**Anvelopele** sunt piese de schimb: șapte anvelope cumpărate și folosite pe rând intră în
**3024**, nu pe cheltuială directă.

**Reparațiile (611):** se folosesc când factura are **deviz** în spate — de exemplu piese
de 5.000 lei și manoperă de 2.000. Devizul e cel care permite separarea: manopera pe 611,
piesele după regula gestiunii.

### 9.4 Transferul între gestiuni: marfa devenită materie primă

Cazul apare des: ai recepționat ceva ca **marfă** în 371, dar se dovedește că-l consumi
într-o lucrare, nu-l revinzi.

```
301 = 371         transferul, pe bază de bon de transfer
601 = 301         consumul, pe bază de bon de consum
```

➕ Nu se sare peste primul pas. `601 = 371` ar asocia o cheltuială cu materii prime unei
gestiuni de mărfuri, iar contul de cheltuială și-ar pierde înțelesul. Formatorul e explicit:
**niciodată 601 la 371**, nici dacă programul îl propune prestabilit.

### 9.5 Bonul de consum

Notița cerea clarificarea. Ordinea e:

1. **Se creează gestiunea** — se definește ce ține, cine răspunde de ea;
2. **Abia apoi se pune problema consumului**, pe bază de bon de consum.

Orice ieșire din gestiune se face pe bon de consum. Fără el, scăderea din stoc nu are
document justificativ, iar diferența se constată la inventar fără explicație.

✅ Forma bonului de consum e reglementată de OMFP 2634/2015. „Fișa limită de consum”, pe
care o pusesem aici ca posibilă alternativă, a fost ELIMINATĂ prin același ordin — nu mai
e formular valid, așa că notița brută avea dreptate să nu o pomenească. La transferul între
gestiuni se folosește bonul de transfer (aviz intern), exact ca în notiță. Răspuns
verificat pe OMFP 2634/2015; vezi Anexa G.

## 10. Verificarea analitic ↔ sintetic

### 10.1 De ce se rupe

Programul te lasă să mai faci o operațiune **după** ce ai dat închiderea de lună. Dacă nu
te întorci să refaci închiderea, apare o diferență între analitic și sintetic — care nu se
anunță singură.

### 10.2 Conturile la care se rupe cel mai des

**Banca.** Extrasul de cont trebuie să se potrivească cu balanța. Cazul tipic: jurnalul de
bancă dă cu extrasul, dar nu dă cu balanța — semn că diferența e între analitic și
sintetic, nu în operare.

**Clienții și furnizorii.** Nu se lasă solduri nealocate pe 4111 sau 401: denaturează și
fișa partenerului, și corelația analitic ↔ sintetic.

➕ Regula formatorului, repetată: **niciodată nu pleci fără analitic.** Chiar și acolo unde
pare inutil — 446 se ține pe `446.1` de la bun început, nu pe sintetic, pentru că a doua
taxă apare întotdeauna, iar despărțirea retroactivă e mult mai scumpă decât analiticul
făcut din prima.

### 10.3 Sumele nealocate și contul 473

Când o încasare nu se poate aloca înainte de închiderea lunii, se pune în **473**, cu
notiță despre proveniență:

```
473  = 4111       la închiderea lunii, dacă nu se știe alocarea
4111 = 473        luna următoare, la stornare și alocare corectă
```

➕ Importantul nu e contul, e **să fie într-un cont de care să-ți mai amintești**. Nu e o
problemă să stornezi luna viitoare și să pui pe clientul corect. Problema e să ratezi
alocarea cu totul.

### 10.4 Compensările 4091 ↔ 419

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

### 10.5 Preluarea unei balanțe în cursul anului

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

### 10.6 Cele trei verificări din softul formatorului

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

## 11. Ce s-a cerut pentru sesiunile următoare

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
