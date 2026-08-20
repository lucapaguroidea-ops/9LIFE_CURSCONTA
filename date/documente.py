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

DOCUMENTE = [
    dict(
        nume="training-2",
        sursa="surse/training-2-2026-08-07/notite-revizuit.md",
        iesire="dist/notite-training-2-2026-08-07.md",
        titlu="Notițe training — 07.08.2026",
        subtitlu="Capitaluri, credite, leasing, provizioane — versiune revizuită",
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
        nume="training-3",
        sursa="surse/training-3-2026-08-12/notite-revizuit.md",
        iesire="dist/notite-training-3-2026-08-12.md",
        titlu="Imobilizări — notițe training 12.08.2026",
        subtitlu="Versiune revizuită, reorganizată și contraverificată",
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
        nume="training-4",
        sursa="surse/training-4-2026-08-14/notite-revizuit.md",
        iesire="dist/notite-training-4-2026-08-14.md",
        titlu="Notițe training — 14.08.2026",
        subtitlu="Stocuri (clasa 3), TVA și corelații de balanță — versiune revizuită",
        legenda_veche=[],          # are deja forma canonică
        anexe={},                  # anexele A–E sunt deja denumite corect
        genereaza=["F"],
        nota="Singurul dintre cele trei care avea deja anexele denumite. Primește "
             "Anexa F, care exista doar ca notă în foaia Legendă a workbook-ului.",
    ),
]
