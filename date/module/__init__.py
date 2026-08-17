"""Modulele declarative adăugate în Etapa 4.

Fiecare modul expune `COD`, `CATALOG` (rândul din CatalogModule) și
`construieste(F, P)`, unde F e fabrica de foi (build.foaie.Foaie legat de workbook)
și P e dicționarul de referințe către parametrii globali.
"""
from . import capitaluri, iesire_mf, imobilizari, leasing_fin

MODULE = [imobilizari, iesire_mf, capitaluri, leasing_fin]

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
]

# Module care existau în CatalogModule ca „EXEMPLU EXTERN” și sunt acum implementate.
# Rândul vechi își păstrează poziția, dar primește un status nou care trimite la rândul
# implementat. Poarta 9 acceptă schimbarea DOAR pentru codurile enumerate aici.
STATUS_INLOCUIT = ["MOD_LEASING_FIN"]

__all__ = ["MODULE", "PARAMETRI_NOI", "STATUS_INLOCUIT"]
