# Salarii, contribuții și rețineri — notițe training 21.08.2026

*Versiune revizuită. Sursa: notițele brute din 21.08.2026.*

## 1. Înainte de înregistrare: de unde vine statul de plată

Contabilitatea primește statul de plată gata făcut. Asta e și riscul: dacă statul e
greșit, nota contabilă e greșită, iar eroarea se vede abia la control.

### 1.1 Salariul minim și norma parțială

Salariul minim brut pe economie este **4.325 lei** ❓. Verificarea care se face lunar,
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

❓ Tratamentul exact al reținerilor din indemnizația de concediu medical — ce contribuții
se datorează și pe ce parte — nu era în notițe și nu îl afirm aici.

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

❓ Limita de o treime se aplică datoriilor obișnuite; pentru obligații de întreținere
legea prevede o limită mai mare. Procentul aplicabil pe caz concret — de confirmat.

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

## 6. Impozit pe profit sau impozit pe venit

### 6.1 Impozitul pe profit

Cota este 16%, aplicată la baza impozabilă:

```
691  = 441                  (cheltuiala cu impozitul pe profit)
```

### 6.2 Condițiile pentru microîntreprindere

Ambele trebuie îndeplinite:

1. **cel puțin un salariat cu normă întreagă** — sau un contract de mandat, obligatoriu
   cel puțin la nivelul salariului minim. Contractul de mandat se încheie prin avocat și
   **nu se înregistrează în REGES**;
2. **venituri totale sub 100.000 EUR** ❓, calculate la cursul de la închiderea
   exercițiului anterior. Pragul e din Codul fiscal, nu din OMFP.

Cota este 1% ❓.

```
698  = 4418                 (impozitul pe venitul microîntreprinderii)
```

⚠️ **Notița scria `6918`.** Contul nu există. Corect este **698**, „Cheltuieli cu
impozitul pe venit și cu alte impozite care nu apar în elementele de mai sus”. Nu poate
fi un analitic al lui 691: 691 este impozit pe **profit**, iar microul e impozit pe
**venit** — ar fi o clasificare greșită, nu doar o notație.

### 6.3 Depășirea pragului

Dacă în cursul anului veniturile depășesc pragul, societatea devine plătitoare de impozit
pe profit **începând cu trimestrul în care s-a depășit**, nu cu următorul.

➕ Consecința practică: clientul care se apropie de prag trebuie anunțat înainte, nu
după. Declarațiile devin **D100 trimestrial** și **D101 anual**.

### 6.4 Ce sold trebuie să aibă

**441** (impozit pe profit) și **4418** (impozit pe venit) sunt conturi de pasiv, deci
soldul lor normal este **creditor**. Un sold debitor înseamnă că s-a plătit mai mult
decât se datorează — de verificat, nu de ignorat.

---

## 7. Decontul de TVA și D300

### 7.1 Decontul nu are variantă rectificativă

Decontul de TVA este **singura declarație care nu se rectifică**. Corecțiile se fac pe
rândurile de **regularizări** ale decontului următor.

Consecința: facturile înregistrate **după** depunerea decontului nu mai pot fi „puse la
locul lor” retroactiv — decontul nu se mai potrivește cu balanța până la regularizare.

### 7.2 Regularizări — cazul cotei schimbate

Avansuri primite și stornate cu **19%**, iar factura finală emisă cu **21%**. Diferența
nu mai poate fi corectată prin decont de corecții materiale — se înscrie pe rândurile de
regularizări.

### 7.3 Deciziile de impunere ANAF

Sumele stabilite de ANAF prin decizie de impunere la control **nu se trec niciodată în
decont**. Ele se înregistrează în **4423 cu analitic distinct**, tocmai ca să nu ajungă
din greșeală în decontul lunii următoare.

➕ Analiticul nu e o preferință de organizare: e singurul lucru care împiedică o eroare
care altfel se face singură.

### 7.4 Corelația cu fișa de rol

Fișa de rol nu preia soldul decontului, ci **rulajul lunii** — suma de plată sau de
rambursat a lunii respective.

❓ Notițele indică rânduri diferite în două locuri: un pasaj spune rândurile 36 și 37,
altul rândurile 44 și 45. Numerele de rând se schimbă între versiunile formularului, iar
cele două afirmații nu pot fi ambele adevărate.

Greșeala întâlnită în practică: ANAF încarcă doar suma lunii, iar cine completează
decontul uită **TVA-ul neachitat din perioadele precedente**. La finanțe soldul pare în
regulă, dar decontul e greșit.

### 7.5 Corelația sfântă a TVA-ului

> **soldul din decontul de TVA = soldul din balanță**

Pe **sold**, nu pe rulajul lunii. La rambursare, atenția se duce pe **soldul cu care
pleci**: dacă el e greșit, tot ce urmează e greșit.

❓ **Temă lăsată de formator:** corelațiile complete între D300 și fișa de rol la TVA.

---

## 8. Răspunsuri la întrebările din notițe

Întrebările de mai jos erau notate în text ca lucruri de lămurit. Nu sunt întrebări
pentru formator — sunt lucruri care se pot răspunde din logica înregistrării.

### 8.1 Cum se leagă rulajul debit/credit cu soldul, la 421 și 423

Rulajul este **mișcarea perioadei**; soldul este **ce a rămas**. Pe un cont de pasiv:

> sold creditor final = sold inițial + rulaj creditor − rulaj debitor

La 421, rulajul creditor al lunii este brutul datorat, iar rulajul debitor conține
reținerile și plata. Ce rămâne pe credit este exact ce mai ai de dat — deci se compară cu
restul de plată de pe stat.

Diferența față de regula „rulaj = sold” de la 444 sau 436 este că acolo soldul inițial e
zero la începutul fiecărei luni, pentru că obligația lunii precedente s-a stins. La 421,
dacă soldul inițial nu e zero, ai deja o restanță din trecut — și corelația îți spune
asta înainte să o caute altcineva.

### 8.2 De ce creanța față de un fost salariat e cont de activ

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

### 8.3 De ce nu trebuie solduri creditoare pe conturi de activ

Pentru că ar afirma ceva imposibil: „am o creanță negativă”. În practică înseamnă
întotdeauna una din trei — s-a înregistrat pe partea greșită, s-a încasat de două ori,
sau s-a încasat ceva ce nu era înregistrat ca datorat.

Bilanțul prezintă activele pe o parte și pasivele pe alta. Un activ cu sold creditor ori
se prezintă greșit, ori trebuie reclasificat ca datorie — și atunci nu mai e ce spune
numele contului.

### 8.4 Ce alte corelații se pot face din balanță

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

## 9. Checklist lunar rezultat din notițe

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

## 10. Lista erorilor corectate din notițe

| Notița | Corect | Unde |
|---|---|---|
| `436 - 646` pentru CAM | `646 = 436` | 2.2 |
| `4428` pentru datoria fostului salariat | `4282` | 4.3 |
| `6918` pentru impozitul micro | `698` | 6.2 |
| `4315 = CASS (pensia)`, `4316 = CAS (sănătate)` | 4315 = CAS = pensii · 4316 = CASS = sănătate | 2.1 |
| Tichetele de masă sub 423 | 642 | 2.4 |
| Minimul proporțional rotunjit la 2.163 / 1.081 | 2.162,50 / 1.081,25 | 1.1 |

---
