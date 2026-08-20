# Stocuri, TVA și corelații de balanță
### Surse: training 14.08.2026 · adâncit cu 19.08.2026 — stocuri (clasa 3), TVA și corelații de balanță, versiune revizuită

---

---

## Cum citești acest document

| Marcaj | Semnificație |
|---|---|
| ✅ | Notița originală era corectă — doar reformulată/completată |
| ⚠️ | **Eroare în notița originală** — corectată aici, cu explicație |
| ➕ | Completare (lucru care lipsea, dar era necesar ca raționamentul să stea în picioare) |
| ❓ | Rămas deschis — de clarificat cu formatorul (vezi Anexa D) |

**Cote de TVA folosite peste tot:** 21% standard / 11% redusă (Legea 141/2025, în vigoare de la 01.08.2025). Regim tranzitoriu 9% pentru locuințe doar până la 31.07.2026.

**Atenție generală:** cifrele fiscale din acest document (praguri, cote, contribuții) sunt valabile la data trainingului. Sunt exact genul de lucruri care se schimbă prin OUG peste noapte — reverifică înainte să le aplici la un client.

---

## 0. Harta subiectelor

```
CLASA 3 (stocuri)
│
├── 30x  Materii prime / materiale / obiecte de inventar
│         └── legătura cu 60x și cu 8035
├── 32x  Stocuri în curs de aprovizionare
├── 33x  Producție în curs de execuție ──┐
├── 34x  Produse (finite, reziduale)  ───┤── legătura cu 711/712
├── 37x  Mărfuri ────────────────────────┘   și cu 378 / 4428
└── 38x  Ambalaje ── obligații de mediu (AFM)

TRANSVERSAL: regimul de TVA (4426 / 4427 / 4428 / 4423 / 4424)
             + jurnalele de cumpărări și vânzări
```

---

## 1. Clasa 3 — cadrul general

✅ Conturile de clasa 3 sunt, în principiu, **conturi de activ**: cresc în debit la intrare, scad în credit la ieșire.

⚠️ **Nuanță care lipsea:** nu toate. În clasa 3 există și conturi **rectificative**, cu funcție de pasiv:

| Cont | Denumire | Funcție |
|---|---|---|
| 378 | Diferențe de preț la mărfuri (adaos comercial) | rectificativ, sold **creditor** |
| 388 | Diferențe de preț la ambalaje | rectificativ, sold creditor |
| 348 | Diferențe de preț la produse | bifuncțional |
| 39x | Ajustări pentru deprecierea stocurilor | rectificativ, sold creditor |

Deci: **371 (activ) – 378 (rectificativ) – 4428 (rectificativ) = valoarea reală a mărfii la cost de achiziție.** Ține minte formula asta, e coloana vertebrală a capitolului despre gestiunea cu amănuntul (cap. 8).

---

## 2. Achiziția de stocuri și regimul de TVA

Contul-pereche standard: **301 „Materii prime" ↔ 401 „Furnizori"**.

### 2.1 Cele trei regimuri — formulele complete

⚠️ În notițe formulele erau scrise incomplet (lipsea 4426, iar la taxare inversă 4427 apărea greșit „sub" 401). Forma corectă:

**a) Achiziție internă, cu TVA (furnizor român, plătitor):**
```
%           =  401           121.000
  301                        100.000
  4426                        21.000
```

**b) Achiziție intracomunitară / taxare inversă:**
```
301         =  401           100.000     (factura vine fără TVA)

și, simultan, autolichidarea:
4426        =  4427           21.000     (cota din România)
```
➕ Efectul net în decontul de TVA este **zero**. Asta e ideea măsurii de simplificare: nici tu nu deduci efectiv, nici furnizorul nu colectează, deci nu există bani de recuperat de la stat pe operațiunea asta.

⚠️ Formularea din notițe „*cel care livrează și cel care achiziționează nu mai deduc*" este imprecisă. Corect: **furnizorul nu colectează**, iar **beneficiarul înregistrează simultan și colectat, și deductibil**. Beneficiarul chiar deduce — dar deducerea e anulată de colectare.

**c) Scutire (export, livrare intracomunitară, alte scutiri):**
```
301         =  401           100.000     (fără TVA deloc)
```

### 2.2 Verificarea partenerului — de ce contează

O firmă poate să **emită în continuare facturi cu TVA înscris pe ele deși codul de TVA i-a fost anulat**. Tu, ca beneficiar, **nu ai drept de deducere** pe acel TVA (art. 11 Cod fiscal). Paguba e a ta, nu a lui.

⚠️ **Corecție importantă:** notițele spun că ANAF anulează codul dacă nu s-au depus deconturi **2 luni consecutive**. Fals. Conform art. 316 alin. (11) lit. d) Cod fiscal, termenul este:
- **6 luni consecutive** — pentru cei cu perioadă fiscală luna;
- **2 trimestre consecutive** — pentru cei cu perioadă fiscală trimestrul.

(Confuzia vine probabil de la varianta trimestrială, unde „două perioade" înseamnă două trimestre.)

✅ Celelalte cauze de anulare din oficiu menționate sunt corecte. Lista completă (art. 316 alin. 11):

| Lit. | Cauză |
|---|---|
| a) | societatea e declarată inactivă fiscal |
| b) | inactivitate temporară înscrisă la Registrul Comerțului |
| c) | asociații/administratorii au fapte înscrise în **cazierul fiscal** |
| d) | **nedepunerea niciunui decont** 6 luni / 2 trimestre |
| e) | deconturi depuse, dar **fără nicio operațiune** 6 luni / 2 trimestre |
| f) | societatea nu era obligată și nici nu avea dreptul să se înregistreze |
| g) | risc fiscal ridicat |

⚠️ **Nu verificăm „pe Google".** Verificăm în registrele oficiale ANAF:

| Ce verifici | Unde |
|---|---|
| Este partenerul înregistrat în scopuri de TVA? | Registrul persoanelor impozabile înregistrate în scopuri de TVA |
| I-a fost anulat codul? | Registrul persoanelor cu cod de TVA anulat |
| Aplică TVA la încasare? | Registrul persoanelor care aplică TVA la încasare |
| Este inactiv fiscal? | Registrul contribuabililor inactivi/reactivați |
| Partener UE — cod valid? | **VIES** (obligatoriu pentru scutirea la livrarea intracomunitară) |

✅ Softurile bune fac verificarea automată la ANAF, inclusiv atributul de TVA la încasare — dar **verifică tu că funcția e activată și că rulează la închiderea lunii**, nu doar la introducerea facturii.

➕ **Regulă practică:** furnizor nou = verificare obligatorie *înainte* de prima plată, nu la închidere. Salvează dovada verificării (printscreen/PDF) la dosarul lunii — la inspecție ți se cere.

### 2.3 Unde ajunge informația

| Declarație | Ce conține | Termen |
|---|---|---|
| **D300** — decont de TVA | toate operațiunile perioadei | 25 a lunii următoare perioadei fiscale |
| **D394** — declarație informativă | tranzacții **pe teritoriul național**, defalcate pe parteneri | 30 a lunii următoare perioadei fiscale |
| **D390** — declarație recapitulativă | operațiuni **intracomunitare** | 25 a lunii următoare |

