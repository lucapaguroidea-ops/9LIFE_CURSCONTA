"""Unde merge fiecare subsecțiune a unei surse care alimentează mai multe destinații.

Până acum fiecare document avea exact o sursă, iar poarta 12 verifica perechea. Sursa
din 19.08.2026 rupe tiparul: teritoriul ei se suprapune peste trei documente existente
și mai naște unul nou. Patru destinații, o singură sursă.

Riscul specific nu e „nimeni n-a luat secțiunea”, ci **„am crezut că a luat-o celălalt”**.
Fiecare document poate trece separat poarta 12 în timp ce material cade între ele. De
aceea împărțirea se DECLARĂ aici, înainte de a fi făcută, iar poarta 16 verifică două
lucruri diferite:

    16a  nicio subsecțiune a sursei nu rămâne fără destinație;
    16b  fiecare linie ajunge în destinația care i-a fost declarată — nu doar undeva.

16b e strict mai tare decât o verificare pe reuniunea destinațiilor: reuniunea spune că
textul există pe undeva, nu că a ajuns unde trebuia.

Granularitatea e subsecțiunea (`###`), nu secțiunea, pentru că sursa chiar se rupe pe
dinăuntru: §2 e despre mărfuri la preț cu amănuntul, dar §2.6–2.7 sunt închiderea
exercițiului și impozitul pe profit — capitaluri, nu stocuri.
"""

#: Sursa care se împarte. Fișierul din `surse/` nu se modifică niciodată.
SURSA = "surse/training-5-2026-08-19/ghid-contabilitate.md"

# ---------------------------------------------------------------------------
# Destinațiile
#
# O destinație nu e neapărat un document. Tabelul de conturi al sursei aparține
# planului, lista de întrebări deschise aparține listei de întrebări, iar disciplina
# de închidere aparține foii care o ține. Dacă destinațiile ar fi numai documente,
# materialul care nu e proză ar trebui împins într-un document ca să aibă unde sta —
# adică exact segmentarea pe care sistemul o refuză.
# ---------------------------------------------------------------------------

#: cheie → (ce artefact ține conținutul, cum se citește la verificare)
DESTINATII = {
    "doc:capitaluri":   ("dist/capitaluri-credite-provizioane.md", "fisier"),
    "doc:imobilizari":  ("dist/imobilizari.md", "fisier"),
    "doc:stocuri-tva":  ("dist/stocuri-tva-corelatii.md", "fisier"),
    "doc:control":      ("dist/control-documente-numerar.md", "fisier"),
    "date:plan":        ("Plan de conturi", "foaie"),
    "foaie:inchideri":  ("Închideri periodice", "foaie"),
    "date:intrebari":   ("dist/intrebari-formator.md", "fisier"),
}

# ---------------------------------------------------------------------------
# Harta
#
# `(titlul subsecțiunii, destinație, motivul)`. Motivul nu e ornament: la revizuire,
# singura întrebare care contează e „de ce acolo și nu dincolo”, iar răspunsul trebuie
# să fie lângă decizie, nu în capul cuiva.
# ---------------------------------------------------------------------------

