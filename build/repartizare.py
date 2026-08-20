"""Taie sursa împărțită pe subsecțiuni și verifică unde a ajuns fiecare.

Perechea lui `date/repartizare.py`: acolo se declară unde merge fiecare bucată, aici se
verifică faptul că a ajuns acolo. Poarta 16 din `build/verifica.py` cheamă `verifica()`.

Două reguli de comparație, ambele cu precedent în sistem:

1. **Numerotarea titlurilor nu e conținut.** `### 2.1 Achiziția` din sursă devine
   `### 7.3 Achiziția` în destinație, pentru că destinația are numerotarea ei. E același
   raționament ca la renumerotarea fluxurilor în poarta 9: poziția e liberă, textul nu.

2. **Rândurile de tabel se compară pe celule, nu pe rând întreg.** Un tabel de sursă
   ajunge rareori tabel identic în destinație — tabelul de conturi din §11 devine
   coloane în `Plan de conturi`. Celula rămâne însă celulă. Sub PRAG nu se verifică
   nimic individual, ca peste tot în sistem.
"""
import os
import re

from build.conservare import PRAG, _normalizeaza
from date import documente as ddoc
from date import repartizare as drep
from date import reformulari as dreform

RADACINA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#: Accentul Markdown și backslash-urile de escape sunt FORMATARE, nu conținut: aceeași
#: propoziție ajunge „**sold zero**” în document și „sold zero” într-o celulă de Excel.
#: Din același motiv se compară case-insensitive — titlul unei foi e majuscul din stil,
#: nu pentru că ar spune altceva. Ambele părți trec prin aceeași normalizare.
RE_ACCENT = re.compile(r"[*`\\_]+")

RE_TITLU = re.compile(r"^(#{2,3})\s+(.*)$")
#: „## 2. Mărfuri…”, „### 2.1 Achiziția”, „### Lunar — obligatoriu” (fără număr)
RE_NUMAR = re.compile(r"^\d+(\.\d+)*\.?\s+")

PREAMBUL = "(preambul)"


#: Workbook-ul-sămânță din training 4 a fost scris fără diacritice („Instalatii
#: tehnice si mijloace de transport”), sursa nouă le are. E același cuvânt, deci
#: pentru verificarea de plasare diacritica se pliază. Poarta 9 NU face asta: acolo se
#: compară textul cu el însuși, iar o diacritică pierdută chiar ar fi o modificare.
DIACRITICE = str.maketrans("ăâîșşțţĂÂÎȘŞȚŢ", "aaissttAAISSTT")


def _norm(s):
    """Normalizarea porții 16: cea comună, plus accent Markdown, majuscule, diacritice."""
    return RE_ACCENT.sub("", _normalizeaza(s)).strip().lower().translate(DIACRITICE)


def cheie_titlu(titlu):
    """Titlul fără marcajul de nivel și fără numerotare — ce rămâne e conținutul."""
    m = RE_TITLU.match(titlu)
    text = m.group(2) if m else titlu
    return _norm(RE_NUMAR.sub("", text))


def sectiuni(text):
    """[(titlu, [linii])] — sursa tăiată pe titluri, în ordinea din fișier.

    Un `##` ține doar liniile lui proprii, până la primul `###`. Subsecțiunile sunt
    intrări separate, pentru că exact acolo se rupe sursa: §2 e despre mărfuri, dar
    §2.6 e închiderea exercițiului.
    """
    out, curent = [], (PREAMBUL, [])
    for linie in text.split("\n"):
        if RE_TITLU.match(linie):
            out.append(curent)
            curent = (linie.strip(), [])
        else:
            curent[1].append(linie)
    out.append(curent)
    return [(t, l) for t, l in out if t != PREAMBUL or any(x.strip() for x in l)]


