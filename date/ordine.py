"""Ordinea canonică a sistemului — singura sursă de adevăr pentru poziții și ID-uri.

Principiul: ordinea documentului este ordinea planului de conturi (clasa 1 → 9),
nu ordinea în care au fost adăugate trainingurile. ID-ul unui flux codifică clasa
contului său principal, deci un flux nou primește următorul număr liber din clasa
lui și stă fizic la locul lui, pentru totdeauna.

    F-1xx  capitaluri, provizioane, împrumuturi   (clasa 1)
    F-2xx  imobilizări                            (clasa 2)
    F-3xx  stocuri și producție                   (clasa 3)
    F-4xx  terți, TVA, declarativ                 (clasa 4)
    F-5xx  trezorerie                             (clasa 5)
    F-8xx  extrabilanțier                         (clasa 8)

Ordinea din listele de mai jos ESTE ordinea fizică din foaia „Fluxuri”. Ca să
inserezi un flux nou, îl pui la locul lui contabil în listă și îi dai următorul
număr liber din clasă — nu renumerota restul.
"""

# ---------------------------------------------------------------------------
# Harta: ID nou → (ID vechi, denumire scurtă pentru foaia Istoric)
#
# „vechi” se referă la numerotarea F-01…F-62 dinainte de refactorizare: F-01…F-44
# veneau din trainingul 4, F-45…F-62 din trainingurile 2 și 3.
# ---------------------------------------------------------------------------

CLASA_1 = [
    ("F-101", "F-45", "Constituire / majorare capital social"),
    ("F-102", "F-48", "Rezerve din reevaluare: 105 → 1175"),
    ("F-103", "F-46", "Repartizarea rezultatului: 121 → 129/1061 → 1171"),
    ("F-104", "F-37", "Închiderea exercițiului (121/129/117 + 691/697/4417)"),
    ("F-105", "F-47", "Corecția erorilor din exerciții anterioare (1174)"),
    ("F-106", "F-51", "Provizioane pentru litigii (151x)"),
    ("F-107", "F-49", "Credit bancar în valută (162x)"),
    ("F-108", "F-50", "Leasing financiar autoturism cu deductibilitate 50%"),
    ("F-109", "F-71", "Dividende certe din rezultatul reportat (1171 → 457)"),
    ("F-110", "F-72", "Dividende interimare (463) cu plafonul lui 121"),
    ("F-111", "F-73", "Creditarea de societate (4551)"),
    ("F-112", "F-74", "Majorarea capitalului social din creditare"),
    ("F-113", "F-75", "Remiterea de datorie (4551 → 7582)"),
    ("F-114", "F-76", "Analiticele pe 1012 = cotele de participare"),
]

CLASA_2 = [
    ("F-201", "F-52", "Imobilizări necorporale (20x)"),
    ("F-202", "F-53", "Terenuri și amenajări de terenuri (211)"),
    ("F-203", "F-54", "Construcții (212)"),
    ("F-204", "F-26", "Achiziție mijloc fix intern + amortizare liniară"),
    ("F-205", "F-55", "Instalații tehnice și mijloace de transport (213)"),
    ("F-206", "F-56", "Investiții imobiliare (215) și defalcarea teren / construcție"),
    ("F-207", "F-57", "Imobilizări facturate dar nesosite (223 / 224)"),
    ("F-208", "F-58", "Imobilizări în curs de execuție (231)"),
    ("F-209", "F-28", "Producție de imobilizări în regie proprie (722)"),
    ("F-210", "F-29", "Subvenție 475 eliberată pe măsura amortizării"),
    ("F-211", "F-59", "Vânzarea unui mijloc fix și testul valorii rămase"),
    ("F-212", "F-60", "Casarea unui mijloc fix și piesele recuperate"),
    ("F-213", "F-62", "Imobilizări financiare (26x)"),
    ("F-214", "F-61", "Controlul lunar analitic ↔ sintetic la imobilizări"),    ("F-215", "F-77", "Subvenție din fonduri europene (4452 → 4758 → 7584)"),
    ("F-216", "F-78", "Plus la inventar la imobilizări (21x → 4754)"),

]

