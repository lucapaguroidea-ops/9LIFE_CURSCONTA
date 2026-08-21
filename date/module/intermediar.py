"""MOD_INTERMEDIAR — conturile care așteaptă un eveniment discret: 408, 418, 581, 473.

Acoperă F-23 (408/418), F-30… — vezi `CATALOG`. Un singur tipar pentru patru conturi,
pentru că toate patru fac același lucru: se deschid când operațiunea începe și se sting
când **evenimentul discret** are loc — documentul sosește, suma se identifică, transferul
se confirmă. Nu trece timpul, nu se amortizează nimic: se întâmplă ceva, sau nu.

Modulul era una din cele șapte foi rămase din sămânța de 14.08.2026, întreținute de mână.
Portarea a scos la iveală un defect viu, descris mai jos.

## Defectul găsit la portare: red flag-ul pe 473 nu se aprindea niciodată

Sămânța scria controlul așa:

    =IF(B10=473,"Sold 473 la 31.12 = suspect — clarificare obligatorie","—")

`B10` conține textul `"473"`, iar Excel nu compară text cu număr: `"473"=473` e FALSE,
întotdeauna. Cu tipul implicit chiar pe 473, celula afișa `—`. Adică singurul avertisment
serios al modulului — soldul de 473 rămas la 31 decembrie, care în notițe e SUSPECT, nu
LEGITIM — era cod mort.

Aici se compară text cu text, deci se aprinde. E singura valoare care diferă de sămânță,
și diferă intenționat: restul portării reproduce cifră cu cifră.
"""

COD = "MOD_INTERMEDIAR"

CATALOG = dict(
    # Cele două liste vechi nu coincideau: `Index module` spunea „F-408, F-411, F-304”,
    # `CatalogModule` spunea „F-408, F-501, F-411”. Aici e una singură, citită din ce
    # acoperă foile efectiv: tabelul A tratează 408/418 (F-408), 581 (F-501) și 473
    # (F-411). F-304 iese — acolo e intersecția 32x ↔ 408 cu același furnizor, o stare
    # inițială murdară pe care tiparul generic de aici nu o modelează.
    fluxuri="F-23, F-33, F-34",
    tip="Eveniment discret",
    variabile="Sumă, Cont intermediar (408/418/581/473), Cont final, Document",
    porti="Un set de Declarații = un tip + o operațiune; modulul nu amestecă tipurile",
    blocuri="B1 Deschidere intermediar; B2 Stingere",
    # `Index module` are alte două coloane: „Ce face” și „Când îl rulezi”. Până acum
    # primeau `blocuri` și `tip`, deci textul mai descriptiv din sămânță se pierdea la
    # regenerare. Un câmp per coloană; lipsa lui cade înapoi pe cel vechi.
    ce_face="408/418/473: deschidere + stingere + red flags",
    cand="La facturi nesosite / sume neclare",
    activ="NU",
)

#: tip, denumire, rol, deschidere tipică, stingere tipică, pas revelator / red flag
TIPURI = [
    ("408", "Furnizori — facturi nesosite", "Intermediar",
     "Dr stoc / 4426 = Cr 408", "Dr 408 = Cr 401",
     "Sold 408 la 31.12 = facturi încă nesosite"),
    ("418", "Clienți — facturi de întocmit", "Intermediar",
     "Dr 418 = Cr venit / 4427", "Dr 411 = Cr 418",
     "Sold 418 = livrat nefacturat"),
    ("581", "Viramente interne", "Intermediar",
     "Dr 581 = Cr 512 (ieșire)", "Dr 531/512 = Cr 581 (intrare)",
     "Sold 581 = transfer neconfirmat"),
    ("473", "Operațiuni în curs de clarificare", "Intermediar",
     "Dr 512 = Cr 473 (intrare neid.)", "Dr 473 = Cr 411/401/768",
     "Sold 473 la 31.12 = SUSPECT — clarificare obligatorie"),
]


