"""Ordinea de uz a livrabilelor — partea scrisă de mână a pachetului.

Regula acestui fișier, ca la `date/parcurs.py`: aici stă doar ce nu se poate deduce din
cod. Titlurile, subtitlurile și numărătorile se citesc din artefacte la generare. Ce se
scrie aici e **judecata**: în ce ordine ajungi la fișiere, când deschizi fiecare și — mai
util decât toate — la ce să NU-l folosești.

Ordinea nu e alfabetică și nu e cronologică. E ordinea în care ajungi la ele:

    lucrezi → studiezi → întrebi → adaugi

Iar înăuntrul studiului, ordinea e a planului de conturi, nu a zilelor de training:
clasa 1, clasa 2, clasele 3–4, salariile, apoi transversalul. Aceeași decizie ca la reordonarea
Excel-ului și la retitrarea documentelor — „logica integralității contabile, nu logica
adăugirii la fișier”.

Câmpul `nu` e cel care face pachetul util. Fără el, documentele de contabilitate arată
interschimbabile, iar cine caută o regulă o caută în primul care-i cade sub mână.
"""

#: (etapă, explicație scurtă) — cele patru momente de uz.
ETAPE = [
    ("Lucrezi",
     "Ce deschizi când ai un caz concret pe masă: un document de înregistrat, o lună de "
     "închis, un sold care nu arată bine."),
    ("Studiezi",
     "Materialul de curs, în ordinea planului de conturi — nu în ordinea zilelor de "
     "training. Cauți o regulă pe clasa contului, nu pe data când s-a predat."),
    ("Întrebi",
     "Ce a rămas neclarificat. Se trimite ca atare formatorului."),
    ("Adaugi",
     "Ce faci când vine un set nou de notițe, ca să intre la același standard."),
]

