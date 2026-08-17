"""Fluxurile F-52…F-62 — imobilizări necorporale, corporale, în curs, ieșiri, financiare.

Sursa: surse/training-3-2026-08-12/notite-revizuit.md (trainingul din 12.08.2026).
Erorile din notițele brute sunt deja corectate în documentul revizuit și NU se
reintroduc aici: contul 7815 nu există (corect 6811 = 2805/2808), taxele vamale
se CAPITALIZEAZĂ (nu 635 = 5121), softul dezvoltat intern se capitalizează prin
721 (nu 711), salariile din imobilizări în curs prin 722, iar „2114” este 214.
"""
from .comun import flux, pas

FLUXURI = [
    # ------------------------------------------------------------------ F-52
    flux(
        "F-52", "Imobilizări necorporale: achiziție, marcă, soft dezvoltat intern", didactic=True,
        roluri="Activ imobilizat + Neutralizare rezultat (721)",
        conturi="205, 208, 233, 404, 641, 421, 721, 6811, 2805, 2808",
        note="Pas revelator: capitalizarea internă trece prin 721, nu prin 711",
        principiu="Softul dezvoltat intern este IMOBILIZARE NECORPORALĂ (233 → 208, neutralizat prin 721), "
                  "nu stoc (331/711). Diferența e de fond: imobilizarea se amortizează pe ani, stocul se "
                  "descarcă la vânzare. Contul 7815 din notițe nu există — amortizarea necorporalelor se "
                  "înregistrează 6811 = 2805 / 2808 (7813 există, dar e „Venituri din ajustări”).",
        pasi=[
            pas(1, "Factură furnizor de imobilizări",
                "Achiziția unui program de contabilitate. Furnizorul de imobilizări este 404, nu 401.",
                dr=[("208", 12000), ("4426", 2520)], cr=[("404", 14520)],
                rol="Activ imobilizat necorporal + TVA deductibilă", declarativ="D300, D394"),
            pas(2, "Plan de amortizare",
                "Amortizarea programului pe 3 ani = 36 luni: 12.000 / 36 = 333,33 lei/lună.",
                dr=[("6811", 333.33)], cr=[("2808", 333.33)],
                rol="Cheltuială + Rectificativ contra-activ"),
            pas(3, "Certificat OSIM / contract",
                "Mărcile se înregistrează și se amortizează pe 10 ani (durata din notițe, confirmată). "
                "Contul de amortizare pereche este 2805.",
                dr=[("205", 6000)], cr=[("404", 6000)],
                rol="Concesiuni, brevete, licențe, mărci"),
            pas(4, "State de plată — dezvoltare internă",
                "Costurile salariale ale echipei care dezvoltă softul intern, în luna curentă. "
                "(În notițe apărea `641 = 241` — typo pentru 421.)",
                dr=[("641", 30000)], cr=[("421", 30000)],
                rol="Cheltuială cu personalul"),
            pas(5, "Notă de capitalizare (lunară)",
                "Costurile se acumulează în imobilizări necorporale în curs, iar cheltuiala este "
                "NEUTRALIZATĂ printr-un venit din producția de imobilizări necorporale. "
                "⚠ 721, NU 711: 711 e variația stocurilor de produse.",
                dr=[("233", 30000)], cr=[("721", 30000)],
                rol="Pas revelator: 721 ține 121 la zero cât timp softul e în dezvoltare",
                revelator=True),
            pas(6, "Proces-verbal de recepție / punere în funcțiune",
                "Softul finalizat trece din „în curs” în imobilizare necorporală amortizabilă.",
                dr=[("208", 30000)], cr=[("233", 30000)],
                rol="Imobilizare în curs → imobilizare finalizată"),
            pas(7, "Verificare",
                "Sold 233 = 0 după punerea în funcțiune. Efect pe 121 în perioada dezvoltării: "
                "641 (30.000) − 721 (30.000) = 0. Amortizarea începe din luna următoare punerii în funcțiune. "
                "Dacă înregistrezi softul intern pe 331, ai și cont greșit, și tratament fiscal greșit.",
                rol="Stare terminală: 233 = 0, cost capitalizat, rezultat neafectat"),
        ],
    ),
    # ------------------------------------------------------------------ F-53
    flux(
        "F-53", "Terenuri și amenajări de terenuri (211)",
        roluri="Activ imobilizat (parte neamortizabilă)",
        conturi="2111, 2112, 2811, 404, 6811",
        note="Declarare la primărie în 30 de zile de la achiziție",
        principiu="Terenul (2111) NU se amortizează; amenajarea de teren (2112) se amortizează pe 10 ani. "
                  "Terenurile se țin cât mai analitic (arabil, curți-construcții, în curs de construcții) "
                  "pentru că TRATAMENTUL FISCAL LA VÂNZARE este diferit.",
        pasi=[
            pas(1, "Contract notarial + factură",
                "Achiziția terenului. Se înregistrează analitic pe categorie de folosință.",
                dr=[("2111.arabil", 100000)], cr=[("404", 100000)],
                rol="Activ imobilizat neamortizabil", declarativ="D394"),
            pas(2, "Situație de lucrări",
                "Amenajarea terenului (tasare, nivelare, împrejmuire) — lucrări care POT fi amortizate.",
                dr=[("2112", 20000), ("4426", 4200)], cr=[("404", 24200)],
                rol="Amenajare de teren (amortizabilă)", declarativ="D300"),
            pas(3, "Plan de amortizare",
                "Amenajările se amortizează pe 10 ani = 120 luni: 20.000 / 120 = 166,67 lei/lună. "
                "Contul pereche este 2811.",
                dr=[("6811", 166.67)], cr=[("2811", 166.67)],
                rol="Pas revelator: se amortizează amenajarea, nu terenul", revelator=True),
            pas(4, "Declarație la primărie",
                "Toată grupa de imobilizări corporale se declară la primărie în 30 de zile de la achiziție, "
                "iar impozitul se plătește pe tot anul — chiar dacă bunul se vinde în cursul anului, "
                "primăria nu returnează impozitul deja plătit.",
                rol="Obligație declarativă locală", declarativ="Declarație impozit local"),
            pas(5, "Verificare",
                "2111 nu are cont de amortizare — nu trebuie să apară niciodată sold pe 2811 aferent lui. "
                "Sold 2811 corespunde exclusiv lui 2112.",
                rol="Stare terminală: teren neamortizat, amenajare în amortizare"),
        ],
    ),
    # ------------------------------------------------------------------ F-54
    flux(
        "F-54", "Construcții (212) — cele trei regimuri de TVA și codul 27", didactic=True,
        roluri="Activ imobilizat + TVA (taxare inversă)",
        conturi="212, 404, 4426, 4427, 2812, 6811",
        note="Pas revelator: codul 27 în D394 pentru taxare inversă la clădiri",
        principiu="Fără codul de operațiune 27 din nomenclatorul D394, decontul și declarația NU recunosc "
                  "operațiunea ca taxare inversă. Clădirile au obligatoriu amortizare LINIARĂ. "
                  "Codul de clasificare din catalog trebuie trecut în modulul de mijloace fixe — merge în D406.",
        pasi=[
            pas(1, "Factură + contract notarial",
                "Varianta A — achiziție cu TVA standard 21% de la un vânzător plătitor.",
                dr=[("212", 500000), ("4426", 105000)], cr=[("404", 605000)],
                rol="Activ imobilizat + TVA deductibilă", declarativ="D300, D394"),
            pas(2, "Contract notarial",
                "Varianta B — achiziție de la persoană fizică: fără TVA, deci fără 4426.",
                dr=[("212", 500000)], cr=[("404", 500000)],
                rol="Achiziție fără TVA (vânzător neimpozabil)", declarativ="D394"),
            pas(3, "Factură cu mențiunea „taxare inversă”",
                "Varianta C — între doi plătitori de TVA (art. 331 CF). Se aplică cota din România, 21%, "
                "simultan pe deductibil și pe colectat; efectul în decont este zero. "
                "⚠ În soft trebuie pus codul 27 din nomenclatorul D394, altfel operațiunea nu e recunoscută "
                "ca taxare inversă.",
                dr=[("4426", 105000)], cr=[("4427", 105000)],
                rol="Pas revelator: autolichidare + cod 27 în D394",
                declarativ="D300, D394 (cod 27)", revelator=True),
            pas(4, "Catalog de clasificare + plan de amortizare",
                "Încadrarea decide durata: clădire administrativă 30–40 ani, șopron 16 ani, hală etc. "
                "Exemplu la 40 de ani = 480 luni: 500.000 / 480 = 1.041,67 lei/lună. "
                "Amortizarea începe cu luna următoare punerii în funcțiune.",
                dr=[("6811", 1041.67)], cr=[("2812", 1041.67)],
                rol="Cheltuială + Rectificativ (oglinda 212 ↔ 2812)"),
            pas(5, "Verificare",
                "Codul de clasificare e completat în modulul de mijloace fixe (alimentează D406/SAF-T). "
                "Amortizarea fiscală e cea din catalog; amortizarea contabilă poate diferi — diferența "
                "se urmărește în registrul de evidență fiscală. Verifică în PRIMA lună că nota de amortizare "
                "postează 212 în oglindă cu 2812, nu cu alt cont.",
                rol="Stare terminală: durata corectă, oglinda corectă", declarativ="D406/SAF-T"),
        ],
    ),
    # ------------------------------------------------------------------ F-55
    flux(
        "F-55", "Instalații tehnice și mijloace de transport (213): intracomunitar și import",
        roluri="Activ imobilizat + TVA + Cost de achiziție",
        conturi="2131, 2133, 404, 4426, 4427, 446, 5121",
        note="Taxele vamale și transportul se CAPITALIZEAZĂ. D390, D300",
        principiu="Taxele vamale nerecuperabile și transportul fac parte din COSTUL DE ACHIZIȚIE "
                  "(OMFP 1802/2014) — nu se trec pe 635. Notița brută avea ambele variante și se "
                  "contrazicea; corectă este capitalizarea.",
        pasi=[
            pas(1, "Factură intracomunitară",
                "Achiziție de echipament din spațiul UE. Condiții pentru scutirea la furnizor: să fim "
                "înregistrați în VIES cu cod valid ȘI să avem dovada transportului din UE în România.",
                dr=[("2131", 100000)], cr=[("404", 100000)],
                rol="Activ imobilizat (factură fără TVA)", declarativ="D390, D394"),
            pas(2, "Notă de autolichidare",
                "Se aplică cota de TVA din România (21%) simultan pe deductibil și colectat. "
                "Efect net în decont: zero.",
                dr=[("4426", 21000)], cr=[("4427", 21000)],
                rol="Taxare inversă la achiziție intracomunitară", declarativ="D300, D390"),
            pas(3, "Declarația vamală de import (DVI)",
                "La import, documentul de bază este DVI, NU factura furnizorului. Valoarea de intrare se "
                "fixează la cursul din DVI — atenție, unele sisteme recalculează la plată și alterează "
                "valoarea de amortizat.",
                dr=[("2133", 80000)], cr=[("404", 80000)],
                rol="Activ imobilizat la valoarea din DVI"),
            pas(4, "DVI + extras",
                "⚠ Taxele vamale se CAPITALIZEAZĂ în valoarea bunului, nu pe 635. La fel transportul.",
                dr=[("2133", 6400)], cr=[("446.VAMA", 6400)],
                rol="Pas revelator: taxa vamală intră în cost, nu pe cheltuială", revelator=True),
            pas(5, "Extras de cont",
                "TVA plătit efectiv în vamă. Cine are certificat de amânare de la plata TVA în vamă "
                "aplică `4426 = 4427` în loc de plată efectivă — avantaj mare de cash-flow.",
                dr=[("4426", 18144)], cr=[("5121", 18144)],
                rol="TVA deductibilă plătită în vamă", declarativ="D300"),
            pas(6, "Verificare + catalog",
                "Valoare de intrare 2133 = 80.000 + 6.400 = 86.400 lei. "
                "Încadrarea în catalog cere FIȘA TEHNICĂ, nu doar denumirea de pe factură "
                "(ex. 2.1.16.4.1 compresoare cu piston, stabile — 8–12 ani).",
                rol="Stare terminală: cost complet capitalizat, durată din catalog"),
        ],
    ),
    # ------------------------------------------------------------------ F-56
    flux(
        "F-56", "Investiții imobiliare (215) și defalcarea teren / construcție",
        roluri="Activ imobilizat + Documentare valoare",
        conturi="215, 2111, 212, 404, 2815",
        note="Defalcarea e obligatorie, nu opțională",
        principiu="Dacă actul notarial dă o valoare globală, defalcarea teren/construcție NU se face „din pix”: "
                  "e nevoie de încheiere notarială cu valorile separate sau de raport de evaluare. "
                  "Fără ele nu poți înregistra bunurile la primărie și nu poți amortiza corect "
                  "(terenul nu se amortizează).",
        pasi=[
            pas(1, "Contract notarial",
                "Achiziție imobil păstrat pentru valorificare peste 5–10 ani → investiție imobiliară, "
                "rămâne la valoarea din document. Actul dă o valoare globală de 120.000 lei, fără defalcare.",
                rol="Situație: valoare globală, nedefalcată"),
            pas(2, "Încheiere notarială / raport de evaluare",
                "Se solicită defalcarea: teren 40.000, construcție 80.000. Este OBLIGATORIE — "
                "nu îmi dau eu cu părerea.",
                rol="Documentarea valorilor separate"),
            pas(3, "Notă contabilă",
                "Înregistrarea pe cele două componente, cu tratament de amortizare diferit.",
                dr=[("2111", 40000), ("215", 80000)], cr=[("404", 120000)],
                rol="Pas revelator: defalcarea decide ce se amortizează", revelator=True),
            pas(4, "Verificare",
                "Verifică dacă valoarea facturii = valoarea din contractul notarial. "
                "Documente necesare în afara facturii: contractul (tranzacțiile se fac prin notariat) — "
                "oricum vine cerere de la primărie. Contul de amortizare pentru 215 este 2815; "
                "partea de teren (2111) nu se amortizează.",
                rol="Stare terminală: componente separate, declarate la primărie",
                declarativ="Declarație impozit local"),
        ],
    ),
    # ------------------------------------------------------------------ F-57
    flux(
        "F-57", "Imobilizări facturate dar nesosite (223 / 224)",
        roluri="Tranzit / reflectare",
        conturi="223, 224, 2133, 404, 4426",
        note="Oglinda lui F-02, pe imobilizări în loc de stocuri",
        principiu="Am factura dar nu pot face recepția. Fără 223/224 ai fi forțat fie să înregistrezi un "
                  "mijloc fix care nu există fizic (și să începi să-l amortizezi), fie să nu înregistrezi "
                  "factura — ambele greșite.",
        pasi=[
            pas(1, "Factură furnizor de imobilizări",
                "Bunul e facturat, proprietatea a trecut, dar nu a ajuns fizic. Regimul de TVA poate fi "
                "cu TVA sau taxare inversă — nu schimbă rolul lui 223.",
                dr=[("223", 80000), ("4426", 16800)], cr=[("404", 96800)],
                rol="Tranzit: bun facturat, nerecepționat", declarativ="D300, D394"),
            pas(2, "Proces-verbal de recepție",
                "La recepție se stinge tranzitul în contul definitiv de imobilizare. "
                "Abia acum poate începe amortizarea (din luna următoare punerii în funcțiune).",
                dr=[("2133", 80000)], cr=[("223", 80000)],
                rol="Pas revelator: 223 se stinge la recepție", revelator=True),
            pas(3, "Verificare",
                "Sold 223 = 0 pe documentele cu recepție în perioadă. Sold rămas la 31.12 = listă de "
                "bunuri în tranzit, explicată. 223 se stinge în 213, 224 în 214.",
                rol="Stare terminală: 223 = 0 sau listă explicată"),
        ],
    ),
    # ------------------------------------------------------------------ F-58
    flux(
        "F-58", "Imobilizări în curs de execuție (231) și salariile capitalizate prin 722", didactic=True,
        roluri="Activ imobilizat + Neutralizare rezultat (722)",
        conturi="231, 404, 641, 421, 722, 212, 4426",
        note="Pas revelator: 722, nu 711 — și nu 628 pentru prestațiile terților",
        principiu="Prestațiile terților pentru un obiectiv de investiții merg în 231, NU pe 628 — statul "
                  "solicită contractul de prestări servicii și situațiile de lucrări. Salariile proprii "
                  "folosite la ridicarea halei se capitalizează prin 722 „Venituri din producția de "
                  "imobilizări corporale”, nu prin 711 (care e variația stocurilor).",
        pasi=[
            pas(1, "Contract + situații de lucrări",
                "Toate cheltuielile aferente obiectivului — inclusiv arhitectul și restul prestărilor de "
                "servicii — se acumulează în 231. NU pe 628.",
                dr=[("231.obiectiv", 200000), ("4426", 42000)], cr=[("404", 242000)],
                rol="Imobilizare în curs + TVA deductibilă", declarativ="D300, D394"),
            pas(2, "State de plată + notificare internă",
                "Salariații proprii care lucrează la obiectiv. Trebuie o notificare internă care să "
                "stabilească faptul că salariații x, y, z lucrează pentru obiectivul respectiv.",
                dr=[("641", 30000)], cr=[("421", 30000)],
                rol="Cheltuială cu personalul", declarativ="D112"),
            pas(3, "Notă de capitalizare",
                "Cheltuiala se „reia” printr-un venit din producția de imobilizări corporale. "
                "⚠ 722, NU 711.",
                dr=[("231.obiectiv", 30000)], cr=[("722", 30000)],
                rol="Pas revelator: 722 neutralizează cheltuiala capitalizată", revelator=True),
            pas(4, "Proces-verbal de punere în funcțiune",
                "La finalul proiectului se înregistrează valoarea reală a obiectivului.",
                dr=[("212", 230000)], cr=[("231.obiectiv", 230000)],
                rol="Imobilizare în curs → construcție"),
            pas(5, "Verificare",
                "Sold 231 = 0 după PV. Efect pe 121 în perioada construcției: 641 − 722 = 0. "
                "231 se ține pe ANALITIC PE OBIECTIV — la 31.12, dacă ai un sold mare, trebuie să știi "
                "ce e acolo, pentru că administratorii întreabă.",
                rol="Stare terminală: 231 = 0, cost integral în 212"),
        ],
    ),
    # ------------------------------------------------------------------ F-59
    flux(
        "F-59", "Vânzarea unui mijloc fix și testul valorii rămase", didactic=True,
        roluri="Ieșire activ + Rectificativ 28x + Test fiscal",
        conturi="212, 2812, 6583, 461, 7583, 4427",
        note="Pas revelator: 6583 deductibil în limita venitului. D101",
        principiu="Valoarea minimă de valorificare nu e „cât vreau eu”: reperul e valoarea de piață "
                  "(Autovit/OLX pentru auto) sau valoarea de fier vechi — nu poți vinde cu 100 EUR un bun "
                  "doar pentru că e amortizat integral. Prețul trebuie DOCUMENTAT: raport de evaluare, "
                  "referință de piață sau deviz de service care atestă deteriorarea.",
        pasi=[
            pas(1, "Balanță + registrul mijloacelor fixe",
                "Clădire cu valoare de inventar 100.000 lei (212), amortizată 30.000 lei (2812). "
                "Valoare rămasă neamortizată: 70.000 lei.",
                rol="Situație inițială: activ pe debit, amortizare pe credit"),
            pas(2, "Notă de scoatere din evidență",
                "Se descarcă amortizarea cumulată — 2812 este pur rectificativ, nu ține nimic real.",
                dr=[("2812", 30000)], cr=[("212", 30000)],
                rol="Stingere rectificativ contra-activ"),
            pas(3, "Notă de scoatere din evidență",
                "Valoarea rămasă neamortizată trece pe cheltuială.",
                dr=[("6583", 70000)], cr=[("212", 70000)],
                rol="Cheltuială din cedarea activelor"),
            pas(4, "Factura de vânzare",
                "Preț de vânzare 50.000 lei + TVA 21%.",
                dr=[("461", 60500)], cr=[("7583", 50000), ("4427", 10500)],
                rol="Creanță + Venit din cedare + TVA colectată", declarativ="D300, D394"),
            pas(5, "Test fiscal — valoarea rămasă vs. venit",
                "Cheltuiala cu valoarea neamortizată este deductibilă ÎN LIMITA VENITULUI din vânzare: "
                "50.000 deductibil, 20.000 nedeductibil. "
                "❓ De cerut formatorului baza legală exactă — art. 28 alin. 17 CF, citit strict, include "
                "pierderea în rezultatul fiscal; poziția prudentă se sprijină pe art. 11 (reîncadrare) și "
                "art. 25 alin. 1 (scopul activității economice). Concluzia practică e aceeași: "
                "fără document justificativ ai un risc, care se comunică clientului ÎN SCRIS.",
                rol="Pas revelator: deductibilitatea depinde de documentarea prețului",
                declarativ="D101", revelator=True),
            pas(6, "Verificare",
                "Sold 212 = 0 și sold 2812 = 0 pentru bunul ieșit. "
                "⚠ Schimbă STAREA mijlocului fix în modulul de imobilizări în „vândut” — altfel softul "
                "continuă să calculeze amortizare. Ieșirea din nota contabilă trebuie corelată cu modulul.",
                rol="Stare terminală: 212 = 0, 2812 = 0, stare „vândut” în modul"),
        ],
    ),
    # ------------------------------------------------------------------ F-60
    flux(
        "F-60", "Casarea unui mijloc fix și piesele recuperate",
        roluri="Ieșire activ + Stoc din casare",
        conturi="2133, 2813, 6583, 3024, 7588",
        note="Piesele recuperate intră pe stoc, nu direct pe venit la vânzare",
        principiu="Casarea se face pe proces-verbal de scoatere din funcțiune. Ce rezultă din casare — "
                  "deșeuri sau piese componente reutilizabile — trebuie evaluat de o COMISIE TEHNICĂ, care "
                  "dă lista de piese (volan, scaune etc.). Distincția contează: dacă factura conține seria "
                  "de șasiu, bunul se poate înmatricula, deci ai vândut un autoturism, nu piese.",
        pasi=[
            pas(1, "Proces-verbal de scoatere din funcțiune",
                "Uzură morală, defecțiune sau deviz de service care atestă deteriorarea "
                "(ex. mașină deteriorată în proporție de 60%, care nu mai poate rula).",
                rol="Documentul care declanșează casarea"),
            pas(2, "Notă de casare",
                "Mijloc de transport complet amortizat: 2133 = 50.000, 2813 = 50.000. "
                "Descărcarea nu produce cheltuială pentru că valoarea rămasă e zero.",
                dr=[("2813", 50000)], cr=[("2133", 50000)],
                rol="Pas revelator: la bun integral amortizat, ieșirea e doar 28x = 21x",
                revelator=True),
            pas(3, "Listă comisie tehnică + NIR",
                "Piesele recuperate, reutilizabile, se înregistrează pe stoc la valoarea stabilită de comisie.",
                dr=[("3024", 3000)], cr=[("7588", 3000)],
                rol="Stoc din casare + Alte venituri din exploatare"),
            pas(4, "Notă de transfer (dacă se vând)",
                "Dacă piesele nu se consumă intern ci se revând, se schimbă destinația bunului, "
                "deci și contul: transfer în mărfuri și vânzare — vezi F-10.",
                dr=[("371", 3000)], cr=[("3024", 3000)],
                rol="Schimbare de destinație: piese de schimb → marfă"),
            pas(5, "Verificare",
                "Sold 2133 = 0 și 2813 = 0 pentru bunul casat; bunul nu mai este al societății. "
                "⚠ Schimbă starea în modulul de imobilizări în „casat” — mai ales la sistemele care "
                "calculează amortizarea automat. Dacă valoarea rămasă nu era zero, diferența merge pe 6583 "
                "și intră sub testul din F-59.",
                rol="Stare terminală: 2133 = 0, 2813 = 0, stare „casat” în modul"),
        ],
    ),
    # ------------------------------------------------------------------ F-61
    flux(
        "F-61", "Controlul lunar analitic ↔ sintetic la imobilizări", didactic=True,
        roluri="Procedură de control (nu produce note contabile)",
        conturi="21x, 28x, registrul mijloacelor fixe",
        note="Flux de CONTROL: pașii sunt verificări, nu înregistrări",
        principiu="Amortizarea nu se înregistrează automat în toate softurile: dacă mijloacele fixe nu ajung "
                  "în modulul de imobilizări, nu se înregistrează amortizarea, iar la calculul impozitului pe "
                  "profit dai mai mult la plată. De aceea verificarea analitic ↔ sintetic este LUNARĂ. "
                  "Acesta e singurul flux din sistem care nu produce note contabile — e o procedură.",
        pasi=[
            pas(1, "Listing din modulul de imobilizări",
                "La sfârșitul fiecărei luni scoți mijloacele fixe din soft: fișa mijlocului fix și "
                "registrul mijloacelor fixe.",
                rol="Sursa 1: evidența operativă"),
            pas(2, "Balanța contabilă",
                "Soldurile analitice pe conturile 21x și 28x.",
                rol="Sursa 2: evidența contabilă"),
            pas(3, "Confruntarea pe perechi (oglinda)",
                "Fiecare cont de activ are un cont de amortizare pereche: 205↔2805, 208↔2808, "
                "2112↔2811, 212↔2812, 2131/2132/2133↔2813, 214↔2814, 215↔2815. "
                "⚠ Atenție la 2813, care deservește mai multe conturi de imobilizări. "
                "(În notițe apărea „2114 ↔ 2814” — contul 2114 nu există, corect este 214.)",
                rol="Pas revelator: suma din analiticul balanței = suma din registrul MF",
                revelator=True),
            pas(4, "Regula de validare",
                "Soldul conturilor 28x nu poate fi NICIODATĂ mai mare decât soldul conturilor 21x "
                "corespondente. Conturile de activ stau pe debit, amortizarea (pasiv rectificativ) pe credit.",
                rol="Testul de coerență a oglinzii"),
            pas(5, "Dacă soldurile nu corespund",
                "Listezi fișa de cont și cauți mijlocul pentru care nu s-a înregistrat amortizarea. "
                "Cauze frecvente: mijlocul fix nu a fost introdus în modul, sau în planul de conturi al "
                "societății contul a fost setat greșit (bifuncțional, ori pe sens invers).",
                rol="Procedura de localizare a diferenței"),
            pas(6, "Verificarea din PRIMA lună",
                "În prima lună în care se face amortizarea, verifică manual nota contabilă: clădirea din 212 "
                "trebuie să aibă cont de amortizare 2812. Dacă softul nu face automat corespondența, "
                "o prinzi acum, nu în decembrie.",
                rol="Stare terminală: analitic = sintetic = registru MF",
                declarativ="D406/SAF-T (secțiunea Active)"),
        ],
    ),
    # ------------------------------------------------------------------ F-62
    flux(
        "F-62", "Imobilizări financiare (26x): titluri și garanții",
        roluri="Activ imobilizat financiar + Creanță imobilizată",
        conturi="261, 267, 5121",
        note="Analitic pe partener/contract, obligatoriu",
        principiu="Garanțiile se recuperează la finalul contractului, uneori după ani. Fără analitic pe "
                  "partener și contract nu mai poți identifica soldul — și ajungi să scoți fișe de cont pe "
                  "3, 4, 5 ani. Cu atât mai mult la preluarea unei firme noi care are totul la un loc.",
        pasi=[
            pas(1, "Contract + extras de cont",
                "Societatea achiziționează acțiuni la o entitate afiliată.",
                dr=[("261.filiala", 50000)], cr=[("5121", 50000)],
                rol="Imobilizare financiară"),
            pas(2, "Contract de închiriere / documentație licitație",
                "Garanție de participare la licitație sau garanție de chirie, recuperabilă ulterior.",
                dr=[("267.partener", 10000)], cr=[("5121", 10000)],
                rol="Creanță imobilizată"),
            pas(3, "Extras de cont — final de contract",
                "Recuperarea garanției. Fără tipul de partener și analiticul pe contract, identificarea "
                "soldului peste ani devine imposibilă.",
                dr=[("5121", 10000)], cr=[("267.partener", 10000)],
                rol="Pas revelator: analiticul face garanția identificabilă la recuperare",
                revelator=True),
            pas(4, "Verificare",
                "Sold 267 = lista garanțiilor active, pe partener și contract. "
                "Softul trebuie să țină cât mai multe analitice — de aia e soft.",
                rol="Stare terminală: sold 267 = listă identificabilă"),
        ],
    ),
]
