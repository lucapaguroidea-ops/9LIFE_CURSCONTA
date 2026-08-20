"""Armonizează documentele revizuite și le scrie în `dist/`.

Regula de bază: **nimic nu se pierde.** Se schimbă forma legendei, denumirea și poziția
anexelor, se generează Anexa E acolo unde lipsește. Fiecare linie din document trebuie
să se regăsească în varianta armonizată — verificat, nu promis.

Documentele sunt titrate pe SUBIECT, nu pe ziua de training: un document care crește cu
material din mai multe zile n-ar mai putea purta cinstit o dată. Zilele-sursă sunt
listate în antet. E aceeași mișcare făcută în Excel — ordonare pe logică contabilă, nu
pe tranșe.

Corpul primește adâncirile din sursa împărțită, contopite ÎN secțiunea care tratează
același subiect, nu lipite la coadă. Ce nu are secțiune-gazdă devine secțiune nouă:
acela e un gol de subiect, nu o tranșă.

`surse/` rămâne neatins: acolo stau documentele așa cum le-ai scris.

Rulare:  python build/documente.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from build.conservare import _normalizeaza  # noqa: E402
from build.docx_out import converteste  # noqa: E402
from build.html_out import converteste as converteste_html  # noqa: E402
from build import repartizare as brep
from date import documente as D
from date import intrebari as dintr  # noqa: E402
from date import repartizare as drep  # noqa: E402

RADACINA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RE_NUMAR_TITLU = re.compile(r"^(#{2,3})\s*\d+(\.\d+)*\.?\s*")

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


# ------------------------------------------------------------------ contopirea
# O sursă poate alimenta mai multe documente (vezi `date/repartizare.py`). Blocul ei
# nu se lipește la coada documentului-destinație — asta ar fi o cusătură pe tranșe,
# exact ce s-a eliminat din Excel. Intră ÎN secțiunea care tratează același subiect,
# cu subsecțiunile renumerotate ca fii ai ei. Unde destinația n-are secțiune pe acel
# subiect, blocul devine secțiune nouă: e un gol de subiect, nu o tranșă.

def _fara_numar(titlu):
    """„### 2.1 Achiziția” → „Achiziția”. Numerotarea e poziție, nu conținut."""
    return RE_NUMAR_TITLU.sub("", titlu).strip()


def blocuri(dest):
    """Blocurile sursei împărțite care aparțin destinației `dest`.

    Un bloc e o secțiune `##` împreună cu subsecțiunile ei care merg în ACEEAȘI
    destinație. §2.6 nu vine cu §2: e repartizat la capitaluri, și pleacă acolo.
    """
    cale = os.path.join(RADACINA, drep.SURSA)
    if not os.path.exists(cale):
        return {}
    with open(cale, encoding="utf-8") as f:
        sectiuni_sursa = brep.sectiuni(f.read())

    grupe, curent = {}, None
    for titlu, linii in sectiuni_sursa:
        if titlu.startswith("## "):
            curent = titlu
            grupe[curent] = dict(intro=linii, sub=[])
        elif titlu.startswith("### ") and curent:
            grupe[curent]["sub"].append((titlu, linii))

    out = {}
    for titlu, g in grupe.items():
        al_meu = drep.UNDE.get(titlu) == dest
        sub = [(st, sl) for st, sl in g["sub"] if drep.UNDE.get(st) == dest]
        if al_meu or sub:
            out[titlu] = dict(intro=g["intro"] if al_meu else [], sub=sub)
    return out


def _randeaza(bloc, numar, primul_copil):
    """Corpul unui bloc, cu subsecțiunile renumerotate ca `numar.k`."""
    out = [l.rstrip() for l in bloc["intro"]]
    k = primul_copil
    for titlu, linii in bloc["sub"]:
        out += ["", f"### {numar}.{k} {_fara_numar(titlu)}", ""]
        out += [l.rstrip() for l in linii]
        k += 1
    return "\n".join(out).strip("\n")


