"""MOD_CONTROL_BALANTA — analiticul, sinteticul și clasele, confruntate între ele.

Acoperă F-214 (controlul lunar analitic ↔ sintetic) și F-104 (închiderea exercițiului).

Modulul ăsta a fost **cerut explicit** de formator, sub titlul „Later”: *aplicație care
rulează verificările analitic cu sintetic pe balanță — mijloacele fixe și celelalte
corelații, 121 cu 6 și 7, TVA.* Descrierea vine dintr-un soft pe care îl folosește el, cu
„căsuțe care se înverzesc” la trei verificări.

## Granița față de MOD_INCHIDERE_LUNARA

Cele două module par să facă același lucru și nu-l fac. Distincția e reală și merită
scrisă, altfel al doilea l-ar dubla pe primul:

    MOD_INCHIDERE_LUNARA   verifică SOLDURI pe conturi ANUME — obligațiile salariale,
                           conturile de tranzit, 4423 față de decont. Fiecare linie
                           știe despre ce cont vorbește.

    MOD_CONTROL_BALANTA    verifică PROPRIETĂȚI care trebuie să țină pe ORICE cont:
                           suma analiticelor egalează sinteticul; 121 egalează
                           diferența claselor 6 și 7; soldul are semnul naturii
                           contului. Nu-i pasă ce cont e.

Din cele trei căsuțe ale formatorului, **decontul de TVA e deja implementat** —
MOD_INCHIDERE_LUNARA, blocul V4, corelația C-29. Nu se rescrie aici. Rămân balanța pe
partener (analitic ↔ sintetic) și 121 cu clasele 6 și 7, plus două lucruri pe care
formatorul le-a spus în altă parte a ședinței și care sunt de aceeași natură: soldurile
cu semn contrar naturii contului și continuitatea total-sumelor la preluare.

## De ce nimic aici nu se calculează din altceva

Un modul care ar aduna singur analiticele și le-ar compara cu un sintetic tot calculat de
el ar fi verde întotdeauna. Ar arăta ca o verificare și n-ar fi.

Deci **fiecare comparație are două intrări din surse diferite**, transcrise din două
rapoarte diferite ale aceleiași balanțe: suma analiticelor dintr-o balanță analitică,
soldul sintetic dintr-una sintetică. Când programul de contabilitate le desincronizează —
cazul cel mai frecvent, o operațiune făcută DUPĂ închiderea de lună, fără refacerea ei —
cele două chiar diferă, iar modulul o spune.

Aceeași regulă la 121: se introduc rulajele claselor 6 și 7 și soldul lui 121, trei
mărimi citite separat. Modulul verifică relația dintre ele, nu o produce.

Luna-exemplu se reconciliază pe toate verificările, iar cifrele ei se leagă de celelalte
module: soldul lui 5191 e cel din F-507, al lui 444 e cel din MOD_INCHIDERE_LUNARA, iar
121 de 80.000 e chiar plafonul interimarelor din F-110. Un modul livrat cu celule Check
roșii ar pica la poarta 8; unul livrat cu zerouri ar trece fără să demonstreze nimic.

⚠ LIMITĂRI DECLARATE (vezi Reguli, tabelul C) — nu sunt omisiuni tăcute:
  - verifică ce i se dă, nu balanța însăși: dacă cineva transcrie greșit ambele coloane
    în același fel, modulul e verde. E o verificare de coerență, nu de exactitate;
  - lista conturilor cu analitic obligatoriu e o convenție de cabinet, nu o regulă
    legală — se completează pe măsură ce apar conturi noi cu analitic;
  - nu citește balanța din fișier: cifrele se introduc. Automatizarea citirii e sarcina
    următoare, notată ca atare în tabelul D.
"""

from .comun import sectiune_temei

COD = "MOD_CONTROL_BALANTA"

