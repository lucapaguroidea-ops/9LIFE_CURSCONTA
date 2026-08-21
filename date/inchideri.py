"""Cadența de urmărire a conturilor — partea care NU se poate deduce din fluxuri.

Diagnosticul care a produs fișierul ăsta: rândurile listei „conturi de urmărit periodic”
nu sunt recomandări de urmărire, ci **aserțiuni despre soldul așteptat al unui cont la un
moment de timp**:

    473 → sold zero · 581 → sold zero · 4426/4427 → fără sold după închidere

Adică exact predicatul pe care poarta 2 îl cere fiecărui flux — „stare terminală
declarată” — ridicat de la capătul unui flux la capătul unei luni. Nu e un concept nou
în sistem; e unul existent, aplicat la altă scară.

De aceea foaia `Închideri periodice` se DERIVĂ: `build/inchideri.py` citește aserțiunile
`Sold … = …` din pașii de verificare ai fluxurilor. Sunt deja acolo, scrise: F-405 spune
„Sold 4426 = 0; sold 4427 = 0”, F-501 spune „Sold 581 = 0”. O listă scrisă separat ar fi
al doilea adevăr, care diverge de monografii.

Ce rămâne aici: **cadența** (lunar / trimestrial) și motivul. Nu se deduc din niciun
flux — un flux spune ce stare atinge contul, nu cât de des trebuie să te uiți la el.
Asta e judecată profesională, deci se scrie de mână.

Textul din coloana „de ce” e cel din sursa 19.08.2026, verbatim. Poarta 16 verifică
faptul că a ajuns aici, iar poarta 17 că fiecare cont e chiar starea terminală a unui flux.
"""

TITLU = "CONTURI DE URMĂRIT PERIODIC — disciplina de închidere"

NOTA = ("Răspuns la întrebarea din notițe: care sunt conturile care trebuie urmărite "
        "cel puțin trimestrial, dacă nu lunar.")

#: Cadențele, cu titlurile exacte din sursă — sunt și titlurile blocurilor din foaie.
CADENTE = ["Lunar — obligatoriu", "Cel puțin trimestrial"]

#: (conturi, cadență, de ce). Conturile se scriu ca în sursă; `build/inchideri.py` le
#: sparge pe simboluri ca să caute aserțiunea de stare terminală a fiecăruia.
CADENTA = [
    ("4426 / 4427 / 4423 / 4424", "Lunar — obligatoriu",
     "închiderea TVA; orice sold rămas e o eroare"),
    # ---- salarii și rețineri (sursa 21.08) --------------------------------
    ("421 / 423", "Lunar — obligatoriu",
     "soldul creditor trebuie să fie restul de plată de pe stat (C-24); documentul de "
     "control există deja, deci verificarea durează secunde"),
    ("444 / 4315 / 4316 / 436", "Lunar — obligatoriu",
     "rulaj creditor = sold creditor (C-25, C-26); sold mai mare = obligații restante, "
     "iar stopajul la sursă nevirat peste 30 de zile e infracțiune"),
    ("427", "Lunar — obligatoriu",
     "rulaj creditor = sold creditor (C-28); banii sunt opriți din salariul altcuiva, "
     "deci un sold care persistă trece din contabil în penal"),
    ("4382", "Lunar — obligatoriu",
     "indemnizații de recuperat de la FNUASS; un sold care nu se stinge înseamnă bani "
     "ai firmei blocați în dosare incomplete"),
    ("426", "Cel puțin trimestrial",
     "drepturi neridicate; dacă nu se golesc, se caută salariatul, nu se reportează"),
    ("4282", "Cel puțin trimestrial",
     "creanțe față de foști salariați; sold creditor = contrar naturii (C-23)"),
    ("4418", "Cel puțin trimestrial",
     "impozit micro; sold creditor = obligația trimestrului curent, sold debitor = "
     "plată în plus, de investigat"),

    ("4428", "Lunar — obligatoriu",
     "bifuncțional; trebuie să se golească pe operațiunile facturate"),
    ("408 / 418", "Lunar — obligatoriu",
     "bifuncționale; risc de dublare a gestiunii"),
    ("471 / 472", "Lunar — obligatoriu",
     "reluarea eșalonată trebuie făcută lună de lună"),
    ("473 Decontări din operațiuni în curs de clarificare", "Lunar — obligatoriu",
     "trebuie să ajungă la sold zero; altfel ascunde erori"),
    ("581 Viramente interne", "Lunar — obligatoriu",
     "trebuie să aibă sold zero; sold ≠ 0 = transfer neînchis"),
    ("5311 / 5121", "Lunar — obligatoriu",
     "reconciliere cu extrasul și cu registrul de casă"),
    ("542 Avansuri de trezorerie", "Lunar — obligatoriu",
     "deconturi nejustificate"),

    ("4091 – 4094", "Cel puțin trimestrial",
     "avansuri care nu s-au stornat la factura finală"),
    ("419", "Cel puțin trimestrial",
     "avansuri de la clienți rămase deschise"),
    ("401 / 411", "Cel puțin trimestrial",
     "balanță analitică; solduri cu semn contrar = eroare"),
    ("455", "Cel puțin trimestrial",
     "sume datorate asociaților, cu restricții legale"),
    ("461 / 462", "Cel puțin trimestrial",
     "debitori/creditori diverși, se împotmolesc ușor"),
    ("231", "Cel puțin trimestrial",
     "imobilizări în curs care trebuiau puse în funcțiune"),
    ("1621 / 5187", "Cel puțin trimestrial",
     "credite și dobânzi de calculat"),

    # Cele două de mai jos NU sunt în sursa 19.08. Le-a găsit derivarea: sunt conturi
    # de tranzit „în curs de aprovizionare”, cu rol în flux și cu stare terminală
    # „sold = 0” declarată în monografie. Un cont care trebuie să se golească și nu e
    # urmărit e exact clasa de defect pe care lista o previne, deci lipsa lor din sursă
    # e o omisiune a sursei, nu o decizie.
    ("327 Mărfuri în curs de aprovizionare", "Lunar — obligatoriu",
     "tranzit; sold ≠ 0 înseamnă marfă plătită și neintrată în gestiune (F-302)"),
    ("223 Instalații tehnice și mijloace de transport în curs de aprovizionare",
     "Cel puțin trimestrial",
     "tranzit pe imobilizări; sold ≠ 0 înseamnă recepție neînregistrată (F-207)"),
]

