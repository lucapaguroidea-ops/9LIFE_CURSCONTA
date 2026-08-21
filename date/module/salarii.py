"""MOD_SALARII — statul de plată lunar, cu registru pe angajat.

Acoperă F-32. Trece din „EXEMPLU EXTERN” în IMPLEMENTAT.

Cotele și structura sunt preluate din `surse/module-externe/Salarii_AS_Kids_31.07.2026.xlsx`
și verificate contra tuturor celor 4 angajați reali din acel fișier:

    CAS      25%     pe brut
    CASS     10%     pe (brut + tichete)          ← tichetele intră în baza CASS
    Impozit  10%     pe (venit net + tichete)     ← dar NU în baza CAS
    CAM      2,25%   pe brut, cheltuiala angajatorului
    rotunjire la leu la FIECARE pas, nu doar la final

Diferența față de fișierul-sursă: acolo e câte o foaie per angajat; aici e un
registru cu totaluri, iar notele contabile se emit o dată pe lună, agregat. Fișele
individuale rămân vizibile în registru.

⚠ LIMITĂRI DECLARATE (vezi Reguli_SALARII, tabelul C) — nu sunt omisiuni tăcute:
  - fără deducere personală: toți cei 4 angajați din sursă sunt peste plafonul de
    acordare, deci mecanismul nu apare în fișier și nu îl inventez;
  - fără facilități sectoriale (construcții, IT, agricultură, alimentar);
  - fără scutiri pentru persoane cu handicap sau studenți;
  - contribuția la Pilonul II și opțiunile de pensie facultativă nu sunt tratate.
Pentru oricare dintre ele, cotele din Reguli trebuie ajustate ÎNAINTE de folosire.
"""

COD = "MOD_SALARII"

CATALOG = dict(
    fluxuri="F-32",
    tip="Lunar, pe registru de angajați",
    variabile="Brut, tichete, avans, pe angajat; cotele CAS/CASS/impozit/CAM",
    porti="Fără deducere personală și fără facilități sectoriale — vezi Reguli, tabelul C",
    blocuri="B1 Plata avansului; B2 Costurile lunii; B3 Plăți (net, taxe, CAM)",
    activ="DA",
)