#: (etapă, cheie de artefact, nume în pachet, când, la ce NU)
#:
#: `cheie` numește artefactul din `dist/`; titlul și subtitlul vin de acolo, nu de aici.
ITEME = [
    ("Lucrezi", "xlsx:plan", "plan-de-conturi",
     "Prima oprire la orice cont necunoscut: ce rol are, în ce flux intră, ce analitice "
     "cere și ce corelație îl leagă de restul balanței. Foaia `Închideri periodice` se "
     "deschide lunar; `Întrebări deschise` spune ce e încă provizoriu.",
     "Nu produce înregistrări. E harta, nu motorul — pentru nota contabilă gata de "
     "introdus, treci la modulele declarative."),

    ("Lucrezi", "xlsx:module", "module-declarative",
     "Când ai de făcut efectiv înregistrarea: completezi câteva variabile în foaia "
     "`Declarații_…` galbenă și ies jurnalele și nota de export. Celulele `Check` "
     "trebuie să arate OK înainte de a lua rezultatul de bun.",
     "Nu explică de ce. Raționamentul e în flux, în workbook-ul de plan — un modul care "
     "dă un rezultat pe care nu-l poți justifica nu ți-e de folos la control."),

    ("Studiezi", "doc:capitaluri", "capitaluri-credite-provizioane",
     "Capital social și pragurile noi, repartizarea rezultatului, închiderea "
     "exercițiului, provizioane, credite în valută, leasing financiar.",
     "Nu conține stocuri și nici TVA, dincolo de ce atinge subiectul."),

    ("Studiezi", "doc:imobilizari", "imobilizari",
     "Intrarea pe grupe, imobilizările în curs, regia proprie, subvențiile, amortizarea, "
     "ieșirile prin vânzare și casare, controlul analitic ↔ sintetic.",
     "Nu tratează stocurile. Granița e reală și se greșește des: pragul de 5.000 lei "
     "decide dacă un bun e mijloc fix sau obiect de inventar."),

    ("Studiezi", "doc:stocuri-tva", "stocuri-tva-corelatii",
     "Cel mai gros dintre cele patru: aprovizionare, gestiune la preț cu amănuntul, "
     "producție, mărfuri, import, toată mecanica TVA și corelațiile de balanță. Aici "
     "stau și 408/418, avansurile și analiticele pe 4428.",
     "Nu e material de citit din scoarță-n scoarță. Se intră prin cuprins, pe subiectul "
     "care te interesează."),

    ("Studiezi", "doc:salarii", "salarii-contributii-retineri",
     "Statul de plată, contribuțiile, medicalele, popririle — și verificările care se "
     "fac în secunda doi, pentru că documentul de control există deja. Aici stau și "
     "interfețele cu HR: REGES, D112, pontajul, fișa de plătitor din SPV.",
     "Nu conține impozitul pe profit sau pe venit — acela ține de rezultatul "
     "exercițiului și stă la capitaluri, chiar dacă a fost predat în aceeași zi."),

    ("Studiezi", "doc:trezorerie", "trezorerie",
     "Banca, casa, efectele de încasat și avansurile de trezorerie: stările prin care "
     "trec banii între „am dreptul la ei” și „sunt în cont”. Aici stau scontarea, "
     "liniile de credit, dobânzile pe 5186/5187 și tichetele ca stoc de trezorerie.",
     "Nu conține disciplina de numerar — plafoanele de casă și regulile de document "
     "sunt la control, pentru că sunt despre ce se poate face, nu despre cum se "
     "înregistrează."),

    ("Studiezi", "doc:declaratii", "declaratii-fisa-platitor-bilant",
     "Capătul lanțului: ce se declară, cum se confruntă declarația cu balanța și ce se "
     "face când e greșită. Vocabularul balanței, impozitul pe profit calculat cumulat, "
     "SAF-T, fondul de handicap, chiriile cu stopaj la sursă, bilanțul pe F10–F40 și "
     "regimul de rectificare al fiecărei declarații.",
     "Nu e un document de monografii. Monografiile lui stau în celelalte — aici e "
     "despre locurile unde contabilitatea și declarația trebuie să dea la fel."),

    ("Studiezi", "doc:control", "control-documente-numerar",
     "Transversal, și cel mai practic: cum se citește un cont și ce înseamnă un sold "
     "contrar naturii lui, ce cere legea de la un document, plafoanele de numerar, "
     "cazurile în care ANAF a impus venituri. Se citește o dată, întreg.",
     "Nu e o listă de monografii. E despre cum vezi că ceva e greșit — nu despre cum se "
     "înregistrează corect."),

    ("Întrebi", "lista:intrebari", "intrebari-formator",
     "Se trimite ca atare. Fiecare întrebare are contextul din notițe, ce anume din "
     "sistem depinde de răspuns și ce s-a presupus între timp, ca să se poată răspunde "
     "fără să recitească nimeni notițele.",
     "Nu e o listă de nelămuriri personale. Fiecare punct blochează ceva concret în "
     "sistem — de-asta scrie lângă el ce anume."),

    ("Adaugi", "lista:parcurs", "parcurs-training-nou",
     "Se citește înainte de a atinge un set nou de notițe: ce întrebări trebuie puse, "
     "unde se scrie fiecare lucru, și cele patru locuri unde se pierde coerența fără ca "
     "vreo poartă să observe.",
     "Nu explică regulile contabile și nu re-descrie porțile. Indică unde scrie — o "
     "parafrază s-ar citi mai ușor decât originalul, deci ar fi crezută în locul lui."),
]

#: Formatele care intră în pachet, pentru documente. `.md` rămâne în repo: e sursa
#: documentelor, nu un format de uz.
FORMATE = [
    (".html", "de citit — monografiile sunt randate ca registru, cu storno în roșu"),
    (".docx", "de tipărit și adnotat"),
]

INTRO = """\
Pachetul e ordonat după **momentul în care ajungi la fiecare fișier**, nu alfabetic și
nu după data trainingului. Numerele din nume dau ordinea; nu le schimba, pentru că
legăturile din pagina asta le urmează.

Materialul de studiu e în ordinea planului de conturi — clasa 1, clasa 2, clasele 3 și
4, salariile, apoi transversalul. Cauți o regulă pe clasa contului, nu pe ziua când s-a predat.

Rândul **„nu”** de sub fiecare item e partea de care e nevoie cel mai des: cinci
documente de contabilitate arată interschimbabile, iar cine caută o regulă o caută în
primul care-i cade sub mână.\
"""

NOTA_FINAL = """\
Toate fișierele din pachet sunt generate din același depozit, printr-o singură comandă,
și trec printr-un set de porți de calitate înainte de a fi scrise. Numerele de mai sus
sunt citite din fișierele reale la generarea paginii, nu scrise de mână — dacă nu
corespund, pagina e veche, nu fișierele.\
"""
