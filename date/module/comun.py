"""Ce folosesc toate modulele declarative deopotrivă.

Stă separat de `__init__.py` fiindcă acela importă submodulele, iar submodulele au
nevoie de helperul de aici: importat din pachet, ar fi import circular.
"""

#: Câte rânduri se scanează în `CatalogModule` când un modul își caută steagul `Activ`.
#: Generos față de cele ~35 de rânduri reale, dar MĂRGINIT — și asta contează: motorul
#: de recalcul nu evaluează `INDEX(CatalogModule!A:A, …)` pe coloană întreagă. Formula
#: pe coloană întreagă e validă în Excel, deci nicio poartă n-o semnala; celula ieșea
#: pur și simplu goală la build, în toate cele patru module care o foloseau.
CATALOG_RANDURI = 200


def formula_activ(cod, activ="ACTIV", inactiv="INACTIV"):
    """Formula „Modul activ?” — căutată pe COD, nu pe rândul din catalog.

    Sămânța scria `=IF(CatalogModule!A14="DA",…)`, cu rândul scris în formulă. Mutai un
    rând în catalog și celula citea steagul altui modul, tăcut. Aici cheia e codul, deci
    reordonarea catalogului devine inofensivă — condiția pusă în plan înainte de a
    atinge ordinea rândurilor.
    """
    r = CATALOG_RANDURI
    return (f'=IF(INDEX(CatalogModule!$A$1:$A${r},'
            f'MATCH("{cod}",CatalogModule!$B$1:$B${r},0))="DA",'
            f'"{activ}","{inactiv}")')
