"""Reordonarea foilor tabelare pe simbol de cont + curățarea Legendei.

`Analitice (Tier A)` și `Matrice acoperire` erau ordonate după momentul adăugirii:
întâi conturile de clasa 3 și TVA (training 4), apoi, la coadă, cele de clasa 1 și 2
(trainingurile 2 și 3). Aici se reordonează pe simbol de cont, adică în aceeași ordine
ca `Plan de conturi` — și se contopesc rândurile duplicate apărute din adăugire.

Contopirea nu pierde text: dacă două rânduri au același simbol și celule diferite pe
aceeași coloană, ambele conținuturi rămân, unite. Poarta de conservare verifică asta.
"""
import re

from build import randuri as R
from build import stil

RE_DIGITE = re.compile(r"\d+")


def cheie_cont(simbol):
    """Cheie de sortare care pune conturile în ordinea planului.

    `32x` → 3200, `371` → 3710, `4428` → 4428, `121/129` → 1210. Primul grup de cifre
    decide; se completează la 4 caractere ca sinteticele de 3 cifre să stea înaintea
    analiticelor de 4 din aceeași grupă.
    """
    m = RE_DIGITE.search(str(simbol or ""))
    if not m:
        return (9999, str(simbol or ""))
    d = m.group(0)[:4]
    return (int(d.ljust(4, "0")), str(simbol))


def _norm(s):
    return re.sub(r"\s+", "", str(s or "")).strip().lower()


def _contopeste_randuri(a, b):
    """Două rânduri cu același simbol → unul singur, fără să se piardă text."""
    va, vb = a.valori(), b.valori()
    out = a
    for col in sorted(set(va) | set(vb)):
        x = str(va.get(col, "") or "").strip()
        y = str(vb.get(col, "") or "").strip()
        if not y or y == x or y in x:
            continue
        out = out.cu_valoare(col, y if (not x or x == "—") else f"{x} | {y}")
    return out


def reordoneaza_tabel(wb, nume, *, col_simbol=1, latime=7, titlu=None, nota=None):
    """Rescrie o foaie tabelară: antet păstrat, rânduri de date sortate și contopite."""
    ws = wb[nume]
    rows = R.citeste(ws)

    antet, date = [], []
    cap_gasit = False
    for r in rows:
        t = r.text(col_simbol).strip()
        v = r.valori()
        e_data = bool(t) and bool(RE_DIGITE.search(t)) and len(t) < 22 \
            and any(str(v.get(c, "") or "").strip() for c in v if c != col_simbol)
        if e_data and cap_gasit:
            date.append(r)
        else:
            if r.gol():
                continue
            if not cap_gasit and any(str(x or "").strip().lower() in ("simbol", "cont", "id")
                                     for x in v.values()):
                cap_gasit = True
            # titlurile de secțiune „TRANȘA 4 …” dispar: ordinea nu mai e pe tranșe
            if "tranșa" in t.lower() or "tranşa" in t.lower():
                continue
            antet.append(r)

    unic = {}
    for r in date:
        k = _norm(r.text(col_simbol))
        unic[k] = _contopeste_randuri(unic[k], r) if k in unic else r
    ordonate = sorted(unic.values(), key=lambda r: cheie_cont(r.text(col_simbol)))

    out = list(antet)
    if titlu:
        out.insert(0, R.Rand([(1, titlu, None)], span=(1, latime),
                             stil_nou=dict(font=stil.F_TITLU_BLOC)))
    if nota:
        out.append(R.Rand([(1, nota, None)], span=(1, latime),
                          stil_nou=dict(font=stil.F_NOTA, align=stil.A_WRAP_TOP)))
    out.extend(ordonate)
    R.inlocuieste_foaia(wb, nume, out)
    return len(date) - len(ordonate)          # câte duplicate s-au contopit


