# Parcursul unui set nou de notițe

*Document de îndrumare. Nu explică sistemul — îl indică.*

---

## 0. Cum se folosește

Documentul ăsta nu explică sistemul. Îl **indică**.

Suprafața de referință e mare — două workbook-uri, patru documente revizuite, o listă de
întrebări deschise — și fiecare are logica lui internă. O parafrază a lor s-ar citi mai
ușor decât originalul, deci ar fi crezută în locul lui. Exact asta trebuie evitat.

Ce găsești aici: **ce întrebări trebuie puse**, **unde se scrie fiecare lucru** și
**unde se pierde coerența fără ca vreo poartă să observe**. Regulile contabile nu sunt
aici; sunt în documentele pe care le indică fiecare secțiune.

Parcursul are două faze, de naturi diferite. Faza A e judecată și aproape nimic din ea nu
se poate verifica automat. Faza B e mecanică și e acoperită aproape integral de porți.


> **Testul aplicat fiecărui paragraf:** dacă documentul de referință s-ar schimba mâine, paragraful ăsta ar deveni fals? Dacă da, e parafrază, nu îndrumare — și nu are ce căuta aici.

Secțiunile marcate *[generat]* se recitesc din cod și din workbook-uri la fiecare `make tot`. Nu le edita: se suprascriu.

---

## 1. Unde se uită *[generat]*

Tabelul de mai jos nu e scris aici: e citit din foaia `Legendă`, secțiunea „STRUCTURA FINALĂ A WORKBOOK-ULUI”, pe care poarta 14 o ține completă. Dacă apare o foaie nouă în workbook, apare și aici.

| Foaie | Ce ține |
|---|---|
| Legendă | Taxonomia rolurilor + tipologia factorilor + convenția de analitic + tierizare + TVA confirmat |
| Plan de conturi | 257 conturi, cu 3 coloane noi: Analitice recomandate · Factor · Flux (pas) |
| Doar rol în flux | 80 conturi de serviciu, grupate pe rol |
| Analitice (Tier A) | Detaliu pe conturile Tier A: structură, factor, ce se rupe și de ce |
| Fluxuri | 68 fluxuri × pași, tabelar cu note complete + coloană Declarativ |
| Matrice acoperire | Cont → flux(uri) → pas revelator; arată golurile |
| Index module | Legătura cu Module_Declarative_Fluxuri.xlsx: ce modul acoperă ce flux, cu ce foi și când se rulează |
| Arbore analitice | Arborele de decizie pentru analitice (3 întrebări) + contra-regula: când analiticul e o greșeală |
| Corelații de control | Formulă · unde se verifică · ce o rupe LEGITIM vs. SUSPECT · fluxul și modulul legat |
| Întrebări deschise | Ce e încă provizoriu în workbook: întrebările la care sistemul așteaptă răspuns. Fluxurile atinse poartă ❓ |
| Închideri periodice | Disciplina de închidere: ce cont, la ce cadență, cu ce stare terminală declarată în flux. Rândurile fără flux sunt goluri cunoscute, marcate ca atare |
| Istoric | Echivalența de numerotare veche → nouă, contopirile, defectele reparate, textul mutat la deduplicare |

**Documente conexe:** cele trei `.md`/`.docx` revizuite (structura lor canonică e în `date/documente.py`) și `intrebari-formator.md` — lista întrebărilor deschise, aceeași sursă cu foaia `Întrebări deschise`.

---

## 2. Faza A — notițe brute → document revizuit

Nu e o listă de pași, ci de întrebări. Documentul revizuit e bun când răspunde la toate
— nu când urmează o procedură.

Porțile 12 și 13 verifică **forma** rezultatului (nimic pierdut, legendă și anexe
canonice). Nu verifică nimic din ce urmează: acolo nu există automatizare, doar citire
atentă.

**1. Ce spunea notița, cuvânt cu cuvânt?**

Notița brută rămâne sursa. Documentul revizuit o citează înainte de a o corecta, altfel corecția nu se poate judeca — și nici reface, dacă se dovedește greșită.

↳ `surse/training-*/notite-brut.txt` rămân în repo, neatinse, exact pentru asta