CATALOG = dict(
    fluxuri="F-214, F-104",
    tip="Lunar, pe balanța de verificare; obligatoriu la preluarea unei societăți",
    variabile="Σ analitice și sold sintetic pe fiecare cont urmărit; rulajele claselor "
              "6 și 7; soldul lui 121; total sume debitoare și creditoare",
    porti="Fiecare comparație are două intrări din surse diferite — vezi Reguli, tabelul C",
    blocuri="V1 Analitic ↔ sintetic; V2 121 cu clasele 6 și 7; "
            "V3 Solduri cu semn contrar naturii; V4 Continuitatea total-sumelor",
    activ="DA",
    prefixe=("Declarații", "Reguli", "Verificări", "Abateri"),
    # Verifică rezultatul celorlalte module, deci stă la coadă indiferent de clasă.
    ordine="final",
)

#: (cont, denumire, de ce are analitic obligatoriu, sursa externă de confruntat)
#: Ordinea NU e pe simbol de cont: e ordinea în care se verifică, cerută explicit de
#: formator la finalul ședinței — „conturile cele mai comune, cele mai esențiale, în ce
#: ordine”. Criteriul: cât de mult strică eroarea, nu cât de mare e contul.
URMARITE = [
    ("512x", "Conturi la bănci",
     "Extrasul e o sursă externă, independentă de contabilitate — deci diferența se "
     "localizează, nu se presupune",
     "Extrasul de cont, pe fiecare bancă"),
    ("4111", "Clienți",
     "Fișa clientului e documentul pe care îl vede și partenerul; o denaturezi o dată "
     "și se propagă în toate confirmările de sold",
     "Confirmarea de sold / fișa partenerului"),
    ("401", "Furnizori",
     "Oglinda lui 4111. E și a doua căsuță verde din softul formatorului",
     "Fișa partenerului"),
    ("542", "Avansuri de trezorerie",
     "Soldul merge în ambele sensuri pe persoane diferite; pe sintetic se anulează și "
     "arată aproape zero — corect ca sumă, fals pe fiecare om",
     "Deconturile semnate, pe fiecare salariat"),
    ("21x / 28x", "Imobilizări și amortizarea lor",
     "Prima verificare cerută de formator pentru aplicație. Registrul mijloacelor fixe "
     "e sursa externă",
     "Registrul mijloacelor fixe (F-214)"),
    ("446", "Alte impozite și taxe",
     "Se ține pe analitic DE LA BUN ÎNCEPUT — a doua taxă apare întotdeauna, iar "
     "despărțirea retroactivă e mult mai scumpă decât analiticul făcut din prima",
     "Fișa pe plătitor din SPV"),
    ("455", "Sume datorate asociaților",
     "Fără analitic, compensarea între doi asociați se ascunde într-un sold total care "
     "arată curat (C-30)",
     "Contractele de creditare"),
    ("1012", "Capital subscris vărsat",
     "Cotele trebuie să se citească din balanță în ziua în care vine hotărârea AGA (C-31)",
     "Certificatul constatator ONRC"),
]

#: cont → (Σ analitice, sold sintetic) pentru luna-exemplu. Trebuie să SE
#: RECONCILIEZE: un modul livrat cu celule Check roșii ar pica la poarta 8, iar unul
#: livrat cu zerouri ar trece fără să demonstreze nimic. Cifrele se leagă de celelalte
#: module — 5191 are soldul din F-507, 444 pe cel din MOD_INCHIDERE_LUNARA.
EXEMPLU = {
    "512x": (145320.50, 145320.50),
    "4111": (238400, 238400),
    "401": (176250, 176250),
    "542": (5000, 5000),
    "21x / 28x": (412000, 412000),
    "446": (12240, 12240),
    "455": (20000, 20000),
    "1012": (30000, 30000),
}

