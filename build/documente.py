"""Armonizează cele trei documente revizuite și le scrie în `dist/`.

Regula de bază: **corpul nu se atinge.** Se schimbă doar forma legendei, denumirea și
poziția anexelor, plus se generează Anexa E acolo unde lipsește. Fiecare linie din
document trebuie să se regăsească în varianta armonizată — verificat, nu promis.

`surse/` rămâne neatins: acolo stau documentele așa cum le-ai scris.

Rulare:  python build/documente.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from build.conservare import _normalizeaza  # noqa: E402
from build.docx_out import converteste  # noqa: E402
from date import documente as D  # noqa: E402

RADACINA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Tiparele de citare. Sunt deliberat stricte: mai bine ratez o citare exotică decât să
# raportez ca „act normativ” un fragment de propoziție.
RE_ACTE = [
    re.compile(r"\b(?:Legea|L\.)\s*(?:nr\.\s*)?(\d+/\d{4})"),
    re.compile(r"\b(OMFP?|OMF)\s*(?:nr\.\s*)?(\d+/\d{4})"),
    re.compile(r"\b(OUG)\s*(?:nr\.\s*)?(\d+/\d{4})"),
    re.compile(r"\b(HG)\s*(?:nr\.\s*)?(\d+/\d{4})"),
    re.compile(r"\b(Ordinul)\s*(?:nr\.\s*)?(\d+/\d{4})"),
    re.compile(r"\b(Directiva)\s*(\d{4}/\d+/\w+)"),
]
RE_CODURI = re.compile(r"\bCod(?:ul)?\s+(fiscal|silvic|muncii|civil)\b", re.I)
RE_ART = re.compile(r"\bart\.\s*(\d+)(?:\s*alin\.\s*\(?(\d+)\)?)?")


def _sectiuni(text):
    """Împarte în (antet, [(titlu, corp), …]) după titlurile de nivel 2."""
    linii = text.split("\n")
    taieturi = [i for i, l in enumerate(linii) if l.startswith("## ")]
    if not taieturi:
        return text, []
    antet = "\n".join(linii[:taieturi[0]])
    sectiuni = []
    for k, i in enumerate(taieturi):
        j = taieturi[k + 1] if k + 1 < len(taieturi) else len(linii)
        sectiuni.append((linii[i].strip(), "\n".join(linii[i + 1:j])))
    return antet, sectiuni


def _legenda():
    out = [f"## {D.LEGENDA_TITLU}", "", "| Marcaj | Semnificație |", "|---|---|"]
    out += [f"| {m} | {s} |" for m, s in D.LEGENDA_TABEL]
    return "\n".join(out)


def _anexa_e(text):
    """Baza legală citată, extrasă din text. Derivare, nu invenție."""
    acte, vazute = [], set()
    for rx in RE_ACTE:
        for m in rx.finditer(text):
            eticheta = (f"{m.group(1)} {m.group(2)}" if m.lastindex and m.lastindex > 1
                        else f"Legea {m.group(1)}")
            if eticheta not in vazute:
                vazute.add(eticheta)
                acte.append(eticheta)
    coduri = []
    for m in RE_CODURI.finditer(text):
        c = "Codul " + m.group(1).lower()
        if c not in coduri:
            coduri.append(c)

    articole = sorted({(int(m.group(1)), int(m.group(2)) if m.group(2) else 0)
                       for m in RE_ART.finditer(text)})
    art_txt = ", ".join(f"art. {a}" + (f" alin. ({b})" if b else "")
                        for a, b in articole)

    out = [f"## Anexa E — {D.ANEXE['E']}", "",
           "Extrasă automat din textul documentului: sunt listate actele și articolele "
           "care apar efectiv citate mai sus. Contextul fiecărei citări e în secțiunea "
           "unde apare.", ""]
    if acte or coduri:
        out += ["**Acte normative citate**", ""]
        out += [f"- {a}" for a in acte + coduri]
        out.append("")
    if art_txt:
        out += ["**Articole citate**", "", art_txt, ""]
    return "\n".join(out)


def armonizeaza(cfg):
    sursa = os.path.join(RADACINA, cfg["sursa"])
    with open(sursa, encoding="utf-8") as f:
        original = f.read()

    antet, sectiuni = _sectiuni(original)

    # Documentul care are deja secțiunea canonică nu o primește a doua oară — ar apărea
    # de două ori. Tabelul canonic e chiar al lui, deci nu are ce să se schimbe.
    are_deja = any(t.strip() == f"## {D.LEGENDA_TITLU}" for t, _ in sectiuni)

    # --- antetul: titlu + subtitlu + legenda canonică
    antet_nou = [f"# {cfg['titlu']}", f"### {cfg['subtitlu']}", "", "---", ""]
    if not are_deja:
        antet_nou += [_legenda(), ""]
    # ce era în antet și NU e legendă veche se păstrează (note de metodă etc.)
    vechi_norm = {_normalizeaza(l) for l in cfg["legenda_veche"] if l.strip()}
    pastrate = [l for l in antet.split("\n")
                if l.strip() and not l.startswith("#") and l.strip() != "---"
                and _normalizeaza(l) not in vechi_norm]
    if pastrate:
        antet_nou += pastrate + [""]
    antet_nou += ["---", ""]

    # --- corpul, fără secțiunile care devin anexe
    de_mutat = cfg["anexe"]
    corp, mutate = [], {}
    for titlu, body in sectiuni:
        if titlu in de_mutat:
            mutate[de_mutat[titlu]] = body.strip("\n")
        else:
            corp += [titlu, body.rstrip() + "\n"]

    # --- anexele, în ordine canonică
    anexe = []
    for litera in sorted(set(mutate) | set(cfg["genereaza"])):
        if litera in mutate:
            anexe += ["---", "", f"## Anexa {litera} — {D.ANEXE[litera]}", "",
                      mutate[litera], ""]
        elif litera == "E":
            anexe += ["---", "", _anexa_e(original), ""]
        elif litera == "F":
            anexe += ["---", "", f"## Anexa {litera} — {D.ANEXE[litera]}", "",
                      D.ANEXA_F_TRAINING_4, ""]

    if cfg["nota"]:
        anexe += ["---", "", f"*{cfg['nota']}*", ""]

    return "\n".join(antet_nou + corp + anexe), original


def verifica_conservare(original, nou, cfg):
    """Fiecare linie din original trebuie să se regăsească în varianta armonizată."""
    declarate = {_normalizeaza(l) for l in cfg["legenda_veche"] if l.strip()}
    # titlurile redenumite: „## 10. Listă de verificat…” devine „## Anexa D — …”
    declarate |= {_normalizeaza(t) for t in cfg["anexe"]}
    # titlul și subtitlul se reformulează
    declarate |= {_normalizeaza(l) for l in original.split("\n")
                  if l.startswith("# ") or l.startswith("### ") or l.startswith("*Versiune")}

    prezente = {_normalizeaza(l) for l in nou.split("\n") if l.strip()}
    lipsa = []
    for l in original.split("\n"):
        n = _normalizeaza(l)
        if not n or n in declarate or n in prezente:
            continue
        if any(n in p for p in prezente):
            continue
        lipsa.append(l.strip())
    return lipsa


def main():
    total = 0
    for cfg in D.DOCUMENTE:
        nou, original = armonizeaza(cfg)
        lipsa = verifica_conservare(original, nou, cfg)
        if lipsa:
            print(f"✘ {cfg['nume']}: {len(lipsa)} linii pierdute")
            for l in lipsa[:8]:
                print("   ·", l[:110])
            raise SystemExit(1)
        cale = os.path.join(RADACINA, cfg["iesire"])
        os.makedirs(os.path.dirname(cale), exist_ok=True)
        with open(cale, "w", encoding="utf-8") as f:
            f.write(nou)
        docx = cale.replace(".md", ".docx")
        converteste(nou, docx)
        anexe = sorted(set(cfg["anexe"].values()) | set(cfg["genereaza"]))
        print(f"scris: {cfg['iesire']} + .docx  (anexe {', '.join(anexe) or '—'}, "
              f"0 linii pierdute)")
        total += 1
    print(f"{total} documente armonizate")


if __name__ == "__main__":
    main()
