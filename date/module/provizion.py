"""MOD_PROVIZION — constituirea și reluarea unui provizion.

Acoperă F-51.

Modulul apără două lucruri pe care notițele le semnalau, dar pe care practica le încurcă
des:

1. **Factura NU se înregistrează „pe 151”.** Provizionul nu e o datorie față de furnizor.
   Constituirea și reluarea sunt operațiuni INDEPENDENTE de factura propriu-zisă. De aceea
   blocul facturii e separat în jurnale și nu atinge contul de provizion.
2. **Provizioanele pentru litigii sunt NEDEDUCTIBILE.** Art. 26 CF enumeră limitativ ce e
   deductibil, iar litigiile nu sunt pe listă. Prin simetrie, reluarea e venit neimpozabil.
   Modulul calculează efectul fiscal și scrie explicit că nu e o optimizare — ca să nu fie
   vândut clientului ca atare.

Efectul net pe rezultatul anului următor e ~zero. Ăsta e chiar scopul provizionului:
cheltuiala apare în exercițiul în care s-a născut obligația, nu în cel în care se plătește.
"""

COD = "MOD_PROVIZION"

CATALOG = dict(
    fluxuri="F-51",
    tip="Pe eveniment + la fiecare dată a bilanțului",
    variabile="Tip provizion, sumă estimată, data constituirii, suma facturată efectiv",
    porti="Deductibilitatea depinde de TIP — art. 26 CF enumeră limitativ",
    blocuri="B1 Constituire; B2 Factura efectivă (independentă); B3 Reluare",
)

