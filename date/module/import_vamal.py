"""MOD_IMPORT — cele două căi prin care TVA-ul vamal ajunge pe 4426.

Acoperă F-15 (import prin comisionar) și F-16 (import cu plată directă în vamă).

Diferența dintre ele e cine plătește TVA-ul în vamă. Cu comisionar, el avansează banii,
deci apare un INTERMEDIAR — 446.VAMA — care ține TVA-ul până se stinge datoria față de
comisionar. Cu plată directă, nu există intermediar: banii ies din bancă și TVA-ul intră
direct pe 4426.

## Cele două capcane, ambele pe cifre

**Baza TVA vamală = valoarea mărfii + taxele vamale.** Nu doar valoarea. Calculat pe
valoarea goală, TVA-ul iese mai mic cu exact cota × taxe — 630 de lei pe exemplul din
monografie. E o eroare care nu se vede în balanță, pentru că nota se echilibrează
oricum; se vede abia la control.

**Transportul intern intră în COST, dar NU în baza TVA vamală.** Amândouă sumele merg
pe 371, deci se confundă ușor:

    cost final    = 100.000 + 3.000 taxe + 2.000 transport = 105.000
    bază TVA vamă = 100.000 + 3.000 taxe                   = 103.000

Cine folosește 105.000 ca bază adaugă TVA pe un transport intern care are deja TVA-ul
lui pe factura transportatorului — și îl deduce de două ori.

## Starea terminală care contează

446.VAMA: rulaj debitor = rulaj creditor, sold zero. Un sold rămas înseamnă că
comisionarul a avansat TVA-ul și nu i s-a stins datoria — bani datorați cuiva care i-a
scos din buzunar.
"""
from .comun import formula_activ, sectiune_temei

COD = "MOD_IMPORT"

CATALOG = dict(
    fluxuri="F-15, F-16",
    tip="Pe declarație vamală",
    variabile="Valoarea mărfii, taxele vamale, transportul intern, cota TVA, calea "
              "(comisionar sau plată directă)",
    porti="Baza TVA = marfă + taxe vamale, fără transportul intern; 446.VAMA sold 0",
    blocuri="A Import prin comisionar (446.VAMA); B Import cu plată directă în vamă",
    ce_face="TVA vamală prin 446.VAMA sau plătită direct; taxele în costul stocului",
    cand="La fiecare DVI",
    activ="NU",
)

#: element, intră în costul stocului?, intră în baza TVA vamală?, observație
COMPOZITIE = [
    ("Valoarea mărfii de pe factura externă", "DA", "DA",
     "Convertită la cursul de la data DVI"),
    ("Taxe vamale", "DA", "DA",
     "Sunt parte din baza de impozitare la import"),
    ("Comisioane vamale, taxe de manipulare", "DA", "DA",
     "Dacă apar pe DVI, urmează același regim ca taxele"),
    ("Transport EXTERN, până la frontieră", "DA", "DA",
     "Intră în baza vamală dacă e până la primul loc de destinație din UE"),
    ("Transport INTERN, după vămuire", "DA", "NU",
     "Cost de achiziție, dar are TVA-ul lui pe factura transportatorului"),
    ("TVA-ul vamal însuși", "NU", "—",
     "Merge pe 4426, nu în costul stocului"),
]

#: cale, cine plătește TVA în vamă, cont folosit, stare terminală
CAI = [
    ("Prin comisionar", "Comisionarul avansează TVA-ul",
     "446.VAMA — intermediar, până la stingerea datoriei",
     "446.VAMA: rulaj D = rulaj C, sold 0"),
    ("Plată directă în vamă", "Firma, din contul propriu",
     "Fără intermediar — direct 4426 = 512",
     "401.EXT rămâne doar cu valoarea mărfii"),
]


