# Trezorerie: bancă, casă, efecte de încasat și avansuri
### Sursă: training 28.08.2026 — stările prin care trec banii între „am dreptul la ei” și „sunt în cont”

---

## Cum citești acest document

| Marcaj | Semnificație |
|---|---|
| ✅ | Notița originală era corectă — doar reformulată/completată |
| ⚠️ | **Eroare în notița originală** — corectată aici, cu explicație |
| ➕ | Completare (lucru care lipsea, dar era necesar ca raționamentul să stea în picioare) |
| ❓ | Rămas deschis — de clarificat cu formatorul (vezi Anexa D) |

---

## 1. Investiții pe termen scurt: acțiuni și obligațiuni
### 1.1 Achiziția de acțiuni


```
501 = 5121        achiziția acțiunilor
```

➕ **Analitic pe fiecare societate emitentă.** Dacă firma deține participații la mai
multe societăți, un 501 sintetic nu poate spune care participație s-a apreciat și care
s-a depreciat — iar ajustările pentru pierdere de valoare (591) se constituie pe fiecare
titlu, nu pe total.


### 1.2 Acțiuni vs. obligațiuni — ce cumperi de fapt


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
eventualele diferențe de curs dacă e în valută, formează rezultatul operațiunii. De aceea
ajustările pentru pierdere de valoare au conturi separate pe fiecare fel de titlu — 591
pentru acțiuni la afiliate, 595 pentru obligațiuni emise și răscumpărate, 596 pentru
obligațiuni, 598 pentru alte investiții.

## 2. Efecte de încasat: CEC-uri și bilete la ordin
### 2.1 De la factură la încasare


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


### 2.2 Scontarea biletului la ordin


Dacă biletul are scadență peste două luni, banca poate să-l **sconteze**: îți dă acum un
procent din valoare, și încasează ea efectul la scadență.

Pe biletul de **12.100 lei**, cu 80% avansat de bancă:

```
5114 = 5113       12.100     efectul pleacă spre scontare
5121 = 5114        9.680     lichiditatea primită, 80%
667  = 5114        2.420     costul scontării, restul de 20%
```

⚠️ Notița scria contul de cheltuială ca `6067`. Contul corect este **667 — „Cheltuieli
privind sconturile acordate”**. `6067` nu există în planul de conturi.

⚠️ Notița pornea de la „bilet la ordine de **12k** lei”, dar calcula 80% = 9,68k. 80% din
12.000 dă 9.600. Baza corectă e **12.100** — suma cu TVA din exemplul de mai sus.

➕ De ce trece prin 5114 și nu direct din 5113: mutarea spune că efectul **a plecat din
mâna ta**. Cât timp stă pe 5113, îl mai ai. Din 5114 se închide în trei direcții — bani,
cost, și zero rest — iar dacă rămâne sold acolo, scontarea nu s-a finalizat.

Contul 5114 se închide exact: 9.680 + 2.420 = 12.100.


### 2.3 Când merită scontarea și când nu


Scontarea e un instrument **scump** — cei 20% nu sunt dobândă la an, sunt costul
operațiunii. Banca o acordă societăților cu activitate îndelungată și clienți la fel; nu
e o facilitate pentru firme mici.

Rostul ei e altul decât costul: **contabilitatea românească e de angajamente.** Faci
factura, nu o încasezi, și statul cere TVA-ul și impozitul oricum. Societatea se poate
bloca având vânzări. Scontarea aduce lichiditatea mai devreme decât încasarea, iar analiza
băncii e mult mai rapidă decât la un credit clasic — pentru că se uită la efectul din
mână, nu la indicatorii tăi de profit.

## 3. Conturile la bănci
### 3.1 Conturile în valută și reevaluarea lunară


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


### 3.2 Diferențele de curs: 665/765 sau 668/768?


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


### 3.3 Dobânzi de plătit și de încasat


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


### 3.4 Linii de credit (5191) vs. credite cu scadențar (1621)


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

## 4. Tichete de masă și alte valori
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

## 5. Avansuri de trezorerie (542)
### 5.1 Monografia decontului


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


### 5.2 Diurna — partea care lipsea