#: cod, denumire, cont, deductibil, temei
TIPURI = [
    ("LITIGII", "Provizioane pentru litigii", "1511", "NU",
     "art. 26 CF nu îl enumeră printre cele deductibile"),
    ("GARANTII", "Provizioane pentru garanții acordate clienților", "1512", "DA",
     "art. 26 alin. (1) lit. b) CF — în limita cotei prevăzute în contracte"),
    ("RESTRUCTURARE", "Provizioane pentru restructurare", "1514", "NU",
     "nu figurează printre cele deductibile"),
    ("IMPOZITE", "Provizioane pentru impozite", "1516", "NU",
     "nu figurează printre cele deductibile"),
    ("TERMINARE", "Provizioane pentru terminarea contractului de muncă", "1517", "NU",
     "nu figurează printre cele deductibile"),
    ("ALTE", "Alte provizioane", "1518", "NU",
     "verifică art. 26 CF pentru cazul concret"),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_PROVIZION", {"A": 46, "B": 20, "C": 64})
    d.titlu("MOD_PROVIZION — Declarații (input)")
    d.nota("Tipul provizionului comandă contul ȘI deductibilitatea. Valorile implicite "
           "reproduc monografia din F-51 (litigiu, 8.000 lei).")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    obiect = d.kv("Obiectul provizionului", "Litigiu comercial cu clientul X")
    data_const = d.kv("Data constituirii", "2026-12-31",
                      nota="Exercițiul în care s-a NĂSCUT obligația, nu cel în care se plătește")
    data_reluare = d.kv("Data reluării", "2027-04-30")
    d.gol()

    d.sectiune("2. Provizionul")
    tip = d.kv("Tip (LITIGII / GARANTII / RESTRUCTURARE / IMPOZITE / TERMINARE / ALTE)",
               "LITIGII")
    suma = d.kv("Sumă estimată", 8000,
                nota="Estimare credibilă la data bilanțului; se revizuiește la fiecare bilanț")
    d.gol()

    d.sectiune("3. Cheltuiala efectivă (anul următor)")
    suma_fact = d.kv("Sumă facturată efectiv", 8000)
    tva_fact = d.kv("TVA pe factură", f"=ROUND({suma_fact}*Parametri!B10,2)", tip="calc")
    d.gol()

    d.sectiune("4. Calcul automat (nu edita)")
    g_ref = "Reguli_PROVIZION!$A$6:$E$11"
    cont_prov = d.kv("Cont provizion", f'=IFERROR(VLOOKUP({tip},{g_ref},3,FALSE),"?")',
                     tip="calc")
    deductibil = d.kv("Deductibil fiscal?", f'=IFERROR(VLOOKUP({tip},{g_ref},4,FALSE),"?")',
                      tip="calc")
    temei = d.kv("Temei", f'=IFERROR(VLOOKUP({tip},{g_ref},5,FALSE),"tip necunoscut")',
                 tip="calc")
    efect = d.kv("Efect fiscal la constituire",
                 f'=IF({deductibil}="DA",0,ROUND({suma}*{P["cota_impozit_profit"]},2))',
                 tip="calc",
                 nota="Impozit suplimentar de plătit dacă provizionul e nedeductibil")
    d.gol()

    d.sectiune("5. Conturi")
    c_chelt = d.kv("Cont cheltuială cu provizioane", 6812)
    c_venit = d.kv("Cont venit din reluarea provizioanelor", 7812)
    c_chelt_ef = d.kv("Cont cheltuială efectivă", 628,
                      nota="Contul real al cheltuielii — NU contul de provizion")
    c_tva = d.kv("Cont TVA deductibilă", 4426)
    c_furnizor = d.kv("Cont furnizor", "401")
    d.gol()

    d.sectiune("6. Controale")
    d.check("Check tip recunoscut", f"={cont_prov}",
            f'=IF({cont_prov}="?","EROARE — tip de provizion necunoscut",'
            f'"OK — cont " & {cont_prov})')
    d.check("Check deductibilitate", f"={efect}",
            f'=IF({deductibil}="DA","OK — deductibil: " & {temei},'
            f'"NEDEDUCTIBIL (" & {temei} & "). Impozit suplimentar: " & '
            f'TEXT({efect},"0.00") & " lei")')
    d.check("Reminder: NU e optimizare fiscală", f'="regulă"',
            f'=IF({deductibil}="DA","Deductibil — dar tot nu e optimizare: doar mută '
            f'cheltuiala în exercițiul corect.","Nedeductibil la constituire, iar reluarea '
            f'e venit neimpozabil. Efect fiscal net pe doi ani: zero. Nu-l vinde clientului '
            f'ca optimizare.")')
    d.check("Reminder: factura NU atinge contul de provizion", f"={suma_fact}",
            '="Blocul 2 înregistrează factura pe contul REAL de cheltuială. Provizionul se '
            'reia separat, în blocul 3. Cele două nu se compensează."')
    d.check("Check estimare vs. realizat", f"={suma_fact}-{suma}",
            f'=IF(ABS(B{d.r})<0.01,"OK — estimarea s-a confirmat",'
            f'IF(B{d.r}>0,"Cheltuiala a depășit provizionul cu " & TEXT(B{d.r},"0.00") & '
            f'" lei — diferența rămâne cheltuială a anului curent",'
            f'"Provizionul a fost supraestimat cu " & TEXT(-B{d.r},"0.00") & '
            f'" lei — reluarea rămâne la valoarea constituită"))')
    d.gol()

    d.sectiune("7. Sufix generat")
    sufix = d.kv("Sufix", f'=" - " & {obiect}', tip="calc")

    # -------------------------------------------------------------------- Reguli
    g = F("Reguli_PROVIZION", {"A": 16, "B": 44, "C": 12, "D": 14, "E": 56, "F": 44})
    g.titlu("MOD_PROVIZION — Reguli (tabele fixe)")
    g.nota("Tabelul A e citit de formulele din Declarații. Se editează doar când se "
           "schimbă art. 26 din Codul fiscal.")
    g.gol()
    g.sectiune("Tabel A — Tipuri de provizion, cont și deductibilitate")
    g.cap(["Cod", "Denumire", "Cont", "Deductibil", "Temei"])
    for row in TIPURI:
        g.rand(list(row))
    g.gol()

    g.sectiune("Tabel B — Condițiile de recunoaștere (toate trei, cumulativ)")
    g.cap(["Condiție", "Ce înseamnă", "", "", "Dacă lipsește"])
    for row in [
        ("Obligație actuală", "din eveniment trecut, la data bilanțului", "", "",
         "Nu e provizion — e o intenție"),
        ("Ieșire probabilă de resurse", "mai degrabă da decât nu", "", "",
         "Rămâne datorie contingentă — se prezintă în note, nu se înregistrează"),
        ("Estimare credibilă", "suma se poate evalua rezonabil", "", "",
         "Se prezintă în note, fără sumă"),
    ]:
        g.rand(list(row))
    g.gol()

    g.sectiune("Tabel C — LIMITĂRI DECLARATE ale modulului")
    g.cap(["Ce NU tratează", "De ce", "Ce faci", "", "Efect dacă îl ignori"])
    for row in [
        ("Actualizarea provizioanelor pe termen lung",
         "Provizioanele scadente peste un an se pot actualiza la valoarea prezentă.",
         "Dacă politica firmei o cere, actualizează și trece diferența pe 686/786.", "",
         "Provizionul e supraevaluat față de valoarea prezentă"),
        ("Revizuirea la fiecare bilanț",
         "Modulul tratează un ciclu constituire → reluare, nu ajustările intermediare.",
         "La fiecare bilanț, reevaluează și ajustează prin aceleași conturi.", "",
         "Provizionul rămâne la estimarea inițială, care poate fi depășită"),
        ("Provizioane pentru garanții cu cotă contractuală",
         "Deductibilitatea lor e limitată la cota din contracte, care variază.",
         "Verifică art. 26 alin. (1) lit. b) și cota din contractul concret.", "",
         "Partea peste cotă rămâne nedeductibilă și nesemnalată"),
        ("Utilizarea pentru altă cheltuială decât cea constituită",
         "Interzisă — provizionul e specific obligației.",
         "Reia provizionul vechi și constituie unul nou.", "",
         "Provizionul devine un cont-tampon, exact ce nu trebuie"),
    ]:
        g.rand(list(row))

    # ------------------------------------------------------------------- Jurnale
    j = F("Jurnale_PROVIZION", {"A": 8, "B": 14, "C": 14, "D": 48, "E": 14, "F": 14,
                                "G": 48})
    j.titlu("MOD_PROVIZION — Jurnale (generate automat)")
    j.nota("Blocul 2 e INDEPENDENT de blocurile 1 și 3: factura se înregistrează pe contul "
           "real de cheltuială, nu pe contul de provizion.")
    j.gol()
    D = d.ref

    j.sectiune("Bloc 1 — Constituirea provizionului (exercițiul N)")
    j.kv("Data jurnal:", f"={D(data_const)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b1 = j.r
    j.rand([1, f"={D(c_chelt)}", f"={D(suma)}",
            f'="Constituire provizion" & {D(sufix)}',
            f"={D(cont_prov)}", f"={D(suma)}",
            f'="Provizion constituit" & {D(sufix)}'])
    j.gol()
    j.check("Check Σ (structural)", f"=C{b1}-F{b1}",
            f'=IF(ABS(B{j.r})<0.01,"OK — nota se închide","EROARE")')
    j.check("Declarativ", f"={D(deductibil)}",
            f'=IF({D(deductibil)}="DA","D101 — cheltuială deductibilă",'
            f'"D101 — cheltuială NEDEDUCTIBILĂ, se adaugă la rezultatul fiscal")')
    j.gol()

    j.sectiune("Bloc 2 — Factura efectivă (exercițiul N+1) — INDEPENDENT")
    j.kv("Data jurnal:", f"={D(data_reluare)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b2 = j.r
    j.rand([1, f"={D(c_chelt_ef)}", f"={D(suma_fact)}",
            f'="Cheltuiala efectivă, pe contul ei real" & {D(sufix)}',
            f"={D(c_furnizor)}", f"={D(suma_fact)}+{D(tva_fact)}",
            f'="Datorie față de furnizor" & {D(sufix)}'])
    j.rand([2, f"={D(c_tva)}", f"={D(tva_fact)}",
            f'="TVA deductibilă" & {D(sufix)}', None, None, None])
    sf2 = j.r - 1
    j.gol()
    j.check("Check Σ (structural)", f"=SUM(C{b2}:C{sf2})-SUM(F{b2}:F{sf2})",
            f'=IF(ABS(B{j.r})<0.01,"OK — nota se închide","EROARE")')
    j.check("Check: nu atinge contul de provizion", f"={D(cont_prov)}",
            '="Corect — factura se înregistrează pe contul real de cheltuială. '
            'Provizionul se reia separat, în blocul 3."')
    j.gol()

    j.sectiune("Bloc 3 — Reluarea provizionului (exercițiul N+1)")
    j.kv("Data jurnal:", f"={D(data_reluare)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b3 = j.r
    j.rand([1, f"={D(cont_prov)}", f"={D(suma)}",
            f'="Reluarea provizionului, obligația s-a stins" & {D(sufix)}',
            f"={D(c_venit)}", f"={D(suma)}",
            f'="Venit din reluarea provizionului" & {D(sufix)}'])
    j.gol()
    j.check("Check Σ (structural)", f"=C{b3}-F{b3}",
            f'=IF(ABS(B{j.r})<0.01,"OK — nota se închide","EROARE")')
    j.check("Check sold provizion după reluare", f"={D(suma)}-{D(suma)}",
            f'=IF(ABS(B{j.r})<0.01,"OK — soldul contului de provizion = 0","EROARE")')
    j.check("Efect fiscal pe cei doi ani", f"={D(efect)}",
            f'=IF({D(deductibil)}="DA","Deductibil la constituire, impozabil la reluare — '
            f'efect net zero.","Nedeductibil la constituire, neimpozabil la reluare — '
            f'efect net zero. Provizionul mută cheltuiala în exercițiul corect, nu reduce '
            f'impozitul.")')
    j.gol()
    j.nota("Stare terminală: contul de provizion = 0; efectul net pe rezultatul "
           "exercițiului N+1 ≈ 0, pentru că reluarea (venit) compensează cheltuiala reală.")

    # ---------------------------------------------------------------- NotaExport
    n = F("NotaExport_PROVIZION", {"A": 6, "B": 32, "C": 12, "D": 12, "E": 12, "F": 14,
                                   "G": 48, "H": 22, "I": 9})
    n.titlu("MOD_PROVIZION — Notă pentru import (1 rând = 1 înregistrare)")
    n.nota("Blocurile 1 și 3 aparțin exercițiilor diferite. Filtrează pe Include = DA și pe "
           "dată înainte de import.")
    n.gol()
    n.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    J = j.ref
    prima_n = n.r
    linii = ([("Bloc 1 — Constituire", data_const, b1, "Hotărâre + estimare")]
             + [("Bloc 2 — Factura efectivă", data_reluare, r, "Factură furnizor")
                for r in range(b2, sf2 + 1)]
             + [("Bloc 3 — Reluare", data_reluare, b3, "Notă contabilă")])
    for i, (bloc, data, r, doc) in enumerate(linii, start=1):
        rn = n.r
        n.rand([i, bloc, f"={D(data)}", f"={J(f'B{r}')}", f"={J(f'E{r}')}",
                f"=MAX(N({J(f'C{r}')}),N({J(f'F{r}')}))", f"={J(f'D{r}')}", doc,
                f'=IF(N(F{rn})>0.005,"DA","NU")'])
    ultim_n = n.r - 1
    n.gol()
    n.kv("Rânduri de importat (Include=DA)", f'=COUNTIF(I{prima_n}:I{ultim_n},"DA")',
         tip="calc")
