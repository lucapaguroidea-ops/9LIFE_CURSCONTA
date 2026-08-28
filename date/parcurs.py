"""Partea SCRISĂ DE MÂNĂ a documentului de parcurs.

Regula acestui fișier: aici stă doar ce nu se poate deduce din cod. Orice enumerare a
stării sistemului — porți, clase, module, anexe, fișiere — se generează în
`build/parcurs.py`, din sursele reale. Scrisă aici, ar începe să diveargă din prima zi.

Testul aplicat fiecărui paragraf de mai jos:

    Dacă documentul de referință s-ar schimba mâine, paragraful ăsta ar deveni fals?

Dacă da, nu e îndrumare — e parafrază, și nu are ce căuta aici. De aceea nu vei găsi
nicio regulă contabilă în acest fișier, ci doar trimiteri la locul unde stă regula.
"""

INTRO = """\
Documentul ăsta nu explică sistemul. Îl **indică**.

Suprafața de referință e mare — două workbook-uri, patru documente revizuite, o listă de
întrebări deschise — și fiecare are logica lui internă. O parafrază a lor s-ar citi mai
ușor decât originalul, deci ar fi crezută în locul lui. Exact asta trebuie evitat.

Ce găsești aici: **ce întrebări trebuie puse**, **unde se scrie fiecare lucru** și
**unde se pierde coerența fără ca vreo poartă să observe**. Regulile contabile nu sunt
aici; sunt în documentele pe care le indică fiecare secțiune.

Parcursul are două faze, de naturi diferite. Faza A e judecată și aproape nimic din ea nu
se poate verifica automat. Faza B e mecanică și e acoperită aproape integral de porți.
"""

# ---------------------------------------------------------------------------
# FAZA A — notițe brute → document revizuit
# ---------------------------------------------------------------------------

FAZA_A_INTRO = """\
Nu e o listă de pași, ci de întrebări. Documentul revizuit e bun când răspunde la toate
— nu când urmează o procedură.

Porțile 12 și 13 verifică **forma** rezultatului (nimic pierdut, legendă și anexe
canonice). Nu verifică nimic din ce urmează: acolo nu există automatizare, doar citire
atentă.\
"""

#: (întrebare, de ce contează, unde se vede răspunsul în documentele existente)
FAZA_A = [
    ("Ce din materialul ăsta e deja în sistem?",
     "Înainte de a scrie orice, fiecare temă din notițe se pune lângă fluxul, modulul "
     "sau corelația care o acoperă deja. Ce rămâne e material nou; restul e ADÂNCIRE, "
     "și se scrie ca adâncire — cu trimitere la ce adâncește. Fără pasul ăsta, "
     "duplicarea se descoperă în faza B, în timpul scrierii codului, sau deloc: la "
     "trainingul 8, mecanismul codului din nomenclatorul D394 a fost scris ca material "
     "nou, deși era pasul revelator al lui F-203 de la trainingul 3. Tabelul rezultat "
     "intră ca §0 în documentul revizuit, unde poate fi verificat.",
     "`date/ordine.py:DENUMIRE`, foaia `CatalogModule` și `date/corelatii.py` — trei "
     "liste citibile, care răspund în cinci minute"),

    ("Ce spunea notița, cuvânt cu cuvânt?",
     "Notița brută rămâne sursa. Documentul revizuit o citează înainte de a o corecta, "
     "altfel corecția nu se poate judeca — și nici reface, dacă se dovedește greșită.",
     "`surse/training-*/notite-brut.txt` rămân în repo, neatinse, exact pentru asta"),

    ("Care afirmații sunt verificabile în lege și care sunt practică de cabinet?",
     "Sunt două feluri de adevăr, iar amestecul lor e cea mai frecventă sursă de "
     "eroare. Primul se verifică; al doilea se întreabă.",
     "practica se marchează ❓ și ajunge în `date/intrebari.py` — vezi cele 21 existente"),

    ("Pentru fiecare corecție ⚠️: care e temeiul, cu articol?",
     "O corecție fără temei e o opinie. Cu temei, se poate contesta — și e exact ce "
     "vrei să se poată face.",
     "Anexa E a fiecărui document revizuit adună actele citate; se generează din text"),

    ("Cifrele din exemplele în proză se leagă?",
     "Poarta 1 verifică ΣD=ΣC doar pentru fluxurile din `date/`, NU pentru monografiile "
     "scrise în document. Exemplul rezervei legale din trainingul 2 nu se lega — 5% din "
     "250 nu dau 125 — și a fost prins de citire, nu de o poartă. Recalculează fiecare "
     "exemplu cu creionul.",
     "gol cunoscut, candidat de automatizare — vezi secțiunea de goluri"),

    ("Conturile citate există, cu denumirea aia?",
     "Notițele brute conțineau `7815`, `2114`, `1067`, `4424` — conturi inexistente sau "
     "confundate. Fiecare simbol se confruntă cu planul de conturi înainte de a intra "
     "în document.",
     "foaia `Plan de conturi`; erorile deja prinse sunt în Anexa F a trainingului 4"),

    ("Cotele, pragurile și termenele sunt cele în vigoare LA DATA trainingului?",
     "Se schimbă prin OUG peste noapte. Un prag corect acum poate fi fals la aplicare, "
     "iar documentul trebuie să spună la ce dată a fost verificat.",
     "secțiunea de verificare legislativă din foaia `Legendă`, cu data ei"),

    ("Ce lipsea din raționament ca să stea în picioare?",
     "Completările ➕ sunt partea care transformă notițele în material utilizabil. "
     "Trebuie însă marcate ca atare: cititorul are dreptul să știe ce a spus formatorul "
     "și ce am adăugat eu.",
     "legenda de marcaje, identică în toate documentele (poarta 13)"),

    ("Ce a rămas ambiguu?",
     "Ambiguitatea nu se rezolvă prin ghicit. Se marchează ❓, se scrie ce am presupus "
     "ca să pot merge mai departe, și intră în lista pentru formator.",
     "`date/intrebari.py` → documentul, pagina publicată ȘI foaia `Întrebări deschise`"),

    ("Ce erori din notițele brute NU trebuie reintroduse?",
     "Cine reia notițele originale peste un an va relua și erorile. Lista lor explicită "
     "e singura apărare.",
     "Anexa F — vezi `date/documente.py`, `ANEXA_F_TRAINING_4`"),
]

