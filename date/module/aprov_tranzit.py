"""MOD_APROV_TRANZIT — factura sosește înaintea mărfii: 32x → stoc real.

Acoperă F-02.

Contul 32x are rol de **tranzit**: destinația e cunoscută (marfa se știe ce va deveni),
așteaptă doar un PAS — recepția. Pasul revelator e stingerea `371 = 327` la NIR. Fără el,
stocul rămâne subevaluat și 327 rămâne deschis la infinit — cele două erori merg mereu
împreună, pentru că sunt aceeași eroare privită din două părți.

Cazul SIMETRIC — marfa sosește înaintea facturii — nu e aici: acela trece prin 408, are
rol de *intermediar* (așteaptă un eveniment discret, documentul), și e MOD_INTERMEDIAR.
Tabelul B îl numește explicit ca să nu fie căutat aici.

Modulul era una din cele șapte foi rămase din sămânța de 14.08.2026.
"""
from .comun import formula_activ

COD = "MOD_APROV_TRANZIT"

CATALOG = dict(
    fluxuri="F-02",
    tip="Eveniment + stingere",
    variabile="Sumă netă, TVA, Cont stoc, Furnizor, Data factură, Data recepție",
    porti="Tranzit vs. direct",
    blocuri="B1 Factură→32x; B2 Recepție 30x=32x",
    ce_face="32x: factură înainte de marfă / NIR înainte de factură",
    cand="La aprovizionări incomplete",
    activ="NU",
)

#: pas, moment, cont Dr, cont Cr, sumă, temei / observație
SECVENTA = [
    (1, "Factură (marfă pe drum)", "327 (tranzit)", "401.RO", "Netă",
     "Rol: Tranzit / reflectare — destinația cunoscută, așteaptă recepția"),
    (2, "Factură — TVA", "4426", "401.RO", "TVA",
     "Tranzit TVA; se închide lunar în 4423/4424"),
    (3, "Recepție NIR", "371 (sau 301)", "327", "Netă",
     "Stingere tranzit → stoc real (pas revelator)"),
]

