"""Reordonarea foii „Fluxuri” pe clase contabile, plus foaia „Istoric”.

Foaia originală era ordonată după ordinea livrărilor: Etapa 1, apoi Etapa 2, apoi
Etapa 3, apoi cazurile grele, apoi trainingurile 2 și 3. Modulul ăsta o rescrie în
ordinea planului de conturi (clasa 1 → 8), cea din `date/ordine.py`.

Trei lucruri se rezolvă odată cu reordonarea:

1. **Catalogul devine DERIVAT.** În original, 13 din 44 de fluxuri nu aveau rând de
   catalog (F-08…F-14 fuseseră împinse afară de blocul orfan F-07, iar F-39…F-44 nu
   fuseseră adăugate niciodată). Catalogul se generează acum din blocurile reale,
   deci nu mai poate să diveargă de conținut.
2. **Blocul orfan F-07 dispare** din zona de catalog. Textul lui, redundant dar
   diferit ca formulare, se păstrează verbatim în foaia `Istoric`.
3. **Contopirile** (F-27 în F-208, F-31 în F-211) devin variante etichetate ale
   fluxului gazdă — cu cifrele lor proprii, nu șterse.
"""
import re

from build import randuri as R
from build import stil
from date import ordine as O

RE_ID = re.compile(r"^F-\d+$")
RE_BLOC = re.compile(r"^(F-\d+)\s+—")
DIDACTIC = ("nu", "★ DA")


# --------------------------------------------------------------------- parsare
def _tip(rand):
    """Clasifică un rând înainte de orice grupare — altfel granițele ies greșit."""
    t = rand.text().strip()
    v = rand.valori()
    if RE_BLOC.match(t):
        return "bloc"
    if t == "Flux ID":
        return "cap"
    if RE_ID.match(t):
        if str(v.get(4, "") or "").strip() in DIDACTIC:
            return "catalog"
        if isinstance(v.get(2), (int, float)):
            return "pas"
        return "alt"
    if t.startswith("Principiul:"):
        return "principiu"
    if rand.gol():
        return "gol"
    if _e_titlu_sectiune(rand):
        return "sectiune"
    return "alt"


def parseaza(rows):
    """Împarte foaia în preambul, rânduri de catalog, blocuri de monografie și orfane.

    Granițele unui bloc de monografie: începe la un rând-titlu `F-xx — …` și ține până
    la următorul titlu, până la primul rând de catalog sau până la un titlu de secțiune.
    Rândurile goale de la coadă se taie.

    Două particularități ale fișierului original, tratate explicit:
      - F-18 nu are rând-titlu: pașii lui plutesc după blocul F-16. Un set de pași cu
        alt ID decât proprietarul blocului devine bloc propriu, cu titlu sintetizat.
      - F-07 are pași duplicați în zona de catalog, fără titlu și fără pasul 1. Aceia
        ies ca „orfani” și nu intră în reconstrucție.
    """
    n = len(rows)
    tipuri = [_tip(r) for r in rows]

    # --- 1. regiunile blocurilor de monografie
    limite, i = [], 0
    while i < n:
        if tipuri[i] != "bloc":
            i += 1
            continue
        j = i + 1
        while j < n and tipuri[j] not in ("bloc", "catalog", "sectiune"):
            j += 1
        sfarsit = j
        while sfarsit > i + 1 and tipuri[sfarsit - 1] == "gol":
            sfarsit -= 1
        limite.append((RE_BLOC.match(rows[i].text().strip()).group(1), i, sfarsit))
        i = j

    # --- 2. pași cu alt ID în interiorul unui bloc → bloc propriu (cazul F-18)
    blocuri = {}
    for fid, i, j in limite:
        taie = None
        for x in range(i + 1, j):
            if tipuri[x] == "pas" and rows[x].text().strip() != fid:
                taie = x
                break
        if taie is None:
            blocuri[fid] = rows[i:j]
            continue
        gazda = rows[i:taie]
        while gazda and tipuri[i + len(gazda) - 1] == "gol":
            gazda.pop()
        blocuri[fid] = gazda
        strain = rows[taie:j]
        sid = rows[taie].text().strip()
        blocuri[sid] = strain

    # --- 3. catalog și orfani (pași în afara oricărui bloc)
    in_bloc = {x for _, i, j in limite for x in range(i, j)}
    catalog, orfane = {}, []
    for i, r in enumerate(rows):
        if tipuri[i] == "catalog":
            catalog[r.text().strip()] = r
        elif i not in in_bloc and tipuri[i] == "pas":
            orfane.append(i)
    # „Principiul:” lipit de un orfan aparține tot orfanului
    for i in list(orfane):
        if i + 1 < n and tipuri[i + 1] == "principiu" and (i + 1) not in in_bloc:
            orfane.append(i + 1)

    prima = min([i for i, t in enumerate(tipuri) if t in ("catalog", "pas", "bloc")], default=5)
    cap_catalog = next((r for i, r in enumerate(rows[:prima]) if tipuri[i] == "cap"), None)
    preambul = [r for i, r in enumerate(rows[:prima])
                if tipuri[i] not in ("cap", "gol")]

    # tot ce nu e preambul, catalog, bloc sau orfan: titluri de secțiune și note libere.
    # Descriau gruparea veche (pe tranșe / pe etape), care dispare — dar textul lor se
    # păstrează, mutat în foaia Istoric.
    consumate = set(in_bloc) | set(orfane) | set(range(prima))
    consumate |= {i for i, t in enumerate(tipuri) if t == "catalog"}
    resturi = [rows[i] for i in range(n)
               if i not in consumate and tipuri[i] != "gol"]

    return preambul, cap_catalog, catalog, blocuri, [rows[i] for i in sorted(orfane)], resturi


