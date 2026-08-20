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
        cheie="doc:capitaluri",
        sursa="surse/training-2-2026-08-07/notite-revizuit.md",
        iesire="dist/capitaluri-credite-provizioane.md",
        titlu="Capitaluri, credite, leasing și provizioane",
        subtitlu="Surse: training 07.08.2026 · adâncit cu 19.08.2026 — versiune revizuită",
        adaugiri=[
            # Închiderea lui 121 și impozitul pe profit sunt F-104: capitaluri, nu
            # stocuri. Sursa le ține sub §2, „mărfuri” — aici se rup de acolo.
            dict(bloc="## 2. Mărfuri la preț cu amănuntul (371)",
                 in_sectiune="## 2. Pierderea contabilă vs. pierderea fiscală"),
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
        genereaza=["E"],
        nota="Rolul Anexei C îl joacă secțiunea 0 (Sinteza corecțiilor), păstrată în "
             "față pentru că funcționează ca rezumat executiv al documentului.",
    ),
    dict(
        nume="imobilizari",
        cheie="doc:imobilizari",
        sursa="surse/training-3-2026-08-12/notite-revizuit.md",
        iesire="dist/imobilizari.md",
        titlu="Imobilizări",
        subtitlu="Surse: training 12.08.2026 · adâncit cu 19.08.2026 — "
                 "versiune revizuită, reorganizată și contraverificată",
        adaugiri=[
            dict(bloc="## 7. Operațiuni speciale",
                 in_sectiune="## 11. Ieșiri din gestiune"),
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
        genereaza=["E"],
        nota="Secțiunea 18 (anticiparea sesiunii pe ajustări) rămâne în corp, nu în "
             "anexe: e conținut de continuare, nu material de referință.",
    ),
    dict(
        nume="stocuri-tva",
        cheie="doc:stocuri-tva",
        sursa="surse/training-4-2026-08-14/notite-revizuit.md",
        iesire="dist/stocuri-tva-corelatii.md",
        titlu="Stocuri, TVA și corelații de balanță",
        subtitlu="Surse: training 14.08.2026 · adâncit cu 19.08.2026 — "
                 "stocuri (clasa 3), TVA și corelații de balanță, versiune revizuită",
        adaugiri=[
            dict(bloc="## 4. Mecanica TVA", in_sectiune="## 7. Conturile de TVA"),
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
        ],
        legenda_veche=[],          # are deja forma canonică
        anexe={},                  # anexele A–E sunt deja denumite corect
        genereaza=["F"],
        extinde_anexe={"C": CORECTII_SURSA_19_08},
        nota="Singurul care avea deja anexele denumite. Primește Anexa F, care exista "
             "doar ca notă în foaia Legendă a workbook-ului.",
    ),
    dict(
        # Construit integral din secțiunile pe care `date/repartizare.py` i le dă.
        # Materialul lui nu e monografie: plafoane, reguli de document, practică de
        # control. De-asta n-avea unde să intre în celelalte trei — sistemul e făcut
        # pentru fluxuri, iar astea nu produc articole contabile.
        nume="control",
        cheie="doc:control",
        repartizat=True,
        sursa="surse/training-5-2026-08-19/ghid-contabilitate.md",
        iesire="dist/control-documente-numerar.md",
        titlu="Control, documente și numerar",
        subtitlu="Sursă: training 19.08.2026 — cum se citește un cont, ce cere legea de "
                 "la un document și unde se rupe disciplina de casă",
        legenda_veche=[],
        anexe={"## 12. Erori frecvente și capcane": "B"},
        genereaza=["E"],
        nota="Singurul document care nu vine dintr-o zi de training proprie: e partea "
             "din 19.08.2026 care nu adâncea niciun subiect existent.",
    ),
]
