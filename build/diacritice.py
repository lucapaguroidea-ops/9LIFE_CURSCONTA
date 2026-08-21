"""Aplică harta de diacritice pe cele două foi rămase în registrul vechi.

Trei reguli, toate restrictive:

1. **Doar pe foile din `FOI`.** Restul workbook-ului e deja în registrul nou.
2. **Niciodată pe coloana de simbol.** Se recunoaște după antet, iar orice celulă care
   arată a cont e sărită indiferent de coloană. Un simbol atins ar rupe navigarea și,
   mai rău, poarta 20.
3. **Doar cuvinte din hartă.** Ce nu e în hartă rămâne cum e. Fără regex de ghicit.

Potrivirea e pe cuvânt întreg și păstrează majuscula inițială: „Actiuni” → „Acțiuni”,
„actiuni” → „acțiuni”. Cuvintele integral majuscule (titluri de secțiune) primesc forma
majusculă a înlocuirii.
"""
import re

from date import diacritice as D

#: Ce arată a simbol de cont: 3–4 cifre, eventual cu analitic. Aceeași formă ca în
#: `build/cifre.py` — o celulă care se potrivește nu se atinge niciodată.
RE_CONT = re.compile(r"^\d{3,4}([./][\w.]+)?$")

_RE_CUVANT = re.compile(r"[A-Za-z][A-Za-z\-']*")


def _forma(gasit, inlocuire):
    """Păstrează felul în care era scris cuvântul găsit."""
    if gasit.isupper():
        return inlocuire.upper()
    if gasit[:1].isupper():
        return inlocuire[:1].upper() + inlocuire[1:]
    return inlocuire


def aplica_text(text):
    """Textul cu diacriticele restaurate. Întoarce (text_nou, câte cuvinte s-au schimbat)."""
    schimbate = 0

    def fn(m):
        nonlocal schimbate
        g = m.group(0)
        nou = D.HARTA.get(g.lower())
        if nou is None:
            return g
        schimbate += 1
        return _forma(g, nou)

    return _RE_CUVANT.sub(fn, text), schimbate


def aplica(wb):
    """Aplică harta pe workbook. Întoarce (celule atinse, cuvinte schimbate)."""
    celule = cuvinte = 0
    for nume in D.FOI:
        ws = wb[nume]
        # coloanele de simbol, după antet — se sar cu totul
        col_simbol = set()
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.strip().lower() in D.CAP_SIMBOL:
                    col_simbol.add(c.column)
        for row in ws.iter_rows():
            for c in row:
                if not isinstance(c.value, str) or c.data_type == "f":
                    continue
                if c.column in col_simbol or RE_CONT.match(c.value.strip()):
                    continue
                nou, n = aplica_text(c.value)
                if n:
                    c.value = nou
                    celule += 1
                    cuvinte += n
    return celule, cuvinte


def ramase(wb):
    """Cuvintele din cele două foi care nu sunt nici în hartă, nici în excepții.

    Raport, nu poartă. Prima versiune filtra cu o euristică („conține «ti» + vocală,
    se termină în «-ari»…”) și scotea 31 de candidați, dintre care ZERO aveau nevoie de
    ceva: „gestiune”, „venituri”, „privind”, „furnizori” se scriu exact așa. Un raport
    care semnalează doar fals pozitivi e mai rău decât niciunul — te învață să-l ignori,
    și atunci nu-l mai citești nici când are dreptate.

    Deci fără euristică: lista întreagă a cuvintelor nemapate, cu frecvența lor. La
    scrierea hărții au fost parcurse toate cele 642 de cuvinte distincte din cele două
    foi; 192 au primit intrare, 15 sunt omografe declarate, restul nu cer nimic. Lista
    de aici e pentru CE VINE — un set nou de notițe aduce vocabular nou, iar atunci se
    uită cineva peste diferență.
    """
    import collections
    DIAC = set("ăâîșțĂÂÎȘȚ")
    out = collections.Counter()
    for nume in D.FOI:
        for row in wb[nume].iter_rows():
            for c in row:
                if not isinstance(c.value, str) or DIAC & set(c.value):
                    continue
                for w in _RE_CUVANT.findall(c.value):
                    lw = w.lower()
                    if lw not in D.HARTA and lw not in D.EXCEPTII and len(lw) > 3:
                        out[lw] += 1
    return out