#: cont, denumire, rol, observație
CONTURI = [
    ("327", "Mărfuri în curs de aprovizionare", "Tranzit / reflectare",
     "Se stinge 371=327 la recepție. Fără pasul de stingere → stoc subevaluat + "
     "327 deschis"),
    ("321-328", "Familia 32x", "Tranzit / reflectare",
     "321 materii, 322 consumabile, 323 obiecte inventar, 327 mărfuri, 328 ambalaje"),
    ("371 / 301", "Stoc real", "Patrimonial — Stoc", "Destinația finală după recepție"),
    ("401.RO", "Furnizori RO", "Patrimonial — Datorie",
     "Analitic pe rezidență pentru D394"),
    ("4426", "TVA deductibilă", "Tranzit / reflectare",
     "Fără sold după închiderea lunară"),
    ("408", "Furnizori — facturi nesosite", "Intermediar / clarificare",
     "Cazul SIMETRIC (marfă înainte de factură) — modul separat MOD_INTERMEDIAR"),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_APROV_TRANZIT", {"A": 54, "B": 26, "C": 52})
    d.titlu("MOD_APROV_TRANZIT — Declarații (input)")
    d.nota("Completează doar celulele galbene. Modulul acoperă: factură înainte de "
           "recepție (32x) + stingere la recepție. Cazul simetric 408 (marfă înainte de "
           "factură) se notează, dar se activează separat dacă e nevoie.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    d.kv("CUI", "=Parametri!B6", tip="calc")
    luna = d.kv("Luna (AAAA-LL)", "2026-07")
    data_f = d.kv("Data factură (jurnal B1)", "2026-07-10")
    data_r = d.kv("Data recepție NIR (jurnal B2)", "2026-07-18")
    furnizor = d.kv("Furnizor (denumire scurtă)", "Furnizor DEMO")
    nr_f = d.kv("Nr. factură / document", "F-1234/10.07.2026")
    d.gol()

    d.sectiune("2. Sume factură")
    net = d.kv("Valoare netă (fără TVA)", 8000)
    cota = d.kv("Cota TVA", 0.21)
    tva = d.kv("TVA (calculat)", f"={net}*{cota}", tip="calc")
    d.kv("Total factură", f"={net}+{tva}", tip="calc")
    d.gol()

    d.sectiune("3. Politică de conturi")
    c_stoc = d.kv("Cont stoc final (după recepție)", "371")
    c_tranzit = d.kv("Cont tranzit (32x)", "327")
    c_furn = d.kv("Cont furnizor", "401.RO")
    c_tva = d.kv("Cont TVA deductibilă", "4426")
    platitor = d.kv("Platitor TVA? (DA/NU)", "DA")
    d.gol()

    d.sectiune("4. Poartă — tip eveniment")
    p_factura = d.kv("Factură înainte de marfă? (DA = tranzit 32x)", "DA")
    p_marfa = d.kv("Marfă înainte de factură? (DA = 408 — nu e acoperit de acest modul)",
                   "NU")
    d.kv("Notă poartă",
         f'=IF(AND({p_factura}="DA",{p_marfa}="NU"),"Cale standard F-02: 32x → stoc",'
         f'"Verifică: dacă ambele DA sau ambele NU, situația nu e tranzit clasic")',
         tip="calc")
    d.gol()

    d.sectiune("5. Sufix descriere (generat)")
    sufix = d.kv("Sufix", f'="— " & {luna} & " — " & {furnizor} & " — " & {nr_f}',
                 tip="calc")
    d.gol()

    d.sectiune("6. Control modul")
    d.kv("Modul activ în Catalog?", formula_activ(COD), tip="calc")

    # ------------------------------------------------------------------- Reguli
    g = F("Reguli_APROV_TRANZIT",
          {"A": 10, "B": 30, "C": 20, "D": 20, "E": 12, "F": 58})
    g.titlu("MOD_APROV_TRANZIT — Reguli (tabele fixe)")
    g.nota("Regula este dată, nu formulă. Se editează doar la schimbare de lege sau "
           "politică.")
    g.gol()

    g.sectiune("Tabel A — Secvența de înregistrare (calea standard F-02)")
    g.cap(["Pas", "Moment", "Cont Dr", "Cont Cr", "Sumă", "Temei / observație"])
    for rand in SECVENTA:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel B — Conturi din planul pe rol")
    g.cap(["Cont", "Denumire", "Rol", "Observație"])
    for rand in CONTURI:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel C — Porți de calitate")
    for linie in [
        "• ΣDr = ΣCr pe fiecare bloc (B1 factură, B2 recepție)",
        "• După B2: sold 327 = 0",
        "• Dacă poarta „Factură înainte de marfă” = NU → modulul nu ar trebui activat "
        "(calea e F-01 direct)",
        "• 408 nu se folosește în acest modul (e oglinda simetrică)",
    ]:
        g.nota(linie)

    # ------------------------------------------------------------------ Jurnale
    j = F("Jurnale_APROV_TRANZIT",
          {"A": 28, "B": 16, "C": 14, "D": 50, "E": 16, "F": 14, "G": 50})
    j.titlu("MOD_APROV_TRANZIT — Jurnale (generate automat)")
    j.nota("Nu se scrie nimic manual. Sumele și descrierile vin din "
           "Declarații_APROV_TRANZIT.")
    j.gol()

    D = d.ref
    # TVA intră în notă doar dacă firma e plătitoare. La neplătitor, TVA-ul e cost și
    # merge în valoarea stocului — altă cale, nu acest modul; aici rândul iese 0.
    tva_daca = f'=IF({D(platitor)}="DA",{D(tva)},0)'

    j.sectiune("Bloc 1 — Factură (marfă pe drum) — rol Tranzit")
    j.kv("Data jurnal:", f"={D(data_f)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr",
           "Descriere Cr"])
    b1a = j.rand([1, f"={D(c_tranzit)}", f"={D(net)}",
                  f'="Marfă în curs de aprovizionare " & {D(sufix)}',
                  f"={D(c_furn)}", f"={D(net)}",
                  f'="Datorie furnizor (net) " & {D(sufix)}'])
    b1b = j.rand([2, f"={D(c_tva)}", tva_daca,
                  f'="TVA deductibilă pe factură în tranzit " & {D(sufix)}',
                  f"={D(c_furn)}", tva_daca,
                  f'="Datorie furnizor (TVA) " & {D(sufix)}'])
    j.gol()
    j.sectiune("Sumar Bloc 1")
    t1d = j.kv("Total Dr", f"={b1a['C']}+{b1b['C']}", tip="calc")
    t1c = j.kv("Total Cr", f"={b1a['F']}+{b1b['F']}", tip="calc")
    c1 = j.check("Check B1", f"={t1d}-{t1c}",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Bloc 2 — Recepție NIR — stingere tranzit (pas revelator)")
    j.kv("Data jurnal:", f"={D(data_r)}", tip="calc")
    j.gol()
    j.cap(["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr",
           "Descriere Cr"])
    b2 = j.rand([1, f"={D(c_stoc)}", f"={D(net)}",
                 f'="Recepție stoc real (stingere tranzit) " & {D(sufix)}',
                 f"={D(c_tranzit)}", f"={D(net)}",
                 f'="Stingere 32x " & {D(sufix)}'])
    j.gol()
    j.sectiune("Sumar Bloc 2")
    t2d = j.kv("Total Dr", f"={b2['C']}", tip="calc")
    t2c = j.kv("Total Cr", f"={b2['F']}", tip="calc")
    c2 = j.check("Check B2", f"={t2d}-{t2c}",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Stare terminală așteptată")
    j.nota("Sold 327 = 0 | Stoc 371 (sau 301) reflectă marfa | 401 = total factură | "
           "4426 conține TVA (se închide la final de lună cu MOD_INCHIDERE_TVA)")
    j.gol()
    glob = j.check("Check global (toate blocurile)", f"=ABS({c1})+ABS({c2})",
                   f'=IF(B{j.r}<0.01,"OK — toate blocurile se închid",'
                   f'"EROARE — cel puțin un bloc dezechilibrat")')

    # --------------------------------------------------------------- NotaExport
    e = F("NotaExport_APROV_TRANZIT",
          {"A": 6, "B": 24, "C": 14, "D": 12, "E": 12, "F": 14, "G": 50, "H": 24,
           "I": 10})
    e.titlu("MOD_APROV_TRANZIT — Notă pentru import")
    e.nota("Filtrează Include=DA. Bloc 1 = data facturii; Bloc 2 = data recepției "
           "(pot fi luni diferite).")
    e.gol()
    e.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    primul = e.r
    for i, (bloc, data, r, doc) in enumerate([
        ("Bloc 1 — Factură tranzit", D(data_f), b1a, f"={D(nr_f)}"),
        ("Bloc 1 — Factură tranzit", D(data_f), b1b, f"={D(nr_f)}"),
        ("Bloc 2 — Recepție", D(data_r), b2, "NIR"),
    ], start=1):
        e.rand([i, bloc, f"={data}", f"={j.ref(r['B'])}", f"={j.ref(r['E'])}",
                f"={j.ref(r['C'])}", f"={j.ref(r['D'])}", doc,
                f'=IF(F{e.r}>0,"DA","NU")'])
    ultim = e.r - 1
    e.gol()
    e.kv("Rânduri de importat", f'=COUNTIF(I{primul}:I{ultim},"DA")', tip="calc")
    e.check("Check global", f"={j.ref(glob)}",
            f'=IF(ABS(B{e.r})<0.01,"OK","EROARE")')
