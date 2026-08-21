"""MOD_SALARII_EVENIMENTE — cele patru cazuri în care lanțul de salarii deviază.

Acoperă F-64 (concediu medical), F-65 (poprire), F-66 (drepturi neridicate),
F-67 (creanță față de un fost salariat).

MOD_SALARII face statul lunar. Modulul ăsta face ce se întâmplă *pe lângă* el: un
salariat intră în concediu medical, altul are poprire, cineva nu-și ridică banii, un
fost angajat pleacă dator. Toate patru ating grupa 42x, toate patru au stare terminală
de sold zero, și toate patru se pot întâmpla în aceeași lună — de-aia fiecare are
comutatorul lui, nu o poartă de tip care le-ar face exclusive.

## Ce apără fiecare bloc

**A. Concediul medical — linia de demarcație decide baza CAM.** Indemnizația trece
INTEGRAL prin datoria față de salariat, dar numai partea suportată de angajator e
cheltuiala firmei. Restul e creanță pe 4382: bani avansați în numele casei, nu
cheltuiți. Iar CAM se calculează DOAR pe partea proprie — cine trece toată indemnizația
pe cheltuieli își subestimează rezultatul ȘI plătește CAM pe banii altcuiva.
Reținerile, în schimb, se fac pe TOATĂ indemnizația, indiferent cine o suportă.

**B. Poprirea — limita se calculează din NET, nu din brut.** Banii merg la executor,
nu la stat, deci după ce statul și-a luat partea. Art. 729 Cod procedură civilă: 1/2
pentru obligații de întreținere sau alocații pentru copii, 1/3 pentru alte datorii, iar
la mai multe popriri maximum 1/2 în total indiferent de natura creanțelor.

**C. Drepturile neridicate — reclasificare, nu dispariție.** Fără pasul 421 → 426,
corelația „sold 421 = restul de plată de pe stat” se rupe și pare că firma are restanțe
de salarii, când de fapt are bani nerevendicați.

**D. Creanța față de un fost salariat — activ, nu reducere de cheltuială.** La încasare
crește un activ și scade altul; nu-ți trebuie „opusul băncii”. Un sold CREDITOR pe 4282
e contrar naturii contului (C-23).

## O cifră corectată față de flux

F-65 scria „33,33% din 29.250 = 9.749,03”. Art. 729 spune *o treime*, iar o treime din
29.250 e exact **9.750,00**. Numărul vechi nu venea nici din 33,33% (care dă 9.748,94).
Modulul calculează fracția legală, iar fluxul a fost corectat odată cu el.
"""
from .comun import formula_activ

COD = "MOD_SALARII_EVENIMENTE"

CATALOG = dict(
    fluxuri="F-64, F-65, F-66, F-67",
    tip="Pe eveniment, pe angajat",
    variabile="Indemnizație brută și partea angajatorului; net de plată și tipul "
              "creanței poprite; sume neridicate; creanță față de fost salariat",
    porti="Patru comutatoare independente — evenimentele pot coexista în aceeași lună",
    blocuri="A Concediu medical; B Poprire; C Drepturi neridicate; D Creanță fost "
            "salariat",
    ce_face="42x: medicale, popriri, drepturi neridicate, creanțe față de foști "
            "salariați",
    cand="Pe eveniment, lângă statul lunar",
    activ="NU",
)

#: eveniment, ce declanșează, lanțul, starea terminală
EVENIMENTE = [
    ("A. Concediu medical", "Certificat medical + stat de plată",
     "6458 + 4382 = 423 · 423 = 4315/4316/444 · 646 = 436 · 423 = 5121 · 5121 = 4382",
     "Sold 423 = 0 și sold 4382 = 0 pe indemnizația decontată"),
    ("B. Poprire", "Adresă de înființare a popririi",
     "421 = 427 · 427 = 5121",
     "Sold 427 = 0 după virare; rulaj creditor = sold creditor pe lună"),
    ("C. Drepturi neridicate", "Stat de plată + registru de casă",
     "421 = 426 · 426 = 5311",
     "Sold 421 reconciliat cu statul; sold 426 = doar sumele nerevendicate"),
    ("D. Creanță fost salariat", "Notă de lichidare + proces-verbal",
     "4282 = 7588 · 5311 = 4282",
     "Sold 4282 = 0, niciodată creditor"),
]

