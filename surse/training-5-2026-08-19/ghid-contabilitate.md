# Ghid de contabilitate — mărfuri, TVA neexigibilă și clasa 4

*Material de studiu structurat pe baza notițelor de training din 19.08.2026.*

Convenție de notare folosită peste tot în ghid:

> `cont debitor = cont creditor · sumă`

---

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

## 2. Mărfuri la preț cu amănuntul (371)

Metoda prețului cu amănuntul: marfa stă în gestiune la **prețul de vânzare cu TVA**, nu la cost. Diferența dintre cost și prețul de raft se ține în două conturi **rectificative** ale lui 371:

- **378** Diferențe de preț la mărfuri (adaosul comercial)
- **4428** TVA neexigibilă

### 2.1 Achiziția

Cost de achiziție 20.000 lei, TVA 11%, adaos comercial 20%.

```
371  = 401    ·  20.000     (costul de achiziție)
4426 = 401    ·   2.200     (TVA deductibilă, 11% × 20.000)

371  = 378    ·   4.000     (adaos comercial, 20% × 20.000)
371  = 4428   ·   2.640     (TVA neexigibilă, 11% × 24.000)
```

Atenție la baza TVA-ului neexigibil: se aplică la **marfă + adaos** (20.000 + 4.000 = 24.000), nu doar la cost.

Soldul lui 371 devine **26.640** = 20.000 + 4.000 + 2.640, adică exact prețul de raft cu TVA.

### 2.2 Vânzarea prin casierie

```
5311 = 707    ·  24.000     (venitul din vânzarea mărfurilor)
5311 = 4427   ·   2.640     (TVA colectată)
```

### 2.3 Descărcarea de gestiune

Se scot cele trei componente cu care a intrat marfa:

```
607  = 371    ·  20.000     (cheltuiala — costul de achiziție, fără adaos)
378  = 371    ·   4.000     (anularea adaosului)
4428 = 371    ·   2.640     (TVA devine exigibilă)
```

Total scos din 371: 26.640 — gestiunea se închide exact.

În practică se face ca articol contabil compus: `% = 371 · 26.640`.

### 2.4 Închiderea TVA la sfârșitul lunii

Situația conturilor înainte de închidere:

- 4426 TVA deductibilă → **2.200** debitor
- 4427 TVA colectată → **2.640** creditor

```
4427 = 4426   ·   2.200     (se compensează partea comună)
4427 = 4423   ·     440     (diferența rămasă = TVA de plată)
```

Dacă deductibilul ar fi fost mai mare decât colectatul, diferența mergea invers, în **4424 TVA de recuperat**: `4424 = 4426`.

### 2.5 Plata TVA

```
4423 = 5121   ·     440
```

**5121** este contul de bancă, indiferent de instrumentul folosit (ordin de plată, internet banking, mandat). Nu confunda: **5311** este casa în lei, iar **5111** este *Cecuri de încasat* — un cont de **încasări**, care nu are ce căuta într-o plată de TVA.

Dacă ai TVA de recuperat din luna anterioară (sold debitor pe 4424) și TVA de plată în luna curentă, se pot compensa:

```
4423 = 4424
```

### 2.6 Închiderea conturilor de cheltuieli și venituri

```
121  = 607    ·  20.000
707  = 121    ·  24.000
```

Rezultatul contabil: 121 are sold **creditor de 4.000** lei — profitul pe care se calculează impozitul.

### 2.7 Impozitul pe profit

Cota este **16%**, aplicată la baza impozabilă. Cei 4.000 lei sunt **baza**, nu impozitul:

> 16% × 4.000 = **640 lei**

```
691  = 4411   ·     640     (cheltuiala cu impozitul pe profit)
121  = 691    ·     640     (închiderea contului de cheltuială)
```

Profitul net rămâne 4.000 − 640 = **3.360 lei**.

> Contul sintetic este **441** *Impozitul pe profit și alte impozite*; pentru impozitul pe profit se folosește analiticul **4411**.

---

## 3. Ajustări pentru deprecierea stocurilor

Când marfa se depreciază (expiră, se demodează, se degradează), deprecierea nu se estimează după ureche: se **întrunește o comisie tehnică**, se face inventarierea, iar procentul (20%, 15%, 50% — după caz) se stabilește de comun acord și ajunge în contabilitate printr-un **proces-verbal**.

