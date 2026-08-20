"""Fluxul F-63 (→ F-415) — încasare mai mare decât factura.

Sursa: surse/training-5-2026-08-19/ghid-contabilitate.md, §7.3.

E singurul material din 19.08 care naște un flux propriu în loc să adâncească unul
existent. Restul secțiunilor „noi” — plafoane de numerar, cerințe de document,
practică de control — nu produc articole contabile, deci n-au ce monografie să aibă.

Cifrele sunt cele din sursă: factură 10.000, încasat 15.000, diferența de 5.000 e
TVA-inclusivă și se sparge în 4.132,23 bază + 867,77 TVA. Factura se modelează tot cu
total 10.000, ca cele două sume să fie comparabile — sursa nu spune dacă e cu sau fără
TVA, iar §7.2 din același material stabilește chiar regula că o sumă fără mențiune se
consideră cu tot cu TVA.
"""
from .comun import flux, pas

FLUXURI = [
    # ------------------------------------------------------------------ F-63
    flux(
        "F-63", "Încasare mai mare decât factura (supraîncasare → 419 + TVA)",
        didactic=True,
        roluri="Creanță + Datorie din avans + Colectare TVA",
        conturi="4111, 419, 4427, 707, 5121",
        note="Diferența e TVA-inclusivă (§7.2: sumă fără mențiune = cu tot cu TVA). "
             "Legiuitorul nu cere corecție când TU plătești în plus, dar o cere când "
             "TU încasezi în plus.",
        principiu="Un sold creditor pe 4111 nu e o curiozitate de balanță, e un avans "
                  "neînregistrat. Banii primiți peste factură sunt o datorie față de "
                  "partener, nu un venit — deci merg pe 419, nu pe 472, iar TVA-ul din "
                  "ei se colectează chiar dacă banii se returnează luna următoare.",
        pasi=[
            pas(1, "Factură emisă",
                "Factura de 10.000 lei, total cu TVA 21%: bază 8.264,46 + TVA 1.735,54.",
                dr=[("4111.partener", 10000)],
                cr=[("707", 8264.46), ("4427", 1735.54)],
                rol="Creanță + Venit + TVA colectată"),
            pas(2, "Extras de cont",
                "Partenerul virează 15.000 lei — cu 5.000 mai mult decât factura. "
                "Creanța se stinge și trece pe credit: 4111 ajunge cu sold creditor 5.000, "
                "adică un cont de activ cu sold contrar naturii lui.",
                dr=[("5121", 15000)], cr=[("4111.partener", 15000)],
                rol="Trezorerie + Creanță stinsă și depășită"),
            pas(3, "Notă contabilă — reclasificarea diferenței",
                "Diferența nu e venit, deci nu poate merge pe 472. E avans: 419. Iar din "
                "ea se extrage TVA-ul, pentru că suma încasată e TVA-inclusivă: "
                "5.000 ÷ 1,21 = 4.132,23 bază, 867,77 TVA. Fără pasul ăsta, TVA-ul rămâne "
                "necolectat și nimic nu semnalează.",
                dr=[("4111.partener", 5000)],
                cr=[("419.partener", 4132.23), ("4427", 867.77)],
                rol="Pas revelator: soldul creditor de pe 4111 se dovedește a fi avans "
                    "purtător de TVA, nu o eroare de încasare",
                revelator=True),
            pas(4, "Verificare",
                "Sold 4111 = 0 pe partenerul respectiv; sold 419 = 4.132,23; TVA colectată "
                "suplimentar 867,77. Se ia fișa pe plătitor și se contraverifică 4427, ca "
                "să confirmi că softul chiar a extras TVA-ul — vezi întrebarea deschisă. "
                "Dacă încasarea și restituirea se închid în aceeași lună, situația se "
                "neutralizează și impactul fiscal dispare.",
                rol="Stare terminală: sold 4111 = 0, avansul identificat pe 419 cu TVA "
                    "colectat"),
        ],
    ),
]
