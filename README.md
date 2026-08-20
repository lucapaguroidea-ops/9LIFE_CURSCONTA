# 9LIFE — sistem Excel de notițe de contabilitate (curs conta)

Acest depozit transformă notițele de la cursurile de contabilitate într-un instrument
de lucru pentru cabinet + învățare: o pereche de workbook-uri Excel legate, generate
reproductibil din scripturi.

Metoda a fost stabilită la **trainingul 4** (14.08.2026, stocuri + TVA). Aici o
reproducem și o extindem la **trainingul 2** (07.08.2026, capitaluri) și **trainingul 3**
(12.08.2026, imobilizări), în același sistem — un singur graf navigabil, fără fișiere
paralele care divergează.

## Cele două workbook-uri

| Fișier (în `dist/`) | Rol |
|---|---|
| `Plan_de_conturi_ROL_Analitice_Fluxuri_SAGA.xlsx` | **referință** — planul de conturi clasificat pe *rol*, fluxurile cu pași, corelațiile de control, matricea de acoperire |
| `Module_Declarative_Fluxuri.xlsx` | **execuție** — module `Declarații → Reguli → Jurnale → NotaExport` care produc note contabile din câteva variabile de input |

### Ideea centrală: clasificarea pe *rol*

Fiecare cont primește un rol funcțional (grilă pentru control și înțelegere, **nu**
clasificarea oficială A/P). Ori **ține ceva real** (patrimonial: activ, datorie, capital,
cheltuială, venit), ori **face un serviciu în flux**: tranzit, intermediar/clarificare,
rectificativ/contra, regularizare temporală, neutralizare rezultat, colectare rezultat,
decontare internă, extrabilanțier/memorie, tehnic de închidere.

Fiecare cont cu rol în flux are un **flux didactic** cu un **pas revelator** care îi
demonstrează rolul pe cifre. Analiticele nu se recomandă „de frumusețe”: fiecare are un
**factor** — `D` declarativ / `N` normativ / `C` corelație / `F` fiscal / `B` bilanț /
`V` valută / `O` operațional. Fără factor → fără recomandare.

### Corelațiile „sfinte” și porțile de calitate

Un flux e valid doar dacă: `ΣDebit = ΣCredit` pe fiecare pas · se închide într-o **stare
terminală** declarată · fiecare cont din antet apare într-un pas real · fiecare cont cu rol
în flux are un pas revelator. Corelațiile (`Corelații de control`, C-01…C-22) se verifică
**pe cifrele fluxului**, nu declarativ, și disting explicit *ce rupe o corelație legitim*
de *ce o rupe suspect*.

## Structura depozitului

```
surse/         notițele fiecărui training (.txt brut + .md revizuit + .docx) și,
               pentru training 4, cele două xlsx originale — folosite ca bază („seed”)
date/          CONȚINUTUL NOU, separat de cod (structuri Python, ușor de citit în diff)
  fluxuri.py       F-45…F-62 (capitaluri + imobilizări)
  corelatii.py     C-13…C-22
  analitice.py     conturi clasa 1 și 2 promovate la Tier A
  plan.py          conturi noi / actualizări de coloană „Flux (pas)”
  module/          definițiile celor 9 module declarative noi
  ordine.py        ordinea canonică: singura sursă de adevăr pentru poziții și ID-uri
  intrebari.py     cele 21 de întrebări deschise (o sursă → .md, .html și foaia din workbook)
  parcurs.py       partea scrisă de mână a documentului de parcurs
build/         generatoarele
  stil.py          paleta exactă a workbook-urilor originale
  build_plan.py    surse/…Plan…xlsx  → dist/…Plan…xlsx  (extindere non-distructivă)
  build_module.py  surse/…Module…xlsx → dist/…Module…xlsx
  recalc.py        recalc pur-Python (vezi mai jos)
  parcurs.py       dist/parcurs-training-nou.md (straturile generate)
  verifica.py      porțile de calitate; cod de ieșire ≠ 0 la eșec
dist/          xlsx-urile, documentele și listele generate (commit-ate)
```

## Cum se construiește

```sh
make build      # generează dist/*.xlsx din surse/ + date/
make verifica   # rulează porțile de calitate pe dist/*.xlsx
make tot        # build + documente + întrebări + parcurs + verifica
```

Necesită `openpyxl`, `formulas`, `numpy` (`pip install openpyxl formulas numpy`).

