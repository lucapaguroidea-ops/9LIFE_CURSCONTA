"""MOD_FARA_DOCUMENT — două cazuri în care TVA nu urmează regula obișnuită.

Acoperă F-22.

Numele vine din notițe și e ușor înșelător: nu e vorba că lipsește documentul, ci că
documentul nu-ți dă dreptul obișnuit. La vehiculul cu regim mixt ai factură, dar deduci
doar jumătate din TVA. La lipsa nejustificată nu ai nicio ieșire de marfă documentată,
dar ai obligația să colectezi ca și cum ai fi vândut.

## Cele două principii, din notițe

**(1) TVA nedeductibilă se INCORPOREAZĂ în cheltuială.** Nu se pierde și nu rămâne
suspendată: jumătatea nedeductibilă e cost, ca oricare altul. Cine o lasă pe 4426 va
avea un sold care nu se închide la finalul lunii; cine o aruncă rămâne cu o notă
dezechilibrată.

    factură 1.000 + TVA 210 → 628 = 1.105 (1.000 + 105) și 4426 = 105

**(2) La lipsă nejustificată, 4427 se CREDITEAZĂ.** Reflexul „am dedus TVA la
achiziție, deci acum o storneez" e greșeală de sens. Legea nu-ți cere să anulezi
deducerea, îți cere să **colectezi** — bunul se tratează ca și cum ar fi fost livrat.
Debitarea lui 4427 ar reduce TVA-ul colectat al lunii, adică exact invers decât trebuie.

Nu e o subtilitate: primul caz se lovește lunar la orice firmă cu mașină, al doilea la
fiecare inventar cu minus.
"""
from .comun import formula_activ

COD = "MOD_FARA_DOCUMENT"

CATALOG = dict(
    fluxuri="F-22",
    tip="Pe eveniment",
    variabile="Valoare factură și cota, pentru vehicul; costul lipsei la inventar",
    porti="Procentul de deducere vine din param_proc_vehicul; 4427 se creditează la lipsă",
    blocuri="A Vehicul cu regim mixt (50%); B Lipsă la inventar nejustificată",
    ce_face="TVA nedeductibilă în cheltuială; colectare la lipsa nejustificată",
    cand="Lunar la cheltuielile auto; la fiecare inventar cu minus",
    activ="NU",
)

