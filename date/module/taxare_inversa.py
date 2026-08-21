"""MOD_TAXARE_INVERSA — autolichidarea TVA: 4426 și 4427 în aceeași notă.

Acoperă F-03 (achiziție intracomunitară) și F-18 (taxare inversă internă).

Mecanismul e identic în ambele cazuri: cumpărătorul își face singur TVA-ul, deducându-l
și colectându-l simultan pe aceeași sumă. Efectul net pe trezorerie e **zero** — de-aia
se și numește autolichidare. Ce diferă e doar partenerul și declarația în care ajunge
operațiunea, iar confuzia celor două nu produce o notă contabilă greșită, produce o
declarație greșită.

    intracomunitar  →  401.UE, cod VIES valid   →  D300 + D390 + D394
    intern          →  401.RO, plătitor de TVA  →  D300 + D394, fără D390

## Ce se greșește

**Sume diferite pe 4426 și 4427.** Dacă cineva scrie una din ele de mână, netul nu mai
e zero și apare TVA de plată sau de recuperat din senin. Garda din foaia de control
compară cele două rânduri.

**D390 la operațiune internă, sau lipsa lui la una intracomunitară.** Declarația
recapitulativă privește doar tranzacțiile intracomunitare. Un partener intern trecut
acolo, sau unul din UE omis, se vede la ANAF prin necorelare cu VIES.

## Termen în calendar

Taxarea inversă **internă** nu e un regim permanent: art. 331 Cod fiscal se aplică pe
baza unei derogări acordate de Consiliul UE, prelungite succesiv, iar cea în vigoare
**expiră la 31.12.2026**. La ultima verificare (21.08.2026) nu era publicată o prelungire
dincolo de data asta. Nu se presupune prelungirea automată — se reverifică înainte de
prima factură din 2027.
"""
from .comun import formula_activ

COD = "MOD_TAXARE_INVERSA"

CATALOG = dict(
    fluxuri="F-03, F-18",
    tip="Pe factură",
    variabile="Valoare (sau valută × curs), cota TVA, tipul operațiunii, partenerul",
    porti="4426 = 4427 exact; D390 doar la intracomunitar",
    blocuri="A Achiziție intracomunitară; B Taxare inversă internă",
    ce_face="Autolichidare 4426 = 4427, intracomunitar și intern",
    cand="La fiecare factură cu taxare inversă",
    activ="NU",
)

#: caz, partener, cont furnizor, ce declară, condiție
CAZURI = [
    ("Achiziție intracomunitară", "Persoană impozabilă din alt stat membru", "401.UE",
     "D300 (casete taxare inversă) + D390 + D394",
     "Cod de TVA valid în VIES la data operațiunii"),
    ("Taxare inversă internă", "Plătitor de TVA din România", "401.RO",
     "D300 (casete taxare inversă) + D394, FĂRĂ D390",
     "Bunul sau serviciul e pe lista art. 331 CF"),
]