## Ce conține sistemul acum

Sistemul e ordonat după **planul de conturi**, nu după ordinea în care au fost adăugate
trainingurile. ID-ul unui flux codifică clasa contului principal, deci un flux adăugat
peste un an primește următorul număr liber din clasa lui și stă fizic la locul lui.

| Bloc | Conținut | Fluxuri |
|---|---|---|
| `F-1xx` | capitaluri, provizioane, împrumuturi, închiderea exercițiului, leasing | 8 |
| `F-2xx` | imobilizări: intrare pe grupe → în curs → regie proprie → subvenții → ieșiri → control analitic↔sintetic | 14 |
| `F-3xx` | stocuri și producție: aprovizionare, obiecte de inventar, producție, mărfuri, import | 20 |
| `F-4xx` | terți și TVA: TVA la încasare, taxare inversă, închidere lunară, 408/418, salarii | 14 |
| `F-5xx` | trezorerie | 2 |
| `F-8xx` | conturi în afara bilanțului | 2 |

**16 module declarative**, fiecare cu `Declarații → Reguli → Jurnale → NotaExport` și
celule `Check`. Niciunul nu mai e „exemplu extern”: `MOD_LEASING_FIN`, `MOD_SALARII` și
`MOD_DECONT` au devenit interne, cu cifrele verificate contra fișierelor reale, iar
`MOD_CREDIT_VALUTA`, `MOD_PROVIZION` și `MOD_SUBVENTIE` acoperă fluxurile care aveau
monografie dar nu și motor executabil.

23 corelații de control, 58 de conturi Tier A cu analitice justificate.

### Foaia `Închideri periodice`

Disciplina de închidere — ce cont, la ce cadență, cu ce stare terminală. Nu e o listă
scrisă de mână: aserțiunile există deja în monografii, în pașii de verificare (`F-405`:
„Sold 4426 = 0; sold 4427 = 0”, `F-501`: „Sold 581 = 0”), iar foaia le **citește** de
acolo. De mână rămâne doar cadența — un flux spune ce stare atinge contul, nu cât de des
te uiți la el.

Poarta 17 leagă cele două sensuri. Sensul invers a găsit imediat două conturi de tranzit
pe care notițele le omiseseră: `327` și `223`, ambele „în curs de aprovizionare”, ambele
cu „sold = 0” declarat în monografie. Conturile fără flux în spate apar în foaie **fără
ancoră**, cu motivul scris — un checklist care afirmă ceva ce sistemul nu demonstrează e
mai rău decât unul incomplet.

## Ce mai produce repo-ul, pe lângă workbook-uri

| Livrabil | Ce e |
|---|---|
| `dist/intrebari-formator.md` + `.html` | cele 21 de întrebări rămase deschise, grupate pe temă contabilă, cu context și cu ce s-a presupus între timp |
| `dist/stocuri-tva-corelatii.md`, `imobilizari.md`, `capitaluri-credite-provizioane.md`, `control-documente-numerar.md` (+ `.docx` + `.html`) | cele patru documente revizuite, **titrate pe subiect, nu pe ziua de training** — un document care crește cu material din mai multe zile nu mai poate purta cinstit o dată |
| `dist/parcurs-training-nou.md` | parcursul pe care trebuie să-l urmeze **următorul set de notițe** — vezi mai jos |

Documentele din `surse/` rămân neatinse — acolo stau variantele tale originale.
În `.html`, monografiile nu sunt text preformatat: trec prin același parser ca poarta 18
și ies ca **registru** — debit, credit, sumă aliniată la dreapta, storno în roșu, cu
ancoră pe fiecare înregistrare. Randarea și verificarea citesc aceeași structură, deci
nu pot diverge; un `.html` convertit separat devine al doilea adevăr.

`.docx`-urile generate **nu** reproduc identic pe cele existente (acelea vin din alt
lanț, cu fonturi încorporate); sunt însă consistente între ele.

## Invariantul: cont → flux → modul → întrebare

Sistemul se navighează în lanț, iar fiecare verigă e **derivată**, nu scrisă de mână:

- din `Plan de conturi`, coloana „Flux (pas)” duce la fluxurile contului;
- din `Fluxuri`, `Corelații de control` și `Matrice acoperire`, ancora `modul: MOD_…`
  duce la motorul care produce nota. Legătura se deduce din `CATALOG["fluxuri"]` al
  fiecărui modul — o hartă scrisă separat ar fi al doilea adevăr, care diverge;
