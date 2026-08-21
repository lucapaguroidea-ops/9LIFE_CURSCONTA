# Capitaluri, credite, leasing și provizioane
### Surse: training 07.08.2026 · adâncit cu 19.08.2026 — versiune revizuită

---

## Cum citești acest document

| Marcaj | Semnificație |
|---|---|
| ✅ | Notița originală era corectă — doar reformulată/completată |
| ⚠️ | **Eroare în notița originală** — corectată aici, cu explicație |
| ➕ | Completare (lucru care lipsea, dar era necesar ca raționamentul să stea în picioare) |
| ❓ | Rămas deschis — de clarificat cu formatorul (vezi Anexa D) |

> **Notă de metodă:** verificările s-au făcut față de OMFP 1802/2014, Legea contabilității 82/1991, Legea societăților 31/1990 (cu modificările din Legea 239/2025) și Codul fiscal la zi (Legea 141/2025, Legea 239/2025, OUG 8/2026). Punctele marcate `❓` sunt cele unde notița e ambiguă sau unde practica diferă – merită reluate la training.

---

## 0. Sinteza corecțiilor importante

| # | În notiță | Corect / de reținut |
|---|---|---|
| 1 | „2027 depuneri: 101 în Martie" | ⚠️ **Termenul de 25 iunie a fost permanentizat** pentru majoritatea plătitorilor de impozit pe profit. Pentru anul fiscal 2026 → **25 iunie 2027**, nu martie. |
| 2 | `129 = 1171` (închiderea repartizării) | ⚠️ Corect este **`121 = 129`**. |
| 3 | „121 = 250 lei; 129 = 1061 → 125 lei" | ⚠️ 5% din 250 = 12,50 lei. Cifrele se leagă doar dacă **profitul era 2.500 lei**. |
| 4 | „când vine factura de la avocat, o înregistrez pe 151" | ⚠️ **Nu.** Factura se înregistrează normal pe cheltuială (628 = 401), iar provizionul se **reia separat** (1511 = 7812). |
| 5 | „1067 – banii datorați firmei de leasing" | ⚠️ Typo: **167**. (1067 nici nu mai există în planul de conturi actual.) |
| 6 | „4426 = 4424 (de roșu)" | ⚠️ Typo: contrapartida e **404**, nu 4424. Sau, mai simplu: `635/6588 = 4426`. |
| 7 | „615 neded" pentru CASCO | ⚠️ 615 = *Cheltuieli cu pregătirea personalului*. Corect: **613 analitic nedeductibil** (sau 6588). |
| 8 | CASCO: „50% din 100 lei" | ⚠️ În exemplu CASCO era **20 lei** → nedeductibil 10 lei, nu 50. |
| 9 | „unii reduc avansul cu 231" | ⚠️ 231 = imobilizări **în curs de execuție**. Avansul pentru imobilizări corporale = **4093**. |
| 10 | „lunar / obligatoriu la 3 luni" (reevaluare valută) | ⚠️ Reevaluarea elementelor monetare în valută este **lunară**, obligatoriu (OMFP 1802/2014). Trimestrial e prea rar. |
| 11 | secțiunea „leasing operațional" | ⚠️ Descrierea din notiță (bun la mijloace fixe, 167, amortizare) este de fapt **leasing financiar**. Vezi cap. 7. |
| 12 | — | ➕ **Lipsește complet** limita de amortizare de **1.500 lei/lună** pentru autoturismele M1 (art. 28 alin. (14) CF) – are impact direct pe impozitul pe profit. |
| 13 | „capitaluri proprii > 50% din capital social" | ✅ Corect, dar temeiul s-a schimbat: **Legea 239/2025** (art. 67 alin. (2³) și art. 69¹ din L31/1990), în vigoare din 18.12.2025. Vezi cap. 1.2. |
| 14 | 1175 | ✅ **Corect** – 1175 este contul valabil din 2015 (a înlocuit 1065). |

---

## 1. Capitaluri proprii – clasa 10

### 1.1 Capital social: subscriere → vărsare

```
456  =  1011      subscrierea (creanța față de asociați)
5121 =  456       vărsarea efectivă
1011 =  1012      trecerea la „subscris și vărsat"
```

- ✅ **Analitice distincte pe fiecare asociat** la 456 – bună practică obligatorie în practică (altfel nu poți justifica cine ce datorează).
- ✅ **Răspuns la (Q – ONRC):** momentul `1011 → 1012` este **vărsarea efectivă**, nu înregistrarea la ONRC. Înregistrarea la Registrul Comerțului validează juridic majorarea/constituirea (deci naște creanța 456), dar transformarea în „vărsat" urmează depunerii efective a banilor. Ordinea practică la o majorare: hotărâre AGA → depunere ONRC → `456 = 1011` → încasare → `5121 = 456` + `1011 = 1012`.

### ➕ 1.1.bis Capital social minim – reguli noi din 2026 (aici era „5k cat (Q)")

Legea 239/2025 (în vigoare 18.12.2025) a reintrodus praguri minime:

