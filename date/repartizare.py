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

# Fișierele din `surse/` nu se modifică niciodată. Structura pe surse e mai jos, în
# `SURSE`: fiecare cu harta ei, pentru că două surse pot avea secțiuni cu același titlu
# („## 1. …”), iar o hartă comună le-ar confunda între ele.

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
    "doc:salarii":      ("dist/salarii-contributii-retineri.md", "fisier"),
    "date:plan":        ("Plan de conturi", "foaie"),
    "foaie:inchideri":  ("Închideri periodice", "foaie"),
    "doc:trezorerie":   ("dist/trezorerie.md", "fisier"),
    "date:intrebari":   ("dist/intrebari-formator.md", "fisier"),
}

# ---------------------------------------------------------------------------
# Harta
#
# `(titlul subsecțiunii, destinație, motivul)`. Motivul nu e ornament: la revizuire,
# singura întrebare care contează e „de ce acolo și nu dincolo”, iar răspunsul trebuie
# să fie lângă decizie, nu în capul cuiva.
# ---------------------------------------------------------------------------

REPARTIZARE_19_08 = [
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

ABSORBITE_19_08 = {
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


# ===========================================================================
# Sursa din 21.08.2026 — salarii, impozit pe venit, D300
#
# A doua sursă care se împarte, și prima care sosește BRUTĂ. Faza A a produs
# `notite-revizuit.md` alături de `.txt`-ul neatins; repartizarea lucrează pe cea
# revizuită, ca la trainingurile 2, 3 și 4.
#
# Se împarte la patru destinații, dintre care una nouă: salariile sunt clasa 4, dar un
# document intitulat „Stocuri, TVA și corelații de balanță” nu le poate găzdui fără să
# mintă. Materialul e coerent și mare cât să stea singur.
# ===========================================================================

REPARTIZARE_21_08 = [
    ("## 1. Înainte de înregistrare: de unde vine statul de plată", "doc:salarii",
     "Interfața cu HR — de unde vine documentul pe care contabilitatea îl ia de bun."),
    ("### 1.1 Salariul minim și norma parțială", "doc:salarii",
     "Minimul proporțional cu norma: verificarea care se uită cel mai des în practică."),
    ("### 1.2 REGES, D112 și pontajul", "doc:salarii",
     "Cele trei surse care trebuie să spună același lucru."),
    ("### 1.3 Fișa de plătitor din SPV", "doc:salarii",
     "Lanțul stat → D112 → fișă de plătitor → balanță, și nota rectificativă."),

    ("## 2. Monografia salariilor", "doc:salarii",
     "Adâncește F-413: brutul realizat, reținerile, CAM, restul de plată."),
    ("### 2.1 Salariul brut și reținerile", "doc:salarii",
     "Corectează acronimele CAS/CASS inversate în notiță."),
    ("### 2.2 Singura contribuție a angajatorului", "doc:salarii",
     "Corectează sensul CAM: notița scria `436 - 646`, adică invers."),
    ("### 2.3 Restul de plată", "doc:salarii",
     "Închiderea obligațiilor, ca articol compus."),
    ("### 2.4 Tichetele de masă", "doc:salarii",
     "Corectează contul: 642, nu 423."),

    ("## 3. Concediile medicale", "doc:salarii",
     "Flux nou: împărțirea indemnizației între angajator (6458) și FNUASS (4382)."),

    ("## 4. Rețineri, avansuri și datorii reciproce", "doc:salarii",
     "Grupa 42x în afara salariului propriu-zis."),
    ("### 4.1 Popriri — contul 427", "doc:salarii",
     "Flux nou, cu cel mai mare risc penal din grupă."),
    ("### 4.2 Drepturi de personal neridicate — contul 426", "doc:salarii",
     "Flux nou: datoria nu dispare, își schimbă natura."),
    ("### 4.3 Creanțe față de personal la plecare — contul 4282", "doc:salarii",
     "Flux nou. Corectează 4428 → 4282: notița folosea contul de TVA neexigibilă."),
    ("### 4.4 Avansul", "doc:salarii",
     "425 și închiderea lui la statul de lichidare."),

    ("## 5. Corelațiile de balanță pe salarii", "doc:salarii",
     "Miezul practic: verificarea în secunda doi, pentru că statul există deja."),
    ("### 5.1 Regula generală: rulaj creditor = sold creditor", "doc:salarii",
     "Regula se demonstrează pe conturile de salarii, deci stă lângă ele. "
     "Generalizarea trăiește în foaia „Închideri periodice” și în corelații."),
    ("### 5.2 Corelația cu statul de plată", "doc:salarii",
     "421 + 423 = restul de plată. Corelația cea mai ieftină din contabilitate."),
    ("### 5.3 Verificarea CAM pe cifre", "doc:salarii",
     "2,25% × brut = rulaj creditor 436."),
    ("### 5.4 Solduri cu semn contrar naturii contului", "doc:salarii",
     "Aplicarea lui C-23 pe grupa 42x, cu 4282 ca exemplu."),

    ("## 6. Impozit pe profit sau impozit pe venit", "doc:capitaluri",
     "Impozitarea rezultatului adâncește F-104, închiderea exercițiului — capitaluri, "
     "nu salarii, chiar dacă a fost predat în aceeași zi."),
    ("### 6.1 Impozitul pe profit", "doc:capitaluri", "Cota de 16% și `691 = 441`."),
    ("### 6.2 Condițiile pentru microîntreprindere", "doc:capitaluri",
     "Flux nou. Corectează 6918 → 698: contul din notiță nu există."),
    ("### 6.3 Depășirea pragului", "doc:capitaluri",
     "Trecerea la 16% din trimestrul depășirii, nu din următorul."),
    ("### 6.4 Ce sold trebuie să aibă", "doc:capitaluri",
     "441 și 4418 sunt pasive: soldul normal e creditor."),

    ("## 7. Decontul de TVA și D300", "doc:stocuri-tva",
     "Adâncește F-405 și F-407 — teritoriul TVA al documentului de stocuri."),
    ("### 7.1 Decontul nu are variantă rectificativă", "doc:stocuri-tva",
     "Consecința: corecțiile merg pe regularizări."),
    ("### 7.2 Regularizări — cazul cotei schimbate", "doc:stocuri-tva",
     "Avans la 19%, factură la 21% — tranziția de cotă."),
    ("### 7.3 Deciziile de impunere ANAF", "doc:stocuri-tva",
     "Analitic distinct pe 4423, ca să nu ajungă în decont."),
    ("### 7.4 Corelația cu fișa de rol", "doc:stocuri-tva",
     "Rulajul lunii, nu soldul. Contradicția din notiță pe numerele de rând."),
    ("### 7.5 Corelația sfântă a TVA-ului", "doc:stocuri-tva",
     "Soldul din decont = soldul din balanță."),

    ("## 8. Răspunsuri la întrebările din notițe", "doc:salarii",
     "Întrebările marcate în notițe, care se răspund din logica înregistrării."),
    ("### 8.1 Cum se leagă rulajul debit/credit cu soldul, la 421 și 423", "doc:salarii",
     "Răspuns conceptual, pe conturile de salarii."),
    ("### 8.2 De ce creanța față de un fost salariat e cont de activ", "doc:salarii",
     "Răspuns conceptual + corecția 4428 → 4282."),
    ("### 8.3 De ce nu trebuie solduri creditoare pe conturi de activ", "doc:salarii",
     "Răspuns conceptual, legat de C-23."),
    ("### 8.4 Ce alte corelații se pot face din balanță", "doc:control",
     "Tiparul „ce document extern conține aceeași informație” e transversal: e despre "
     "cum se construiește o verificare, nu despre salarii."),

    ("## 9. Checklist lunar rezultat din notițe", "doc:salarii", "Devine Anexa B."),
    ("## 10. Lista erorilor corectate din notițe", "doc:salarii", "Devine Anexa C."),
]

ABSORBITE_21_08 = {
    "*Versiune revizuită. Sursa: notițele brute din 21.08.2026.*":
        "Rândul de versiune al sursei. Fiecare document primește propriul subtitlu din "
        "`date/documente.py`, cu ziua-sursă în el.",
    "## 7. Decontul de TVA și D300":
        "Absorbit în „## 7. Conturile de TVA” din documentul de stocuri: decontul e "
        "capătul mecanicii TVA, nu un subiect paralel.",
    "# Salarii, contribuții și rețineri — notițe training 21.08.2026":
        "Titlul sursei. Documentul de salarii îl primește din `date/documente.py`, "
        "iar restul materialului pleacă la alte trei documente cu titlurile lor.",
}


# ===========================================================================
# Sursa din 26.08.2026 — subvenții europene, dividende, conturile-coș
#
# A treia sursă care se împarte, și cea care se împarte cel mai curat: trei teme mari,
# trei destinații, fără nicio secțiune care să se rupă pe dinăuntru. Motivul e că
# trainingul a fost ținut pe teme, nu pe conturi.
#
# Gruparea din §4 nu e a mea, e a sursei, și merită spus de ce ține: 446, 4481, 4482 și
# 461 sunt patru răspunsuri la aceeași întrebare — **cum ții rulajele curente curate**.
# Documentul de control e exact despre cum vezi că un cont arată greșit, deci le
# primește împreună. Împărțite pe conturi (446 la TVA, 4481 la control, 461 la terți),
# fiecare ar fi rămas o regulă izolată, iar întrebarea comună ar fi dispărut.
# ===========================================================================

REPARTIZARE_26_08 = [
    # --- §1 subvenții: în întregime la imobilizări -------------------------
    ("## 1. Subvenții pentru investiții și fonduri europene", "doc:imobilizari",
     "Subvenția pentru investiții trăiește pe durata de amortizare a activului "
     "finanțat: fără imobilizare n-are ce relua la venit. Adâncește F-58."),
    ("### 1.1 Corespondența 445 ↔ 475", "doc:imobilizari",
     "Tabelul perechilor creanță ↔ venit amânat. Conturile intră și în plan, prin "
     "faza 1; aici stă raționamentul care le leagă două câte două."),
    ("### 1.2 Când se înregistrează un proiect european", "doc:imobilizari",
     "Momentul nașterii creanței — la aprobare, nu la încasare. E o stare inițială de "
     "flux, deci stă lângă monografia lui."),
    ("### 1.3 Aportul propriu și TVA-ul nedecontat", "doc:imobilizari",
     "Cota de finanțare și excluderea TVA din proiect: exemplul numeric pe care se "
     "sprijină tot mecanismul de reluare."),
    ("### 1.4 Amortizarea și reluarea la venit merg împreună", "doc:imobilizari",
     "Pasul revelator al lui F-215. Aici stă și corecția 166,40 → 166,67, verificată "
     "de poarta 18 pe aritmetica afirmată."),
    ("### 1.5 Plusuri la inventar la imobilizări", "doc:imobilizari",
     "Plusul la imobilizări urmează același ritm ca subvenția — 4458 → 4754, apoi la "
     "venit pe măsura amortizării. F-216."),

    # --- §2 dividende: capitaluri -----------------------------------------
    ("## 2. Dividende", "doc:capitaluri",
     "Repartizarea rezultatului e capătul lui F-104: ce se întâmplă cu profitul după "
     "ce 121 s-a închis."),
    ("### 2.1 Analiticele pe 1012 — cotele de participare", "doc:capitaluri",
     "Analiticele pe asociat sunt condiția prealabilă a oricărei repartizări. F-114 le "
     "face procedură de control."),
    ("### 2.2 Hotărârea AGA e documentul de bază", "doc:capitaluri",
     "Documentul justificativ al repartizării. Stă lângă dividende, nu la documente în "
     "general: fără AGA nu există înregistrarea, nu doar dosarul."),
    ("### 2.3 Dividende certe din rezultatul reportat", "doc:capitaluri",
     "F-109: 1171 → 457 pe analitic, plus distincția 456 / 457."),
    ("### 2.4 Impozitul pe dividende", "doc:capitaluri",
     "Cota de 16 % și rețineriea prin 446 — al doilea bloc din MOD_DIVIDENDE."),
    ("### 2.5 Declarațiile: D100, D205, Declarația Unică", "doc:capitaluri",
     "Declarațiile care ies din aceleași cifre. Termenul de 25.01 și corelația D205 ↔ "
     "D100 ↔ fișa lui 446 aparțin temei, nu unui capitol de declarații."),
    ("### 2.6 Dividende interimare — contul 463", "doc:capitaluri",
     "F-110: plafonul soldului lui 121 și calendarul iulie/iunie."),
    ("### 2.7 Regularizarea la 31.12 și rectificativa D710", "doc:capitaluri",
     "Închiderea lui 463 și stornarea. Aici stă corecția 453 → 463."),

    # --- §3 creditare: capitaluri -----------------------------------------
    ("## 3. Creditarea de societate și relațiile cu asociații", "doc:capitaluri",
     "Creditarea e sursă de finanțare de la asociat — vecina capitalului social, nu a "
     "datoriilor comerciale."),
    ("### 3.1 Contul 455 — reguli de fier", "doc:capitaluri",
     "F-111. Regula „455 niciodată debitor” devine și corelație de balanță, dar "
     "monografia și contractul stau aici."),
    ("### 3.2 Majorarea capitalului social din creditare", "doc:capitaluri",
     "F-112: 4551 → 456 → 1011, iar 1011 → 1012 abia la ONRC."),
    ("### 3.3 Remiterea de datorie", "doc:capitaluri",
     "F-113: creditarea la care se renunță devine venit, deci profit fără exploatare."),
    ("### 3.4 Decontări între entități afiliate — 451", "doc:capitaluri",
     "Pragul de 25 % și oglinda dintre cele două societăți. Ține de relația cu "
     "acționariatul, ca 455."),
    ("### 3.5 Operațiuni în participație — 458", "doc:capitaluri",
     "F-426: transferul de venituri și cheltuieli, ca fiecare să plătească impozit pe "
     "activitatea proprie. Impozitarea rezultatului e teritoriul capitalurilor."),

    # --- §4–§5 conturile-coș și verificarea: control ----------------------
    ("## 4. Conturile care țin rulajele curate", "doc:control",
     "Titlul grupării. 446, 4481, 4482 și 461 sunt răspunsuri la aceeași întrebare — "
     "cum ții rulajele curente curate — iar documentul de control e cel despre cum "
     "vezi că un cont arată greșit."),
    ("### 4.1 Taxele locale prin 446, nu direct pe cheltuială", "doc:control",
     "F-423: taxa nu intră direct pe cheltuială. 471 la perioade lungi, direct la sume "
     "mici — pragul e o decizie de disciplină, nu de fiscalitate."),
    ("### 4.2 Contul 4481 — datorii din acte de control", "doc:control",
     "Revizuiește F-421, nu naște flux nou: aceeași decizie de impunere, aceeași stare "
     "terminală, alt cont. Plus contradicția declarată cu notițele din 21.08. "
     "Contradicția stă în document, nu doar în listă: cititorul trebuie s-o vadă unde "
     "ar aplica regula."),
    ("### 4.3 Contul 4482 — plăți eronate către buget", "doc:control",
     "F-424: soldul în așteptare păstrează corelațiile nealterate până la lămurire."),
    ("### 4.4 Conturile 461 / 462 — coșul firmei", "doc:control",
     "F-425: vânzarea de mijloc fix și imputația. Aici stă corecția 121 → 461."),
    ("## 5. Verificarea care încheie ședința", "doc:control",
     "Soldul contrar naturii contului, aplicat pe conturile ședinței. E C-23 văzut din "
     "partea cealaltă — de la cont către eroare."),
]

ABSORBITE_26_08 = {
    "# Subvenții, dividende și conturile care devin coșuri — notițe training 26.08.2026":
        "Titlul sursei. Materialul se împarte la trei documente cu titluri pe subiect; "
        "un singur titlu nu-l mai poate acoperi.",
    "*Versiune revizuită. Sursa: notițele brute din 26.08.2026.*":
        "Rândul de versiune al sursei. Fiecare document își primește subtitlul din "
        "`date/documente.py`, cu zilele-sursă din care e făcut.",
}

# ===========================================================================
# Sursa din 28.08.2026 — trezoreria și verificarea balanței
#
# A patra sursă care se împarte, și a doua care naște un document nou. Motivul e
# același ca la salarii, în 21.08: materialul e clasa 5, coerent și mare, iar niciunul
# din cele cinci documente existente nu-l putea găzdui fără să mintă.
#
# Împărțirea are un caz de rupere pe dinăuntru, ca §2 din 19.08: §5 e despre casă, dar
# §5.1–5.3 sunt plafoane și reguli de numerar, care stau deja în documentul de control.
# Doar §5.4 (tichetele) merge la trezorerie. Granularitatea pe subsecțiune există exact
# pentru cazul ăsta.
# ===========================================================================

REPARTIZARE_28_08 = [
    # --- §0 inventarul: la parcurs, nu într-un document -------------------
    # Tabelul „ce e deja în sistem” nu e conținut contabil, e METODĂ: rezultatul
    # primului pas al fazei A. Locul lui e documentul de parcurs, lângă întrebarea
    # care îl cere — nu într-un document de subiect, unde ar fi o listă de referințe
    # care se învechește la fiecare training.
    ("## 0. Ce e deja în sistem", "doc:control",
     "Rezultatul pasului 0 din faza A. Merge la control pentru că e o procedură de "
     "verificare — de data asta a materialului contra sistemului, nu a balanței contra "
     "documentelor. Rândul despre codul D394 e cel care justifică pasul: mecanismul "
     "fusese scris ca material nou deși era pasul revelator al lui F-203."),

    # --- §1 taxarea inversă: la TVA, unde stă deja mecanica ---------------
    ("## 1. Recapitulare: taxarea inversă", "doc:stocuri-tva",
     "Recapitulare peste F-402 și MOD_TAXARE_INVERSA. Teritoriul TVA e al "
     "documentului de stocuri, indiferent că materialul a venit într-o zi de "
     "trezorerie."),
    ("### 1.1 Ce operațiuni intră", "doc:stocuri-tva",
     "Lista art. 331, cu nuanța semințelor și cea a construcțiilor: criteriul nu e "
     "vechimea, e regimul livrării."),
    ("### 1.2 Codurile din nomenclatorul D394", "doc:stocuri-tva",
     "Material NOU: fără codul de operațiune, D394 nu se validează. E un refuz la "
     "depunere, nu o eroare care se vede la control peste doi ani."),
    ("### 1.3 Ce se înregistrează și ce nu", "doc:stocuri-tva",
     "Nuanța care lipsea din MOD_TAXARE_INVERSA: la LIVRARE nu se face notă contabilă, "
     "doar mențiune în jurnal și cod. Cine caută nota n-o găsește pentru că nu există."),
    ("### 1.4 Rubricile separate din jurnale", "doc:stocuri-tva",
     "Fiecare rubrică alimentează alt rând din D300 și altă declarație."),

    # --- §2–§4 trezoreria: documentul nou ---------------------------------
    ("## 2. Investiții pe termen scurt: acțiuni și obligațiuni", "doc:trezorerie",
     "Clasa 50. Deschide documentul nou cu partea cea mai puțin operațională, dar care "
     "explică restul: ce fel de bani sunt ăștia."),
    ("### 2.1 Achiziția de acțiuni", "doc:trezorerie",
     "501 și analiticul pe emitent, condiție pentru ajustările de valoare."),
    ("### 2.2 Acțiuni vs. obligațiuni — ce cumperi de fapt", "doc:trezorerie",
     "Rezolvă instrucțiunea `{AI: de detaliat}` din notițe: proprietate vs. împrumut, "
     "cu consecințele pe risc, pe venit și pe rangul la lichidare."),

    ("## 3. Efecte de încasat: CEC-uri și bilete la ordin", "doc:trezorerie",
     "F-503 și F-504. Miezul documentului: banii au mai multe stări între „am dreptul "
     "la ei” și „sunt în cont”."),
    ("### 3.1 De la factură la încasare", "doc:trezorerie",
     "F-503: creanța se stinge înaintea încasării, iar riscul se mută pe 511x."),
    ("### 3.2 Scontarea biletului la ordin", "doc:trezorerie",
     "F-504. Aici stau corecțiile 6067 → 667 și baza de 12.100."),
    ("### 3.3 Când merită scontarea și când nu", "doc:trezorerie",
     "Contabilitatea de angajamente ca motiv economic: faci factura, n-o încasezi, și "
     "statul cere banii oricum."),

    ("## 4. Conturile la bănci", "doc:trezorerie",
     "512x, 518x, 5191 — partea cea mai operațională a clasei 5."),
    ("### 4.1 Conturile în valută și reevaluarea lunară", "doc:trezorerie",
     "Cele patru cazuri de diferență de curs, cu regula unică din care ies toate; aici "
     "stă corecția sensurilor inversate la creanțe."),
    ("### 4.2 Diferențele de curs: 665/765 sau 668/768?", "doc:trezorerie",
     "Divergența declarată cu formatorul. Stă în document, nu doar în lista de "
     "întrebări: cititorul trebuie s-o vadă unde ar aplica regula."),
    ("### 4.3 Dobânzi de plătit și de încasat", "doc:trezorerie",
     "F-505 și F-506: 471 înseamnă „știu suma ȘI perioada”, deci dobânda variabilă "
     "n-are ce căuta acolo."),
    ("### 4.4 Linii de credit (5191) vs. credite cu scadențar (1621)", "doc:trezorerie",
     "F-507 și C-35: la linie nu există scadențar, deci soldul de la bancă e singura "
     "verificare independentă."),

    # --- §5 numerarul, §6 valorile de trezorerie --------------------------
    # Prima variantă a documentului revizuit le ținea împreună, sub „Casa și alte
    # valori”, iar repartizarea le rupea la subsecțiune. Ieșea corect ca CONȚINUT și
    # strâmb ca TITLU: documentul de trezorerie primea o secțiune care anunța „Casa” și
    # livra numai tichete. Sursa chiar acoperă două subiecte — disciplina numerarului
    # și valorile ținute în trezorerie — deci s-au despărțit acolo, nu aici.
    ("## 5. Casa și plafoanele de numerar", "doc:control",
     "Plafoane și reguli de plată în numerar — adâncesc secțiunea care le are deja."),
    ("### 5.1 Plafonul soldului de casă", "doc:control",
     "Adâncește §3 „Numerar și plafoane” cu plafonul de SOLD, care lipsea de acolo: "
     "documentul avea plafoanele de tranzacție, nu pe cel de sold."),
    ("### 5.2 Ce plăți sunt plafonate și ce plăți nu", "doc:control",
     "Completează aceeași secțiune cu excepțiile — salarii și buget, fără plafon."),
    ("### 5.3 Plăți fragmentate și contractul cu plata în rate", "doc:control",
     "Calea legitimă în afara fragmentării, cu condiția respectării scadențarului."),
    ("## 6. Tichete de masă și alte valori", "doc:trezorerie",
     "Tichetele sunt STOC DE TREZORERIE (5328), nu o regulă de numerar: stau alături "
     "de bancă și casă, nu de plafoane. F-508."),

    # --- §6–§7 trezoreria, continuare -------------------------------------
    ("## 7. Avansuri de trezorerie (542)", "doc:trezorerie",
     "Adâncește F-502 cu monografia completă a decontului."),
    ("### 7.1 Monografia decontului", "doc:trezorerie",
     "Cele două părți cu TVA, pe cote diferite (21% și 11%), fiecare prin furnizor."),
    ("### 7.2 Diurna — partea care lipsea", "doc:trezorerie",
     "Completarea care închide decontul la exact 5.000: diurna n-are furnizor și "
     "n-are TVA, deci rupe tiparul primelor două părți."),
    ("### 7.3 De ce analiticul e obligatoriu aici", "doc:trezorerie",
     "Soldul merge în ambele sensuri pe persoane diferite; pe sintetic se anulează."),

    ("## 8. Viramente interne (581)", "doc:trezorerie",
     "Adâncește F-501, care azi nu spune nimic despre valută."),
    ("### 8.1 Când 581 are voie să aibă sold", "doc:trezorerie",
     "Excepția legitimă: transferul la cumpăna lunii. C-36."),
    ("### 8.2 Diferența de curs la transferul valută → lei", "doc:trezorerie",
     "Regula pe care notițele o subliniază cu șase semne de exclamare. E regulă de "
     "control, nu pas de monografie — de aceea trăiește în C-36 și aici, nu în F-501, "
     "a cărui monografie vine din workbook-ul-sămânță."),

    # --- §8 gestiunile: la stocuri ----------------------------------------
    ("## 9. Cheltuielile de clasa 6 și gestiunile de clasa 3", "doc:stocuri-tva",
     "Teritoriul stocurilor. Rezolvă instrucțiunea `{AI: de contraverificat și "
     "completat}` din notițe."),
    ("### 9.1 Tabelul corespondențelor", "doc:stocuri-tva",
     "Tabelul complet cheltuială ↔ gestiune. Aici stă corecția 608 ↔ 381."),
    ("### 9.2 Regula: consumul trece prin gestiune", "doc:stocuri-tva",
     "F-321. Un bun trecut direct pe cheltuială n-a intrat niciodată în evidență, deci "
     "nu poate fi scos din ea."),
    ("### 9.3 Excepțiile", "doc:stocuri-tva",
     "Bonul de benzină, nestocatele, anvelopele, devizul de reparație. Criteriul e "
     "destinația bunului, nu obiectul lui."),
    ("### 9.4 Transferul între gestiuni: marfa devenită materie primă", "doc:stocuri-tva",
     "F-321 pasul revelator: 301 = 371 înaintea consumului, niciodată 601 la 371."),
    ("### 9.5 Bonul de consum", "doc:stocuri-tva",
     "Ordinea gestiune → consum, cu forma documentului lăsată ❓."),

    # --- §9–§10 verificarea: la control -----------------------------------
    ("## 10. Verificarea analitic ↔ sintetic", "doc:control",
     "Miezul celei de-a doua jumătăți a trainingului. Documentul de control e exact "
     "despre cum se vede că un cont arată greșit."),
    ("### 10.1 De ce se rupe", "doc:control",
     "Operațiunea făcută după închiderea de lună, fără refacerea ei — cauza cea mai "
     "frecventă, și nu se anunță singură."),
    ("### 10.2 Conturile la care se rupe cel mai des", "doc:control",
     "Banca, clienții, furnizorii. Plus regula „niciodată fără analitic”, cu 446.1 ca "
     "exemplu de analitic făcut din prima."),
    ("### 10.3 Sumele nealocate și contul 473", "doc:control",
     "Adâncește F-411: important nu e contul, e să fie unul de care să-ți amintești."),
    ("### 10.4 Compensările 4091 ↔ 419", "doc:control",
     "Rezolvă instrucțiunea `{AI: de analizat}`: se poate, dar cu acord scris, iar "
     "TVA-ul nu se compensează odată cu avansurile."),
    ("### 10.5 Preluarea unei balanțe în cursul anului", "doc:control",
     "C-39, plus distincția sold / rulaj / total sume — răspunsul la a doua întrebare "
     "pusă pentru sesiunea următoare."),
    ("### 10.6 Cele trei verificări din softul formatorului", "doc:control",
     "Modelul pe care îl execută MOD_CONTROL_BALANTA. Aici se spune și care dintre ele "
     "era deja implementată."),

    ("## 11. Ce s-a cerut pentru sesiunile următoare", "doc:control",
     "Cererea de aplicație și întrebările rămase. Stă la control pentru că despre "
     "verificări e vorba, iar MOD_CONTROL_BALANTA e răspunsul la ea."),
]

ABSORBITE_28_08 = {
    "# Trezorerie, efecte de încasat și verificarea balanței — notițe training 28.08.2026":
        "Titlul sursei. Materialul se împarte la trei documente cu titluri pe subiect.",
    "*Versiune revizuită. Sursa: notițele brute din 28.08.2026.*":
        "Rândul de versiune al sursei. Fiecare document își primește subtitlul din "
        "`date/documente.py`, cu zilele-sursă din care e făcut.",
    "## 1. Recapitulare: taxarea inversă":
        "Absorbit în „## 5. Taxarea inversă pe teritoriul României” din documentul de "
        "stocuri. Două titluri pe același subiect ar fi doar zgomot — conținutul "
        "adâncește secțiunea, nu concurează cu ea.",

}

# ===========================================================================
# Vederile derivate
# ===========================================================================

#: Fiecare sursă cu harta ei. Hărțile NU se contopesc înainte de verificare: două surse
#: pot avea secțiuni cu același titlu („## 1. …”), iar o hartă comună le-ar confunda.
SURSE = [
    dict(cheie="19.08.2026",
         cale="surse/training-5-2026-08-19/ghid-contabilitate.md",
         repartizare=REPARTIZARE_19_08,
         absorbite=ABSORBITE_19_08),
    dict(cheie="21.08.2026",
         cale="surse/training-6-2026-08-21/notite-revizuit.md",
         repartizare=REPARTIZARE_21_08,
         absorbite=ABSORBITE_21_08),
    dict(cheie="26.08.2026",
         cale="surse/training-7-2026-08-26/notite-revizuit.md",
         repartizare=REPARTIZARE_26_08,
         absorbite=ABSORBITE_26_08),
    dict(cheie="28.08.2026",
         cale="surse/training-8-2026-08-28/notite-revizuit.md",
         repartizare=REPARTIZARE_28_08,
         absorbite=ABSORBITE_28_08),
]

#: Toate intrările, pentru numărători și pentru parcurgerea în ordine.
REPARTIZARE = [e for s in SURSE for e in s["repartizare"]]

#: titlu → destinație. Valabil global pentru că titlurile chiar nu se repetă azi;
#: verificarea de mai jos pică zgomotos dacă vreodată se repetă.
UNDE = {titlu: dest for titlu, dest, _ in REPARTIZARE}
DE_CE = {titlu: motiv for titlu, _, motiv in REPARTIZARE}
ABSORBITE = {k: v for s in SURSE for k, v in s["absorbite"].items()}

_toate = [t for t, _, _ in REPARTIZARE]
if len(_toate) != len(set(_toate)):
    _dubluri = sorted({t for t in _toate if _toate.count(t) > 1})
    raise SystemExit(f"date/repartizare.py: titluri repetate între surse — {_dubluri}. "
                     f"Harta globală `UNDE` nu le mai poate distinge; repartizarea "
                     f"trebuie făcută pe sursă.")