def _ultimul_copil(body):
    """Al câtelea `###` are secțiunea — ca adăugirea să continue numerotarea, nu s-o reia."""
    nr = [int(m.group(1)) for m in re.finditer(r"^###\s*\d+\.(\d+)", body, flags=re.M)]
    return max(nr) if nr else 0


def _contopeste_adaugirile(cfg, sectiuni):
    """Bagă blocurile repartizate acestui document în secțiunile lor gazdă.

    Întoarce (secțiuni, textul adăugat). Textul adăugat se lipește la `original`
    pentru conservare: poarta 12 verifică documentul față de tot ce ar fi trebuit să
    conțină, nu doar față de sursa lui inițială.
    """
    adaugiri = cfg.get("adaugiri") or []
    if not adaugiri:
        return sectiuni, ""

    disponibile = blocuri(cfg["cheie"])
    sectiuni = list(sectiuni)
    indice = {t.strip(): i for i, (t, _) in enumerate(sectiuni)}
    adaugat = []
    noi = {}                                   # titlu secțiune nouă → [bloc, …]

    for a in adaugiri:
        bloc = disponibile.get(a["bloc"])
        if bloc is None:
            raise SystemExit(f"{cfg['nume']}: blocul {a['bloc']!r} nu e repartizat aici "
                             f"— verifică date/repartizare.py")
        if a.get("sectiune_noua"):
            noi.setdefault(a["sectiune_noua"], []).append(bloc)
            continue

        gazda = a["in_sectiune"]
        if gazda not in indice:
            raise SystemExit(f"{cfg['nume']}: secțiunea gazdă {gazda!r} nu există")
        i = indice[gazda]
        titlu, body = sectiuni[i]
        numar = re.match(r"^##\s*(\d+)", titlu)
        numar = numar.group(1) if numar else "0"
        text = _randeaza(bloc, numar, _ultimul_copil(body) + 1)
        sectiuni[i] = (titlu, body.rstrip() + "\n\n" + text + "\n")
        adaugat.append(text)

    # secțiunile noi merg la coada corpului, numerotate în continuare
    urmator = max([int(m.group(1)) for t, _ in sectiuni
                   for m in [re.match(r"^##\s*(\d+)", t)] if m] or [0]) + 1
    for titlu_nou, lista in noi.items():
        corp, k = [], 1
        for bloc in lista:
            text = _randeaza(bloc, urmator, k)
            k += len(bloc["sub"])
            corp.append(text)
        body = "\n\n".join(corp)
        # Înaintea anexelor: un document care are deja anexe în corp (training 4 le
        # avea denumite corect de la bun început) nu trebuie să primească secțiuni de
        # conținut după ele.
        prima_anexa = next((i for i, (t, _) in enumerate(sectiuni)
                            if t.strip().startswith("## Anexa")), len(sectiuni))
        sectiuni.insert(prima_anexa, (f"## {urmator}. {titlu_nou}", body))
        adaugat.append(body)
        urmator += 1

    return sectiuni, "\n".join(adaugat)


def _din_repartizare(cfg):
    """Documentul construit integral din secțiunile care i-au fost repartizate.

    Preambulul sursei (convenția de notare) merge în prima secțiune, nu în antet:
    antetul e rescris cu titlul și legenda canonice, deci ce s-ar pune acolo s-ar
    pierde la armonizare — iar poarta 16 chiar asta verifică.
    """
    disponibile = blocuri(cfg["cheie"])
    sectiuni, bucati = [], []
    if drep.UNDE.get(brep.PREAMBUL) == cfg["cheie"]:
        cale = os.path.join(RADACINA, drep.SURSA)
        with open(cale, encoding="utf-8") as f:
            pre = next((l for t, l in brep.sectiuni(f.read()) if t == brep.PREAMBUL), [])
        text = "\n".join(l.rstrip() for l in pre
                          if not l.startswith("# ") and l.strip() != "---").strip("\n")
        if text:
            sectiuni.append(("## Convenția de notare", text))
            bucati.append(text)
    for nr, (titlu, bloc) in enumerate(disponibile.items(), start=1):
        text = _randeaza(bloc, nr, 1)
        sectiuni.append((f"## {nr}. {_fara_numar(titlu)}", text))
        bucati.append(f"{titlu}\n{text}")
    return "\n\n".join(bucati), sectiuni


