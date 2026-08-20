# Control, documente și numerar
### Sursă: training 19.08.2026 — cum se citește un cont, ce cere legea de la un document și unde se rupe disciplina de casă

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


Contul **455** Sume datorate acționarilor/asociaților are restricții privind operațiunile în numerar: plățile din 455 prin casierie nu mai sunt permise în condițiile anterioare. Vezi secțiunea 13 — punct de verificat în textul legal în vigoare.

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

> Cifrele exacte au fost modificate prin Legea 296/2023. Înainte de a le aplica la un client, confirmă valorile în textul Legii 70/2015 în vigoare la data operațiunii — vezi secțiunea 13.

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

---

## Anexa B — Checklist practic

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

---

## Anexa E — Baza legală citată

Extrasă automat din textul documentului: sunt listate actele și articolele care apar efectiv citate mai sus. Contextul fiecărei citări e în secțiunea unde apare.

**Acte normative citate**

- Legea 70/2015
- Legea 296/2023
- Codul fiscal

**Articole citate**

art. 25 alin. (1), art. 319


---

*Singurul document care nu vine dintr-o zi de training proprie: e partea din 19.08.2026 care nu adâncea niciun subiect existent.*