REPARTIZARE = [
    ("(preambul)", "doc:control",
     "Titlul și convenția de notare `cont debitor = cont creditor · sumă`. Convenția "
     "intră în documentul nou, care e singurul construit de la zero din sursa asta."),

    ("## 1. Cum se citește un cont", "doc:control",
     "Debit/credit, activ/pasiv, conturile bifuncționale și semnalul de eroare la sold "
     "contrar naturii. E fundamentul detectării erorii, deci al controlului — nu ține "
     "de un subiect contabil anume."),

    # --- §2 mărfuri la preț cu amănuntul: se rupe la 2.6 -------------------
    ("## 2. Mărfuri la preț cu amănuntul (371)", "doc:stocuri-tva",
     "Intro propriu: metoda prețului cu amănuntul și cele două conturi rectificative "
     "ale lui 371. Adâncește F-316."),
    ("### 2.1 Achiziția", "doc:stocuri-tva",
     "Adâncește F-316: baza TVA neexigibile e cost + adaos, nu costul."),
    ("### 2.2 Vânzarea prin casierie", "doc:stocuri-tva", "Adâncește F-317."),
    ("### 2.3 Descărcarea de gestiune", "doc:stocuri-tva",
     "Adâncește F-317: articolul compus `% = 371` și verificarea că gestiunea se "
     "închide exact."),
    ("### 2.4 Închiderea TVA la sfârșitul lunii", "doc:stocuri-tva",
     "Adâncește F-405 pe cifrele exemplului de amănunt."),
    ("### 2.5 Plata TVA", "doc:stocuri-tva",
     "Adâncește F-405 și lămurește confuzia 5121/5311/5111."),
    ("### 2.6 Închiderea conturilor de cheltuieli și venituri", "doc:capitaluri",
     "Aici sursa se rupe: închiderea 121 e F-104, capitaluri — nu stocuri."),
    ("### 2.7 Impozitul pe profit", "doc:capitaluri",
     "Tot F-104: soldul creditor al lui 121 e BAZA, nu impozitul."),

    # --- §3 ajustări ------------------------------------------------------
    ("## 3. Ajustări pentru deprecierea stocurilor", "doc:stocuri-tva",
     "Intro propriu: deprecierea nu se estimează, se stabilește prin comisie și "
     "proces-verbal. Adâncește F-307."),
    ("### 3.1 Înregistrarea deprecierii", "doc:stocuri-tva",
     "Adâncește F-307. Aici stă și corecția 391 → 397."),
    ("### 3.2 Reluarea la venituri, la valorificarea bunului", "doc:stocuri-tva",
     "Adâncește F-307 cu pasul de reluare, care lipsea din monografie."),
    ("### 3.3 Regimul fiscal — atenție", "doc:stocuri-tva",
     "Nedeductibilitatea ajustării de stoc și neimpozabilitatea reluării — art. 26 și "
     "art. 23 lit. d. Ține de F-307."),
    ("### 3.4 Inventarierea — nota de practică", "doc:stocuri-tva",
     "Rămâne lângă ajustare, deși e practică: procesul-verbal al comisiei e documentul "
     "care justifică procentul din 3.1. Separată, nota și-ar pierde obiectul."),

    # --- §4 TVA -----------------------------------------------------------
    ("## 4. Mecanica TVA", "doc:stocuri-tva", "Titlul blocului de TVA."),
    ("### 4.1 Conturile", "doc:stocuri-tva", "Tabelul conturilor de TVA — F-401/405."),
    ("### 4.2 Taxarea inversă", "doc:stocuri-tva",
     "Adâncește F-402 cu nuanța avansului la achiziția intracomunitară de bunuri."),
    ("### 4.3 De ce are 4428 nevoie de analitice", "doc:stocuri-tva",
     "Justificarea analiticelor 4428 pe situație ȘI pe cotă — analitic Tier A, F-408 "
     "și F-316."),

    # --- §5 furnizori -----------------------------------------------------
    ("## 5. Furnizori — clasa 40", "doc:stocuri-tva", "Titlul blocului de furnizori."),
    ("### 5.1 Contul 408 — Furnizori, facturi nesosite", "doc:stocuri-tva",
     "Adâncește F-408: termenul de facturare până pe 15 și avizul fără preț."),
    ("### 5.2 Varianta completă, cu TVA", "doc:stocuri-tva",
     "Adâncește F-408 cu pasul `408 = 4428`, care închide ambele conturi."),
    ("### 5.3 De ce 408 este un cont periculos", "doc:stocuri-tva",
     "Dublarea gestiunii prin factura care nu menționează avizul — riscul lui F-408."),
    ("### 5.4 Contul 409 — Furnizori-debitori (avansuri plătite)", "doc:stocuri-tva",
     "Adâncește F-410 cu analiticele 4091–4094 pe destinație și legătura cu 404."),
    ("### 5.5 Regula generală pe clasa 40", "doc:stocuri-tva", "Închide blocul F-408/F-410."),

    # --- §6 clienți -------------------------------------------------------
    ("## 6. Clienți — clasa 41", "doc:stocuri-tva", "Titlul blocului de clienți."),
    ("### 6.1 Contul 411 și legătura cu veniturile", "doc:stocuri-tva",
     "Distincția 70x / 472 / 419 — adâncește F-410 și F-412."),
    ("### 6.2 Contul 418 — Clienți, facturi de întocmit", "doc:stocuri-tva",
     "Oglinda lui 408 — adâncește F-408."),
    ("### 6.3 Avans încasat de la client", "doc:stocuri-tva",
     "Adâncește F-410 cu stornarea avansului. Aici lipsea pasul de încasare."),

    # --- §7 operațiuni speciale: se rupe în trei --------------------------
    ("## 7. Operațiuni speciale", "doc:control",
     "Titlul blocului. Trei din patru subsecțiuni merg la control; titlul îl urmează "
     "pe majoritar."),
    ("### 7.1 Vânzarea unui mijloc fix", "doc:imobilizari",
     "Scoaterea din evidență — F-211/F-212. Imobilizări, nu stocuri."),
    ("### 7.2 Prețul din contract fără mențiune de TVA", "doc:control",
     "Tulică și Plavoșin (C-249/12). Nu e flux: e regulă de citire a contractului."),
    ("### 7.3 Încasare mai mare decât factura", "doc:control",
     "Material nou — devine flux propriu în clasa 4. Sold contrar naturii pe 4111."),
    ("### 7.4 Note despre 455", "doc:control",
     "Restricții de numerar pe 455 — rămas deschis, merge cu §8."),

    # --- §8–§9 disciplină și control -------------------------------------
    ("## 8. Numerar și plafoane (Legea 70/2015)", "doc:control",
     "Plafoane și interdicția fragmentării. Nu produce articole contabile."),
    ("## 9. Documente, contracte și riscuri la control", "doc:control",
     "Titlul blocului de documente și control."),
    ("### 9.1 „Prestări servicii conform contract\"", "doc:control",
     "Art. 319 Cod fiscal — descrierea naturii serviciului."),
    ("### 9.2 Contractul la prestările de servicii", "doc:control",
     "Art. 25 alin. 1 și abrogarea cerinței exprese de contract la management."),
    ("### 9.3 Cazul penalităților — de reținut", "doc:control",
     "Penalități contractuale nerealiste impuse ca venit la control."),
    ("### 9.4 Sistemele informatice", "doc:control",
     "Fișa de cont ca instrument de verificare — practică de control."),

    # --- §10 disciplina de închidere -------------------------------------
    ("## 10. Conturi de urmărit periodic", "foaie:inchideri",
     "Introducerea listei. Aserțiunile ei sunt stări terminale la scară de lună, deci "
     "aparțin foii care le ține, nu unui document."),
    ("### Lunar — obligatoriu", "foaie:inchideri", "Cadență lunară, coloana din foaie."),
    ("### Cel puțin trimestrial", "foaie:inchideri", "Cadență trimestrială."),

    # --- §11–§13 transversale --------------------------------------------
    ("## 11. Tabel recapitulativ de conturi", "date:plan",
     "Denumiri și naturi de conturi — aparțin planului de conturi, unde se contopesc "
     "cu rândurile existente. Într-un document ar fi al doilea plan, care diverge."),
    ("## 12. Erori frecvente și capcane", "doc:control",
     "Cele 13 capcane rămân împreună, ca Anexa B a documentului de control. Împărțite "
     "pe subiect ar produce exact cusătura pe care poarta 16 o previne, iar lista "
     "numerotată și-ar pierde sensul."),
    ("## 13. De verificat și de testat", "date:intrebari",
     "Cele cinci puncte deschise intră în lista de întrebări, cu aceleași câmpuri ca "
     "celelalte 21 — de unde ies singure în foaie, în .md și ca marcaje ❓ pe fluxuri."),
]

