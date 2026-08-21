"""MOD_TVA_INCASARE — regimul TVA la încasare: 4428.INC pe ambele sensuri.

Acoperă F-17.

Contul 4428.INC are rol de **intermediar**: ține TVA-ul până la un eveniment discret —
plata către furnizor, respectiv încasarea de la client. Până atunci TVA nu e nici
deductibil, nici colectat. Cele patru blocuri sunt două perechi simetrice:

    factură achiziție → 4428.INC        plată      → 4426
    factură vânzare   → 4428.INC        încasare   → 4427

Ce se greșește: se pune TVA direct pe 4426/4427 la factură, ca în regimul normal. Atunci
TVA se deduce sau se colectează cu o lună mai devreme decât are dreptul firma, iar D300
iese greșit. Tabelul A scrie explicit „TVA NU intră pe 4426 la factură”.

**4428.INC nu e 4428.AM.** Sunt două analitice ale aceluiași sintetic, cu roluri
diferite: unul așteaptă plata/încasarea, celălalt e rectificativ de preț la gestiunea cu
amănunt. Amestecate, niciuna din corelații nu mai închide.

Modulul era una din cele șapte foi rămase din sămânța de 14.08.2026.
"""

COD = "MOD_TVA_INCASARE"

CATALOG = dict(
    # Foile de sămânță se numesc `…_TVA_INC`, nu `…_TVA_INCASARE`. Redenumirea ar rupe
    # referințele existente pentru un câștig de simetrie; sufixul se declară în schimb.
    sufix="TVA_INC",
    fluxuri="F-17",
    tip="Pe factură",
    variabile="Sumă netă, TVA, Tip (achiziție/vânzare), Data plată/încasare",
    porti="4428.INC activ",
    blocuri="B1 Factură→4428.INC; B2 Plată/Încasare→4426/4427",
    ce_face="4428.INC: factură → plată/încasare → 4426/4427",
    cand="Când regimul e TVA la încasare",
    activ="DA",
)