# ---------------------------------------------------------------------------
# Scutirile de la sensul invers al porții 17
#
# Poarta cere ca orice cont CU ROL ÎN FLUX care declară „sold = 0” într-o monografie
# să aibă o cadență. Cele de mai jos declară starea, dar nu se urmăresc periodic —
# fiecare cu motivul lui. Fără lista asta, poarta ar cere cadență pentru conturi care
# se golesc prin însăși operațiunea, nu prin calendar.
# ---------------------------------------------------------------------------

FARA_CADENTA = {
    "121": "Se golește la închiderea exercițiului, prin reportare. Cadența lui e "
           "anuală și e chiar F-104, nu o verificare periodică.",
    "129": "Idem 121: repartizarea profitului se face o dată, la aprobarea situațiilor.",
    "2812": "Amortizarea cumulată se golește la ieșirea activului, nu la o dată din "
            "calendar. Se verifică pe operațiune (F-211), nu periodic.",
    "308": "Diferențele de preț se sting pe măsura consumului, proporțional. Un sold "
           "acolo e normal cât timp există stoc.",
    "711": "Se închide la 31.12 împreună cu variația stocurilor (F-314). Sold în cursul "
           "anului e starea normală, nu o eroare.",
}

# ---------------------------------------------------------------------------
# Golurile declarate
#
# Un cont din listă care nu e starea terminală a niciunui flux înseamnă că
# checklistul afirmă ceva ce sistemul nu demonstrează nicăieri. Nu se ascunde:
# rândul apare în foaie FĂRĂ ancoră, exact cum C-22 a rămas fără ancoră de modul
# pentru că niciun modul nu-i acoperea fluxurile.
#
# Cheia e simbolul de cont; valoarea spune ce lipsește ca golul să se închidă.
# ---------------------------------------------------------------------------

GOLURI = {
    "4424": "F-405 declară starea lui 4426/4427, nu și pe a lui 4424 (TVA de recuperat).",
    "4428": "Se golește în F-408, F-316 și F-401, dar niciunul nu declară asta ca stare "
            "terminală pe 4428 — se vede doar pe conturile din jur.",
    "5311": "Reconcilierea cu registrul de casă nu e flux: nu produce articol contabil.",
    "5121": "Reconcilierea cu extrasul nu e flux.",
    "4091": "F-410 declară starea lui 409 la nivel sintetic, nu pe analiticele de "
            "destinație 4091–4094.",
    "4092": "Idem 4091.",
    "4093": "Idem 4091 — plus că avansul pentru imobilizări are furnizor 404, nu 401.",
    "4094": "Idem 4093.",
    "401": "Nu există flux care să declare „401 fără sold debitor”. Regula e o corelație "
           "de sold contrar naturii, nu o stare terminală de flux.",
    "411": "Idem 401 — vezi C-23.",
    "455": "Nu există flux pe 455. Restricțiile de numerar sunt rămase deschise.",
    "461": "Nu există flux pe debitori/creditori diverși.",
    "462": "Idem 461.",
    "5187": "F-107 declară starea lui 1621, nu și dobânda de calculat pe 5187.",
}
