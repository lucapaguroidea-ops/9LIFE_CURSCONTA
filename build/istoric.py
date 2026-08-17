"""Foaia `Istoric` — memoria sistemului, ca documentul de lucru să rămână curat.

Tot ce e istoric de livrare („ETAPA 0…4”, „Tranșa 1…3”), tot ce a fost renumerotat și
tot ce a fost eliminat la deduplicare ajunge aici, VERBATIM. Foaia de lucru descrie
sistemul așa cum este; foaia asta descrie cum a ajuns așa.

Așa se rezolvă tensiunea dintre „ordonează contabil, nu cronologic” și „nu pierde
nimic”: cronologia nu se șterge, se mută unde îi e locul.
"""
from build import randuri as R
from build import stil
from date import ordine as O


def _titlu(text, latime=6):
    return R.Rand([(1, text, None)], span=(1, latime),
                  stil_nou=dict(font=stil.F_TITLU_BLOC))


def _nota(text, latime=6):
    return R.Rand([(1, text, None)], span=(1, latime),
                  stil_nou=dict(font=stil.F_NOTA, align=stil.A_WRAP_TOP))


def _cap(capete):
    return R.Rand([(i, h, None) for i, h in enumerate(capete, start=1)],
                  stil_nou=dict(font=stil.F_CAP_TABEL_ALB, fill=stil.FILL_ANTET,
                                align=stil.A_CENTER))


def _rand(valori):
    return R.Rand([(i, v, None) for i, v in enumerate(valori, start=1)],
                  stil_nou=dict(font=stil.F_NORMAL, align=stil.A_WRAP))


def construieste(wb, *, mutate, orfane, reformulari, resturi=(), absorbite=None):
    """Creează foaia Istoric. `mutate` = rândurile de narativ scoase din Legendă."""
    gol = R.Rand([])
    out = [
        R.Rand([(1, "ISTORIC — cum a ajuns fișierul aici", None)], span=(1, 6),
               stil_nou=dict(font=stil.F_TITLU)),
        _nota("Foaia de lucru descrie sistemul așa cum este ACUM, ordonat contabil. "
              "Aici stă cronologia: ce s-a renumerotat, ce s-a contopit, ce s-a eliminat "
              "ca duplicat și ce narativ de etapă a fost mutat din Legendă. "
              "Nimic din originalul training 4 nu s-a pierdut — s-a mutat."),
        gol,
    ]

    # ---- 1. echivalența de numerotare
    out.append(_titlu("1. Echivalența de numerotare (permanentă)"))
    out.append(_nota("Numerotarea veche era secvențială, în ordinea livrărilor. Cea nouă "
                     "codifică clasa contului principal, deci un flux adăugat peste un an "
                     "primește următorul număr liber din clasa lui și stă fizic la locul lui. "
                     "Tabelul rămâne aici permanent, ca referințele vechi să se poată rezolva."))
    out.append(_cap(["ID nou", "ID vechi", "Clasa", "Denumire"]))
    for nou, vechi, den in O.ORDINE:
        out.append(_rand([nou, vechi, O.CLASA[nou], den]))
    out.append(gol)

    # ---- 2. contopiri
    out.append(_titlu("2. Fluxuri contopite"))
    out.append(_nota("Fluxul absorbit nu a fost șters: pașii și cifrele lui au devenit o "
                     "variantă etichetată în interiorul fluxului gazdă."))
    out.append(_cap(["ID vechi", "A intrat în", "Ca", "De ce", "Titlu original",
                     "Conturi cheie / roluri (din catalogul vechi)"]))
    for vechi, (gazda, eticheta, motiv) in O.CONTOPIRI.items():
        meta = (absorbite or {}).get(vechi, {})
        cat = meta.get("catalog", {})
        metadate = " · ".join(str(cat.get(c, "") or "").strip()
                              for c in (5, 6) if str(cat.get(c, "") or "").strip())
        out.append(_rand([vechi, gazda, eticheta, motiv,
                          meta.get("titlu", ""), metadate]))
    out.append(gol)

    # ---- 3. defecte preexistente reparate
    out.append(_titlu("3. Defecte preexistente, reparate la reordonare"))
    out.append(_cap(["Ce", "Constatare", "Remediu"]))
    for r in [
        ("Catalog incomplet",
         "13 din 44 de fluxuri nu aveau rând de catalog: F-08…F-14 (împinse afară de "
         "blocul orfan F-07) și F-39…F-44 (nu fuseseră adăugate niciodată). Toate aveau "
         "monografie completă — doar indexul nu le cunoștea.",
         "Catalogul se GENEREAZĂ acum din monografiile reale. Nu mai poate diverge."),
        ("F-07 duplicat",
         "Pașii 2 și 3 ai lui F-07 apăreau de două ori: o dată orfan în zona de catalog "
         "(fără pasul 1, fără titlu) și o dată în blocul propriu. Aceleași cifre, aceleași "
         "conturi, formulare diferită.",
         "Blocul canonic rămâne; formularea eliminată e păstrată verbatim la punctul 4."),
        ("F-18 fără antet",
         "Pașii lui F-18 pluteau după blocul F-16, fără rând-titlu propriu, deci fluxul "
         "nu era vizibil ca entitate.",
         "A primit titlu și antet de tabel proprii."),
    ]:
        out.append(_rand(list(r)))
    out.append(gol)

    # ---- 4. text eliminat la deduplicare
    out.append(_titlu("4. Text eliminat la deduplicare (verbatim)"))
    out.append(_nota("Păstrat cuvânt cu cuvânt, ca poarta de conservare să treacă fără "
                     "excepții și ca formularea să rămână consultabilă."))
    for r in orfane:
        for _, v, _ in r.celule:
            if isinstance(v, str) and v.strip():
                out.append(_rand([v]))
    out.append(gol)

    # ---- 5. reformulări declarate
    out.append(_titlu("5. Texte înlocuite intenționat"))
    out.append(_cap(["Text original", "A devenit", "Motiv"]))
    for d in reformulari:
        out.append(_rand([d["text"], d["devine"], d["motiv"]]))
    out.append(gol)

    # ---- 6. titluri și note de secțiune, scoase la reordonare
    if resturi:
        out.append(_titlu("6. Titluri și note de secțiune, scoase la reordonare"))
        out.append(_nota("Descriau gruparea veche — pe tranșe și pe etape de livrare — care "
                         "nu mai există: fluxurile stau acum la clasa lor de conturi. "
                         "Textul se păstrează verbatim."))
        for r in resturi:
            for _, v, _ in r.celule:
                if isinstance(v, str) and v.strip():
                    out.append(_rand([v]))
        out.append(gol)

    # ---- 7. narativul de etape, mutat din Legendă
    if mutate:
        out.append(_titlu("7. Narativul de etape, mutat din Legendă"))
        out.append(_nota("Descria ordinea livrărilor, nu conținutul contabil. Mutat aici "
                         "verbatim ca Legenda să descrie sistemul, nu istoria lui."))
        out.extend(mutate)

    ws = wb.create_sheet("Istoric")
    R.scrie(ws, out)
    for col, lat in (("A", 30), ("B", 26), ("C", 40), ("D", 60), ("E", 30), ("F", 24)):
        ws.column_dimensions[col].width = lat
    return ws