#: pas, cont Dr, cont Cr, sumă (sursă), condiție, temei / observație
SECVENTA = [
    (1, "3xx/6xx + 4428.INC", "401", "net + TVA",
     "La factură achiziție (regim TVA la încasare)",
     "TVA NU intră pe 4426 la factură"),
    (2, "401", "512", "total factură", "La plată furnizor", "Stingere datorie"),
    (3, "4426", "4428.INC", "TVA", "La plată (același moment sau ulterior)",
     "TVA devine exigibilă / deductibilă"),
    (4, "411", "7xx + 4428.INC", "net + TVA",
     "La factură vânzare (regim TVA la încasare)",
     "TVA NU intră pe 4427 la factură"),
    (5, "512", "411", "total factură", "La încasare client", "Stingere creanță"),
    (6, "4428.INC", "4427", "TVA", "La încasare", "TVA devine exigibilă / colectată"),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_TVA_INC", {"A": 40, "B": 24, "C": 54})
    d.titlu("MOD_TVA_INCASARE — Declarații (input)")
    d.nota("Rol dual 4428.INC: pe achiziție până la plată → 4426; pe vânzare până la "
           "încasare → 4427. Nu se amestecă cu 4428.AM.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    luna = d.kv("Luna", "2026-07")
    d.gol()

    d.sectiune("2. Achiziție (TVA la încasare)")
    data_fa = d.kv("Data factură achiziție", "2026-07-08")
    data_plata = d.kv("Data plată furnizor", "2026-07-20")
    net_a = d.kv("Sumă netă achiziție", 5000)
    cota = d.kv("Cotă TVA", 0.21)
    tva_a = d.kv("TVA achiziție", f"={net_a}*{cota}", tip="calc")
    total_a = d.kv("Total factură achiziție", f"={net_a}+{tva_a}", tip="calc")
    d.gol()

    d.sectiune("3. Vânzare (TVA la încasare)")
    data_fv = d.kv("Data factură vânzare", "2026-07-12")
    data_inc = d.kv("Data încasare client", "2026-07-28")
    net_v = d.kv("Sumă netă vânzare", 8000)
    tva_v = d.kv("TVA vânzare", f"={net_v}*{cota}", tip="calc")
    total_v = d.kv("Total factură vânzare", f"={net_v}+{tva_v}", tip="calc")
    d.gol()

    d.sectiune("4. Conturi")
    c_stoc = d.kv("Cont stoc / cheltuială", "301")
    c_furn = d.kv("Cont furnizor", "401.RO")
    c_client = d.kv("Cont client", "411.RO")
    c_venit = d.kv("Cont venit", "707")
    c_inc = d.kv("Cont 4428.INC", "4428.INC")
    c_4426 = d.kv("Cont 4426", "4426")
    c_4427 = d.kv("Cont 4427", "4427")
    c_trez = d.kv("Cont trezorerie", "512.1")
    d.gol()

    d.sectiune("5. Sufix")
    sufix = d.kv("Sufix", f'="— TVA la încasare " & {luna}', tip="calc")

    # ------------------------------------------------------------------- Reguli
    g = F("Reguli_TVA_INC",
          {"A": 8, "B": 24, "C": 20, "D": 18, "E": 44, "F": 44})
    g.titlu("MOD_TVA_INCASARE — Reguli (tabele fixe)")
    g.nota("Rol dual 4428.INC: pe achiziție până la plată → 4426; pe vânzare până la "
           "încasare → 4427. Separat de 4428.AM.")
    g.gol()

    g.sectiune("Tabel A — Secvența operațională")
    g.cap(["Pas", "Cont Dr", "Cont Cr", "Sumă (sursă)", "Condiție",
           "Temei / observație"])
    for rand in SECVENTA:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel B — Porți de calitate")
    for linie in [
        "• ΣDr=ΣCr pe fiecare moment (global cu ABS)",
        "• Sold 4428.INC = 0 după toate plățile și încasările perioadei",
        "• 4428.INC ≠ 4428.AM (analitice separate — amănunt vs TVA la încasare)",
        "• La închiderea lunară TVA: doar 4426/4427 exigibile intră în "
        "MOD_INCHIDERE_TVA",
    ]:
        g.nota(linie)

    # ------------------------------------------------------------------ Jurnale
    j = F("Jurnale_TVA_INC",
          {"A": 12, "B": 16, "C": 14, "D": 46, "E": 16, "F": 14, "G": 46})
    j.titlu("MOD_TVA_INCASARE — Jurnale")
    j.gol()

    D = d.ref
    antet = ["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr",
             "Descriere Cr"]

    # Articolele compuse au partea de credit scrisă O SINGURĂ DATĂ, pe primul rând, cu
    # TOTALUL. Rândul al doilea poartă doar componenta de debit, cu zerouri pe cealaltă
    # parte — de-aia `Check` însumează debitele și le compară cu creditul unic.
    j.sectiune("Bloc 1 — Factură achiziție (TVA neexigibilă)")
    j.kv("Data:", f"={D(data_fa)}", tip="calc")
    j.cap(antet)
    b1a = j.rand([1, f"={D(c_stoc)}", f"={D(net_a)}",
                  f'="Achiziție (net) " & {D(sufix)}',
                  f"={D(c_furn)}", f"={D(total_a)}",
                  f'="Datorie furnizor total " & {D(sufix)}'])
    b1b = j.rand([2, f"={D(c_inc)}", f"={D(tva_a)}",
                  f'="TVA neexigibilă achiziție " & {D(sufix)}', 0, 0])
    c1 = j.check("Check B1", f"=({b1a['C']}+{b1b['C']})-{b1a['F']}",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Bloc 2 — Plată furnizor (TVA devine exigibilă)")
    j.kv("Data:", f"={D(data_plata)}", tip="calc")
    j.cap(antet)
    b2a = j.rand([1, f"={D(c_furn)}", f"={D(total_a)}",
                  f'="Plată furnizor " & {D(sufix)}',
                  f"={D(c_trez)}", f"={D(total_a)}",
                  f'="Ieșire bancă " & {D(sufix)}'])
    b2b = j.rand([2, f"={D(c_4426)}", f"={D(tva_a)}",
                  f'="TVA deductibilă (exigibilă) " & {D(sufix)}',
                  f"={D(c_inc)}", f"={D(tva_a)}",
                  f'="Stingere 4428.INC achiziție " & {D(sufix)}'])
    c2 = j.check("Check B2",
                 f"=({b2a['C']}+{b2b['C']})-({b2a['F']}+{b2b['F']})",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Bloc 3 — Factură vânzare (TVA neexigibilă)")
    j.kv("Data:", f"={D(data_fv)}", tip="calc")
    j.cap(antet)
    b3a = j.rand([1, f"={D(c_client)}", f"={D(total_v)}",
                  f'="Creanță client total " & {D(sufix)}',
                  f"={D(c_venit)}", f"={D(net_v)}",
                  f'="Venit " & {D(sufix)}'])
    b3b = j.rand([2, 0, 0, None, f"={D(c_inc)}", f"={D(tva_v)}",
                  f'="TVA neexigibilă vânzare " & {D(sufix)}'])
    c3 = j.check("Check B3", f"={b3a['C']}-({b3a['F']}+{b3b['F']})",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Bloc 4 — Încasare client (TVA devine exigibilă)")
    j.kv("Data:", f"={D(data_inc)}", tip="calc")
    j.cap(antet)
    b4a = j.rand([1, f"={D(c_trez)}", f"={D(total_v)}",
                  f'="Încasare client " & {D(sufix)}',
                  f"={D(c_client)}", f"={D(total_v)}",
                  f'="Stingere creanță " & {D(sufix)}'])
    b4b = j.rand([2, f"={D(c_inc)}", f"={D(tva_v)}",
                  f'="Stingere 4428.INC vânzare " & {D(sufix)}',
                  f"={D(c_4427)}", f"={D(tva_v)}",
                  f'="TVA colectată (exigibilă) " & {D(sufix)}'])
    c4 = j.check("Check B4",
                 f"=({b4a['C']}+{b4b['C']})-({b4a['F']}+{b4b['F']})",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    glob = j.check("Check global",
                   f"=ABS({c1})+ABS({c2})+ABS({c3})+ABS({c4})",
                   f'=IF(B{j.r}<0.01,"OK — toate blocurile se închid",'
                   f'"EROARE — cel puțin un bloc dezechilibrat")')
    j.gol()
    j.nota("Stare terminală: 4428.INC sold 0 | 4426 conține TVA ded. exigibilă | "
           "4427 conține TVA col. exigibilă")

    # --------------------------------------------------------------- NotaExport
    e = F("NotaExport_TVA_INC",
          {"A": 6, "B": 12, "C": 14, "D": 12, "E": 12, "F": 14, "G": 22, "H": 10,
           "I": 10})
    e.titlu("MOD_TVA_INCASARE — Notă pentru import")
    e.gol()
    e.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    primul = e.r
    # (bloc, data, cont Dr, cont Cr, sumă) — la articolele compuse, creditul unic al
    # primului rând se repetă pe componenta a doua, ca fiecare linie exportată să fie o
    # înregistrare completă.
    linii = [
        ("B1 Ach.", data_fa, b1a["B"], b1a["E"], b1a["C"]),
        ("B1 Ach.", data_fa, b1b["B"], b1a["E"], b1b["C"]),
        ("B2 Plată", data_plata, b2a["B"], b2a["E"], b2a["C"]),
        ("B2 Plată", data_plata, b2b["B"], b2b["E"], b2b["C"]),
        ("B3 Vânz.", data_fv, b3a["B"], b3a["E"], b3a["F"]),
        ("B3 Vânz.", data_fv, b3a["B"], b3b["E"], b3b["F"]),
        ("B4 Înc.", data_inc, b4a["B"], b4a["E"], b4a["C"]),
        ("B4 Înc.", data_inc, b4b["B"], b4b["E"], b4b["C"]),
    ]
    for i, (bloc, data, cd, cc, suma) in enumerate(linii, start=1):
        e.rand([i, bloc, f"={D(data)}", f"={j.ref(cd)}", f"={j.ref(cc)}",
                f"={j.ref(suma)}", "TVA la încasare", "F-17",
                f'=IF(AND(ISNUMBER(F{e.r}),F{e.r}>0),"DA","NU")'])
    e.gol()
    e.check("Check global", f"={j.ref(glob)}",
            f'=IF(ABS(B{e.r})<0.01,"OK","EROARE")')