def fragmente(linii):
    """Bucățile de text care se verifică individual: linii, iar tabelele pe celule."""
    out = []
    for linie in linii:
        s = linie.strip()
        if not s or set(s) <= set("|-: "):        # separatorul de tabel nu e conținut
            continue
        bucati = [c for c in s.split("|")] if s.startswith("|") else [s]
        for b in bucati:
            n = _norm(b)
            if len(n) >= PRAG:
                out.append((n, s))
    return out


def _corpus(dest, foi):
    """Mulțimea liniilor normalizate ale destinației."""
    tinta, fel = drep.DESTINATII[dest]
    if fel == "foaie":
        return {_norm(l) for l in foi.get(tinta, set())}
    cale = os.path.join(RADACINA, tinta)
    if not os.path.exists(cale):
        return None
    with open(cale, encoding="utf-8") as f:
        brut = f.read()
    out = set()
    for linie in brut.split("\n"):
        s = linie.strip()
        for b in (s.split("|") if s.startswith("|") else [s]):
            n = _norm(b)
            if n:
                out.add(n)
        if RE_TITLU.match(s):
            out.add(cheie_titlu(s))
    return out


def verifica(foi):
    """(orfane, lipsa, fara_artefact).

    orfane        — subsecțiuni fără destinație declarată (16a)
    lipsa         — [(titlu, destinație, fragment)] care nu s-au regăsit acolo (16b)
    fara_artefact — destinații al căror fișier nu există încă
    """
    cale = os.path.join(RADACINA, drep.SURSA)
    with open(cale, encoding="utf-8") as f:
        text = f.read()
    # Sursa trece prin înlocuirile declarate ale documentelor înainte de comparație.
    # Declararea singură n-ar ajunge: înlocuirea prinde un FRAGMENT de linie, iar
    # poarta compară linii și celule întregi. Aplicată unde nu apare, e un no-op.
    for cfg in ddoc.DOCUMENTE:
        for i in cfg.get("inlocuiri") or []:
            text = text.replace(i["text"], i["devine"])

    declarate = {_norm(t) for t in dreform.DECLARATE}
    # titlurile de bloc absorbite într-o secțiune-gazdă: dispariția lor e o
    # decizie de repartizare, declarată cu gazda ei în date/repartizare.py
    declarate |= {_norm(t) for t in drep.ABSORBITE}
    declarate |= {cheie_titlu(t) for t in drep.ABSORBITE if t.startswith("#")}
    # Un text înlocuit declarat într-un document e declarat pentru TOATE porțile de
    # conservare, nu doar pentru cea care l-a văzut prima. Altfel aceeași decizie ar
    # trebui scrisă de două ori, iar cele două copii ar începe să difere.
    for cfg in ddoc.DOCUMENTE:
        for i in cfg.get("inlocuiri") or []:
            declarate.add(_norm(i["text"]))
    cunoscute = {cheie_titlu(t) for t in drep.UNDE}

    orfane, lipsa, fara_artefact = [], [], []
    cache = {}
    for titlu, linii in sectiuni(text):
        cheie = cheie_titlu(titlu) if titlu != PREAMBUL else PREAMBUL
        if cheie not in cunoscute and titlu != PREAMBUL:
            orfane.append(titlu)
            continue
        dest = next((d for t, d in drep.UNDE.items()
                     if (cheie_titlu(t) if t != PREAMBUL else PREAMBUL) == cheie), None)
        if dest is None:
            orfane.append(titlu)
            continue
        if dest not in cache:
            cache[dest] = _corpus(dest, foi)
        corpus = cache[dest]
        if corpus is None:
            if dest not in fara_artefact:
                fara_artefact.append(dest)
            continue
        de_cautat = list(fragmente(linii))
        if titlu != PREAMBUL:
            de_cautat.append((cheie, titlu))
        for n, brut in de_cautat:
            if n in declarate or n in corpus:
                continue
            if any(n in c for c in corpus):
                continue
            lipsa.append((titlu, dest, brut))
    return orfane, lipsa, fara_artefact
