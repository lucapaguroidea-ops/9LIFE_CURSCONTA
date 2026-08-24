"""MOD_AVANSURI — 419 și 409: banii care sosesc înaintea livrării.

Acoperă F-25 (avansuri clienți / furnizori) și F-63 (supraîncasare).

Avansul cu TVA se înregistrează INTEGRAL la primire sau la plată. La factura finală se
stinge capitalul avansului, se completează diferența de valoare și se adaugă doar
**restul** de TVA — nu tot TVA-ul facturii, pentru că o parte din el a fost deja
colectată sau dedusă la avans.

    avans     5.000 + TVA 1.050 =  6.050
    factură  12.000 + TVA 2.520 = 14.520
    din care TVA:  1.050 (deja) + 1.470 (rest) = 2.520
    rămâne pe 411: 14.520 − 6.050 = 8.470

Cine re-colectează TVA pe toată factura finală plătește de două ori pe aceeași bază.
Garda din foaia de control compară TVA-ul avansului plus restul cu TVA-ul total.

## Supraîncasarea e același mecanism, intrat pe ușa din dos

Un sold CREDITOR pe 4111 nu e o curiozitate de balanță — e un avans neînregistrat.
Contul de creanță a trecut pe credit pentru că partenerul a virat mai mult decât
factura, iar diferența e o datorie față de el.

Două lucruri se greșesc aici, amândouă din același reflex:

- **diferența pusă pe 472** („venituri în avans"). Nu e venit: nu s-a livrat nimic
  pentru ea. E datorie — deci 419.
- **diferența pusă integral pe 419**, fără să se extragă TVA-ul. Suma încasată e
  TVA-inclusivă, deci se împarte la 1 + cotă: 5.000 ÷ 1,21 = 4.132,23 bază și 867,77
  TVA. Fără pasul ăsta TVA-ul rămâne necolectat și **nimic nu semnalează** — de-aia e
  pasul revelator al fluxului.

TVA-ul se colectează chiar dacă banii se returnează luna următoare. Dacă încasarea și
restituirea se închid în aceeași lună, situația se neutralizează singură.
"""
from .comun import formula_activ, sectiune_temei

COD = "MOD_AVANSURI"

CATALOG = dict(
    fluxuri="F-25, F-63",
    tip="Pe avans / pe extras",
    variabile="Avansul și factura finală, la client și la furnizor; suma încasată peste "
              "factură",
    porti="TVA avans + rest = TVA totală; 419 și 409 se închid la zero",
    blocuri="A Avans client; B Factură finală client; C Avans furnizor; D Recepție "
            "furnizor; E Supraîncasare",
    ce_face="419/409: avans cu TVA, stingere la factura finală, supraîncasare",
    cand="La fiecare avans și la orice sold creditor pe 4111",
    activ="NU",
)

#: situație, unde merge suma, de ce NU altundeva
UNDE_MERGE = [
    ("Avans încasat de la client", "419 + 4427",
     "Nu 704/707: nu s-a livrat nimic. Datorie, nu venit."),
    ("Avans plătit furnizorului", "409 + 4426",
     "Nu 6xx și nu 3xx: nu s-a primit nimic. Creanță, nu cost."),
    ("Încasare peste valoarea facturii", "419 + 4427, pe diferență",
     "Nu 472 (nu e venit în avans) și nu 758. E datorie față de partener."),
    ("Sold creditor rămas pe 4111", "se reclasifică pe 419",
     "Un cont de activ cu sold contrar naturii lui = avans neînregistrat (C-23)."),
    ("TVA din suma încasată peste factură", "se extrage: sumă ÷ (1 + cotă)",
     "Suma virată e TVA-inclusivă. Pusă integral pe 419, TVA rămâne necolectată."),
]