✅ Observația din notițe despre D394 este corectă și importantă: declarația are **casete separate** pentru operațiunile cu persoane înregistrate în scopuri de TVA și pentru cele cu neînregistrate. Softul repartizează pe baza **atributului fiscal al CUI-ului** (prefixul „RO").

➕ Consecință practică: când un client trece de la neplătitor la plătitor de TVA, trebuie să actualizezi atributul în nomenclatorul de parteneri **la data efectivă a înregistrării**, nu retroactiv pe toată fișa. Altfel D394 iese greșit și primești notificare de conformare.

⚠️ Notițele întreabă „unde se mai duce informația, în afară de D300?". Răspuns complet: **D394** (pentru tranzacțiile interne), **D390** (dacă sunt operațiuni intracomunitare), **RO e-Factura** (raportarea facturii propriu-zise) și **D406/SAF-T** (fișierul standard de audit). Nu doar D394.

### 2.4 Legătura cu producția

✅ Contul 301 se folosește cel mai des în **producție**. Din punct de vedere al tratamentului contabil, este cuplat cu:
- **601** „Cheltuieli cu materiile prime" — la consum;
- **711** „Venituri aferente costurilor stocurilor de produse" — la obținerea produsului;
- **7015** „Venituri din vânzarea produselor finite" — la vânzare.

⚠️ Notița originală zicea „*cuplat cu 704 și 7015*". **704** este „Venituri din servicii prestate" — nu are legătură cu materiile prime consumate în producția de bunuri. 704 apare când vinzi manoperă/servicii, nu produse. Corect este **7015** (+ 711 pe traseu).

---

## 3. Materiale consumabile (302) și obiecte de inventar (303)

### 3.1 Structura analitică a lui 302

➕ Notițele lăsaseră doar „302 / 3021 / etc". Lista completă:

| Cont stoc | Denumire | Cont cheltuială pereche |
|---|---|---|
| 3021 | Materiale auxiliare | 6021 |
| 3022 | Combustibili | 6022 |
| 3023 | Materiale pentru ambalat | 6023 |
| 3024 | Piese de schimb | 6024 |
| 3025 | Semințe și materiale de plantat | 6025 |
| 3026 | Furaje | 6026 |
| 3028 | Alte materiale consumabile | 6028 |

Perechea e 1:1. Dacă vezi un 602x fără 302x corespondent în balanță, ai o problemă.

### 3.2 REGULA: nu treci niciodată direct pe cheltuială

> ❌ `6021 / 6024 / 6028 = 401`
> ✅ `3021 / 3024 / 3028 = 401`, apoi `6021 / 6024 / 6028 = 302x` pe bon de consum

**De ce — argumentul de audit** (⚠️ reformulat, notița originală amestecase conturile):

Auditorul care verifică situațiile financiare cere **balanța analitică a conturilor de stoc**, nu a lui 401. Pe un cont 302x el citește instantaneu:
- **rulaj debitor** = ce a intrat în gestiune pe parcursul anului (achiziții);
- **rulaj creditor** = ce s-a consumat efectiv (bonuri de consum);
- **sold final** = ce ar trebui să existe fizic la inventariere.

Dacă tu treci direct pe 6021, contul de stoc e gol, corelația dispare, iar auditorul nu are cu ce să confrunte inventarul faptic. La 401 ai altceva: credit = facturi primite, debit = plăți. Alt tip de informație.

➕ **Excepție de reținut:** OMFP 1802/2014 permite și metoda **inventarului intermitent**, unde achizițiile chiar se trec direct pe cheltuială, iar la sfârșitul perioadei se stornează stocul rămas. E o opțiune de politică contabilă, nu o scuză. Dacă nu ai declarat explicit metoda intermitentă în politicile contabile ale clientului, **regula de mai sus e obligatorie**.

### 3.3 Transferul spre mărfuri

✅ Corect în notițe: dacă piesele de schimb cumpărate pentru consum propriu ajung să fie **revândute**, se schimbă destinația bunului, deci și contul:

```
371         =  3024        (transfer la valoarea de intrare)
371         =  378         (adaosul comercial, dacă vinzi cu amănuntul)
371         =  4428        (TVA neexigibilă, dacă vinzi cu amănuntul)
```

➕ Documentul justificativ: **notă de transfer între gestiuni**, aprobată. Nu se face „din pix" în contabilitate.

### 3.4 Obiect de inventar vs. mijloc fix — pragul

⚠️ **Aici notițele au două probleme.**

**Problema 1 — pragul.** Notițele zic „5.000". Este corect **acum**, dar merită știut de când și de ce: prin **OUG nr. 8/2026** (M.Of. nr. 147 din 25.02.2026) pragul fiscal a crescut de la 2.500 lei la 5.000 lei, după 12 ani de stagnare (fusese fixat prin HG 276/2013).

Consecințe:
- **Achiziții din 2026:** bun sub 5.000 lei → deductibil integral la punerea în funcțiune, fără amortizare.
- **Bunuri deja în patrimoniu la 31.12.2025 cu valoare între 2.500 și 5.000 lei:** rămân mijloace fixe, se amortizează în continuare pe durata rămasă. **Nu se reclasifică retroactiv.**
- Pragul urmează să fie actualizat anual în funcție de inflație.

➕ **Nuanță de reținut, pe care mulți o ratează:** pragul de 5.000 lei este **fiscal**, nu contabil. Din punct de vedere contabil, entitatea își poate stabili prin politici contabile un alt prag de recunoaștere ca imobilizare. Dacă cele două diferă, apar diferențe temporare între rezultatul contabil și cel fiscal — de urmărit în registrul de evidență fiscală.

**Problema 2 — criteriile.** Notița spune: „*>1 an durată de utilizare, chiar dacă <5.000 ⟺ mijloc fix*". **Fals.** Cele două condiții sunt **cumulative**, nu alternative (art. 28 alin. 2 Cod fiscal):

| Condiție | |
|---|---|
| deținut și utilizat în producție, prestare de servicii, închiriere sau scopuri administrative | ȘI |
| valoare fiscală de intrare **≥ 5.000 lei** | ȘI |
| durată normală de utilizare **> 1 an** | |

Deci: laptop de 4.000 lei folosit 4 ani → **obiect de inventar** (303), nu mijloc fix. Exact invers față de ce zicea notița.

✅ Observația că majoritatea societăților *preferă* obiectele de inventar este corectă și e chiar motivul economic al majorării pragului: deducere imediată, avantaj de cash-flow, mai puțină birocrație (fără registru de mijloace fixe, fără calcul lunar de amortizare).

### 3.5 Darea în folosință și contul 8035

```
603         =  303          (darea în consum/folosință)
Debit 8035                  (extrabilanțier, simultan)
```
La casare sau vânzare a obiectului de inventar:
```
Credit 8035
```

**8035 „Stocuri de natura obiectelor de inventar date în folosință"** — cont în afara bilanțului.

✅ Raționamentul din notițe este corect și merită subliniat: prin darea în folosință, obiectele de inventar **dispar din balanță** (603 se închide la 121, deci devine 0). Fără 8035 nu mai ai nicio evidență contabilă a bunurilor care fizic există și sunt folosite în societate.

➕ De aceea 303→603 și 8035 se fac **concomitent**. Un soft bun le generează automat din același document. Dacă nu o face, e o slăbiciune reală, nu un moft.

❓ **Întrebarea de pus către furnizorul de soft** (era formulată în notițe, o păstrez ca sarcină concretă):
> *„La inventariere, îmi puteți lista separat obiectele de inventar date în folosință, cu valoare și loc de folosință, ca să pot confrunta valoarea scriptică (8035) cu cea faptică de pe teren?"*

Fără lista asta, inventarierea obiectelor de inventar nu se poate face — și e o constatare frecventă la audit.

---

## 4. Stocuri în curs de aprovizionare (32x)

**Situația:** ai factura (o vezi în SPV / e-Factura), proprietatea a trecut la tine conform condiției de livrare, dar **marfa nu a ajuns fizic în gestiune**. Clasic la sfârșit de lună: factura e din 30, marfa ajunge pe 2–3.

Legiuitorul a prevăzut asta prin conturile 32x. Fără ele ai fi forțat fie să înregistrezi un stoc care nu există fizic, fie să nu înregistrezi factura — ambele greșite.

### 4.1 Nomenclatorul complet

⚠️ Notițele aveau corespondențele parțial amestecate. Forma corectă:

| În curs de aprovizionare | Se transferă în | Denumire destinație |
|---|---|---|
| **321** | **301** | Materii prime |
| **322** | **302** | Materiale consumabile |
| **323** | **303** | Materiale de natura obiectelor de inventar |
| **326** | **361** | Active biologice de natura stocurilor |
| **327** | **371** | Mărfuri |
| **328** | **381** | Ambalaje |

(În notițe apărea „303 = 323" — corect — dar și „371 = 327" scris ca „371 - 327", corect ca sens, doar notat inconsistent. `302 = 322` lipsea complet.)

### 4.2 Fluxul complet

**Luna 1 — primesc factura, marfa e pe drum:**
```
321         =  401           100.000
4426        =  401            21.000        (achiziție internă)
   sau
4426        =  4427           21.000        (achiziție intracomunitară)
```

**Luna 2 — marfa ajunge în curte, gestionarul confirmă recepția (NIR):**
```
301         =  321           100.000
```

**Luna 2 sau ulterior — consum, pe bon de consum:**
```
601         =  301           100.000
```

➕ **Documentul care declanșează pasul 2 este NIR-ul semnat de gestionar.** Nu confirmarea verbală. Dacă gestionarul nu semnează, marfa rămâne în 32x — și atunci ai o discuție de purtat cu clientul despre de ce.

---

## 5. Taxarea inversă pe teritoriul României (art. 331 Cod fiscal)

### 5.1 Condiția obligatorie — de reținut pe de rost

> **AMBII PARTENERI trebuie să fie înregistrați în scopuri de TVA conform art. 316.**

✅ Notița are dreptate să o marcheze cu semnul exclamării. Este singura condiție de fond, și e cea care se ratează cel mai des.

**Regulă practică:** când vezi mențiunea „taxare inversă" pe o factură primită, primul lucru pe care îl faci este să verifici **codul de TVA al furnizorului la data facturii** — nu la data la care înregistrezi tu.

⚠️ **Consecința nerespectării, care nu era în notițe și e importantă:** dacă furnizorul emite greșit factură **cu TVA** pentru o operațiune care intra la taxare inversă, iar tu deduci acel TVA, **pierzi dreptul de deducere** pe acea achiziție. Condițiile de fond ale taxării inverse nu au fost respectate, iar factura e greșit întocmită. Nu te salvează faptul că ai plătit TVA-ul furnizorului. Se cere factură corectată.

### 5.2 Logica economică

România are categorii de produse cu **risc fiscal ridicat** (fraudă de tip carusel, firme fantomă). Statul zice, în esență: *nu mai deduci tu TVA-ul, pentru că nu am garanția că celălalt îl colectează și îl varsă*. Prin taxare inversă, banii nu mai circulă între parteneri, deci nu mai există ce să dispară.

### 5.3 Categoriile (art. 331 alin. 2)

⚠️ Notițele listau doar „cheresteaua, imobile noi, x". Lista principalelor categorii:

| Categorie | Observații |
|---|---|
| Deșeuri feroase și neferoase, rebuturi, semifabricate rezultate din prelucrarea lor | |
| Reziduuri și alte materiale reciclabile (hârtie, carton, textile, cauciuc, plastic, sticlă) | |
| Deșeuri de materiale feroase/neferoase și aliaje | |
| **Masă lemnoasă și materiale lemnoase** (Codul silvic, L. 46/2008) | **cheresteaua intră aici** |
| Cereale și plante tehnice, semințe oleaginoase, sfeclă de zahăr | pe coduri NC din norme |
| Transferul de certificate de emisii de gaze cu efect de seră | |
| Energia electrică către un comerciant persoană impozabilă | condiție: consum propriu neglijabil, declarat |
| Certificate verzi | |
| **Construcții, părți de construcții și terenuri** | vezi mai jos |
| Telefoane mobile, dispozitive cu circuite integrate, console de jocuri, tablete, laptopuri | doar dacă valoarea **fără TVA pe factură ≥ 22.500 lei** |
| Aur de investiții / materii prime din aur | |

⚠️ **Corecție la „imobile noi":** formularea legală nu este „imobile noi vândute între societăți". Textul acoperă construcțiile, părțile de construcție și terenurile **pentru a căror livrare se aplică regimul de taxare — fie prin efectul legii, fie prin opțiune**. Adică:
- construcție nouă (taxabilă prin lege) vândută între doi plătitori → taxare inversă;
- construcție veche (scutită prin lege) pentru care vânzătorul a **depus notificarea de opțiune de taxare** → tot taxare inversă.

Diferența contează: dacă vânzătorul nu a depus notificarea de opțiune, operațiunea rămâne scutită și taxarea inversă nu se aplică.

⚠️ **De verificat periodic:** o parte din categoriile de mai sus se aplică în baza unei derogări UE cu **termen limită (31.12.2026)**, prelungită succesiv de Consiliul UE. Înainte de a aplica taxarea inversă pe cereale sau pe electronice, verifică textul în vigoare al art. 331 alin. (6). Nu presupune că e prelungită automat.

### 5.4 Mențiunea obligatorie pe factură

✅ Notița are dreptate, o formalizez:

> **Dacă nu aplici cota standard de 21% (sau 11%), ești obligat să înscrii pe factură temeiul legal.**

Art. 319 alin. (20) Cod fiscal:
- **lit. n)** — pentru operațiuni **scutite**: o referire la dispoziția aplicabilă din Codul fiscal sau din Directiva 2006/112/CE, ori orice mențiune că livrarea e scutită;
- **lit. o)** — pentru operațiuni cu taxare inversă: mențiunea **„taxare inversă"**.