def _e_titlu_sectiune(rand):
    t = rand.text().strip()
    if not t or RE_BLOC.match(t):
        return False
    return t.startswith("———") or (t.isupper() and len(t) > 14) or t.startswith("STATUS FINAL")


# ------------------------------------------------------- catalog derivat din bloc
def _deriva_catalog(fid, bloc, sablon):
    """Construiește rândul de catalog pentru un flux care nu avea unul.

    Metadatele se citesc din bloc — nu se inventează: didactic din ★ din titlu,
    conturile din coloanele Cont D/Cont C ale pașilor, rolul din pasul revelator.
    """
    titlu = bloc[0].text().strip()
    denumire = RE_BLOC.sub("", titlu).strip(" —").strip()
    didactic = "★ DA" if "★" in titlu else "nu"
    denumire = denumire.replace("★", "").strip()

    conturi, roluri = [], []
    for r in bloc:
        v = r.valori()
        if not RE_ID.match(r.text().strip()):
            continue
        for col in (5, 6):
            for c in str(v.get(col, "") or "").split("\n"):
                c = c.strip()
                if c and c != "—" and c not in conturi:
                    conturi.append(c)
        rol = str(v.get(8, "") or "").strip()
        if "pas revelator" in rol.lower():
            roluri.append(rol)

    nota = roluri[0] if roluri else "—"
    scurt = ", ".join(conturi[:6]) + (" …" if len(conturi) > 6 else "")
    valori = {1: fid, 2: O.CLASA.get(O.HARTA.get(fid, fid), ""), 3: denumire,
              4: didactic, 5: _roluri_din(bloc), 6: scurt, 7: "Detaliat", 8: nota}
    rand = sablon
    for col, val in valori.items():
        rand = rand.cu_valoare(col, val)
    return rand


def _roluri_din(bloc):
    """Rolurile revelate, unificate din coloana «Rol revelat» a pașilor."""
    vazute = []
    for r in bloc:
        if not RE_ID.match(r.text().strip()):
            continue
        rol = str(r.valori().get(8, "") or "").strip()
        rol = re.sub(r"\s*\(pas revelator[^)]*\)", "", rol)
        rol = rol.split(":")[0].strip()
        for parte in re.split(r"\s*\+\s*", rol):
            parte = parte.strip()
            if parte and parte not in ("—", "") and parte not in vazute \
                    and not parte.lower().startswith("stare terminală"):
                vazute.append(parte)
    return " + ".join(vazute[:3]) if vazute else "—"