CLASA_3 = [
    ("F-301", "F-01", "Aprovizionare internă (fără tranzit)"),
    ("F-302", "F-02", "Aprovizionare prin 32x (tranzit)"),
    ("F-303", "F-03", "Aprovizionare intracomunitară cu taxare inversă"),
    ("F-304", "F-39", "Intersecție 32x ↔ 408 (marfă parțială)"),
    ("F-305", "F-04", "Obiecte de inventar cu 8035 cap-coadă"),
    ("F-306", "F-08", "Diferențe de preț 308 / 348"),
    ("F-307", "F-09", "Ajustare pentru deprecierea stocurilor"),
    ("F-308", "F-10", "Piese de schimb 3024 → 371"),
    ("F-309", "F-11", "Stocuri aflate la terți"),
    ("F-310", "F-12", "Ambalaje + taxa AFM"),
    ("F-311", "F-05", "Producție termopan multi-stadiu (331 → 711 → 345)"),
    ("F-312", "F-07", "Servicii în curs 332 / 712"),
    ("F-313", "F-06", "Deșeuri 346"),
    ("F-314", "F-41", "Sold 331 la 31.12 → inventar → reluare ianuarie"),
    ("F-315", "F-13", "Vânzare en-gros"),
    ("F-316", "F-14", "Gestiune amănunt completă"),
    ("F-317", "F-43", "Vânzare parțială amănunt"),
    ("F-318", "F-40", "Retur din gestiune amănunt"),
    ("F-319", "F-15", "Import prin comisionar (446.VAMA)"),
    ("F-320", "F-16", "Import cu plată directă în vamă"),
    ("F-321", "F-90", "Marfa devenită materie primă (301 = 371) și consumul din gestiune"),
]

CLASA_4 = [
    ("F-401", "F-17", "TVA la încasare (4428.INC)"),
    ("F-402", "F-18", "Taxare inversă internă"),
    ("F-403", "F-19", "Livrare intracomunitară scutită"),
    ("F-404", "F-20", "Export"),
    ("F-405", "F-21", "Închiderea lunară de TVA"),
    ("F-406", "F-22", "Înregistrări fără document (50% auto, lipsă la inventar)"),
    ("F-407", "F-42", "Corecție după D300 depusă"),
    ("F-408", "F-23", "408 / 418 (facturi nesosite / de întocmit)"),
    ("F-409", "F-24", "Reduceri comerciale 609 / 709"),
    ("F-410", "F-25", "Avansuri clienți / furnizori (419 / 409)"),
    ("F-411", "F-34", "Sumă neidentificată din extras → 473"),
    ("F-412", "F-30", "Avansuri 471 / 472 (regularizare temporală)"),
    ("F-413", "F-32", "Salarii"),
    ("F-414", "F-38", "Decontări 481 / 482 (unitate ↔ subunități)"),
    ("F-415", "F-63", "Încasare peste factură (supraîncasare → 419 + TVA)"),
    ("F-416", "F-64", "Concediu medical (împărțire angajator / FNUASS)"),
    ("F-417", "F-65", "Poprire pe salariu (rețineri datorate terților)"),
    ("F-418", "F-66", "Drepturi de personal neridicate (421 → 426)"),
    ("F-419", "F-67", "Creanță față de un fost salariat (4282)"),
    ("F-420", "F-68", "Impozitul pe venitul microîntreprinderii (698 → 4418)"),
    ("F-421", "F-69", "Decizie de impunere ANAF prin 4481 (în afara rulajului curent)"),
    ("F-422", "F-70", "Închiderea lunară a obligațiilor salariale (rulaj = sold)"),
    ("F-423", "F-79", "Taxe locale prin 446, cu 471 la perioade lungi"),
    ("F-424", "F-80", "Plată eronată către buget (4482)"),
    ("F-425", "F-81", "Debitori diverși 461 (mijloc fix vândut și imputație)"),
    ("F-426", "F-82", "Decontări din operațiuni în participație (458)"),
]

