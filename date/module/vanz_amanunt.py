"""MOD_VANZ_AMANUNT — gestiunea la preț de vânzare cu amănuntul (PVA).

Acoperă F-14, F-40, F-43.

La amănunt, stocul stă în 371 la **prețul de raft**, adică deja cu adaos și cu TVA
înăuntru. Cele două conturi care fac diferența dintre preț și cost sunt rectificative:
378 ține adaosul, 4428.AM ține TVA-ul neexigibil. Niciunul nu ține ceva real — corectează
valoarea lui 371.

De aici vin cele două corelații sfinte, verificate pe cifre chiar în foaia de Declarații:

    C-01:  sold 371 × c/(100+c) = sold 4428
    C-02:  707 − 607 = rulaj debitor 378

Ele nu sunt decorative. Dacă descărcarea la vânzare se face doar pe cost — greșeala
clasică — 378 și 4428 rămân încărcate, iar ambele corelații se rup în aceeași lună.
De-asta blocul 3 are trei rânduri, nu unul: se descarcă proporțional 607, 378 ȘI 4428
contra unui singur credit pe 371.

**4428.AM nu e 4428.INC.** Același sintetic, două analitice, roluri diferite: aici e
rectificativ de preț, dincolo e intermediar care așteaptă încasarea. Amestecate, C-01 nu
mai închide pe nicio gestiune.

Modulul era ultima din cele șapte foi rămase din sămânța de 14.08.2026.
"""

COD = "MOD_VANZ_AMANUNT"

CATALOG = dict(
    sufix="AMANUNT",
    # `Index module` avea dreptate aici, `CatalogModule` dădea doar F-316: modulul chiar
    # tratează și returul (blocul de storno proporțional) și vânzarea parțială — Tabelul
    # B le numește pe amândouă în coloana „Flux”.
    fluxuri="F-14, F-40, F-43",
    tip="Pe gestiune + cotă",
    variabile="Cost, Adaos %, Cotă TVA, Gestiune",
    porti="En-gros vs Amănunt",
    blocuri="B1 Aprovizionare PVA; B2 TVA ded.; B3 Descărcare; B4 Venit; "
            "B5 Închidere TVA",
    ce_face="Gestiune amănunt: PVA, corelații, retur, vânzare parțială",
    cand="La operațiuni amănunt + închidere lună amănunt",
    activ="NU",
)

#: pas, cont Dr, cont Cr, sumă (sursă), condiție, temei / observație
SECVENTA = [
    (1, "371.gest.cotă", "401 + 378 + 4428", "PVA = cost+adaos+TVA_PVA",
     "La aprovizionare amănunt", "Stoc la preț de vânzare cu amănuntul"),
    (2, "4426", "401", "cost × cotă", "Din factură furnizor",
     "TVA deductibilă ≠ TVA din PVA"),
    (3, "607 + 378 + 4428", "371.gest.cotă", "proporțional pe PVA vândut",
     "La vânzare / Z-report", "Descărcare proporțională (nu doar cost)"),
    (4, "531/512", "707 + 4427", "bază + TVA = PVA vândut", "La vânzare",
     "Venit pe bază (cost+adaos), TVA colectată"),
    (5, "4427", "4426 + 4423", "rulaje lunare", "La închidere TVA",
     "Vezi MOD_INCHIDERE_TVA"),
    (6, "707 + 4427", "411/531", "proporțional retur", "La retur client",
     "Storno venit+TVA; apoi reîncarcă 371+378+4428 (F-40)"),
]

