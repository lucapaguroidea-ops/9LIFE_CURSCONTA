"""Generează dist/intrebari-formator.md — lista consolidată de întrebări deschise.

Cele 21 de întrebări erau împrăștiate în secțiunile „rămase deschise” ale celor trei
documente revizuite, numerotate independent, în trei formate. Aici devin un singur
document, grupat pe temă contabilă, pe care îl poți trimite ca atare.

Rulare:  python build/intrebari.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from date import intrebari as I  # noqa: E402

RADACINA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IESIRE = os.path.join(RADACINA, "dist", "intrebari-formator.md")
IESIRE_HTML = os.path.join(RADACINA, "dist", "intrebari-formator.html")

#: Întrebările care blochează cel mai mult, scoase în față. Cheia e un fragment din
#: câmpul `sursa`, ca lista să nu se rupă dacă se reformulează întrebarea.
PRIORITARE = [
    ("12.08.2026, întrebarea 6",
     "Blochează singurul flux de procedură din sistem (F-214) și corelația C-15."),
    ("07.08.2026, întrebarea 3",
     "Schimbă valoarea de intrare a mijlocului fix, deci amortizarea și impozitul pe "
     "profit pe toată durata contractului."),
    ("12.08.2026, întrebarea 3",
     "E testul central al MOD_IESIRE_MF; azi semnalează un risc fără să poată cita "
     "articolul pe care se sprijină."),
]


def _antet():
    return [
        "# Întrebări rămase deschise după trainingurile 2, 3 și 4",
        "",
        "Cele **21 de întrebări** de mai jos s-au acumulat la revizuirea notițelor din "
        "07.08.2026 (capitaluri), 12.08.2026 (imobilizări) și 14.08.2026 (stocuri și TVA).",
        "",
        "Sunt grupate pe **temă contabilă**, nu pe training, ca să nu răspundeți de trei "
        "ori la aceeași chestiune în trei contexte diferite. Fiecare întrebare vine cu "
        "contextul din notițe, ca să nu fie nevoie de recitire.",
        "",
        "Sub fiecare întrebare, **„Ce am presupus”** spune ce am ales acolo unde a trebuit "
        "să aleg ca să pot merge mai departe. Acelea sunt exact locurile unde un răspuns "
        "diferit schimbă ce e deja construit.",
        "",
    ]


def _prioritare():
    linii = ["---", "", "## Dacă aveți timp doar pentru trei", ""]
    for cheie, motiv in PRIORITARE:
        q = _gaseste(cheie)
        linii += [f"- **{q['intrebare']}**  ", f"  {motiv}", ""]
    return linii


def _gaseste(fragment):
    for _, qs in I.TEME:
        for q in qs:
            if fragment in q["sursa"]:
                return q
    raise SystemExit(f"Întrebare prioritară negăsită: {fragment!r}")


def construieste():
    linii = _antet() + _prioritare() + ["---", ""]
    nr = 0
    for tema, qs in I.TEME:
        linii += [f"## {tema}", ""]
        for q in qs:
            nr += 1
            linii += [
                f"### {nr}. {q['intrebare']}",
                "",
                f"**Context.** {q['context']}",
                "",
                f"**De ce contează.** {q['conteaza']}",
                "",
            ]
            if q["presupunere"]:
                linii += [f"**Ce am presupus.** {q['presupunere']}", ""]
            linii += [f"<sub>sursa: {q['sursa']}</sub>", "", ""]
    linii += [
        "---",
        "",
        f"*{I.TOTAL} de întrebări, {len(I.TEME)} teme. Generat din notițele revizuite; "
        "fiecare întrebare se poate urmări înapoi la training și la numărul ei original.*",
        "",
    ]
    return "\n".join(linii)


def main():
    os.makedirs(os.path.dirname(IESIRE), exist_ok=True)
    for cale, text in ((IESIRE, construieste()), (IESIRE_HTML, construieste_html())):
        with open(cale, "w", encoding="utf-8") as f:
            f.write(text)
    print(f"scris: {os.path.relpath(IESIRE, RADACINA)} + .html  "
          f"({I.TOTAL} întrebări, {len(I.TEME)} teme)")




# ---------------------------------------------------------------------- HTML
# Paleta e chiar cea a workbook-urilor: #1F4E79 e culoarea de titlu din foaia
# Legendă, iar roșul de avertisment vine din aceeași grilă. Documentul ăsta pleacă
# din același sistem, deci arată ca el — nu ca un fișier oarecare.
import html as _html  # noqa: E402
import re as _re  # noqa: E402

#: Tokenuri fără ambiguitate, marcate ca respiratie tehnica in proza. Sumele si anii
#: NU se marcheaza — „250 lei” si „2026” arata la fel ca un cont, iar o marcare gresita
#: e mai rea decat niciuna.
RE_COD = _re.compile(r"\b(F-\d{3}|MOD_[A-Z_]+|C-\d{2}|D\d{3})\b")

CSS = """
:root{
  --ground:#F6F8FA; --raised:#FFFFFF; --ink:#14202B; --muted:#5D6E7E;
  --accent:#1F4E79; --rule:#DBE3EA; --panel:#EDF2F6; --flag:#A32424;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ground:#0F1721; --raised:#141F2B; --ink:#DCE5ED; --muted:#90A2B3;
    --accent:#7FB0D8; --rule:#24313F; --panel:#17222E; --flag:#E08D8D;
  }
}
:root[data-theme="dark"]{
  --ground:#0F1721; --raised:#141F2B; --ink:#DCE5ED; --muted:#90A2B3;
  --accent:#7FB0D8; --rule:#24313F; --panel:#17222E; --flag:#E08D8D;
}
*{box-sizing:border-box}
body{
  margin:0; background:var(--ground); color:var(--ink);
  font-family:"Source Serif 4",Georgia,"Times New Roman",serif;
  font-size:17px; line-height:1.62; -webkit-font-smoothing:antialiased;
}
.wrap{max-width:46rem; margin:0 auto; padding:4rem 1.5rem 6rem; display:flex;
  flex-direction:column; gap:3rem}