#: Angajații din fișierul-sursă, ca valori implicite verificabile.
#: (nume, brut, tichete, avans)
ANGAJATI = [
    ("CHIRIACESCU DIANA-ELENA", 24610, 690, 0),
    ("NEAGU VLAD-FLORIAN", 12513, 480, 0),
    ("POPESCU IOANA-GABRIELA", 9627, 690, 0),
    ("SASCAU COSMIN-BOGDAN", 24127, 690, 0),
]
RANDURI_LIBERE = 4


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_SALARII", {"A": 30, "B": 22, "C": 12, "D": 12, "E": 12, "F": 12,
                                 "G": 12, "H": 13, "I": 12, "J": 13, "K": 14, "L": 12})
    d.titlu("MOD_SALARII — Declarații (input)")
    d.nota("Completează galben: antetul, apoi brut / tichete / avans pe fiecare angajat. "
           "Restul coloanelor din registru sunt formule. Valorile implicite sunt cele din "
           "statul real din 31.07.2026, ca modulul să poată fi verificat contra lui.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    d.kv("CUI", "=Parametri!B6", tip="calc")
    luna = d.kv("Luna (AAAA-LL)", "2026-07")
    data_cost = d.kv("Data notei de costuri (ultima zi a lunii)", "2026-07-31",
                     nota="Costurile se înregistrează la închiderea lunii")
    data_plata = d.kv("Data plăților (din extras)", "2026-08-10",
                      nota="Netul și taxele se plătesc în luna următoare")
    data_avans = d.kv("Data plății avansului", "2026-07-20")
    d.gol()

    d.sectiune("2. Cote (din Parametri — se schimbă doar când se schimbă legea)")
    cas = d.kv("CAS (pensie), pe brut", f"={P['cota_cas']}", tip="calc")
    cass = d.kv("CASS (sănătate), pe brut + tichete", f"={P['cota_cass']}", tip="calc")
    imp = d.kv("Impozit pe venit, pe venit net + tichete", f"={P['cota_impozit']}", tip="calc")
    cam = d.kv("CAM (asigurare de muncă), pe brut", f"={P['cota_cam']}", tip="calc")
    d.gol()

    d.sectiune("3. Registrul angajaților")
    d.nota("Coloanele F–L sunt formule. Rotunjirea e la leu, la fiecare pas — la fel ca "
           "în statul de plată; altfel totalurile diferă de cele din soft cu câțiva lei.")
    d.cap(["Nr.", "Angajat", "Brut", "Tichete", "Avans", "CAS", "CASS",
           "Venit net", "Impozit", "Salariu net", "Total de plată", "CAM"])

    prima = d.r
    for i in range(len(ANGAJATI) + RANDURI_LIBERE):
        r = d.r
        nume, brut, tichete, avans = ANGAJATI[i] if i < len(ANGAJATI) else ("", None, None, None)
        d._scrie(1, i + 1, font=_f_normal())
        d._scrie(2, nume, font=_f_input(), fill=_fill_input())
        d._scrie(3, brut, font=_f_input(), fill=_fill_input())
        d._scrie(4, tichete, font=_f_input(), fill=_fill_input())
        d._scrie(5, avans, font=_f_input(), fill=_fill_input())
        gol = f'IF($C{r}="","",'
        d._scrie(6, f'={gol}ROUND($C{r}*{cas},0))', font=_f_normal())
        d._scrie(7, f'={gol}ROUND(($C{r}+$D{r})*{cass},0))', font=_f_normal())
        d._scrie(8, f'={gol}$C{r}-$F{r}-$G{r})', font=_f_normal())
        d._scrie(9, f'={gol}ROUND(($H{r}+$D{r})*{imp},0))', font=_f_normal())
        d._scrie(10, f'={gol}$H{r}-$I{r})', font=_f_normal())
        d._scrie(11, f'={gol}$J{r}-$E{r})', font=_f_normal())
        d._scrie(12, f'={gol}ROUND($C{r}*{cam},0))', font=_f_normal())
        d.r += 1
    ultim = d.r - 1

    def suma(col):
        return f"SUM({col}{prima}:{col}{ultim})"

    d.cap(["", "TOTAL", f"={suma('C')}", f"={suma('D')}", f"={suma('E')}",
           f"={suma('F')}", f"={suma('G')}", f"={suma('H')}", f"={suma('I')}",
           f"={suma('J')}", f"={suma('K')}", f"={suma('L')}"])
    t = d.r - 1
    #: coloana totalurilor → referință locală, pe care `d.ref` o prefixează cu foaia
    T = {c: f"${c}${t}" for c in "CDEFGHIJKL"}
    d.gol()

    d.sectiune("4. Conturi")
    c_chelt = d.kv("Cont cheltuieli cu salariile", 641)
    c_pers = d.kv("Cont personal — salarii datorate", 421)
    c_avans = d.kv("Cont avansuri acordate personalului", 425)
    c_cas = d.kv("Cont CAS reținut", 4315)
    c_cass = d.kv("Cont CASS reținut", 4316)
    c_imp = d.kv("Cont impozit pe venit reținut", 444)
    c_cam_ch = d.kv("Cont cheltuieli cu CAM", 646)
    c_cam_dat = d.kv("Cont CAM datorat bugetului", 436)
    c_tich_ch = d.kv("Cont cheltuieli cu tichetele", 642)
    c_tich_st = d.kv("Cont tichete în gestiune", 5328)
    c_banca = d.kv("Cont trezorerie", "5121")
    d.gol()

    d.sectiune("5. Controale")
    d.check("Check brut = net + rețineri",
            f"={T['C']}-({T['J']}+{T['F']}+{T['G']}+{T['I']})",
            '=IF(ABS(B{0})<0.51,"OK — brutul se descompune integral",'
            '"EROARE — rotunjirile nu se închid")'.format(d.r))
    d.check("Check total de plată = net − avans",
            f"={T['K']}-({T['J']}-{T['E']})",
            '=IF(ABS(B{0})<0.01,"OK","EROARE")'.format(d.r))
    d.check("Reminder bază CASS",
            f"={T['D']}",
            '="Tichetele intră în baza CASS și în baza impozitului, dar NU în baza CAS. '
            'Dacă softul le tratează altfel, diferența apare aici."')
    d.check("Reminder deducere personală",
            '="—"',
            '="Modulul NU calculează deducerea personală. La salarii mici devine "'
            '&"obligatorie — vezi Reguli_SALARII, tabelul C."')
    d.gol()

    d.sectiune("6. Sufix generat")
    sufix = d.kv("Sufix", f'=" - " & {luna}', tip="calc")

    # -------------------------------------------------------------------- Reguli
    g = F("Reguli_SALARII", {"A": 26, "B": 30, "C": 14, "D": 40, "E": 22, "F": 54})
    g.titlu("MOD_SALARII — Reguli (tabele fixe)")
    g.nota("Regula fiscală e dată, nu formulă. Se editează doar când se schimbă legea.")
    g.gol()
    g.sectiune("Tabel A — Contribuții și baze")
    g.cap(["Element", "Bază de calcul", "Cotă", "Cine suportă", "Cont", "Temei"])
    for row in [
        ("CAS — pensie", "salariul brut", "25%", "angajatul (reținut)", "4315",
         "art. 138 Cod fiscal"),
        ("CASS — sănătate", "brut + tichete de masă", "10%", "angajatul (reținut)", "4316",
         "art. 156 CF; tichetele intră în bază din 2024"),
        ("Impozit pe venit", "venit net + tichete", "10%", "angajatul (reținut)", "444",
         "art. 78 CF"),
        ("CAM — asigurare de muncă", "salariul brut", "2,25%", "angajatorul (cheltuială)",
         "436", "art. 220^3 CF"),
        ("Tichete de masă", "valoare nominală", "—", "angajatorul (cheltuială)", "642 / 5328",
         "nu intră în baza CAS; intră în CASS și impozit"),
    ]:
        g.rand(list(row))
    g.gol()

    g.sectiune("Tabel B — Ordinea înregistrărilor")
    g.cap(["Moment", "Ce se înregistrează", "Data", "", "", "Observație"])
    for row in [
        ("Avans", "425 = 5121", "în cursul lunii", "", "",
         "Doar dacă există avans acordat"),
        ("Închiderea lunii", "641 = 421; 421 = 4315/4316/444; 646 = 436; 642 = 5328",
         "ultima zi a lunii", "", "", "Costul aparține lunii lucrate"),
        ("Stingerea avansului", "421 = 425", "ultima zi a lunii", "", "",
         "Diminuează datoria salarială cu avansul deja plătit"),
        ("Plăți", "421 = 5121; 4315/4316/444 = 5121; 436 = 5121", "luna următoare", "", "",
         "Termenul legal: 25 a lunii următoare"),
    ]:
        g.rand(list(row))
    g.gol()

    g.sectiune("Tabel C — LIMITĂRI DECLARATE ale modulului")
    g.nota("Enumerate explicit ca să nu fie luate drept acoperite. Fiecare cere ajustare "
           "manuală înainte de folosire la un client căruia i se aplică.")
    g.cap(["Ce NU tratează", "De ce", "Ce faci", "", "", "Efect dacă îl ignori"])
    for row in [
        ("Deducerea personală", "Cei 4 angajați din statul-sursă sunt peste plafonul de "
         "acordare, deci mecanismul nu apare în fișier și nu a fost inventat.",
         "La salarii mici: calculează deducerea și scade-o din baza impozitului.", "", "",
         "Impozit supraevaluat, net subevaluat"),
        ("Facilități sectoriale (construcții, IT, agricultură, alimentar)",
         "Cotele și scutirile diferă pe sector și se schimbă des.",
         "Ajustează cotele din Parametri și verifică scutirea de CASS/impozit.", "", "",
         "Contribuții calculate greșit în ambele sensuri"),
        ("Scutiri (handicap, studenți)", "Regim special, pe document justificativ.",
         "Tratează separat angajatul respectiv.", "", "", "Impozit reținut nedatorat"),
        ("Pilonul II / pensii facultative", "Rețineri opționale, pe cerere.",
         "Adaugă coloană de reținere și cont 4315 analitic.", "", "",
         "Netul plătit nu corespunde statului"),
        ("Concedii medicale (FNUASS)", "Recuperarea de la buget are mecanism propriu.",
         "Tratează prin 4382 / 4315 analitic.", "", "", "Cheltuiala rămâne umflată"),
    ]:
        g.rand(list(row))

    # ------------------------------------------------------------------- Jurnale
    j = F("Jurnale_SALARII", {"A": 8, "B": 14, "C": 14, "D": 46, "E": 14, "F": 14, "G": 46})
    j.titlu("MOD_SALARII — Jurnale (generate automat)")
    j.nota("Notele sunt agregate pe lună. Fișele individuale rămân în registrul din "
           "Declarații. Fiecare bloc are rând de Check.")
    j.gol()
    D = d.ref

    j.sectiune("Bloc 1 — Plata avansului")
    j.kv("Data jurnal:", f"={D(data_avans)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b1 = j.r
    j.rand([1, f"={D(c_avans)}", f"={D(T['E'])}",
            f'="Avans acordat personalului" & {D(sufix)}',
            f"={D(c_banca)}", f"={D(T['E'])}",
            f'="Plata avansului din bancă" & {D(sufix)}'])
    j.gol()
    j.check("Check Σ (structural)", f"=C{b1}-F{b1}",
            f'=IF(ABS(B{j.r})<0.01,"OK — nota se închide","EROARE")')
    j.check("Bloc activ?", f"={D(T['E'])}",
            f'=IF(B{j.r}>0,"ACTIV — există avans","INACTIV — fără avans în această lună")')
    j.gol()

    j.sectiune("Bloc 2 — Costurile lunii")
    j.kv("Data jurnal:", f"={D(data_cost)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b2 = j.r
    j.rand([1, f"={D(c_chelt)}", f"={D(T['C'])}",
            f'="Cheltuieli cu salariile" & {D(sufix)}',
            f"={D(c_pers)}", f"={D(T['C'])}",
            f'="Salarii brute datorate personalului" & {D(sufix)}'])
    j.rand([2, f"={D(c_pers)}", f"={D(T['F'])}+{D(T['G'])}+{D(T['I'])}",
            f'="Rețineri din salarii: CAS, CASS, impozit" & {D(sufix)}',
            f"={D(c_cas)}", f"={D(T['F'])}",
            f'="CAS reținut, datorat bugetului" & {D(sufix)}'])
    j.rand([3, None, None, None, f"={D(c_cass)}", f"={D(T['G'])}",
            f'="CASS reținut, datorat bugetului" & {D(sufix)}'])
    j.rand([4, None, None, None, f"={D(c_imp)}", f"={D(T['I'])}",
            f'="Impozit pe venit reținut, datorat bugetului" & {D(sufix)}'])
    j.rand([5, f"={D(c_cam_ch)}", f"={D(T['L'])}",
            f'="Cheltuieli cu CAM" & {D(sufix)}',
            f"={D(c_cam_dat)}", f"={D(T['L'])}",
            f'="CAM datorat bugetului" & {D(sufix)}'])
    j.rand([6, f"={D(c_tich_ch)}", f"={D(T['D'])}",
            f'="Cheltuieli cu tichetele de masă" & {D(sufix)}',
            f"={D(c_tich_st)}", f"={D(T['D'])}",
            f'="Descărcarea tichetelor din gestiune" & {D(sufix)}'])
    j.rand([7, f"={D(c_pers)}", f"={D(T['E'])}",
            f'="Diminuarea datoriei salariale cu avansul acordat" & {D(sufix)}',
            f"={D(c_avans)}", f"={D(T['E'])}",
            f'="Stingerea avansului acordat personalului" & {D(sufix)}'])
    sf2 = j.r - 1
    j.gol()
    j.check("Total Dr", f"=SUM(C{b2}:C{sf2})", "")
    j.check("Total Cr", f"=SUM(F{b2}:F{sf2})", "")
    j.check("Check Σ (structural)", f"=SUM(C{b2}:C{sf2})-SUM(F{b2}:F{sf2})",
            f'=IF(ABS(B{j.r})<0.01,"OK — notele se închid","EROARE")')
    j.check("Check sold 421 după bloc",
            f"={D(T['C'])}-({D(T['F'])}+{D(T['G'])}+{D(T['I'])}+{D(T['E'])})",
            f'=IF(ABS(B{j.r}-{D(T["K"])})<0.51,'
            f'"OK — soldul 421 = total de plată","EROARE — 421 nu corespunde netului")')
    j.gol()

    j.sectiune("Bloc 3 — Plăți")
    j.kv("Data jurnal:", f"={D(data_plata)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr", "Descriere Cr"])
    b3 = j.r
    j.rand([1, f"={D(c_pers)}", f"={D(T['K'])}",
            f'="Plata salariilor nete" & {D(sufix)}',
            f"={D(c_banca)}", f"={D(T['K'])}",
            f'="Plata salariilor nete din bancă" & {D(sufix)}'])
    j.rand([2, f"={D(c_cas)}", f"={D(T['F'])}",
            f'="Stingerea datoriei CAS" & {D(sufix)}',
            f"={D(c_banca)}", f"={D(T['F'])}+{D(T['G'])}+{D(T['I'])}",
            f'="Plata CAS, CASS și impozit din bancă" & {D(sufix)}'])
    j.rand([3, f"={D(c_cass)}", f"={D(T['G'])}",
            f'="Stingerea datoriei CASS" & {D(sufix)}', None, None, None])
    j.rand([4, f"={D(c_imp)}", f"={D(T['I'])}",
            f'="Stingerea datoriei de impozit" & {D(sufix)}', None, None, None])
    j.rand([5, f"={D(c_cam_dat)}", f"={D(T['L'])}",
            f'="Stingerea datoriei CAM" & {D(sufix)}',
            f"={D(c_banca)}", f"={D(T['L'])}",
            f'="Plata CAM din bancă" & {D(sufix)}'])
    sf3 = j.r - 1
    j.gol()
    j.check("Total Dr", f"=SUM(C{b3}:C{sf3})", "")
    j.check("Total Cr", f"=SUM(F{b3}:F{sf3})", "")
    j.check("Check Σ (structural)", f"=SUM(C{b3}:C{sf3})-SUM(F{b3}:F{sf3})",
            f'=IF(ABS(B{j.r})<0.01,"OK — notele se închid","EROARE")')
    j.gol()
    j.nota("Stare terminală așteptată: 421 = 0, 425 = 0, 4315/4316/444/436 = 0 după plăți; "
           "641, 642 și 646 se închid pe 121 la finalul exercițiului (vezi fluxul de "
           "închidere a exercițiului).")

    # ---------------------------------------------------------------- NotaExport
    n = F("NotaExport_SALARII", {"A": 6, "B": 26, "C": 12, "D": 12, "E": 12, "F": 14,
                                 "G": 48, "H": 20, "I": 9})
    n.titlu("MOD_SALARII — Notă pentru import (1 rând = 1 înregistrare)")
    n.nota("Filtrează pe Include = DA. Echilibrul se verifică pe bloc în Jurnale, nu pe "
           "totalul listei.")
    n.gol()
    n.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere",
           "Document", "Include"])
    J = j.ref
    prima_n = n.r
    linii = ([("Bloc 1 — Avans", data_avans, r) for r in range(b1, b1 + 1)]
             + [("Bloc 2 — Costuri", data_cost, r) for r in range(b2, sf2 + 1)]
             + [("Bloc 3 — Plăți", data_plata, r) for r in range(b3, sf3 + 1)])
    for i, (bloc, data, r) in enumerate(linii, start=1):
        rn = n.r
        n.rand([i, bloc, f"={D(data)}", f"={J(f'B{r}')}", f"={J(f'E{r}')}",
                f"={J(f'C{r}')}", f"={J(f'D{r}')}", "Stat de plată",
                f'=IF(N(F{rn})>0,"DA","NU")'])
    ultim_n = n.r - 1
    n.gol()
    n.kv("Rânduri de importat (Include=DA)", f'=COUNTIF(I{prima_n}:I{ultim_n},"DA")',
         tip="calc")


# stilurile se importă târziu ca modulul de date să nu depindă de build la import
def _f_normal():
    from build import stil
    return stil.F_NORMAL


def _f_input():
    from build import stil
    return stil.F_INPUT


def _fill_input():
    from build import stil
    return stil.FILL_INPUT
