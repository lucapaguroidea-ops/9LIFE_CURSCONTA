"""Reface blocul de cifre din `README.md`, între marcaje.

Proza rămâne scrisă de mână — acolo stă judecata, și niciun generator n-o poate scrie.
Ce se generează sunt **numerele**, pentru că numerele scrise de mână rămân în urmă. Au
și rămas: README-ul afirma „23 corelații de control” când erau 29, „58 de conturi
Tier A” când 87 sunt clasificate și 39 detaliate, și trimitea la `date/fluxuri.py`,
fișier dispărut de la reorganizarea pe clase.

E același tipar ca la documentul de parcurs, unde secțiunile `[generat]` se recitesc din
cod la fiecare build. Diferența: README-ul stă în rădăcina depozitului, nu în `dist/`,
deci poate fi comis fără să treacă prin `make`. De-asta poarta 22 verifică nu doar că
blocul e corect, ci că e **exact** cel pe care generatorul l-ar produce.

Rulare:  python build/readme.py   (după `make build documente`)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from build import cifre  # noqa: E402

RADACINA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CALE = os.path.join(RADACINA, "README.md")

START = "<!-- generat: cifre — nu edita între marcaje, se suprascrie la `make tot` -->"
STOP = "<!-- /generat -->"

NUME_CLASA = {
    "1": "capitaluri, provizioane, împrumuturi, închiderea exercițiului, leasing",
    "2": "imobilizări: intrare pe grupe → în curs → regie proprie → subvenții → ieșiri "
         "→ control analitic ↔ sintetic",
    "3": "stocuri și producție: aprovizionare, obiecte de inventar, producție, mărfuri, "
         "import",
    "4": "terți, TVA, salarii: TVA la încasare, taxare inversă, închidere lunară, "
         "408/418, salarii, medicale, popriri, impozit micro",
    "5": "trezorerie",
    "8": "conturi în afara bilanțului",
}


def bloc(n=None):
    """Blocul, exact așa cum trebuie să apară între marcaje."""
    n = n or cifre.citeste()
    L = [START, "",
         f"**{n['fluxuri']} fluxuri** cu monografie pas cu pas, ordonate după planul de "
         f"conturi. ID-ul codifică clasa contului principal, deci un flux adăugat peste "
         f"un an primește următorul număr liber din clasa lui și stă fizic la locul lui.",
         "",
         "| Bloc | Conținut | Fluxuri |", "|---|---|---|"]
    for c, cate in n["pe_clasa"].items():
        L.append(f"| `F-{c}xx` | {NUME_CLASA.get(c, '—')} | {cate} |")
    L += ["",
          f"**{n['module']} module declarative** în {n['foi_module']} foi, fiecare cu "
          f"`Declarații → Reguli → Jurnale → NotaExport` și celule `Check`.",
          "",
          "| Ce | Cât |", "|---|---|",
          f"| Conturi în planul clasificat pe rol | {n['conturi']} |",
          f"| Conturi clasificate Tier A | {n['tier_a']} |",
          f"| Dintre ele, cu rând detaliat de analitice | {n['detaliate']} |",
          f"| Corelații de control | {n['corelatii']} |",
          f"| Rânduri de cadență în „Închideri periodice” | {n['cadente']} |",
          f"| Foi în workbook-ul de referință | {n['foi']} |",
          f"| Documente de studiu | {n['documente']} |",
          f"| Întrebări: deschise / verificate / decizii de cabinet | "
          f"{n['deschise']} / {n['verificate']} / {n['decizii']} |",
          f"| Porți de calitate | {n['porti']} |",
          "",
          "*Cifrele de mai sus se citesc din workbook-urile construite la fiecare "
          "`make tot`. Dacă nu corespund, blocul e vechi — nu fișierele.*",
          "", STOP]
    return "\n".join(L)


def scrie():
    with open(CALE, encoding="utf-8") as f:
        text = f.read()
    if START not in text or STOP not in text:
        raise SystemExit("README.md: lipsesc marcajele blocului generat "
                         f"({START!r} … {STOP!r})")
    i, j = text.index(START), text.index(STOP) + len(STOP)
    nou = text[:i] + bloc() + text[j:]
    if nou != text:
        with open(CALE, "w", encoding="utf-8") as f:
            f.write(nou)
    return nou != text


def main():
    schimbat = scrie()
    print(f"README.md: blocul de cifre {'refăcut' if schimbat else 'era la zi'}")


if __name__ == "__main__":
    main()
