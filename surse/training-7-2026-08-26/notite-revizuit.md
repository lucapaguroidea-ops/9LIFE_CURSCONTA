# Subvenții, dividende și conturile care devin coșuri — notițe training 26.08.2026

*Versiune revizuită. Sursa: notițele brute din 26.08.2026.*

## 1. Subvenții pentru investiții și fonduri europene

### 1.1 Corespondența 445 ↔ 475

Grupa 445 ține **creanța** față de finanțator; grupa 475 ține **venitul amânat** care
urmează să fie recunoscut pe măsura amortizării. Se folosesc în pereche:

| Creanță | Venit amânat | Ce finanțează |
|---|---|---|
| 4451 | 4751 | Subvenții guvernamentale pentru investiții |
| 4452 | 4752 | Împrumuturi nerambursabile cu caracter de subvenții |
| 4458 | 4753 / 4754 / 4758 | Alte sume primite cu caracter de subvenții |

➕ Corespondența nu e mnemotehnică: fiecare pereche păstrează separat *de la cine ai de
primit* și *cât din venit nu ți se cuvine încă*. Confundate, subvenția ajunge venit în
luna încasării, ceea ce umflă rezultatul cu bani care acoperă o cheltuială viitoare.

### 1.2 Când se înregistrează un proiect european

Un proiect pe fonduri europene se înregistrează în contabilitate **când primesc
aprobarea de la autoritate** — nu când primesc banii, nu la semnarea contractului de
consultanță.

⚠️ Momentul contează: creanța și venitul amânat se nasc la aprobare. Înregistrat la
încasare, tot mecanismul de reluare la venit pornește cu întârziere, iar corelația dintre
amortizare și venit se rupe pentru lunile dintre aprobare și încasare.

### 1.3 Aportul propriu și TVA-ul nedecontat

Societatea vine cu un **aport de 10 / 20 / 30 %**, în funcție de proiect și de ramura în
care se încadrează. Restul e subvenție.

Valorile din proiect sunt **fără TVA**: TVA-ul nu se decontează și nu face parte dintr-un
proiect european.

Exemplu: proiect de **100.000 lei**, subvenție **80 %**.

```
4452 = 4758        80.000     creanța și venitul amânat, la aprobare
5121 = 4452        80.000     încasarea fondurilor
```

➕ Între cele două înregistrări, creanța poate sta „latentă" oricât: nimic nu se reia la
venit până nu apare prima cheltuială cu activul finanțat.

### 1.4 Amortizarea și reluarea la venit merg împreună

Aici e tot rostul mecanismului. Clădirea din proiect se amortizează pe 40 de ani:

```
100.000 ÷ 40 ani ÷ 12 luni = 208,33 lei amortizare lunară
```

În aceeași lună, subvenția se reia la venit **în cota de finanțare**:

```
208,33 × 80 % = 166,67 lei
```

Nota lunară, cu ambele jumătăți la vedere:

```
6811 = 2812       208,33     cheltuiala cu amortizarea, pe toată valoarea
4758 = 7584       166,67     reluarea subvenției, doar pe cota finanțată
```

Efectul net pe rezultat e **41,66 lei pe lună** — adică exact amortizarea aportului
propriu (20 % × 208,33). Timp de 40 de ani: cheltuială, venit, cheltuială, venit.

⚠️ Notița scria reluarea ca **166,40**, calculată pe amortizarea rotunjită (208 × 80 %).
Cifra corectă e 166,67, pe amortizarea reală de 208,33. Diferența e mică lunar, dar
sistematică: pe 480 de luni se acumulează.

➕ Concluzia formatorului, formulată ca regulă de verificare: **dacă am o cheltuială din
proiect, trebuie să am și un venit în aceeași lună.** O lună cu amortizare și fără
reluare e o eroare, nu o opțiune.

### 1.5 Plusuri la inventar la imobilizări

Un plus constatat la inventar la imobilizări se înregistrează tot prin grupa venitului
amânat, nu direct la venit:

```
4458 = 4754
```

Motivul e același: o imobilizare are drept cheltuială **amortizarea**, iar venitul
trebuie să apară în același ritm. Recunoașterea imediată la venit ar concentra într-o
lună un venit care acoperă o cheltuială întinsă pe toată durata de viață.

❓ Notița indică `7584 / 7588` fără să tranșeze care se folosește la plusul de inventar.
Cele două nu sunt echivalente: 7584 e „venituri din subvenții pentru investiții", 7588 e
„alte venituri din exploatare". Presupun **7584**, prin simetrie cu 475x, dar rămâne de
confirmat.

## 2. Dividende

### 2.1 Analiticele pe 1012 — cotele de participare

**1012 se ține pe analitic, pe asociat**, iar denumirea analiticului poartă procentul:

```
1012.1 = Ionescu 33,3 %
1012.2 = Popescu 33,3 %
1012.3 = Xulescu 33,3 %
```

➕ Rostul: balanța trebuie să vorbească de la sine. Când vine hotărârea AGA, verifici
direct în balanță ce cotă are fiecare, fără să deschizi actul constitutiv.