h1,h2,h3,.label,.eyebrow,.num{font-family:Archivo,"Helvetica Neue",Arial,sans-serif}
h1{font-size:2.1rem; line-height:1.15; font-weight:700; margin:0; text-wrap:balance;
  letter-spacing:-.015em}
.lede{margin:0; color:var(--muted); font-size:1.05rem}
.lede+.lede{margin-top:.9rem}
code,.mono{font-family:"JetBrains Mono",ui-monospace,Menlo,Consolas,monospace;
  font-size:.86em; background:var(--panel); padding:.1em .34em; border-radius:3px;
  border:1px solid var(--rule)}

/* --- cele trei prioritare --- */
.prio{border:1px solid var(--rule); border-left:3px solid var(--flag);
  background:var(--raised); padding:1.6rem 1.7rem; display:flex;
  flex-direction:column; gap:1.1rem}
.prio h2{margin:0; font-size:.78rem; text-transform:uppercase; letter-spacing:.09em;
  color:var(--flag); font-weight:700}
.prio ol{margin:0; padding-left:1.2rem; display:flex; flex-direction:column; gap:.9rem}
.prio li::marker{font-family:"JetBrains Mono",monospace; color:var(--muted);
  font-size:.85rem}
.prio p{margin:0}
.prio .why{color:var(--muted); font-size:.94rem; margin-top:.25rem}

/* --- cuprins --- */
.toc{border-top:1px solid var(--rule); border-bottom:1px solid var(--rule);
  padding:1.4rem 0}
.toc h2{margin:0 0 .9rem; font-size:.78rem; text-transform:uppercase;
  letter-spacing:.09em; color:var(--muted); font-weight:700}
.toc ol{margin:0; padding:0; list-style:none; display:grid; gap:.35rem .5rem;
  grid-template-columns:1fr}
@media(min-width:38rem){.toc ol{grid-template-columns:1fr 1fr}}
.toc a{color:var(--ink); text-decoration:none; display:flex; justify-content:space-between;
  gap:.75rem; border-bottom:1px solid transparent; padding:.1rem 0; font-size:.96rem}
.toc a:hover,.toc a:focus-visible{color:var(--accent); border-bottom-color:var(--accent)}
.toc .n{font-family:"JetBrains Mono",monospace; font-size:.8rem; color:var(--muted);
  font-variant-numeric:tabular-nums}

/* --- teme și întrebări --- */
.tema{display:flex; flex-direction:column; gap:2.2rem}
.tema>h2{margin:0; font-size:1.02rem; font-weight:700; letter-spacing:.02em;
  padding-bottom:.5rem; border-bottom:2px solid var(--accent); color:var(--accent);
  text-wrap:balance}
.q{display:flex; flex-direction:column; gap:.85rem}
.q>h3{margin:0; font-size:1.16rem; line-height:1.32; font-weight:600;
  text-wrap:balance; letter-spacing:-.005em}
.num{font-family:"JetBrains Mono",monospace; font-size:.78rem; color:var(--muted);
  letter-spacing:.06em; font-variant-numeric:tabular-nums}
