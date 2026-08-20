"""Randează documentele revizuite ca `.html`. Pereche cu `build/docx_out.py`.

Diferența față de o conversie Markdown obișnuită: **înregistrările contabile nu sunt
text preformatat, sunt structură.** Blocurile de monografie trec prin
`build/monografii.py` — același parser pe care îl folosește poarta 18 — și ies ca
registru: debit, credit, sumă aliniată la dreapta, notă. Storno în roșu, pentru că e
citit ca storno, nu ca sumă negativă oarecare.

Asta e și motivul pentru care randarea nu-și face propria citire. Un `.html` convertit
separat de `.md` devine al doilea adevăr — iar exemplul e chiar fișierul care a pornit
discuția: acolo, escape-urile `70\\*` rupseseră perechea de bold, iar cele treisprezece
capcane din §12 ajunseseră treisprezece liste `<ol>` de câte un element, numerotate
„1. 1. 1.”. Ambele defecte vin din aceeași cauză — o a doua trecere peste text, făcută
altfel decât prima.

Paleta e cea din `surse/training-5-2026-08-19/ghid-contabilitate.html`, cu tokeni de
temă definiți complet pe `:root` gol și redefiniți în ambele gărzi de dark, ca pagina să
fie corectă și la alegere explicită, și la „system”.
"""
import html as _html
import os
import re

from build import monografii as M

RADACINA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RE_TABEL = re.compile(r"^\s*\|.*\|\s*$")
RE_SEP_TABEL = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
RE_TITLU = re.compile(r"^(#{1,4})\s+(.*)$")
RE_LISTA = re.compile(r"^\s*[-*]\s+(.*)$")
RE_NUMEROTAT = re.compile(r"^\s*(\d+)\.\s+(.*)$")
RE_CITAT = re.compile(r"^>\s?(.*)$")

#: Escape-urile Markdown se scot ÎNAINTE de formatarea inline și se pun la loc după.
#: Altfel `70\*` lasă backslash-ul în text și, mai rău, `*`-ul lui intră în perechea de
#: bold a frazei următoare — exact defectul din fișierul convertit de mână.
RE_ESCAPE = re.compile(r"\\([\\`*_{}\[\]()#+\-.!])")
SEMN = "\x00%d\x00"


def _inline(text):
    """`**bold**`, `*italic*`, `` `cod` `` → HTML, cu escape-urile păstrate literal."""
    pastrate = []

    def prinde(m):
        pastrate.append(m.group(1))
        return SEMN % (len(pastrate) - 1)

    text = RE_ESCAPE.sub(prinde, text)
    text = _html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", text)
    for i, ch in enumerate(pastrate):
        text = text.replace(SEMN % i, _html.escape(ch))
    return text


def _ancora(text, folosite):
    """Ancoră stabilă și unică dintr-un titlu — ca Excel-ul să poată trimite aici."""
    baza = re.sub(r"[^a-z0-9]+", "-",
                  _html.unescape(re.sub(r"<[^>]+>", "", text)).lower()).strip("-")[:48]
    baza = baza or "sectiune"
    n, a = 2, baza
    while a in folosite:
        a = f"{baza}-{n}"
        n += 1
    folosite.add(a)
    return a


def _ro(x):
    """1234.5 → „1.234,50”; 20000 → „20.000”. Aceeași convenție ca în workbook."""
    if x is None:
        return ""
    neg = x < 0
    x = abs(x)
    intreg = int(x)
    zecimi = round((x - intreg) * 100)
    if zecimi == 100:
        intreg, zecimi = intreg + 1, 0
    s = f"{intreg:,}".replace(",", ".")
    if zecimi:
        s = f"{s},{zecimi:02d}"
    return ("−" + s) if neg else s


