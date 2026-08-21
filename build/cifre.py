"""Numărătorile care descriu sistemul — citite din artefacte, niciodată scrise.

Un singur loc, doi consumatori: indexul pachetului și blocul de cifre din `README.md`.
Dacă fiecare și-ar număra singur, cele două ar începe să difere — iar diferența nu s-ar
vedea, pentru că amândouă ar arăta plauzibil.

Motivul pentru care fișierul ăsta există: README-ul chiar rămăsese în urmă. Afirma „23
corelații de control” când erau 29, și trimitea la `date/fluxuri.py`, fișier dispărut la
reorganizarea pe clase. Era singurul artefact cu cifre pe care nicio poartă nu-l
verifica.
"""
import os
import re
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

RADACINA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(RADACINA, "dist")

PLAN = "Plan_de_conturi_ROL_Analitice_Fluxuri_SAGA.xlsx"
MODULE = "Module_Declarative_Fluxuri.xlsx"

RE_FLUX = re.compile(r"^(F-(\d)\d\d)\b")
RE_COREL = re.compile(r"^C-\d\d$")
RE_CONT = re.compile(r"^\d{3,4}([./]\d+)?$")


def _prima_coloana(ws):
    for r in ws.iter_rows(min_col=1, max_col=1, values_only=True):
        yield str(r[0] or "").strip()


def citeste():
    """Toate numărătorile, într-un dicționar. Ridică dacă workbook-urile lipsesc."""
    from date import documente as ddoc
    from date import inchideri as dinch
    from date import intrebari as dintr
    from build import parcurs as bparc

    cale_plan = os.path.join(DIST, PLAN)
    if not os.path.exists(cale_plan):
        raise SystemExit(f"cifre: lipsește {PLAN} — rulează `make build`")

    wbp = openpyxl.load_workbook(cale_plan, read_only=True)
    fluxuri, pe_clasa = set(), {}
    for v in _prima_coloana(wbp["Fluxuri"]):
        m = RE_FLUX.match(v)
        if m:
            fluxuri.add(m.group(1))
            pe_clasa[m.group(2)] = pe_clasa.get(m.group(2), set()) | {m.group(1)}
    conturi = {v for v in _prima_coloana(wbp["Plan de conturi"]) if RE_CONT.match(v)}
    corelatii = {v for v in _prima_coloana(wbp["Corelații de control"]) if RE_COREL.match(v)}
    # Două cifre diferite, ambele adevărate, cu etichete care spun ce numără:
    # câte conturi sunt CLASIFICATE Tier A în plan, și câte au rând DETALIAT în foaia
    # de analitice. README-ul afirma o a treia, care nu era niciuna din ele.
    ws = wbp["Plan de conturi"]
    cap = next(([str(x or "") for x in r]
                for r in ws.iter_rows(min_col=1, max_col=12, values_only=True)
                if str(r[0] or "").strip() == "Simbol"), None)
    i_tier = [k for k, x in enumerate(cap or []) if "Tier" in x]
    tier_a = 0
    if i_tier:
        tier_a = sum(1 for r in ws.iter_rows(min_col=1, max_col=12, values_only=True)
                     if RE_CONT.match(str(r[0] or "").strip())
                     and str(r[i_tier[0]] or "").strip().upper().startswith("A"))
    detaliate = len({v for v in _prima_coloana(wbp["Analitice (Tier A)"])
                     if RE_CONT.match(v)})
    foi = len(wbp.sheetnames)
    wbp.close()

    wbm = openpyxl.load_workbook(os.path.join(DIST, MODULE), read_only=True)
    module = {str(r[0] or "").strip()
              for r in wbm["CatalogModule"].iter_rows(min_col=2, max_col=2,
                                                      values_only=True)
              if str(r[0] or "").strip().startswith("MOD_")}
    foi_module = len(wbm.sheetnames)
    wbm.close()

    return dict(
        fluxuri=len(fluxuri),
        pe_clasa={c: len(v) for c, v in sorted(pe_clasa.items())},
        conturi=len(conturi), corelatii=len(corelatii),
        tier_a=tier_a, detaliate=detaliate,
        cadente=len(dinch.CADENTA), module=len(module), foi=foi, foi_module=foi_module,
        documente=len(ddoc.DOCUMENTE),
        intrebari=len(dintr.toate()),
        deschise=len([q for _, q in dintr.toate() if not q["raspuns"]]),
        verificate=len(dintr.verificate()),
        decizii=len(dintr.decizii()),
        porti=len(bparc.porti()),
    )