#: prag / regulă, valoare, temei
REGULI_LEGALE = [
    ("Poprire — obligații de întreținere sau alocații pentru copii", "1/2 din net",
     "art. 729 alin. (1) lit. a) Cod procedură civilă"),
    ("Poprire — alte datorii", "1/3 din net",
     "art. 729 alin. (1) lit. b) Cod procedură civilă"),
    ("Poprire — mai multe popriri pe aceeași sumă", "maximum 1/2 în total",
     "art. 729 alin. (2) CPC — indiferent de natura creanțelor"),
    ("Poprire — venit sub salariul minim net", "doar partea peste 1/2 din minimul net",
     "art. 729 alin. (3) CPC"),
    ("Medical — prima zi de boală obișnuită", "nu se plătește",
     "februarie 2026 – decembrie 2027; NU se aplică la urgențe, accidente de muncă, "
     "sarcină, carantină"),
    ("Medical — baza de calcul", "media brutului pe ultimele 6 luni",
     "plafonată la 12 salarii minime brute"),
    ("Medical — CASS pe indemnizație", "10%, din veniturile lunii august 2026",
     "Legea 170/2026 — până atunci CASS nu se datora pe indemnizație"),
    ("Medical — baza CAM", "DOAR partea suportată de angajator",
     "pe partea din FNUASS nu se datorează CAM: nu e cheltuiala firmei"),
]