- marcajul `❓ Î-nn` duce la foaia `Întrebări deschise`, unde scrie ce anume din acea
  regulă e încă provizoriu și ce s-a presupus între timp.

Ultima verigă contează: restul workbook-ului prezintă regulile ca tranșate. Unde nu
sunt, marcajul o spune acolo unde te uiți.

## Cum crește sistemul

Un training nou **nu se lipește la coadă**. Se adaugă la clasa lui:

1. fluxul nou intră în lista clasei din `date/ordine.py`, la locul lui contabil, cu
   următorul număr liber din clasă (`ordine.urmatorul_liber(3)`);
2. monografia se scrie în `date/fluxuri_*.py`;
3. `make tot` reordonează, renumerotează și verifică.

Catalogul de fluxuri e **derivat** din monografii, deci nu poate rămâne în urma lor.

### `dist/parcurs-training-nou.md`

Parcursul complet al unui set nou de notițe — de la fișierul brut până la workbook.
E un document de **îndrumare**, nu de explicare: unde există poartă, spune „poarta N
verifică asta” și se oprește. Regulile contabile rămân în documentele de referință, ca
să nu existe un al doilea adevăr care să diveargă de ele.

Are două straturi. Cel scris de mână (`date/parcurs.py`) ține doar ce nu se poate deduce
din cod: întrebările de judecată ale fazei A, punctele de convergență, traseul real al
trainingului 3. Cel generat (`build/parcurs.py`) ține tot ce enumeră starea sistemului —
lista porților, harta claselor, modulele, fișierele din `date/` — citit din cod și din
workbook-urile construite. Harta documentelor de referință nu e nici măcar scrisă: e
chiar tabelul de structură din foaia `Legendă`.

Miezul lui e secțiunea **puncte de convergență**: cele 12 locuri unde un training nou
poate rupe coerența. Opt sunt prinse de câte o poartă și sunt enumerate ca să nu te uiți
degeaba după ele; **patru sunt goluri cunoscute**, marcate „nimic — verifică tu”.

## Porțile de calitate

`make verifica` rulează 19 porți; toate trebuie verzi:

1. ΣDebit = ΣCredit pe fiecare pas de flux cu sume
2. fiecare flux se închide cu stare terminală declarată și un „Principiul:”
3. fiecare flux didactic ★ are exact un pas revelator
4. matricea de acoperire nu are goluri nedeclarate
5. fiecare analitic Tier A are un factor din `D/N/C/F/B/V/O` și spune ce se rupe fără el
6. fiecare token `MOD_*` referit există în `CatalogModule` (verificare între fișiere)
7. corelațiile se recalculează pe cifrele fluxurilor, nu declarativ
8. formule echilibrate; zero erori; toate celulele `Check` = OK; nicio celulă de text scrisă din greșeală ca formulă
9. **conservare** — vezi mai jos
10. catalogul acoperă fix monografiile
11. zero nume definite rupte
12. conservare pe documentele revizuite — nicio linie pierdută la armonizare
13. documentele au aceeași legendă și anexe canonice, în ordine
14. tabelul de structură din Legendă cunoaște toate foile workbook-ului
15. documentul de parcurs nu citează foi, fișiere sau porți care nu există — și lista
    canonică de porți din `build/verifica.py` coincide cu porțile chemate efectiv
16. **repartizare** — o sursă împărțită pe mai multe destinații nu pierde nimic în
    cusătură: fiecare subsecțiune are destinație declarată și ajunge exact acolo
17. disciplina de închidere e ancorată în ambele sensuri: fiecare cont urmărit periodic
    e starea terminală a unui flux, iar fiecare cont cu rol în flux care se golește are
    o cadență — sau un motiv declarat pentru care nu are
18. **monografiile scrise în proză** se echilibrează, iar aritmetica afirmată în text
    („5% din 250 = 12,50”) chiar se verifică — acolo unde poarta 1 nu ajunge
19. marcajul ❓ e **aplicat**, nu doar definit: un document pe care o întrebare deschisă
    îl privește îl poartă, iar un document care îl poartă are întrebări deschise

### Poarta de repartizare

Poarta 12 verifică perechea document ↔ sursa lui. Când o singură sursă hrănește patru
destinații, fiecare document poate trece poarta 12 separat **în timp ce material cade
între ele**. Riscul nu e „nimeni n-a luat-o”, ci *„am crezut că a luat-o celălalt”*.