.field{display:flex; flex-direction:column; gap:.28rem}
.label{font-size:.7rem; text-transform:uppercase; letter-spacing:.1em;
  color:var(--muted); font-weight:700}
.field p{margin:0}
.presup{background:var(--panel); border-left:2px solid var(--accent);
  padding:.85rem 1rem; border-radius:0 3px 3px 0}
.presup .label{color:var(--accent)}
.sursa{font-size:.78rem; color:var(--muted); font-family:"JetBrains Mono",monospace}
footer{border-top:1px solid var(--rule); padding-top:1.5rem; color:var(--muted);
  font-size:.9rem}
a{color:var(--accent)}
:focus-visible{outline:2px solid var(--accent); outline-offset:3px}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
"""


def _esc(t):
    """Escapare + marcarea tokenurilor tehnice."""
    return RE_COD.sub(r"<code>\1</code>", _html.escape(str(t)))


def _slug(t):
    s = _re.sub(r"[^a-z0-9]+", "-", t.lower().replace("ă", "a").replace("â", "a")
                .replace("î", "i").replace("ș", "s").replace("ț", "t"))
    return s.strip("-")


def construieste_html():
    p = ['<title>Registrul întrebărilor deschise</title>',
         '<link rel="preconnect" href="https://fonts.googleapis.com">',
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Archivo:wght@400;600;700&family=JetBrains+Mono:wght@400;500&'
         'family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400'
         '&display=swap">',
         f"<style>{CSS}</style>", '<div class="wrap">']

    p += ['<header>',
          '<h1>Întrebări rămase deschise după trainingurile 2, 3 și 4</h1>',
          f'<p class="lede">Cele <strong>{I.TOTAL} de întrebări</strong> de mai jos s-au '
          'acumulat la revizuirea notițelor din 07.08.2026 (capitaluri), 12.08.2026 '
          '(imobilizări) și 14.08.2026 (stocuri și TVA).</p>',
          '<p class="lede">Sunt grupate pe <strong>temă contabilă</strong>, nu pe training, '
          'ca să nu răspundeți de trei ori la aceeași chestiune. Fiecare întrebare vine cu '
          'contextul din notițe, ca să nu fie nevoie de recitire.</p>',
          '<p class="lede">Sub fiecare întrebare, <strong>„Ce am presupus”</strong> spune ce '
          'am ales acolo unde a trebuit să aleg ca să pot merge mai departe. Acelea sunt '
          'exact locurile unde un răspuns diferit schimbă ce e deja construit.</p>',
          '</header>']

    p.append('<section class="prio"><h2>Dacă aveți timp doar pentru trei</h2><ol>')
    for cheie, motiv in PRIORITARE:
        q = _gaseste(cheie)
        p.append(f'<li><p>{_esc(q["intrebare"])}</p>'
                 f'<p class="why">{_esc(motiv)}</p></li>')
    p.append('</ol></section>')

    p.append('<nav class="toc"><h2>Temele</h2><ol>')
    for tema, qs in I.TEME:
        p.append(f'<li><a href="#{_slug(tema)}"><span>{_html.escape(tema)}</span>'
                 f'<span class="n">{len(qs)}</span></a></li>')
    p.append('</ol></nav>')

    nr = 0
    for tema, qs in I.TEME:
        p.append(f'<section class="tema" id="{_slug(tema)}">'
                 f'<h2>{_html.escape(tema)}</h2>')
        for q in qs:
            nr += 1
            p.append('<article class="q">')
            p.append(f'<div class="num">Întrebarea {nr:02d} / {I.TOTAL}</div>')
            p.append(f'<h3>{_esc(q["intrebare"])}</h3>')
            p.append(f'<div class="field"><div class="label">Context</div>'
                     f'<p>{_esc(q["context"])}</p></div>')
            p.append(f'<div class="field"><div class="label">De ce contează</div>'
                     f'<p>{_esc(q["conteaza"])}</p></div>')
            if q["presupunere"]:
                p.append(f'<div class="field presup"><div class="label">Ce am presupus</div>'
                         f'<p>{_esc(q["presupunere"])}</p></div>')
            p.append(f'<div class="sursa">{_html.escape(q["sursa"])}</div>')
            p.append('</article>')
        p.append('</section>')

    p.append(f'<footer>{I.TOTAL} de întrebări, {len(I.TEME)} teme. Generat din notițele '
             'revizuite; fiecare întrebare se poate urmări înapoi la training și la '
             'numărul ei original.</footer>')
    p.append('</div>')
    return "\n".join(p)


if __name__ == "__main__":
    main()