def construieste(F, P):
    # ---------------------------------------------------------------- Declarații
    d = F("Declarații_SALARII_EVENIMENTE", {"A": 52, "B": 22, "C": 56})
    d.titlu("MOD_SALARII_EVENIMENTE — Declarații (input)")
    d.nota("Patru evenimente independente. Pune DA pe cele care s-au întâmplat luna "
           "asta — pot fi mai multe deodată, iar blocurile neactivate ies cu zero și nu "
           "intră în nota de export.")
    d.gol()

    d.sectiune("1. Antet")
    d.kv("Societate", "=Parametri!B5", tip="calc")
    d.kv("CUI", "=Parametri!B6", tip="calc")
    luna = d.kv("Luna (AAAA-LL)", "2026-07")
    data_j = d.kv("Data jurnal", "2026-07-31")
    d.gol()

    d.sectiune("2. Eveniment A — Concediu medical")
    a_on = d.kv("Se aplică? (DA/NU)", "DA")
    a_brut = d.kv("Indemnizație brută", 1000,
                  nota="Media brutului pe ultimele 6 luni, plafonată la 12 salarii "
                       "minime brute")
    a_ang = d.kv("Partea suportată de angajator", 250,
                 nota="Numărul de zile depinde de codul de indemnizație; prima zi de "
                      "boală obișnuită nu se plătește (feb. 2026 – dec. 2027)")
    a_fnuass = d.kv("Partea din FNUASS (auto)", f"={a_brut}-{a_ang}", tip="calc")
    a_cas = d.kv("CAS reținut (auto)", f"=ROUND({a_brut}*{P['cota_cas']},2)", tip="calc")
    a_cass = d.kv("CASS reținut (auto)", f"=ROUND({a_brut}*{P['cota_cass']},2)",
                  tip="calc",
                  nota="Din veniturile lunii august 2026 (Legea 170/2026)")
    a_imp = d.kv("Impozit reținut (auto)",
                 f"=ROUND(({a_brut}-{a_cas}-{a_cass})*{P['cota_impozit']},2)",
                 tip="calc")
    a_retinut = d.kv("Total reținut (auto)", f"={a_cas}+{a_cass}+{a_imp}", tip="calc")
    a_net = d.kv("Net de plată (auto)", f"={a_brut}-{a_retinut}", tip="calc")
    a_cam = d.kv("CAM (auto) — DOAR pe partea angajatorului",
                 f"=ROUND({a_ang}*{P['cota_cam']},2)", tip="calc",
                 nota="Pe partea din FNUASS nu se datorează CAM — sunt bani avansați în "
                      "numele casei, nu cheltuiala firmei")
    d.gol()

    d.sectiune("3. Eveniment B — Poprire pe salariu")
    b_on = d.kv("Se aplică? (DA/NU)", "DA")
    b_net = d.kv("Net de plată al salariatului", 29250,
                 nota="Limita se calculează din NET, nu din brut: banii merg la "
                      "executor, după ce statul și-a luat partea")
    b_tip = d.kv("Tip creanță (INTRETINERE / ALTA)", "ALTA")
    b_multe = d.kv("Mai multe popriri pe aceeași sumă? (DA/NU)", "NU")
    b_fractie = d.kv(
        "Fracția aplicabilă (auto)",
        f'=IF(OR({b_tip}="INTRETINERE",{b_multe}="DA"),1/2,1/3)', tip="calc",
        nota="art. 729 CPC: 1/2 la întreținere sau la popriri multiple, 1/3 în rest")
    b_retinut = d.kv("Sumă reținută (auto)", f"=ROUND({b_net}*{b_fractie},2)",
                     tip="calc")
    d.gol()

    d.sectiune("4. Eveniment C — Drepturi de personal neridicate")
    c_on = d.kv("Se aplică? (DA/NU)", "DA")
    c_suma = d.kv("Sume neridicate", 3400)
    c_ridicat = d.kv("S-au ridicat ulterior? (DA/NU)", "DA")
    d.gol()

    d.sectiune("5. Eveniment D — Creanță față de un fost salariat")
    e_on = d.kv("Se aplică? (DA/NU)", "DA")
    e_suma = d.kv("Valoarea bunului nepredat / debitului", 400)
    e_incasat = d.kv("S-a încasat? (DA/NU)", "DA")
    d.gol()

    d.sectiune("6. Conturi")
    c_6458 = d.kv("Cheltuială indemnizație (6458)", "6458")
    c_4382 = d.kv("Creanță FNUASS (4382)", "4382")
    c_423 = d.kv("Datorie indemnizație (423)", "423")
    c_4315 = d.kv("CAS reținut (4315)", "4315")
    c_4316 = d.kv("CASS reținut (4316)", "4316")
    c_444 = d.kv("Impozit reținut (444)", "444")
    c_646 = d.kv("Cheltuială CAM (646)", "646")
    c_436 = d.kv("Datorie CAM (436)", "436")
    c_421 = d.kv("Personal — salarii datorate (421)", "421")
    c_426 = d.kv("Drepturi neridicate (426)", "426")
    c_427 = d.kv("Rețineri datorate terților (427)", "427")
    c_4282 = d.kv("Alte creanțe cu personalul (4282)", "4282")
    c_7588 = d.kv("Venit din despăgubiri (7588)", "7588")
    c_banca = d.kv("Bancă (5121)", "5121")
    c_casa = d.kv("Casă (5311)", "5311")
    d.gol()

    d.sectiune("7. Sufix")
    sufix = d.kv("Sufix", f'="— evenimente salariale " & {luna}', tip="calc")
    d.gol()

    d.sectiune("8. Control")
    d.kv("Modul activ?", formula_activ(COD), tip="calc")
    ver_cam = d.kv(
        "Verificare: baza CAM = partea angajatorului, nu brutul",
        f'=IF(ABS({a_cam}-ROUND({a_ang}*{P["cota_cam"]},2))<0.01,'
        f'"OK — CAM doar pe partea proprie","EROARE")', tip="calc")
    ver_pop = d.kv(
        "Verificare: reținerea nu depășește limita legală",
        f'=IF({b_retinut}<=ROUND({b_net}*{b_fractie},2)+0.01,'
        f'"OK — în limita art. 729","EROARE — peste limita legală")', tip="calc")

    # ------------------------------------------------------------------- Reguli
    g = F("Reguli_SALARII_EVENIMENTE",
          {"A": 30, "B": 34, "C": 62, "D": 52})
    g.titlu("MOD_SALARII_EVENIMENTE — Reguli (tabele fixe)")
    g.nota("Regula e dată, nu formulă. Se editează doar când se schimbă legea.")
    g.gol()

    g.sectiune("Tabel A — Cele patru evenimente")
    g.cap(["Eveniment", "Ce îl declanșează", "Lanțul", "Stare terminală"])
    for rand in EVENIMENTE:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel B — Praguri și temeiuri")
    g.cap(["Regulă", "Valoare", "Temei"])
    for rand in REGULI_LEGALE:
        g.rand(list(rand))
    g.gol()

    g.sectiune("Tabel C — Ce NU se face")
    for linie in [
        "• Toată indemnizația pe cheltuieli. Partea din FNUASS e CREANȚĂ pe 4382 — "
        "bani avansați în numele casei. Trecută pe cheltuieli, subestimează rezultatul.",
        "• CAM pe indemnizația întreagă. Se datorează DOAR pe partea suportată de "
        "angajator.",
        "• Poprirea calculată din brut. Limita se aplică pe NET.",
        "• Salariul neridicat lăsat pe 421. Fără reclasificarea pe 426, corelația "
        "„sold 421 = restul de plată de pe stat” se rupe și pare restanță de salarii.",
        "• 4428 în loc de 4282 la creanța față de un fost salariat. 4428 e TVA "
        "neexigibilă; contul corect e „Alte creanțe în legătură cu personalul”.",
    ]:
        g.nota(linie)
    g.gol()

    g.sectiune("Tabel D — Corelații atinse")
    g.cap(["Corelație", "Ce o rupe SUSPECT"])
    g.rand(["Sold 4382 = 0 după decontare",
            "Indemnizații nerecuperate de la casă — bani ai firmei blocați, adesea din "
            "dosare incomplete"])
    g.rand(["Sold 427 = 0 după virare",
            "Bani opriți din salariul cuiva și nevirați — trece din problemă contabilă "
            "în problemă penală"])
    g.rand(["Sold 421 = restul de plată de pe stat",
            "Reclasificarea pe 426 nu s-a făcut"])
    g.rand(["Sold 4282 niciodată creditor",
            "Încasare dublă sau înregistrare inițială pe partea greșită (C-23)"])

    # ------------------------------------------------------------------ Jurnale
    j = F("Jurnale_SALARII_EVENIMENTE",
          {"A": 34, "B": 16, "C": 14, "D": 50, "E": 16, "F": 14, "G": 50})
    j.titlu("MOD_SALARII_EVENIMENTE — Jurnale (generate automat)")
    j.nota("Fiecare bloc iese cu zero dacă evenimentul lui nu e activat. Verificarea "
           "globală însumează cu ABS, deci două erori de semn contrar nu se anulează.")
    j.gol()

    D = d.ref
    antet = ["Nr", "Cont Dr", "Sumă Dr", "Descriere Dr", "Cont Cr", "Sumă Cr",
             "Descriere Cr"]

    def daca(comutator, valoare):
        """Suma intră în notă doar dacă evenimentul e activat."""
        return f'=IF({D(comutator)}="DA",{D(valoare)},0)'

    # ---- A. concediu medical
    j.sectiune("Bloc A — Concediu medical")
    j.kv("Data:", f"={D(data_j)}", tip="calc")
    j.cap(antet)
    a1 = j.rand([1, f"={D(c_6458)}", daca(a_on, a_ang),
                 f'="Indemnizație — partea angajatorului " & {D(sufix)}',
                 f"={D(c_423)}", daca(a_on, a_brut),
                 f'="Datorie indemnizație (brut) " & {D(sufix)}'])
    a2 = j.rand([2, f"={D(c_4382)}", daca(a_on, a_fnuass),
                 f'="Creanță FNUASS — avansat în numele casei " & {D(sufix)}', 0, 0])
    ca = j.check("Check A1 (constituire)",
                 f"=({a1['C']}+{a2['C']})-{a1['F']}",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    a3 = j.rand([3, f"={D(c_423)}", daca(a_on, a_retinut),
                 f'="Rețineri din indemnizație (pe TOT brutul) " & {D(sufix)}',
                 f"={D(c_4315)}", daca(a_on, a_cas),
                 f'="CAS reținut " & {D(sufix)}'])
    a4 = j.rand([4, 0, 0, None, f"={D(c_4316)}", daca(a_on, a_cass),
                 f'="CASS reținut " & {D(sufix)}'])
    a5 = j.rand([5, 0, 0, None, f"={D(c_444)}", daca(a_on, a_imp),
                 f'="Impozit reținut " & {D(sufix)}'])
    cb = j.check("Check A2 (rețineri)",
                 f"={a3['C']}-({a3['F']}+{a4['F']}+{a5['F']})",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    a6 = j.rand([6, f"={D(c_646)}", daca(a_on, a_cam),
                 f'="CAM — doar pe partea angajatorului " & {D(sufix)}',
                 f"={D(c_436)}", daca(a_on, a_cam),
                 f'="Datorie CAM " & {D(sufix)}'])
    cc = j.check("Check A3 (CAM)", f"={a6['C']}-{a6['F']}",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    a7 = j.rand([7, f"={D(c_423)}", daca(a_on, a_net),
                 f'="Plata netului către salariat " & {D(sufix)}',
                 f"={D(c_banca)}", daca(a_on, a_net),
                 f'="Ieșire bancă " & {D(sufix)}'])
    a8 = j.rand([8, f"={D(c_banca)}", daca(a_on, a_fnuass),
                 f'="Decontarea cu FNUASS " & {D(sufix)}',
                 f"={D(c_4382)}", daca(a_on, a_fnuass),
                 f'="Stingerea creanței sociale " & {D(sufix)}'])
    cd = j.check("Check A4 (plăți)",
                 f"=({a7['C']}+{a8['C']})-({a7['F']}+{a8['F']})",
                 f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    # ---- B. poprire
    j.sectiune("Bloc B — Poprire pe salariu")
    j.cap(antet)
    b1 = j.rand([1, f"={D(c_421)}", daca(b_on, b_retinut),
                 f'="Reținere din salariu (poprire) " & {D(sufix)}',
                 f"={D(c_427)}", daca(b_on, b_retinut),
                 f'="Datorie față de terț " & {D(sufix)}'])
    b2 = j.rand([2, f"={D(c_427)}", daca(b_on, b_retinut),
                 f'="Virare către executor " & {D(sufix)}',
                 f"={D(c_banca)}", daca(b_on, b_retinut),
                 f'="Ieșire bancă " & {D(sufix)}'])
    cb2 = j.check("Check B", f"=({b1['C']}+{b2['C']})-({b1['F']}+{b2['F']})",
                  f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    # ---- C. drepturi neridicate
    j.sectiune("Bloc C — Drepturi de personal neridicate")
    j.cap(antet)
    c1 = j.rand([1, f"={D(c_421)}", daca(c_on, c_suma),
                 f'="Reclasificare drepturi neridicate " & {D(sufix)}',
                 f"={D(c_426)}", daca(c_on, c_suma),
                 f'="Datorie neridicată " & {D(sufix)}'])
    # Ridicarea ulterioară e un eveniment separat: dacă nu s-a întâmplat, rândul e 0 și
    # soldul lui 426 rămâne — exact ce trebuie urmărit.
    c2 = j.rand([2, f"={D(c_426)}", f'=IF(AND({D(c_on)}="DA",{D(c_ridicat)}="DA"),'
                                    f'{D(c_suma)},0)',
                 f'="Ridicarea ulterioară " & {D(sufix)}',
                 f"={D(c_casa)}", f'=IF(AND({D(c_on)}="DA",{D(c_ridicat)}="DA"),'
                                  f'{D(c_suma)},0)',
                 f'="Ieșire casă " & {D(sufix)}'])
    cc2 = j.check("Check C", f"=({c1['C']}+{c2['C']})-({c1['F']}+{c2['F']})",
                  f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    # ---- D. creanță fost salariat
    j.sectiune("Bloc D — Creanță față de un fost salariat")
    j.cap(antet)
    e1 = j.rand([1, f"={D(c_4282)}", daca(e_on, e_suma),
                 f'="Creanță față de fostul salariat " & {D(sufix)}',
                 f"={D(c_7588)}", daca(e_on, e_suma),
                 f'="Venit din despăgubiri " & {D(sufix)}'])
    e2 = j.rand([2, f"={D(c_casa)}", f'=IF(AND({D(e_on)}="DA",{D(e_incasat)}="DA"),'
                                     f'{D(e_suma)},0)',
                 f'="Încasarea creanței " & {D(sufix)}',
                 f"={D(c_4282)}", f'=IF(AND({D(e_on)}="DA",{D(e_incasat)}="DA"),'
                                  f'{D(e_suma)},0)',
                 f'="Stingerea creanței " & {D(sufix)}'])
    cd2 = j.check("Check D", f"=({e1['C']}+{e2['C']})-({e1['F']}+{e2['F']})",
                  f'=IF(ABS(B{j.r})<0.01,"OK","EROARE")')
    j.gol()

    glob = j.check(
        "Check global",
        f"=ABS({ca})+ABS({cb})+ABS({cc})+ABS({cd})+ABS({cb2})+ABS({cc2})+ABS({cd2})",
        f'=IF(B{j.r}<0.01,"OK — toate blocurile se închid",'
        f'"EROARE — cel puțin un bloc dezechilibrat")')
    j.gol()

    j.sectiune("Stare terminală")
    j.nota("Sold 423 = 0 și sold 4382 = 0 pe indemnizația decontată | sold 427 = 0 după "
           "virare | sold 421 reconciliat cu statul, sold 426 = doar sumele "
           "nerevendicate | sold 4282 = 0, niciodată creditor. Pe rezultat rămân doar "
           "partea angajatorului din indemnizație și CAM-ul aferent ei.")

    # --------------------------------------------------------------- NotaExport
    e = F("NotaExport_SALARII_EVENIMENTE",
          {"A": 6, "B": 26, "C": 14, "D": 12, "E": 12, "F": 14, "G": 50, "H": 26,
           "I": 10})
    e.titlu("MOD_SALARII_EVENIMENTE — Notă pentru import")
    e.nota("Filtrează Include=DA. Blocurile neactivate ies cu sumă 0 și apar ca NU.")
    e.gol()
    e.cap(["Nr", "Bloc", "Data", "Cont Dr", "Cont Cr", "Sumă", "Descriere", "Document",
           "Include"])
    primul = e.r
    linii = [
        ("A Medical — cheltuiala proprie", a1, a1["C"], "Certificat medical"),
        ("A Medical — creanța FNUASS", a2, a2["C"], "Certificat medical"),
        ("A Medical — CAS", a3, a4["F"], "Stat de plată"),
        ("A Medical — CASS", a4, a4["F"], "Stat de plată"),
        ("A Medical — impozit", a5, a5["F"], "Stat de plată"),
        ("A Medical — CAM", a6, a6["C"], "Notă de contribuții"),
        ("A Medical — plata netului", a7, a7["C"], "Extras de cont"),
        ("A Medical — decontare FNUASS", a8, a8["C"], "Extras de cont"),
        ("B Poprire — reținere", b1, b1["C"], "Adresă de poprire"),
        ("B Poprire — virare", b2, b2["C"], "Extras de cont"),
        ("C Neridicate — reclasificare", c1, c1["C"], "Registru de casă"),
        ("C Neridicate — ridicare", c2, c2["C"], "Dispoziție de plată"),
        ("D Fost salariat — creanța", e1, e1["C"], "Notă de lichidare"),
        ("D Fost salariat — încasarea", e2, e2["C"], "Chitanță"),
    ]
    for i, (bloc, r, suma, doc) in enumerate(linii, start=1):
        # La rândurile-componentă, contul de credit e cel al componentei, iar contul de
        # debit e cel al capului compus — o linie exportată e o înregistrare completă.
        cd_ref = r["B"] if "B" in r else a3["B"]
        e.rand([i, bloc, f"={D(data_j)}", f"={j.ref(cd_ref)}", f"={j.ref(r['E'])}",
                f"={j.ref(suma)}", f"={j.ref(r['D'] if 'D' in r else r['G'])}", doc,
                f'=IF(AND(ISNUMBER(F{e.r}),F{e.r}>0),"DA","NU")'])
    ultim = e.r - 1
    e.gol()
    e.kv("Rânduri de importat", f'=COUNTIF(I{primul}:I{ultim},"DA")', tip="calc")
    e.check("Check global", f"={j.ref(glob)}",
            f'=IF(ABS(B{e.r})<0.01,"OK","EROARE")')