**2. Care afirmații sunt verificabile în lege și care sunt practică de cabinet?**

Sunt două feluri de adevăr, iar amestecul lor e cea mai frecventă sursă de eroare. Primul se verifică; al doilea se întreabă.

↳ practica se marchează ❓ și ajunge în `date/intrebari.py` — vezi cele 21 existente

**3. Pentru fiecare corecție ⚠️: care e temeiul, cu articol?**

O corecție fără temei e o opinie. Cu temei, se poate contesta — și e exact ce vrei să se poată face.

↳ Anexa E a fiecărui document revizuit adună actele citate; se generează din text

**4. Cifrele din exemplele în proză se leagă?**

Poarta 1 verifică ΣD=ΣC doar pentru fluxurile din `date/`, NU pentru monografiile scrise în document. Exemplul rezervei legale din trainingul 2 nu se lega — 5% din 250 nu dau 125 — și a fost prins de citire, nu de o poartă. Recalculează fiecare exemplu cu creionul.

↳ gol cunoscut, candidat de automatizare — vezi secțiunea de goluri

**5. Conturile citate există, cu denumirea aia?**

Notițele brute conțineau `7815`, `2114`, `1067`, `4424` — conturi inexistente sau confundate. Fiecare simbol se confruntă cu planul de conturi înainte de a intra în document.

↳ foaia `Plan de conturi`; erorile deja prinse sunt în Anexa F a trainingului 4

**6. Cotele, pragurile și termenele sunt cele în vigoare LA DATA trainingului?**

Se schimbă prin OUG peste noapte. Un prag corect acum poate fi fals la aplicare, iar documentul trebuie să spună la ce dată a fost verificat.

↳ secțiunea de verificare legislativă din foaia `Legendă`, cu data ei

**7. Ce lipsea din raționament ca să stea în picioare?**

Completările ➕ sunt partea care transformă notițele în material utilizabil. Trebuie însă marcate ca atare: cititorul are dreptul să știe ce a spus formatorul și ce am adăugat eu.

↳ legenda de marcaje, identică în toate documentele (poarta 13)

**8. Ce a rămas ambiguu?**

Ambiguitatea nu se rezolvă prin ghicit. Se marchează ❓, se scrie ce am presupus ca să pot merge mai departe, și intră în lista pentru formator.

↳ `date/intrebari.py` → documentul, pagina publicată ȘI foaia `Întrebări deschise`

**9. Ce erori din notițele brute NU trebuie reintroduse?**

Cine reia notițele originale peste un an va relua și erorile. Lista lor explicită e singura apărare.

↳ Anexa F — vezi `date/documente.py`, `ANEXA_F_TRAINING_4`

### Forma rezultatului *[generat]*

Documentul revizuit are aceeași legendă de marcaje ca celelalte trei și anexele denumite canonic. Poarta 13 verifică asta.

| Anexa | Conținut |
|---|---|
| **A** | Recapitulare: conturi și perechile lor |
| **B** | Checklist practic |
| **C** | Ce am corectat față de notițele originale |
| **D** | Rămase deschise |
| **E** | Baza legală citată |
| **F** | Erori din notițele brute, NEreintroduse |
| **G** | Răspunsuri verificate pe surse publice |

Nu orice document are toate anexele — le are pe cele pentru care există conținut real. Vezi `date/documente.py` pentru ce anexă e servită de ce secțiune în fiecare document.

---

## 3. Faza B — document revizuit → Excel

Aici lucrurile sunt mecanice și acoperite de porți. Regula de aur: **nu edita
workbook-urile direct.** Se scrie în `date/`, se rulează `make tot`, iar workbook-urile
se regenerează. O modificare făcută în Excel se pierde la următorul build.

**1. Alege clasa fiecărui flux nou**

Clasa contului principal decide ID-ul și poziția fizică. Nu se adaugă la coadă: `ordine.urmatorul_liber(clasa)` dă următorul număr liber, iar fluxul se pune la locul lui contabil în lista clasei.

**2. Scrie monografia**

Un flux = catalog + pași + „Principiul:”. Ultimul pas e verificare, fără sume, și declară starea terminală. Fluxurile didactice au exact un pas revelator. Porțile 1, 2 și 3 verifică toate astea.

