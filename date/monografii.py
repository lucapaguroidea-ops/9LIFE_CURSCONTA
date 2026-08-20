"""Excepțiile porții 18 — blocuri de monografie care NU trebuie să se echilibreze.

Documentele citează uneori, deliberat, o înregistrare greșită din notițele brute, ca s-o
corecteze imediat sub ea. Un asemenea bloc n-are de ce să treacă verificarea: e greșit
prin definiție, iar asta e chiar rostul lui.

Detectarea automată prin `❌` ar fi prea fragilă ca să fie singurul criteriu — marcajul
poate lipsi, sau poate apărea în alt context. Ca peste tot în sistem, excepția se
declară, cu motiv.
"""

#: Fragmente distinctive din blocurile care citează o eroare. Un bloc care conține
#: fragmentul e scutit de verificarea de echilibru.
CITEAZA_EROARE = {
    "641 - 241": "Citează eroarea din notițele trainingului 3: fondul de salarii "
                 "capitalizat prin 241 în loc de 722. Corectată imediat sub bloc.",
    "641 - 436": "Aceeași citare: CAM pus direct pe 641, în loc de 646 = 436.",
}

# ---------------------------------------------------------------------------
# Ce NU verifică poarta 18, și de ce
#
# Am încercat și a treia verificare — totalurile afirmate în proză lângă bloc („Total
# scos din 371: 26.640”). Din șase afirmații găsite, trei erau fals pozitive: „sold
# creditor de 4.000” e rezultatul NET al blocului (24.000 − 20.000), nu suma debitelor,
# iar „totalul lui 371 = 20.000” numește o componentă, nu totalul.
#
# Formulările din proză sunt prea variate ca potrivirea mecanică să fie de încredere, iar
# o poartă care semnalează jumătate fals încetează să mai fie citită — ceea ce o face mai
# rea decât absența ei. Rămâne gol cunoscut, declarat în documentul de parcurs.
# ---------------------------------------------------------------------------

#: Toleranța la comparațiile aritmetice. Coeficienții rotunjiți din documente
#: („0,1667 × 24.000 = 4.000”, unde exact ar fi 4.000,80) sunt corecți ca practică.
TOLERANTA_RELATIVA = 0.002
TOLERANTA_ABSOLUTA = 0.02