from .comun import formula_activ  # noqa: E402


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_INTERMEDIAR", {"A": 46, "B": 30, "C": 58})
    d.titlu("MOD_INTERMEDIAR — Declarații (input)")
    d.nota("Modul generic pentru conturi de tip Intermediar / clarificare: 408, 418, "
           "581, 473. Alege tipul, completează sumele și conturile — jurnalele se "
           "generează pe cele două momente (deschidere + stingere).")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    d.kv("CUI", "=Parametri!B6", tip="calc")
    luna = d.kv("Luna (AAAA-LL)", "2026-07")
    d.gol()

    d.sectiune("2. Tip intermediar (poartă principală)")
    tip = d.kv("Tip (408 / 418 / 581 / 473)", "473")
    desc_tip = d.kv(
        "Descriere tip (auto)",
        "=IF({t}=\"408\",\"Furnizori — facturi nesosite\","
        "IF({t}=\"418\",\"Clienți — facturi de întocmit\","
        "IF({t}=\"581\",\"Viramente interne\","
        "IF({t}=\"473\",\"Operațiuni în curs de clarificare\","
        "\"Tip necunoscut — verifică\"))))".format(t=tip), tip="calc")
    d.gol()

    d.sectiune("3. Moment deschidere (Bloc 1)")
    data_desch = d.kv("Data deschidere", "2026-07-15")
    suma = d.kv("Sumă", 2350)
    cont_int = d.kv("Cont intermediar (Dr sau Cr după tip)", "473")
    cont_contra = d.kv("Cont contrapartidă deschidere", "5121")
    sens = d.kv("Sens deschidere (Dr_intermediar / Cr_intermediar)", "Cr_intermediar")
    doc_desch = d.kv("Document / referință deschidere",
                     "Extras bancă 15.07 — sumă neidentificată")
    d.gol()

    d.sectiune("4. Moment stingere (Bloc 2)")
    data_sting = d.kv("Data stingere", "2026-07-22")
    cont_final = d.kv("Cont final (după clarificare)", "411.RO")
    doc_sting = d.kv("Document / referință stingere", "Identificat: client X, factura Y")
    d.gol()

    d.sectiune("5. Sufix descriere (generat)")
    sufix = d.kv("Sufix", f'="— " & {luna} & " — " & {tip} & " — " & {doc_desch}',
                 tip="calc")
    d.gol()

    d.sectiune("6. Control")
    d.kv("Modul activ?",
         formula_activ(COD), tip="calc",
         nota="Căutat pe codul modulului, nu pe rândul din catalog. Sămânța scria "
              "`CatalogModule!A14`: mutai un rând în catalog și celula citea steagul "
              "altui modul, fără să spună nimic.")
    d.kv("Regulă 473",
         f'=IF({tip}="473","Sold 473 la 31.12 = suspect — clarificare obligatorie","—")',
         tip="calc",
         nota="Comparație text cu text. În sămânță era `=IF(B10=473,…)`, cu 473 ca "
              "NUMĂR — deci mereu FALSE, deci avertismentul nu apărea niciodată.")

    # ------------------------------------------------------------------- Reguli
    g = F("Reguli_INTERMEDIAR", {"A": 10, "B": 34, "C": 14, "D": 30, "E": 30, "F": 46})
    g.titlu("MOD_INTERMEDIAR — Reguli (tabele fixe)")
    g.nota("Pattern comun: deschidere pe cont intermediar → stingere pe cont final când "
           "evenimentul discret (document, identificare, confirmare) are loc.")
    g.gol()

    g.sectiune("Tabel A — Tipuri și sensuri standard")
    g.cap(["Tip", "Denumire", "Rol", "Deschidere tipică", "Stingere tipică",
           "Pas revelator / red flag"])
    for rand in TIPURI:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel B — Secvența generică a modulului")
    g.cap(["Pas", "Moment", "Logică", "Condiție"])
    g.rand([1, "Deschidere",
            "Cont intermediar ↔ Cont contrapartidă (bancă/stoc/venit)",
            "Sensul (Dr/Cr intermediar) se alege în Declarații"])
    g.rand([2, "Stingere",
            "Cont intermediar ↔ Cont final (401/411/512/531/768…)",
            "Când documentul / identificarea / confirmarea există"])
    g.gol()

    g.sectiune("Tabel C — Porți de calitate")
    for linie in [
        "• ΣDr = ΣCr pe fiecare bloc",
        "• După stingere: sold cont intermediar = 0 pe această operațiune",
        "• Pentru 473: dacă data stingerii e goală sau > 31.12 → semnalează red flag",
        "• Modulul nu amestecă tipurile — un set de Declarații = un tip + o operațiune",
    ]:
        g.nota(linie)

    # ------------------------------------------------------------------ Jurnale
    j = F("Jurnale_INTERMEDIAR",
          {"A": 12, "B": 16, "C": 14, "D": 52, "E": 16, "F": 14, "G": 52})
    j.titlu("MOD_INTERMEDIAR — Jurnale (generate automat)")
    j.nota("Sensul deschiderii (Dr sau Cr pe intermediar) se citește din Declarații. "
           "Stingerea inversează sensul.")
    j.gol()

    # `Foaie.kv` întoarce o coordonată SIMPLĂ („B27”). Folosită ca atare din altă foaie,
    # trimite la B27 din foaia curentă — goală. Aici se califică o dată, la început, și
    # se folosesc numai aliasurile de mai jos. Prima portare a sărit pasul ăsta și
    # jurnalele au ieșit cu descrieri fără sufix și cu sume 0.
    D_sens, D_suma = d.ref(sens), d.ref(suma)
    D_int, D_contra, D_final = d.ref(cont_int), d.ref(cont_contra), d.ref(cont_final)
    D_sufix, D_tip, D_desc = d.ref(sufix), d.ref(tip), d.ref(desc_tip)
    D_dd, D_ds = d.ref(data_desch), d.ref(data_sting)
    D_docd, D_docs = d.ref(doc_desch), d.ref(doc_sting)

    #: „Cr_intermediar” înseamnă că la DESCHIDERE contul intermediar stă pe credit, deci
    #: debitul e contrapartida. La STINGERE se inversează. Cele patru formule de mai jos
    #: sunt aceeași întrebare pusă de patru ori, o dată pe fiecare colț al notei.
    def pe_sens(daca_cr, daca_dr):
        return f'=IF({D_sens}="Cr_intermediar",{daca_cr},{daca_dr})'

    j.sectiune("Bloc 1 — Deschidere intermediar")
    j.kv("Data:", f"={D_dd}", tip="calc")
    j.kv("Tip:", f'={D_tip} & " — " & {D_desc}', tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr",
           "Descriere Cr"])
    b1 = j.rand([
        1,
        pe_sens(D_contra, D_int),
        f"={D_suma}",
        pe_sens('"Contrapartidă deschidere "', '"Deschidere intermediar "')
        + f" & {D_sufix}",
        pe_sens(D_int, D_contra),
        f"={D_suma}",
        pe_sens('"Deschidere intermediar "', '"Contrapartidă deschidere "')
        + f" & {D_sufix}",
    ])
    j.gol()
    # `j.r` e rândul pe care `check` ABIA urmează să-l scrie: argumentele f-string se
    # evaluează înainte de apel, deci nu se scade 1. Referința e locală (B11), nu
    # calificată cu numele foii — verdictul stă pe același rând cu valoarea.
    c1 = j.check("Check B1", f"={b1['C']}-{b1['F']}",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Bloc 2 — Stingere intermediar (pas revelator)")
    j.kv("Data:", f"={D_ds}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr",
           "Descriere Cr"])
    b2 = j.rand([
        1,
        pe_sens(D_int, D_final),
        f"={D_suma}",
        pe_sens('"Stingere intermediar "', '"Cont final (stingere) "') + f" & {D_sufix}",
        pe_sens(D_final, D_int),
        f"={D_suma}",
        pe_sens('"Cont final (stingere) "', '"Stingere intermediar "') + f" & {D_sufix}",
    ])
    j.gol()
    c2 = j.check("Check B2", f"={b2['C']}-{b2['F']}",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Stare terminală")
    j.nota("Sold intermediar pe această operațiune = 0. Pentru 473: dacă rămâne sold "
           "la 31.12 → red flag audit.")
    j.gol()
    glob = j.check("Check global", f"=ABS({c1})+ABS({c2})",
                   f'=IF(B{j.r}<0.01,"OK — toate blocurile se închid",'
                   f'"EROARE — cel puțin un bloc dezechilibrat")')

    # --------------------------------------------------------------- NotaExport
    e = F("NotaExport_INTERMEDIAR",
          {"A": 6, "B": 24, "C": 14, "D": 12, "E": 12, "F": 14, "G": 52, "H": 38,
           "I": 10})
    e.titlu("MOD_INTERMEDIAR — Notă pentru import")
    e.nota("Filtrează Include=DA. Cele două blocuri pot avea date diferite "
           "(deschidere vs. stingere).")
    e.gol()
    e.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    primul = e.r
    for i, (eticheta, data, b, doc) in enumerate([
        ("Bloc 1 — Deschidere", D_dd, b1, D_docd),
        ("Bloc 2 — Stingere", D_ds, b2, D_docs),
    ], start=1):
        e.rand([i, eticheta, f"={data}", f"={j.ref(b['B'])}", f"={j.ref(b['E'])}",
                f"={j.ref(b['C'])}", f"={j.ref(b['D'])}", f"={doc}",
                f'=IF(F{e.r}>0,"DA","NU")'])
    ultim = e.r - 1
    e.gol()
    e.kv("Rânduri de importat", f'=COUNTIF(I{primul}:I{ultim},"DA")', tip="calc")
    e.check("Check global", f"={j.ref(glob)}",
            f'=IF(ABS(B{e.r})<0.01,"OK","EROARE")')