Ajustarea se înregistrează la valoarea din gestiune / prețul de achiziție.

### 3.1 Înregistrarea deprecierii

Cost de achiziție 20 lei, depreciere stabilită 30% → 6 lei.

```
6814 = 391    ·       6     (cheltuiala cu ajustarea)
```

### 3.2 Reluarea la venituri, la valorificarea bunului

Vine un cumpărător și dă 10 lei pe bun. În momentul în care bunul iese din gestiune, ajustarea nu mai are obiect și **legea obligă la reluarea ei la venituri**:

```
391  = 7814   ·       6
```

Conturile de ajustare funcționează **în oglindă**: `6814 ↔ 7814`.

**Logica, pe scurt:** la vânzarea bunului din gestiune, ajustarea se mută de pe 39\* într-un cont de venit, ca să compenseze cheltuiala deja înregistrată în luna în care s-a constituit ajustarea. Efectul pe rezultat: −20 (descărcare) +10 (venit din vânzare) +6 (reluarea ajustării) = **−4 lei**.

### 3.3 Regimul fiscal — atenție

Ajustările pentru deprecierea **stocurilor** sunt **nedeductibile fiscal**. Art. 26 din Codul fiscal enumeră limitativ provizioanele și ajustările deductibile, iar deprecierea stocurilor nu se regăsește acolo.

Corespunzător, **venitul din reluarea lor este neimpozabil** (art. 23 lit. d — veniturile din anularea cheltuielilor pentru care nu s-a acordat deducere). Cele două se neutralizează fiscal.

Deductibile — condiționat — sunt ajustările pentru deprecierea **creanțelor** (491, 496), în limitele și condițiile art. 26. Nu confunda cele două regimuri.

### 3.4 Inventarierea — nota de practică

De partea de inventariere răspunde **administratorul**, deci e la latitudinea lui. Dar un economist bun punctează aceste lucruri clientului, indiferent de mărimea firmei: pentru fiecare proprietar, afacerea lui este cea mai importantă, iar clientul trebuie să simtă că ai un interes real față de business-ul lui.

---

## 4. Mecanica TVA

### 4.1 Conturile

| Cont | Denumire | Natură | Când apare |
|---|---|---|---|
| **4426** | TVA deductibilă | activ | la achiziții, pe baza facturii |
| **4427** | TVA colectată | pasiv | la livrări/prestări, pe baza facturii |
| **4423** | TVA de plată | pasiv | la închidere, dacă colectat > deductibil |
| **4424** | TVA de recuperat | activ | la închidere, dacă deductibil > colectat |
| **4428** | TVA neexigibilă | **bifuncțional** | aviz, facturi nesosite, mărfuri la preț cu amănuntul |

### 4.2 Taxarea inversă

La achiziții intracomunitare și la operațiunile supuse măsurilor de simplificare, TVA se auto-lichidează:

```
4426 = 4427
```

Efectul pe trezorerie este zero — se colectează și se deduce simultan.

**Nuanță importantă:** un **avans** plătit pentru o **achiziție intracomunitară de bunuri** nu generează exigibilitatea TVA. Faptul generator intervine la emiterea facturii sau cel târziu în a 15-a zi a lunii următoare livrării. La serviciile intracomunitare regula diferă.

### 4.3 De ce are 4428 nevoie de analitice

4428 este bifuncțional și apare în trei situații diferite, cu sensuri diferite:

| Situație | Înregistrare | Sensul lui 4428 |
|---|---|---|
| **Achiziție pe aviz** (facturi nesosite) | `4428 = 408` | **debitor** |
| **Livrare pe aviz** (facturi de întocmit) | `418 = 4428` | **creditor** |
| **Mărfuri la preț cu amănuntul** | `371 = 4428` | **creditor** |

Fără analitice distincte — pe fiecare situație **și pe fiecare cotă de TVA** — programul nu va ști să facă distincția la descărcarea de gestiune și va amesteca sumele.

Regula practică: **dacă firma are mărfuri și aprovizionare prin aviz, analiticele pe 4428 nu sunt opționale.**

Același raționament se aplică lui **408** și **418**: sunt bifuncționale și trebuie urmărite.

---

## 5. Furnizori — clasa 40