La o firmă nouă cu 1012 „la grămadă", cota de participare se ia de la ONRC și se creează
analiticele.

⚠️ Cazuri ajunse la comisia de disciplină la ANAF — la fuziuni și cedări de părți sociale
— pentru că experții contabili nu obținuseră procentele pe analitice. Consecința nu e doar
a firmei: afectează și persoana în cauză, la ce poate ridica din societate.

### 2.2 Hotărârea AGA e documentul de bază

Documentul de bază pentru distribuirea dividendelor este **hotărârea AGA**, întocmită
statutar și semnată. Repartizarea se face în funcție de participarea la capitalul social.

⚠️ **Nu se înregistrează dividende fără hotărârea AGA.** Formatorul citează cazuri de
experți contabili ajunși la comisia de disciplină exact pentru asta.

Ordinea de lucru: se ia balanța de la început, se verifică în 1012 cota fiecăruia, apoi
se contraverifică ce scrie în AGA.

### 2.3 Dividende certe din rezultatul reportat

Contul **1171** ține profitul nerepartizat din anii anteriori, pe analitic **pe an**.
Poate avea sold debitor (pierdere) sau creditor (profit).

Repartizarea a câte 10.000 lei către trei asociați:

```
1171 = 457.1      10.000
1171 = 457.2      10.000
1171 = 457.3      10.000
```

**457** se ține pe analitic pe persoană, conform procentelor din 1012.

Cele două feluri de dividende:

| Tip | Cont | Când |
|---|---|---|
| Interimare | 456 | distribuite în cursul anului curent |
| Certe | 457 | repartizate din rezultatul unui exercițiu încheiat |

### 2.4 Impozitul pe dividende

Cota este **16 %**. Dacă firma alege să plătească impozitul înainte de ridicare:

```
457.1 = 446       1.600      16 % × 10.000
457.2 = 446       1.600
457.3 = 446       1.600
```

Rămâne pe fiecare analitic de 457 un rest de plată de **8.400 lei**.

Plățile:

```
457.1 = 5121      8.400      dividendul net
446   = 5121      1.600      impozitul
```

### 2.5 Declarațiile: D100, D205, Declarația Unică

- **D100** — ori de câte ori am impozit de plată. La completare, atenție la distincția
  persoane fizice / persoane juridice: există rubrică separată pentru impozitul pe
  dividende la persoane fizice.
- **D205** — declarație informativă, o dată pe an, cumulativ. Acoperă și alte surse
  (chirii, dividende), cu două rubrici distincte: **dividende distribuite** și
  **dividende ridicate**.
- **Declarația Unică** — la dividendele **ridicate** se plătește sănătate, nu la cele
  distribuite. ❓

**Termenul care surprinde:** impozitul pe dividende se plătește cel târziu la **25.01 a
anului următor repartizării, chiar dacă dividendele nu au fost ridicate.** Obligația e
față de buget, nu față de asociat.

➕ **Verificarea încrucișată:** D205 trebuie corelat cu D100. La întocmire se cere fișa
pe plătitor (sau fișa simplificată) și se confruntă cu fișa contului 446 din balanță —
cazul care se caută e o plată făcută fără declarație.

### 2.6 Dividende interimare — contul 463

Dividendele interimare se distribuie **din profitul anului curent**, tot în baza AGA, dar
legea cere în plus **inventariere** și **bilanț interimar**. Se acordă doar trimestrial.

Exemplu: la iulie, după închiderea a 6 luni și după înregistrarea impozitului, soldul lui
121 e **80.000 lei**. Administratorul vrea să ridice 100.000 — nu poate: plafonul e
profitul realizat.

```
463 = 456        80.000      maximul e soldul contului 121
456 = 446        12.800      impozitul, 16 %
456 = 5121       67.200      plata către administrator
```

➕ Din 100.000 pe care îi vedea în bancă, ajunge să ridice 67.200.

**Calendarul, care nu e intuitiv:** hotărârea AGA se face în **iulie** (are nevoie de
balanța închisă), dar înregistrarea contabilă se face în **iunie**, luna bilanțului
interimar — pentru că bilanțul interimar are rubrică separată pentru 463, deci ANAF vede
ce s-a repartizat interimar. Bilanțul se depune până la **31 iulie**.

### 2.7 Regularizarea la 31.12 și rectificativa D710

Contul 463 rămâne cu sold debitor până la închiderea anului. Atunci se compară cu 121:

Dacă profitul final e mai mic — să zicem **70.000** față de 80.000 repartizați:

```
463 = 456       −10.000      storno, pentru diferența nerealizată
456 = 446         1.600      storno impozit, 16 % × 10.000
```

Se depune **rectificativă la D100 — formularul D710** — în care apare suma plătită
inițial și suma corectată. Rămâne plătit în plus la ANAF, sumă pentru care se poate face
cerere de compensare sau de restituire. Iar asociatul trebuie să aducă banii înapoi.

În anul următor, la AGA:

```
121  = 1171      70.000      rezultatul trece la reportat
1171 = 463       70.000      se soldează dividendele interimare
```

