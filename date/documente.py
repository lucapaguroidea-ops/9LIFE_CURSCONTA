"""Planul de armonizare a celor trei documente revizuite.

Ce se schimbă:

1. **Legenda.** Toate trei o au deja — dar una e un rând inline, una un tabel fără
   titlu, una un tabel sub „Cum citești acest document”. Devine aceeași peste tot.
2. **Anexele.** Secțiunile care joacă deja rol de anexă (checklist, ce s-a corectat,
   ce a rămas deschis, recapitulare de conturi) se redenumesc `Anexa X — …` și se mută
   la spate, în aceeași ordine. Textul lor nu se atinge.
3. **Anexa E — Baza legală citată** se GENEREAZĂ din text acolo unde lipsește:
   se extrag actele normative citate în document. Derivare, nu invenție — fiecare
   intrare trebuie să existe în textul sursă.

Ce NU se schimbă: corpul documentelor. Nicio secțiune de conținut nu se rescrie, nu se
scurtează și nu se reordonează. Poarta de conservare din `build/documente.py` verifică
faptul că fiecare linie din original se regăsește în varianta armonizată.

Fișierele din `surse/` rămân neatinse — rezultatul se scrie în `dist/`.
"""

LEGENDA_TITLU = "Cum citești acest document"

#: Formularea canonică e chiar cea din documentul trainingului 4 — el e cel care avea
#: deja forma completă, iar celelalte două o preiau cuvânt cu cuvânt. Așa, documentul
#: care o avea deja nu trebuie atins deloc.
LEGENDA_TABEL = [
    ("✅", "Notița originală era corectă — doar reformulată/completată"),
    ("⚠️", "**Eroare în notița originală** — corectată aici, cu explicație"),
    ("➕", "Completare (lucru care lipsea, dar era necesar ca raționamentul să stea "
           "în picioare)"),
    ("❓", "Rămas deschis — de clarificat cu formatorul (vezi Anexa D)"),
]

#: Ordinea și denumirile canonice ale anexelor. Un document nu trebuie să le aibă pe
#: toate; are doar pe cele pentru care există conținut real.
ANEXE = {
    "A": "Recapitulare: conturi și perechile lor",
    "B": "Checklist practic",
    "C": "Ce am corectat față de notițele originale",
    "D": "Rămase deschise",
    "E": "Baza legală citată",
    "F": "Erori din notițele brute, NEreintroduse",
    "G": "Răspunsuri verificate pe surse publice",
}

#: Conținut adus din foaia Legendă a workbook-ului, ca documentul trainingului 4 să
#: aibă și el setul de erori evitate — există deja, dar doar în Excel.
ANEXA_F_TRAINING_4 = """Erorile de mai jos existau în notițele brute și au fost corectate
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
"""

#: Defectele găsite la verificarea cifrelor sursei din 19.08.2026. Toate șase cad în
#: documentul de stocuri, pentru că toate sunt în §2–§6 ale sursei. Se adaugă la Anexa C
#: existentă, cu textul original alături — reparate tăcut, ar fi dispărut din istorie.
CORECTII_SURSA_19_08 = """### Corecții la materialul din 19.08.2026

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
asupra controlului. Punctele 5–6 sunt afirmații incomplete, nu greșite."""