#: (ce se sprijină pe el, temei) — secțiunea finală din `Reguli`.
TEMEI_LEGAL = [
    ('TVA devine exigibilă la data încasării avansului, înainte de livrare',
     'art. 282 alin. (2) lit. b) Cod fiscal'),
    ('La factura finală se regularizează avansul facturat anterior',
     'art. 330 alin. (1) lit. c) Cod fiscal — corectarea facturii'),
    ('Sumele încasate peste valoarea facturii sunt datorie față de client, nu venit',
     'OMFP 1802/2014 — funcțiunea contului 419'),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_AVANSURI", {"A": 52, "B": 22, "C": 58})
    d.titlu("MOD_AVANSURI — Declarații (input)")
    d.nota("Trei situații independente: avans de la client, avans către furnizor, "
           "supraîncasare. Pune DA pe cele care s-au întâmplat.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    d.kv("CUI", "=Parametri!B6", tip="calc")
    luna = d.kv("Luna (AAAA-LL)", "2026-07")
    data_j = d.kv("Data jurnal", "2026-07-31")
    cota = d.kv("Cota TVA", 0.21)
    d.gol()

    d.sectiune("2. Avans de la CLIENT (blocurile A și B)")
    a_on = d.kv("Se aplică? (DA/NU)", "DA")
    a_client = d.kv("Client", "Client DEMO")
    a_avans = d.kv("Avans încasat, fără TVA", 5000)
    a_avans_tva = d.kv("TVA pe avans (auto)", f"=ROUND({a_avans}*{cota},2)", tip="calc")
    a_avans_tot = d.kv("Total avans încasat (auto)", f"={a_avans}+{a_avans_tva}",
                       tip="calc")
    a_factura = d.kv("Factura finală, fără TVA", 12000)
    a_fact_tva = d.kv("TVA totală pe factură (auto)",
                      f"=ROUND({a_factura}*{cota},2)", tip="calc")
    a_fact_tot = d.kv("Total factură (auto)", f"={a_factura}+{a_fact_tva}", tip="calc")
    a_rest_tva = d.kv("REST de TVA de colectat (auto)",
                      f"={a_fact_tva}-{a_avans_tva}", tip="calc",
                      nota="Doar diferența — TVA-ul avansului a fost deja colectat")
    a_rest_val = d.kv("Rest de valoare (auto)", f"={a_factura}-{a_avans}", tip="calc")
    a_creanta = d.kv("Rămâne de încasat pe 411 (auto)",
                     f"={a_fact_tot}-{a_avans_tot}", tip="calc")
    d.gol()

    d.sectiune("3. Avans către FURNIZOR (blocurile C și D)")
    c_on = d.kv("Se aplică? (DA/NU)", "DA")
    c_furnizor = d.kv("Furnizor", "Furnizor DEMO")
    c_avans = d.kv("Avans plătit, fără TVA", 3000)
    c_avans_tva = d.kv("TVA pe avans (auto)", f"=ROUND({c_avans}*{cota},2)", tip="calc")
    c_avans_tot = d.kv("Total avans plătit (auto)", f"={c_avans}+{c_avans_tva}",
                       tip="calc")
    c_factura = d.kv("Factura de recepție, fără TVA", 8000)
    c_fact_tva = d.kv("TVA totală pe factură (auto)",
                      f"=ROUND({c_factura}*{cota},2)", tip="calc")
    c_fact_tot = d.kv("Total factură (auto)", f"={c_factura}+{c_fact_tva}", tip="calc")
    c_rest_tva = d.kv("REST de TVA de dedus (auto)", f"={c_fact_tva}-{c_avans_tva}",
                      tip="calc")
    c_rest_val = d.kv("Rest de valoare (auto)", f"={c_factura}-{c_avans}", tip="calc")
    c_datorie = d.kv("Rămâne de plătit pe 401 (auto)",
                     f"={c_fact_tot}-{c_avans_tot}", tip="calc")
    d.gol()

    d.sectiune("4. SUPRAÎNCASARE (blocul E)")
    e_on = d.kv("Se aplică? (DA/NU)", "DA")
    e_partener = d.kv("Partener", "Partener DEMO")
    e_factura = d.kv("Factura emisă, TOTAL cu TVA", 10000,
                     nota="Aici se introduce totalul, nu baza — așa vine de pe factură")
    e_baza = d.kv("Baza facturii (auto)", f"=ROUND({e_factura}/(1+{cota}),2)",
                  tip="calc")
    e_tva = d.kv("TVA pe factură (auto)", f"={e_factura}-{e_baza}", tip="calc")
    e_incasat = d.kv("Suma încasată efectiv", 15000)
    e_dif = d.kv("Diferența încasată în plus (auto)", f"={e_incasat}-{e_factura}",
                 tip="calc")
    # Pasul revelator: diferența e TVA-inclusivă, deci se DESCOMPUNE.
    e_dif_baza = d.kv("Din care bază de avans (auto)",
                      f"=ROUND({e_dif}/(1+{cota}),2)", tip="calc",
                      nota="Suma virată e TVA-inclusivă: se împarte la 1 + cotă")
    e_dif_tva = d.kv("Din care TVA de colectat (auto)", f"={e_dif}-{e_dif_baza}",
                     tip="calc")
    d.gol()

    d.sectiune("5. Conturi")
    k_411 = d.kv("Clienți", "4111")
    k_419 = d.kv("Clienți-creditori (avansuri încasate)", "419")
    k_409 = d.kv("Furnizori-debitori (avansuri plătite)", "409")
    k_401 = d.kv("Furnizori", "401.RO")
    k_707 = d.kv("Venit", "707")
    k_stoc = d.kv("Cont stoc / cheltuială", "371")
    k_4426 = d.kv("TVA deductibilă", "4426")
    k_4427 = d.kv("TVA colectată", "4427")
    k_banca = d.kv("Bancă", "5121")
    d.gol()

    d.sectiune("6. Sufix")
    sufix = d.kv("Sufix", f'="— avansuri " & {luna}', tip="calc")
    d.gol()

    d.sectiune("7. Control")
    d.kv("Modul activ?", formula_activ(COD), tip="calc")
    ver_tva_client = d.kv(
        "Verificare: TVA avans + rest = TVA totală (client)",
        f'=IF(OR({a_on}<>"DA",ABS(({a_avans_tva}+{a_rest_tva})-{a_fact_tva})<0.01),'
        f'"OK — TVA nu se colectează de două ori",'
        f'"EROARE — TVA recolectată pe toată factura")', tip="calc")
    ver_tva_furn = d.kv(
        "Verificare: TVA avans + rest = TVA totală (furnizor)",
        f'=IF(OR({c_on}<>"DA",ABS(({c_avans_tva}+{c_rest_tva})-{c_fact_tva})<0.01),'
        f'"OK — TVA nu se deduce de două ori",'
        f'"EROARE — TVA redusă pe toată factura")', tip="calc")
    # Garda asta a trebuit rescrisă. Prima formă compara (bază + TVA) cu diferența —
    # dar TVA e DEFINITĂ ca diferență minus bază, deci egalitatea era garantată
    # algebric și celula ieșea verde chiar și când toată suma ajungea pe 419.
    #
    # Aici se compară două căi de calcul DIFERITE pentru aceeași mărime:
    #     dif − dif/(1+cotă)      (calea folosită în Declarații)
    #     dif × cotă/(1+cotă)     (calea de control, independentă)
    # Algebric egale, dar calculate altfel — deci o rescriere a uneia n-o mișcă pe
    # cealaltă, iar diferența se vede. E același tipar cu corelațiile 1 și 2 din
    # MOD_VANZ_AMANUNT, care se verifică tot prin a doua formulă.
    ver_descompunere = d.kv(
        "Verificare: TVA extrasă corect din suma încasată",
        f'=IF(OR({e_on}<>"DA",'
        f'ABS({e_dif_tva}-ROUND({e_dif}*{cota}/(1+{cota}),2))<0.01),'
        f'"OK — TVA extrasă din suma încasată",'
        f'"EROARE — diferența pusă integral pe 419, TVA necolectată")', tip="calc")
    d.kv("Atenție la 472",
         f'=IF({e_on}="DA",'
         f'"Diferența NU merge pe 472: nu e venit în avans, e datorie față de partener. '
         f'Merge pe 419.","—")', tip="calc")

    # ------------------------------------------------------------------- Reguli
    g = F("Reguli_AVANSURI", {"A": 42, "B": 34, "C": 62})
    g.titlu("MOD_AVANSURI — Reguli (tabele fixe)")
    g.nota("Regula e dată, nu formulă. Tabelul A răspunde la singura întrebare care se "
           "pune în practică: unde merge suma.")
    g.gol()

    g.sectiune("Tabel A — Unde merge suma, și de ce nu altundeva")
    g.cap(["Situație", "Unde merge", "De ce NU altundeva"])
    for rand in UNDE_MERGE:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel B — Aritmetica avansului")
    for linie in [
        "Avansul cu TVA se înregistrează INTEGRAL la primire sau la plată.",
        "La factura finală se stinge capitalul avansului, se completează diferența de "
        "valoare și se adaugă doar RESTUL de TVA.",
        "TVA avans + TVA rest = TVA totală a facturii. Cine recolectează TVA pe toată "
        "factura plătește de două ori pe aceeași bază.",
        "Suma încasată peste factură e TVA-inclusivă: se împarte la 1 + cotă ca să se "
        "separe baza de TVA.",
    ]:
        g.nota(linie)
    g.gol()

    g.sectiune("Tabel C — Porți de calitate")
    for linie in [
        "• ΣDr = ΣCr pe fiecare bloc",
        "• Sold 419 = 0 și sold 409 = 0 după livrare / recepție",
        "• Sold 4111 = 0 pe partenerul supraîncasat, după reclasificare",
        "• Un sold CREDITOR pe 4111 e avans neînregistrat, nu eroare de încasare (C-23)",
        "• TVA-ul din supraîncasare se colectează chiar dacă banii se returnează luna "
        "următoare; dacă încasarea și restituirea se închid în aceeași lună, se "
        "neutralizează",
        "• La regimul TVA la încasare, TVA-ul avansului trece prin 4428.INC — vezi "
        "MOD_TVA_INCASARE",
    ]:
        g.nota(linie)

    sectiune_temei(g, TEMEI_LEGAL)

    # ------------------------------------------------------------------ Jurnale
    j = F("Jurnale_AVANSURI",
          {"A": 40, "B": 16, "C": 14, "D": 52, "E": 16, "F": 14, "G": 52})
    j.titlu("MOD_AVANSURI — Jurnale (generate automat)")
    j.nota("Blocurile B și D sunt articole compuse: factura finală stinge avansul ȘI "
           "înregistrează restul, într-o singură notă.")
    j.gol()

    D = d.ref
    antet = ["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr",
             "Descriere Cr"]

    def daca(comutator, valoare):
        return f'=IF({D(comutator)}="DA",{D(valoare)},0)'

    j.sectiune("Bloc A — Avans încasat de la client")
    j.kv("Data:", f"={D(data_j)}", tip="calc")
    j.cap(antet)
    a1 = j.rand([1, f"={D(k_banca)}", daca(a_on, a_avans_tot),
                 f'="Încasare avans client " & {D(a_client)} & " " & {D(sufix)}',
                 f"={D(k_419)}", daca(a_on, a_avans),
                 f'="Datorie din avans (bază) " & {D(sufix)}'])
    a2 = j.rand([2, 0, 0, None, f"={D(k_4427)}", daca(a_on, a_avans_tva),
                 f'="TVA colectată pe avans " & {D(sufix)}'])
    ca = j.check("Check A", f"={a1['C']}-({a1['F']}+{a2['F']})",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Bloc B — Factura finală + stingerea avansului")
    j.cap(antet)
    b1 = j.rand([1, f"={D(k_419)}", daca(a_on, a_avans),
                 f'="Stingerea avansului (bază) " & {D(sufix)}',
                 f"={D(k_707)}", daca(a_on, a_factura),
                 f'="Venit din vânzare (total factură) " & {D(sufix)}'])
    b2 = j.rand([2, f"={D(k_411)}", daca(a_on, a_creanta),
                 f'="Rest de încasat de la client " & {D(sufix)}',
                 f"={D(k_4427)}", daca(a_on, a_rest_tva),
                 f'="REST de TVA colectată (nu toată factura) " & {D(sufix)}'])
    # Fără rând de stornare. Monografia nu stornează TVA-ul avansului: acela a fost
    # colectat la încasare și acolo rămâne. La factura finală se înregistrează doar
    # RESTUL, iar cele două rânduri se echilibrează singure:
    #     5.000 + 8.470 = 12.000 + 1.470 = 13.470
    # Prima versiune avea un al treilea rând care debita 4427 cu 1.050 fără credit
    # corespondent — jumătate de stornare, care dezechilibra nota cu exact suma aia.
    cb = j.check("Check B",
                 f"=({b1['C']}+{b2['C']})-({b1['F']}+{b2['F']})",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    cb2 = j.check("Check B2 (419 se închide la zero)",
                  f"={a1['F']}-{b1['C']}",
                  f'=IF(ABS(B{j.r})<0.01,"OK — sold 419 = 0",'
                  f'"EROARE — avansul nu s-a stins integral")')
    j.gol()

    j.sectiune("Bloc C — Avans plătit furnizorului")
    j.cap(antet)
    c1 = j.rand([1, f"={D(k_409)}", daca(c_on, c_avans),
                 f'="Avans plătit furnizorului (bază) " & {D(sufix)}',
                 f"={D(k_banca)}", daca(c_on, c_avans_tot),
                 f'="Ieșire bancă (total avans) " & {D(sufix)}'])
    c2 = j.rand([2, f"={D(k_4426)}", daca(c_on, c_avans_tva),
                 f'="TVA deductibilă pe avans " & {D(sufix)}', 0, 0])
    cc = j.check("Check C", f"=({c1['C']}+{c2['C']})-{c1['F']}",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    j.sectiune("Bloc D — Recepție + stingerea avansului furnizor")
    j.cap(antet)
    d1 = j.rand([1, f"={D(k_stoc)}", daca(c_on, c_factura),
                 f'="Stoc recepționat (total factură) " & {D(sufix)}',
                 f"={D(k_409)}", daca(c_on, c_avans),
                 f'="Stingerea avansului (bază) " & {D(sufix)}'])
    d2 = j.rand([2, f"={D(k_4426)}", daca(c_on, c_rest_tva),
                 f'="REST de TVA deductibilă " & {D(sufix)}',
                 f"={D(k_401)}", daca(c_on, c_datorie),
                 f'="Rest de plătit furnizorului " & {D(sufix)}'])
    # Simetric cu blocul B: fără stornare, doar restul de TVA.
    #     8.000 + 1.050 = 3.000 + 6.050 = 9.050
    cd = j.check("Check D",
                 f"=({d1['C']}+{d2['C']})-({d1['F']}+{d2['F']})",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    cd2 = j.check("Check D2 (409 se închide la zero)",
                  f"={c1['C']}-{d1['F']}",
                  f'=IF(ABS(B{j.r})<0.01,"OK — sold 409 = 0",'
                  f'"EROARE — avansul nu s-a stins integral")')
    j.gol()

    j.sectiune("Bloc E — Supraîncasare (pas revelator)")
    j.cap(antet)
    e1 = j.rand([1, f"={D(k_411)}", daca(e_on, e_factura),
                 f'="Factura emisă (total) " & {D(sufix)}',
                 f"={D(k_707)}", daca(e_on, e_baza),
                 f'="Venit " & {D(sufix)}'])
    e2 = j.rand([2, 0, 0, None, f"={D(k_4427)}", daca(e_on, e_tva),
                 f'="TVA colectată pe factură " & {D(sufix)}'])
    ce1 = j.check("Check E1 (factura)", f"={e1['C']}-({e1['F']}+{e2['F']})",
                  f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    e3 = j.rand([3, f"={D(k_banca)}", daca(e_on, e_incasat),
                 f'="Încasare peste factură " & {D(sufix)}',
                 f"={D(k_411)}", daca(e_on, e_incasat),
                 f'="Creanța stinsă și depășită — 4111 trece pe credit " & {D(sufix)}'])
    ce2 = j.check("Check E2 (încasarea)", f"={e3['C']}-{e3['F']}",
                  f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    e4 = j.rand([4, f"={D(k_411)}", daca(e_on, e_dif),
                 f'="Reclasificarea soldului creditor de pe 4111 " & {D(sufix)}',
                 f"={D(k_419)}", daca(e_on, e_dif_baza),
                 f'="Avans identificat (bază) " & {D(sufix)}'])
    e5 = j.rand([5, 0, 0, None, f"={D(k_4427)}", daca(e_on, e_dif_tva),
                 f'="TVA extrasă din suma încasată " & {D(sufix)}'])
    ce3 = j.check("Check E3 (descompunerea diferenței)",
                  f"={e4['C']}-({e4['F']}+{e5['F']})",
                  f'=IF(ABS(B{j.r})<0.01,"OK — bază + TVA = diferența încasată",'
                  f'"EROARE — TVA nu s-a extras din suma încasată")')
    j.gol()

    glob = j.check(
        "Check global",
        f"=ABS({ca})+ABS({cb})+ABS({cb2})+ABS({cc})+ABS({cd})+ABS({cd2})"
        f"+ABS({ce1})+ABS({ce2})+ABS({ce3})",
        f'=IF(B{j.r}<0.01,"OK — toate blocurile se închid",'
        f'"EROARE — cel puțin un bloc dezechilibrat")')
    j.gol()
    j.sectiune("Stare terminală")
    j.nota("Sold 419 = 0 și sold 409 = 0 după livrare / recepție. La supraîncasare: "
           "sold 4111 = 0 pe partenerul respectiv, iar diferența stă pe 419 cu TVA-ul "
           "ei colectat. TVA pe avans regularizată în D300.")

    # --------------------------------------------------------------- NotaExport
    e = F("NotaExport_AVANSURI",
          {"A": 6, "B": 30, "C": 14, "D": 12, "E": 12, "F": 14, "G": 52, "H": 24,
           "I": 10})
    e.titlu("MOD_AVANSURI — Notă pentru import")
    e.nota("Filtrează Include=DA. Situațiile neactivate ies cu sumă 0 și apar ca NU.")
    e.gol()
    e.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    primul = e.r
    linii = [
        ("A Avans client — bază", a1["B"], a1["E"], a1["F"], a1["D"], "Extras de cont"),
        ("A Avans client — TVA", a1["B"], a2["E"], a2["F"], a2["G"], "Extras de cont"),
        ("B Factură finală — stingere avans", b1["B"], b1["E"], b1["C"], b1["D"],
         "Factură"),
        ("B Factură finală — rest creanță", b2["B"], b2["E"], b2["C"], b2["D"],
         "Factură"),
        ("C Avans furnizor — bază", c1["B"], c1["E"], c1["C"], c1["D"], "Extras de cont"),
        ("C Avans furnizor — TVA", c2["B"], c1["E"], c2["C"], c2["D"], "Extras de cont"),
        ("D Recepție — stingere avans", d1["B"], d1["E"], d1["F"], d1["D"], "NIR"),
        ("D Recepție — rest datorie", d2["B"], d2["E"], d2["C"], d2["D"], "NIR"),
        ("E Supraîncasare — factura", e1["B"], e1["E"], e1["F"], e1["D"], "Factură"),
        ("E Supraîncasare — încasarea", e3["B"], e3["E"], e3["C"], e3["D"],
         "Extras de cont"),
        ("E Supraîncasare — reclasificare", e4["B"], e4["E"], e4["F"], e4["D"],
         "Notă contabilă"),
        ("E Supraîncasare — TVA extrasă", e4["B"], e5["E"], e5["F"], e5["G"],
         "Notă contabilă"),
    ]
    for i, (bloc, cd_, cc_, suma, desc, doc) in enumerate(linii, start=1):
        e.rand([i, bloc, f"={D(data_j)}", f"={j.ref(cd_)}", f"={j.ref(cc_)}",
                f"={j.ref(suma)}", f"={j.ref(desc)}", doc,
                f'=IF(AND(ISNUMBER(F{e.r}),F{e.r}>0),"DA","NU")'])
    ultim = e.r - 1
    e.gol()
    e.kv("Rânduri de importat", f'=COUNTIF(I{primul}:I{ultim},"DA")', tip="calc")
    e.check("Check global", f"={j.ref(glob)}",
            f'=IF(ABS(B{e.r})<0.01,"OK","EROARE")')
