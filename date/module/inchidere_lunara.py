"""MOD_INCHIDERE_LUNARA — verificarea lunară a balanței, pe corelațiile declarate.

Foaia `Închideri periodice` din workbook-ul de plan spune **ce** se verifică lunar.
Modulul ăsta **face** verificarea, pe cifrele clientului. Acoperă F-70 (închiderea
obligațiilor salariale) și F-32 (statul de plată).

Tiparul celor patru foi se adaptează, și o spun ca atare: modulul nu produce înregistrări
contabile, produce un verdict. `Jurnale_` devine `Verificări_`, iar `NotaExport_` devine
`Abateri_` — doar ce nu s-a potrivit, cu ce înseamnă și ce se face.

Regula pe care o aplică peste tot, în familia C-24…C-29: **pentru orice datorie
constituită lunar și achitată în luna următoare, la sfârșit de lună soldul creditor
egalează rulajul creditor.** Nu e coincidență de calendar, e consecința decalajului de
scadență — deci orice depășire e restanță, nu decalaj.

Luna-exemplu continuă cifrele din F-413 și F-422: brut 50.000, obligații 21.875, net
29.250 neplătit încă la 31 iulie. E o lună care SE RECONCILIAZĂ — altfel celulele Check
ar fi roșii la build, iar poarta 8 ar pica pe un modul livrat cu erori.

⚠ LIMITĂRI DECLARATE (vezi Reguli, tabelul C) — nu sunt omisiuni tăcute:
  - verifică soldurile, nu documentele: nu poate spune dacă statul de plată e corect
    întocmit, doar dacă balanța se potrivește cu el;
  - `421 + 423 = rest de plată` cere restul de plată introdus manual, din stat;
  - conturile fără corelație declarată (455, 461, 462, 5187) nu apar aici — n-au flux
    care să le declare starea, iar golul e declarat în `date/inchideri.py:GOLURI`.
"""

COD = "MOD_INCHIDERE_LUNARA"

CATALOG = dict(
    fluxuri="F-70, F-32",
    tip="Lunar, pe balanța de verificare",
    variabile="Rulaj debitor, rulaj creditor și sold pentru conturile cu cadență; "
              "restul de plată de pe stat; soldul din decontul de TVA",
    porti="Verifică solduri, nu documente — vezi Reguli, tabelul C",
    blocuri="V1 Obligații lunare (rulaj = sold); V2 Datoria față de salariați; "
            "V3 Conturi care trebuie golite; V4 Verificarea CAM pe cifre",
)

#: (cont, etichetă, rulaj debitor, rulaj creditor, sold) — luna-exemplu, iulie.
#: Obligațiile lunii curente pe credit, plata lunii precedente pe debit. Ce rămâne pe
#: credit e exact obligația lunii, deci sold = rulaj creditor.
OBLIGATII = [
    ("444", "Impozit pe venituri din salarii", 3250, 3250, 3250),
    ("4315", "CAS — contribuția de asigurări sociale", 12500, 12500, 12500),
    ("4316", "CASS — asigurări sociale de sănătate", 5000, 5000, 5000),
    ("436", "CAM — contribuția asiguratorie pentru muncă", 1125, 1125, 1125),
    ("427", "Rețineri din salarii datorate terților", 0, 0, 0),
]