Exemple de formulări corecte:

| Operațiune | Mențiune pe factură |
|---|---|
| Livrare intracomunitară de bunuri | „Scutit cu drept de deducere, art. 294 alin. (2) lit. a) Cod fiscal" |
| Export | „Scutit cu drept de deducere, art. 294 alin. (1) lit. a) Cod fiscal" |
| Cherestea către plătitor de TVA | „Taxare inversă, art. 331 alin. (2) lit. b) Cod fiscal" |
| Servicii B2B către firmă UE | „Taxare inversă, art. 278 alin. (2) Cod fiscal / art. 44 Directiva 2006/112/CE" |

➕ Lipsa mențiunii = factură incompletă = risc de refuz al scutirii la inspecție. Este cel mai ieftin risc de eliminat din toată lista asta: se rezolvă cu o setare în softul de facturare.

---

## 6. Producția: 33x, 34x și conturile 711/712

### 6.1 Principiul — de ce există contul 331

> **Nu poți avea o cheltuială fără să ai un venit corespondent în aceeași perioadă.**

Este principiul **conectării cheltuielilor la venituri** (independența exercițiului). Dacă în luna 1 consumi materie primă de 50.000 lei dar nu livrezi niciun produs, ai o cheltuială fără venit → rezultat artificial negativ → bază de impozitare distorsionată.

Legiuitorul îți dă soluția: înregistrezi **producția în curs de execuție** printr-un venit de aceeași mărime.

| Cont producție în curs | Cont de venit pereche |
|---|---|
| **331** Produse în curs de execuție | **711** Venituri aferente costurilor stocurilor de produse |
| **332** Servicii în curs de execuție | **712** Venituri aferente costurilor serviciilor în curs de execuție |

⚠️ **Corecție:** notițele scriau „331/332 cu 711/722". **722** este „Venituri din producția de imobilizări corporale" — cu totul altceva (vezi 6.5). Perechea lui 332 este **712**.

### 6.2 Contul 711 — cum funcționează efectiv

711 nu este un venit „real" din vânzare. Este contul de **variație a stocurilor de produse**. E bifuncțional:

| | Când | Sens |
|---|---|---|
| **Credit 711** | obții produse (în curs, semifabricate, finite, reziduale) | crește stocul → „venit" |
| **Debit 711** | scoți produse din stoc (vânzare, reluare producție în curs) | scade stocul → „cheltuială" |

✅ Formularea din notițe este corectă și merită păstrată ca atare:
> *„Când am un produs în societate, îl înregistrez pe 711, indiferent în ce etapă e."*

### 6.3 Exemplu complet — geam termopan

Notițele porneau exemplul dar îl lăsau neterminat (și cu o eroare de sens). Îl reconstruiesc integral, cu cifre.

⚠️ **Eroarea:** notița scria `301 - 601 50k` pentru achiziția sticlei. Sensul e inversat și contul e greșit — achiziția nu se face niciodată din contul de cheltuială.

**LUNA 1**

*(1) Achiziția sticlei — 50.000 lei + TVA 21%*
```
%           =  401            60.500
  301                         50.000
  4426                        10.500
```

*(2) Consumul — bon de consum, am tăiat sticla*
```
601         =  301            50.000
```

*(3) La 31 ale lunii, produsul nu e finalizat — nu pot livra*
```
331         =  711            50.000
```

➕ **Atenție la evaluare:** 331 se înregistrează la **cost de producție**, nu doar la valoarea materialelor. Costul include: materii prime consumate + manoperă directă (641, 6451) + amortizarea utilajelor de producție (6811) + cota de regie de producție. Dacă înregistrezi doar materialul, subevaluezi stocul și tot rămâi cu cheltuieli neacoperite.

**Rezultatul lunii 1:** cheltuieli 50.000 (601) − venituri 50.000 (711) = **0**.
✅ Exact asta observa notița: *„când am avut și cheltuială și venit, nu am afectat contul de impozit pe profit"*.

➕ **Evidența pe comenzi:** trebuie să știi **pentru ce comandă** ai făcut producția. OMFP 1802/2014 permite mai multe metode de calculație a costurilor; **metoda pe comenzi** este cea mai utilizată în producția la comandă (exact cazul termopanelor, unde fiecare geam are dimensiuni proprii). Gestiunea lui 331 se ține analitic, pe comandă.

**LUNA 2**

*(4) Anulez producția în curs (reiau soldul)*
```
711         =  331            50.000
```

*(5) Obțin produsul finit — cost complet 62.000 (50.000 materiale + 12.000 manoperă și regie)*
```
345         =  711            62.000
```

*(6) Vânzarea — preț 80.000 lei + TVA 21%*

⚠️ Notița se oprea la `4111 - ?`. Răspunsul complet sunt **două** înregistrări, nu una:
```
4111        =  %              96.800
  7015                        80.000       (venitul din vânzare)
  4427                        16.800       (TVA colectată)
```
*(7) și descărcarea de gestiune — fără ea, stocul rămâne umflat*
```
711         =  345            62.000
```

**Verificare pe ansamblul celor două luni:**