### 5.1 Contul 408 — Furnizori, facturi nesosite

Se folosește când **prestația s-a produs, dar factura nu a sosit** — tipic serviciile din decembrie facturate în ianuarie (principiul independenței exercițiului / *accrual*). La mărfuri și materii prime, echivalentul este intrarea **pe aviz**.

Legal, marfa livrată pe aviz poate fi facturată **până pe data de 15 a lunii următoare** celei în care a avut loc faptul generator.

**Recepție de materii prime pe aviz:**

```
301  = 408                  (în baza avizului)
```

Problema practică: de cele mai multe ori, **avizul nu conține prețul**. Legea nu obligă furnizorul să îl treacă. Ca să poți face înregistrarea la o valoare corectă, îți trebuie **contractul**. Dacă factura vine ulterior cu alt preț, se fac ajustări — sau, în practică, se convine un discount / se facturează la valoarea pusă pe 408.

**La primirea facturii:**

```
408  = 401                  (se închide provizionul de factură)
```

### 5.2 Varianta completă, cu TVA

Recepție în valoare de 10.000 lei, TVA 21%.

**Pasul 1 — la recepție, în baza avizului:**
```
231  = 408    ·  10.000
4428 = 408    ·   2.100     (TVA neexigibilă)
```

**Pasul 2 — la primirea facturii:**
```
408  = 401    ·  10.000
4426 = 401    ·   2.100     (TVA devine deductibilă)
```

**Pasul 3 — închiderea TVA-ului neexigibil:**
```
408  = 4428   ·   2.100
```

După pasul 3 atât 408, cât și 4428 rămân cu sold zero pe operațiunea respectivă. Pasul 3 este **corect și necesar** — fără el, cele două conturi rămân umflate reciproc.

Pentru 4428 provenit din 408 se folosesc **analitice distincte**.

> Notă: 231 este *Imobilizări corporale în curs*, iar furnizorul de imobilizări este **404**. Când se lucrează cu imobilizări, folosește analitice dedicate pe 408 sau direct 404, ca să nu amesteci furnizorii de exploatare cu cei de imobilizări.

### 5.3 De ce 408 este un cont periculos

Când livrezi cu aviz, legea cere ca **factura să menționeze numărul avizului**. Dacă cel care a întocmit factura nu a fost atent și factura nu se împerechează cu avizul — iar tu nu sesizezi — înregistrezi materii prime a doua oară și **dublezi gestiunea**.

Contabilitatea primește documente fără să aibă legătură cu ce se întâmplă pe teren. De aceea:

- trebuie să știi permanent **ce facturi sunt înregistrate pentru ce avize**;
- închiderea facturilor pe furnizori prin 408 se urmărește activ;
- la orice dubiu, se sună clientul. El știe cel mai bine ce se întâmplă în curtea lui și clarifică în câteva secunde ceea ce ție ți-ar lua ore.

### 5.4 Contul 409 — Furnizori-debitori (avansuri plătite)

| Cont | Pentru ce | Furnizor asociat |
|---|---|---|
| **4091** | avansuri pentru stocuri / mărfuri | 401 |
| **4092** | avansuri pentru prestări de servicii | 401 |
| **4093** | avansuri pentru imobilizări corporale | **404** |
| **4094** | avansuri pentru imobilizări necorporale | **404** |

**La plata avansului (factura de avans), 50.000 lei + TVA 21%:**

```
4091 = 401    ·  50.000
4426 = 401    ·  10.500
```

**La primirea facturii finale**, factura conține două poziții — stornarea avansului și produsele efectiv facturate:

```
4091 = 401    · −30.000     (storno avans, în roșu; parțial dacă avansul a fost parțial)
 ?   = 401                  (produsele/serviciile facturate)
```

Legea cere ca stornarea să se facă **și pe 4091, și pe 401** — pentru că efectul net trebuie să fie zero: 401 apare pe debit, 4091 pe credit, se anulează reciproc.

Factura finală poate avea sold zero sau orice sold, în funcție de cât a acoperit avansul.

**Avansurile în valută:** pe avansuri **nu** se calculează diferențe de curs valutar. Stornarea avansului se face la **cursul de la data înregistrării avansului**. Avansurile sunt elemente nemonetare și nu se reevaluează.