CLASA_5 = [
    ("F-501", "F-33", "Viramente interne 581"),
    ("F-502", "F-35", "Avansuri de trezorerie (542)"),
    ("F-503", "F-84", "Efecte de încasat: CEC (5112) și bilet la ordin (5113)"),
    ("F-504", "F-85", "Scontarea biletului la ordin (5114)"),
    ("F-505", "F-86", "Dobânda la credit: fixă prin 471 vs. variabilă prin 5186"),
    ("F-506", "F-87", "Dobânzi de încasat (5187 → 472 → 766)"),
    ("F-507", "F-88", "Linie de credit (5191) vs. credit cu scadențar"),
    ("F-508", "F-89", "Tichete de masă: 5328 → 6422"),
]

CLASA_8 = [
    ("F-801", "F-36", "Angajamente extrabilanțiere"),
    ("F-802", "F-44", "Inventariere 8035 (scriptic vs. faptic)"),
]

BLOCURI = [
    (1, "CLASA 1 — CAPITALURI, PROVIZIOANE, ÎMPRUMUTURI", CLASA_1),
    (2, "CLASA 2 — IMOBILIZĂRI", CLASA_2),
    (3, "CLASA 3 — STOCURI ȘI PRODUCȚIE", CLASA_3),
    (4, "CLASA 4 — TERȚI, TVA, DECONTĂRI", CLASA_4),
    (5, "CLASA 5 — TREZORERIE", CLASA_5),
    (8, "CLASA 8 — CONTURI ÎN AFARA BILANȚULUI", CLASA_8),
]

ORDINE = [e for _, _, bloc in BLOCURI for e in bloc]

# ---------------------------------------------------------------------------
# Contopiri: fluxuri care se absorb în altul.
#
# Nu se pierde nimic — pașii fluxului absorbit devin o VARIANTĂ în interiorul
# celui gazdă, cu cifrele lui proprii. Motivul contopirii se scrie în foaia
# Istoric, ca să se știe de ce a dispărut ID-ul vechi.
# ---------------------------------------------------------------------------

CONTOPIRI = {
    "F-27": ("F-208", "Varianta A — doar terți, fără salarii capitalizate",
             "F-27 era conținut practic de F-58: aceeași secvență 231 → 21x, "
             "doar fără pasul de capitalizare a salariilor."),
    "F-31": ("F-211", "Varianta A — cedare simplă, fără testul valorii rămase",
             "F-31 și F-59 tratau același subiect (vânzarea unui mijloc fix) "
             "cu cifre diferite; F-59 adaugă testul fiscal care lipsea."),
}

# Retitulări, ca fluxurile să nu mai concureze semantic între ele.
RETITULARI = {
    "F-204": "Achiziție mijloc fix intern + amortizare liniară",
}

# ---------------------------------------------------------------------------
# Derivate
# ---------------------------------------------------------------------------

#: ID vechi → ID nou. Include contopirile (F-27 → F-208).
HARTA = {vechi: nou for nou, vechi, _ in ORDINE}
HARTA.update({vechi: nou for vechi, (nou, _, _) in CONTOPIRI.items()})

#: ID nou → ID vechi (doar fluxurile care au supraviețuit ca entitate proprie).
INVERS = {nou: vechi for nou, vechi, _ in ORDINE}

#: ID nou → clasa contabilă.
CLASA = {nou: cls for cls, _, bloc in BLOCURI for nou, _, _ in bloc}

#: ID nou → denumire scurtă (pentru Istoric și matrice).
DENUMIRE = {nou: den for nou, _, den in ORDINE}


def clasa_din_id(fid):
    """F-317 → 3. Funcționează pentru orice ID nou, inclusiv unele neînregistrate încă."""
    return int(fid.split("-")[1][0])


def urmatorul_liber(clasa):
    """Următorul număr liber din clasă — pentru fluxuri adăugate în viitor."""
    folosite = [int(n.split("-")[1]) for n in CLASA if CLASA[n] == clasa]
    return f"F-{max(folosite) + 1}" if folosite else f"F-{clasa}01"