DOCUMENTE = [
    dict(
        nume="capitaluri",
        zi="07.08.2026",
        cheie="doc:capitaluri",
        sursa="surse/training-2-2026-08-07/notite-revizuit.md",
        iesire="dist/capitaluri-credite-provizioane.md",
        titlu="Capitaluri, credite, leasing și provizioane",
        subtitlu="Surse: training 07.08.2026 · adâncit cu 19.08.2026, 21.08.2026 și 26.08.2026 — versiune revizuită",
        adaugiri=[
            # Închiderea lui 121 și impozitul pe profit sunt F-104: capitaluri, nu
            # stocuri. Sursa le ține sub §2, „mărfuri” — aici se rup de acolo.
            dict(bloc="## 2. Mărfuri la preț cu amănuntul (371)",
                 in_sectiune="## 2. Pierderea contabilă vs. pierderea fiscală"),
            # Impozitarea rezultatului (21.08) adâncește F-104. Documentul n-avea
            # secțiune despre regimul de impozitare — e un gol de subiect, nu o tranșă.
            dict(bloc="## 6. Impozit pe profit sau impozit pe venit",
                 sectiune_noua="Impozit pe profit sau impozit pe venit (micro)"),
            # Dividendele au deja un fir în §1 (restricțiile L. 239/2025) și în §1.3
            # (cota de 16%), dar acolo e vorba de CÂND se POATE distribui. Materialul
            # din 26.08 e despre CUM se face — cotele din 1012, impozitul, interimarele,
            # regularizarea — și e destul cât să stea singur, nu îngropat în §1.
            dict(bloc="## 2. Dividende",
                 sectiune_noua="Dividende: repartizare, impozit și interimare"),
            # Creditarea e datorie față de asociat, nu capital propriu: 455 stă lângă
            # capitaluri pentru că e finanțare de la același om, nu pentru că ar fi
            # aceeași natură. De aceea secțiune proprie, nu subsecțiune în §1.
            #
            # Simbolul de cont se pune la COADA titlului, nu în mijloc. Poarta 16
            # acceptă un titlu îmbogățit prin containment — „Dividende” se regăsește în
            # „Dividende: repartizare, impozit și interimare” — dar o inserție la mijloc
            # rupe potrivirea, și chiar asta s-a întâmplat la prima încercare.
            dict(bloc="## 3. Creditarea de societate și relațiile cu asociații",
                 sectiune_noua="Creditarea de societate și relațiile cu asociații (455)"),
        ],
        # rândurile de legendă vechi, înlocuite de tabelul canonic
        legenda_veche=[
            "**Legendă:**",
            "`✅` confirmat · `⚠️` corectat față de notița originală · "
            "`❓` de confirmat cu trainerul · `➕` completare (nu era în notițe)",
        ],
        anexe={
            "## 11. Checklist lunar / trimestrial rezultat din notițe": "B",
            "## 10. Listă de verificat / întrebări pentru trainer": "D",
        },
        genereaza=["E", "G"],
        inlocuiri=[
            dict(text="- ❓ **Răspuns la (Q – ONRC):**",
                 devine="- ✅ **Răspuns la (Q – ONRC):**",
                 motiv="Legenda spune că ❓ înseamnă „rămas deschis”. Rândul ăsta e un "
                       "răspuns tranșat, deci ✅. Cu marcajul vechi, cine căuta ce e "
                       "provizoriu găsea un rezultat fals — iar poarta 13 verifică forma "
                       "legendei, nu aplicarea ei."),
            dict(text="### 3.4 ❓ Răspuns la întrebarea ta despre 1174",
                 devine="### 3.4 ✅ Răspuns la întrebarea ta despre 1174",
                 motiv="Același lucru: titlul anunță un răspuns, nu o întrebare deschisă."),

            dict(text="**venituri totale sub 100.000 EUR** ❓, calculate la cursul de la "
                      "închiderea\n   exercițiului anterior. Pragul e din Codul fiscal, "
                      "nu din OMFP.",
                 devine="**venituri totale sub 100.000 EUR** ✅, calculate la cursul de "
                        "la închiderea\n   exercițiului anterior. Pragul e din Codul "
                        "fiscal, nu din OMFP, și a coborât în trepte: 500.000 până în "
                        "2024, 250.000 în 2025, **100.000 din 2026**.",
                 motiv="Verificat pe surse publice la 21.08.2026: Cod fiscal, Titlul IV."),

            dict(text="Cota este 1% ❓.",
                 devine="✅ Cota este **1%**, unică: cota de 3% pentru firmele fără "
                        "salariat a fost **eliminată de la 1 ianuarie 2026**.",
                 motiv="Verificat pe surse publice la 21.08.2026: Cod fiscal, Titlul IV."),
        ],
        nota="Rolul Anexei C îl joacă secțiunea 0 (Sinteza corecțiilor), păstrată în "
             "față pentru că funcționează ca rezumat executiv al documentului.",
    ),
    dict(
        nume="imobilizari",
        zi="12.08.2026",
        cheie="doc:imobilizari",
        sursa="surse/training-3-2026-08-12/notite-revizuit.md",
        iesire="dist/imobilizari.md",
        titlu="Imobilizări",
        subtitlu="Surse: training 12.08.2026 · adâncit cu 19.08.2026 și 26.08.2026 — "
                 "versiune revizuită, reorganizată și contraverificată",
        adaugiri=[
            dict(bloc="## 7. Operațiuni speciale",
                 in_sectiune="## 11. Ieșiri din gestiune"),
            # Subvenția pentru investiții e despre un ACTIV pe toată durata lui de
            # amortizare: fără imobilizare n-are ce relua la venit. Documentul n-avea
            # secțiune pe subiect, deși F-210 exista — e un gol de temă, nu o tranșă.
            dict(bloc="## 1. Subvenții pentru investiții și fonduri europene",
                 sectiune_noua="Subvenții pentru investiții și fonduri europene"),
        ],
        legenda_veche=[
            "**Legendă folosită în document:**",
            "| Marcaj | Semnificație |",
            "|---|---|",
            "| ✅ | Din notițe, confirmat corect |",
            "| ⚠️ | **Corectat** — în notițe era greșit sau ambiguu |",
            "| ➕ | Completare (nu era în notițe, dar lipsea din raționament) |",
            "| ❓ | De clarificat cu formatorul / de verificat în speța concretă |",
        ],
        anexe={
            "## 14. Tabel corespondențe cont de activ ↔ cont de amortizare": "A",
            "## 16. Lista erorilor corectate din notițe": "C",
            "## 17. De clarificat / întrebări pentru mail": "D",
        },
        genereaza=["E", "G"],
        nota="Secțiunea 18 (anticiparea sesiunii pe ajustări) rămâne în corp, nu în "
             "anexe: e conținut de continuare, nu material de referință.",
    ),
    dict(
        nume="stocuri-tva",
        zi="14.08.2026",
        cheie="doc:stocuri-tva",
        sursa="surse/training-4-2026-08-14/notite-revizuit.md",
        iesire="dist/stocuri-tva-corelatii.md",
        titlu="Stocuri, TVA și corelații de balanță",
        subtitlu="Surse: training 14.08.2026 · adâncit cu 19.08.2026, 21.08.2026 și "
                 "28.08.2026 — "
                 "stocuri (clasa 3), TVA și corelații de balanță, versiune revizuită",
        adaugiri=[
            dict(bloc="## 4. Mecanica TVA", in_sectiune="## 7. Conturile de TVA"),
            # Decontul și D300 (21.08) adâncesc F-405 și F-407 — aceeași secțiune de TVA
            dict(bloc="## 7. Decontul de TVA și D300",
                 in_sectiune="## 7. Conturile de TVA"),
            dict(bloc="## 2. Mărfuri la preț cu amănuntul (371)",
                 in_sectiune="## 8. Mărfuri (371)"),
            dict(bloc="## 3. Ajustări pentru deprecierea stocurilor",
                 in_sectiune="## 8. Mărfuri (371)"),
            # Clasele 40 și 41 nu aveau secțiune-gazdă: e un gol de subiect într-un
            # document titrat pe subiect, deci devin secțiune proprie.
            dict(bloc="## 5. Furnizori — clasa 40",
                 sectiune_noua="Furnizori și clienți — clasele 40 și 41"),
            dict(bloc="## 6. Clienți — clasa 41",
                 sectiune_noua="Furnizori și clienți — clasele 40 și 41"),
            # Recapitularea taxării inverse (28.08) intră în secțiunea care o tratează
            # deja: aduce codurile D394 și regula că la LIVRARE nu se face notă
            # contabilă — două lucruri care lipseau de acolo.
            dict(bloc="## 1. Recapitulare: taxarea inversă",
                 in_sectiune="## 5. Taxarea inversă pe teritoriul României "
                             "(art. 331 Cod fiscal)"),
            # Corespondențele clasa 6 ↔ clasa 3 traversează TOATE secțiunile de stocuri
            # — 301, 302, 303, 371, 381 — deci n-au o gazdă naturală. Sunt un subiect
            # propriu: nu „ce stoc”, ci „cum iese stocul pe cheltuială”.
            dict(bloc="## 9. Cheltuielile de clasa 6 și gestiunile de clasa 3",
                 sectiune_noua="Cheltuielile de clasa 6 și gestiunile de clasa 3"),
        ],
        legenda_veche=[],          # are deja forma canonică
        anexe={},                  # anexele A–E sunt deja denumite corect
        # Defecte prinse de poarta 30 (denumirea afirmată aparține altui simbol) la
        # contraverificarea cu revizuirile paralele T2–T7. 7015 e cel mult un analitic
        # al lui 701 în softuri; denumirea „Venituri din vânzarea produselor finite” e
        # a sinteticului 701. 5111 nu există — Cecuri de încasat e 5112. Nu se ating
        # monografiile: o postare pe analiticul 7015 e legitimă; doar AFIRMAȚIA că 7015
        # poartă denumirea sinteticului e greșită.
        inlocuiri=[
            dict(text='- **7015** „Venituri din vânzarea produselor finite" — la '
                      'vânzare.',
                 devine='- **701** „Venituri din vânzarea produselor finite" — la '
                        'vânzare (în multe softuri se ține pe analiticul **7015**).',
                 motiv="Denumirea e a sinteticului 701; 7015 e analitic, nu sintetic. "
                       "Poarta 30."),
            dict(text="Corect este **7015** (+ 711 pe traseu).",
                 devine="Corect este **701** (+ 711 pe traseu); 7015 e analiticul lui "
                        "în multe softuri.",
                 motiv="Corecția mea înlocuise 704 cu 7015 — un cont fără rând în plan. "
                       "Sinteticul care poartă denumirea e 701."),
            dict(text="corect **7015** și 711",
                 devine="corect **701** și 711",
                 motiv="Aceeași corecție, în rândul din Anexa C. Partea din stânga "
                       "(citatul brutului „704 și 7015”) rămâne, e ce a scris nota."),
            dict(text="iar **5111** este *Cecuri de încasat*",
                 devine="iar **5112** este *Cecuri de încasat*",
                 motiv="5111 nu există în plan; Cecuri de încasat e 5112. Poarta 30."),
        ],
        genereaza=["F", "G"],
        extinde_anexe={"C": CORECTII_SURSA_19_08},
        nota="Singurul care avea deja anexele denumite. Primește Anexa F, care exista "
             "doar ca notă în foaia Legendă a workbook-ului.",
    ),
    dict(
        cheie="doc:salarii",
        nume="salarii",
        zi=None,   # sursa din 21.08 se împarte la patru documente, ca cea din 19.08
        repartizat=True,
        sursa=None,
        iesire="dist/salarii-contributii-retineri.md",
        titlu="Salarii, contribuții și rețineri",
        subtitlu="Sursă: training 21.08.2026 — de la statul de plată la balanță, "
                 "cu verificările care se fac în secunda doi",
        legenda_veche=[],
        inlocuiri=[
            dict(text="Salariul minim brut pe economie este **4.325 lei** ❓.",
                 devine="✅ Salariul minim brut pe economie este **4.325 lei**, de la "
                        "**1 iulie 2026** (anterior 4.050 lei) — HG 146/2026. Tot de "
                        "atunci și până la 31.12.2026, suma neimpozabilă lunară scade "
                        "de la 300 la **200 lei**.",
                 motiv="Verificat pe surse publice la 21.08.2026: HG 146/2026. Cifra "
                       "din notițe era corectă, dar nedatată — iar un prag fără dată "
                       "nu se poate aplica la o operațiune."),

            dict(text="❓ Tratamentul exact al reținerilor din indemnizația de concediu "
                      "medical — ce contribuții\n"
                      "se datorează și pe ce parte — nu era "
                      "în notițe și nu îl afirm aici.",
                 devine="✅ **Reținerile din indemnizație.** Se rețin **CAS 25%** și "
                        "**impozit 10%**. **CASS 10% se datorează începând cu "
                        "veniturile lunii august 2026** (Legea 170/2026) — până atunci "
                        "nu se datora; fac excepție indemnizațiile pentru accidente de "
                        "muncă și boli profesionale. **CAM 2,25% NU se datorează** pe "
                        "partea suportată din FNUASS (art. 220^5 Cod fiscal): "
                        "angajatorul datorează CAM doar pe zilele pe care le suportă "
                        "el. Baza de calcul e media veniturilor brute din ultimele 6 "
                        "luni, plafonată la 12 salarii minime brute pe lună. "
                        "*(art. 139 alin. (1) lit. o) și art. 144 Cod fiscal; "
                        "OUG 158/2005 — verificat 21.08.2026)*",
                 motiv="Verificat pe surse publice. Răspunsul e relevant imediat: "
                       "notițele sunt din 21.08.2026, iar CASS-ul a devenit datorat "
                       "chiar pe veniturile lunii august."),

            dict(text="❓ Limita de o treime se aplică datoriilor obișnuite; pentru "
                      "obligații de întreținere\nlegea prevede o limită mai mare. "
                      "Procentul aplicabil pe caz concret — de confirmat.",
                 devine="✅ **Sunt trei reguli, nu una** (art. 729 Cod procedură "
                        "civilă): **1/2** din venitul net pentru obligații de "
                        "întreținere sau alocații pentru copii · **1/3** pentru orice "
                        "alte datorii · la mai multe popriri pe aceeași sumă, reținerea "
                        "totală nu poate depăși **1/2**, indiferent de natura "
                        "creanțelor. Iar dacă venitul e sub salariul minim net, se "
                        "poate urmări doar partea care depășește **jumătate din "
                        "salariul minim net** — prag de protecție pe care notițele "
                        "nu-l aveau deloc. *(verificat 21.08.2026)*",
                 motiv="Verificat pe surse publice. Notițele aveau o singură limită din "
                       "trei, iar pragul de protecție sub salariul minim lipsea — "
                       "exact cazul în care reținerea greșită îl păgubește pe salariat."),

        ],
        anexe={"## 9. Checklist lunar rezultat din notițe": "B",
               "## 10. Lista erorilor corectate din notițe": "C"},
        genereaza=["D", "E", "G"],
        nota="Al cincilea document. Salariile sunt clasa 4, dar un document intitulat "
             "„Stocuri, TVA și corelații de balanță” nu le putea găzdui fără să mintă — "
             "iar materialul e coerent și mare cât să stea singur.",
    ),
    dict(
        # Al șaselea document, și al treilea construit integral din repartizare.
        # Precedentul e exact cel al salariilor din 21.08: clasa 5 e material coerent și
        # mare, iar niciunul din cele cinci documente existente nu-l putea găzdui fără
        # să mintă. Documentul de control avea deja plafoanele de numerar, dar plafonul
        # nu e trezorerie — e disciplină de numerar, ceea ce e altceva.
        nume="trezorerie",
        zi=None,   # sursa din 28.08 se împarte la trei documente
        cheie="doc:trezorerie",
        repartizat=True,
        sursa=None,
        iesire="dist/trezorerie.md",
        titlu="Trezorerie: bancă, casă, efecte de încasat și avansuri",
        subtitlu="Sursă: training 28.08.2026 — stările prin care trec banii între "
                 "„am dreptul la ei” și „sunt în cont”",
        legenda_veche=[],
        inlocuiri=[],
        anexe={},
        genereaza=["D", "E", "G"],
        nota="Clasa 5 avea, până la sursa asta, două fluxuri și două conturi de patru "
             "cifre în plan. Documentul e primul care o tratează ca teritoriu, nu ca "
             "anexă a altor subiecte.",
    ),
    dict(
        # Construit integral din secțiunile pe care `date/repartizare.py` i le dă.
        # Materialul lui nu e monografie: plafoane, reguli de document, practică de
        # control. De-asta n-avea unde să intre în celelalte trei — sistemul e făcut
        # pentru fluxuri, iar astea nu produc articole contabile.
        nume="control",
        zi=None,   # nu vine dintr-o zi proprie: e partea din 19.08 care n-adâncea nimic
        cheie="doc:control",
        repartizat=True,
        sursa="surse/training-5-2026-08-19/ghid-contabilitate.md",
        iesire="dist/control-documente-numerar.md",
        titlu="Control, documente și numerar",
        subtitlu="Surse: training 19.08.2026 · adâncit cu 21.08.2026, 26.08.2026 și "
                 "28.08.2026 — cum se citește un cont, ce cere legea de "
                 "la un document și unde se rupe disciplina de casă",
        legenda_veche=[],
        adaugiri=[
            dict(bloc="## 8. Răspunsuri la întrebările din notițe",
                 sectiune_noua="Cum se construiește o verificare"),
        ],
        anexe={"## 12. Erori frecvente și capcane": "B"},
        genereaza=["D", "E", "G"],
        inlocuiri=[
            dict(text="Vezi secțiunea 13 — punct de verificat în textul legal în vigoare.",
                 devine="❓ Punct de verificat în textul legal în vigoare — vezi Anexa D.",
                 motiv="Trimitere moartă: §13 al sursei nu a devenit secțiune aici, ci "
                       "întrebări în `date/intrebari.py`. Primește și ❓, pentru că exact "
                       "asta e: material provizoriu."),
            dict(text="în vigoare la data operațiunii — vezi secțiunea 13.",
                 devine="în vigoare la data operațiunii ❓ — vezi Anexa D.",
                 motiv="Aceeași trimitere moartă. Plafoanele sunt primul lucru pe care "
                       "cineva îl aplică la un client, deci marcajul trebuie să fie "
                       "acolo unde se citește, nu doar în anexă."),
            # Același defect ca în stocuri-tva, a treia oară: 5111 nu există, iar Cecuri
            # de încasat e 5112. Aici e într-o listă de confuzii de trezorerie, cu
            # simbolul netformatat, deci poarta 30 nu-l prinde — dar e la fel de greșit.
            dict(text="**Confuzia 5121 / 5311 / 5111.** 5121 = bancă, 5311 = casa în "
                      "lei, 5111 = *cecuri de încasat*.",
                 devine="**Confuzia 5121 / 5311 / 5112.** 5121 = bancă, 5311 = casa în "
                        "lei, 5112 = *cecuri de încasat*.",
                 motiv="5111 nu există în plan; contul de cecuri de încasat e 5112. "
                       "Prins de aceeași contraverificare ca defectele din poarta 30."),
        ],
        nota="Singurul document care nu vine dintr-o zi de training proprie: e partea "
             "din 19.08.2026 care nu adâncea niciun subiect existent.",
    ),
]