| | |
|---|---|
| Rulaj creditor 711 | 50.000 + 62.000 = 112.000 |
| Rulaj debitor 711 | 50.000 + 62.000 = 112.000 |
| **Sold 711** | **0** ✅ |
| Cheltuieli totale | 50.000 (601) + 12.000 (641/6451/6811) = 62.000 |
| Venituri din vânzare | 80.000 (7015) |
| **Rezultat** | **18.000** |

Marja apare integral în luna în care s-a produs vânzarea. Asta e tot rostul mecanismului.

### 6.4 Produse reziduale — contul 346

✅ **346 „Produse reziduale"** — deșeurile rezultate din procesul de producție (în cazul termopanelor: cioburi, profil tăiat, rumeguș la mobilă).

*(1) Obținerea deșeului, la valoarea negociată în contractul cu colectorul:*
```
346         =  711             3.000
```
➕ *(2) Facturarea către colectorul de deșeuri:*
```
4111        =  %
  703                          3.000       Venituri din vânzarea produselor reziduale
  4427                                     ⚠️ vezi mai jos
```
*(3) Descărcarea de gestiune:*
```
711         =  346             3.000
```

⚠️ **Capcană pe care notițele o ratau, deși aveau ambele piese pe masă:** livrarea de deșeuri feroase/neferoase și de reziduuri reciclabile este pe **lista de taxare inversă** (art. 331). Dacă și tu și colectorul sunteți plătitori de TVA, factura se emite **fără TVA**, cu mențiunea „taxare inversă". Deci în înregistrarea (2) nu apare 4427 la tine, ci autolichidarea o face colectorul.

### 6.5 Producția de imobilizări ≠ producția în curs de execuție

⚠️ Notița menționa „*soft făcut cu salariații societății*" în dreptul lui 331/332. Greșit. Softul dezvoltat intern este o **imobilizare necorporală**, nu un stoc:

| Ce produci intern | Cont în curs | Cont de venit | Cont final |
|---|---|---|---|
| **Software, brevete** (dezvoltate intern) | 233 Imobilizări necorporale în curs | **721** Venituri din producția de imobilizări necorporale | 203 / 208 |
| **Hală, utilaj** (construit în regie proprie) | 231 Imobilizări corporale în curs | **722** Venituri din producția de imobilizări corporale | 212 / 213 |
| **Produse pentru vânzare** | 331 Produse în curs | **711** | 345 |
| **Servicii nefinalizate** | 332 Servicii în curs | **712** | — |

Diferența e de fond: imobilizarea se **amortizează** pe ani, stocul se **descarcă** la vânzare. Dacă înregistrezi softul intern pe 331, ai și cont greșit, și tratament fiscal greșit.

---

## 7. Conturile de TVA

### 7.1 Nomenclator

| Cont | Denumire oficială | Funcție |
|---|---|---|
| **4423** | TVA de plată | pasiv — datorie la buget |
| **4424** | **TVA de recuperat** ⚠️ | activ — creanță asupra bugetului |
| **4426** | TVA deductibilă | achiziții, contrapartidă 401 → **jurnalul de cumpărări** |
| **4427** | TVA colectată | vânzări, contrapartidă 4111 → **jurnalul de vânzări** |
| **4428** | TVA neexigibilă | bifuncțional |

⚠️ Notița scria „4424 — de rambursat". Denumirea oficială din planul de conturi este **„TVA de recuperat"**. Nuanța contează: soldul lui 4424 poate fi *recuperat* (reportat, compensat) sau *rambursat efectiv* (prin cerere de rambursare, D300 cu opțiunea bifată) — sunt lucruri diferite.

### 7.2 Conturi fără sold în balanță

✅ Corect în notițe, cu o precizare de formulare:

**Clasa 6 și clasa 7** — nu au sold **după închiderea** lor la 121. În balanța lunară, înainte de închidere, au sold (cumulat de la începutul anului). În bilanț nu apar deloc.

**4426 și 4427** — se **regularizează** la sfârșitul fiecărei perioade fiscale în 4423 sau 4424:
```
4427        =  %
  4426
  4423                 (dacă rezultă TVA de plată)
sau
%           =  4426
  4427
  4424                 (dacă rezultă TVA de recuperat)
```

⚠️ Notița adăuga „excluzând 711" la conturile care ar avea sold. Nu e corect: **711 se închide la 121 exact ca orice alt cont de clasa 7**. Ce e adevărat despre 711 e altceva — că are rulaje *în ambele sensuri* în cursul perioadei, ceea ce îl face să arate diferit de restul clasei 7. Soldul lui însă se închide.

➕ **Excepții reale la regula „4426/4427 fără sold":**
- entitățile cu **pro-rată** de deducere (deducere parțială);
- entitățile cu **TVA la încasare** — unde partea neexigibilă stă în 4428.

### 7.3 Jurnalele — corelația obligatorie

```
Rulaj 4426  ⟺  Total TVA din jurnalul de cumpărări
Rulaj 4427  ⟺  Total TVA din jurnalul de vânzări
Decontul D300 se construiește DIN cele două jurnale
```

✅ La inspecție ANAF ți se cer exact trei lucruri împreună: **jurnalul de cumpărări, jurnalul de vânzări și decontul de TVA**. Dacă cele trei nu se leagă, discuția devine foarte lungă.

### 7.4 Înregistrări care NU vin dintr-o factură ⚠️

Punctul cel mai valoros din toată secțiunea, formalizat. Există operațiuni cu impact în TVA care **nu au un document de tip factură în spate** și pe care softul **nu le duce automat în jurnale**:

**a) TVA nedeductibilă 50% la autoturisme** (art. 298 Cod fiscal)

Pentru vehicule care nu sunt utilizate exclusiv în scopul activității economice, dreptul de deducere e limitat la 50%.
```
%           =  401
  6xx / 2133                     (baza)
  4426                           (50% din TVA — partea deductibilă)
  6xx                            (50% din TVA — nedeductibilă, în cheltuială)
```
➕ Se aplică și limitarea de 50% la **cheltuielile aferente** (combustibil, reparații, întreținere) — art. 25 alin. (3) lit. l) Cod fiscal, la calculul impozitului pe profit.

⚠️ Trebuie să te asiguri că ajustarea apare **cu semnul minus în jurnalul de cumpărări**, altfel jurnalul nu se mai leagă cu 4426.

**b) Lipsă la inventar**

Pe lângă cheltuiala nedeductibilă, apare și un efect de TVA. ⚠️ **Atenție la formulare** — notița zicea simplu „trebuie să colectez TVA", dar tratamentul diferă:

| Situație | Tratament TVA |
|---|---|
| Lipsă **imputabilă** (se recuperează de la o persoană) | operațiune asimilată unei livrări → **colectare TVA** (4427) |
| Lipsă **neimputabilă**, nejustificată | **ajustarea dreptului de deducere** (art. 304/305) |
| Bunuri distruse/degradate calitativ, **cu documente justificative** (proces-verbal, condiții de la art. 304 alin. 2) | **fără ajustare** |
| Perisabilități în limitele legale | fără ajustare |

❓ De confirmat cu formatorul care dintre variante se practică în cabinet ca default și ce documentație se cere.

**c) Alte cazuri de același tip:** autofacturare, ajustări de TVA la bunuri de capital, TVA la achiziții pentru care s-a schimbat destinația.

➕ **Regulă de lucru:** la închiderea fiecărei luni, listează diferența dintre TVA din balanță și TVA din jurnale. Dacă e diferență, cauza e aproape întotdeauna una dintre înregistrările de mai sus.

### 7.5 Contul 4428 — două utilizări complet diferite

✅ Notița observa corect că 4428 „poate fi și de activ și de pasiv". Motivul: sunt două mecanisme distincte care folosesc același cont.

**Utilizarea 1 — TVA la încasare** (cont de tranzit)

Pentru entitățile care aplică sistemul TVA la încasare, exigibilitatea se amână până la încasare/plată:
```
La primirea facturii:      4428  =  401         (nu am plătit → nu deduc încă)
La plata facturii:         4426  =  4428        (acum deduc)

La emiterea facturii:      4111  =  4428        (nu am încasat → nu colectez încă)
La încasare:               4428  =  4427        (acum colectez)
```
➕ **Analitic obligatoriu:** `4428.1 TVA neexigibilă la cumpărări` / `4428.2 TVA neexigibilă la vânzări`. Fără separare, soldul e ilizibil și nu poți justifica nimic la control.

