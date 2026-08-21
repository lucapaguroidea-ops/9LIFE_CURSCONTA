"""MOD_DECONT — decontul de cheltuieli al unui titular, cu motor pe linii.

Acoperă F-35. Trece din „EXEMPLU EXTERN” în IMPLEMENTAT.

Structura și regulile vin din `surse/module-externe/Deconturi_AS_Kids_…xlsx` și sunt
verificate contra celor 5 linii reale din decontul CHIRIACESCU DIANA (total 3.938,76).

Ideea motorului: nu scrii tu tratamentul fiecărei linii, ci îl DEDUCI din două tabele.

  1. `Natura cheltuielii` — codul spune contul, cota de TVA și regimul.
  2. `Matricea dreptului de deducere` — perechea (tip document × CUI pe document)
     spune dacă TVA se deduce și dacă cheltuiala se acceptă.

Coloana **„Regula aplicată”** scrie în clar de ce a ieșit așa. Fără ea, un decont
respins arată ca o eroare de calcul; cu ea, se vede că e o factură fără CUI.

⚠ Preluat ca atare din template: liniile fără document justificativ NU se înregistrează
pe cheltuială. Dacă totuși se plătesc, suma devine avantaj de natură salarială și intră
în statul de plată (impozit + contribuții) — tratament care ține de MOD_SALARII, nu de
aici. Modulul le semnalează și le ține separat, nu le calculează.
"""

COD = "MOD_DECONT"

CATALOG = dict(
    fluxuri="F-35",
    tip="Pe decont",
    variabile="Linii de decont (furnizor, sumă, natură, tip document, CUI), avans, cote",
    porti="Plătitor de TVA; % deducere vehicule; matricea document × CUI",
    blocuri="B1 Avans; B2 Cheltuieli + TVA; B3 Regularizare avans; B4 Plată / restituire",
    activ="NU",
    prefixe=("Declarații", "Reguli", "Registru", "Jurnale", "NotaExport"),
)

#: Liniile reale din decontul-sursă, ca valori implicite verificabile.
#: (furnizor, data, sumă brută, cod natură, tip document, CUI pe document)
LINII = [
    ("WIZZ AIR MALTA LIMITED", "2026-07-20", 1780.38, "TRANSP_INT", "Factura", "DA"),
    ("WIZZ AIR MALTA LIMITED", "2026-07-29", 1720.38, "TRANSP_INT", "Factura", "DA"),
    ("CITY CAFÉ EXPRESS", "2026-07-14", 38, "MASA", "Bon fiscal", "NU"),
    ("OLIMPIA PARKING", "2026-07-16", 200, "PARCARE", "Bon fiscal", "NU"),
    ("OLIMPIA PARKING", "2026-07-30", 200, "PARCARE", "Bon fiscal", "NU"),
]
RANDURI_LIBERE = 5

#: cod, denumire, cont, cotă, regim, % deducere, tratament fiscal, temei
NATURI = [
    ("TRANSP_INT", "Transport aerian internațional de persoane", "624", "0",
     "Scutit cu drept de deducere", "1", "Deductibil",
     "art. 294 alin. (1) — scutire cu drept de deducere, TVA zero"),
    ("TRANSP_INTERN", "Transport intern de persoane", "624", "redusa", "Taxabil", "1",
     "Deductibil", "cotă redusă pentru transportul de persoane"),
    ("PARCARE", "Parcare, taxe de drum", "624", "standard", "Taxabil", "1", "Deductibil",
     "cotă standard"),
    ("TAXI", "Taxi, transfer aeroport", "624", "redusa", "Taxabil", "1", "Deductibil",
     "transport de persoane"),
    ("CAZARE", "Cazare hotelieră", "625", "redusa", "Taxabil", "1", "Deductibil",
     "cotă redusă HoReCa"),
    ("MASA", "Masă în deplasare", "625", "redusa", "Taxabil", "1", "Deductibil",
     "restaurant/catering; dacă se acordă diurnă, comută pe 6588"),
    ("PROTOCOL", "Protocol cu partener / client", "6231", "redusa", "Taxabil", "1",
     "Deductibil limitat 2%", "limita de 2% din profitul contabil"),
    ("COMBUSTIBIL", "Combustibil auto", "6022", "standard", "Taxabil", "vehicul",
     "Deductibil limitat 50%", "art. 298 — deducere TVA 50% fără utilizare exclusivă"),
    ("SERVICII", "Alte servicii executate de terți", "628", "standard", "Taxabil", "1",
     "Deductibil", "—"),
    ("MATERIALE", "Materiale consumabile", "6028", "standard", "Taxabil", "1",
     "Deductibil", "—"),
    ("PERSONAL", "Cheltuială personală / nejustificată", "6588", "0",
     "Fără drept de deducere", "0", "Nedeductibil", "nu se acceptă la deducere fiscală"),
]