### 5.5 Regula generală pe clasa 40

La toate înregistrările care țin de furnizori (40\*) avem **TVA deductibilă (4426)** — și putem avea și **taxare inversă**.

---

## 6. Clienți — clasa 41

### 6.1 Contul 411 și legătura cu veniturile

411 intră în legătură fie cu conturi de **venituri (70\*)**, fie cu **venituri în avans (472)**.

**Care e diferența?**

| | **70\*** Venituri | **472** Venituri în avans | **419** Clienți-creditori |
|---|---|---|---|
| Natură | cont de venit | **pasiv** (datorie) | **pasiv** (datorie) |
| Când | prestația **este** realizată, în perioada curentă | sumă facturată/încasată care privește **perioade viitoare** | **avans** încasat **înainte** de livrare/prestare |
| Exemplu | vânzare de marfă în luna curentă | chirie încasată anticipat pe 12 luni, abonamente | 30% avans la o lucrare care nu a început |
| Cum dispare | se închide la 121 | `472 = 70*` pe măsura trecerii timpului | se stornează la factura finală |
| TVA | colectată la faptul generator | urmează regulile de exigibilitate | **colectată la încasarea avansului** |

Conturi **în oglindă**:
- `409` (furnizori-debitori) ↔ `419` (clienți-creditori)
- `471` (cheltuieli în avans) ↔ `472` (venituri în avans)

O cheltuială financiară care se întinde pe 2 ani se înregistrează pe **471** și se reia eșalonat.

### 6.2 Contul 418 — Clienți, facturi de întocmit

Oglinda lui 408, pentru situația în care **noi** livrăm marfă pe aviz.

**La livrarea pe aviz** — marfă de 10.000 lei, TVA 21%:

```
418  = 707    ·  10.000     (venitul)
418  = 4428   ·   2.100     (TVA neexigibilă)
```

Creanța totală pe 418 este **12.100** lei.

**La emiterea facturii finale:**

```
4111 = 418    ·  12.100     (creanța trece pe client)
4428 = 4427   ·   2.100     (TVA devine exigibilă)
```

Observă sensul: TVA-ul **iese** din 4428 (care era creditor) și **intră** în 4427. Nu invers.

După aceste înregistrări, 418 și 4428 rămân cu sold zero pe operațiune, iar creanța reală de încasat este 12.100 lei pe 4111.

### 6.3 Avans încasat de la client

Lucrare de 100.000 lei, avans 30%, TVA 21%.

**La încasarea avansului:**
```
4111 = 419    ·  30.000
4111 = 4427   ·   6.300     (TVA se colectează la avans)
```

**La livrarea produsului finit — storno avans:**
```
4111 = 419    · −30.000
4111 = 4427   ·  −6.300
```

**Produsul finit facturat:**
```
4111 = 7015   · 100.000
4111 = 4427   ·  21.000
```

**Factura finală de încasat:** 121.000 − 36.300 = **84.700 lei**.

```
5121 = 4111   ·  84.700     (încasarea prin bancă)
```

---

## 7. Operațiuni speciale

### 7.1 Vânzarea unui mijloc fix

Preț de vânzare 60.000 lei, TVA 21%.

**Facturarea:**
```
4111 = 7583   ·  60.000     (venituri din vânzarea activelor)
4111 = 4427   ·  12.600
```

Raționamentul de control: conturile de clasa 6 stau pe **debit**, cele de clasa 7 stau pe **credit**. Deci contul de venit (7583) merge pe credit, iar clientul (4111) pe debit. TVA-ul colectat, fiind un cont de pasiv care crește, merge tot pe **credit**.

**Scoaterea din evidență a mijlocului fix** — pasul pe care nu trebuie să-l uiți. Presupunem valoare de intrare 50.000, amortizare cumulată 38.000:

```
2813 = 213    ·  38.000     (amortizarea cumulată)
6583 = 213    ·  12.000     (valoarea rămasă neamortizată)
```

**Închiderea TVA colectată** (dacă nu există deductibil în luna respectivă):
```
4427 = 4423   ·  12.600
```

### 7.2 Prețul din contract fără mențiune de TVA

Când un contract menționează sec o sumă — „100.000 lei", punct, fără nicio precizare — acea sumă se consideră că este **cu tot cu TVA**.