def _registru(linii, idp):
    """Un bloc de monografie → registru. Dacă n-are articole, rămâne `<pre>`."""
    arte = M.articole(linii)
    if not arte:
        return ('<pre class="cod">' + _html.escape("\n".join(linii)) + "</pre>")

    randuri = []
    for k, a in enumerate(arte):
        perechi = []
        if a["compus"]:
            # Capul compus e rând propriu, cu TOTALUL lângă contul fix. Componentele
            # vin sub el, fiecare cu suma ei și cu partea opusă goală. Pusă suma
            # componentei pe rândul contului fix, randarea ar afirma că 401 a fost
            # creditat cu 100.000, când de fapt a fost cu 121.000.
            pe_debit = a["parte_multipla"] == "debit"
            multe = a["debit"] if pe_debit else a["credit"]
            fix = (a["credit"] if pe_debit else a["debit"])[0][0]
            perechi.append(("%" if pe_debit else fix,
                            fix if pe_debit else "%", a["total"], a["nota"]))
            for cont, suma in multe:
                perechi.append((cont, "", suma, "") if pe_debit else ("", cont, suma, ""))
        else:
            perechi.append((a["debit"][0][0], a["credit"][0][0], a["total"], a["nota"]))

        for j, (d, c, suma, nota) in enumerate(perechi):
            aid = f"{idp}-a{k + 1}" + (f"-{j + 1}" if len(perechi) > 1 else "")
            neg = " neg" if (suma is not None and suma < 0) else ""
            randuri.append(
                f'<div class="led-row" id="{aid}">'
                f'<span class="led-d">{_html.escape(d)}</span>'
                f'<span class="led-eq">{"=" if d and c else ""}</span>'
                f'<span class="led-c">{_html.escape(c)}</span>'
                f'<span class="led-amt{neg}">{_ro(suma)}</span>'
                f'<span class="led-note">{_inline(nota or "")}</span></div>')
    return '<div class="ledger">' + "".join(randuri) + "</div>"