#: (cont, etichetă, sold) — conturi de tranzit, care trebuie să ajungă la zero.
GOLIRE = [
    ("473", "Decontări din operațiuni în curs de clarificare", 0),
    ("581", "Viramente interne", 0),
    ("542", "Avansuri de trezorerie", 0),
    ("4382", "Alte creanțe sociale (de recuperat de la FNUASS)", 0),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_INCHIDERE_LUNARA",
          {"A": 12, "B": 44, "C": 16, "D": 16, "E": 16, "F": 46})
    d.titlu("MOD_INCHIDERE_LUNARA — Declarații (input din balanță)")
    d.nota("Completează galben, din balanța de verificare a lunii: rulajul debitor, "
           "rulajul creditor și soldul final, pentru fiecare cont. Valorile implicite "
           "sunt luna-exemplu din F-422 (brut 50.000), care se reconciliază — "
           "înlocuiește-le cu ale clientului.")
    d.gol()

    d.sectiune("1. Antet")
    luna = d.kv("Luna verificată", "iulie 2026")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    d.gol()

    d.sectiune("2. Obligații constituite lunar și achitate în luna următoare")
    d.nota("Regula: la sfârșitul lunii, soldul creditor = rulajul creditor al lunii. "
           "Un sold mai mare înseamnă restanță, iar mărimea ei spune de cât timp.")
    d.cap(["Cont", "Denumire", "Rulaj debitor", "Rulaj creditor", "Sold creditor"])
    ref_obl = {}
    for cont, den, rd, rc, sold in OBLIGATII:
        r = d.rand([cont, den, rd, rc, sold])
        # coloanele C, D, E sunt input; le rescriem ca atare
        for col, val in (("C", rd), ("D", rc), ("E", sold)):
            d.ws[f"{col}{d.r - 1}"] = val
        ref_obl[cont] = dict(rd=f"C{d.r - 1}", rc=f"D{d.r - 1}", sold=f"E{d.r - 1}")
    d.gol()

    d.sectiune("3. Datoria față de salariați")
    s421 = d.kv("Sold creditor 421 — salarii datorate", 29250)
    s423 = d.kv("Sold creditor 423 — ajutoare materiale", 0)
    stat = d.kv("Rest de plată din statul de plată", 29250,
                nota="Se ia din stat, nu din balanță — asta e tot rostul corelației")
    d.gol()

    d.sectiune("4. Baza CAM")
    brut = d.kv("Rulaj creditor 421 — brutul realizat al lunii", 50000)
    d.kv("Cota CAM", "=param_cota_cam", tip="calc",
         nota="Din Parametri; 2,25% aplicat la fondul de salarii")
    d.gol()

    d.sectiune("5. Conturi de tranzit — trebuie golite")
    d.cap(["Cont", "Denumire", "Sold la sfârșitul lunii"])
    ref_gol = {}
    for cont, den, sold in GOLIRE:
        d.rand([cont, den, sold])
        d.ws[f"C{d.r - 1}"] = sold
        ref_gol[cont] = f"C{d.r - 1}"
    d.gol()

    d.sectiune("6. TVA")
    s4423 = d.kv("Sold 4423 din balanță", 5250)
    dec = d.kv("Sold de plată din decontul de TVA", 5250,
               nota="Soldul, nu rulajul lunii. La rambursare, atenția merge pe soldul "
                    "cu care pleci")

    # ------------------------------------------------------------------- Reguli
    g = F("Reguli_INCHIDERE_LUNARA", {"A": 10, "B": 52, "C": 52, "D": 52})
    g.titlu("MOD_INCHIDERE_LUNARA — Reguli")
    g.nota("Tabele fixe. Se editează doar când se schimbă legea sau când o corelație "
           "nouă intră în workbook-ul de plan.")
    g.gol()

    g.sectiune("Tabelul A — corelațiile verificate și ce le rupe")
    g.cap(["Cod", "Corelația", "Ce o rupe LEGITIM", "Ce o rupe SUSPECT"])
    for cod, formula, legitim, suspect in [
        ("C-24", "sold C 421 + sold C 423 = rest de plată din stat",
         "Avans pe 425, nescăzut încă · drepturi neridicate mutate pe 426",
         "Plată înregistrată pe alt cont decât 421 · salarii restante nereclasificate"),
        ("C-25", "rulaj C 444 = sold C 444",
         "Rectificativă pe o lună anterioară · plată în avans",
         "Sold > rulaj constant = stopaj la sursă nevirat. Peste 30 de zile, penal"),
        ("C-26", "rulaj C 4315/4316/436 = soldurile lor",
         "Rectificativă · eșalonare la plată aprobată de ANAF",
         "Contribuții restante · bază de calcul care nu corespunde brutului"),
        ("C-27", "cota CAM × rulaj C 421 = rulaj C 436",
         "Luni cu concedii medicale: CAM nu se datorează pe partea din FNUASS "
         "(art. 220^5) · categorii cu cotă redusă",
         "Sporuri sau prime omise din fondul de salarii · CAM înregistrat invers"),
        ("C-28", "rulaj C 427 = sold C 427",
         "Poprire înființată la final de lună, cu virare în luna următoare",
         "Sold care persistă = bani opriți din salariul altcuiva și nevirați"),
        ("C-29", "sold 4423 din balanță = sold din decontul de TVA",
         "Sume din decizii de impunere, pe analitic distinct (F-421)",
         "TVA neachitat din perioade precedente, omis din decont"),
        ("—", "sold 473, 581, 542, 4382 = 0",
         "Operațiune de final de lună, închisă în primele zile ale lunii următoare",
         "Sold care se reportează = operațiune neterminată, ascunsă în balanță"),
    ]:
        g.rand([cod, formula, legitim, suspect])
    g.gol()

    g.sectiune("Tabelul B — cadențele, din foaia „Închideri periodice”")
    g.nota("Lista nu se rescrie aici: e aceeași cu cea din workbook-ul de plan, care o "
           "derivă din stările terminale ale fluxurilor (poarta 17).")
    g.gol()

    g.sectiune("Tabelul C — LIMITĂRI DECLARATE")
    g.cap(["Ce NU face modulul", "De ce contează"])
    for a, b in [
        ("Verifică solduri, nu documente",
         "Nu poate spune dacă statul de plată e corect întocmit — doar dacă balanța se "
         "potrivește cu el. Un stat greșit, reflectat fidel în balanță, trece."),
        ("Restul de plată se introduce manual",
         "Vine din stat, nu din balanță. Dacă îl copiezi din balanță, corelația devine "
         "tautologie și nu mai verifică nimic."),
        ("Conturile fără corelație declarată nu apar",
         "455, 461, 462, 5187 au cadență, dar niciun flux nu le declară starea "
         "terminală. Golul e declarat în `date/inchideri.py`, nu ascuns aici."),
        ("O singură lună odată",
         "Restanța se vede ca diferență sold − rulaj, dar vechimea ei se află doar "
         "comparând mai multe luni. Aici se vede CĂ există, nu de când."),
    ]:
        g.rand([a, b])

    # --------------------------------------------------------------- Verificări
    v = F("Verificări_INCHIDERE_LUNARA",
          {"A": 10, "B": 46, "C": 16, "D": 16, "E": 16, "F": 40})
    v.titlu("MOD_INCHIDERE_LUNARA — Verificări")
    v.nota("O linie pe corelație, calculată din Declarații. Coloana „Diferență” e ce "
           "contează: zero înseamnă că se potrivește.")
    v.gol()

    D = "Declarații_INCHIDERE_LUNARA"
    verificari = []

    v.sectiune("V1 — obligații lunare: rulaj creditor = sold creditor")
    v.cap(["Cod", "Ce verifică", "Rulaj C", "Sold C", "Diferență", "Verdict"])
    for cont, den, *_ in OBLIGATII:
        r = ref_obl[cont]
        cod = {"444": "C-25", "4315": "C-26", "4316": "C-26",
               "436": "C-26", "427": "C-28"}[cont]
        v.rand([cod, f"{cont} — {den}",
                f"={D}!{r['rc']}", f"={D}!{r['sold']}",
                f"={D}!{r['sold']}-{D}!{r['rc']}",
                f'=IF(ABS(E{v.r})<0.01,"OK",'
                f'"ATENȚIE — sold peste rulaj: restanță de "&TEXT(E{v.r},"#,##0")&" lei")'])
        verificari.append((cod, f"{cont} {den}", f"E{v.r - 1}"))
    v.gol()

    v.sectiune("V2 — datoria față de salariați")
    v.cap(["Cod", "Ce verifică", "Din balanță", "Din stat", "Diferență", "Verdict"])
    v.rand(["C-24", "421 + 423 = rest de plată de pe stat",
            f"={D}!{s421}+{D}!{s423}", f"={D}!{stat}",
            f"={D}!{s421}+{D}!{s423}-{D}!{stat}",
            f'=IF(ABS(E{v.r})<0.01,"OK",'
            f'"ATENȚIE — balanța nu corespunde statului")'])
    verificari.append(("C-24", "421 + 423 vs. stat", f"E{v.r - 1}"))
    v.gol()

    v.sectiune("V3 — conturi de tranzit, care trebuie golite")
    v.cap(["Cod", "Ce verifică", "Sold", "Așteptat", "Diferență", "Verdict"])
    for cont, den, _ in GOLIRE:
        v.rand(["—", f"{cont} — {den}", f"={D}!{ref_gol[cont]}", 0,
                f"={D}!{ref_gol[cont]}",
                f'=IF(ABS(E{v.r})<0.01,"OK",'
                f'"ATENȚIE — operațiune neterminată, ascunsă în balanță")'])
        verificari.append(("—", f"{cont} sold zero", f"E{v.r - 1}"))
    v.gol()

    v.sectiune("V4 — CAM pe cifre și TVA")
    v.cap(["Cod", "Ce verifică", "Calculat", "Din balanță", "Diferență", "Verdict"])
    r436 = ref_obl["436"]
    v.rand(["C-27", "cota CAM × brut = rulaj C 436",
            f"=ROUND({D}!{brut}*param_cota_cam,2)", f"={D}!{r436['rc']}",
            f"={D}!{r436['rc']}-ROUND({D}!{brut}*param_cota_cam,2)",
            f'=IF(ABS(E{v.r})<0.01,"OK",'
            f'"ATENȚIE — bază de calcul greșită sau concedii medicale (vezi Reguli A)")'])
    verificari.append(("C-27", "CAM pe cifre", f"E{v.r - 1}"))
    v.rand(["C-29", "sold 4423 din balanță = sold din decont",
            f"={D}!{s4423}", f"={D}!{dec}", f"={D}!{s4423}-{D}!{dec}",
            f'=IF(ABS(E{v.r})<0.01,"OK",'
            f'"ATENȚIE — decontul și balanța nu spun același lucru")'])
    verificari.append(("C-29", "4423 vs. decont", f"E{v.r - 1}"))
    v.gol()

    v.sectiune("Control final")
    total = "+".join(f"ABS({r})" for _, _, r in verificari)
    v.check("Check — toate corelațiile lunii", f"={total}",
            f'=IF(ABS(B{v.r})<0.01,"OK — luna se reconciliază pe toate corelațiile",'
            f'"EROARE — vezi foaia Abateri")')

    # ------------------------------------------------------------------ Abateri
    a = F("Abateri_INCHIDERE_LUNARA", {"A": 10, "B": 12, "C": 46, "D": 16, "E": 56})
    a.titlu("MOD_INCHIDERE_LUNARA — Abateri")
    a.nota("Coloana „Include” spune DA doar unde corelația nu s-a potrivit. Lista e "
           "completă: dacă toate sunt NU, luna e curată.")
    a.gol()
    a.cap(["Include", "Cod", "Ce nu s-a potrivit", "Diferență", "Ce se face"])
    ACTIUNE = {
        "C-24": "Se scot statele lună de lună și se caută luna în care s-a rupt. "
                "Cauza tipică: plată pe alt cont decât 421.",
        "C-25": "Se verifică fișa de plătitor din SPV. Stopaj nevirat peste 30 de zile "
                "= răspundere penală, nu întârziere.",
        "C-26": "Se confruntă cu D112. Dacă e eșalonare, se notează; altfel e restanță.",
        "C-27": "Se verifică dacă luna are concedii medicale — CAM nu se datorează pe "
                "partea din FNUASS. Altfel, bază de calcul incompletă.",
        "C-28": "Se virează imediat. Banii sunt ai salariatului, opriți pentru altcineva.",
        "C-29": "Se verifică dacă e sumă din decizie de impunere (analitic distinct) "
                "sau TVA neachitat din perioade precedente, omis din decont.",
        "—": "Se identifică operațiunea neterminată și se închide. Un sold reportat pe "
             "un cont de tranzit ascunde ceva.",
    }
    V = "Verificări_INCHIDERE_LUNARA"
    for cod, eticheta, ref in verificari:
        a.rand([f'=IF(ABS({V}!{ref})<0.01,"NU","DA")', cod, eticheta,
                f"={V}!{ref}", ACTIUNE[cod]])
    a.gol()
    a.check("Check — număr de abateri",
            f'=COUNTIF(A{a.r - len(verificari) - 1}:A{a.r - 2},"DA")',
            f'=IF(B{a.r}=0,"OK — nicio abatere",'
            f'"ATENȚIE — "&B{a.r}&" corelații nu se potrivesc")')