#: titlu → destinație
UNDE = {titlu: dest for titlu, dest, _ in REPARTIZARE}

#: titlu → motiv
DE_CE = {titlu: motiv for titlu, _, motiv in REPARTIZARE}


# ---------------------------------------------------------------------------
# Titlurile absorbite
#
# Contopirea „în secțiunea care tratează același subiect” înseamnă că titlul blocului
# dispare: conținutul lui §4 „Mecanica TVA” trăiește sub §7 „Conturile de TVA”, iar
# două titluri pe același subiect ar fi doar zgomot.
#
# Dispariția e o DECIZIE, nu o pierdere — deci se declară, cu gazda ei. Fără lista
# asta, poarta 16 ar cere ca fiecare titlu-sursă să apară undeva, iar singurul mod de
# a o mulțumi ar fi lipirea blocurilor la coadă: exact cusătura pe tranșe pe care
# retitrarea pe subiect a eliminat-o.
# ---------------------------------------------------------------------------

ABSORBITE = {
    "# Ghid de contabilitate — mărfuri, TVA neexigibilă și clasa 4":
        "Titlul sursei. Documentele poartă acum titluri pe subiect, iar materialul "
        "sursei s-a împărțit la patru: un singur titlu nu-l mai poate acoperi.",
    "## 2. Mărfuri la preț cu amănuntul (371)":
        "Absorbit în „## 8. Mărfuri (371)” din documentul de stocuri.",
    "## 3. Ajustări pentru deprecierea stocurilor":
        "Absorbit tot în „## 8. Mărfuri (371)”: ajustarea se face pe gestiunea de "
        "mărfuri, deci stă lângă ea.",
    "## 4. Mecanica TVA":
        "Absorbit în „## 7. Conturile de TVA”.",
    "## 5. Furnizori — clasa 40":
        "Absorbit în secțiunea nouă „Furnizori și clienți — clasele 40 și 41”.",
    "## 6. Clienți — clasa 41":
        "Absorbit în aceeași secțiune nouă, împreună cu furnizorii: 408 și 418 sunt "
        "oglinzi, iar separate ar cere cititorului să sară între secțiuni.",
    "## 12. Erori frecvente și capcane":
        "Devine „Anexa B — Checklist practic” în documentul de control: aceeași listă, "
        "denumirea canonică a anexelor.",
    # §13 nu se copiază: se RESTRUCTUREAZĂ în formatul de întrebare, cu aceleași
    # câmpuri ca celelalte 21 (`sursa`, `context`, `conteaza`, `presupunere`). Fiecare
    # punct își păstrează trasabilitatea prin câmpul `sursa`. Copiat verbatim, ar fi
    # rămas o listă paralelă care spune același lucru cu alte cuvinte.
    "## 13. De verificat și de testat":
        "Devine tema „Plafoane de numerar și contul 455” și următoarele două din "
        "date/intrebari.py.",
    "Puncte rămase deschise, de confirmat înainte de a le aplica la un client:":
        "Introducerea listei; rolul ei îl joacă nota din capul foii „Întrebări deschise”.",
    "1. **Plafoanele de numerar** — valorile exacte din Legea 70/2015, așa cum a fost "
    "modificată prin Legea 296/2023, la data operațiunii.":
        "Devine întrebarea „training 19.08.2026, punctul 1”.",
    "2. **Restricțiile pe contul 455** — care sunt exact operațiunile în numerar "
    "interzise și temeiul legal.":
        "Devine întrebarea „training 19.08.2026, punctul 2”.",
    "3. **Simulare în softul de contabilitate** pentru cazul încasării în plus (7.3): "
    "de verificat dacă programul extrage automat TVA-ul pe diferența trecută la 419, "
    "sau dacă trebuie forțat manual. De contraverificat 4427 după simulare.":
        "Devine întrebarea „training 19.08.2026, punctul 3”.",
    "4. **Analiticele pe 4428** — de configurat pe fiecare situație (aviz intrare / "
    "aviz ieșire / mărfuri) **și** pe fiecare cotă de TVA, înainte de a începe operarea.":
        "Devine întrebarea „training 19.08.2026, punctul 4”.",
    "5. **Contul folosit pentru facturi nesosite la imobilizări** — 408 cu analitic sau "
    "404 cu analitic; de stabilit convenția și de respectat consecvent.":
        "Devine întrebarea „training 19.08.2026, punctul 5”.",

    "## 7. Operațiuni speciale":
        "Blocul s-a rupt în trei destinații, deci titlul lui n-are ce acoperi: §7.1 e "
        "la imobilizări, restul la control.",
}
