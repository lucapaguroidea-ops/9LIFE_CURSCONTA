"""Citește monografiile scrise în proză din documente și le face structură.

Poarta 1 verifică `ΣD = ΣC` doar pentru fluxurile din `date/`. În cele patru documente
stau peste o sută de blocuri de monografie la care nu se uită nimic — și prin care au
trecut deja două erori, prinse de citire, nu de o poartă: rezerva legală din trainingul 2
(5% din 250 ≠ 125) și avansul de 50.000 stornat cu 30.000, fără stornarea TVA.

O singură trecere, doi consumatori: **poarta 18** verifică echilibrul, iar
`build/html_out.py` randează aceleași înregistrări ca registru. Dacă randarea și-ar face
propria citire, cele două ar începe să difere — și tocmai asta a produs defectele din
`.html`-ul convertit de mână.

Trei convenții de scriere coexistă în documente, toate legitime:

    121 = 129      125 lei              separator „=”, sumă cu „lei”
    121  = 607    ·  20.000             convenția din 19.08, cu „·”
    %      =  404       60.500          articol compus, cu linii de continuare
    4093              50.000
    4426              10.500      (21% × 50.000)

**Poziția decide ce e sumă, nu forma.** După `debit <sep> credit`, orice număr e sumă —
inclusiv `6`, care altfel s-ar putea citi ca început de cont. Înainte de separator, orice
număr e cont — inclusiv `5121`, care altfel s-ar citi ca cinci mii o sută douăzeci și
unu. Fără regula asta, parserul confundă planul de conturi cu balanța.
"""
import os
import re

RADACINA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#: Un cont: 3–4 cifre, eventual cu analitic (`371.AM.21`, `401.RO`, `32x`, `121/129`).
CONT = r"%|\d[\d.x/]{1,}(?:\.[A-Za-zĂÂÎȘȚăâîșț0-9]+)*|\d{3,4}"

#: Separatorul dintre debit și credit. `-` doar înconjurat de spații, ca `613.NED` să nu
#: se rupă în două, iar `→` pentru monografiile scrise cu săgeată.
RE_ARTICOL = re.compile(
    rf"^(?P<ind>\s*)(?P<d>{CONT})\s*(?:=|→|(?<=\s)-(?=\s))\s*(?P<c>{CONT})\s*(?P<rest>.*)$")

#: O linie de continuare a unui articol compus: cont + sumă, FĂRĂ separator.
#: Indentarea nu se cere — documentele o scriu în ambele feluri, iar ce distinge
#: continuarea de un articol nou e absența separatorului, nu marginea din stânga.
RE_CONTINUARE = re.compile(rf"^(?P<ind>\s*)(?P<cont>{CONT})\s+(?P<rest>.*)$")

#: Sume: cu separator de mii, cu zecimale, sau întregi (poziția le confirmă).
RE_SUMA = re.compile(r"-?\d{1,3}(?:\.\d{3})+(?:,\d{1,2})?|-?\d+,\d{1,2}|-?\d+")

#: Afirmațiile aritmetice din proză: „5% din 250 = 12,50”, „0,1667 × 24.000 = 4.000”,
#: „5.000 ÷ 1,21 = 4.132,23”. ASTA e verificarea care ar fi prins eroarea rezervei legale
#: din trainingul 2 — articolul se echilibra (125 = 125), dar 5% din 250 nu e 125.
#:
#: `/` NU e operator aici: în corpusul ăsta separă conturi („635/6588 = 4426”, „6024 /
#: 6028 = 401”) mult mai des decât împarte. Cu el inclus, patru din șase potriviri erau
#: perechi de conturi citite ca împărțiri.
_N = r"\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+(?:,\d+)?"
RE_ARITMETIC = re.compile(
    rf"(?P<a>{_N})\s*(?P<pc>%)?\s*(?P<op>[×x*÷])\s*(?P<b>{_N})\s*=\s*(?P<c>{_N})")
RE_PROCENT_DIN = re.compile(
    rf"(?P<a>{_N})\s*%\s+din\s+(?P<b>{_N})\s*(?:=|→|:)\s*(?P<c>{_N})", re.I)


def afirmatii(cale):
    """[(rând, text, valoare calculată, valoare scrisă)] — aritmetica afirmată în text."""
    out = []
    with open(cale, encoding="utf-8") as f:
        for i, linie in enumerate(f, 1):
            for m in RE_ARITMETIC.finditer(linie):
                a, b, c = (numar(m.group(x)) for x in ("a", "b", "c"))
                if None in (a, b, c):
                    continue
                if m.group("pc"):
                    a /= 100
                if m.group("op") in "×x*":
                    r = a * b
                elif b:
                    r = a / b
                else:
                    continue
                out.append((i, m.group(0), r, c))
            for m in RE_PROCENT_DIN.finditer(linie):
                a, b, c = (numar(m.group(x)) for x in ("a", "b", "c"))
                if None in (a, b, c):
                    continue
                out.append((i, m.group(0), a / 100 * b, c))
    return out