#: (tip document, CUI pe document, deducere TVA, cheltuială acceptată, motivare)
DEDUCERE = [
    ("Factura", "DA", "DA", "DA", "Factură completă conform art. 319 — TVA deductibil"),
    ("Factura", "NU", "NU", "DA",
     "Lipsesc datele cumpărătorului — TVA nedeductibil, cheltuiala rămâne acceptată"),
    ("Bon fiscal", "DA", "DA", "DA",
     "Factură simplificată — deducere permisă sub plafonul de 100 EUR"),
    ("Bon fiscal", "NU", "NU", "DA",
     "Bon fără CUI — TVA nedeductibil; justificare cu ordin de deplasare"),
    ("Lipsa document", "DA", "NU", "NU",
     "Fără document justificativ — decontul nu se acceptă"),
    ("Lipsa document", "NU", "NU", "NU",
     "Fără document justificativ — decontul nu se acceptă"),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_DECONT", {"A": 40, "B": 22, "C": 58})
    d.titlu("MOD_DECONT — Declarații (input)")
    d.nota("Antetul și politica de conturi se completează o dată. Liniile propriu-zise "
           "se lipesc în foaia Registru_DECONT. Valorile implicite sunt cele din decontul "
           "real din 31.07.2026, ca modulul să poată fi verificat contra lui.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    titular = d.kv("Titular decont", "CHIRIACESCU DIANA")
    data_dec = d.kv("Data decontului", "2026-07-31")
    data_plata = d.kv("Data plății / restituirii", "2026-08-05")
    d.gol()

    d.sectiune("2. Declarații fiscale")
    platitor = d.kv("Societate plătitoare de TVA (DA / NU)", "DA")
    cota_std = d.kv("Cotă TVA standard", "=Parametri!B10", tip="calc")
    cota_red = d.kv("Cotă TVA redusă", "=Parametri!B11", tip="calc")
    ded_veh = d.kv("Procent deducere TVA vehicule", f"={P['proc_vehicul']}", tip="calc")
    d.gol()

    d.sectiune("3. Politica de conturi (comutatoare)")
    c_datorie = d.kv("Cont datorie față de titular", "542",
                     nota="542 avansuri de trezorerie / 462 creditori / 4281 alte datorii")
    c_avans = d.kv("Cont avans de trezorerie", "542", nota="542 / 425")
    c_transport = d.kv("Cont transport și parcare", "625",
                       nota="624 / 625 — comutator; 625 e convenția din decontul-sursă")
    c_masa = d.kv("Cont masă în deplasare", "625", nota="625 / 6231 / 6588 — comutator")
    c_tva = d.kv("Cont TVA deductibilă", 4426)
    c_trez = d.kv("Cont trezorerie pentru plăți", "5121", nota="5121 / 5311")
    d.gol()

    d.sectiune("4. Avans și control")
    avans = d.kv("Avans primit (declarat în decont)", 0)
    sold_balanta = d.kv("Sold cont avans din balanță", 0,
                        nota="Din fișa contului, la data decontului")
    d.check("Verdict control avans", f"={sold_balanta}-{avans}",
            f'=IF(ABS(B{d.r})<0.01,"OK — avansul declarat corespunde balanței",'
            f'"ATENȚIE — declarația titularului nu corespunde evidenței contabile")')
    d.gol()

    d.sectiune("5. Sufix generat")
    sufix = d.kv("Sufix", f'=" - decont " & {titular} & " " & {data_dec}', tip="calc")

    # -------------------------------------------------------------------- Reguli
    g = F("Reguli_DECONT", {"A": 16, "B": 40, "C": 10, "D": 12, "E": 24, "F": 12,
                            "G": 22, "H": 52})
    g.titlu("MOD_DECONT — Reguli (tabele fixe)")
    g.nota("Regula fiscală e dată, nu formulă. Motorul din Registru caută în tabelele "
           "astea; se editează doar când se schimbă legea sau politica firmei.")
    g.gol()

    g.sectiune("Tabel A — Natura cheltuielii")
    cap_a = g.r
    g.cap(["Cod", "Denumire", "Cont", "Cotă TVA", "Regim TVA", "% deducere",
           "Impozit pe profit", "Temei / observație"])
    prima_a = g.r
    D = d.ref
    for cod, den, cont, cota, regim, proc, fiscal, temei in NATURI:
        cont_f = {"624": f"={D(c_transport)}", "625": f"={D(c_masa)}"}.get(cont, cont)
        cota_f = {"standard": f"={D(cota_std)}", "redusa": f"={D(cota_red)}",
                  "0": 0}.get(cota, cota)
        proc_f = f"={D(ded_veh)}" if proc == "vehicul" else float(proc)
        g.rand([cod, den, cont_f, cota_f, regim, proc_f, fiscal, temei])
    ultim_a = g.r - 1
    g.gol()

    g.sectiune("Tabel B — Matricea dreptului de deducere")
    g.nota("Cheia e perechea „tip document | CUI pe document”. Aici se decide dacă TVA "
           "se deduce și dacă cheltuiala se acceptă la decont.")
    g.cap(["Cheie", "Tip document", "CUI pe document", "Deducere TVA",
           "Cheltuială acceptată", "", "", "Motivare"])
    prima_b = g.r
    for tip, cui, ded, acc, motiv in DEDUCERE:
        g.rand([f"{tip}|{cui}", tip, cui, ded, acc, None, None, motiv])
    ultim_b = g.r - 1
    g.gol()

    g.sectiune("Tabel C — Limitare cunoscută")
    g.rand(["Liniile fără document justificativ nu se înregistrează pe cheltuială. "
            "Dacă suma se plătește totuși titularului, ea devine avantaj de natură "
            "salarială și se impozitează prin statul de plată (impozit + contribuții) — "
            "tratament care ține de MOD_SALARII. Modulul le ține separat, nu le calculează."])

    # ------------------------------------------------------------------ Registru
    reg = F("Registru_DECONT", {"A": 5, "B": 28, "C": 12, "D": 12, "E": 14, "F": 12,
                                "G": 10, "H": 10, "I": 10, "J": 10, "K": 10, "L": 14,
                                "M": 14, "N": 14, "O": 18, "P": 56})
    reg.titlu("MOD_DECONT — Registrul liniilor")
    reg.nota("Completează galben coloanele B–G. Coloanele H–P sunt formule: contul, cota, "
             "regimul și dreptul de deducere se citesc din Reguli. Coloana „Regula aplicată” "
             "spune de ce a ieșit așa.")
    reg.gol()
    reg.cap(["Nr.", "Furnizor", "Data doc.", "Sumă brută", "Natura chelt.", "Tip document",
             "CUI pe doc.", "Cont", "Cotă", "% ded.", "Deducere TVA", "Acceptat",
             "Bază cheltuială", "TVA deductibil", "Impozit pe profit", "Regula aplicată"])

    G = g.ref
    tbl_natura = G(f"$A${prima_a}:$H${ultim_a}")
    tbl_ded = G(f"$A${prima_b}:$H${ultim_b}")
    prima_r = reg.r
    for i in range(len(LINII) + RANDURI_LIBERE):
        r = reg.r
        val = LINII[i] if i < len(LINII) else ("", None, None, "", "", "")
        furnizor, data, suma, natura, tipdoc, cui = val
        reg._scrie(1, i + 1, font=_f_normal())
        for col, v in ((2, furnizor), (3, data), (4, suma), (5, natura),
                       (6, tipdoc), (7, cui)):
            reg._scrie(col, v, font=_f_input(), fill=_fill_input())
        gol = f'IF($D{r}="","",'
        vl = f'VLOOKUP($E{r},{tbl_natura},'
        vd = f'VLOOKUP($F{r}&"|"&$G{r},{tbl_ded},'
        reg._scrie(8, f'={gol}IFERROR({vl}3,FALSE),"?"))', font=_f_normal())
        reg._scrie(9, f'={gol}IFERROR({vl}4,FALSE),0))', font=_f_normal())
        reg._scrie(10, f'={gol}IFERROR({vl}6,FALSE),0))', font=_f_normal())
        reg._scrie(11, f'={gol}IF({D(platitor)}<>"DA","NU",'
                       f'IFERROR({vd}4,FALSE),"NU")))', font=_f_normal())
        reg._scrie(12, f'={gol}IFERROR({vd}5,FALSE),"NU"))', font=_f_normal())
        # baza = brut − TVA dedus; TVA dedus doar dacă deducerea e permisă
        tva = (f'IF($K{r}<>"DA",0,ROUND($D{r}*$I{r}/(1+$I{r})*$J{r},2))')
        reg._scrie(14, f'={gol}IF($L{r}<>"DA",0,{tva}))', font=_f_normal())
        reg._scrie(13, f'={gol}IF($L{r}<>"DA",0,$D{r}-$N{r}))', font=_f_normal())
        reg._scrie(15, f'={gol}IFERROR({vl}7,FALSE),"?"))', font=_f_normal())
        reg._scrie(16, f'={gol}IFERROR({vd}8,FALSE),"cod de natură necunoscut"))',
                   font=_f_nota())
        reg.r += 1
    ultim_r = reg.r - 1

    def s(col):
        return f"SUM({col}{prima_r}:{col}{ultim_r})"

    reg.cap(["", "TOTAL", "", f"={s('D')}", "", "", "", "", "", "", "", "",
             f"={s('M')}", f"={s('N')}", "", ""])
    tr = reg.r - 1
    R = reg.ref
    t_brut, t_baza, t_tva = R(f"$D${tr}"), R(f"$M${tr}"), R(f"$N${tr}")
    reg.gol()
    reg.sectiune("Recapitulație")
    t_acceptat = f"{t_baza}+{t_tva}"
    reg.kv("Total datorat titularului (bază + TVA dedus)", f"={t_acceptat}", tip="calc")
    ref_datorat = f"$B${reg.r - 1}"
    reg.kv("Total neacceptat (fără document justificativ)",
           f"={t_brut}-({t_acceptat})", tip="calc")
    ref_neacceptat = f"$B${reg.r - 1}"
    reg.kv("Avans acordat", f"={D(avans)}", tip="calc")
    reg.kv("De plătit titularului (+) / de restituit (−)",
           f"={R(ref_datorat)}-{D(avans)}", tip="calc")
    ref_sold = f"$B${reg.r - 1}"
    reg.gol()
    reg.check("Check Σ linii",
              f"={t_brut}-({t_acceptat})-{R(ref_neacceptat)}",
              f'=IF(ABS(B{reg.r})<0.01,"OK — brut = acceptat + neacceptat","EROARE")')
    reg.check("Check linii fără document",
              f"={R(ref_neacceptat)}",
              f'=IF(B{reg.r}<0.01,"OK — toate liniile au document justificativ",'
              f'"ATENȚIE — sumă fără document: nu se trece pe cheltuială. Dacă se '
              f'plătește, devine avantaj salarial — vezi MOD_SALARII")')

    # ------------------------------------------------------------------- Jurnale
    j = F("Jurnale_DECONT", {"A": 8, "B": 14, "C": 14, "D": 46, "E": 14, "F": 14, "G": 46})
    j.titlu("MOD_DECONT — Jurnale (generate automat)")
    j.nota("Cheltuielile se înregistrează agregat, pe contul dominant din decont. "
           "Pentru deconturi cu naturi multiple, folosește NotaExport, unde fiecare linie "
           "își poartă contul propriu.")
    j.gol()

    j.sectiune("Bloc 1 — Acordarea avansului")
    j.kv("Data jurnal:", f"={D(data_dec)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b1 = j.r
    j.rand([1, f"={D(c_avans)}", f"={D(avans)}",
            f'="Avans de trezorerie acordat" & {D(sufix)}',
            f"={D(c_trez)}", f"={D(avans)}",
            f'="Plata avansului de trezorerie" & {D(sufix)}'])
    j.gol()
    j.check("Check Σ (structural)", f"=C{b1}-F{b1}",
            f'=IF(ABS(B{j.r})<0.01,"OK — nota se închide","EROARE")')
    j.check("Bloc activ?", f"={D(avans)}",
            f'=IF(B{j.r}>0,"ACTIV — există avans","INACTIV — decont fără avans")')
    j.gol()

    j.sectiune("Bloc 2 — Cheltuielile din decont")
    j.kv("Data jurnal:", f"={D(data_dec)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b2 = j.r
    j.rand([1, f"={D(c_transport)}", f"={t_baza}",
            f'="Cheltuieli din decont, bază fără TVA dedus" & {D(sufix)}',
            f"={D(c_datorie)}", f"={R(ref_datorat)}",
            f'="Datorie față de titularul de decont" & {D(sufix)}'])
    j.rand([2, f"={D(c_tva)}", f"={t_tva}",
            f'="TVA deductibilă din decont" & {D(sufix)}', None, None, None])
    sf2 = j.r - 1
    j.gol()
    j.check("Total Dr", f"=SUM(C{b2}:C{sf2})", "")
    j.check("Total Cr", f"=SUM(F{b2}:F{sf2})", "")
    j.check("Check Σ (structural)", f"=SUM(C{b2}:C{sf2})-SUM(F{b2}:F{sf2})",
            f'=IF(ABS(B{j.r})<0.01,"OK — nota se închide","EROARE")')
    j.check("Check contul de cheltuială",
            f"={D(c_transport)}",
            '="Bloc agregat pe contul dominant. Dacă decontul are naturi multiple, '
            'importă din NotaExport, unde fiecare linie poartă contul ei."')
    j.gol()

    j.sectiune("Bloc 3 — Regularizarea avansului și plata")
    j.kv("Data jurnal:", f"={D(data_plata)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b3 = j.r
    j.rand([1, f"={D(c_datorie)}", f"={R(ref_sold)}",
            f'="Plata diferenței către titular" & {D(sufix)}',
            f"={D(c_trez)}", f"={R(ref_sold)}",
            f'="Plata din trezorerie" & {D(sufix)}'])
    sf3 = j.r - 1
    j.gol()
    j.check("Check Σ (structural)", f"=SUM(C{b3}:C{sf3})-SUM(F{b3}:F{sf3})",
            f'=IF(ABS(B{j.r})<0.01,"OK — nota se închide","EROARE")')
    j.check("Sensul plății", f"={R(ref_sold)}",
            f'=IF(B{j.r}>=0,"Se plătește titularului",'
            f'"Titularul restituie diferența — inversează sensul notei")')
    j.gol()
    j.nota("Stare terminală așteptată: contul de avans = 0, contul de datorie față de "
           "titular = 0 după plată.")

    # ---------------------------------------------------------------- NotaExport
    n = F("NotaExport_DECONT", {"A": 6, "B": 24, "C": 12, "D": 12, "E": 12, "F": 14,
                                "G": 48, "H": 22, "I": 9})
    n.titlu("MOD_DECONT — Notă pentru import (1 rând = 1 înregistrare)")
    n.nota("Aici fiecare linie de decont își păstrează contul propriu, spre deosebire de "
           "blocul agregat din Jurnale. Filtrează pe Include = DA.")
    n.gol()
    n.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere",
           "Document", "Include"])
    prima_n = n.r
    for i in range(len(LINII) + RANDURI_LIBERE):
        rr = prima_r + i
        rn = n.r
        n.rand([i + 1, "Bloc 2 — Cheltuieli pe linie", f"={D(data_dec)}",
                f"={R(f'$H${rr}')}", f"={D(c_datorie)}", f"={R(f'$M${rr}')}",
                f'=IF({R(f"$B${rr}")}="","",{R(f"$B${rr}")} & " — " & {R(f"$P${rr}")})',
                "Decont de cheltuieli",
                f'=IF(N(F{rn})>0,"DA","NU")'])
    ultim_n = n.r - 1
    n.gol()
    n.kv("Rânduri de importat (Include=DA)", f'=COUNTIF(I{prima_n}:I{ultim_n},"DA")',
         tip="calc")
    n.check("Check total linii vs. registru",
            f"=SUM(F{prima_n}:F{ultim_n})-{t_baza}",
            f'=IF(ABS(B{n.r})<0.01,"OK — suma liniilor = baza din registru","EROARE")')


def _f_normal():
    from build import stil
    return stil.F_NORMAL


def _f_nota():
    from build import stil
    return stil.F_NOTA


def _f_input():
    from build import stil
    return stil.F_INPUT


def _fill_input():
    from build import stil
    return stil.FILL_INPUT