`date/repartizare.py` declară împărțirea înainte de a fi făcută — fiecare subsecțiune cu
destinația și **motivul** ei. Destinația nu e mereu un document: tabelul de conturi
aparține planului, întrebările deschise listei de întrebări, disciplina de închidere foii
care o ține.

Verificarea pe *reuniunea* destinațiilor ar spune doar că textul există pe undeva — exact
întrebarea greșită. Poarta compară cu destinația **declarată**.

### Poarta de conservare

Cea mai importantă. Verifică faptul că **fiecare linie de text din workbook-urile
originale se regăsește în cele generate** — ca *mulțime*, nu ca ordine, tocmai ca
reordonarea să fie liberă iar pierderea de conținut să fie imposibilă. Renumerotarea nu
contează ca pierdere: textul original trece prin harta `F-vechi → F-nou` înainte de
căutare.

Un text care chiar trebuie înlocuit se declară în `date/reformulari.py`, **cu motiv**.
Fără declarație, build-ul pică. Cele 34 de înlocuiri declarate apar și în foaia
`Istoric`, cu textul original alături de cel nou.

Poarta a prins imediat 12 linii pe care o etapă anterioară le pierduse prin „actualizări
în loc”. De aceea actualizarea unei celule se face acum prin **contopire**: ce era acolo
rămâne, noul conținut se adaugă. Clasa asta de pierdere a devenit imposibilă, nu doar
reparată o dată.

## Defecte preexistente, găsite la citirea integrală

| Defect | Remediu |
|---|---|
| **13 din 44 de fluxuri nu aveau rând de catalog** — `F-08…F-14` fuseseră împinse afară de un bloc orfan `F-07`, `F-39…F-44` nu fuseseră adăugate niciodată | catalogul se generează din monografii |
| **`F-07` duplicat** — pașii 2 și 3 apăreau de două ori, cu aceleași cifre și formulare diferită | deduplicat; formularea eliminată e păstrată verbatim în `Istoric` |
| **`F-18` fără antet** — pașii lui pluteau după blocul `F-16`, deci fluxul nu era vizibil ca entitate | a primit titlu și antet proprii |
| **contul 235 purta denumirea lui 233**, iar 233 lipsea din plan | corectat; 233 adăugat |

## O corecție aplicată planului original

Contul **235** purta denumirea contului **233**. Conform OMFP 1802/2014:
231 = imobilizări corporale în curs, 233 = imobilizări necorporale în curs,
235 = investiții imobiliare în curs. Contul 233 lipsea complet din plan și a fost adăugat
(training 3 îl folosește pentru softul dezvoltat intern). Corecția e vizibilă în foaia
`Legendă` și în observația contului.

## Două decizii de proiectare (abateri conștiente, documentate)

1. **Extindere pe bază de seed, nu regenerare completă.** Generatoarele **încarcă**
   workbook-urile originale din `surse/training-4-…/` și **adaugă conținut nou la finalul
   fiecărei foi**, non-distructiv. Astfel conținutul original din training 4 e păstrat
   1:1 (fără riscul de a re-transcrie manual 246 de conturi), iar diff-ul e pur aditiv.
   `date/` ține doar ce e nou. La training 5: adaugi în `date/`, rulezi `make tot`.

2. **Recalc pur-Python în locul LibreOffice.** Fișierele originale au fost salvate cu
   LibreOffice, care cache-uiește valorile formulelor. LibreOffice headless **nu
   funcționează** în mediul acesta (filtrele de conversie nu se încarcă), așa că
   `build/recalc.py` face recalc-ul cu biblioteca `formulas`: setează
   `fullCalcOnLoad=True` (orice aplicație reală recalculează la deschidere) **și**
   injectează valorile calculate în XML-ul foilor, păstrând stilurile. Rezultatul:
   fișierul arată complet și în vizualizatoare care nu recalculează.

## Sursa de adevăr

Pentru trainingurile 2 și 3, **documentele `.md` revizuite** din `surse/` sunt sursa de
adevăr, nu `.txt`-urile brute — `.md`-urile au deja corectate erorile din notițele de
mână (ex. soft dezvoltat intern se capitalizează prin **721**, nu 711; salariile proprii
din imobilizări în curs prin **722**; operațional vs. financiar la leasing). `.txt`-urile
brute se păstrează doar ca trasabilitate.