De aceea este esențial ca în contract să se menționeze explicit: prețul **cu sau fără TVA**, și tranșele în care se primesc banii.

Principiul este consacrat de jurisprudența CJUE (cauzele conexate C-249/12 și C-250/12, *Tulică și Plavoșin*).

### 7.3 Încasare mai mare decât factura

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

### 7.4 Note despre 455

Contul **455** Sume datorate acționarilor/asociaților are restricții privind operațiunile în numerar: plățile din 455 prin casierie nu mai sunt permise în condițiile anterioare. Vezi secțiunea 13 — punct de verificat în textul legal în vigoare.

---

## 8. Numerar și plafoane (Legea 70/2015)

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

> Cifrele exacte au fost modificate prin Legea 296/2023. Înainte de a le aplica la un client, confirmă valorile în textul Legii 70/2015 în vigoare la data operațiunii — vezi secțiunea 13.

---

## 9. Documente, contracte și riscuri la control

### 9.1 „Prestări servicii conform contract"

Când pe documentul de intrare scrie doar atât, ai o problemă: legea obligă la descrierea **naturii serviciului prestat** (art. 319 Cod fiscal — denumirea și cantitatea bunurilor livrate, denumirea serviciilor prestate).

Prestările de servicii sunt foarte diverse, iar încadrarea contează:
- dacă factura menționează **numărul contractului**, ești norocos — te uiți în contract;
- o factură de 628 de 100.000 lei cere o cu totul altă abordare decât una de 500 lei;
- cazul fericit: servicii de arhitectură / proiectare → nu e cheltuială, e **imobilizare în curs**.

### 9.2 Contractul la prestările de servicii

La prestări de servicii trebuie să existe **contract**. Factura este documentul fiscal; contractul detaliază **cum interacționezi cu partenerul**.

> Nuanță: cerința expresă de a avea contract pentru servicii de management și consultanță, din vechiul Cod fiscal, a fost abrogată. Codul fiscal actual (art. 25 alin. 1) cere ca o cheltuială să fie efectuată **în scopul desfășurării activității economice** și susținută cu documente justificative. Contractul rămâne principalul mijloc de probă la control — deci, practic, indispensabil.

### 9.3 Cazul penalităților — de reținut

O firmă de construcții a avut contract de livrare cu un client. Clientul nu a mai achitat. În contract, la capitolul penalități, erau trecute sume foarte mari — pe care firma nu le-a mai facturat și nu le-a trecut la venituri.

ANAF a constatat că firma **nu și-a respectat propriul contract**, a calculat venituri și majorări pentru soldurile neîncasate, iar firma a rămas și fără venit, și cu bani dați la stat.

**Concluzie:** în contracte se trec **penalități realiste**. O clauză de penalitate exagerată nu te protejează — te expune.

### 9.4 Sistemele informatice

Programele au ecrane cu o structură în spate care generează notele contabile fără ca tu să le vezi. Dacă ceva pare suspect, instrumentul de verificare este **fișa de cont**. Nu te baza pe faptul că softul „știe" — mai ales pe conturile bifuncționale.

---

## 10. Conturi de urmărit periodic

Răspuns la întrebarea din notițe: care sunt conturile care trebuie urmărite cel puțin trimestrial, dacă nu lunar.

### Lunar — obligatoriu

| Cont | De ce |
|---|---|
| **4426 / 4427 / 4423 / 4424** | închiderea TVA; orice sold rămas e o eroare |
| **4428** | bifuncțional; trebuie să se golească pe operațiunile facturate |
| **408 / 418** | bifuncționale; risc de dublare a gestiunii |
| **471 / 472** | reluarea eșalonată trebuie făcută lună de lună |
| **473** Decontări din operațiuni în curs de clarificare | trebuie să ajungă la **sold zero**; altfel ascunde erori |
| **581** Viramente interne | trebuie să aibă **sold zero**; sold ≠ 0 = transfer neînchis |
| **5311 / 5121** | reconciliere cu extrasul și cu registrul de casă |
| **542** Avansuri de trezorerie | deconturi nejustificate |

### Cel puțin trimestrial