# ---------------------------------------------------------------------------
# FAZA B — document revizuit → Excel
# ---------------------------------------------------------------------------

FAZA_B_INTRO = """\
Aici lucrurile sunt mecanice și acoperite de porți. Regula de aur: **nu edita
workbook-urile direct.** Se scrie în `date/`, se rulează `make tot`, iar workbook-urile
se regenerează. O modificare făcută în Excel se pierde la următorul build.\
"""

RUNBOOK = [
    ("1. Alege clasa fiecărui flux nou",
     "Clasa contului principal decide ID-ul și poziția fizică. Nu se adaugă la coadă: "
     "`ordine.urmatorul_liber(clasa)` dă următorul număr liber, iar fluxul se pune la "
     "locul lui contabil în lista clasei."),

    ("2. Scrie monografia",
     "Un flux = catalog + pași + „Principiul:”. Ultimul pas e verificare, fără sume, și "
     "declară starea terminală. Fluxurile didactice au exact un pas revelator. Porțile "
     "1, 2 și 3 verifică toate astea."),

    ("3. Completează planul cu conturile pe care le folosești",
     "Dacă un flux folosește un cont absent din plan, navigarea cont → flux se rupe. "
     "Nicio poartă nu prinde asta încă — la trainingurile 2 și 3 au fost 27 de conturi "
     "lipsă, găsite prin comparație manuală."),

    ("4. Adaugă analiticele și corelațiile",
     "Fiecare analitic are un factor și spune ce se rupe fără el (poarta 5). Fiecare "
     "corelație spune ce o rupe LEGITIM și ce o rupe SUSPECT — fără coloana asta, "
     "corelația nu ajută pe nimeni la închiderea lunii."),

    ("5. Rulează `make tot`",
     "Regenerează ambele workbook-uri, documentele și lista de întrebări, apoi "
     "rulează toate porțile. Nimic nu se consideră gata până nu sunt toate verzi."),

    ("6. Când o poartă pică, nu o ocoli",
     "Fiecare poartă are un motiv scris în `build/verifica.py`. Dacă un text chiar "
     "trebuie înlocuit, se declară în `date/reformulari.py` CU MOTIV — nu se șterge "
     "poarta."),
]

# ---------------------------------------------------------------------------
# Puncte de convergență — miezul documentului
# ---------------------------------------------------------------------------