⚠️ Notița scria stornarea ca `453 - 456`. Contul este **463**; 453 nu are legătură cu
dividendele.

➕ **Concluzia practică:** la dividendele interimare trebuie mers în limita lui 121 și,
în practică, sub ea — nu se știe ce prognoză există până la sfârșitul anului. Corecția e
un proces lung, cu bani care trebuie dați înapoi.

**Condiție prealabilă:** nu se pot acorda dividende, nici interimare, nici certe, dacă
există pierderi din anii anteriori neacoperite (sold debitor pe 1171).

## 3. Creditarea de societate și relațiile cu asociații

### 3.1 Contul 455 — reguli de fier

**455 este cont de pasiv și trebuie să apară doar pe credit.** Un sold debitor înseamnă
ori înregistrare greșită, ori că asociatul a ridicat mai mulți bani decât a pus.

```
5121 = 4551       încasez creditarea
4551 = 5121       restitui
```

Regulile pe care formatorul le repetă:

- **Contract pentru fiecare creditare.** Nu trebuie să fie complicat, dar trebuie să
  existe — înregistrarea din bancă nu e suficientă. Se poate genera din softul de
  contabilitate și doar semnat. Alternativ, un contract pe lună, pe totalul fișei.
- **Analitic pe fiecare asociat.** Trei asociați, trei analitice de 455.
- **Nu se compensează între asociați.** Creditarea unui asociat nu poate stinge ridicarea
  altuia, decât cu o înțelegere notarială — nu pe cuvânt și nu pe mesaj.
- **Se ajunge la sold 0.**

➕ 455 funcționează ca 451, dar pe persoană fizică, nu între entități.

⚠️ Administratorul nu ține minte cât a creditat și cât a ridicat. De aceea contul se
urmărește pe analitic, în ambele sensuri — altfel se descoperă târziu și greu.

### 3.2 Majorarea capitalului social din creditare

Creditarea se poate transforma în capital social:

```
455.1 = 456       5.000      capital subscris nevărsat
456   = 1011      5.000      constituirea capitalului
1011  = 1012      5.000      după înregistrarea la ONRC
```

Cele două înregistrări se fac în baza a două documente: **hotărârea AGA** și **expertiza
contabilă**, care atestă că sumele sunt *certe, lichide și exigibile* — adică au existat
în realitate, au fost virate și există contract.

➕ Distincția pe care formatorul o subliniază: **acționarii** creditează societatea,
**asociații** constituie capitalul social.

### 3.3 Remiterea de datorie

Societățile ajunse în impas primesc uneori sugestia de a renunța la creditare. Actul se
numește **remitere de datorie** și se face **prin notariat**, în baza acelorași două
documente (AGA + expertiză contabilă).

```
4551 = 7582       suma la care se renunță devine venit
7582 = 121        se închide în rezultat
```

Exemplu: pierdere de 100.000, renunțare la creditare de 120.000 → profit de 20.000.

⚠️ Profitul rezultat **nu e din exploatare**. Din două înregistrări societatea trece pe
profit, dar natura lui trebuie citită corect la analiza rezultatului.

### 3.4 Decontări între entități afiliate — 451

Entități afiliate = cele cu **peste 25 % acționari comuni**. Împrumuturile între ele se
fac pe bază de contract, iar înregistrările sunt **în oglindă** la cele două societăți.

### 3.5 Operațiuni în participație — 458

Două sau mai multe societăți încheie un **contract de participațiune** pentru un obiectiv
comun: una vine cu utilajele, alta cu angajații. O parte din venituri și cheltuieli se
transferă între ele, astfel încât fiecare să plătească impozit pe profit **doar pe
activitatea proprie**.

458 e contul de decontare al acestor transferuri.

## 4. Conturile care țin rulajele curate

### 4.1 Taxele locale prin 446, nu direct pe cheltuială

```
446 = 5121                  plata taxei
471 = 446                   dacă acoperă o perioadă mai lungă
635 = 471                   eșalonat, pe luni
635 = 446                   direct, dacă suma e mică
```

➕ Rostul lui 446 ca punct de trecere: taxa plătită anticipat pentru un an întreg nu e
cheltuiala lunii în care s-a plătit. Pentru sume mici nu merită mecanismul cu 471.

### 4.2 Contul 4481 — datorii din acte de control

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

### 4.3 Contul 4482 — plăți eronate către buget

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

### 4.4 Conturile 461 / 462 — coșul firmei

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

## 5. Verificarea care încheie ședința

Regula generală, formulată de formator ca temă: **să verificăm activul și pasivul —
conturile care stau pe invers.** Un cont de activ cu sold creditor sau un cont de pasiv
cu sold debitor nu e o curiozitate de balanță; e o eroare care încă n-a fost căutată.

Conturile din ședința asta care se verifică așa: 455 (niciodată debitor), 461/462, 4482,
463 față de 121.

➕ Tema dată: identificarea în balanță a lucrurilor care pot fi rezolvate — pentru că, o
dată ce li se stabilește cursul, nu mai sunt erori.