# ----------------------------------------------------------------- reconstrucție
def rescrie(wb, nume="Fluxuri"):
    """Rescrie foaia Fluxuri în ordine canonică. Întoarce rândurile eliminate."""
    ws = wb[nume]
    rows = R.citeste(ws)
    preambul, cap_catalog, catalog, blocuri, orfane, resturi = parseaza(rows)

    sablon = next(iter(catalog.values()))
    gol = R.Rand([])

    # blocurile fără rând-titlu (F-18 în originalul training 4) îl primesc acum
    sablon_titlu = next(b[0] for b in blocuri.values() if RE_BLOC.match(b[0].text().strip()))
    sablon_cap = next((r for b in blocuri.values() for r in b
                       if r.text().strip() == "Flux ID"), None)
    for fid, bloc in list(blocuri.items()):
        if RE_BLOC.match(bloc[0].text().strip()):
            continue
        cat_rand = catalog.get(fid)
        denumire = str(cat_rand.valori().get(3, "") or "").strip() if cat_rand else fid
        didactic = str(cat_rand.valori().get(4, "") or "").strip() if cat_rand else "nu"
        titlu = f"{fid} — {denumire}" + (" ★" if didactic.startswith("★") else "")
        cap = [sablon_cap] if (sablon_cap and bloc[0].text().strip() != "Flux ID") else []
        blocuri[fid] = [sablon_titlu.cu_valoare(1, titlu)] + cap + bloc

    statusuri = {}
    out = list(preambul)
    out.append(_nota(sablon,
                     "Observație păstrată din gruparea veche, valabilă în continuare: fluxurile "
                     "didactice grele „nu sunt liniare. Fiecare pornește dintr-o stare «murdară» "
                     "sau produce intersecție între două roluri. Acolo apar erorile de cabinet.” "
                     "Ele nu mai stau grupate la final, ci fiecare la clasa lui de conturi.", 9))
    out.append(gol)

    # ---- catalogul, derivat, grupat pe clase
    out.append(_titlu(sablon, "CATALOGUL FLUXURILOR — grupat pe clase de conturi", 9))
    out.append(_nota(sablon,
                     "Catalogul se generează din monografiile reale, deci nu poate să rămână "
                     "în urma lor. ★ = flux didactic, cu pas revelator identificat.", 9))
    out.append(gol)
    if cap_catalog:
        out.append(cap_catalog)

    for clasa, titlu_clasa, bloc_clasa in O.BLOCURI:
        out.append(_subtitlu(sablon, titlu_clasa, 9))
        for nou, vechi, _ in bloc_clasa:
            r = catalog.get(vechi) or _deriva_catalog(vechi, blocuri[vechi], sablon)
            r = r.cu_valoare(2, clasa)
            if nou in O.RETITULARI:
                r = r.cu_valoare(3, O.RETITULARI[nou])
            vechi_status = str(r.valori().get(7, "") or "").strip()
            statusuri[vechi] = vechi_status
            r = r.cu_valoare(7, _status_curat(vechi_status))
            out.append(r)
    out.append(gol)
    out.append(gol)

    # ---- monografiile, în aceeași ordine
    out.append(_titlu(sablon, "MONOGRAFIILE FLUXURILOR — pas cu pas", 9))
    out.append(gol)
    for clasa, titlu_clasa, bloc_clasa in O.BLOCURI:
        out.append(_subtitlu(sablon, titlu_clasa, 9))
        out.append(gol)
        for nou, vechi, _ in bloc_clasa:
            corp = blocuri[vechi]
            if nou in O.RETITULARI:
                titlu_nou = f"{vechi} — {O.RETITULARI[nou]}"
                if "★" in corp[0].text():
                    titlu_nou += " ★"
                corp = [corp[0].cu_valoare(1, titlu_nou)] + corp[1:]
            out.extend(corp)
            out.append(gol)
            for absorbit, (gazda, eticheta, motiv) in O.CONTOPIRI.items():
                if gazda == nou:
                    out.extend(_varianta(blocuri[absorbit], vechi, eticheta, motiv, sablon))
                    out.append(gol)

    R.inlocuieste_foaia(wb, nume, out)
    # metadatele fluxurilor absorbite (rând de catalog + titlu de bloc) nu se pierd:
    # pleacă în tabelul de contopiri din Istoric
    absorbite = {}
    for vechi in O.CONTOPIRI:
        absorbite[vechi] = dict(
            titlu=blocuri[vechi][0].text().strip() if vechi in blocuri else "",
            catalog=catalog.get(vechi).valori() if vechi in catalog else {},
        )
    return orfane, resturi, absorbite, statusuri


def _varianta(bloc, id_gazda, eticheta, motiv, sablon):
    """Blocul absorbit, re-etichetat ca variantă a gazdei. Cifrele rămân ale lui."""
    vechi = RE_BLOC.match(bloc[0].text().strip()).group(1)
    out = [bloc[0].cu_valoare(1, f"{id_gazda} (variantă) — {eticheta} [fost {vechi}]")]
    for r in bloc[1:]:
        out.append(r.cu_valoare(1, id_gazda) if RE_ID.match(r.text().strip()) else r)
    out.append(_nota(sablon, f"De ce e variantă și nu flux separat: {motiv}", 9))
    return out


RE_ETAPA = re.compile(r"\s*\(Etapa\s*\d+\)")


def _status_curat(status):
    """Scoate „(Etapa N)” din status — e istoric de livrare, nu stare a fluxului.

    Marcajele „CORECTAT / CLARIFICAT <dată>” rămân: acelea spun ceva despre CONȚINUT
    (că o eroare a fost reparată), nu despre ordinea în care a fost scris fișierul.
    Statusul original se păstrează integral în foaia Istoric.
    """
    return RE_ETAPA.sub("", str(status or "")).strip() or "Detaliat"


def _rand_nou(text, latime, **stil_nou):
    """Un rând creat acum (nu preluat din original), îmbinat pe toată lățimea."""
    return R.Rand([(1, text, None)], span=(1, latime), stil_nou=stil_nou)


def _titlu(_, text, latime):
    return _rand_nou(text, latime, font=stil.F_TITLU_BLOC)


def _subtitlu(_, text, latime):
    return _rand_nou(text, latime, font=stil.F_CAP_TABEL, fill=stil.FILL_ANTET,
                     align=stil.A_WRAP)


def _nota(_, text, latime):
    return _rand_nou(text, latime, font=stil.F_NOTA, align=stil.A_WRAP_TOP)