Notița se opreşte la „part 3 din 3: 2.000 lei decontul = diurna”, fără înregistrare.

➕ Nu e o omisiune de transcriere: **diurna rupe tiparul primelor două.** Nu are furnizor
și nu are TVA de dedus — e o sumă cuvenită salariatului pentru deplasare. Deci nu trece
prin 401:

```
625 = 542         2.000     direct, fără furnizor și fără TVA
```

Decontul se închide exact: 2.000 + 1.000 + 2.000 = **5.000 lei**, cât s-a acordat.

❓ **Plafonul de deductibilitate al diurnei** nu era în notițe. Peste plafon, diurna se
asimilează salariului și se impozitează ca atare — deci cifra contează. De confirmat
nivelul în vigoare la data deplasării.


### 5.3 De ce analiticul e obligatoriu aici


Formatorul e categoric: **„542 pe analitic este esențial”**, cu patru semne de exclamare.

Motivul e că soldul poate merge în ambele sensuri, pe același cont, pe persoane diferite:
un șofer a pus bani de la el și firma îi datorează, altul a primit avans mai mare și
trebuie să restituie. Pe un 542 sintetic, cele două se anulează și soldul arată aproape
zero — corect ca total, fals pe fiecare om.

Partea asta e cea mai greu de ținut din toată trezoreria, și fiecare program de
contabilitate o tratează altfel.

## 6. Viramente interne (581)
### 6.1 Când 581 are voie să aibă sold


581 trebuie să ajungă la **zero**. Excepția legitimă: transferul făcut la sfârșitul lunii
și primit la începutul lunii următoare — atunci soldul e chiar realitatea, banii sunt pe
drum.


### 6.2 Diferența de curs la transferul valută → lei


⚠️ La transferul din valută în lei, diferența de curs **se reglează prin bancă, nu prin
581** — notițele subliniază cu șase semne de exclamare.

Motivul: 581 e un cont de **tranzit pur**, care trebuie să iasă cu exact cât a intrat.
Dacă diferența de curs se lasă acolo, contul nu se mai închide și devine imposibil de spus
dacă soldul rămas e un transfer în curs sau o diferență necontabilizată. Diferența
aparține contului de bancă în valută, unde s-a și produs.

---

## Anexa D — Rămase deschise

Ce e încă provizoriu în documentul ăsta. Lista nu e scrisă aici: vine din `date/intrebari.py`, aceeași sursă cu foaia „Întrebări deschise” a workbook-ului și cu lista trimisibilă formatorului.

**❓ Reevaluarea de sfârșit de lună a conturilor în valută se înregistrează pe 665/765 sau pe 668/768?**

*Trezorerie — diferențe de curs și plafoane · training 28.08.2026, punctul 1*

Notițele din 28.08 spun: diferențele de curs curente prin 665/765, iar reevaluarea de la sfârșitul lunii prin 668/768, cu observația „să fie clară diferența de curs din reevaluare, și cea de la furnizori”.

**Ce am presupus între timp:** Am păstrat 665/765 pentru ambele situații, cu analitic .DEC și .REV. Motivul: funcțiunea contului 665 din OMFP 1802/2014 include explicit diferențele rezultate „la sfârșitul lunii/exercițiului financiar, din evaluarea disponibilităților bancare și a numerarului în valută” — deci reevaluarea e chiar în funcțiunea lui. Iar 668/768 au alt rost: creanțele și datoriile exprimate în LEI, decontabile după cursul unei valute. Scopul formatorului — reevaluarea separată de decontare — se atinge cu analiticul, fără să mute reevaluarea în afara contului de diferențe de curs. Dacă formatorul confirmă varianta lui, se schimbă; dar atunci trebuie explicat cum se raportează diferențele de curs care nu mai sunt în contul lor.


---

## Anexa E — Baza legală citată

Extrasă automat din textul documentului: sunt listate actele și articolele care apar efectiv citate mai sus. Contextul fiecărei citări e în secțiunea unde apare.

**Acte normative citate**

- OMFP 1802/2014


---

*Clasa 5 avea, până la sursa asta, două fluxuri și două conturi de patru cifre în plan. Documentul e primul care o tratează ca teritoriu, nu ca anexă a altor subiecte.*