| Situație | Capital social minim | Termen |
|---|---|---|
| Firmă nou-înființată (din 2026) | **500 lei** | la înființare |
| Firmă existentă, CA netă **> 400.000 lei** | **5.000 lei** | ~decembrie 2027 |
| Firmă existentă, CA netă ≤ 400.000 lei | fără obligație expresă deocamdată | – |
| Depășire prag în cursul unui an | 5.000 lei | finalul exercițiului următor |

- Sancțiune pentru neconformare: risc de **dizolvare judiciară**; se discută și riscul de inactivare / anulare cod TVA.
- ➕ Există mecanism de „clichet": capitalul nu mai poate fi redus sub minimul legal.
- 💡 Recomandare practică: fă o listă cu clienții care au depășit 400.000 lei la 31.12.2025 și programează majorările – nu lăsa pe ultima sută de metri (act constitutiv + hotărâre AGA + ONRC + **vărsare efectivă în cont**).

### 1.2 Corelația activ net ↔ capital social ⚠️ REGULI NOI

Aici era întrebarea din notiță („(Q – creditare de societate, dividende / dividende interimare)"). Răspunsul e **Legea 239/2025**, care a modificat Legea 31/1990:

**Când activul net (= capitaluri proprii) < ½ din capitalul social subscris:**
1. **Nu se pot distribui dividende** (nici anuale, nici interimare) până la reîntregirea activului net.
2. **Nu se pot restitui împrumuturile** primite de la asociați / alte finanțări de la persoane afiliate. → Acesta e răspunsul la „creditare de societate".
3. Societatea are **obligația de reconstituire** a activului net până la cel puțin ½ din capitalul social, **până la încheierea exercițiului financiar ulterior** celui în care s-au constatat pierderile.
4. Contravenții: amenzi în paliere (ordin de mărime **10.000 – 300.000 lei**, în funcție de faptă). Asociatul căruia i s-au restituit împrumuturi poate răspunde **solidar** cu societatea pentru obligațiile fiscale restante, în limita sumelor restituite.

**Chiar dacă activul net e OK**, dividendele din profitul curent se pot distribui doar **după**:
- constituirea rezervei legale,
- **acoperirea integrală a pierderii contabile reportate**,
- îndeplinirea cerințelor statutare.

> ⚠️ Practic: „am profit + am cash" **nu mai e suficient**. Verificarea se face pe bilanț, nu pe cont. ANAF a anunțat (mai 2026) verificări etapizate începând cu situațiile financiare pe 2025.

`❓` De clarificat la training: cum se documentează concret „reîntregirea activului net" (conversie creanță asociat în capital social? aport nou? renunțare la creanță – atenție, venit impozabil).

### 1.3 Rezerve din reevaluare (105) și surplusul realizat (1175)

✅ Notița e corectă – 1175 e contul valabil (a înlocuit 1065 de la 01.01.2015, prin OMFP 1802/2014).

```
105 = 1175     transferul surplusului realizat
```

Surplusul se consideră realizat:
- **integral**, la scoaterea din evidență a activului; sau
- **treptat, pe măsura amortizării** – cu suma = amortizarea pe valoarea reevaluată **minus** amortizarea pe costul inițial.

**Fiscal (era nota „cheltuiala cu amortizarea deductibilă"):** amortizarea aferentă reevaluării **este deductibilă**, dar rezerva din reevaluare **se impozitează concomitent** cu deducerea amortizării fiscale (respectiv la scoaterea din gestiune). Practic e o operațiune neutră – dar trebuie urmărită, altfel apar diferențe la D101.

- ✅ **1175 cu analitice** – pe fiecare activ / fiecare reevaluare. Fără asta nu poți proba nici impozitarea corelată, nici ce sumă e distribuibilă.
- ➕ Restricție: sumele din 1175 **nu pot majora capitalul social** (art. 210 alin. (3) L31/1990). Pot însă acoperi pierderi contabile.

### 1.4 Rezerva legală (1061)

**Regula juridică** (art. 183 L31/1990): minimum 5% din profit anual, până la **1/5 (20%) din capitalul social**.

**Regula fiscală** (art. 26 alin. (1) lit. a) CF): deductibilă în limita a **5% din profitul contabil brut**, adică:

```
bază = sold creditor 121 + rulaj 691 (cheltuiala cu impozitul pe profit)
```

⚠️ Plafon: **20% din capitalul social subscris ȘI VĂRSAT** (nu doar „subscris"). Dacă mai ai capital nevărsat în 1011, nu intră în plafon.

**Înregistrare:**
```
31.12.N      129  = 1061      constituirea rezervei legale
```

⚠️ **Exemplul din notiță nu se leagă.** Pentru profit 250 lei, 5% = 12,50 lei. Cifra de 125 lei corespunde unui **profit de 2.500 lei**. Presupun că asta a fost în exemplu – reia calculul așa:

| | |
|---|---|
| Profit contabil brut (121 + 691) | 2.500 lei |
| Rezerva legală 5% | **125 lei** |
| Rămas de repartizat | 2.375 lei |

### 1.5 Închiderea 121 și 129 ⚠️

```
La începutul exercițiului N+1:
121 = 129      125 lei     (partea repartizată la rezerve)   ⚠️ NU 129 = 1171
121 = 1171   2.375 lei     (profitul rămas nerepartizat)
```

- ⚠️ În notiță apare `129 = 1171`. Sensul e invers: 129 are sold **debitor**, deci se închide **prin creditare**, iar 121 (sold creditor) se închide prin debitare → `121 = 129`.
- ➕ Notă: dacă faci `121 = 1171` cu tot profitul (2.500) și apoi `1171 = 129` (125), ajungi la același sold 1171 = 2.375. Rezultatul e identic, dar varianta conformă cu reglementarea e `121 = 129`.
- ✅ Închiderea se face **la începutul exercițiului următor**, nu se așteaptă AGA. AGA decide ce se întâmplă **ulterior** cu soldul lui 1171 (dividende, 1068, acoperire pierdere).

### 1.6 Repartizări din 1171 (după hotărârea AGA)

```
1171 = 457     dividende
1171 = 1068    alte rezerve
1171 = 1171    acoperire pierdere reportată (pe analitice)
```

- ✅ **1171 cu analitic pe an** – esențial. E bifuncțional și preia soldul lui 121.
- ❓ „în curs de 3 ani" – **nu am găsit un termen legal de 3 ani** pentru a decide destinația profitului reportat. Posibile surse ale confuziei: prescripția de 3 ani a acțiunii în restituirea dividendelor (art. 67 alin. (5) L31/1990) sau prescripția generală. **De întrebat trainerul care e temeiul.**
- ➕ **Fiscal, din 2026:** impozitul pe dividende este **16%** (Legea 141/2025), pentru dividende **distribuite** începând cu 01.01.2026 – inclusiv cele din profitul 2025 aprobate în 2026. Excepție: dividendele interimare distribuite în baza situațiilor interimare din 2025 rămân la 10%, **fără recalculare** la regularizare. Cota urmează **data distribuirii** (hotărârea AGA), nu data plății.

### ➕ 1.7 Cele trei conturi care „se implică" – schema completă

```
        AN N                          AN N+1
  ┌──────────────┐            ┌────────────────────┐
  │ 121 (profit) │──────┐     │ 121 = 129  (rezervă)│
  └──────────────┘      │     │ 121 = 1171 (restul) │
         │              │     └─────────┬───────────┘
   129 = 1061           │               │
   (rezerva legală)     │          ┌────▼────┐   după AGA
                        └─────────►│  1171   │──► 457 dividende
                                   │(analitic│──► 1068 alte rezerve
                                   │  pe an) │──► acoperire pierdere
                                   └─────────┘
```

**Reguli de control (lunar / cel puțin trimestrial):**
- `Σ clasa 7 − Σ clasa 6 = sold 121` → dacă nu se verifică, cel mai probabil **nu ai închis 121 din anul precedent**.
- 129 trebuie închis după repartizarea rezervelor.
- 121 trebuie închis pentru corelația cu anul următor.
- ⚠️ Nu există automatism ca la TVA – **se face manual**. Pune-ți un control fix în ianuarie și încă unul înainte de fiecare calcul de impozit pe profit.

---

## 2. Pierderea contabilă vs. pierderea fiscală

Sunt **două lucruri diferite** și notița le amestecă un pic. De ținut separat:

| | Pierdere contabilă | Pierdere fiscală |
|---|---|---|
| Unde stă | 1171 (sold debitor) | D101, rândurile de pierdere; nu are cont |
| Cum se acoperă | rezerve, prime, capital, profit viitor (hotărâre AGA) | din profitul impozabil viitor |
| Regula | fără termen | **70% din profitul impozabil, în 5 ani consecutivi** (pierderi din 2024 încolo) |

➕ **Regim tranzitoriu:** pierderile rămase de recuperat la 31.12.2023 se recuperează tot în limita a **70%** din profitul impozabil, dar pe **perioada rămasă din cei 7 ani** inițiali, în ordinea înregistrării.

### La firmele preluate (✅ bună practică din notiță, extinsă)

1. Scoate din SPV **duplicatele D101** pentru toți anii din termenul de prescripție. Urmărește rândurile de pierdere și **pierderea rămasă de recuperat**.
2. Reconciliază cu **fișa pe plătitor** și cu balanțele preluate.
3. ⚠️ Dacă **1171 nu reflectă pierderea** care apare în D101 → contul nu e constituit la valoarea reală. Consecință: baza de calcul a impozitului pe profit e greșită și, mai grav, **plafonul de dividende distribuibile e supraevaluat** (cu riscurile din cap. 1.2).
4. Ține **analitice pe 1171 pe ani**, cu marcaj Debitor/Creditor – fără asta nu poți urmări recuperarea pe 5 ani.

`❓` „sunt anumite pierderi care nu sunt deductibile fiscal – astea se înregistrează într-un cont separat": contabil, pierderea e pierdere; **nu există un cont sintetic distinct** pentru pierderea nedeductibilă fiscal. Ce se face în practică este un **analitic de gestiune** (ex. `1171.01` recuperabilă fiscal / `1171.02` nerecuperabilă). De confirmat că asta a fost intenția.

---

### 2.1 Închiderea conturilor de cheltuieli și venituri


```
121  = 607    ·  20.000
707  = 121    ·  24.000
```

Rezultatul contabil: 121 are sold **creditor de 4.000** lei — profitul pe care se calculează impozitul.


### 2.2 Impozitul pe profit


Cota este **16%**, aplicată la baza impozabilă. Cei 4.000 lei sunt **baza**, nu impozitul:

> 16% × 4.000 = **640 lei**

```
691  = 4411   ·     640     (cheltuiala cu impozitul pe profit)
121  = 691    ·     640     (închiderea contului de cheltuială)
```

Profitul net rămâne 4.000 − 640 = **3.360 lei**.

> Contul sintetic este **441** *Impozitul pe profit și alte impozite*; pentru impozitul pe profit se folosește analiticul **4411**.

---

## 3. Documente justificative și corectarea erorilor

### 3.1 Principiul

✅ „Fiecare notă contabilă să aibă un document" – **Legea 82/1991, art. 6**: orice operațiune se consemnează într-un document care devine document justificativ. Detaliile de formă: **OMFP 2634/2015**.

### 3.2 Pragul de semnificație

- ➕ Trebuie **definit expres în politicile contabile**, aprobat de administrator, aplicat **consecvent** (ex.: X% din CA / din total active / din rezultat, cu o valoare absolută minimă).
- Fără el, nu poți justifica alegerea între „corectez pe 6xx" și „corectez pe 1174".

### 3.3 Arbore de decizie – factură lipsă / înregistrată greșit

**A. Factură a exercițiului CURENT, descoperită în același an**
→ înregistrare normală pe cheltuială în luna constatării; TVA se deduce în decontul curent (drept de deducere păstrat 5 ani). Nicio rectificare.

**B. Factură care NU era a mea, constatată în același an**
```
628 = 401   cu minus (storno)
4426 = 401  cu minus
```
- Efect net: 0 pe cheltuială, 0 pe furnizor, 0 pe TVA. ✅ Exact cum e în notiță.
- Dacă factura a fost **achitată** → discuție separată (recuperare/compensare cu furnizorul).
- **Impozit pe profit:** dacă D100 a fost depus cu profit denaturat → **formular 710** (D100 nu are bifă de rectificativă, spre deosebire de D112). ✅ Notița e corectă aici. Dacă rezultă impozit suplimentar → **accesorii** (dobânzi + penalități de întârziere; eventual penalitate de nedeclarare dacă o stabilește organul fiscal). **Discuția cu administratorul se poartă înainte**, nu după.
- **TVA:** ⚠️ nuanță importantă – sumele din corectarea erorilor de înregistrare în evidențele de TVA se înscriu la **rândurile de regularizări din decontul lunii curente**. Decontul de TVA **nu se rectifică** prin depunerea unuia nou. „Cererea de corectare a erorilor materiale" (OMEF 179/2007) e pentru erori **de completare** (căsuțe, tastare), nu pentru sume rezultate din evidență.

**C. Factură a exercițiului ANTERIOR, eroare SEMNIFICATIVĂ**
```
1174 = 401     cheltuiala (fără TVA)
4426 = 401     TVA
```
- ⚠️ **Nu se mai trece prin 628.** ✅ Notița e corectă.
- TVA se deduce în **decontul curent**.
- **Obligatoriu: D101 rectificativ** pentru anul afectat (bifa „Declarație rectificativă" există pe formularul 101 – spre deosebire de D100).
- Ulterior, 1174 se închide prin 1171 (după hotărârea AGA).

**D. Eroare NESEMNIFICATIVĂ (sub prag)**
→ se corectează pe contul de profit și pierdere **curent** (6xx).
→ ⚠️ Risc fiscal: cheltuiala nu e aferentă exercițiului curent, deci poate fi considerată nedeductibilă. Documentează decizia (nota de prag).

### 3.4 ✅ Răspuns la întrebarea ta despre 1174

> *„Dacă scopul lui 1174 era să nu denatureze profitul anilor precedenți, când închidem 1174 în 1171 nu denaturăm profitul anilor precedenți?"*

Întrebarea e bună și răspunsul e că **1174 nu protejează „profitul anilor precedenți", ci două alte lucruri:**

1. **Rezultatul anului CURENT (contul 121).** O cheltuială din 2025 nu are ce căuta în P&L-ul lui 2026. Dacă ai trece factura pe 628 în 2026, ai denatura rezultatul lui 2026 – și, implicit, impozitul pe profit al lui 2026. 1174 ocolește complet contul de profit și pierdere.

2. **Trasabilitatea corecției.** 1174 este un „compartiment cu etichetă": arată explicit *cât* din capitalurile proprii provine dintr-o corecție de eroare, nu din profit efectiv realizat și raportat. Situațiile financiare ale anilor trecuți **nu se retratează** (asta e regula din OMFP 1802/2014) – deci 1174 e singurul loc unde se vede că bilanțul aprobat atunci era greșit.

Odată ce corecția e stabilită, D101-ul rectificativ depus și AGA a luat act, suma **este** parte din rezultatul acumulat – deci transferul în 1171 nu „re-denaturează" nimic, ci doar închide un cont tranzitoriu. Denaturarea ar fi fost să treacă prin 121.

⚠️ **Partea sensibilă, exact cum spune notița:** dacă 1171 nu mai are sold (proprietarul a luat deja dividendele), transferul îl duce **pe debitor** → pierdere reportată neacoperită. Din 2026 asta declanșează restricțiile Legii 239/2025 (blocaj dividende + blocaj restituire împrumuturi asociați + obligație de reîntregire). **Deci ordinea corectă e: corectezi întâi, distribui după.**

### ➕ 3.5 Controlul preventiv care evită tot ce e mai sus

Reconciliază **lunar registrul RO e-Factura din SPV** cu jurnalul de cumpărări. Cazul din notiță („clientul nu a încărcat un document în SPV / s-a încărcat eronat") se prinde în luna respectivă, nu peste un an. Ăsta e cel mai ieftin control din toată lista.

---

## 4. Termene de depunere ⚠️ ATENȚIE – S-A SCHIMBAT

| Declarație | An fiscal 2025 (depus 2026) | An fiscal 2026 (depus 2027) |
|---|---|---|
| **D101** impozit pe profit | 25 iunie 2026 | ⚠️ **25 iunie 2027** (termenul a fost **permanentizat**) |
| **D100** impozit micro T4 | 25 iunie 2026 | ⚠️ revine la **25 ianuarie 2027** |
| **Situații financiare anuale** (societăți) | ~30 mai 2026 | **150 de zile** de la 31.12.2026 → **~30 mai 2027** ✅ |

- ⚠️ Notița spune „101 în Martie" pentru 2027. **Este depășit.** Termenul standard din art. 42 CF era 25 martie, derogarea din OUG 153/2020 l-a mutat la 25 iunie timp de 5 ani (2022–2026), iar în martie 2026 Guvernul l-a făcut **permanent** pentru majoritatea plătitorilor de impozit pe profit.
- Excepții care rămân la termene proprii: ONG-uri și contribuabilii cu venituri majoritare din cereale/plante tehnice (25 februarie), situații speciale (fuziuni, lichidare), an fiscal modificat (25 a lunii a 6-a).
- ➕ Entități fără activitate: declarație de inactivitate, **60 de zile**.
- `❓` **De verificat actul normativ exact** care a permanentizat termenul (adoptat ~martie 2026) înainte de a-l comunica clienților.
- ✅ Punctul din notiță rămâne valabil ca risc: în intervalul ianuarie–iunie se uită frecvent închiderea soldului lui 121.

---

## 5. Credite bancare în valută (162x)

### 5.1 Structura conturilor

⚠️ Precizare: `1621` și `162x` **nu sunt același lucru la nivel de analitic** – sunt sintetice distincte:

| Cont | Conținut |
|---|---|
| 1621 | Credite bancare pe termen lung |
| 1622 | Credite bancare pe termen lung nerambursate la scadență |
| 1623–1627 | Credite externe guvernamentale / garantate de stat / de bănci / trezorerie |
| **1682** | ➕ Dobânzi aferente creditelor bancare pe termen lung (dobânda **calculată și neajunsă la scadență**) |

### 5.2 Monografia lunară

```
1621 = 5121/5124    rata de capital
666  = 5121/5124    dobânda
627  = 5121         comisioane bancare (dacă e cazul)
```

⚠️ **Capcana din notiță:** extrasul arată deseori rata și dobânda **cumulat**. Mergi întotdeauna la **scadențar** și desparte-le. Altfel ajungi cu 1621 pe debit (sau invers, cu sold rămas la finalul creditului) și **ai trecut pe cheltuială mai mult decât trebuia** → impact direct pe impozitul pe profit și pe baza de dividende.

### 5.3 Diferențe de curs ⚠️

✅ Notița e corectă că sunt **două momente**:
1. **La plată** – diferența între cursul de la înregistrare și cursul plății → 665 / 765.
2. **La sfârșitul lunii** – reevaluarea soldului la cursul BNR din **ultima zi bancară a lunii** → 665 / 765.

⚠️ **Reevaluarea este LUNARĂ, obligatoriu** (OMFP 1802/2014), nu „la 3 luni". Trimestrial e insuficient. Verificarea suplimentară la calculul impozitului pe profit e o bună practică peste obligație, nu un substitut.

➕ Verifică **soldul în valută**, nu doar în lei: `sold valută × curs BNR = sold lei`. Dacă nu dă, ai o problemă de curs sau de rată.

➕ Reclasificarea porțiunii curente (scadentă în ≤ 12 luni) trebuie făcută pentru bilanț – prin analitic sau prin cont dedicat.

✅ „Unde am lei, treaba trebuie să fie foarte simplă" – exact, tot efortul se duce pe valută.

---

## 6. Provizioane (151x)

### 6.1 Conceptul ✅

Un provizion se recunoaște când există o **obligație actuală** rezultată dintr-un eveniment trecut, e **probabilă** o ieșire de resurse și suma poate fi **estimată credibil**. Exemplul din notiță (litigiu în curs → cheltuieli previzibile cu avocatul) e corect ca raționament: obligația s-a născut în exercițiul curent, chiar dacă plata vine anul următor.

### 6.2 Monografie ⚠️ AICI E EROAREA

```
Constituire (2026):
6812 = 1511      Cheltuieli de exploatare privind provizioanele

Anul următor (2027), când vine factura de la avocat:
628  = 401       ← factura, ÎNREGISTRARE NORMALĂ
1511 = 7812      ← RELUAREA provizionului, operațiune SEPARATĂ
```

⚠️ **Factura nu se înregistrează „pe 151".** Provizionul nu e un cont de datorii față de furnizor. Cele două operațiuni sunt independente; efectul net pe rezultatul lui 2027 este ~zero, ceea ce e chiar scopul provizionului.

➕ Provizionul se revizuiește la fiecare dată a bilanțului și **nu poate fi utilizat pentru altă cheltuială** decât cea pentru care a fost constituit (OMFP 1802/2014).

### 6.3 ➕ Tratamentul fiscal (lipsea complet)

- **Provizioanele pentru litigii sunt NEDEDUCTIBILE** fiscal. Art. 26 CF enumeră limitativ ce e deductibil (rezerva legală, provizioanele pentru garanții de bună execuție, ajustările pentru creanțe în anumite condiții etc.) – litigiile nu sunt pe listă.
- Prin simetrie, **reluarea (7812) este venit neimpozabil**.
- ⚠️ Consecință practică: provizionul **nu îți scade impozitul pe profit** în anul constituirii. Nu-l vinde clientului ca optimizare fiscală – e o măsură de imagine fidelă a bilanțului.

Subconturi utile: 1511 litigii · 1512 garanții clienți · 1514 restructurare · 1516 impozite · 1518 alte provizioane.

---

## 7. Leasing

### 7.1 ⚠️ Operațional vs. financiar – notița le amestecă

Secțiunea din notiță începe cu „operațional" dar descrie imediat 167, mijloc fix, avans 4093 – **acesta e leasing financiar**.

| | **Operațional** | **Financiar** |
|---|---|---|
| Bunul în bilanț | **NU** (rămâne la locator) | **DA** – 2133 |
| Datoria | nu | **167** |
| Cheltuiala lunară | **612** (chirie) | **666** dobândă + amortizare |
| Evidență extrabilanțieră | **8036** | – |
| Impozit local mijloc de transport | plătit de **locator** | plătit de **locatar**, pe toată durata contractului |
| Valoarea reziduală la final | **achiziție nouă** → intră ca mijloc fix la acea valoare | deja capitalizată; ultima factură doar închide 167 |

Criteriile de clasificare: OG 51/1997 + art. 7 pct. 7–8 CF (transferul riscurilor/beneficiilor, opțiune de cumpărare, durata ≥ 80% din durata de viață, valoarea actualizată a plăților ≈ valoarea bunului).

> ✅ Astfel se citește corect fraza din notiță: „la sfârșitul contractului, valoarea reziduală, când pot achiziționa acel bun" + „merg la primărie în 30 de zile" → asta e scenariul de **leasing operațional**, unde abia atunci apare mijlocul fix.

### 7.2 ✅ Regula de aur din notiță

> **167 este 1-la-1 cu contractul de leasing** – indiferent câte bunuri conține contractul – și pe **tip de valută**.

Motivul: la reevaluarea soldului în valută trebuie să știi **exact la ce rată din scadențar** te raportezi. Fără analitic pe contract, nu poți face reevaluarea corect.

Cele două scopuri distincte (✅ notița):
- **167** = ce datorez firmei de leasing, conform scadențarului (sold curent);
- **2133** = mijlocul fix, la valoarea de intrare.

⚠️ În notiță apare „1067" – e typo pentru **167**.

### 7.3 ➕ Regimul fiscal al autoturismelor (M1, ≤ 3.500 kg, ≤ 9 locuri)

**Trei limitări diferite, care se aplică simultan dar pe baze diferite:**

| Limitare | Bază | Temei |
|---|---|---|
| **TVA deductibilă 50%** | TVA de pe toate facturile aferente vehiculului | art. 298 CF |
| **Cheltuieli deductibile 50%** | combustibil, întreținere, piese, chirii, asigurări, **dobânzi**, **comisioane**, diferențe de curs, **inclusiv TVA nedeductibilă** | art. 25 alin. (3) lit. l) CF |
| **Amortizare max. 1.500 lei/lună** | amortizarea contabilă a fiecărui autoturism | art. 28 alin. (14) CF |

⚠️ **Foarte important:** amortizarea **NU intră** sub limitarea de 50% – are propria plafonare de 1.500 lei/lună. Cele două nu se cumulează.

➕ Art. 25 alin. (3) lit. m): deductibilitate limitată la **un singur autoturism** pentru fiecare persoană cu funcție de conducere/administrare.

➕ Excepțiile (100% deductibil, TVA integral): urgență/pază/curierat, agenți de vânzări și achiziții, taxi, închiriere, școli de șoferi, transport de persoane cu plată. Fără documentație (foi de parcurs, decizie internă), **regimul prudent și conform este 50%**.

### ➕ 7.3.bis Noutăți 2026 relevante pentru mijloace fixe

- **OUG 8/2026** (în vigoare 25.02.2026): pragul fiscal al mijloacelor fixe a crescut de la **2.500 lei la 5.000 lei**; se actualizează anual cu inflația.
- Bunurile între 2.500 și 5.000 lei existente la 31.12.2025 **continuă** amortizarea pe durata rămasă (nu se trec retroactiv pe cheltuieli).
- **Amortizare superaccelerată 65% în primul an** – exclusiv pentru 2026, doar pentru **active noi** din subgrupele 2.1 (echipamente tehnologice) și 2.4 (animale și plantații), puse în funcțiune în 2026. **Nu se aplică autoturismelor.** Cumulabilă cu scutirea pentru profit reinvestit.
- ⚠️ Pragul de 5.000 lei este **fiscal**, nu contabil – contabil, politicile firmei pot stabili alt prag.

### 7.4 Monografie – leasing financiar autoturism cu deductibilitate 50%

**Date:** valoare de intrare 150.000 lei · avans 50.000 lei · TVA 21% · rate capital 100.000 lei + dobândă + comisioane + CASCO

#### Pasul 1 – factura de avans
```
%      =  404       60.500
4093              50.000
4426              10.500      (21% × 50.000)
```

#### Pasul 2 – TVA nedeductibilă pe avans, capitalizată
```
2133   =  4426      5.250      (50% × 10.500)
```
> Varianta din notiță (`4426 = 404` de roșu + `2133 = 404` de negru) dă exact același rezultat. Temeiul: taxele nerecuperabile intră în **costul de achiziție** (OMFP 1802/2014).

#### Pasul 3 – recepția bunului
```
2133   =  167     150.000
167    =  4093     50.000      (închiderea avansului)
```

#### ✅ Valoarea de intrare a mijlocului fix: **155.250 lei**

| | |
|---|---|
| Amortizare contabilă (60 luni) | 2.587,50 lei/lună |
| **Amortizare fiscal deductibilă** | **1.500,00 lei/lună** |
| **Nedeductibil lunar** | **1.087,50 lei/lună** |

⚠️ Acesta e elementul care lipsea complet din notiță și care are **cel mai mare impact** pe impozitul pe profit.

#### Pasul 4 – factura lunară de leasing (la valoarea ei, fără split ✅)
```
%      =  404        3.166
167                  2.000     rata de capital
666                    500     dobândă
628                    100     comision de administrare
613                     20     CASCO
4426                   546     TVA (420 + 105 + 21)
```
> ➕ Comisionul poate fi și pe **627** – aliniază-te la politica firmei și fii consecvent.

#### Pasul 5 – corecția TVA nedeductibilă (50%)

| Element | TVA total | Nedeductibil |
|---|---|---|
| Rata de capital | 420,00 | **210,00** |
| Dobândă | 105,00 | **52,50** |
| Comision | 21,00 | **10,50** |
| **Total** | 546,00 | **273,00** |

```
6588 (sau 635)  = 4426     210,00     ❓ vezi nota de mai jos
666             = 4426      52,50
628             = 4426      10,50
```
> ⚠️ În notiță apare `4426 = 4424` – **typo**, contrapartida corectă e 404 (în varianta cu storno) sau direct 4426 (în varianta simplă de mai sus). Rezultatul e identic; varianta de mai sus e mai curată.
>
> 💡 Și mai simplu: înregistrează direct doar 50% pe 4426, iar restul pe destinația finală. Eviți complet notele în roșu.

`❓` **De clarificat cu trainerul:** TVA nedeductibilă aferentă **ratei de capital** (210 lei) – se capitalizează în 2133 (coerent cu tratamentul avansului, pct. 75 OMFP 1802) sau se trece pe cheltuială (635/6588)? Practica e împărțită. Capitalizarea e mai coerentă conceptual, dar impune ajustarea valorii și a amortizării în fiecare lună. Dacă se trece pe cheltuială, e integral nedeductibilă (**nu se mai aplică încă o dată 50%** – ar fi dublă limitare).

#### Pasul 6 – limitarea de 50% a cheltuielilor

| Cont | Rulaj după corecția TVA | Nedeductibil (50%) |
|---|---|---|
| 666 dobândă | 500,00 + 52,50 = **552,50** | **276,25** |
| 628 comision | 100,00 + 10,50 = **110,50** | **55,25** |
| 613 CASCO | **20,00** | **10,00** ⚠️ (nu 50 – în notiță CASCO era 20 lei, nu 100) |

```
666      = 404      276,25   (de roșu)
666.NED  = 404      276,25   (de negru)

628      = 404       55,25   (de roșu)
628.NED  = 404       55,25   (de negru)

613      = 404       10,00   (de roșu)
613.NED  = 404       10,00   (de negru)     ⚠️ NU 615 (= pregătirea personalului)
```

➕ **Nu uita diferențele de curs valutar** dacă leasingul e în EUR: intră și ele în baza limitării de 50%.

### 7.5 Obligații conexe

- **Impozit local pe mijlocul de transport:** declarație la primărie în **30 de zile**. La leasing financiar, îl datorează **locatarul pe toată durata contractului**. La finalul contractului, când se transferă proprietatea, se depune declarație nouă.
- Verifică pe fiecare factură **rata de schimb comunicată de firma de leasing** și corelează cu rata din scadențar – altfel reevaluarea soldului 167 se face la curs greșit.

---

## 8. An fiscal modificat

✅ Corect: se poate opta pentru un exercițiu financiar diferit de anul calendaristic, tipic pentru alinierea la raportarea firmei-mamă.

- Temei contabil: OMFP 1802/2014 (filiale ale unor societăți străine cu exercițiu diferit).
- Temei fiscal: **art. 16 alin. (5) Cod fiscal** – anul fiscal poate urma exercițiul financiar.
- ➕ **Formular 014** „Notificare privind modificarea anului fiscal", depus la ANAF în **15 zile** de la începutul anului fiscal modificat sau de la începutul anului calendaristic, care intervine primul.
- ➕ Termenul D101 devine **25 a lunii a 6-a** de la închiderea anului fiscal modificat.
- ⚠️ Atenție la perioada de tranziție (anul „scurt") – reguli specifice de calcul și de recuperare a pierderii.

---

## 9. Principii de lucru (partea finală din notițe) ✅

> **juridic → economic → contabil**

- Coerența între cele trei straturi e testul de bază. Dacă înregistrarea contabilă nu are corespondent economic și suport juridic, e greșită indiferent cât de bine arată în balanță.
- Când întâlnești o operațiune pe care nu ai mai văzut-o: **nu trage linie repede**. Caută dintr-un articol în altul, adună câteva opinii, documentează raționamentul în scris.
- ➕ Adaug: **pune raționamentul pe hârtie în dosarul permanent** al clientului. Peste doi ani, la un control sau la o preluare, nota ta e singurul lucru care explică de ce ai făcut ce ai făcut.
- ➕ Și: **discuția cu administratorul se poartă înainte de a face corecția**, nu după ce vin accesoriile.

---

## 12. Impozit pe profit sau impozit pe venit (micro)
### 12.1 Impozitul pe profit


Cota este 16%, aplicată la baza impozabilă:

```
691  = 441                  (cheltuiala cu impozitul pe profit)
```


### 12.2 Condițiile pentru microîntreprindere


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


### 12.3 Depășirea pragului


Dacă în cursul anului veniturile depășesc pragul, societatea devine plătitoare de impozit
pe profit **începând cu trimestrul în care s-a depășit**, nu cu următorul.

➕ Consecința practică: clientul care se apropie de prag trebuie anunțat înainte, nu
după. Declarațiile devin **D100 trimestrial** și **D101 anual**.


### 12.4 Ce sold trebuie să aibă


**441** (impozit pe profit) și **4418** (impozit pe venit) sunt conturi de pasiv, deci
soldul lor normal este **creditor**. Un sold debitor înseamnă că s-a plătit mai mult
decât se datorează — de verificat, nu de ignorat.

---

---

## Anexa B — Checklist practic

- [ ] Σ clasa 7 − Σ clasa 6 = sold 121
- [ ] 121 din anul precedent este închis (121 = 129 și 121 = 1171)
- [ ] 129 închis după repartizarea rezervelor
- [ ] Reevaluare **lunară** a tuturor soldurilor în valută (162x, 167, 401, 411, 5124)
- [ ] Sold valută × curs BNR = sold lei, pe fiecare contract în parte
- [ ] Rata vs. dobândă separate conform scadențarului (nu conform extrasului)
- [ ] Registrul RO e-Factura din SPV reconciliat cu jurnalul de cumpărări
- [ ] Amortizare autoturisme: partea peste 1.500 lei/lună marcată ca nedeductibilă
- [ ] Cheltuieli auto: 50% nedeductibil calculat **după** includerea TVA nedeductibile
- [ ] Analitice: 456 pe asociat · 1171 pe an · 1175 pe activ · 167 pe contract și valută

---

## Anexa D — Rămase deschise

1. ❓ „1171 → decis în curs de 3 ani ce se face cu diferența" – care e temeiul legal al celor 3 ani?
2. ❓ Exemplul cu rezerva legală: profitul era 250 sau 2.500 lei?
3. ❓ TVA nedeductibilă pe rata de capital la leasing: capitalizare în 2133 sau cheltuială 635/6588? Care e poziția firmei?
4. ❓ „pierderi nedeductibile fiscal – cont separat": analitic pe 1171 sau altceva?
5. ❓ „facturi neînregistrate aferente exercițiului anterior" – întrebarea rămăsese deschisă în notițe; vezi cap. 3.3 lit. C și D pentru propunerea de tratament.
6. ⚠️ Termenul D101 pentru 2027 – **confirmă actul normativ** care a permanentizat 25 iunie.
7. ➕ De discutat: cum se documentează reîntregirea activului net (Legea 239/2025) – conversie creanță asociat în capital vs. aport nou.
8. ➕ De adăugat în checklist-ul de închidere: verificarea capitalului social minim (500 / 5.000 lei) pentru portofoliul de clienți.

---

---

## Anexa E — Baza legală citată

Extrasă automat din textul documentului: sunt listate actele și articolele care apar efectiv citate mai sus. Contextul fiecărei citări e în secțiunea unde apare.

**Acte normative citate**

- Legea 239/2025
- Legea 141/2025
- Legea 31/1990
- Legea 82/1991
- OMFP 1802/2014
- OMFP 2634/2015
- OUG 8/2026
- OUG 153/2020
- Codul fiscal

**Articole citate**

art. 6, art. 7, art. 16 alin. (5), art. 25 alin. (3), art. 26 alin. (1), art. 28 alin. (14), art. 42, art. 67 alin. (2), art. 67 alin. (5), art. 69, art. 183, art. 210 alin. (3), art. 298


---

*Rolul Anexei C îl joacă secțiunea 0 (Sinteza corecțiilor), păstrată în față pentru că funcționează ca rezumat executiv al documentului.*