**3. Completează planul cu conturile pe care le folosești**

Dacă un flux folosește un cont absent din plan, navigarea cont → flux se rupe. Nicio poartă nu prinde asta încă — la trainingurile 2 și 3 au fost 27 de conturi lipsă, găsite prin comparație manuală.

**4. Adaugă analiticele și corelațiile**

Fiecare analitic are un factor și spune ce se rupe fără el (poarta 5). Fiecare corelație spune ce o rupe LEGITIM și ce o rupe SUSPECT — fără coloana asta, corelația nu ajută pe nimeni la închiderea lunii.

**5. Rulează `make tot`**

Regenerează ambele workbook-uri, documentele și lista de întrebări, apoi rulează toate porțile. Nimic nu se consideră gata până nu sunt toate verzi.

**6. Când o poartă pică, nu o ocoli**

Fiecare poartă are un motiv scris în `build/verifica.py`. Dacă un text chiar trebuie înlocuit, se declară în `date/reformulari.py` CU MOTIV — nu se șterge poarta.

### Unde se scrie fiecare lucru *[generat]*

| Fișier | Ce ține |
|---|---|
| `date/analitice.py` | Conturi din clasele 1 și 2 promovate la Tier A, cu structura analitică justificată. |
| `date/corelatii.py` | Corelațiile de control C-13…C-22 (capitaluri și imobilizări). |
| `date/documente.py` | Planul de armonizare a celor trei documente revizuite. |
| `date/fluxuri_capitaluri.py` | Fluxurile F-45…F-51 — capitaluri, credite, leasing, provizioane. |
| `date/fluxuri_control.py` | Fluxul F-63 (→ F-415) — încasare mai mare decât factura. |
| `date/fluxuri_imobilizari.py` | Fluxurile F-52…F-62 — imobilizări necorporale, corporale, în curs, ieșiri, financiare. |
| `date/fluxuri_salarii.py` | Fluxurile din trainingul 21.08.2026 — salarii, rețineri, impozit pe venit. |
| `date/inchideri.py` | Cadența de urmărire a conturilor — partea care NU se poate deduce din fluxuri. |
| `date/intrebari.py` | Cele 21 de întrebări deschise, grupate pe temă contabilă. |
| `date/monografii.py` | Excepțiile porții 18 — blocuri de monografie care NU trebuie să se echilibreze. |
| `date/ordine.py` | Ordinea canonică a sistemului — singura sursă de adevăr pentru poziții și ID-uri. |
| `date/pachet.py` | Ordinea de uz a livrabilelor — partea scrisă de mână a pachetului. |
| `date/parcurs.py` | Partea SCRISĂ DE MÂNĂ a documentului de parcurs. |
| `date/plan.py` | Actualizări pe foaia `Plan de conturi` + conturi sintetice lipsă + rânduri de matrice. |
| `date/reformulari.py` | Textele din originalul training 4 care au voie să dispară, fiecare cu motiv. |
| `date/repartizare.py` | Unde merge fiecare subsecțiune a unei surse care alimentează mai multe destinații. |

### Clasele de fluxuri *[generat]*

ID-ul codifică clasa contului principal. Un flux nou primește următorul număr liber din clasa lui — `ordine.urmatorul_liber(clasa)` — și stă fizic la locul lui.

| Bloc | Clasa | Fluxuri acum | Următorul liber |
|---|---|---|---|
| `F-1xx` | CAPITALURI, PROVIZIOANE, ÎMPRUMUTURI | 8 | `F-109` |
| `F-2xx` | IMOBILIZĂRI | 14 | `F-215` |
| `F-3xx` | STOCURI ȘI PRODUCȚIE | 20 | `F-321` |
| `F-4xx` | TERȚI, TVA, DECONTĂRI | 22 | `F-423` |
| `F-5xx` | TREZORERIE | 2 | `F-503` |
| `F-8xx` | CONTURI ÎN AFARA BILANȚULUI | 2 | `F-803` |

### Modulele existente *[generat]*