| Cont | De ce |
|---|---|
| **4091 – 4094** | avansuri care nu s-au stornat la factura finală |
| **419** | avansuri de la clienți rămase deschise |
| **401 / 411** | balanță analitică; **solduri cu semn contrar** = eroare |
| **455** | sume datorate asociaților, cu restricții legale |
| **461 / 462** | debitori/creditori diverși, se împotmolesc ușor |
| **231** | imobilizări în curs care trebuiau puse în funcțiune |
| **1621 / 5187** | credite și dobânzi de calculat |

---

## 11. Tabel recapitulativ de conturi

| Cont | Denumire | Natură |
|---|---|---|
| 121 | Profit sau pierdere | bifuncțional |
| 213 | Instalații tehnice și mijloace de transport | activ |
| 231 | Imobilizări corporale în curs | activ |
| 2813 | Amortizarea instalațiilor și mijloacelor de transport | rectificativ pasiv |
| 301 | Materii prime | activ |
| 371 | Mărfuri | activ |
| 378 | Diferențe de preț la mărfuri (adaos) | rectificativ |
| 391 | Ajustări pentru deprecierea mărfurilor | rectificativ |
| 401 | Furnizori | pasiv |
| 404 | Furnizori de imobilizări | pasiv |
| 408 | Furnizori — facturi nesosite | **bifuncțional** |
| 4091‑4094 | Furnizori-debitori (avansuri plătite) | activ |
| 4111 | Clienți | activ |
| 418 | Clienți — facturi de întocmit | **bifuncțional** |
| 419 | Clienți-creditori (avansuri încasate) | pasiv |
| 4411 | Impozitul pe profit | pasiv |
| 4423 | TVA de plată | pasiv |
| 4424 | TVA de recuperat | activ |
| 4426 | TVA deductibilă | activ |
| 4427 | TVA colectată | pasiv |
| 4428 | TVA neexigibilă | **bifuncțional** |
| 455 | Sume datorate acționarilor/asociaților | pasiv |
| 471 | Cheltuieli înregistrate în avans | activ |
| 472 | Venituri înregistrate în avans | pasiv |
| 473 | Decontări din operațiuni în curs de clarificare | **bifuncțional** |
| 491 | Ajustări pentru deprecierea creanțelor-clienți | rectificativ |
| 5121 | Conturi la bănci în lei | activ |
| 5311 | Casa în lei | activ |
| 581 | Viramente interne | bifuncțional |
| 607 | Cheltuieli privind mărfurile | cheltuială |
| 628 | Alte cheltuieli cu serviciile executate de terți | cheltuială |
| 6583 | Cheltuieli privind activele cedate | cheltuială |
| 6814 | Cheltuieli de exploatare privind ajustările pentru deprecierea activelor circulante | cheltuială |
| 691 | Cheltuieli cu impozitul pe profit | cheltuială |
| 701 / 7015 | Venituri din vânzarea produselor finite | venit |
| 707 | Venituri din vânzarea mărfurilor | venit |
| 7583 | Venituri din vânzarea activelor și alte operațiuni de capital | venit |
| 7814 | Venituri din ajustări pentru deprecierea activelor circulante | venit |

---

## 12. Erori frecvente și capcane

1. **Confuzia 5121 / 5311 / 5111.** 5121 = bancă, 5311 = casa în lei, 5111 = *cecuri de încasat*. Orice plată bancară — inclusiv prin ordin de plată — trece prin **5121**.

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

## 13. De verificat și de testat

Puncte rămase deschise, de confirmat înainte de a le aplica la un client:

1. **Plafoanele de numerar** — valorile exacte din Legea 70/2015, așa cum a fost modificată prin Legea 296/2023, la data operațiunii.
2. **Restricțiile pe contul 455** — care sunt exact operațiunile în numerar interzise și temeiul legal.
3. **Simulare în softul de contabilitate** pentru cazul încasării în plus (7.3): de verificat dacă programul extrage automat TVA-ul pe diferența trecută la 419, sau dacă trebuie forțat manual. De contraverificat 4427 după simulare.
4. **Analiticele pe 4428** — de configurat pe fiecare situație (aviz intrare / aviz ieșire / mărfuri) **și** pe fiecare cotă de TVA, înainte de a începe operarea.
5. **Contul folosit pentru facturi nesosite la imobilizări** — 408 cu analitic sau 404 cu analitic; de stabilit convenția și de respectat consecvent.