# --------------------------------------------------------------------- Legendă
MUTA_DACA = (
    "PROGRES IMPLEMENTARE", "ETAPA 0:", "ETAPA 1:", "ETAPA 2:", "ETAPA 3",
    "Livrat 14.08.2026", "ETAPA 4 —",
)
HARTA_CLASE = [
    ("6. HARTA FLUXURILOR — pe clase de conturi", stil.F_CAP_TABEL),
    ("Ordinea fluxurilor urmează planul de conturi, nu ordinea în care au fost adăugate. "
     "Un flux nou primește următorul număr liber din clasa lui și stă fizic la locul lui. "
     "Echivalența cu numerotarea veche e în foaia Istoric.", stil.F_NOTA),
    ("F-1xx — capitaluri, provizioane, împrumuturi: capital social · rezerve din reevaluare · "
     "repartizarea rezultatului · închiderea exercițiului · corecții 1174 · provizioane · "
     "credite în valută · leasing financiar", stil.F_NORMAL),
    ("F-2xx — imobilizări: necorporale · terenuri · construcții · instalații și transport · "
     "investiții imobiliare · facturate nesosite · în curs de execuție · regie proprie · "
     "subvenții · ieșiri (vânzare, casare) · financiare · control analitic ↔ sintetic",
     stil.F_NORMAL),
    ("F-3xx — stocuri și producție: aprovizionare (internă, tranzit, intracomunitară) · "
     "obiecte de inventar · diferențe de preț · ajustări · producție în curs · deșeuri · "
     "mărfuri en-gros și amănunt · import", stil.F_NORMAL),
    ("F-4xx — terți, TVA, decontări: TVA la încasare · taxare inversă · scutiri și export · "
     "închiderea lunară de TVA · înregistrări fără document · 408/418 · reduceri · avansuri · "
     "473 · salarii · decontări interne", stil.F_NORMAL),
    ("F-5xx — trezorerie: viramente interne · avansuri de trezorerie", stil.F_NORMAL),
    ("F-8xx — conturi în afara bilanțului: angajamente · inventarierea obiectelor de inventar",
     stil.F_NORMAL),
]


#: Foile care lipseau din tabelul „STRUCTURA FINALĂ A WORKBOOK-ULUI”. Tabelul enumera
#: șase foi dintr-un workbook care are unsprezece — se completează în loc, ca să rămână
#: o singură listă, nu două care se contrazic.
FOI_LIPSA = [
    ("Index module", "Legătura cu Module_Declarative_Fluxuri.xlsx: ce modul acoperă "
                     "ce flux, cu ce foi și când se rulează"),
    ("Arbore analitice", "Arborele de decizie pentru analitice (3 întrebări) + "
                         "contra-regula: când analiticul e o greșeală"),
    ("Corelații de control", "Formulă · unde se verifică · ce o rupe LEGITIM vs. "
                             "SUSPECT · fluxul și modulul legat"),
    ("Întrebări deschise", "Ce e încă provizoriu în workbook: întrebările la care "
                           "sistemul așteaptă răspuns. Fluxurile atinse poartă ❓"),
    ("Istoric", "Echivalența de numerotare veche → nouă, contopirile, defectele "
                "reparate, textul mutat la deduplicare"),
]


def _livrabile(nr_module):
    return [
        ("LIVRABILE CONEXE — sistemul nu se termină la acest fișier", stil.F_TITLU_BLOC),
        (f"Module_Declarative_Fluxuri.xlsx — {nr_module} module declarative "
         "(Declarații → Reguli → Jurnale → NotaExport). Niciunul nu mai e „exemplu "
         "extern”: salariile, deconturile și leasingul au devenit interne, cu cifrele "
         "verificate contra fișierelor reale de la client.", stil.F_NORMAL),
        ("intrebari-formator.md / .html — cele 21 de întrebări rămase deschise, grupate "
         "pe temă contabilă. Aceeași sursă cu foaia „Întrebări deschise” de aici.",
         stil.F_NORMAL),
        ("notite-training-2/3/4 .md și .docx — cele trei documente revizuite, "
         "armonizate: aceeași legendă de marcaje, aceleași anexe, aceeași ordine.",
         stil.F_NORMAL),
    ]


