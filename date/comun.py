"""Tipuri și helperi comuni pentru conținutul din `date/`."""


def ro(x) -> str:
    """Formatează un număr în stil românesc: 155250.5 -> '155.250,50', 2000 -> '2.000'."""
    if x is None:
        return "—"
    if isinstance(x, str):
        return x
    neg = x < 0
    x = abs(float(x))
    intreg = int(x)
    zecimi = round((x - intreg) * 100)
    if zecimi == 100:          # 1999.999 -> 2000,00
        intreg += 1
        zecimi = 0
    s = f"{intreg:,}".replace(",", ".")
    if zecimi:
        s = f"{s},{zecimi:02d}"
    return ("-" + s) if neg else s


def pas(nr, doc, explicatie, *, dr=(), cr=(), rol="", declarativ="—", revelator=False):
    """Un pas de flux.

    dr / cr: liste de perechi (cont, sumă). Pași de verificare au ambele goale.
    `revelator=True` marchează pasul care demonstrează rolul contului — poarta
    de calitate cere exact un astfel de pas pe fiecare flux didactic.
    """
    return {
        "nr": nr,
        "doc": doc,
        "explicatie": explicatie,
        "dr": list(dr),
        "cr": list(cr),
        "rol": rol,
        "declarativ": declarativ,
        "revelator": revelator,
    }


def flux(id, denumire, *, transa=4, didactic=False, roluri="", conturi="",
         status="Detaliat (Etapa 4)", note="—", titlu=None, pasi=(), principiu=""):
    return {
        "id": id,
        "transa": transa,
        "denumire": denumire,
        "didactic": "★ DA" if didactic else "nu",
        "roluri": roluri,
        "conturi": conturi,
        "status": status,
        "note": note,
        "titlu": titlu or f"{id} — {denumire}" + (" ★" if didactic else ""),
        "pasi": list(pasi),
        "principiu": principiu,
    }