#: (ce se sprijină pe el, temei) — secțiunea finală din `Reguli`.
TEMEI_LEGAL = [
    ('Baza de impozitare la import = valoarea în vamă + taxele vamale datorate',
     'art. 289 Cod fiscal'),
    ('Taxele vamale intră în costul de achiziție al stocului',
     'OMFP 1802/2014, pct. 8 — costul include taxele nerecuperabile'),
    ('Transportul intern e cost de achiziție, dar nu intră în baza vamală',
     'art. 289 CF (baza vamală) coroborat cu OMFP 1802/2014, pct. 8 (costul)'),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_IMPORT", {"A": 50, "B": 22, "C": 60})
    d.titlu("MOD_IMPORT — Declarații (input)")
    d.nota("Două căi alternative. De regulă se aplică una singură pe un import — pune "
           "DA pe cea folosită.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    d.kv("CUI", "=Parametri!B6", tip="calc")
    luna = d.kv("Luna (AAAA-LL)", "2026-07")
    data_j = d.kv("Data jurnal (DVI)", "2026-07-31")
    cota = d.kv("Cota TVA", 0.21)
    d.gol()

    d.sectiune("2. Calea A — Import prin comisionar")
    a_on = d.kv("Se aplică? (DA/NU)", "DA")
    a_furnizor = d.kv("Furnizor extern", "Furnizor EXT DEMO")
    a_comisionar = d.kv("Comisionar vamal", "Comisionar DEMO")
    a_marfa = d.kv("Valoarea mărfii (lei)", 100000,
                   nota="15.000–20.000 EUR × cursul de la data DVI")
    a_taxe = d.kv("Taxe vamale", 3000)
    a_transport = d.kv("Transport INTERN (după vămuire)", 2000,
                       nota="Intră în COST, dar NU în baza TVA vamală")
    a_baza = d.kv("Baza TVA vamală (auto) = marfă + taxe", f"={a_marfa}+{a_taxe}",
                  tip="calc",
                  nota="Fără transportul intern — acela are TVA-ul lui pe factura "
                       "transportatorului")
    a_tva = d.kv("TVA vamală (auto)", f"=ROUND({a_baza}*{cota},2)", tip="calc")
    a_cost = d.kv("Costul final al stocului (auto)",
                  f"={a_marfa}+{a_taxe}+{a_transport}", tip="calc")
    d.gol()

    d.sectiune("3. Calea B — Import cu plată directă în vamă")
    b_on = d.kv("Se aplică? (DA/NU)", "DA")
    b_furnizor = d.kv("Furnizor extern", "Furnizor EXT DEMO 2")
    b_marfa = d.kv("Valoarea mărfii (lei)", 50000)
    b_taxe = d.kv("Taxe vamale (plătite direct)", 2000)
    b_baza = d.kv("Baza TVA vamală (auto) = marfă + taxe", f"={b_marfa}+{b_taxe}",
                  tip="calc")
    b_tva = d.kv("TVA vamală (auto)", f"=ROUND({b_baza}*{cota},2)", tip="calc")
    b_cost = d.kv("Costul final al stocului (auto)", f"={b_marfa}+{b_taxe}", tip="calc")
    d.gol()

    d.sectiune("4. Conturi")
    c_stoc = d.kv("Cont stoc", "371")
    c_ext = d.kv("Furnizor extern", "401.EXT")
    c_vama = d.kv("Intermediar TVA vamală", "446.VAMA")
    c_comis = d.kv("Furnizor comisionar", "401")
    c_ro = d.kv("Furnizor intern / transport", "401.RO")
    c_4426 = d.kv("TVA deductibilă", "4426")
    c_banca = d.kv("Bancă", "512.1")
    d.gol()

    d.sectiune("5. Sufix")
    sufix = d.kv("Sufix", f'="— import " & {luna}', tip="calc")
    d.gol()

    d.sectiune("6. Control")
    d.kv("Modul activ?", formula_activ(COD), tip="calc")
    # Garda cea mai valoroasă: ce s-ar întâmpla dacă baza ar fi luată greșit.
    ver_baza = d.kv(
        "Verificare: baza TVA exclude transportul intern",
        f'=IF(OR({a_on}<>"DA",ABS({a_baza}-({a_cost}-{a_transport}))<0.01),'
        f'"OK — baza = marfă + taxe, fără transportul intern",'
        f'"EROARE — transportul intern a intrat în baza TVA")', tip="calc")
    d.kv("Cât ar costa greșeala (informativ)",
         f'=IF({a_on}="DA","TVA calculată pe cost în loc de bază: +" & '
         f'TEXT(ROUND({a_transport}*{cota},2),"0.00") & " lei dedusă de două ori",'
         f'"—")', tip="calc",
         nota="Transportul intern are deja TVA pe factura transportatorului")
    d.kv("Cale aleasă",
         f'=IF(AND({a_on}="DA",{b_on}="DA"),'
         f'"ATENȚIE — de regulă un import merge pe o singură cale",'
         f'IF({a_on}="DA","Prin comisionar — 446.VAMA se stinge",'
         f'IF({b_on}="DA","Plată directă — fără intermediar","—")))', tip="calc")

    # ------------------------------------------------------------------- Reguli
    g = F("Reguli_IMPORT", {"A": 44, "B": 16, "C": 22, "D": 58})
    g.titlu("MOD_IMPORT — Reguli (tabele fixe)")
    g.nota("Regula e dată, nu formulă. Tabelul A e cel care se citește cel mai des: "
           "spune ce intră unde.")
    g.gol()

    g.sectiune("Tabel A — Ce intră în cost și ce intră în baza TVA vamală")
    g.cap(["Element", "În cost?", "În baza TVA?", "Observație"])
    for rand in COMPOZITIE:
        g.rand(list(rand))
    g.nota("Cele două coloane NU coincid. Transportul intern e singurul element care "
           "intră în cost fără să intre în bază — acolo se face greșeala.")
    g.gol()

    g.sectiune("Tabel B — Cele două căi")
    g.cap(["Cale", "Cine plătește TVA în vamă", "Cont folosit", "Stare terminală"])
    for rand in CAI:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel C — Porți de calitate")
    for linie in [
        "• ΣDr = ΣCr pe fiecare bloc",
        "• Baza TVA vamală = valoarea mărfii + taxele vamale, NU costul complet",
        "• 446.VAMA: rulaj debitor = rulaj creditor, sold 0. Un sold rămas înseamnă "
        "datorie nestinsă față de comisionarul care a avansat TVA-ul",
        "• 401.EXT rămâne doar cu valoarea mărfii — taxele și TVA-ul nu se datorează "
        "furnizorului extern",
        "• TVA-ul vamal merge pe 4426 și se închide lunar ca oricare altul (vezi "
        "MOD_INCHIDERE_TVA); nu intră niciodată în costul stocului",
    ]:
        g.nota(linie)

    sectiune_temei(g, TEMEI_LEGAL)

    # ------------------------------------------------------------------ Jurnale
    j = F("Jurnale_IMPORT",
          {"A": 36, "B": 16, "C": 14, "D": 52, "E": 16, "F": 14, "G": 52})
    j.titlu("MOD_IMPORT — Jurnale (generate automat)")
    j.nota("Calea A are exact două note pentru TVA-ul vamal: una îl aduce pe 4426 prin "
           "intermediar, alta stinge intermediarul. Sărită a doua, 446.VAMA rămâne "
           "deschis la infinit.")
    j.gol()

    D = d.ref
    antet = ["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr",
             "Descriere Cr"]

    def daca(comutator, valoare):
        return f'=IF({D(comutator)}="DA",{D(valoare)},0)'

    j.sectiune("Bloc A — Import prin comisionar")
    j.kv("Data:", f"={D(data_j)}", tip="calc")
    j.cap(antet)
    a1 = j.rand([1, f"={D(c_stoc)}", daca(a_on, a_marfa),
                 f'="Marfă din import (doar valoarea externă) " & {D(sufix)}',
                 f"={D(c_ext)}", daca(a_on, a_marfa),
                 f'="Datorie furnizor extern " & {D(sufix)}'])
    ca1 = j.check("Check A1 (factura externă)", f"={a1['C']}-{a1['F']}",
                  f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    a2 = j.rand([2, f"={D(c_4426)}", daca(a_on, a_tva),
                 f'="TVA vamală, avansată de comisionar " & {D(sufix)}',
                 f"={D(c_vama)}", daca(a_on, a_tva),
                 f'="Intermediar 446.VAMA (pas revelator) " & {D(sufix)}'])
    ca2 = j.check("Check A2 (TVA prin intermediar)", f"={a2['C']}-{a2['F']}",
                  f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    a3 = j.rand([3, f"={D(c_vama)}", daca(a_on, a_tva),
                 f'="Stingerea intermediarului " & {D(sufix)}',
                 f"={D(c_comis)}", daca(a_on, a_tva),
                 f'="Datorie reală față de comisionar " & {D(sufix)}'])
    ca3 = j.check("Check A3 (stingerea intermediarului)", f"={a3['C']}-{a3['F']}",
                  f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    a4 = j.rand([4, f"={D(c_stoc)}", daca(a_on, a_taxe),
                 f'="Taxe vamale în costul stocului " & {D(sufix)}',
                 f"={D(c_ro)}", daca(a_on, a_taxe),
                 f'="Datorie taxe vamale " & {D(sufix)}'])
    a5 = j.rand([5, f"={D(c_stoc)}", daca(a_on, a_transport),
                 f'="Transport intern în cost (NU în baza TVA) " & {D(sufix)}',
                 f"={D(c_ro)}", daca(a_on, a_transport),
                 f'="Datorie transportator " & {D(sufix)}'])
    ca4 = j.check("Check A4 (taxe + transport în cost)",
                  f"=({a4['C']}+{a5['C']})-({a4['F']}+{a5['F']})",
                  f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    # Starea terminală a intermediarului, verificată pe rulaje, nu presupusă.
    ca5 = j.check("Check A5 (446.VAMA sold 0)",
                  f"={a2['F']}-{a3['C']}",
                  f'=IF(ABS(B{j.r})<0.01,"OK — 446.VAMA rulaj D = rulaj C, sold 0",'
                  f'"EROARE — intermediarul rămâne deschis")')
    j.gol()

    j.sectiune("Bloc B — Import cu plată directă în vamă")
    j.cap(antet)
    b1 = j.rand([1, f"={D(c_stoc)}", daca(b_on, b_marfa),
                 f'="Marfă din import " & {D(sufix)}',
                 f"={D(c_ext)}", daca(b_on, b_marfa),
                 f'="Datorie furnizor extern " & {D(sufix)}'])
    cb1 = j.check("Check B1 (factura externă)", f"={b1['C']}-{b1['F']}",
                  f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    b2 = j.rand([2, f"={D(c_stoc)}", daca(b_on, b_taxe),
                 f'="Taxe vamale plătite direct, în cost " & {D(sufix)}',
                 f"={D(c_banca)}", daca(b_on, b_taxe),
                 f'="Ieșire bancă " & {D(sufix)}'])
    cb2 = j.check("Check B2 (taxe vamale)", f"={b2['C']}-{b2['F']}",
                  f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    b3 = j.rand([3, f"={D(c_4426)}", daca(b_on, b_tva),
                 f'="TVA vamală plătită direct " & {D(sufix)}',
                 f"={D(c_banca)}", daca(b_on, b_tva),
                 f'="Ieșire bancă " & {D(sufix)}'])
    cb3 = j.check("Check B3 (TVA vamală)", f"={b3['C']}-{b3['F']}",
                  f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    glob = j.check(
        "Check global",
        f"=ABS({ca1})+ABS({ca2})+ABS({ca3})+ABS({ca4})+ABS({ca5})"
        f"+ABS({cb1})+ABS({cb2})+ABS({cb3})",
        f'=IF(B{j.r}<0.01,"OK — toate blocurile se închid",'
        f'"EROARE — cel puțin un bloc dezechilibrat")')
    j.gol()
    j.sectiune("Stare terminală")
    j.nota("Calea A: 446.VAMA sold 0, stoc la 105.000 (marfă + taxe + transport), TVA "
           "21.630 pe 4426, datorie 100.000 către furnizorul extern și 21.630 către "
           "comisionar. Calea B: stoc 52.000, TVA 10.920 pe 4426, 401.EXT doar 50.000 — "
           "fără intermediar, pentru că nimeni n-a avansat nimic.")

    # --------------------------------------------------------------- NotaExport
    e = F("NotaExport_IMPORT",
          {"A": 6, "B": 30, "C": 14, "D": 12, "E": 12, "F": 14, "G": 52, "H": 22,
           "I": 10})
    e.titlu("MOD_IMPORT — Notă pentru import")
    e.nota("Filtrează Include=DA. Calea neactivată iese cu sumă 0 și apare ca NU.")
    e.gol()
    e.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    primul = e.r
    for i, (bloc, r, doc) in enumerate([
        ("A Comisionar — marfa", a1, "Factură externă"),
        ("A Comisionar — TVA vamală", a2, "DVI"),
        ("A Comisionar — stingere 446", a3, "Factură comisionar"),
        ("A Comisionar — taxe vamale", a4, "DVI"),
        ("A Comisionar — transport intern", a5, "Factură transport"),
        ("B Direct — marfa", b1, "Factură externă"),
        ("B Direct — taxe vamale", b2, "DVI + extras"),
        ("B Direct — TVA vamală", b3, "DVI + extras"),
    ], start=1):
        e.rand([i, bloc, f"={D(data_j)}", f"={j.ref(r['B'])}", f"={j.ref(r['E'])}",
                f"={j.ref(r['C'])}", f"={j.ref(r['D'])}", doc,
                f'=IF(AND(ISNUMBER(F{e.r}),F{e.r}>0),"DA","NU")'])
    ultim = e.r - 1
    e.gol()
    e.kv("Rânduri de importat", f'=COUNTIF(I{primul}:I{ultim},"DA")', tip="calc")
    e.check("Check global", f"={j.ref(glob)}",
            f'=IF(ABS(B{e.r})<0.01,"OK","EROARE")')
