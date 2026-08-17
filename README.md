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
  module/          definițiile celor 4 module declarative noi
build/         generatoarele
  stil.py          paleta exactă a workbook-urilor originale
  build_plan.py    surse/…Plan…xlsx  → dist/…Plan…xlsx  (extindere non-distructivă)
  build_module.py  surse/…Module…xlsx → dist/…Module…xlsx
  recalc.py        recalc pur-Python (vezi mai jos)
  verifica.py      porțile de calitate; cod de ieșire ≠ 0 la eșec
dist/          cele două xlsx generate (commit-ate)
```

## Cum se construiește

```sh
make build      # generează dist/*.xlsx din surse/ + date/
make verifica   # rulează porțile de calitate pe dist/*.xlsx
make tot        # build + verifica
```

Necesită `openpyxl`, `formulas`, `numpy` (`pip install openpyxl formulas numpy`).

## Ce conține sistemul acum

| | Training 4 (existent) | + Etapa 4 (traininguri 2 și 3) |
|---|---|---|
| Fluxuri | F-01…F-44 | **+18** → F-45…F-62 |
| Corelații de control | C-01…C-12 | **+10** → C-13…C-22 |
| Conturi Tier A cu analitice | 37 | **+21** (clasele 1 și 2) |
| Module declarative | 7 implementate | **+4** (LEASING_FIN, IMOBILIZARI, IESIRE_MF, CAPITALURI) |

Porțile de calitate rulate de `make verifica`:

1. ΣDebit = ΣCredit pe fiecare pas de flux cu sume
2. fiecare flux se închide cu stare terminală declarată și un „Principiul:”
3. fiecare flux didactic ★ are exact un pas revelator
4. matricea de acoperire nu are goluri nedeclarate; marcajele promise ca rezolvate chiar sunt
5. fiecare analitic Tier A are un factor din `D/N/C/F/B/V/O` și spune ce se rupe fără el
6. fiecare token `MOD_*` referit există în `CatalogModule` (verificare între fișiere)
7. corelațiile se recalculează pe cifrele fluxurilor, nu declarativ
8. formulele au paranteze echilibrate; zero erori de formulă; toate celulele `Check` = OK
9. rândurile originale din training 4 supraviețuiesc, în ordine, în fișierele generate

Poarta 1 verifică sumele din **structura de date**, nu din textul afișat, deci cifrele
din coloana „Sumă” nu pot diverge de cele verificate.

## Ce a rămas marcat onest

- **Salarii** (`421/431/444/436`, `641/642/646`) rămân `PARȚIAL` în matricea de acoperire.
  Fluxurile noi ating 641 doar ca bază de capitalizare (F-52, F-58), nu ca monografie
  completă de salarizare — aceea stă în `MOD_SALARII`, exemplu extern. Golurile sunt
  declarate explicit în `date/plan.py → GOLURI_ACCEPTATE`; orice gol *nedeclarat* pică
  verificarea.
- Întrebările marcate `❓` în notițele revizuite (TVA nededusă pe rata de capital —
  capitalizare vs. cheltuială; baza legală exactă pentru vânzarea sub valoarea rămasă)
  apar în sistem ca **opțiune de configurare** și ca **notă de risc**, nu ca regulă
  tranșată. Tratamentul nu a fost inventat.

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