def _tabel(randuri):
    cap, corp = randuri[0], randuri[1:]
    def celule(r):
        return [c.strip() for c in r.strip().strip("|").split("|")]
    out = ['<div class="tw"><table><thead><tr>']
    out += [f"<th>{_inline(c)}</th>" for c in celule(cap)]
    out.append("</tr></thead><tbody>")
    for r in corp:
        out.append("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in celule(r)) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def converteste(md_text, cale_iesire, titlu=None, subtitlu=None):
    """Scrie documentul ca pagină de sine stătătoare."""
    linii = md_text.split("\n")
    corp, cuprins, folosite = [], [], set()
    i, nr_bloc = 0, 0
    lista, numerotata = [], []

    def inchide_liste():
        """Elementele consecutive fac O listă. Câte una de element ar renumerota „1. 1.”."""
        if lista:
            corp.append("<ul>" + "".join(f"<li>{x}</li>" for x in lista) + "</ul>")
            lista.clear()
        if numerotata:
            corp.append("<ol>" + "".join(f"<li>{x}</li>" for x in numerotata) + "</ol>")
            numerotata.clear()

    while i < len(linii):
        l = linii[i]

        if l.startswith("```"):
            inchide_liste()
            j = i + 1
            buf = []
            while j < len(linii) and not linii[j].startswith("```"):
                buf.append(linii[j])
                j += 1
            nr_bloc += 1
            corp.append(_registru(buf, f"m{nr_bloc}"))
            i = j + 1
            continue

        m = RE_TITLU.match(l)
        if m:
            inchide_liste()
            niv, text = len(m.group(1)), _inline(m.group(2))
            if niv == 1:
                i += 1
                continue                      # titlul paginii stă în antet
            a = _ancora(m.group(2), folosite)
            if niv == 2:
                cuprins.append((a, re.sub(r"<[^>]+>", "", text)))
            corp.append(f'<h{niv} id="{a}">{text}</h{niv}>')
            i += 1
            continue

        if RE_TABEL.match(l):
            inchide_liste()
            buf = []
            while i < len(linii) and RE_TABEL.match(linii[i]):
                if not RE_SEP_TABEL.match(linii[i]):
                    buf.append(linii[i])
                i += 1
            corp.append(_tabel(buf))
            continue

        m = RE_CITAT.match(l)
        if m:
            inchide_liste()
            buf = []
            while i < len(linii) and RE_CITAT.match(linii[i]):
                buf.append(RE_CITAT.match(linii[i]).group(1))
                i += 1
            corp.append(f'<div class="note"><p>{_inline(" ".join(buf))}</p></div>')
            continue

        m = RE_LISTA.match(l)
        if m:
            if numerotata:
                inchide_liste()
            lista.append(_inline(m.group(1)))
            i += 1
            continue

        m = RE_NUMEROTAT.match(l)
        if m:
            if lista:
                inchide_liste()
            numerotata.append(_inline(m.group(2)))
            i += 1
            continue

        if l.strip() in ("---", "***", "___"):
            inchide_liste()
            corp.append("<hr>")
            i += 1
            continue

        if l.strip():
            inchide_liste()
            corp.append(f"<p>{_inline(l.strip())}</p>")
        i += 1
    inchide_liste()

    nav = "".join(f'<li><a href="#{a}"><span class="tnum">{n}</span>'
                  f'<span>{t}</span></a></li>'
                  for n, (a, t) in enumerate(cuprins, 1))

    pagina = SABLON.format(
        titlu=_html.escape(titlu or ""), subtitlu=_html.escape(subtitlu or ""),
        css=CSS, nav=nav, corp="\n".join(corp))
    with open(cale_iesire, "w", encoding="utf-8") as f:
        f.write(pagina)
    return cale_iesire


CSS = """
:root{
  --paper:#F8F9F7; --surface:#FFFFFF; --sunk:#F1F4F1;
  --ink:#1A2421; --ink-2:#3D4A45; --muted:#6B7671;
  --accent:#1B5E44; --accent-soft:#E6EFEA; --accent-line:#B9D2C6;
  --storno:#A6342B;
  --rule:#DDE2DE; --rule-soft:#EAEEEB;
  --shadow:0 1px 2px rgba(26,36,33,.05), 0 8px 24px -12px rgba(26,36,33,.14);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --paper:#121715; --surface:#1A211E; --sunk:#161D1A;
    --ink:#E4E9E6; --ink-2:#BAC5C0; --muted:#8C9A94;
    --accent:#5FBF92; --accent-soft:#172C23; --accent-line:#2E5544;
    --storno:#E08278;
    --rule:#2A3430; --rule-soft:#222B27;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 24px -12px rgba(0,0,0,.6);
  }
}
:root[data-theme="dark"]{
  --paper:#121715; --surface:#1A211E; --sunk:#161D1A;
  --ink:#E4E9E6; --ink-2:#BAC5C0; --muted:#8C9A94;
  --accent:#5FBF92; --accent-soft:#172C23; --accent-line:#2E5544;
  --storno:#E08278;
  --rule:#2A3430; --rule-soft:#222B27;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 24px -12px rgba(0,0,0,.6);
}
*{box-sizing:border-box}
body{margin:0; background:var(--paper); color:var(--ink);
  font-family:"IBM Plex Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  font-size:16px; line-height:1.65; -webkit-font-smoothing:antialiased}
.masthead{border-bottom:1px solid var(--rule); background:var(--surface); padding:56px 28px 40px}
.mast-in{max-width:1180px; margin:0 auto; display:flex; flex-direction:column; gap:16px}
.eyebrow{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:.72rem;
  letter-spacing:.16em; text-transform:uppercase; color:var(--accent); margin:0}
h1{font-family:Spectral,Georgia,"Times New Roman",serif; font-weight:600;
  font-size:clamp(2rem,4.6vw,3.15rem); line-height:1.12; letter-spacing:-.015em;
  margin:0; text-wrap:balance; max-width:22ch}
.lede{color:var(--muted); font-size:1.02rem; margin:0; max-width:66ch}
.wrap{max-width:1180px; margin:0 auto; padding:0 28px; display:grid;
  grid-template-columns:232px minmax(0,1fr); gap:56px; align-items:start}
nav.rail{position:sticky; top:24px; padding:36px 0 40px; max-height:100vh; overflow-y:auto}
.rail-h{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:.66rem;
  letter-spacing:.16em; text-transform:uppercase; color:var(--muted);
  margin:0 0 14px; padding-bottom:10px; border-bottom:1px solid var(--rule)}
.rail ol{list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:1px}
.rail a{display:grid; grid-template-columns:24px 1fr; gap:8px; align-items:baseline;
  text-decoration:none; color:var(--ink-2); padding:6px 8px; border-radius:5px;
  font-size:.845rem; line-height:1.35; transition:background .12s,color .12s}
.rail a:hover{background:var(--sunk); color:var(--accent)}
.rail a:focus-visible{outline:2px solid var(--accent); outline-offset:1px}
.tnum{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:.72rem;
  color:var(--muted); font-variant-numeric:tabular-nums}
main{padding:36px 0 96px; min-width:0; max-width:74ch}
h2{font-family:Spectral,Georgia,serif; font-weight:600; font-size:1.62rem; line-height:1.22;
  letter-spacing:-.01em; margin:44px 0 18px; text-wrap:balance;
  padding-top:20px; border-top:1px solid var(--rule-soft); scroll-margin-top:20px}
h3{font-family:Spectral,Georgia,serif; font-weight:600; font-size:1.14rem;
  margin:30px 0 10px; scroll-margin-top:20px}
h4{font-size:1rem; margin:22px 0 8px; scroll-margin-top:20px}
p{margin:0 0 14px; max-width:72ch}
ul,ol{margin:0 0 16px; padding-left:1.2rem; max-width:72ch}
li{margin-bottom:7px}
li::marker{color:var(--muted)}
code{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:.875em;
  background:var(--sunk); border:1px solid var(--rule-soft); border-radius:4px;
  padding:1px 5px; color:var(--ink)}
hr{border:0; border-top:1px solid var(--rule); margin:32px 0}
pre.cod{background:var(--sunk); border:1px solid var(--rule); border-radius:7px;
  padding:14px 16px; overflow-x:auto; font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:.855rem; color:var(--ink-2)}
.ledger{margin:0 0 20px; border:1px solid var(--rule); border-left:3px solid var(--accent);
  border-radius:0 7px 7px 0; background:var(--surface); overflow-x:auto; box-shadow:var(--shadow)}
.led-row{display:grid; grid-template-columns:6.5em 1.2em 6.5em 8.5em 1fr; gap:10px;
  align-items:baseline; padding:8px 16px; font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:.855rem; white-space:nowrap; scroll-margin-top:20px}
.led-row+.led-row{border-top:1px solid var(--rule-soft)}
.led-row:target{background:var(--accent-soft)}
.led-d,.led-c{color:var(--ink); font-weight:500}
.led-eq{color:var(--muted)}
.led-amt{text-align:right; font-variant-numeric:tabular-nums; color:var(--accent); font-weight:500}
.led-amt.neg{color:var(--storno)}
.led-note{color:var(--muted); font-size:.9em; white-space:normal;
  font-family:"IBM Plex Sans",sans-serif}
.note{border-left:3px solid var(--accent-line); background:var(--sunk);
  padding:13px 18px; border-radius:0 6px 6px 0; margin:0 0 20px; max-width:72ch}
.note p{margin:0; color:var(--ink-2); font-size:.94rem}
.tw{overflow-x:auto; margin:0 0 22px; border:1px solid var(--rule); border-radius:7px;
  background:var(--surface)}
table{border-collapse:collapse; width:100%; font-size:.9rem}
thead th{text-align:left; font-family:"IBM Plex Mono",ui-monospace,monospace; font-weight:500;
  font-size:.7rem; letter-spacing:.09em; text-transform:uppercase; color:var(--muted);
  padding:11px 14px; border-bottom:1px solid var(--rule); background:var(--sunk)}
tbody td{padding:10px 14px; border-bottom:1px solid var(--rule-soft);
  vertical-align:top; color:var(--ink-2)}
tbody tr:nth-child(even){background:var(--accent-soft)}
tbody tr:last-child td{border-bottom:none}
tbody td code{background:transparent; border:none; padding:0}
@media (max-width:900px){
  .wrap{grid-template-columns:1fr; gap:0; padding:0 22px}
  nav.rail{position:static; max-height:none; padding:28px 0 8px; border-bottom:1px solid var(--rule)}
  .rail ol{display:grid; grid-template-columns:repeat(auto-fill,minmax(190px,1fr)); gap:2px}
  main{padding-top:26px}
  .masthead{padding:40px 22px 30px}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important; animation:none!important}}
"""

SABLON = """<!doctype html>
<html lang="ro"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titlu}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:wght@500;600;700\
&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>{css}</style></head><body>
<header class="masthead"><div class="mast-in">
<p class="eyebrow">Notițe de curs · contabilitate</p>
<h1>{titlu}</h1>
<p class="lede">{subtitlu}</p>
</div></header>
<div class="wrap">
<nav class="rail" aria-label="Cuprins"><p class="rail-h">Cuprins</p><ol>{nav}</ol></nav>
<main>
{corp}
</main></div></body></html>
"""