**Utilizarea 2 — gestiunea cu amănuntul** (TVA „în așteptare" în preț)

Când marfa e ținută în gestiune la **preț de vânzare cu amănuntul**, prețul include deja TVA-ul. Acel TVA stă în 4428 până la vânzarea efectivă.

⚠️ **Corecție de raționament:** notița explica 4428 în gestiunea cu amănuntul ca „TVA pe care îl dau la stat când îl primesc și eu de la clienți". **Nu e același lucru cu TVA la încasare.** Aici TVA-ul devine exigibil la **momentul vânzării** (bon fiscal emis), indiferent dacă ai încasat sau nu. 4428 e „neexigibil" pentru că **marfa nu s-a vândut încă**, nu pentru că nu ai încasat.

Confuzia asta produce erori reale în decont. Ține-le separate.

---

### 7.6 Conturile


| Cont | Denumire | Natură | Când apare |
|---|---|---|---|
| **4426** | TVA deductibilă | activ | la achiziții, pe baza facturii |
| **4427** | TVA colectată | pasiv | la livrări/prestări, pe baza facturii |
| **4423** | TVA de plată | pasiv | la închidere, dacă colectat > deductibil |
| **4424** | TVA de recuperat | activ | la închidere, dacă deductibil > colectat |
| **4428** | TVA neexigibilă | **bifuncțional** | aviz, facturi nesosite, mărfuri la preț cu amănuntul |


### 7.7 Taxarea inversă


La achiziții intracomunitare și la operațiunile supuse măsurilor de simplificare, TVA se auto-lichidează:

```
4426 = 4427
```

Efectul pe trezorerie este zero — se colectează și se deduce simultan.

**Nuanță importantă:** un **avans** plătit pentru o **achiziție intracomunitară de bunuri** nu generează exigibilitatea TVA. Faptul generator intervine la emiterea facturii sau cel târziu în a 15-a zi a lunii următoare livrării. La serviciile intracomunitare regula diferă.


### 7.8 De ce are 4428 nevoie de analitice


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

## 8. Mărfuri (371)

### 8.1 Prima decizie: ce tip de gestiune creezi

| | **En gros** | **Cu amănuntul** |
|---|---|---|
| Gestiunea se ține la | **preț de achiziție** | **preț de vânzare cu amănuntul (cu TVA)** |
| Conturi implicate | 371, 401 | 371, 401, **378**, **4428** |
| De ce | poți avea prețuri preferențiale pe client; urmărirea și descărcarea de gestiune sunt simple | vinzi la preț unic afișat; nu poți urmări fiecare bon |

✅ Argumentul din notițe e corect: la en gros ții la preț de achiziție tocmai **pentru că prețul de vânzare variază de la client la client**. Dacă ai ține la preț de vânzare, ar trebui să reevaluezi gestiunea la fiecare contract.

**Achiziția en gros:**
```
371         =  401            20.000
4426        =  401             4.200      (intern)
   sau  4426 = 4427            4.200      (intracomunitar)
```

### 8.2 Regula de aur a analiticelor

> **Fiecare gestiune de marfă se ține separat pe analiticul ei. Nu amesteci niciodată:**
> - gestiune cu 11% și gestiune cu 21%
> - gestiune en gros și gestiune cu amănuntul

✅ **De ce:** pentru că verificarea lui 4428 se face aplicând cota pe soldul gestiunii (vezi 8.6). Dacă amesteci cotele, corelația devine imposibil de verificat și nu mai poți spune dacă ai o eroare sau doar un mix de cote.

### 8.3 Importul — TVA în vamă, taxe vamale, transport

**Varianta A — plătești TVA-ul direct în vamă, prin bancă:**
```
4426        =  5121                       (TVA deductibil, plătit efectiv)
```

**Varianta B — prin comisionar vamal:**
```
4426        =  446                        (TVA-ul achitat de comisionar în numele tău)
446         =  401                        (îl datorezi comisionarului)
```
➕ Notița observa că a doua înregistrare „e puțin forțată, pentru că 446 e cont de pasiv". Corect — **446 „Alte impozite, taxe și vărsăminte asimilate"** funcționează aici ca un cont de tranzit. Alternativ, unele cabinete folosesc 461/462 pentru decontarea cu comisionarul. Ce contează e să fie **consecvent** și documentat în politici.

➕ **Varianta C, care lipsea:** societățile cu **certificat de amânare de la plata TVA în vamă** nu plătesc TVA-ul efectiv, ci aplică taxare inversă: `4426 = 4427`. Merită verificat dacă clientul îndeplinește condițiile — e un avantaj mare de cash-flow.

**Taxele vamale și transportul intră în costul mărfii** (OMFP 1802/2014 — costul de achiziție include taxele nerecuperabile, transportul, manipularea):
```
371         =  446            (taxe vamale)
371         =  401            (transport pe factură separată)
```

### 8.4 Capcana majoră: gestiunea ≠ contabilitatea

**Situația reală descrisă în notițe, formalizată:**

Softul de gestiune al clientului ia prețul din **invoice** (fără taxe vamale, fără transport). Contabilitatea înregistrează costul complet (**cu** taxe vamale și transport). Rezultat: **valoarea scriptică din contabilitate e mai mare decât cea din gestiune**. La inventariere, diferența iese la suprafață — și e prea târziu.

Efectele:
1. Valoare de inventar necorelată;
2. **Descărcare de gestiune greșită** — înregistrezi o cheltuială (607) diferită de cea reală;
3. Marja pe produs e falsă, deci și deciziile comerciale ale clientului.

> ⚠️ **Regula:** valoarea la care înregistrezi în 371 trebuie să fie **identică** cu valoarea din softul de gestiune din care clientul emite facturile către clienții lui.

**Exemplul din notițe:**
```
Factura furnizor:  100 lei
NIR:               130 lei
```
Nu accepți diferența, ci **întrebi**: de unde ies cei 30 lei? Răspunsul tipic: „am inclus taxe vamale + transport". Bine — atunci NIR-ul e corect, iar factura de transport **nu se mai înregistrează separat pe 624**, pentru că valoarea ei e deja în 371. Altfel dublezi cheltuiala și umfli prețul mărfii.

➕ **Cine își asumă ce:** dacă gestionarul face NIR-ul cu taxe vamale și transport incluse, el își asumă calculul. Rolul cabinetului e să valideze metoda, nu să o refacă. Dar metoda trebuie **stabilită în scris, la începutul colaborării**, nu descoperită în decembrie.

➕ Există sisteme care fac automat preluarea taxelor vamale și a transportului în prețul mărfii (repartizare pe cantitate sau pe valoare). Merită întrebat furnizorul de soft — economisește ore de reconciliere.

### 8.5 Încărcarea gestiunii cu amănuntul — exemple

**Exemplul 1 — cotă 21%**

Marfă 20.000 lei | adaos 20% | TVA 21%

```
371         =  %              29.040
  401                         20.000        (costul de achiziție)
  378                          4.000        (adaosul comercial: 20% × 20.000)
  4428                         5.040        (21% × 24.000)
```
> ⚠️ **TVA-ul se aplică la preț + adaos, nu doar la preț.** Statul încasează TVA și pe marja ta comercială.

| Cont | Sumă |
|---|---|
| 371 (debit) | **29.040** |
| 401 | 20.000 |
| 378 | 4.000 |
| 4428 | 5.040 |

**Exemplul 2 — cotă 11%** ⚠️ **corectat**

Marfă 20.000 lei | adaos 20% | TVA 11%

```
371         =  %              26.640
  401                         20.000
  378                          4.000
  4428                         2.640        (11% × 24.000)
```

⚠️ În notițe scria `4428 = 0,44` și total `371 = 29,04k`. **Ambele greșite.** 11% din 24.000 = **2.640**, iar totalul lui 371 = 20.000 + 4.000 + 2.640 = **26.640**. (Valoarea de 29.040 era copiată din exemplul cu 21%.)

| Cont | Sumă |
|---|---|
| 371 (debit) | **26.640** |
| 401 | 20.000 |
| 378 | 4.000 |
| 4428 | 2.640 |

### 8.6 Vânzarea și descărcarea de gestiune — răspunsul la `???`

Notițele se opreau la *„să presupunem că vindem integral această marfă — ???"*. Pe exemplul 1 (21%):

**(1) Vânzarea — încasare prin casierie:**
```
5311        =  %              29.040
  707                         24.000        Venituri din vânzarea mărfurilor
  4427                         5.040        TVA colectată
```

**(2) Descărcarea de gestiune — trei componente:**
```
%           =  371            29.040
  607                         20.000        Cheltuieli privind mărfurile (costul real)
  378                          4.000        adaosul aferent mărfurilor vândute
  4428                         5.040        TVA-ul devenit exigibil
```

**Verificare:**

| | |
|---|---|
| Sold 371 | 29.040 − 29.040 = **0** ✅ |
| Sold 378 | 4.000 − 4.000 = **0** ✅ |
| Sold 4428 | 5.040 − 5.040 = **0** ✅ |
| Marja | 707 − 607 = 24.000 − 20.000 = **4.000** = rulajul debitor 378 ✅ |

### 8.7 Corelațiile „sfinte"

Cele două verificări pe care le faci pe orice balanță cu gestiune cu amănuntul:

> **CORELAȚIA 1**
> ```
> Rulaj creditor 707 − Rulaj debitor 607 = Rulaj debitor 378
> ```
> Marja realizată din vânzări trebuie să fie exact adaosul descărcat din gestiune.

> **CORELAȚIA 2**
> ```
> Sold 371 × 21 / 121 = Sold 4428        (gestiune cu cotă 21%)
> Sold 371 × 11 / 111 = Sold 4428        (gestiune cu cotă 11%)
> ```
> TVA-ul conținut în stocul evaluat la preț de vânzare trebuie să fie exact soldul lui 4428.

⚠️ **Limitele corelației 1**, care nu erau menționate: nu se verifică dacă în cursul perioadei au existat reduceri comerciale primite/acordate ulterior facturării (609/709), diferențe de inventar, retururi sau transferuri între gestiuni. În aceste cazuri trebuie ajustată — nu concluziona automat că ai o eroare.

✅ **Și acesta este exact motivul pentru care gestiunile se separă pe cote.** Corelația 2 nu poate fi calculată pe o gestiune mixtă.

### 8.8 Coeficientul de repartizare a adaosului (K)

➕ **Completare necesară.** În practică, la sfârșit de lună nu știi direct care e adaosul aferent mărfurilor vândute (vinzi bon cu bon, nu pe loturi). Se calculează prin coeficientul K:

```
              Si 378 + Rc 378
K = ─────────────────────────────────────────────
     (Si 371 − Si 4428) + (Rd 371 − Rc 4428)
```
*(numitorul = valoarea mărfurilor la preț de vânzare, fără TVA)*

```
Adaos aferent mărfurilor vândute = K × Rulaj creditor 707
```

**Verificare pe exemplul 1:**
```
K = 4.000 / (0 + 29.040 − 5.040) = 4.000 / 24.000 = 0,1667
Adaos aferent vânzărilor = 0,1667 × 24.000 = 4.000   ✅
```

---

Metoda prețului cu amănuntul: marfa stă în gestiune la **prețul de vânzare cu TVA**, nu la cost. Diferența dintre cost și prețul de raft se ține în două conturi **rectificative** ale lui 371:

- **378** Diferențe de preț la mărfuri (adaosul comercial)
- **4428** TVA neexigibilă


### 8.9 Achiziția


Cost de achiziție 20.000 lei, TVA 11%, adaos comercial 20%.

```
371  = 401    ·  20.000     (costul de achiziție)
4426 = 401    ·   2.200     (TVA deductibilă, 11% × 20.000)

371  = 378    ·   4.000     (adaos comercial, 20% × 20.000)
371  = 4428   ·   2.640     (TVA neexigibilă, 11% × 24.000)
```

Atenție la baza TVA-ului neexigibil: se aplică la **marfă + adaos** (20.000 + 4.000 = 24.000), nu doar la cost.

Soldul lui 371 devine **26.640** = 20.000 + 4.000 + 2.640, adică exact prețul de raft cu TVA.


### 8.10 Vânzarea prin casierie


```
5311 = 707    ·  24.000     (venitul din vânzarea mărfurilor)
5311 = 4427   ·   2.640     (TVA colectată)
```


### 8.11 Descărcarea de gestiune


Se scot cele trei componente cu care a intrat marfa:

```
607  = 371    ·  20.000     (cheltuiala — costul de achiziție, fără adaos)
378  = 371    ·   4.000     (anularea adaosului)
4428 = 371    ·   2.640     (TVA devine exigibilă)
```

Total scos din 371: 26.640 — gestiunea se închide exact.

În practică se face ca articol contabil compus: `% = 371 · 26.640`.


### 8.12 Închiderea TVA la sfârșitul lunii


Situația conturilor înainte de închidere:

- 4426 TVA deductibilă → **2.200** debitor
- 4427 TVA colectată → **2.640** creditor

```
4427 = 4426   ·   2.200     (se compensează partea comună)
4427 = 4423   ·     440     (diferența rămasă = TVA de plată)
```

Dacă deductibilul ar fi fost mai mare decât colectatul, diferența mergea invers, în **4424 TVA de recuperat**: `4424 = 4426`.


### 8.13 Plata TVA


```
4423 = 5121   ·     440
```

**5121** este contul de bancă, indiferent de instrumentul folosit (ordin de plată, internet banking, mandat). Nu confunda: **5311** este casa în lei, iar **5111** este *Cecuri de încasat* — un cont de **încasări**, care nu are ce căuta într-o plată de TVA.

Dacă ai TVA de recuperat din luna anterioară (sold debitor pe 4424) și TVA de plată în luna curentă, se pot compensa:

```
4423 = 4424
```

Când marfa se depreciază (expiră, se demodează, se degradează), deprecierea nu se estimează după ureche: se **întrunește o comisie tehnică**, se face inventarierea, iar procentul (20%, 15%, 50% — după caz) se stabilește de comun acord și ajunge în contabilitate printr-un **proces-verbal**.

Ajustarea se înregistrează la valoarea din gestiune / prețul de achiziție.


### 8.14 Înregistrarea deprecierii


Cost de achiziție 20 lei, depreciere stabilită 30% → 6 lei.

```
6814 = 391    ·       6     (cheltuiala cu ajustarea)
```


### 8.15 Reluarea la venituri, la valorificarea bunului


Vine un cumpărător și dă 10 lei pe bun. În momentul în care bunul iese din gestiune, ajustarea nu mai are obiect și **legea obligă la reluarea ei la venituri**:

```
391  = 7814   ·       6
```

Conturile de ajustare funcționează **în oglindă**: `6814 ↔ 7814`.

**Logica, pe scurt:** la vânzarea bunului din gestiune, ajustarea se mută de pe 39\* într-un cont de venit, ca să compenseze cheltuiala deja înregistrată în luna în care s-a constituit ajustarea. Efectul pe rezultat: −20 (descărcare) +10 (venit din vânzare) +6 (reluarea ajustării) = **−4 lei**.


### 8.16 Regimul fiscal — atenție


Ajustările pentru deprecierea **stocurilor** sunt **nedeductibile fiscal**. Art. 26 din Codul fiscal enumeră limitativ provizioanele și ajustările deductibile, iar deprecierea stocurilor nu se regăsește acolo.

Corespunzător, **venitul din reluarea lor este neimpozabil** (art. 23 lit. d — veniturile din anularea cheltuielilor pentru care nu s-a acordat deducere). Cele două se neutralizează fiscal.

Deductibile — condiționat — sunt ajustările pentru deprecierea **creanțelor** (491, 496), în limitele și condițiile art. 26. Nu confunda cele două regimuri.


### 8.17 Inventarierea — nota de practică


De partea de inventariere răspunde **administratorul**, deci e la latitudinea lui. Dar un economist bun punctează aceste lucruri clientului, indiferent de mărimea firmei: pentru fiecare proprietar, afacerea lui este cea mai importantă, iar clientul trebuie să simtă că ai un interes real față de business-ul lui.

---

## 9. Ambalaje și obligațiile de mediu

### 9.1 Conturile

| Cont | Denumire |
|---|---|
| **381** | Ambalaje |
| **388** | Diferențe de preț la ambalaje |
| **358** | Ambalaje aflate la terți |
| **3023** | Materiale pentru ambalat |
| **608** | Cheltuieli privind ambalajele |
| **652** | **Cheltuieli cu protecția mediului înconjurător** |

### 9.2 Tipurile de ambalaj

✅ Corect în notițe, completez al treilea nivel:

| Tip | Definiție | Exemplu (vopsea) |
|---|---|---|
| **Primar** | în contact direct cu produsul | cutia metalică de vopsea |
| **Secundar** | grupează mai multe unități | cutia de carton cu 6 bucăți |
| **Terțiar** (de transport) | pentru manipulare și transport | **paletul, folia stretch** |

➕ Greșeala clasică: se declară doar primarul și secundarul și se uită **terțiarul** (paleții, folia). La import și achiziții intracomunitare, tocmai terțiarul e cel mai greu.

### 9.3 Contribuția la Fondul pentru Mediu

⚠️ **Corecție importantă de fond.** Notița spune „*2 lei/kg pentru cantitățile de ambalaje*". Nu se plătesc 2 lei pe fiecare kilogram introdus pe piață. Contribuția de **2 lei/kg** se datorează **doar pentru diferența** dintre:
- cantitatea de deșeuri corespunzătoare **obiectivului minim de reciclare/valorificare**, și
- cantitatea efectiv reciclată/valorificată.

Dacă îți atingi obiectivul, contribuția este **zero**.

**Două variante de conformare:**

| Variantă | Cum funcționează |
|---|---|
| **Individual** | îndeplinești singur obiectivele, raportezi și plătești diferența la AFM |
| **Prin OIREP/OTR** | transferi responsabilitatea unei organizații autorizate, plătești tarif lunar, ea îți furnizează raportul de reciclare |

A doua e varianta uzuală și de regulă mai ieftină.

**Declarația privind obligațiile la Fondul pentru mediu** se depune la AFM (evidența ambalajelor se ține lunar; raportarea/plata urmează calendarul AFM în vigoare — **verifică termenul curent pe afm.ro**, s-a modificat de mai multe ori).

**Înregistrare când găsești o plată către AFM în extras:**
```
652         =  5121
```
⚠️ Dar nu o înregistrezi mecanic. **Întrebi întâi: pentru ce s-a plătit?** Ambalaje? Ecotaxă pentru pungi? Anvelope? EEE? Fiecare are declarație și evidență proprie. O plată către AFM înseamnă că există o obligație declarativă în spate — și de multe ori clientul nu știe că o are.

### 9.4 Beculețul care trebuie să se aprindă

✅ Cea mai utilă observație practică din notițe, formalizată:

> **Ai o tranzacție intracomunitară sau un import? Uită-te pe CMR / factură la diferența dintre greutatea netă și cea brută. Diferența = ambalaj introdus pe piața din România = posibilă obligație la AFM.**

Exemplul din notițe: firmă care aduce PAL și MDF din Austria — a ajuns să plătească pentru paleții aduși pe teritoriul României. Controalele în vamă sunt frecvente exact pentru că autoritatea are informația brut/net direct pe documentele de transport.

➕ **Trei întrebări de pus clientului la deschiderea dosarului:**
1. Aveți contract cu un OIREP pentru transferul responsabilității?
2. Cine ține evidența ambalajelor introduse pe piață, pe tip de material?
3. Cine depune declarația la AFM și de când?

---

## 10. Atitudinea profesională — nu e o notă filozofică

⚠️ Abordarea „*nu mă interesează mediul / statistica / resursele umane*" este descurajată explicit — și are un motiv practic, nu moral.

**Motivul:** clientul nu are cum să știe ce nu știe. Ai la dispoziție, în munca ta zilnică, informația care declanșează obligația:
- vezi CMR-ul → știi că are ambalaje de declarat;
- vezi extrasul → știi că a plătit la AFM;
- vezi factura de import → știi că are taxe vamale de inclus în cost.

**Cine altcineva are toate aceste informații într-un singur loc? Nimeni.**

Reacția clasică a clientului la o amendă este *„nu mi-a spus contabilul"*. Fie că e drept sau nu, asta e percepția — iar bariera pe care o ridici („nu e treaba mea") nu te protejează, ci doar amână discuția.