Un flux e util și fără modul: fluxul explică, modulul execută. Dacă adaugi un modul, declară fluxurile în `CATALOG['fluxuri']` — de acolo se derivă toate ancorele.

| Modul | Fluxuri acoperite |
|---|---|
| `MOD_INCHIDERE_TVA` | F-405 |
| `MOD_APROV_TRANZIT` | F-302 |
| `MOD_SALARII` | F-413 |
| `MOD_DECONT` | F-502 |
| `MOD_LEASING_FIN` | F-108 |
| `MOD_VANZ_AMANUNT` | F-316 |
| `MOD_TVA_INCASARE` | F-401 |
| `MOD_INCHIDERE_EX` | F-104 |
| `MOD_INTERMEDIAR` | F-408, F-501, F-411 |
| `MOD_NEUTRALIZARE` | F-311, F-312, F-209 |
| `MOD_CAPITALURI` | F-103, F-105 |
| `MOD_CREDIT_VALUTA` | F-107 |
| `MOD_PROVIZION` | F-106 |
| `MOD_IMOBILIZARI` | F-203, F-205, F-207, F-214 |
| `MOD_SUBVENTIE` | F-210 |
| `MOD_IESIRE_MF` | F-211, F-212 |
| `MOD_INCHIDERE_LUNARA` | F-422, F-413 |

### Ce verifică fiecare poartă *[generat]*

| Poarta | Verifică |
|---|---|
| **1** | ΣDebit = ΣCredit pe fiecare pas de flux care are sume |
| **2** | fiecare flux se închide cu un pas de verificare, o stare terminală și „Principiul:” |
| **3** | fiecare flux didactic ★ are exact un pas revelator |
| **4** | matricea nu are goluri nedeclarate, iar fiecare flux nou e referit în ea |
| **5** | fiecare analitic Tier A are un factor din D/N/C/F/B/V/O și spune ce se rupe fără el |
| **6** | fiecare token MOD_* referit există în CatalogModule (verificare între fișiere) |
| **7** | corelațiile se verifică pe cifrele fluxurilor, nu declarativ |
| **8** | formule echilibrate, niciun text scris din greșeală ca formulă, zero erori după recalc, toate celulele Check = OK |
| **9** | conservare: fiecare linie din workbook-urile originale se regăsește în cele generate; înlocuirile intenționate se declară în `date/reformulari.py`, cu motiv |
| **10** | catalogul de fluxuri acoperă fix monografiile — nici mai mult, nici mai puțin |
| **11** | zero nume definite rupte |
| **12** | conservare pe documentele revizuite: nicio linie pierdută la armonizare |
| **13** | documentele au aceeași legendă, anexe canonice în ordine, și toate trei formatele: .md, .docx, .html |
| **14** | tabelul de structură din foaia Legendă cunoaște toate foile workbook-ului |
| **15** | documentul de parcurs nu citează foi, fișiere sau porți care nu există |
| **16** | o sursă împărțită pe mai multe destinații nu pierde nimic în cusătură: fiecare subsecțiune are destinație declarată și ajunge exact acolo |
| **17** | disciplina de închidere e ancorată în ambele sensuri: fiecare cont urmărit periodic e starea terminală a unui flux, iar fiecare cont cu rol în flux care se golește are o cadență — sau un motiv declarat pentru care nu are |
| **18** | monografiile scrise în proză se echilibrează, iar aritmetica afirmată în text („5% din 250 = 12,50”) chiar se verifică — acolo unde poarta 1 nu ajunge |
| **19** | marcajul ❓ e aplicat, nu doar definit: un document pe care o întrebare deschisă îl privește îl poartă, iar un document care îl poartă are întrebări deschise |
| **20** | fiecare cont folosit într-un pas de flux există în „Plan de conturi” |
| **21** | fiecare flux declarat de un modul în `CATALOG['fluxuri']` există cu adevărat |
| **22** | blocul de cifre din README e exact cel pe care generatorul l-ar produce |
| **24** | nicio frază cu cifră din workbook-uri nu contrazice cifra reală („17 module declarative”, „68 fluxuri × pași”) — foaia Istoric e scutită, acolo cifrele vechi sunt chiar conținutul |

