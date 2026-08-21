"""Harta de diacritice pentru cele două foi rămase în registrul vechi.

`Plan de conturi` are 8% din celulele de text lung cu diacritice românești, `Doar rol în
flux` are 0%. Tot ce s-a adăugat după sămânța de 14.08.2026 are 70–85%. Ruptura cade
exact pe linia semințe/derivat, deci „Actiuni proprii” și „Marfuri in curs de
aprovizionare” stau lângă „Închiderea exercițiului”.

## De ce hartă și nu regulă

Nu se poate deriva: `date/plan.py` conține 11 conturi noi și o corecție; cele 257 de
denumiri vin din sămânță. Nu există în cod o sursă din care să se recalculeze. Și nu se
poate ghici: restaurarea automată a diacriticelor în română cere dezambiguizare
gramaticală, iar aici greșeala s-ar face într-o denumire cu formulare legală.

Deci: dicționar explicit, pe CUVÂNT. **Un cuvânt care nu e în hartă rămâne neatins.**

## Omografele nu intră în hartă

Cuvintele de mai jos diferă prin diacritice ȘI prin articol, iar în corpusul ăsta forma
fără diacritice e cea corectă. Sunt lăsate pe loc deliberat, cu motivul lângă ele —
`EXCEPTII`. Mai bine un cuvânt nerestaurat decât unul restaurat greșit.
"""

#: formă fără diacritice → formă corectă. Cheile sunt minuscule; potrivirea păstrează
#: majuscula inițială a apariției.
HARTA = {
    # --- terminologie de bază, cele mai frecvente
    "in": "în", "si": "și", "intre": "între", "catre": "către", "dupa": "după",
    "pana": "până", "fara": "fără", "cat": "cât", "inca": "încă",
    "niciodata": "niciodată",
    # --- clasa 1: capitaluri
    "actiuni": "acțiuni", "actiunilor": "acțiunilor", "actionari": "acționari",
    "actionarii": "acționarii", "actionarilor": "acționarilor",
    "asociati": "asociați", "asociatii": "asociații", "asociatilor": "asociaților",
    "varsaminte": "vărsăminte", "nevarsat": "nevărsat", "varsat": "vărsat",
    "nevarsate": "nevărsate", "rascumparate": "răscumpărate",
    "rascumparari": "răscumpărări", "castiguri": "câștiguri",
    "exercitiului": "exercițiului", "obligatiuni": "obligațiuni",
    "obligatiunilor": "obligațiunilor", "imprumuturi": "împrumuturi",
    "imprumuturilor": "împrumuturilor", "dobanzi": "dobânzi", "dobanzile": "dobânzile",
    "garantii": "garanții", "obligatie": "obligație", "participatie": "participație",
    "participatii": "participații", "estimata": "estimată", "delegata": "delegată",
    "unitatii": "unității", "subunitati": "subunități", "entitati": "entități",
    "entitatile": "entitățile",
    # --- clasa 2: imobilizări
    "imobilizari": "imobilizări", "imobilizarilor": "imobilizărilor",
    "imobilizarile": "imobilizările", "imobilizata": "imobilizată",
    "amortizari": "amortizări", "amortizarile": "amortizările",
    "amortizarii": "amortizării", "amenajari": "amenajări",
    "constructii": "construcții", "constructie": "construcție",
    "instalatii": "instalații", "plantatii": "plantații", "licente": "licențe",
    "marci": "mărci", "investitii": "investiții", "investitiile": "investițiile",
    "executie": "execuție", "antrepriza": "antrepriză", "receptie": "recepție",
    "nereceptionat": "nerecepționat", "detinute": "deținute", "detinut": "deținut",
    "birotica": "birotică", "aparatura": "aparatură",
    # --- clasa 3: stocuri
    "marfuri": "mărfuri", "marfurile": "mărfurile", "marfurilor": "mărfurilor",
    "marfa": "marfă", "deseuri": "deșeuri", "neterminata": "neterminată",
    "productie": "producție", "productia": "producția", "productiei": "producției",
    "pret": "preț", "pretul": "prețul", "amanunt": "amănunt", "diferente": "diferențe",
    "diferentele": "diferențele",
    # --- clasa 4: terți
    "terti": "terți", "tertilor": "terților", "clienti": "clienți",
    "creanta": "creanță", "creante": "creanțe", "creantelor": "creanțelor",
    "contra-creanta": "contra-creanță", "diversi": "diverși",
    "decontari": "decontări", "decontarilor": "decontărilor",
    "retineri": "rețineri", "angajatilor": "angajaților", "somaj": "șomaj",
    "asigurari": "asigurări", "asigurarile": "asigurările", "sociala": "socială",
    "contributia": "contribuția", "asiguratorie": "asigurătorie", "munca": "muncă",
    "protectia": "protecția", "adaugata": "adăugată", "plata": "plată",
    "platit": "plătit", "platita": "plătită", "platite": "plătite",
    "deductibila": "deductibilă", "colectata": "colectată",
    "neexigibila": "neexigibilă", "cumparari": "cumpărări", "vanzari": "vânzări",
    "vanzarea": "vânzarea", "incasare": "încasare", "incasat": "încasat",
    "subventii": "subvenții", "subventia": "subvenția",
    "neidentificata": "neidentificată", "corectie": "corecție",
    "administratie": "administrație", "utilitatile": "utilitățile",
    "intretinerea": "întreținerea", "reparatiile": "reparațiile",
    "redeventele": "redevențele", "locatiile": "locațiile",
    "cercetarile": "cercetările", "reclama": "reclamă", "deplasari": "deplasări",
    "detasari": "detașări", "transferari": "transferări", "postale": "poștale",
    "telecomunicatii": "telecomunicații", "inconjurator": "înconjurător",
    # --- clasa 5: trezorerie
    "banci": "bănci", "valuta": "valută", "evita": "evită", "dubla": "dublă",
    "numarare": "numărare",
    # --- roluri, corelații, proză de clasificare
    "ajustari": "ajustări", "ajustarile": "ajustările", "ajustarilor": "ajustărilor",
    "cheltuiala": "cheltuială", "contra-cheltuiala": "contra-cheltuială",
    "extrabilantier": "extrabilanțier", "extrabilantiera": "extrabilanțieră",
    "bifunctional": "bifuncțional", "bilant": "bilanț", "bilantului": "bilanțului",
    "temporala": "temporală", "interna": "internă", "reala": "reală", "neta": "netă",
    "bruta": "brută", "aferenta": "aferentă", "capitalizata": "capitalizată",
    "reversibila": "reversibilă", "lunara": "lunară", "optional": "opțional",
    "calculatie": "calculație", "corelatie": "corelație", "observatie": "observație",
    "operatiuni": "operațiuni", "inregistrate": "înregistrate",
    "inregistrare": "înregistrare", "intocmit": "întocmit", "inchidere": "închidere",
    "inchide": "închide", "reprezentand": "reprezentând", "folosinta": "folosință",
    "evidenta": "evidență", "legatura": "legătură", "masura": "măsura",
    "contrapartida": "contrapartidă", "achizitiilor": "achizițiilor",
    "activitati": "activități", "activitatii": "activității",
    "activitatilor": "activităților", "variatia": "variația", "baza": "bază",
    "sera": "seră", "reluari": "reluări", "reversari": "reversări",
    "obtinute": "obținute", "obtinuta": "obținută", "colecteaza": "colectează",
    "neutralizeaza": "neutralizează", "cumuleaza": "cumulează",
    "controleaza": "controlează", "elibereaza": "eliberează", "acorda": "acordă",
    "elimina": "elimină", "tine": "ține",
}

