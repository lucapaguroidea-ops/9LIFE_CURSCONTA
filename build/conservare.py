"""Poarta de conservare: nimic din conținutul original nu dispare tăcut.

Ideea: fiecare linie de text din workbook-urile ORIGINALE (`surse/training-4-…`)
trebuie să se regăsească undeva în workbook-urile generate. Oriunde — altă foaie,
alt rând, altă coloană. Poarta verifică **mulțimea** conținutului, nu ordinea lui,
tocmai ca reordonarea să fie liberă iar pierderea de conținut să fie imposibilă.

Ce NU e o pierdere:
  - renumerotarea fluxurilor (F-14 → F-316) — textul original e trecut prin harta
    de renumerotare înainte de căutare;
  - reformatarea spațiilor;
  - restaurarea diacriticelor („Marfuri” → „Mărfuri”). Aceeași categorie cu
    ghilimelele și cratimele de mai jos: forma se schimbă, conținutul nu. Fără
    plierea asta ar trebui 649 de intrări în `date/reformulari.py`, care ar îneca
    fișierul în care stau motivele reale. Concesia declarată: poarta nu mai
    distinge două texte care diferă NUMAI prin diacritice;
  - fragmentele scurte (sub PRAG caractere): coduri de cont, sume, „DA”/„NU”, „—”.
    Acelea sunt acoperite de porțile de sume și de corelații.

Ce E o pierdere: orice propoziție care exista și nu mai există, fără să fie
declarată în `date/reformulari.py` cu un motiv.
"""
import re

import openpyxl

#: Linii mai scurte de atât nu se verifică individual (coduri, sume, marcaje).
PRAG = 12

#: Diacriticele se pliază la baza lor înainte de comparație: „ă”→„a”, „ț”→„t”.
#:
#: E aceeași categorie cu ghilimelele și cratimele de mai jos — forma se schimbă,
#: conținutul nu. Fără plierea asta, restaurarea diacriticelor pe cele două foi rămase
#: în registrul vechi ar cere 279 de intrări în `date/reformulari.py`, care ar îneca
#: fișierul în care stau motivele reale.
#:
#: Concesia, declarată: poarta nu mai distinge două texte care diferă NUMAI prin
#: diacritice. E acceptabil pentru că harta din `date/diacritice.py` e explicită și
#: verificată de poarta 26 — nu se ghicește nimic, deci n-are ce să se strecoare pe aici.
_FARA_DIACRITICE = str.maketrans({
    "ă": "a", "â": "a", "î": "i", "ș": "s", "ț": "t", "ş": "s", "ţ": "t",
    "Ă": "A", "Â": "A", "Î": "I", "Ș": "S", "Ț": "T", "Ş": "S", "Ţ": "T",
})


def _normalizeaza(s):
    """Spații, ghilimele și diacritice uniforme — ca reformatarea să nu dea fals pozitiv."""
    s = str(s)
    s = s.replace(" ", " ").replace("„", '"').replace("”", '"')
    s = s.replace("’", "'").replace("‘", "'").replace("–", "-").replace("—", "-")
    s = s.translate(_FARA_DIACRITICE)
    return re.sub(r"\s+", " ", s).strip()


def linii_din_workbook(cale):
    """Toate liniile de text dintr-un workbook, normalizate, ca mulțime."""
    wb = openpyxl.load_workbook(cale)
    out = set()
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                v = cell.value
                if not isinstance(v, str):
                    continue
                for linie in v.split("\n"):
                    n = _normalizeaza(linie)
                    if len(n) >= PRAG:
                        out.add(n)
    return out


def aplica_harta(text, harta):
    """Trece ID-urile vechi de flux în cele noi, ca renumerotarea să nu pară pierdere.

    Se înlocuiește doar tokenul întreg (F-14, nu F-1 din F-14), de la cel mai lung
    la cel mai scurt, ca F-4 să nu ciopârțească F-44.
    """
    for vechi in sorted(harta, key=len, reverse=True):
        text = re.sub(rf"\b{re.escape(vechi)}\b", harta[vechi], text)
    return text


def verifica(surse, generate, harta, declarate):
    """Întoarce lista liniilor pierdute nedeclarat.

    surse / generate: liste de căi către workbook-uri.
    harta: {ID vechi: ID nou} pentru renumerotare.
    declarate: mulțime de linii normalizate care au voie să dispară.
    """
    prezente = set()
    for c in generate:
        prezente |= linii_din_workbook(c)

    # indexul de căutare: și textul brut, și cel cu ID-urile trecute prin hartă
    cautabil = prezente | {aplica_harta(t, harta) for t in prezente}

    declarate_n = {_normalizeaza(d) for d in declarate}

    pierdute = []
    for c in surse:
        for text in linii_din_workbook(c):
            if text in declarate_n:
                continue
            tinta = aplica_harta(text, harta)
            if tinta in cautabil or text in cautabil:
                continue
            # ultima șansă: textul poate fi înglobat într-o celulă mai lungă
            if any(tinta in p for p in cautabil):
                continue
            pierdute.append(text)
    return sorted(pierdute)