#: caz, ce se întâmplă cu TVA, unde ajunge partea nedeductibilă, temei
CAZURI = [
    ("Vehicul cu regim MIXT (personal + business)", "se deduce 50%",
     "jumătatea nedeductibilă intră în cheltuială",
     "art. 298 CF (TVA) și art. 25 alin. (3) lit. l) CF (cheltuieli)"),
    ("Vehicul folosit EXCLUSIV în scop economic", "se deduce 100%",
     "nimic — TVA e integral deductibilă",
     "cere foaie de parcurs care să dovedească utilizarea exclusivă"),
    ("Vehicul EXCEPTAT (taxi, școală de șoferi, intervenție, agenți de vânzări…)",
     "se deduce 100%", "nimic", "art. 298 alin. (2) CF — enumerare limitativă"),
    ("Lipsă la inventar NEJUSTIFICATĂ", "se COLECTEAZĂ pe valoarea bunului",
     "cheltuiala e valoarea bunului; TVA colectată e separată",
     "bunul se tratează ca livrat către sine"),
    ("Lipsă JUSTIFICATĂ (calamitate, perisabilități în limită, casare documentată)",
     "nu se colectează", "—", "trebuie documentată, altfel intră la nejustificată"),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_FARA_DOCUMENT", {"A": 50, "B": 22, "C": 58})
    d.titlu("MOD_FARA_DOCUMENT — Declarații (input)")
    d.nota("Două cazuri independente. Pune DA pe cel care s-a întâmplat — de obicei "
           "primul se aplică lunar, al doilea doar după inventar.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    d.kv("CUI", "=Parametri!B6", tip="calc")
    luna = d.kv("Luna (AAAA-LL)", "2026-07")
    data_j = d.kv("Data jurnal", "2026-07-31")
    cota = d.kv("Cota TVA", 0.21)
    d.gol()

    d.sectiune("2. Cazul A — Vehicul cu regim mixt (deducere 50%)")
    a_on = d.kv("Se aplică? (DA/NU)", "DA")
    a_regim = d.kv("Regim (MIXT / EXCLUSIV / EXCEPTAT)", "MIXT")
    a_net = d.kv("Valoare factură fără TVA", 1000)
    a_tva = d.kv("TVA de pe factură (auto)", f"=ROUND({a_net}*{cota},2)", tip="calc")
    a_proc = d.kv("Procent de deducere (auto)",
                  f'=IF({a_regim}="MIXT",{P["proc_vehicul"]},1)', tip="calc",
                  nota="La MIXT vine din param_proc_vehicul; la EXCLUSIV și EXCEPTAT "
                       "se deduce integral")
    a_ded = d.kv("TVA deductibilă (auto)", f"=ROUND({a_tva}*{a_proc},2)", tip="calc")
    a_neded = d.kv("TVA nedeductibilă (auto)", f"={a_tva}-{a_ded}", tip="calc")
    a_chelt = d.kv("Cheltuială = net + TVA nedeductibilă (auto)",
                   f"={a_net}+{a_neded}", tip="calc",
                   nota="TVA nedeductibilă NU se pierde: se incorporează în cheltuială")
    a_total = d.kv("Total factură (auto)", f"={a_net}+{a_tva}", tip="calc")
    d.gol()

    d.sectiune("3. Cazul B — Lipsă la inventar")
    b_on = d.kv("Se aplică? (DA/NU)", "DA")
    b_justificata = d.kv("Lipsa e JUSTIFICATĂ? (DA/NU)", "NU",
                         nota="Calamitate, perisabilități în limita legală, casare "
                              "documentată. Nejustificată = se colectează TVA")
    b_cost = d.kv("Costul bunului lipsă", 1200)
    b_tva = d.kv("TVA de colectat (auto)",
                 f'=IF({b_justificata}="DA",0,ROUND({b_cost}*{cota},2))', tip="calc")
    d.gol()

    d.sectiune("4. Conturi")
    c_628 = d.kv("Cheltuială cu serviciile (628)", "628")
    c_658 = d.kv("Alte cheltuieli de exploatare (658)", "658")
    c_401 = d.kv("Furnizor", "401")
    c_stoc = d.kv("Cont stoc", "371")
    c_4426 = d.kv("TVA deductibilă", "4426")
    c_4427 = d.kv("TVA colectată", "4427")
    d.gol()

    d.sectiune("5. Sufix")
    sufix = d.kv("Sufix", f'="— fără document " & {luna}', tip="calc")
    d.gol()

    d.sectiune("6. Control")
    d.kv("Modul activ?", formula_activ(COD), tip="calc")
    # Garda 1 — principiul (1) din notițe, verificat pe cifre: nimic nu se pierde.
    ver_total = d.kv(
        "Verificare: cheltuială + TVA dedusă = total factură",
        f'=IF(OR({a_on}<>"DA",ABS(({a_chelt}+{a_ded})-{a_total})<0.01),'
        f'"OK — TVA nedeductibilă e în cheltuială, nimic nu se pierde",'
        f'"EROARE — nota nu acoperă totalul facturii")', tip="calc")
    # Garda 2 — principiul (2): sensul lui 4427. Se verifică în jurnal, unde se vede
    # pe ce parte stă suma; aici se scrie ce trebuie să se întâmple.
    d.kv("Regula de sens la lipsă",
         f'=IF(AND({b_on}="DA",{b_justificata}<>"DA"),'
         f'"4427 se CREDITEAZĂ — colectezi, nu storna deducerea",'
         f'"—")', tip="calc")

    # ------------------------------------------------------------------- Reguli
    g = F("Reguli_FARA_DOCUMENT", {"A": 54, "B": 32, "C": 44, "D": 52})
    g.titlu("MOD_FARA_DOCUMENT — Reguli (tabele fixe)")
    g.nota("Regula e dată, nu formulă. Se editează doar când se schimbă legea.")
    g.gol()

    g.sectiune("Tabel A — Regimuri și tratamente")
    g.cap(["Caz", "TVA", "Partea nedeductibilă", "Temei / condiție"])
    for rand in CAZURI:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel B — Cele două principii")
    for linie in [
        "(1) TVA nedeductibilă se INCORPOREAZĂ în cheltuială. Nu se pierde și nu rămâne "
        "pe 4426 — acolo ar produce un sold care nu se închide la finalul lunii.",
        "(2) La lipsă nejustificată, 4427 se CREDITEAZĂ. Legea nu cere anularea "
        "deducerii, cere COLECTAREA: bunul se tratează ca livrat. Debitarea lui 4427 ar "
        "reduce TVA-ul colectat al lunii — exact invers decât trebuie.",
    ]:
        g.nota(linie)
    g.gol()

    g.sectiune("Tabel C — Porți de calitate")
    for linie in [
        "• ΣDr = ΣCr pe fiecare bloc",
        "• Cheltuială + TVA dedusă = totalul facturii (1.105 + 105 = 1.210)",
        "• La regim MIXT se deduce exact procentul din param_proc_vehicul, nu unul scris "
        "în celulă",
        "• La lipsă nejustificată, suma stă pe CREDITUL lui 4427",
        "• Limitarea de 50% la TVA nu se cumulează cu plafonul de amortizare auto — sunt "
        "două mecanisme diferite (vezi param_plafon_amo_auto)",
    ]:
        g.nota(linie)

    # ------------------------------------------------------------------ Jurnale
    j = F("Jurnale_FARA_DOCUMENT",
          {"A": 38, "B": 16, "C": 14, "D": 52, "E": 16, "F": 14, "G": 52})
    j.titlu("MOD_FARA_DOCUMENT — Jurnale (generate automat)")
    j.nota("Blocul A e un articol compus: două debite (cheltuiala majorată și TVA "
           "dedusă) contra unui singur credit, totalul facturii.")
    j.gol()

    D = d.ref
    antet = ["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr",
             "Descriere Cr"]

    def daca(comutator, valoare):
        return f'=IF({D(comutator)}="DA",{D(valoare)},0)'

    j.sectiune("Bloc A — Vehicul cu regim mixt")
    j.kv("Data:", f"={D(data_j)}", tip="calc")
    j.cap(antet)
    a1 = j.rand([1, f"={D(c_628)}", daca(a_on, a_chelt),
                 f'="Cheltuială + TVA nedeductibilă " & {D(sufix)}',
                 f"={D(c_401)}", daca(a_on, a_total),
                 f'="Datorie furnizor (total factură) " & {D(sufix)}'])
    a2 = j.rand([2, f"={D(c_4426)}", daca(a_on, a_ded),
                 f'="TVA deductibilă (procentul admis) " & {D(sufix)}', 0, 0])
    ca = j.check("Check A (cheltuială + TVA dedusă = total)",
                 f"=({a1['C']}+{a2['C']})-{a1['F']}",
                 f'=IF(ABS(B{j.r})<0.01,"OK — nimic nu se pierde","EROARE")')
    j.gol()

    # Lipsa produce DOUĂ note independente, nu un articol compus: cheltuiala descarcă
    # stocul, iar TVA-ul colectat nu are contrapartidă în stoc — se naște o datorie.
    j.sectiune("Bloc B — Lipsă la inventar nejustificată")
    j.cap(antet)
    b1 = j.rand([1, f"={D(c_658)}", daca(b_on, b_cost),
                 f'="Cheltuială cu lipsa la inventar " & {D(sufix)}',
                 f"={D(c_stoc)}", daca(b_on, b_cost),
                 f'="Descărcarea stocului lipsă " & {D(sufix)}'])
    cb1 = j.check("Check B1 (descărcarea stocului)", f"={b1['C']}-{b1['F']}",
                  f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    b2 = j.rand([2, f"={D(c_658)}", daca(b_on, b_tva),
                 f'="TVA colectată pe lipsă (NU stornare de deducere) " & {D(sufix)}',
                 f"={D(c_4427)}", daca(b_on, b_tva),
                 f'="TVA colectată — bunul se tratează ca livrat " & {D(sufix)}'])
    # Nu se compară sumele: rândul e echilibrat prin construcție, deci diferența lor e
    # zero orice s-ar întâmpla — ar fi o gardă decorativă. Se verifică CONTUL de pe
    # partea de credit: dacă cineva inversează sensul, acolo se vede.
    cb2 = j.check("Check B2 (4427 pe partea de CREDIT)",
                  f'=IF({b2["E"]}={D(c_4427)},0,1)',
                  f'=IF(B{j.r}=0,"OK — 4427 creditat, cum trebuie",'
                  f'"EROARE — 4427 nu e pe credit: la lipsă se colectează, nu se '
                  f'stornează deducerea")')
    j.gol()

    glob = j.check("Check global", f"=ABS({ca})+ABS({cb1})+ABS({cb2})",
                   f'=IF(B{j.r}<0.01,"OK — toate blocurile se închid",'
                   f'"EROARE — cel puțin un bloc dezechilibrat")')
    j.gol()
    j.sectiune("Stare terminală")
    j.nota("Pe 4426 intră doar partea deductibilă; restul e cost și nu mai apare "
           "nicăieri ca TVA. Pe 4427 intră TVA-ul colectat pe lipsă, care majorează "
           "TVA-ul de plată al lunii — nu îl reduce.")

    # --------------------------------------------------------------- NotaExport
    e = F("NotaExport_FARA_DOCUMENT",
          {"A": 6, "B": 30, "C": 14, "D": 12, "E": 12, "F": 14, "G": 52, "H": 26,
           "I": 10})
    e.titlu("MOD_FARA_DOCUMENT — Notă pentru import")
    e.nota("Filtrează Include=DA. Cazurile neactivate ies cu sumă 0 și apar ca NU.")
    e.gol()
    e.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    primul = e.r
    for i, (bloc, cd, cc, suma, desc, doc) in enumerate([
        ("A Auto — cheltuiala", a1["B"], a1["E"], a1["C"], a1["D"], "Factură"),
        ("A Auto — TVA dedusă", a2["B"], a1["E"], a2["C"], a2["D"], "Factură"),
        ("B Lipsă — cheltuiala", b1["B"], b1["E"], b1["C"], b1["D"],
         "Proces-verbal inventar"),
        ("B Lipsă — TVA colectată", b2["B"], b2["E"], b2["C"], b2["D"],
         "Proces-verbal inventar"),
    ], start=1):
        e.rand([i, bloc, f"={D(data_j)}", f"={j.ref(cd)}", f"={j.ref(cc)}",
                f"={j.ref(suma)}", f"={j.ref(desc)}", doc,
                f'=IF(AND(ISNUMBER(F{e.r}),F{e.r}>0),"DA","NU")'])
    ultim = e.r - 1
    e.gol()
    e.kv("Rânduri de importat", f'=COUNTIF(I{primul}:I{ultim},"DA")', tip="calc")
    e.check("Check global", f"={j.ref(glob)}",
            f'=IF(ABS(B{e.r})<0.01,"OK","EROARE")')