def curata_legenda(wb, *, total_fluxuri, total_corelatii, nr_module=16):
    """Scoate narativul de etape și lista pe tranșe. Întoarce rândurile mutate."""
    ws = wb["Legendă"]
    rows = R.citeste(ws)

    mutate, pastrate = [], []
    i = 0
    while i < len(rows):
        r = rows[i]
        t = r.text().strip()

        if any(t.startswith(p) for p in MUTA_DACA):
            mutate.append(r)
            i += 1
            continue

        # lista pe tranșe (titlu + 3 perechi tranșă/conținut) → harta pe clase
        if t.startswith("6. LISTA FLUXURILOR"):
            mutate.append(r)
            i += 1
            while i < len(rows) and not rows[i].text().strip().startswith("7."):
                if rows[i].text().strip():
                    mutate.append(rows[i])
                i += 1
            for text, font in HARTA_CLASE:
                pastrate.append(R.Rand([(1, text, None)], span=(1, 7),
                                       stil_nou=dict(font=font, align=stil.A_WRAP_TOP)))
            pastrate.append(R.Rand([]))
            continue

        pastrate.append(_actualizeaza_cifre(r, total_fluxuri, total_corelatii))
        i += 1

    # completează tabelul de structură cu foile care lipseau din el
    tinta = next((i for i, r in enumerate(pastrate)
                  if r.text().strip().startswith("6. HARTA FLUXURILOR")), None)
    if tinta is not None:
        randuri = [R.Rand([(1, nume, None), (2, ce, None)],
                          stil_nou=dict(font=stil.F_NORMAL, align=stil.A_WRAP_TOP))
                   for nume, ce in FOI_LIPSA]
        existente = {r.text().strip() for r in pastrate}
        randuri = [r for r in randuri if r.text().strip() not in existente]
        pastrate[tinta:tinta] = randuri + [R.Rand([])]

    pastrate.append(R.Rand([]))
    for text, font in _livrabile(nr_module):
        pastrate.append(R.Rand([(1, text, None)], span=(1, 7),
                               stil_nou=dict(font=font, align=stil.A_WRAP_TOP)))

    pastrate.append(R.Rand([]))
    for text, font in [
        ("VERIFICARE LEGISLATIVĂ — completări ulterioare datei de 14.08.2026",
         stil.F_TITLU_BLOC),
        ("Afirmațiile adăugate odată cu trainingurile 2 și 3 nu intră sub verificarea "
         "din 14.08.2026 de mai sus și au propria dată: L. 239/2025 (capital social minim "
         "și blocajul de activ net), OUG 8/2026 (pragul mijloacelor fixe la 5.000 lei), "
         "L. 141/2025 (cotele 21% / 11%). Reconfirmă orice prag sau cotă înainte de "
         "aplicare la un caz concret.", stil.F_NORMAL),
        ("Reproductibilitate: `make build` regenerează ambele workbook-uri din surse/ + date/; "
         "`make verifica` rulează porțile, inclusiv poarta de conservare care demonstrează "
         "că nimic din originalul training 4 nu s-a pierdut.", stil.F_NOTA),
    ]:
        pastrate.append(R.Rand([(1, text, None)], span=(1, 7),
                               stil_nou=dict(font=font, align=stil.A_WRAP_TOP)))

    R.inlocuieste_foaia(wb, "Legendă", pastrate)
    return mutate


def _actualizeaza_cifre(rand, total_fluxuri, total_corelatii):
    """Numerele care descriau starea veche a fișierului devin cele reale."""
    inlocuiri = [
        ("LISTA FLUXURILOR (~38", f"LISTA FLUXURILOR ({total_fluxuri}"),
        ("~38 fluxuri", f"{total_fluxuri} fluxuri"),
        ("Catalog 38 fluxuri", f"Catalog {total_fluxuri} fluxuri"),
        ("Fluxuri: 38/38 detaliate", f"Fluxuri: {total_fluxuri}/{total_fluxuri} detaliate"),
        ("~38 fluxuri × pași", f"{total_fluxuri} fluxuri × pași"),
        ("245+ rânduri", "270+ rânduri"),
    ]

    def fn(v):
        for a, b in inlocuiri:
            if a in v:
                v = v.replace(a, b)
        return v

    return rand.transformat(fn)