CONVERGENTA_INTRO = """\
Locurile unde un training nou poate rupe coerența. Unele sunt prinse de o poartă — pe
alea le enumăr ca să știi că nu trebuie să te uiți după ele. Restul sunt **goluri
cunoscute**: acolo trebuie să te uiți tu.\
"""

#: (punct, ce se pierde, numărul porții care îl prinde — `None` = gol cunoscut).
#: Poarta se ține ca NUMĂR, nu ca frază: fraza ar trebui apoi tăiată la generare,
#: iar tăierea la ultimul cuvânt producea „poarta acum”.
CONVERGENTA = [
    ("Analitic nou fără factor",
     "Recomandarea de analitic devine „de frumusețe” — exact ce interzice foaia "
     "`Arbore analitice`.", 5),

    ("Flux nou care nu apare în matricea de acoperire",
     "Contul pare neacoperit, deși are flux.", 4),

    ("Pas de flux cu sumele dezechilibrate",
     "Monografia nu se poate înregistra.", 1),

    ("Flux fără stare terminală sau fără „Principiul:”",
     "Cititorul nu știe când s-a terminat și de ce contează.", 2),

    ("Text de tabel scris din greșeală ca formulă",
     "Excel afișează #NAME?, iar recalc-ul nu semnalează.", 8),

    ("Suprascrierea unei celule care avea deja conținut",
     "Conținut vechi pierdut tăcut. S-a întâmplat: 12 linii pierdute la o etapă "
     "anterioară.", 9),

    ("Catalogul rămâne în urma monografiilor",
     "Indexul nu mai cunoaște toate fluxurile. S-a întâmplat: 13 din 44 lipseau — "
     "de atunci catalogul se derivă din monografii.", 10),

    ("Foaie nouă absentă din tabelul de structură al Legendei",
     "Legenda nu-și mai cunoaște propriul fișier.", 14),

    ("Cont folosit într-un flux dar absent din `Plan de conturi`",
     "Navigarea cont → flux se rupe pentru contul acela. La trainingurile 2 și 3 "
     "erau 27 de conturi în situația asta.", 20),

    ("Document cu întrebări deschise, dar fără niciun marcaj ❓",
     "Cititorul vede un document care pare tranșat, deși sistemul știe că nu e. "
     "Documentul de control chiar era așa: trei întrebări deschise, zero marcaje.", 19),

    ("Marcaj ❓ într-un document fără întrebări deschise",
     "Marcajul promite o anexă care nu-l explică. Mai rău decât lipsa lui.", 19),

    ("Marcaj ❓ folosit cu alt înțeles decât cel din legendă",
     "Poarta 19 verifică prezența marcajului pe document, nu înțelesul fiecărei "
     "apariții. Două ❓ marcau răspunsuri, nu întrebări — găsite prin citire și "
     "corectate ca reformulări declarate, nu de o poartă.", None),

    ("Modul care declară în `CATALOG['fluxuri']` un flux inexistent",
     "Ancora nu se mai generează — nici pe flux, nici pe corelație, nici pe matrice. "
     "Nu produce eroare, produce o legătură lipsă.", 21),

    ("Cifră scrisă de mână într-un fișier pe care nu-l reface build-ul",
     "README-ul chiar rămăsese în urmă: 23 corelații când erau 29, și 58 de conturi "
     "Tier A când 87 sunt clasificate iar 39 detaliate.", 22),

    ("Subsecțiune dintr-o sursă împărțită, rămasă nerepartizată",
     "O sursă poate alimenta mai multe documente. Riscul nu e „nimeni n-a luat-o”, ci "
     "„am crezut că a luat-o celălalt”: fiecare document trece poarta 12 separat, în "
     "timp ce materialul cade între ele.", 16),

    ("Material repartizat undeva, dar ajuns în altă parte",
     "Verificarea pe reuniunea destinațiilor ar spune doar că textul există pe undeva "
     "— întrebarea greșită. Poarta compară cu destinația declarată.", 16),

    ("Cont urmărit periodic fără flux care să-i demonstreze starea",
     "Checklistul de închidere ar cere ceva ce sistemul nu arată nicăieri. Invers, un "
     "cont cu rol în flux care se golește și nu e urmărit dispare din disciplina "
     "lunară.", 17),

    ("Articol compus în proză cu totalul greșit",
     "Liniile de continuare nu însumează totalul de pe rândul de cap — exact forma "
     "erorii avansului din 19.08.", 18),

    ("Aritmetică falsă afirmată în text („5% din 250 = 125”)",
     "Articolul se echilibrează, deci poarta de echilibru nu vede nimic. Eroarea "
     "rezervei legale din trainingul 2 era exact asta.", 18),

    ("Sumă greșită într-un articol SIMPLU, scris pe o linie",
     "Un articol pe o linie are o singură sumă, deci nu se poate dezechilibra: nu "
     "există nimic contra cui să fie verificată. Poarta 18 nu ajunge aici, iar "
     "totalurile afirmate în proză s-au dovedit prea variate ca să fie potrivite "
     "mecanic — trei fals pozitive din șase la măsurare.", None),
]