**Consecința operațională:** dacă în cabinet ai informația, transmite-o mai departe — colegilor și clientului. În scris. Un e-mail de trei rânduri care semnalează o obligație valorează mai mult decât orice clauză contractuală.

---

## 11. Furnizori și clienți — clasele 40 și 41
### 11.1 Contul 408 — Furnizori, facturi nesosite


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


### 11.2 Varianta completă, cu TVA


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


### 11.3 De ce 408 este un cont periculos


Când livrezi cu aviz, legea cere ca **factura să menționeze numărul avizului**. Dacă cel care a întocmit factura nu a fost atent și factura nu se împerechează cu avizul — iar tu nu sesizezi — înregistrezi materii prime a doua oară și **dublezi gestiunea**.

Contabilitatea primește documente fără să aibă legătură cu ce se întâmplă pe teren. De aceea:

- trebuie să știi permanent **ce facturi sunt înregistrate pentru ce avize**;
- închiderea facturilor pe furnizori prin 408 se urmărește activ;
- la orice dubiu, se sună clientul. El știe cel mai bine ce se întâmplă în curtea lui și clarifică în câteva secunde ceea ce ție ți-ar lua ore.


### 11.4 Contul 409 — Furnizori-debitori (avansuri plătite)


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


### 11.5 Regula generală pe clasa 40