litera_d = "D"


def _anexa_d(cfg):
    """Anexa D generată din `date/intrebari.py` — întrebările care privesc documentul.

    Documentele trainingurilor 2, 3 și 4 au deja o secțiune de întrebări în textul lor;
    ele nu primesc anexa asta, ar fi a doua listă. O primește documentul construit din
    sursa împărțită, care altfel n-ar arăta nimic provizoriu — deși e.

    Derivată, nu scrisă: aceeași sursă cu foaia „Întrebări deschise” și cu
    `intrebari-formator.md`. Fiecare punct poartă ❓, ca legenda să spună adevărul.
    """
    ale_mele = [(t, q) for t, q in dintr.toate()
                if dintr.documentul(q) == cfg["cheie"]]
    out = [f"## Anexa {litera_d} — {D.ANEXE['D']}", "",
           "Ce e încă provizoriu în documentul ăsta. Lista nu e scrisă aici: vine din "
           "`date/intrebari.py`, aceeași sursă cu foaia „Întrebări deschise” a "
           "workbook-ului și cu lista trimisibilă formatorului.", ""]
    for tema, q in ale_mele:
        out += [f"**❓ {q['intrebare']}**", "",
                f"*{tema} · {q['sursa']}*", "",
                q["context"], ""]
        if q.get("presupunere"):
            out += [f"**Ce am presupus între timp:** {q['presupunere']}", ""]
    return "\n".join(out)


def _aplica_inlocuiri(cfg, sectiuni):
    """Înlocuirile declarate pe corpul documentului, fiecare cu motivul ei.

    Se folosește rar și numai unde textul original spune ceva care a devenit fals: un
    marcaj aplicat greșit, o trimitere la o secțiune care nu mai există. Textul înlocuit
    e declarat, deci poarta de conservare știe că are voie să dispară — la fel ca la
    workbook-uri.
    """
    inl = cfg.get("inlocuiri") or []
    if not inl:
        return sectiuni
    out = []
    for titlu, body in sectiuni:
        t, b = titlu, body
        for i in inl:
            t = t.replace(i["text"], i["devine"])
            b = b.replace(i["text"], i["devine"])
        out.append((t, b))
    negasite = [i["text"] for i in inl
                if not any(i["devine"] in x for _, x in out)
                and not any(i["devine"] in x for x, _ in out)]
    if negasite:
        raise SystemExit(f"{cfg['nume']}: înlocuiri fără țintă — {negasite}")
    return out