# ---------------------------------------------------------------------------
# Traseul real
# ---------------------------------------------------------------------------

TRASEU_INTRO = """\
Cum a intrat efectiv trainingul 3 (imobilizări, 12.08.2026). Nu e o reconstituire — e
ce s-a întâmplat, verificabil în istoricul git. Un traseu real spune mai mult decât o
procedură abstractă, pentru că include și ce a mers prost.\
"""

TRASEU = [
    ("Notițele brute au intrat neatinse în `surse/training-3-2026-08-12/`",
     "Fișierele din `surse/` nu se modifică niciodată. Sunt referința contra căreia "
     "verifică poarta de conservare."),

    ("Documentul revizuit exista deja — a trecut doar prin faza B",
     "Trainingurile 2 și 3 aveau deja `.md`-urile revizuite. Un training nou va trece "
     "prin ambele faze."),

    ("Monografiile au fost scrise în `date/fluxuri_imobilizari.py` — 423 de rânduri",
     "Unsprezece fluxuri, fiecare cu pași, sume structurate, rol revelat și principiu."),

    ("Planul, analiticele și corelațiile, în paralel",
     "`date/plan.py` (conturile lipsă și corecția lui 235), `date/analitice.py` "
     "(conturile Tier A din clasa 2), `date/corelatii.py` (C-13…C-22)."),

    ("Prima rulare a picat pe corecția contului 235",
     "Generatorul refuză să suprascrie o denumire dacă cea din fișier nu e cea "
     "așteptată. Era protecția care funcționa: 235 purta denumirea lui 233, iar 233 "
     "lipsea complet din plan."),

    ("A doua rulare a picat pe poarta 4",
     "Fluxurile noi nu apăreau în matricea de acoperire. Matricea a fost completată, "
     "iar marcajele PARȚIAL promise ca rezolvate au fost verificate că sunt chiar „NU”."),

    ("Modulele au venit după fluxuri, nu odată cu ele",
     "Un flux e util și fără modul — explică. Modulul îl execută. Ordinea asta permite "
     "livrare parțială fără să rămână nimic pe jumătate."),

    ("La final, `make tot` de la zero",
     "Nu build incremental. Un sistem care nu se reconstruiește din nimic nu e "
     "reproductibil, iar reproductibilitatea e singura garanție că `date/` chiar e "
     "sursa adevărului."),
]

# ---------------------------------------------------------------------------
# Goluri cunoscute — ce ar merita mecanizat
# ---------------------------------------------------------------------------

GOLURI = [
    ("Suma dintr-un articol simplu scris în proză",
     "Poarta 18 citește acum monografiile din documente și verifică articolele compuse "
     "plus aritmetica afirmată în text. Articolul simplu îi scapă însă prin construcție: "
     "scris pe o linie, are o singură sumă, deci nu există nimic contra cui să fie "
     "verificat. Confruntarea cu totalurile afirmate în proză s-a dovedit prea "
     "nesigură — trei fals pozitive din șase la măsurare, pentru că „sold creditor de "
     "4.000” e un rezultat net, nu o sumă de debite."),

    ("Înțelesul fiecărui marcaj ❓ în parte",
     "Poarta 19 leagă marcajele de întrebări la nivel de DOCUMENT: unul cu întrebări "
     "deschise îl poartă, unul care îl poartă are întrebări. Ce anume marchează fiecare "
     "apariție rămâne necontrolat — iar două chiar marcau răspunsuri, nu întrebări. "
     "Legarea unu-la-unu ar cere o ancoră de text pe fiecare întrebare, rescrisă la "
     "fiecare editare de frază: o hartă de mână care diverge, exact ce evită sistemul."),
]