#: cuvânt → de ce rămâne neatins. Fiecare e omograf: forma fără diacritice e cea
#: corectă în contextul din care apare aici.
EXCEPTII = {
    "casa": "contul 531 se numește „Casa”, articulat. „Casă” ar fi altceva.",
    "banca": "la fel, „Banca” în denumirea de cont și în „transfer bancă↔casă”.",
    "taxa": "„Taxa pe valoarea adăugată” — denumirea oficială e articulată.",
    "cota": "„pe cota TVA” e articulat; „cotă” ar cere altă prepoziție.",
    "firma": "„creditare firma” — articulat în context.",
    "factura": "„Factura în SPV”, „factura NU” — toate articulate.",
    "oglinda": "„Oglinda lui 327”, „Oglinda internă a cheltuielilor” — articulat.",
    "cifra": "„cifra de afaceri” e termen fix, articulat.",
    "suma": "„suma neidentificată din extras” — articulat (adjectivul se corectează).",
    "vama": "„TVA vama prin comisionar” și codul analitic 446.VAMA.",
    "grupa": "„pe grupa de mijloc fix” — articulat.",
    "uzura": "„cumulează uzura, se scade” — articulat.",
    "natura": "„Materiale de natura obiectelor de inventar” e denumirea OMFP exactă.",
    "clasa": "„CLASA 1” — titlu de secțiune, articulat.",
    "coloana": "„Coloana 1 — Natura” — articulat.",
}

#: Foile pe care se aplică. Restul workbook-ului e deja în registrul nou.
FOI = ("Plan de conturi", "Doar rol în flux")

#: Coloanele de SIMBOL nu se ating niciodată — nici măcar dacă un simbol ar semăna cu un
#: cuvânt din hartă. Se recunosc după antet.
CAP_SIMBOL = ("simbol", "cont", "id")