def numar(text):
    """„26.640” → 26640.0, „4.132,23” → 4132.23, „55,25” → 55.25."""
    t = text.strip().replace(".", "").replace(",", ".")
    try:
        return float(t)
    except ValueError:
        return None


def _suma_din(rest):
    """(sumă, notă) din ce urmează după contul creditor.

    Se sare peste `·`, peste `lei` și peste procentele din paranteze explicative:
    „(21% × 50.000)” e o justificare a sumei, nu o a doua sumă.
    """
    rest = rest.strip()
    if rest.startswith("·"):
        rest = rest[1:].strip()
    # partea explicativă începe la prima paranteză sau la primul cuvânt
    m = RE_SUMA.match(rest)
    if not m:
        return None, rest
    suma = numar(m.group(0))
    nota = rest[m.end():].strip()
    if nota.lower().startswith("lei"):
        nota = nota[3:].strip()
    return suma, nota


def _e_articol(m):
    """Filtrează liniile care au `=` dar nu sunt articole contabile.

    „Adaos aferent vânzărilor = 0,1667 × 24.000 = 4.000” are separator, dar în stânga
    are text, nu cont. Fără filtrul ăsta, fiecare formulă explicativă din documente ar
    intra în poartă ca articol dezechilibrat.
    """
    d, c = m.group("d"), m.group("c")
    for x in (d, c):
        if x == "%":
            continue
        if not re.fullmatch(r"\d{3,4}(?:[./][\w.]+)*", x):
            return False
    return True


def articole(linii, prima=1):
    """[articol] dintr-un bloc. Un articol are debit, credit, sumă și note.

    Articolul compus (`%` pe o parte) adună liniile de continuare care îl urmează, până
    la prima linie care nu mai e continuare.
    """
    out = []
    i = 0
    while i < len(linii):
        l = linii[i]
        m = RE_ARTICOL.match(l)
        if not m or not _e_articol(m):
            i += 1
            continue

        suma, nota = _suma_din(m.group("rest"))
        art = dict(rand=prima + i, brut=[l], nota=nota,
                   debit=[], credit=[], total=suma, compus=False)
        d, c = m.group("d"), m.group("c")

        if "%" in (d, c):
            art["compus"] = True
            art["parte_multipla"] = "debit" if d == "%" else "credit"
            fix = c if d == "%" else d
            (art["credit"] if d == "%" else art["debit"]).append((fix, suma))
            j = i + 1
            while j < len(linii):
                mc = RE_CONTINUARE.match(linii[j])
                if not mc or RE_ARTICOL.match(linii[j]):
                    break
                s, n = _suma_din(mc.group("rest"))
                if s is None:
                    break
                art["brut"].append(linii[j])
                (art["debit"] if d == "%" else art["credit"]).append((mc.group("cont"), s))
                j += 1
            # Capul compus poate să nu declare totalul („4111 = %”). Atunci partea fixă
            # ia suma liniilor: articolul e echilibrat prin construcție, iar ce rămâne
            # de verificat e totalul afirmat în proză, nu egalitatea cu el însuși.
            if suma is None:
                linii_parte = art["debit"] if d == "%" else art["credit"]
                total = sum(x for _, x in linii_parte if x is not None)
                cealalta = art["credit"] if d == "%" else art["debit"]
                cealalta[:] = [(cont, total) for cont, _ in cealalta]
                art["total"] = total
                art["dedus"] = True
            i = j
        else:
            art["debit"].append((d, suma))
            art["credit"].append((c, suma))
            i += 1
        out.append(art)
    return out


def blocuri(cale):
    """[(rând, [linii], context_de_dinainte, text_de_după)] — blocurile ``` ale unui .md."""
    with open(cale, encoding="utf-8") as f:
        linii = f.read().split("\n")
    out, inb, buf, start = [], False, [], 0
    for i, l in enumerate(linii):
        if l.startswith("```"):
            if inb:
                inainte = "\n".join(linii[max(0, start - 5):start - 1])
                dupa = "\n".join(linii[i + 1:i + 4])
                out.append((start + 1, buf, inainte, dupa))
                buf = []
            else:
                start = i + 1
            inb = not inb
        elif inb:
            buf.append(l)
    return out


def citeste(cale):
    """[(rând, articole, context, după, linii)] — doar blocurile care au articole."""
    out = []
    for rand, linii, inainte, dupa in blocuri(cale):
        arte = articole(linii, rand)
        if arte:
            out.append(dict(rand=rand, articole=arte, inainte=inainte,
                            dupa=dupa, linii=linii))
    return out