La toate înregistrările care țin de furnizori (40\*) avem **TVA deductibilă (4426)** — și putem avea și **taxare inversă**.

---

### 11.6 Contul 411 și legătura cu veniturile


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


### 11.7 Contul 418 — Clienți, facturi de întocmit


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


### 11.8 Avans încasat de la client


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

## Anexa A — Recapitulare: conturi și perechile lor

### Stocuri și cheltuieli

| Stoc | Cheltuială | Observație |
|---|---|---|
| 301 Materii prime | 601 | producție |
| 3021 Materiale auxiliare | 6021 | |
| 3022 Combustibili | 6022 | |
| 3023 Materiale pentru ambalat | 6023 | |
| 3024 Piese de schimb | 6024 | poate fi transferat în 371 dacă se revinde |
| 3028 Alte materiale consumabile | 6028 | |
| 303 Obiecte de inventar | 603 | **+ Debit 8035 simultan** |
| 371 Mărfuri | 607 | |
| 381 Ambalaje | 608 | |

### Producție și venituri

| Stoc produs | Venit variație | Venit vânzare |
|---|---|---|
| 331 Produse în curs | 711 | — |
| 332 Servicii în curs | 712 | — |
| 341 Semifabricate | 711 | 702 |
| 345 Produse finite | 711 | **7015** |
| 346 Produse reziduale | 711 | 703 |
| 347 Produse agricole | 711 | 7017 |

### În curs de aprovizionare

```
321 → 301      322 → 302      323 → 303
326 → 361      327 → 371      328 → 381
```

### TVA

```
4423  TVA de plată            4426  TVA deductibilă      4428  TVA neexigibilă
4424  TVA de recuperat        4427  TVA colectată
```

### Extrabilanțiere

```
8035  Stocuri de natura obiectelor de inventar date în folosință
```

---

## Anexa B — Checklist practic (de rulat la fiecare client)

**La deschiderea dosarului**
- [ ] Metoda de evidență a stocurilor (permanent / intermitent) e stabilită și scrisă în politicile contabile?
- [ ] Gestiunile sunt separate pe: cotă de TVA (11 / 21) și tip (en gros / amănuntul)?
- [ ] Valoarea de înregistrare în 371 = valoarea din softul de gestiune al clientului? (taxe vamale, transport)
- [ ] Clientul are contract cu un OIREP pentru ambalaje? Cine depune declarația la AFM?
- [ ] Softul listează obiectele de inventar date în folosință (8035) pentru inventariere?
- [ ] Softul verifică automat codul de TVA al partenerilor la ANAF? Și TVA la încasare, la închidere?

**La fiecare factură de la furnizor nou**
- [ ] Partener înregistrat în scopuri de TVA la **data facturii**? (registru ANAF, nu Google)
- [ ] Partener UE — cod valid în VIES?
- [ ] Dacă apare „taxare inversă": ambii parteneri sunt plătitori de TVA?
- [ ] Dacă nu e cota standard: e înscris articolul de lege pe factură?
- [ ] Import: taxele vamale și transportul sunt incluse în costul mărfii?

**La închiderea lunii**
- [ ] Rulaj 4426 = TVA din jurnalul de cumpărări?
- [ ] Rulaj 4427 = TVA din jurnalul de vânzări?
- [ ] Ajustările fără document (50% auto, lipsă la inventar) apar în jurnale?
- [ ] `707 − 607 = Rd 378`?
- [ ] `Sold 371 × cotă/(100+cotă) = Sold 4428`, pe fiecare gestiune?
- [ ] 4426 și 4427 s-au regularizat în 4423/4424?
- [ ] 331 e evaluat la cost de producție complet (nu doar materiale)?
- [ ] Există 602x fără 302x corespondent? (semn că s-a trecut direct pe cheltuială)

---

## Anexa C — Ce am corectat față de notițele originale

