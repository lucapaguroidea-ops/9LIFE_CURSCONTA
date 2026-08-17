"""Textele din originalul training 4 care au voie să dispară, fiecare cu motiv.

Poarta de conservare (build/conservare.py) verifică faptul că nimic din conținutul
original nu se pierde. Când un text chiar TREBUIE înlocuit — pentru că era greșit
sau pentru că a devenit fals — se trece aici, explicit. Fără intrare în lista asta,
build-ul pică.

Regula: se declară doar CORECȚII și STATUSURI DEVENITE FALSE. Dacă textul original
era pur și simplu mai scurt decât cel nou, nu se declară — se contopesc (vezi
auto-merge-ul din build/build_plan.py, care păstrează originalul și adaugă la el).
"""

INLOCUIRI = [
    # ---- notații de cont greșite în coloana „Analitice recomandate” ----------
    dict(
        text="101.1 nevarsat / 101.2 varsat",
        motiv="Notație inexistentă. OMFP 1802/2014 definește conturile 1011 „Capital "
              "subscris nevărsat” și 1012 „Capital subscris vărsat” — nu analitice "
              "„101.1 / 101.2” ale lui 101.",
        devine="1011 subscris nevărsat / 1012 subscris vărsat [N]",
    ),
    dict(
        text="151.1 litigii / 151.2 garanții / 151.8 alte [N]",
        motiv="Aceeași problemă de notație: conturile sunt 1511, 1512, 1514, 1516, 1518. "
              "În plus, lista originală omitea restructurarea (1514) și impozitele (1516).",
        devine="1511 litigii / 1512 garanții / 1514 restructurare / 1516 impozite / 1518 alte [N]",
    ),
    dict(
        text="280.x pe tip imobilizare",
        motiv="„280.x” nu e o notație de cont. Conturile sunt 2803, 2805, 2808, iar "
              "regula reală e oglinda cu contul de activ (vezi C-14).",
        devine="2803 / 2805 / 2808, în oglindă cu contul de activ",
    ),
    # ---- statusuri devenite false -------------------------------------------
    dict(
        text="- (modul extern Leasing)",
        motiv="MOD_LEASING_FIN nu mai e extern: e implementat în "
              "Module_Declarative_Fluxuri.xlsx și acoperit de flux propriu.",
        devine="F-50",
    ),
    dict(
        text="Template_leasing_financiar_auto, nu în Fluxuri",
        motiv="Idem — afirmația „nu în Fluxuri” a devenit falsă odată cu F-50.",
        devine="F-50 pas 9: 167 = scadențar, 1:1 cu contractul",
    ),
    # ---- retitulări care elimină concurența semantică între fluxuri ----------
    dict(
        text="Achiziție MF + amortizare",
        motiv="Titlu prea generic: concura cu fluxul de achiziție intracomunitară / import "
              "de mijloc fix, care tratează alt regim. Precizarea „intern” le separă.",
        devine="Achiziție mijloc fix intern + amortizare liniară",
    ),
    dict(
        text="F-26 - Achiziție mijloc fix + amortizare",
        motiv="Idem, pe titlul blocului de monografie.",
        devine="F-204 — Achiziție mijloc fix intern + amortizare liniară",
    ),

    # ---- cifre care descriau starea veche a fișierului -----------------------
    dict(
        text="Fluxuri: 38/38 detaliate. Matrice Tier A: acoperire completă.",
        motiv="Numărătoare depășită: sunt 60 de fluxuri după trainingurile 2 și 3 și "
              "după cele două contopiri. Textul original e păstrat în foaia Istoric.",
        devine="Fluxuri: 60/60 detaliate. Matrice Tier A: acoperire completă.",
    ),
    dict(
        text="~38 fluxuri × pași, tabelar cu note complete + coloană Declarativ",
        motiv="Idem — descrierea structurii workbook-ului anunța 38 de fluxuri.",
        devine="60 fluxuri × pași, tabelar cu note complete + coloană Declarativ",
    ),
    dict(
        text="245+ rânduri, cu 3 coloane noi: Analitice recomandate · Factor · Flux (pas)",
        motiv="Planul are acum 270+ rânduri, după adăugarea conturilor care lipseau "
              "(1011, 1012, 1171, 1174, 2812, 6583 ș.a.).",
        devine="270+ rânduri, cu 3 coloane noi: Analitice recomandate · Factor · Flux (pas)",
    ),
    dict(
        text="Ilustrativ (sume descriptive)",
        motiv="Marcajul PARȚIAL de la 681/781 era corect când sumele erau descriptive. "
              "Acum 681 și 781 au cifre reale în F-50 (plafonul de 1.500 lei/lună) și "
              "F-51 (reluarea prin 7812), deci nota nu mai descrie realitatea.",
        devine="F-50 plafon 1.500 lei/lună; F-51 reluare 7812",
    ),
]

#: Doar textele, pentru poartă.
DECLARATE = [d["text"] for d in INLOCUIRI]

#: text original -> textul care îl înlocuiește (folosit de auto-merge ca să știe
#: că nu trebuie să contopească, ci să suprascrie).
SUPRASCRIE = {d["text"]: d["devine"] for d in INLOCUIRI}