def armonizeaza(cfg):
    if cfg.get("repartizat"):
        original, sectiuni = _din_repartizare(cfg)
        antet = ""
    else:
        sursa = os.path.join(RADACINA, cfg["sursa"])
        with open(sursa, encoding="utf-8") as f:
            original = f.read()
        antet, sectiuni = _sectiuni(original)
        sectiuni, adaugat = _contopeste_adaugirile(cfg, sectiuni)
        original += "\n" + adaugat
    sectiuni = _aplica_inlocuiri(cfg, sectiuni)

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
    # potrivirea se face fără numerotare: o secțiune repartizată e renumerotată în
    # documentul-gazdă, dar rămâne aceeași secțiune.
    de_mutat = {_fara_numar(t): a for t, a in cfg["anexe"].items()}
    corp, mutate = [], {}
    for titlu, body in sectiuni:
        if _fara_numar(titlu) in de_mutat:
            mutate[de_mutat[_fara_numar(titlu)]] = body.strip("\n")
        else:
            corp += [titlu, body.rstrip() + "\n"]

    # --- anexele, în ordine canonică
    anexe = []
    for litera in sorted(set(mutate) | set(cfg["genereaza"])):
        if litera in mutate:
            anexe += ["---", "", f"## Anexa {litera} — {D.ANEXE[litera]}", "",
                      mutate[litera], ""]
        elif litera == "D":
            anexe += ["---", "", _anexa_d(cfg), ""]
        elif litera == "E":
            anexe += ["---", "", _anexa_e(original), ""]
        elif litera == "F":
            anexe += ["---", "", f"## Anexa {litera} — {D.ANEXE[litera]}", "",
                      D.ANEXA_F_TRAINING_4, ""]

    # Anexele care există deja în corp se EXTIND, nu se rescriu: corecțiile aduse de o
    # sursă nouă stau lângă cele vechi, în aceeași anexă, nu într-una paralelă.
    for litera, text in (cfg.get("extinde_anexe") or {}).items():
        cap = f"## Anexa {litera} — "
        # `corp` e o listă plată titlu, corp, titlu, corp… — corpul e imediat după titlu
        for i in range(0, len(corp) - 1, 2):
            if str(corp[i]).strip().startswith(cap):
                corp[i + 1] = corp[i + 1].rstrip() + "\n\n" + text + "\n"
                break
        else:
            raise SystemExit(f"{cfg['nume']}: nu există Anexa {litera} de extins")

    if cfg["nota"]:
        anexe += ["---", "", f"*{cfg['nota']}*", ""]

    return "\n".join(antet_nou + corp + anexe), original


def verifica_conservare(original, nou, cfg):
    """Fiecare linie din original trebuie să se regăsească în varianta armonizată."""
    declarate = {_normalizeaza(l) for l in cfg["legenda_veche"] if l.strip()}
    # Originalul trece prin aceleași înlocuiri declarate înainte de comparație. A-l
    # declara ca „text care are voie să dispară” n-ar funcționa: înlocuirea prinde un
    # FRAGMENT de linie, iar conservarea compară linii întregi.
    for i in cfg.get("inlocuiri") or []:
        original = original.replace(i["text"], i["devine"])
    # titlurile redenumite: „## 10. Listă de verificat…” devine „## Anexa D — …”
    declarate |= {_normalizeaza(t) for t in cfg["anexe"]}
    # titlul și subtitlul se reformulează
    declarate |= {_normalizeaza(l) for l in original.split("\n")
                  if l.startswith("# ") or l.startswith("### ") or l.startswith("*Versiune")}

    prezente = {_normalizeaza(l) for l in nou.split("\n") if l.strip()}
    # Un titlu renumerotat nu e un titlu pierdut: secțiunea repartizată primește
    # numerotarea documentului-gazdă. Aceeași regulă ca la poarta 16 — numerotarea e
    # poziție, iar poziția a fost liberă de la reordonarea Excel-ului încoace.
    titluri = {_normalizeaza(_fara_numar(l)) for l in nou.split("\n")
               if l.startswith("##")}
    lipsa = []
    for l in original.split("\n"):
        n = _normalizeaza(l)
        if not n or n in declarate or n in prezente:
            continue
        if l.startswith("##") and _normalizeaza(_fara_numar(l)) in titluri:
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
        converteste(nou, cale.replace(".md", ".docx"))
        converteste_html(nou, cale.replace(".md", ".html"),
                         titlu=cfg["titlu"], subtitlu=cfg["subtitlu"])
        anexe = sorted(set(cfg["anexe"].values()) | set(cfg["genereaza"]))
        print(f"scris: {cfg['iesire']} + .docx + .html  "
              f"(anexe {', '.join(anexe) or '—'}, 0 linii pierdute)")
        total += 1
    print(f"{total} documente armonizate")


if __name__ == "__main__":
    main()