#: cont → sold CU SEMN (pozitiv = debitor). Toate pe sensul corect al naturii lor.
EXEMPLU_SOLD = {
    "4111": 238400, "401": -176250, "409": 8500, "419": -12100,
    "4551": -20000, "5191": -1000, "444": -3250, "4282": 1200,
    "1621": -85000,
}

#: (cont, natura, sensul normal) — pentru blocul V3. Natura vine din planul de conturi,
#: nu se deduce din sold: altfel verificarea și-ar da singură răspunsul.
NATURI = [
    ("4111", "Activ", "Debitor"),
    ("401", "Pasiv", "Creditor"),
    ("409", "Activ", "Debitor"),
    ("419", "Pasiv", "Creditor"),
    ("4551", "Pasiv", "Creditor"),
    ("5191", "Pasiv", "Creditor"),
    ("444", "Pasiv", "Creditor"),
    ("4282", "Activ", "Debitor"),
    # 1621 e datorie: sold debitor la finalul creditului = prea multă rambursare sau
    # prea puțină dobândă înregistrată, cu impozit pe profit și dividende strâmbe.
    # Semnalat de contraverificarea cu revizuirea paralelă din 07.08.
    ("1621", "Pasiv", "Creditor"),
]

#: (ce se sprijină pe el, temei) — secțiunea finală din `Reguli`.
TEMEI_LEGAL = [
    ('Contabilitatea analitică se ține obligatoriu, în dezvoltarea celei sintetice',
     'Legea contabilității 82/1991, art. 2 alin. (1)'),
    ('Balanța de verificare are rolul de a controla exactitatea înregistrărilor și '
     'concordanța dintre contabilitatea sintetică și cea analitică',
     'Legea 82/1991, art. 22 — chiar rostul declarat al balanței'),
    ('Registrele obligatorii: registrul-jurnal, registrul-inventar și Cartea mare',
     'Legea 82/1991, art. 20'),
    ('Situațiile financiare se întocmesc pe baza balanței de verificare',
     'OMFP 1802/2014, pct. 26 și 583'),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_CONTROL_BALANTA", {"A": 34, "B": 18, "C": 18, "D": 54})
    d.titlu("MOD_CONTROL_BALANTA — Declarații (input)")
    d.nota("Cele două coloane se transcriu din DOUĂ rapoarte diferite ale aceleiași "
           "balanțe — analitică și sintetică. Dacă ar veni din același loc, sau dacă "
           "una s-ar calcula din cealaltă, verificarea ar fi verde întotdeauna.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    d.kv("CUI", "=Parametri!B6", tip="calc")
    luna = d.kv("Luna verificată (AAAA-LL)", "2026-07")
    preluare = d.kv("E prima lună după preluarea societății? (DA/NU)", "NU",
                    nota="DA activează blocul V4 — continuitatea total-sumelor")
    d.gol()

    d.sectiune("2. Analitic ↔ sintetic — cele două coloane, din două rapoarte")
    d.cap(["Cont", "Σ analitice", "Sold sintetic", "Sursa externă de confruntat"])
    ref_an = {}
    for cont, den, _, extern in URMARITE:
        r = d.r
        an, si = EXEMPLU[cont]
        d.rand([f"{cont} — {den}", an, si, extern])
        ref_an[cont] = (f"B{r}", f"C{r}")
    d.gol()

    d.sectiune("3. Închiderea claselor 6 și 7 în 121")
    r_cls6 = d.kv("Rulaj total clasa 6 (cheltuieli)", 480000)
    r_cls7 = d.kv("Rulaj total clasa 7 (venituri)", 560000)
    sold_121 = d.kv("Sold 121 din balanță (creditor pozitiv)", 80000,
                    nota="Se citește din balanță, nu se calculează din cele de mai sus")
    d.gol()

    d.sectiune("4. Solduri, pentru verificarea semnului")
    d.nota("Soldul se scrie CU SEMN: pozitiv = debitor, negativ = creditor. Natura "
           "contului vine din tabelul din Reguli, nu din semnul introdus.")
    d.cap(["Cont", "Sold cu semn", "", ""])
    ref_sold = {}
    for cont, _, _ in NATURI:
        r = d.r
        d.rand([cont, EXEMPLU_SOLD[cont], "", ""])
        ref_sold[cont] = f"B{r}"
    d.gol()

    d.sectiune("5. Continuitatea total-sumelor (doar la preluare)")
    ts_d_ant = d.kv("Total sume DEBITOARE, balanța lunii anterioare", 2450000)
    ts_c_ant = d.kv("Total sume CREDITOARE, balanța lunii anterioare", 2450000)
    ts_d = d.kv("Total sume DEBITOARE, luna curentă", 2780000)
    ts_c = d.kv("Total sume CREDITOARE, luna curentă", 2780000)
    d.gol()

    d.sectiune("6. Control")
    d.kv("Modul activ?",
         '=IF(INDEX(CatalogModule!$A$1:$A$200,'
         'MATCH("MOD_CONTROL_BALANTA",CatalogModule!$B$1:$B$200,0))="DA",'
         '"ACTIV","INACTIV")', tip="calc")
    d.kv("Cauza cea mai frecventă a diferenței analitic ↔ sintetic",
         "O operațiune făcută DUPĂ închiderea de lună, fără refacerea închiderii. "
         "Programul te lasă, iar diferența nu se anunță singură.", tip="calc")
    d.kv("Ordinea de verificare",
         "Tabelul A din Reguli e ordonat după cât de mult strică eroarea, nu după "
         "simbolul contului — cum a cerut formatorul la finalul ședinței.", tip="calc")

    # ------------------------------------------------------------------- Reguli
    g = F("Reguli_CONTROL_BALANTA", {"A": 16, "B": 30, "C": 52, "D": 40})
    g.titlu("MOD_CONTROL_BALANTA — Reguli (tabele fixe)")
    g.nota("Ce e regulă dată, nu formulă: ordinea de verificare, naturile conturilor și "
           "limitele modulului.")
    g.gol()

    g.sectiune("Tabelul A — Ordinea de verificare")
    g.nota("Ordonat după cât de mult strică eroarea, nu după simbolul contului. "
           "Formatorul a cerut explicit „conturile cele mai comune, cele mai esențiale, "
           "în ce ordine”.")
    g.cap(["Cont", "Denumire", "De ce are analitic obligatoriu", "Sursa externă"])
    for cont, den, motiv, extern in URMARITE:
        g.rand([cont, den, motiv, extern])
    g.gol()

    g.sectiune("Tabelul B — Naturile conturilor verificate")
    g.nota("Natura vine de aici, nu din soldul introdus. Un cont de activ cu sold "
           "creditor nu e o curiozitate de balanță — e o eroare care încă n-a fost "
           "căutată (C-23).")
    g.cap(["Cont", "Natura", "Sensul normal al soldului", ""])
    for cont, natura, sens in NATURI:
        g.rand([cont, natura, sens, ""])
    g.gol()

    g.sectiune("Tabelul C — LIMITĂRI DECLARATE")
    for linie in [
        "• Modulul verifică CE I SE DĂ, nu balanța însăși. Dacă ambele coloane sunt "
        "transcrise greșit în același fel, iese verde — e verificare de coerență, nu de "
        "exactitate.",
        "• Lista conturilor cu analitic obligatoriu e o convenție de cabinet, nu o "
        "regulă legală. Se completează pe măsură ce apar conturi noi cu analitic.",
        "• Cifrele se introduc; modulul nu citește balanța din fișier. Citirea automată "
        "e sarcina următoare — vezi tabelul D.",
        "• Decontul de TVA (a treia căsuță a formatorului) NU e aici: e deja "
        "implementat în MOD_INCHIDERE_LUNARA, blocul V4, corelația C-29.",
        "• V4 se rulează doar la preluare. În restul lunilor continuitatea e dată de "
        "faptul că lucrezi în același fișier.",
    ]:
        g.nota(linie)
    g.gol()

    g.sectiune("Tabelul D — Ce rămâne de automatizat")
    g.cap(["Pasul", "Ce ar face", "De ce nu e făcut încă", ""])
    for rand in [
        ("Citirea balanței", "Preluarea cifrelor direct din fișierul de balanță",
         "Formatul diferă de la un program la altul; cere o hartă pe fiecare", ""),
        ("Detectarea analiticelor", "Recunoașterea automată a conturilor cu analitic",
         "Cere convenția de denumire a analiticelor, care nu e uniformă", ""),
        ("Localizarea diferenței", "Nu doar CĂ diferă, ci pe ce analitic",
         "Cere balanța analitică rând cu rând, nu doar totalul", ""),
    ]:
        g.rand(list(rand))

    sectiune_temei(g, TEMEI_LEGAL)

    # --------------------------------------------------------------- Verificări
    v = F("Verificări_CONTROL_BALANTA",
          {"A": 10, "B": 40, "C": 18, "D": 18, "E": 16, "F": 56})
    v.titlu("MOD_CONTROL_BALANTA — Verificări")
    v.nota("O linie pe verificare. Coloana „Diferență” e ce contează: zero înseamnă că "
           "cele două surse spun același lucru.")
    v.gol()

    D = "Declarații_CONTROL_BALANTA"
    verificari = []

    v.sectiune("V1 — analitic ↔ sintetic, în ordinea de verificare")
    v.cap(["Cod", "Ce verifică", "Σ analitice", "Sold sintetic", "Diferență", "Verdict"])
    for cont, den, _, _ in URMARITE:
        an, si = ref_an[cont]
        v.rand(["C-37", f"{cont} — {den}",
                f"={D}!{an}", f"={D}!{si}", f"={D}!{an}-{D}!{si}",
                f'=IF(ABS(E{v.r})<0.01,"OK",'
                f'"ATENȚIE — analiticul diferă de sintetic cu "'
                f'&TEXT(E{v.r},"#,##0.00")&" lei; cauza tipică: operațiune după '
                f'închiderea de lună, fără refacerea ei")'])
        verificari.append(("C-37", f"{cont} analitic ↔ sintetic", f"E{v.r - 1}"))
    v.gol()

    v.sectiune("V2 — 121 cu clasele 6 și 7")
    v.cap(["Cod", "Ce verifică", "Calculat", "Din balanță", "Diferență", "Verdict"])
    v.rand(["—", "clasa 7 − clasa 6 = sold 121",
            f"={D}!{r_cls7}-{D}!{r_cls6}", f"={D}!{sold_121}",
            f"={D}!{sold_121}-({D}!{r_cls7}-{D}!{r_cls6})",
            f'=IF(ABS(E{v.r})<0.01,"OK — 6 și 7 s-au închis complet în 121",'
            f'"ATENȚIE — cel mai probabil 121 din anul precedent n-a fost închis; '
            f'se vede la bilanț, când cifrele nu se leagă")'])
    verificari.append(("—", "121 vs. clasele 6 și 7", f"E{v.r - 1}"))
    v.gol()

    v.sectiune("V3 — solduri cu semn contrar naturii contului")
    v.cap(["Cod", "Ce verifică", "Sold cu semn", "Sens normal", "Abatere", "Verdict"])
    for cont, natura, sens in NATURI:
        s = ref_sold[cont]
        # Abaterea e soldul care are semnul GREȘIT, zero altfel. Sensul normal vine
        # din tabelul de mai sus, nu din soldul introdus.
        cond = f"{D}!{s}<0" if sens == "Debitor" else f"{D}!{s}>0"
        v.rand(["C-23", f"{cont} — {natura}, sold normal {sens.lower()}",
                f"={D}!{s}", sens,
                f'=IF({cond},ABS({D}!{s}),0)',
                f'=IF(E{v.r}<0.01,"OK",'
                f'"ATENȚIE — {cont} are sold contrar naturii: '
                f'"&TEXT(E{v.r},"#,##0.00")&" lei pe sensul greșit")'])
        verificari.append(("C-23", f"{cont} sens sold", f"E{v.r - 1}"))
    v.gol()

    v.sectiune("V4 — continuitatea total-sumelor (la preluare)")
    v.cap(["Cod", "Ce verifică", "Luna anterioară", "Luna curentă", "Creștere", "Verdict"])
    for eticheta, ant, cur in (("debitoare", ts_d_ant, ts_d),
                               ("creditoare", ts_c_ant, ts_c)):
        v.rand(["C-39", f"total sume {eticheta} cresc monoton",
                f"={D}!{ant}", f"={D}!{cur}",
                f'=IF({D}!{preluare}<>"DA",0,MIN(0,{D}!{cur}-{D}!{ant}))',
                f'=IF({D}!{preluare}<>"DA","— (nu e lună de preluare)",'
                f'IF(E{v.r}>=0,"OK — total sumele au continuitate",'
                f'"ATENȚIE — total sumele au SCĂZUT: s-au preluat soldurile ca sold '
                f'inițial, nu total sumele. Orice verificare pe rulaj devine falsă"))'])
        verificari.append(("C-39", f"total sume {eticheta}", f"E{v.r - 1}"))
    v.gol()

    v.sectiune("Control final")
    total = "+".join(f"ABS({r})" for _, _, r in verificari)
    v.check("Check — toate verificările balanței", f"={total}",
            f'=IF(ABS(B{v.r})<0.01,"OK — balanța e coerentă pe toate verificările",'
            f'"EROARE — vezi foaia Abateri")')

    # ------------------------------------------------------------------ Abateri
    a = F("Abateri_CONTROL_BALANTA", {"A": 10, "B": 12, "C": 44, "D": 16, "E": 60})
    a.titlu("MOD_CONTROL_BALANTA — Abateri")
    a.nota("Coloana „Include” spune DA doar unde verificarea n-a trecut. Lista e "
           "completă: dacă toate sunt NU, balanța e coerentă.")
    a.gol()
    a.cap(["Include", "Cod", "Ce nu s-a potrivit", "Diferență", "Ce se face"])
    ACTIUNE = {
        "C-37": "Se reface închiderea de lună — cauza cea mai frecventă. Dacă persistă, "
                "se compară balanța analitică rând cu rând cu sursa externă din "
                "tabelul A, ca să se localizeze analiticul.",
        "—": "Se verifică dacă 121 din anul precedent a fost închis. Nu există "
             "automatism ca la TVA: închiderea lui 121 se face manual, la începutul "
             "exercițiului următor.",
        "C-23": "Se caută operațiunea care a răsturnat soldul. Un cont de activ cu sold "
                "creditor e cel mai des un avans neînregistrat ca avans (vezi F-415).",
        "C-39": "Se reface preluarea: se introduc TOTAL SUMELE debitoare și creditoare "
                "din balanța de preluare, nu soldurile. Altfel rulajele anului pornesc "
                "de la zero din luna preluării.",
    }
    V = "Verificări_CONTROL_BALANTA"
    for cod, eticheta, ref in verificari:
        a.rand([f'=IF(ABS({V}!{ref})<0.01,"NU","DA")', cod, eticheta,
                f"={V}!{ref}", ACTIUNE[cod]])
    a.gol()
    a.check("Check — număr de abateri",
            f'=COUNTIF(A{a.r - len(verificari) - 1}:A{a.r - 2},"DA")',
            f'=IF(B{a.r}=0,"OK — nicio abatere",'
            f'"ATENȚIE — "&B{a.r}&" verificări nu trec")')