| # | Notița originală | Corecția |
|---|---|---|
| 1 | `301 = 401` cu TVA, fără 4426 | formula compusă: `% = 401` cu 301 și 4426 |
| 2 | Taxare inversă: `301 = 401 + 4427` | `301 = 401` **și separat** `4426 = 4427` |
| 3 | „nedepunere D300 **2 luni** consecutive" | **6 luni** consecutive / 2 trimestre (art. 316 alin. 11 lit. d) |
| 4 | „verificăm pe Google" | registrele oficiale ANAF + VIES |
| 5 | „301 cuplat cu **704** și 7015" | 704 = servicii prestate; corect **7015** și 711 |
| 6 | „>1 an durată, chiar dacă <5.000 ⟹ mijloc fix" | condițiile sunt **cumulative**; sub prag = obiect de inventar |
| 7 | prag 5.000 fără context | OUG 8/2026, de la 25.02.2026, **prag fiscal**, cu regim tranzitoriu |
| 8 | audit: „balanța analitică la **401** — debit achiziții, credit consum" | corelația debit=intrări / credit=consum e la **conturile de stoc 3xx** |
| 9 | lipsea `302 = 322` din corespondențele 32x | tabel complet 321–328 |
| 10 | „taxare inversă: și furnizorul și cumpărătorul nu mai deduc" | furnizorul **nu colectează**; beneficiarul înregistrează **și** 4426 **și** 4427 |
| 11 | „imobile noi vândute între societăți" | construcții/terenuri taxabile **prin lege sau prin opțiune** |
| 12 | `331/332` cu `711/**722**` | perechea lui 332 este **712**; 722 = producția de imobilizări corporale |
| 13 | „soft făcut cu salariații" la 331/332 | software intern = **233 → 721 → 203/208**, nu stoc |
| 14 | `sticlă: 301 = 601 50k` | achiziția e `301 = 401`; consumul e `601 = 301` |
| 15 | `4111 = ?` la vânzarea produsului finit | `4111 = % (7015 + 4427)` **plus** `711 = 345` |
| 16 | 4424 „de rambursat" | denumire oficială: **TVA de recuperat** |
| 17 | „clasa 6 și 7 fără sold, **excluzând 711**" | 711 se închide la 121 ca oricare; particularitatea e că are rulaje bidirecționale |
| 18 | lipsă la inventar: „colectez TVA" | depinde: imputabilă → colectare; neimputabilă → **ajustare** |
| 19 | 4428 la amănuntul explicat ca „dau TVA când încasez" | exigibilitatea e **la vânzare**, nu la încasare — altceva decât TVA la încasare |
| 20 | Ex. 2 (11%): `4428 = 0,44` și `371 = 29,04k` | `4428 = 2.640`, `371 = **26.640**` |
| 21 | „2 lei/kg pentru cantitățile de ambalaje" | 2 lei/kg **doar pe diferența** neatinsă față de obiectivul de reciclare |
| 22 | 346 „mai departe trebuie să fac factură" | factura către colectorul de deșeuri intră la **taxare inversă** |
| 23 | „să vindem integral marfa — ???" | rezolvat integral în 8.6 |

---

### Corecții la materialul din 19.08.2026

Cifrele fiecărui exemplu din sursă au fost refăcute. Cinci din șase se leagă exact:
gestiunea la preț cu amănuntul (26.640 la intrare și la descărcare), avansul de client
(121.000 − 36.300 = 84.700), vânzarea mijlocului fix (38.000 + 12.000 = valoarea de
intrare), supraîncasarea (4.132,23 + 867,77 = 5.000) și închiderea 408/4428 la zero.
Mai jos, ce nu s-a legat.

| # | În sursă scria | Corect | De ce contează |
|---|---|---|---|
| 1 | `391` — „Ajustări pentru deprecierea mărfurilor” | **`397`** | În OMFP 1802/2014, `391` e pentru materii prime, iar `397` pentru mărfuri. Planul nostru le are pe amândouă, denumite corect, iar F-307 folosea deja `397`. Simbolul din sursă intra în coliziune directă cu ce aveam. |
| 2 | avans furnizor 50.000, stornat cu `4091 = 401 · −30.000` | storno pe suma avansului, **plus `4426 = 401 · −10.500`** | Sursa sare de la 50.000 la 30.000 fără explicație, iar stornarea TVA lipsește cu totul. Fără ea rămâne TVA dedusă pe un avans anulat. |
| 3 | „La încasarea avansului” urmat doar de `4111 = 419` și `4111 = 4427` | plus **`5121 = 4111 · 36.300`** | Titlul spune încasare, dar dedesubt sunt doar înregistrările de facturare. Fără pasul de încasare, 4111 rămâne cu sold și fluxul nu are stare terminală — ceea ce poarta 2 refuză. |
| 4 | `408` și `418` — „bifuncționale” | `408` = **P**, `418` = **A** | Observația practică e corectă: pot ajunge cu sold contrar. Dar ce descrie sursa nu e *funcțiunea* contului, e **rolul în flux** — intermediar/clarificare. Distincția e chiar grila acestui sistem, iar amestecarea lor face 408 să pară că are voie să stea oricum. |
| 5 | §2 la cota de **11%**, restul materialului la **21%** | ambele corecte, dar motivul lipsea | Fără explicație, cititorul poate lua 11% drept „cota la mărfuri”. 11% e cota redusă (alimente, cărți, medicamente), 21% cea standard — L. 141/2025. |
| 6 | „Efectul pe rezultat: −20 +10 +6 = **−4 lei**” | −4 e efectul **lunii vânzării** | Cumulat, pierderea reală e −10: bun cumpărat cu 20, vândut cu 10. Cei 6 lei ai ajustării au lovit rezultatul în luna constituirii. Afirmația nu e greșită, e neterminată — și fără precizare pare că pierderea totală ar fi 4.|

Punctele 1–3 sunt erori de conținut. Punctul 4 e o confuzie de vocabular cu efect real
asupra controlului. Punctele 5–6 sunt afirmații incomplete, nu greșite.

## Anexa D — Rămase deschise

1. **Metoda de calculație a costurilor** — notița menționa „metoda pe comenzi" ca fiind des utilizată. De clarificat: care sunt celelalte metode acceptate de OMFP 1802/2014 și în ce situații se alege fiecare (pe faze, pe produs, standard-cost)?

2. **Lipsă la inventar** — care e practica default în cabinet: colectare sau ajustare? Ce set de documente se cere clientului (proces-verbal, decizie de imputare, notă de constatare)?

3. **446 vs. 462 la comisionarul vamal** — care variantă e standardul cabinetului și de ce?

4. **Certificat de amânare la plata TVA în vamă** — se verifică sistematic dacă clienții importatori îndeplinesc condițiile?

5. **Termenul curent de depunere a declarației la AFM** — s-a modificat de mai multe ori (lunar / trimestrial). De confirmat forma în vigoare.

6. **Notița „Fișierul atașat arată corelații importante între conturi"** și marcajul **„task"** — au rămas fără conținut în notițele originale. De recuperat de la formator ce fișier / ce sarcină era.

7. **Durata de aplicare a taxării inverse** pentru cereale și electronice — derogarea UE avea termen 31.12.2026. De verificat dacă a fost prelungită.

---

## Anexa E — Baza legală citată

| Act | Ce reglementează |
|---|---|
| Legea 227/2015 — Codul fiscal | art. 28 (amortizare), 270 (livrări asimilate), 292 (scutiri imobile), 294 (scutiri LIC/export), 298 (limitare 50% auto), 304–305 (ajustări), 316 (înregistrare/anulare TVA), 319 (facturare), **331 (taxare inversă)** |
| **OUG 8/2026** (M.Of. 147/25.02.2026) | majorarea pragului mijloacelor fixe la 5.000 lei |
| **Legea 141/2025** (M.Of. 699/25.07.2025) | cotele de TVA 21% / 11%, de la 01.08.2025 |
| OMFP 1802/2014 | reglementările contabile, planul de conturi, costul de achiziție și de producție |
| OUG 196/2005 + Legea 249/2015 | Fondul pentru mediu, ambalaje, contribuția de 2 lei/kg |
| Ordinul 3769/2015 | formularul D394 |

---

*Document revizuit pe baza notițelor din 14.08.2026. Verificările legislative au fost făcute la data revizuirii — reconfirmă orice prag sau cotă înainte de aplicare la un caz concret.*

---

## Anexa F — Erori din notițele brute, NEreintroduse

Erorile de mai jos existau în notițele brute și au fost corectate
la revizuire. Sunt enumerate aici ca să nu fie reintroduse dacă cineva reia notițele
originale.

| Eroare în notițele brute | Corect |
|---|---|
| `7815` ca reluare a amortizării | Contul nu există. Amortizarea se înregistrează `6811 = 2805/2808` |
| Taxele vamale pe `635` | Se capitalizează în costul bunului (OMFP 1802/2014) |
| Softul dezvoltat intern prin `711` | Imobilizare necorporală: `233 → 721 → 203/208` |
| Salariile capitalizate în `231` prin `711` | Prin `722` — producție de imobilizări corporale |
| `2114` ca mobilier | Contul este `214` |
| CASCO nedeductibil pe `615` | Pe `613.NED` — partea nedeductibilă a asigurării |
| `1067` la leasing | Contul este `167` |
| `4424` la corecția TVA nedeductibilă | Contul este `4426` |


---

*Singurul care avea deja anexele denumite. Primește Anexa F, care exista doar ca notă în foaia Legendă a workbook-ului.*
