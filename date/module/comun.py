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


def sufix(m):
    """Sufixul foilor unui modul.

    De obicei e codul fără prefix (MOD_SALARII → `Declarații_SALARII`), dar nu mereu:
    MOD_TVA_INCASARE are foi `…_TVA_INC`, MOD_VANZ_AMANUNT are `…_AMANUNT`. Sufixul se
    declară atunci în `CATALOG['sufix']`. Alternativa — redenumirea foilor ca să se
    potrivească cu codul — ar rupe orice referință existentă la ele, pentru un câștig de
    simetrie; portarea nu are voie să facă asta.
    """
    return m.CATALOG.get("sufix") or m.COD.removeprefix("MOD_")


#: Tiparul obișnuit: patru foi, în ordinea în care se folosesc.
PREFIXE_STANDARD = ("Declarații", "Reguli", "Jurnale", "NotaExport")


def foi(m):
    """Numele foilor pe care modulul le construiește EFECTIV.

    Nu toate modulele au cele patru foi standard. MOD_INCHIDERE_LUNARA produce un
    verdict, nu o înregistrare, deci are `Verificări_` și `Abateri_` în locul lui
    `Jurnale_` și `NotaExport_`; MOD_DECONT are în plus un `Registru_`. Cine deviază
    își declară prefixele în `CATALOG['prefixe']`.

    Coloana „Foile din modul” din `Index module` se generează de aici. Înainte lista era
    presupusă — cele patru prefixe standard, pentru toată lumea — deci pentru
    MOD_INCHIDERE_LUNARA trimitea la două foi care nu există. Aceeași clasă de greșeală
    ca „Declarații_TVA” din sămânță, doar că de data asta produsă de generator.
    """
    return [f"{p}_{sufix(m)}" for p in (m.CATALOG.get("prefixe") or PREFIXE_STANDARD)]


#: Modulele care stau la coadă indiferent de clasa fluxurilor lor.
FINAL = "final"


def cheie_ordine(m):
    """Cheia de sortare a unui modul: (clasa minimă acoperită, cel mai mic ID de flux).

    Ordinea documentului e ordinea planului de conturi — clasa 1 → 5 — nu ordinea în
    care au fost adăugate modulele. Până acum poziția se scria de mână în `MODULE`, iar
    asta a derapat exact cum derapează orice listă întreținută manual: după opt commituri
    de adăugiri, 12 module din 22 stăteau în afara ordinii pe care fișierul o declara în
    propriul docstring — MOD_INCHIDERE_EX, care acoperă un flux de clasa 1, ajunsese pe
    poziția 15, după clasa 5.

    Aici se calculează. Nimeni nu mai alege poziția, deci nimeni n-o mai poate greși.

    `CATALOG['ordine'] = "final"` scoate modulul din regulă și îl trimite la coadă —
    pentru cele care VERIFICĂ rezultatul celorlalte, nu produc înregistrări proprii.
    """
    from date import ordine as O

    if m.CATALOG.get("ordine") == FINAL:
        return (9, "")

    fluxuri = [O.HARTA.get(f.strip(), f.strip())
               for f in str(m.CATALOG["fluxuri"]).replace(";", ",").split(",")
               if f.strip().startswith("F-")]
    clase = [int(f[2]) for f in fluxuri if len(f) > 2 and f[2].isdigit()]
    return (min(clase) if clase else 8, min(fluxuri) if fluxuri else "")