Motivul fiecărei porți e scris în `build/verifica.py`, lângă ea. Când o poartă pică, acolo scrie de ce există.

---

## 4. Puncte de convergență

Locurile unde un training nou poate rupe coerența. Unele sunt prinse de o poartă — pe
alea le enumăr ca să știi că nu trebuie să te uiți după ele. Restul sunt **goluri
cunoscute**: acolo trebuie să te uiți tu.

| Ce se poate rupe | Ce se pierde | Prins de |
|---|---|---|
| Analitic nou fără factor | Recomandarea de analitic devine „de frumusețe” — exact ce interzice foaia `Arbore analitice`. | poarta 5 |
| Flux nou care nu apare în matricea de acoperire | Contul pare neacoperit, deși are flux. | poarta 4 |
| Pas de flux cu sumele dezechilibrate | Monografia nu se poate înregistra. | poarta 1 |
| Flux fără stare terminală sau fără „Principiul:” | Cititorul nu știe când s-a terminat și de ce contează. | poarta 2 |
| Text de tabel scris din greșeală ca formulă | Excel afișează #NAME?, iar recalc-ul nu semnalează. | poarta 8 |
| Suprascrierea unei celule care avea deja conținut | Conținut vechi pierdut tăcut. S-a întâmplat: 12 linii pierdute la o etapă anterioară. | poarta 9 |
| Catalogul rămâne în urma monografiilor | Indexul nu mai cunoaște toate fluxurile. S-a întâmplat: 13 din 44 lipseau — de atunci catalogul se derivă din monografii. | poarta 10 |
| Foaie nouă absentă din tabelul de structură al Legendei | Legenda nu-și mai cunoaște propriul fișier. | poarta 14 |
| Cont folosit într-un flux dar absent din `Plan de conturi` | Navigarea cont → flux se rupe pentru contul acela. La trainingurile 2 și 3 erau 27 de conturi în situația asta. | poarta 20 |
| Document cu întrebări deschise, dar fără niciun marcaj ❓ | Cititorul vede un document care pare tranșat, deși sistemul știe că nu e. Documentul de control chiar era așa: trei întrebări deschise, zero marcaje. | poarta 19 |
| Marcaj ❓ într-un document fără întrebări deschise | Marcajul promite o anexă care nu-l explică. Mai rău decât lipsa lui. | poarta 19 |
| Marcaj ❓ folosit cu alt înțeles decât cel din legendă | Poarta 19 verifică prezența marcajului pe document, nu înțelesul fiecărei apariții. Două ❓ marcau răspunsuri, nu întrebări — găsite prin citire și corectate ca reformulări declarate, nu de o poartă. | **nimic — verifică tu** |
| Modul care declară în `CATALOG['fluxuri']` un flux inexistent | Ancora nu se mai generează — nici pe flux, nici pe corelație, nici pe matrice. Nu produce eroare, produce o legătură lipsă. | poarta 21 |
| Cifră scrisă de mână într-un fișier pe care nu-l reface build-ul | README-ul chiar rămăsese în urmă: 23 corelații când erau 29, și 58 de conturi Tier A când 87 sunt clasificate iar 39 detaliate. | poarta 22 |
| Subsecțiune dintr-o sursă împărțită, rămasă nerepartizată | O sursă poate alimenta mai multe documente. Riscul nu e „nimeni n-a luat-o”, ci „am crezut că a luat-o celălalt”: fiecare document trece poarta 12 separat, în timp ce materialul cade între ele. | poarta 16 |
| Material repartizat undeva, dar ajuns în altă parte | Verificarea pe reuniunea destinațiilor ar spune doar că textul există pe undeva — întrebarea greșită. Poarta compară cu destinația declarată. | poarta 16 |
| Cont urmărit periodic fără flux care să-i demonstreze starea | Checklistul de închidere ar cere ceva ce sistemul nu arată nicăieri. Invers, un cont cu rol în flux care se golește și nu e urmărit dispare din disciplina lunară. | poarta 17 |
| Articol compus în proză cu totalul greșit | Liniile de continuare nu însumează totalul de pe rândul de cap — exact forma erorii avansului din 19.08. | poarta 18 |
| Aritmetică falsă afirmată în text („5% din 250 = 125”) | Articolul se echilibrează, deci poarta de echilibru nu vede nimic. Eroarea rezervei legale din trainingul 2 era exact asta. | poarta 18 |
| Sumă greșită într-un articol SIMPLU, scris pe o linie | Un articol pe o linie are o singură sumă, deci nu se poate dezechilibra: nu există nimic contra cui să fie verificată. Poarta 18 nu ajunge aici, iar totalurile afirmate în proză s-au dovedit prea variate ca să fie potrivite mecanic — trei fals pozitive din șase la măsurare. | **nimic — verifică tu** |

