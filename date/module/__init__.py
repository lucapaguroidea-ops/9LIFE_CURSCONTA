"""Modulele declarative: fiecare execută unul sau mai multe fluxuri din planul de conturi.

Fiecare modul expune `COD`, `CATALOG` (rândul din CatalogModule) și
`construieste(F, P)`, unde F e fabrica de foi (build.foaie.Foaie legat de workbook)
și P e dicționarul de referințe către parametrii globali.

**Ordinea nu se scrie aici, se calculează.** `MODULE` e lista importurilor sortată cu
`comun.cheie_ordine`, adică pe clasa de conturi a fluxurilor acoperite. Scrisă de mână,
ordinea a derapat: după opt commituri de adăugiri, 12 module din 22 stăteau în afara
ordinii pe care acest fișier o declara în propriul docstring. Lista de mai jos e
alfabetică — poziția în workbook nu depinde de ea.
"""
from .comun import CATALOG_RANDURI, cheie_ordine, formula_activ  # noqa: F401
from . import (aprov_tranzit, avansuri, capitaluri, control_balanta, credit_valuta,
               decont, dividende, fara_document, iesire_mf, imobilizari,
               import_vamal, inchidere_ex,
               inchidere_lunara, inchidere_tva, intermediar, leasing_fin,
               neutralizare, provizion, salarii, salarii_evenimente, subventie,
               taxare_inversa, tva_incasare, vanz_amanunt)

#: Toate modulele, în ordine alfabetică. Ordinea de aici NU contează.
_TOATE = [aprov_tranzit, avansuri, capitaluri, control_balanta, credit_valuta,
          decont, dividende, fara_document, iesire_mf, imobilizari, import_vamal,
          inchidere_ex, inchidere_lunara,
          inchidere_tva, intermediar, leasing_fin, neutralizare, provizion, salarii,
          salarii_evenimente, subventie, taxare_inversa, tva_incasare, vanz_amanunt]

#: Ordinea reală: pe clasa de conturi, derivată din fluxurile acoperite. Foile din
#: workbook, `Index module` și `CatalogModule` o urmează pe asta.
MODULE = sorted(_TOATE, key=cheie_ordine)

# Parametri globali adăugați în foaia `Parametri`: cheie, etichetă, valoare, notă.
# Cheia se folosește în module ca P["cheie"] și se rezolvă la o referință de celulă.
PARAMETRI_NOI = [
    ("proc_rezerva", "Procent rezervă legală (din profitul brut)", 0.05,
     "art. 26 alin. (1) lit. a) Cod fiscal"),
    ("plafon_rezerva", "Plafon rezervă legală (din capitalul vărsat)", 0.20,
     "art. 183 Legea 31/1990 — capital subscris ȘI VĂRSAT"),
    ("prag_mf", "Prag mijloc fix (lei)", 5000,
     "OUG 8/2026, de la 25.02.2026; se actualizează anual cu inflația"),
    ("proc_vehicul", "Procent de deducere vehicule (regim mixt)", 0.50,
     "art. 298 CF (TVA) și art. 25 alin. (3) lit. l) CF (cheltuieli)"),
    ("plafon_amo_auto", "Plafon amortizare autoturism (lei/lună)", 1500,
     "art. 28 alin. (14) CF — NU se cumulează cu limitarea de 50%"),
    # cotele de salarii, confirmate pe toți cei 4 angajați din statul real 31.07.2026
    ("cota_cas", "CAS — pensie (pe brut)", 0.25, "art. 138 CF"),
    ("cota_cass", "CASS — sănătate (pe brut + tichete)", 0.10,
     "art. 156 CF — tichetele intră în bază, dar NU în baza CAS"),
    ("cota_impozit", "Impozit pe venit (pe venit net + tichete)", 0.10, "art. 78 CF"),
    ("cota_cam", "CAM — asigurare de muncă (pe brut)", 0.0225,
     "art. 220^3 CF — cheltuiala angajatorului, nu reținere"),
    ("cota_impozit_profit", "Impozit pe profit", 0.16,
     "art. 17 CF — folosit la cuantificarea efectului unei cheltuieli nedeductibile"),
    # Aceeași valoare ca impozitul pe profit, dar alt temei și alt istoric: dividendele
    # au trecut de la 8% la 10% și apoi la 16% pentru distribuirile de la 01.01.2026.
    # Un parametru comun ar lega două cote care se schimbă independent.
    ("cota_impozit_dividend", "Impozit pe dividende", 0.16,
     "art. 43 CF, modificat prin L. 141/2025 — cota urmează data DISTRIBUIRII"),
]

# Module care existau în CatalogModule ca „EXEMPLU EXTERN” și sunt acum implementate.
# Rândul vechi își păstrează poziția, dar primește un status nou care trimite la rândul
# implementat. Poarta 9 acceptă schimbarea DOAR pentru codurile enumerate aici.
STATUS_INLOCUIT = ["MOD_LEASING_FIN"]

__all__ = ["MODULE", "PARAMETRI_NOI", "STATUS_INLOCUIT", "formula_activ",
           "CATALOG_RANDURI", "cheie_ordine"]