#: operațiune din lista art. 331 CF, observație
LISTA_331 = [
    ("Cereale și plante tehnice", "fără prag valoric"),
    ("Certificate de emisii de gaze cu efect de seră", "fără prag valoric"),
    ("Energie electrică și gaze naturale către comercianți persoane impozabile",
     "fără prag valoric"),
    ("Certificate verzi", "fără prag valoric"),
    ("Telefoane mobile", "doar dacă valoarea fără TVA de pe factură ≥ 22.500 lei"),
    ("Dispozitive cu circuite integrate",
     "doar dacă valoarea fără TVA de pe factură ≥ 22.500 lei"),
    ("Console de jocuri", "doar dacă valoarea fără TVA de pe factură ≥ 22.500 lei"),
    ("Tablete și laptopuri", "doar dacă valoarea fără TVA de pe factură ≥ 22.500 lei"),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_TAXARE_INVERSA", {"A": 46, "B": 24, "C": 58})
    d.titlu("MOD_TAXARE_INVERSA — Declarații (input)")
    d.nota("Două cazuri, același mecanism. Pune DA pe cel care s-a întâmplat — pot fi "
           "și amândouă în aceeași lună, pe facturi diferite.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    d.kv("CUI", "=Parametri!B6", tip="calc")
    luna = d.kv("Luna (AAAA-LL)", "2026-07")
    data_j = d.kv("Data jurnal", "2026-07-31")
    cota = d.kv("Cota TVA", 0.21)
    d.gol()

    d.sectiune("2. Cazul A — Achiziție intracomunitară")
    a_on = d.kv("Se aplică? (DA/NU)", "DA")
    a_furnizor = d.kv("Furnizor UE", "Furnizor UE DEMO")
    a_vies = d.kv("Cod TVA valid în VIES? (DA/NU)", "DA",
                  nota="Verificat la DATA operațiunii, nu azi — VIES arată starea curentă")
    a_valuta = d.kv("Valoare în valută", 15000)
    a_curs = d.kv("Curs la data facturii", 4.97)
    a_lei = d.kv("Valoare în lei (auto)", f"=ROUND({a_valuta}*{a_curs},2)", tip="calc")
    # TVA se INTRODUCE, nu se calculează: în practică vine din program sau de pe
    # autofactură. Calculul stă alături ca să aibă garda ce compara — o valoare pe care
    # modulul o produce singur nu poate fi verificată de el.
    a_tva = d.kv("TVA autolichidată (din autofactură)", 15655.50)
    a_tva_calc = d.kv("TVA recalculată (auto)", f"=ROUND({a_lei}*{cota},2)", tip="calc")
    a_tranzit = d.kv("Marfa e în tranzit? (DA = 327, NU = 371)", "NU")
    d.gol()

    d.sectiune("3. Cazul B — Taxare inversă internă")
    b_on = d.kv("Se aplică? (DA/NU)", "DA")
    b_furnizor = d.kv("Furnizor RO (plătitor de TVA)", "Furnizor RO DEMO")
    b_operatiune = d.kv("Operațiunea din art. 331 CF", "Cereale")
    b_lei = d.kv("Valoare fără TVA", 10000)
    b_tva = d.kv("TVA autolichidată (din autofactură)", 2100)
    b_tva_calc = d.kv("TVA recalculată (auto)", f"=ROUND({b_lei}*{cota},2)", tip="calc")
    d.gol()

    d.sectiune("4. Conturi")
    c_stoc = d.kv("Cont stoc / cheltuială", "371")
    c_tranzit = d.kv("Cont tranzit (32x)", "327")
    c_ue = d.kv("Cont furnizor UE", "401.UE")
    c_ro = d.kv("Cont furnizor RO", "401.RO")
    c_4426 = d.kv("Cont TVA deductibilă", "4426")
    c_4427 = d.kv("Cont TVA colectată", "4427")
    d.gol()

    d.sectiune("5. Sufix")
    sufix = d.kv("Sufix", f'="— taxare inversă " & {luna}', tip="calc")
    d.gol()

    d.sectiune("6. Control")
    d.kv("Modul activ?", formula_activ(COD), tip="calc")
    # Garda compară TVA-ul INTRODUS cu cel recalculat. Netul zero e garantat prin
    # construcție (ambele părți citesc aceeași celulă), deci o gardă pe el ar fi
    # decorativă — ar fi mereu verde, indiferent ce se întâmplă.
    ver_net = d.kv(
        "Verificare: TVA de pe autofactură = cotă × bază",
        f'=IF(AND(OR({a_on}<>"DA",ABS({a_tva}-{a_tva_calc})<0.01),'
        f'OR({b_on}<>"DA",ABS({b_tva}-{b_tva_calc})<0.01)),'
        f'"OK — TVA corect calculată pe ambele cazuri",'
        f'"EROARE — TVA de pe autofactură nu corespunde cotei")', tip="calc")
    ver_vies = d.kv(
        "Verificare: intracomunitar fără cod VIES valid",
        f'=IF(AND({a_on}="DA",{a_vies}<>"DA"),'
        f'"ATENȚIE — fără cod VIES valid, operațiunea NU e scutită la furnizor și '
        f'nu poate fi declarată în D390","OK")', tip="calc")
    d.kv("Declarații de depus (auto)",
         f'=IF({a_on}="DA","D300 + D390 + D394","") & '
         f'IF(AND({a_on}="DA",{b_on}="DA")," · ","") & '
         f'IF({b_on}="DA","D300 + D394 (fără D390)","")', tip="calc")
    d.kv("Derogare art. 331 CF",
         "Taxarea inversă INTERNĂ se aplică pe baza unei derogări UE care expiră la "
         "31.12.2026. La 21.08.2026 nu era publicată o prelungire — reverifică înainte "
         "de prima factură din 2027.", tip="calc")

    # ------------------------------------------------------------------- Reguli
    g = F("Reguli_TAXARE_INVERSA",
          {"A": 30, "B": 44, "C": 16, "D": 44, "E": 48})
    g.titlu("MOD_TAXARE_INVERSA — Reguli (tabele fixe)")
    g.nota("Regula e dată, nu formulă. Mecanismul contabil e identic în ambele cazuri; "
           "diferă partenerul și declarația.")
    g.gol()

    g.sectiune("Tabel A — Cele două cazuri")
    g.cap(["Caz", "Partener", "Cont furnizor", "Ce declară", "Condiție"])
    for rand in CAZURI:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel B — Operațiuni cu taxare inversă internă (art. 331 CF)")
    g.cap(["Operațiune", "Prag"])
    for rand in LISTA_331:
        g.rand(list(rand))
    g.nota("Derogarea Consiliului UE pe baza căreia se aplică art. 331 expiră la "
           "31.12.2026. Verificat la 21.08.2026: nicio prelungire publicată. Nu se "
           "presupune prelungirea automată.")
    g.gol()

    g.sectiune("Tabel C — Porți de calitate")
    for linie in [
        "• 4426 și 4427 primesc EXACT aceeași sumă — netul pe operațiune e zero",
        "• D390 doar la intracomunitar; un partener intern trecut acolo se vede la ANAF "
        "prin necorelare cu VIES",
        "• Codul VIES se verifică la DATA operațiunii, nu la data când te uiți",
        "• Fără TVA plătită efectiv: autolichidarea nu produce flux de trezorerie",
        "• La închiderea lunară, sumele astea intră în 4426/4427 ca oricare altele și se "
        "anulează reciproc — vezi MOD_INCHIDERE_TVA",
    ]:
        g.nota(linie)

    # ------------------------------------------------------------------ Jurnale
    j = F("Jurnale_TAXARE_INVERSA",
          {"A": 30, "B": 16, "C": 14, "D": 50, "E": 16, "F": 14, "G": 50})
    j.titlu("MOD_TAXARE_INVERSA — Jurnale (generate automat)")
    j.nota("Fiecare caz iese cu zero dacă nu e activat. Pasul de autolichidare are "
           "aceeași sumă pe ambele părți — asta e chiar mecanismul, nu o coincidență.")
    j.gol()

    D = d.ref
    antet = ["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr",
             "Descriere Cr"]

    def daca(comutator, valoare):
        return f'=IF({D(comutator)}="DA",{D(valoare)},0)'

    j.sectiune("Bloc A — Achiziție intracomunitară")
    j.kv("Data:", f"={D(data_j)}", tip="calc")
    j.cap(antet)
    a1 = j.rand([1, f'=IF({D(a_tranzit)}="DA",{D(c_tranzit)},{D(c_stoc)})',
                 daca(a_on, a_lei),
                 f'="Achiziție intracomunitară " & {D(a_furnizor)} & " " & {D(sufix)}',
                 f"={D(c_ue)}", daca(a_on, a_lei),
                 f'="Datorie furnizor UE " & {D(sufix)}'])
    ca1 = j.check("Check A1 (factura)", f"={a1['C']}-{a1['F']}",
                  f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    a2 = j.rand([2, f"={D(c_4426)}", daca(a_on, a_tva),
                 f'="TVA deductibilă prin autolichidare " & {D(sufix)}',
                 f"={D(c_4427)}", daca(a_on, a_tva),
                 f'="TVA colectată prin autolichidare " & {D(sufix)}'])
    # Aici netul e zero prin construcție; ce se verifică e că suma pusă în notă e chiar
    # cea recalculată din bază, nu una scrisă de mână peste ea.
    ca2 = j.check("Check A2 (autolichidare = cotă × bază)",
                  f"={a2['C']}-IF({D(a_on)}=\"DA\",{D(a_tva_calc)},0)",
                  f'=IF(ABS(B{j.r})<0.01,"OK — 4426 = 4427 = cotă × bază",'
                  f'"EROARE — suma din notă nu e cotă × bază")')
    j.gol()

    j.sectiune("Bloc B — Taxare inversă internă")
    j.cap(antet)
    b1 = j.rand([1, f"={D(c_stoc)}", daca(b_on, b_lei),
                 f'="Achiziție cu taxare inversă (" & {D(b_operatiune)} & ") " '
                 f'& {D(sufix)}',
                 f"={D(c_ro)}", daca(b_on, b_lei),
                 f'="Datorie furnizor RO " & {D(sufix)}'])
    cb1 = j.check("Check B1 (factura)", f"={b1['C']}-{b1['F']}",
                  f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    b2 = j.rand([2, f"={D(c_4426)}", daca(b_on, b_tva),
                 f'="TVA deductibilă prin autolichidare " & {D(sufix)}',
                 f"={D(c_4427)}", daca(b_on, b_tva),
                 f'="TVA colectată prin autolichidare " & {D(sufix)}'])
    cb2 = j.check("Check B2 (autolichidare = cotă × bază)",
                  f"={b2['C']}-IF({D(b_on)}=\"DA\",{D(b_tva_calc)},0)",
                  f'=IF(ABS(B{j.r})<0.01,"OK — 4426 = 4427 = cotă × bază",'
                  f'"EROARE — suma din notă nu e cotă × bază")')
    j.gol()

    glob = j.check("Check global",
                   f"=ABS({ca1})+ABS({ca2})+ABS({cb1})+ABS({cb2})",
                   f'=IF(B{j.r}<0.01,"OK — toate blocurile se închid",'
                   f'"EROARE — cel puțin un bloc dezechilibrat")')
    j.gol()
    j.sectiune("Stare terminală")
    j.nota("Nicio TVA de plată suplimentară din operațiunile astea: 4426 și 4427 s-au "
           "mișcat cu aceeași sumă și se anulează la închiderea lunară. Ce rămâne e "
           "raportarea: D300 la ambele, D390 doar la intracomunitar.")

    # --------------------------------------------------------------- NotaExport
    e = F("NotaExport_TAXARE_INVERSA",
          {"A": 6, "B": 26, "C": 14, "D": 12, "E": 12, "F": 14, "G": 50, "H": 24,
           "I": 10})
    e.titlu("MOD_TAXARE_INVERSA — Notă pentru import")
    e.nota("Filtrează Include=DA. Cazurile neactivate ies cu sumă 0 și apar ca NU.")
    e.gol()
    e.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    primul = e.r
    for i, (bloc, r, doc) in enumerate([
        ("A Intracomunitar — factura", a1, "Factură furnizor UE"),
        ("A Intracomunitar — autolichidare", a2, "Autofactură"),
        ("B Intern — factura", b1, "Factură (mențiune taxare inversă)"),
        ("B Intern — autolichidare", b2, "Autofactură"),
    ], start=1):
        e.rand([i, bloc, f"={D(data_j)}", f"={j.ref(r['B'])}", f"={j.ref(r['E'])}",
                f"={j.ref(r['C'])}", f"={j.ref(r['D'])}", doc,
                f'=IF(AND(ISNUMBER(F{e.r}),F{e.r}>0),"DA","NU")'])
    ultim = e.r - 1
    e.gol()
    e.kv("Rânduri de importat", f'=COUNTIF(I{primul}:I{ultim},"DA")', tip="calc")
    e.check("Check global", f"={j.ref(glob)}",
            f'=IF(ABS(B{e.r})<0.01,"OK","EROARE")')