---

## 5. Traseul trainingului 3, pas cu pas

Cum a intrat efectiv trainingul 3 (imobilizări, 12.08.2026). Nu e o reconstituire — e
ce s-a întâmplat, verificabil în istoricul git. Un traseu real spune mai mult decât o
procedură abstractă, pentru că include și ce a mers prost.

**1.** Notițele brute au intrat neatinse în `surse/training-3-2026-08-12/`

   Fișierele din `surse/` nu se modifică niciodată. Sunt referința contra căreia verifică poarta de conservare.

**2.** Documentul revizuit exista deja — a trecut doar prin faza B

   Trainingurile 2 și 3 aveau deja `.md`-urile revizuite. Un training nou va trece prin ambele faze.

**3.** Monografiile au fost scrise în `date/fluxuri_imobilizari.py` — 423 de rânduri

   Unsprezece fluxuri, fiecare cu pași, sume structurate, rol revelat și principiu.

**4.** Planul, analiticele și corelațiile, în paralel

   `date/plan.py` (conturile lipsă și corecția lui 235), `date/analitice.py` (conturile Tier A din clasa 2), `date/corelatii.py` (C-13…C-22).

**5.** Prima rulare a picat pe corecția contului 235

   Generatorul refuză să suprascrie o denumire dacă cea din fișier nu e cea așteptată. Era protecția care funcționa: 235 purta denumirea lui 233, iar 233 lipsea complet din plan.

**6.** A doua rulare a picat pe poarta 4

   Fluxurile noi nu apăreau în matricea de acoperire. Matricea a fost completată, iar marcajele PARȚIAL promise ca rezolvate au fost verificate că sunt chiar „NU”.

**7.** Modulele au venit după fluxuri, nu odată cu ele

   Un flux e util și fără modul — explică. Modulul îl execută. Ordinea asta permite livrare parțială fără să rămână nimic pe jumătate.

**8.** La final, `make tot` de la zero

   Nu build incremental. Un sistem care nu se reconstruiește din nimic nu e reproductibil, iar reproductibilitatea e singura garanție că `date/` chiar e sursa adevărului.

---

## 6. Goluri cunoscute

Lucruri care ar merita mecanizate și care azi cad în sarcina cititorului. Enumerate ca să nu fie confundate cu ceva acoperit.

**Suma dintr-un articol simplu scris în proză**

Poarta 18 citește acum monografiile din documente și verifică articolele compuse plus aritmetica afirmată în text. Articolul simplu îi scapă însă prin construcție: scris pe o linie, are o singură sumă, deci nu există nimic contra cui să fie verificat. Confruntarea cu totalurile afirmate în proză s-a dovedit prea nesigură — trei fals pozitive din șase la măsurare, pentru că „sold creditor de 4.000” e un rezultat net, nu o sumă de debite.

**Înțelesul fiecărui marcaj ❓ în parte**

Poarta 19 leagă marcajele de întrebări la nivel de DOCUMENT: unul cu întrebări deschise îl poartă, unul care îl poartă are întrebări. Ce anume marchează fiecare apariție rămâne necontrolat — iar două chiar marcau răspunsuri, nu întrebări. Legarea unu-la-unu ar cere o ancoră de text pe fiecare întrebare, rescrisă la fiecare editare de frază: o hartă de mână care diverge, exact ce evită sistemul.

---

*Secțiunile [generat] provin din `build/verifica.py`, `date/ordine.py`, `date/documente.py` și din workbook-urile construite. 23 porți, 17 module, 68 fluxuri la data generării.*