#: id, formulă, când, ce o rupe legitim, ce o rupe suspect, flux
CORELATII = [
    ("C-01", "sold 371 × c/(100+c) = sold 4428", "Pe gestiune+cotă, oricând",
     "Vânzare parțială, retur, transfer gestiuni",
     "4428 omis; descărcare fără 378/4428", "F-14, F-40, F-43"),
    ("C-02", "707 − 607 = rulaj D 378", "Pe perioadă",
     "Retur, 709, discount furnizor pe stoc vândut",
     "607 greșit; 378 nestins", "F-14, F-40, F-43"),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_AMANUNT", {"A": 36, "B": 26, "C": 52})
    d.titlu("MOD_VANZ_AMANUNT — Declarații (input)")
    d.nota("Gestiune amănunt la PVA. Corelații: 371×c/(100+c)=4428 și 707−607=rulaj D "
           "378. Completează galben.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    gestiune = d.kv("Gestiune (analitic)", "AM.21")
    luna = d.kv("Luna", "2026-07")
    data_a = d.kv("Data aprovizionare", "2026-07-05")
    data_v = d.kv("Data vânzare (Z-report)", "2026-07-31")
    d.gol()

    d.sectiune("2. Aprovizionare")
    cost = d.kv("Cost (fără TVA)", 10000)
    proc_adaos = d.kv("Adaos %", 0.3)
    cota = d.kv("Cotă TVA", 0.21)
    adaos = d.kv("Adaos (lei)", f"={cost}*{proc_adaos}", tip="calc")
    baza = d.kv("Bază PVA (cost+adaos)", f"={cost}+{adaos}", tip="calc")
    tva_pva = d.kv("TVA în PVA", f"={baza}*{cota}", tip="calc")
    pva = d.kv("PVA total (371)", f"={baza}+{tva_pva}", tip="calc")
    tva_ded = d.kv("TVA deductibilă (pe cost)", f"={cost}*{cota}", tip="calc")
    d.gol()

    d.sectiune("3. Conturi")
    c_371 = d.kv("Cont stoc (371.gest.cotă)", "371.AM.21")
    c_378 = d.kv("Cont adaos (378)", "378.AM.21")
    c_4428 = d.kv("Cont TVA neexigibilă (4428)", "4428.AM")
    c_furn = d.kv("Cont furnizor", "401.RO")
    c_4426 = d.kv("Cont TVA deductibilă", "4426")
    c_607 = d.kv("Cont cheltuială (607)", "607")
    c_707 = d.kv("Cont venit (707)", "707")
    c_4427 = d.kv("Cont TVA colectată", "4427")
    c_casa = d.kv("Cont casă / bancă", "531.1")
    c_4423 = d.kv("Cont TVA de plată", "4423")
    d.gol()

    # Corelațiile se verifică AICI, pe cifrele introduse, nu doar în jurnal: dacă adaosul
    # sau cota sunt greșite, se vede înainte de a genera vreo notă.
    d.sectiune("4. Corelații (auto)")
    cor1 = d.kv("Corelație 1: 371×c/(100+c) =?", f"={pva}*{cota}/(1+{cota})",
                tip="calc")
    verdict1 = d.kv("Trebuie = 4428",
                    f'=IF(ABS({cor1}-{tva_pva})<0.01,"OK — corelație 1 ține","EROARE")',
                    tip="calc")
    cor2 = d.kv("Corelație 2: 707−607 =?", f"={baza}-{cost}", tip="calc")
    verdict2 = d.kv("Trebuie = adaos (rulaj D 378)",
                    f'=IF(ABS({cor2}-{adaos})<0.01,"OK — corelație 2 ține","EROARE")',
                    tip="calc")
    d.gol()

    d.sectiune("5. Sufix")
    sufix = d.kv("Sufix", f'="— amănunt " & {gestiune} & " — " & {luna}', tip="calc")

    # ------------------------------------------------------------------- Reguli
    g = F("Reguli_AMANUNT",
          {"A": 8, "B": 34, "C": 26, "D": 40, "E": 36, "F": 22})
    g.titlu("MOD_VANZ_AMANUNT — Reguli (tabele fixe)")
    g.nota("Regula e dată, nu formulă. Se editează doar când se schimbă politica de "
           "gestiune sau cotele.")
    g.gol()

    g.sectiune("Tabel A — Secvența operațională")
    g.cap(["Pas", "Cont Dr", "Cont Cr", "Sumă (sursă)", "Condiție",
           "Temei / observație"])
    for rand in SECVENTA:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel B — Corelații de control (obligatorii pe cifre)")
    g.cap(["ID", "Formulă", "Când", "Ce o rupe legitim", "Ce o rupe suspect", "Flux"])
    for rand in CORELATII:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel C — Porți")
    for linie in [
        "• ΣDr=ΣCr pe fiecare bloc (verificare cu ABS la global — erorile nu se anulează)",
        "• După vânzare integrală: sold 371=378=4428=0 pe gestiune",
        "• Vânzare parțială: C-01 pe soldul RĂMAS, nu pe rulajul de la intrare",
        "• Retur: reîncarcă proporțional 371+378+4428 — omisiunea 378/4428 = ruptură "
        "suspectă C-01",
    ]:
        g.nota(linie)

    # ------------------------------------------------------------------ Jurnale
    j = F("Jurnale_AMANUNT",
          {"A": 32, "B": 16, "C": 14, "D": 46, "E": 16, "F": 14, "G": 46})
    j.titlu("MOD_VANZ_AMANUNT — Jurnale")
    j.gol()

    D = d.ref
    antet = ["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr",
             "Descriere Cr"]

    # Articol compus: UN debit pe 371 la PVA, contra TREI credite (cost, adaos, TVA).
    j.sectiune("Bloc 1 — Aprovizionare la PVA")
    j.kv("Data:", f"={D(data_a)}", tip="calc")
    j.cap(antet)
    b1a = j.rand([1, f"={D(c_371)}", f"={D(pva)}",
                  f'="Intrare stoc la PVA " & {D(sufix)}',
                  f"={D(c_furn)}", f"={D(cost)}",
                  f'="Datorie furnizor (cost) " & {D(sufix)}'])
    b1b = j.rand([2, 0, 0, None, f"={D(c_378)}", f"={D(adaos)}",
                  f'="Adaos comercial " & {D(sufix)}'])
    b1c = j.rand([3, 0, 0, None, f"={D(c_4428)}", f"={D(tva_pva)}",
                  f'="TVA neexigibilă în PVA " & {D(sufix)}'])
    c1 = j.check("Check B1 (371 = cost+adaos+TVA PVA)",
                 f"={b1a['C']}-({b1a['F']}+{b1b['F']}+{b1c['F']})",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    # TVA deductibilă se calculează pe COST, nu pe PVA. Confuzia celor două e una din
    # erorile pe care Tabelul A le numește explicit.
    j.sectiune("Bloc 2 — TVA deductibilă din factură")
    j.cap(antet)
    b2 = j.rand([1, f"={D(c_4426)}", f"={D(tva_ded)}",
                 f'="TVA deductibilă pe cost " & {D(sufix)}',
                 f"={D(c_furn)}", f"={D(tva_ded)}",
                 f'="Datorie furnizor (TVA) " & {D(sufix)}'])
    c2 = j.check("Check B2", f"={b2['C']}-{b2['F']}",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    # Trei debite contra unui credit: descărcarea proporțională. Făcută doar pe cost,
    # 378 și 4428 rămân încărcate și ambele corelații se rup.
    j.sectiune("Bloc 3 — Descărcare gestiune la PVA")
    j.kv("Data:", f"={D(data_v)}", tip="calc")
    j.cap(antet)
    b3a = j.rand([1, f"={D(c_607)}", f"={D(cost)}",
                  f'="Descărcare la cost " & {D(sufix)}',
                  f"={D(c_371)}", f"={D(pva)}",
                  f'="Stingere stoc PVA " & {D(sufix)}'])
    b3b = j.rand([2, f"={D(c_378)}", f"={D(adaos)}",
                  f'="Stingere adaos " & {D(sufix)}', 0, 0])
    b3c = j.rand([3, f"={D(c_4428)}", f"={D(tva_pva)}",
                  f'="Stingere TVA neexigibilă " & {D(sufix)}', 0, 0])
    c3 = j.check("Check B3",
                 f"=({b3a['C']}+{b3b['C']}+{b3c['C']})-{b3a['F']}",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Bloc 4 — Venit + TVA colectată")
    j.cap(antet)
    b4a = j.rand([1, f"={D(c_casa)}", f"={D(pva)}",
                  f'="Încasare amănunt " & {D(sufix)}',
                  f"={D(c_707)}", f"={D(baza)}",
                  f'="Venit amănunt (bază) " & {D(sufix)}'])
    b4b = j.rand([2, 0, 0, None, f"={D(c_4427)}", f"={D(tva_pva)}",
                  f'="TVA colectată " & {D(sufix)}'])
    c4 = j.check("Check B4", f"={b4a['C']}-({b4a['F']}+{b4b['F']})",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Bloc 5 — Închidere TVA")
    j.cap(antet)
    b5a = j.rand([1, f"={D(c_4427)}", f"={D(tva_pva)}",
                  f'="Închidere TVA colectată " & {D(sufix)}',
                  f"={D(c_4426)}", f"={D(tva_ded)}",
                  f'="Închidere TVA deductibilă " & {D(sufix)}'])
    b5b = j.rand([2, 0, 0, None, f"={D(c_4423)}",
                  f"={D(tva_pva)}-{D(tva_ded)}",
                  f'="TVA de plată " & {D(sufix)}'])
    c5 = j.check("Check B5", f"={b5a['C']}-({b5a['F']}+{b5b['F']})",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    glob = j.check("Check global",
                   f"=ABS({c1})+ABS({c2})+ABS({c3})+ABS({c4})+ABS({c5})",
                   f'=IF(B{j.r}<0.01,"OK — toate blocurile se închid",'
                   f'"EROARE — cel puțin un bloc dezechilibrat")')
    j.gol()
    j.sectiune("Corelații (din Declarații)")
    j.rand([f"={D(verdict1)}"])
    j.rand([f"={D(verdict2)}"])

    # --------------------------------------------------------------- NotaExport
    e = F("NotaExport_AMANUNT",
          {"A": 6, "B": 8, "C": 14, "D": 14, "E": 14, "F": 14, "G": 14, "H": 12,
           "I": 10})
    e.titlu("MOD_VANZ_AMANUNT — Notă pentru import")
    # Două rânduri goale, nu unul: foaia asta n-are notă sub titlu, iar antetul stă pe
    # rândul 4 în sămânță. Cu un singur gol, tot ce urmează se deplasează cu un rând și
    # formulele de control ajung să citeze alte coordonate decât originalul.
    e.gol(2)
    e.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    # (bloc, data, cont Dr, cont Cr, sumă, descriere scurtă)
    linii = [
        ("B1", data_a, b1a["B"], b1a["E"], b1a["F"], "Cost"),
        ("B1", data_a, b1a["B"], b1b["E"], b1b["F"], "Adaos"),
        ("B1", data_a, b1a["B"], b1c["E"], b1c["F"], "TVA PVA"),
        ("B2", data_a, b2["B"], b2["E"], b2["C"], "TVA ded"),
        ("B3", data_v, b3a["B"], b3a["E"], b3a["C"], "Desc cost"),
        ("B3", data_v, b3b["B"], b3a["E"], b3b["C"], "Desc adaos"),
        ("B3", data_v, b3c["B"], b3a["E"], b3c["C"], "Desc 4428"),
        ("B4", data_v, b4a["B"], b4a["E"], b4a["F"], "Venit"),
        ("B4", data_v, b4a["B"], b4b["E"], b4b["F"], "TVA col"),
        ("B5", data_v, b5a["B"], b5a["E"], b5a["F"], "Înch 4426"),
        ("B5", data_v, b5a["B"], b5b["E"], b5b["F"], "TVA plată"),
    ]
    for i, (bloc, data, cd, cc, suma, desc) in enumerate(linii, start=1):
        e.rand([i, bloc, f"={D(data)}", f"={j.ref(cd)}", f"={j.ref(cc)}",
                f"={j.ref(suma)}", desc, "Amănunt",
                f'=IF(AND(ISNUMBER(F{e.r}),F{e.r}>0),"DA","NU")'])
    e.gol()
    e.check("Check global", f"={j.ref(glob)}",
            f'=IF(ABS(B{e.r})<0.01,"OK","EROARE")')
