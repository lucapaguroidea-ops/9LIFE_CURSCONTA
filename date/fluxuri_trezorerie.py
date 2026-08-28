"""Fluxurile de clasa 5 din trainingul 28.08.2026 — efecte, dobânzi, linii, tichete.

Sursa: `surse/training-8-2026-08-28/notite-revizuit.md`, §3–§6.

Clasa 5 era cea mai subțire parte a sistemului: două fluxuri (viramente interne și
avansuri de trezorerie) pe o clasă întreagă. Trainingul din 28.08 e aproape numai clasa
5, deci golul se închide aici.

Firul comun al celor șase: **banii au mai multe stări între „am dreptul la ei” și „sunt
în cont”.** Efectul primit stinge clientul dar nu aduce lichiditate; efectul scontat a
plecat din mână dar n-a ajuns la scadență; dobânda din scadențar e datorată dar nu
plătită; tichetul e cumpărat dar nu acordat. Fiecare stare are contul ei, și fiecare cont
trebuie să ajungă la zero — altfel starea a rămas blocată acolo.

Cifrele continuă exemplul din notițe: vânzarea de 10.000 + 2.100 TVA dă efectul de 12.100
care se scontează la 80%. Un exemplu care traversează trei fluxuri se verifică singur.
"""
from .comun import flux, pas

FLUXURI_TREZORERIE = [

    flux("F-84", "Efecte de încasat: CEC (5112) și bilet la ordin (5113)",
         didactic=True,
         roluri="Tranzit între stingerea creanței și încasare",
         conturi="5112, 5113, 5121, 4111, 4427, 707",
         note="Efectele se emit la TERMEN. Rar se emite factura azi și se primește "
              "efectul tot azi — între cele două momente stă tot riscul.",
         principiu="Primirea efectului stinge clientul, dar nu aduce banii. 4111 ajunge "
                   "la zero în timp ce lichiditatea e încă zero — iar cine se uită doar "
                   "la soldul clienților crede că a încasat. Riscul de neîncasare nu "
                   "dispare, se mută pe 5112 sau 5113.",
         pasi=[
             pas(1, "Factură de vânzare",
                 "Marfă de 10.000 lei, cotă 21%. Total de încasat: 12.100 lei.",
                 dr=[("4111.client", 12100)],
                 cr=[("707", 10000), ("4427", 2100)],
                 rol="Creanță + Venit + TVA colectată"),
             pas(2, "CEC primit de la client",
                 "Clientul plătește cu CEC de 12.100 lei. Fișa lui se închide ACUM, deși "
                 "banii vin la scadența înscrisă pe efect.",
                 dr=[("5112.client", 12100)], cr=[("4111.client", 12100)],
                 rol="Pas revelator: creanța se stinge înaintea încasării",
                 revelator=True),
             pas(3, "Extras de cont — scadența CEC-ului",
                 "Abia acum apar banii. Dacă efectul nu e onorat, 5112 rămâne cu sold și "
                 "arată exact ce s-a întâmplat: clientul a plătit cu o hârtie fără "
                 "acoperire.",
                 dr=[("5121", 12100)], cr=[("5112.client", 12100)],
                 rol="Încasarea efectivă"),
             pas(4, "Varianta cu bilet la ordin",
                 "Mecanica e identică, pe contul 5113. Diferența practică e că biletul "
                 "la ordin poate fi dus la bancă spre scontare — vezi F-504.",
                 dr=[("5113.client", 12100)], cr=[("4111.client", 12100)],
                 rol="Aceeași stare, alt instrument"),
             pas(5, "Verificare",
                 "Sold 4111 = 0 după pasul 2, sold 5112 = 0 după pasul 3. Un sold rămas "
                 "pe 5112 sau 5113 DUPĂ scadență e efect neonorat, nu creanță curentă — "
                 "și se tratează ca atare, cu ajustare dacă e cazul.",
                 rol="Stare terminală: 4111 = 0, 511x = 0 după scadență"),
         ]),

    flux("F-85", "Scontarea biletului la ordin (5114)", didactic=True,
         roluri="Lichiditate anticipată contra cost",
         conturi="5114, 5113, 5121, 667",
         note="Instrument scump. Banca îl acordă societăților cu activitate îndelungată "
              "și clienți la fel — nu e o facilitate pentru firme mici.",
         principiu="Contabilitatea românească e de ANGAJAMENTE: faci factura, nu o "
                   "încasezi, și statul cere TVA-ul și impozitul oricum. O societate se "
                   "poate bloca având vânzări. Scontarea cumpără lichiditate mai "
                   "devreme, iar cei 20% nu sunt dobândă anuală — sunt costul "
                   "operațiunii, plătit o dată.",
         pasi=[
             pas(1, "Bilet la ordin în portofoliu",
                 "Biletul de 12.100 lei din F-503, cu scadență peste două luni. Banca "
                 "acceptă să-l sconteze la 80%.",
                 rol="Starea inițială: efect cu scadență îndepărtată"),
             pas(2, "Borderou de scontare",
                 "Efectul pleacă spre bancă. ⚠ Mutarea din 5113 în 5114 spune că "
                 "efectul A PLECAT DIN MÂNA TA — cât timp stă pe 5113, îl mai ai și "
                 "poți dispune de el.",
                 dr=[("5114", 12100)], cr=[("5113.client", 12100)],
                 rol="Pas revelator: efectul remis nu mai e efect deținut",
                 revelator=True),
             pas(3, "Extras de cont",
                 "Banca virează 80% din valoare: 12.100 × 80% = 9.680 lei.",
                 dr=[("5121", 9680)], cr=[("5114", 9680)],
                 rol="Lichiditatea obținută anticipat"),
             pas(4, "Notă contabilă — costul scontării",
                 "Restul de 2.420 lei e cheltuială financiară, nu creanță pierdută: "
                 "clientul a plătit integral, banca a reținut costul. ⚠ Contul e 667 — "
                 "notițele scriau `6067`, care nu există.",
                 dr=[("667", 2420)], cr=[("5114", 2420)],
                 rol="Costul lichidității anticipate"),
             pas(5, "Verificare",
                 "Sold 5113 = 0, sold 5114 = 0 (9.680 + 2.420 = 12.100), sold 4111 = 0 "
                 "încă din F-503. Circuitul s-a închis: clientul e zero, banii sunt în "
                 "bancă. Un sold pe 5114 înseamnă scontare nefinalizată — cel mai "
                 "probabil costul n-a fost înregistrat.",
                 rol="Stare terminală: 5114 = 0, cu costul recunoscut pe 667"),
         ]),

    flux("F-86", "Dobânda la credit: fixă prin 471 vs. variabilă prin 5186",
         didactic=True,
         roluri="Regularizare temporală + Datorie de dobândă",
         conturi="5186, 666, 471, 5121",
         note="Distincția nu e de stil: 471 înseamnă „știu suma ȘI știu perioada”.",
         principiu="Dobânda FIXĂ din scadențar se cunoaște de la început, deci e "
                   "cheltuială în avans și se eșalonează. Dobânda VARIABILĂ, calculată "
                   "de bancă la sold, nu se poate anticipa — o sumă pusă în 471 pentru "
                   "ea se dovedește greșită la prima schimbare de indice.",
         pasi=[
             pas(1, "Scadențar de credit — dobândă FIXĂ",
                 "Dobânda totală din scadențar, 12.000 lei pe 24 de luni. Se cunoaște "
                 "integral, deci se recunoaște integral ca datorie și ca avans.",
                 dr=[("471.dobanda", 12000)], cr=[("5186.credit", 12000)],
                 rol="Cheltuială în avans + Datorie de dobândă"),
             pas(2, "Extras de cont — plata ratei de dobândă",
                 "Se stinge datoria, lună de lună: 12.000 ÷ 24 = 500 lei.",
                 dr=[("5186.credit", 500)], cr=[("5121", 500)],
                 rol="Stingerea datoriei"),
             pas(3, "Notă contabilă lunară",
                 "Eșalonarea pe cheltuială. Plata și cheltuiala sunt DOUĂ lucruri "
                 "diferite: prima golește 5186, a doua golește 471.",
                 dr=[("666", 500)], cr=[("471.dobanda", 500)],
                 rol="Pas revelator: plata stinge datoria, eșalonarea consumă avansul",
                 revelator=True),
             pas(4, "Varianta cu dobândă VARIABILĂ",
                 "Banca o calculează la sold, în fiecare lună. Nu se cunoaște dinainte, "
                 "deci nu trece prin 471: se recunoaște direct, în luna în care se "
                 "produce. `666 = 5121` direct e la fel de corect.",
                 dr=[("666", 480)], cr=[("5186.credit", 480)],
                 rol="Recunoaștere în luna producerii, fără avans"),
             pas(5, "Verificare",
                 "La dobândă fixă, după 24 de luni: 471 = 0 și 5186 = 0, iar Σ666 = "
                 "12.000. Sold pe 471 după scadență = eșalonarea s-a oprit; sold pe 5186 "
                 "= dobândă datorată și neplătită. Cele două se citesc diferit.",
                 rol="Stare terminală: 471 = 0, 5186 = 0, cheltuiala pe lunile ei"),
         ]),

    flux("F-87", "Dobânzi de încasat (5187 → 472 → 766)", didactic=True,
         roluri="Creanță + Venit amânat",
         conturi="5187, 472, 766, 5121",
         note="Oglinda lui F-505, dar pe conturi de activ. Ține de politica fiecărei "
              "societăți CÂND se face recunoașterea, nu DACĂ.",
         principiu="Creanța de dobândă și venitul amânat se recunosc CONCOMITENT — nu "
                   "una fără cealaltă. Recunoscută doar creanța, ai un activ fără "
                   "contrapartidă; recunoscut doar venitul, ai venit fără drept.",
         pasi=[
             pas(1, "Contract de depozit / plasament",
                 "Dobândă de încasat de 3.000 lei, aferentă perioadei curente.",
                 dr=[("5187.plasament", 3000)], cr=[("472.dobanda", 3000)],
                 rol="Pas revelator: creanța și venitul amânat, în aceeași notă",
                 revelator=True),
             pas(2, "Notă contabilă — recunoașterea venitului",
                 "Venitul se trece la rezultat pe măsura perioadei la care se referă.",
                 dr=[("472.dobanda", 3000)], cr=[("766", 3000)],
                 rol="Venit financiar al perioadei"),
             pas(3, "Extras de cont",
                 "Încasarea. Pasul ăsta lipsea din notițe — fără el, 5187 rămâne cu sold "
                 "și pare creanță neîncasată la infinit.",
                 dr=[("5121", 3000)], cr=[("5187.plasament", 3000)],
                 rol="Stingerea creanței"),
             pas(4, "Verificare",
                 "Sold 5187 = 0, sold 472 = 0, Σ766 = 3.000. Sold pe 5187 după scadență "
                 "= dobândă neîncasată; sold pe 472 după perioadă = venit nerecunoscut.",
                 rol="Stare terminală: 5187 = 0 și 472 = 0"),
         ]),

    flux("F-88", "Linie de credit (5191) vs. credit cu scadențar", didactic=True,
         roluri="Datorie pe termen scurt, fără scadențar",
         conturi="5191, 5121, 666, 1621",
         note="La linie se cere SOLDUL de la sfârșit de lună — e singura verificare "
              "independentă disponibilă.",
         principiu="La un credit cu scadențar, dacă înregistrezi rata în loc de dobândă "
                   "te uiți în scadențar și îți dai seama. La linia de credit nu ai la "
                   "ce să te uiți: extrasele au explicații evazive, diferă de la o bancă "
                   "la alta, iar unele nici nu afișează sold intermediar. Fără extrasul "
                   "de linie cerut clientului, se operează totul prin 5121 și se ratează "
                   "dobânda — iar cheltuiala nedeclarată înseamnă impozit pe profit "
                   "plătit în plus.",
         pasi=[
             pas(1, "Contract de linie de credit",
                 "Linie de 100.000 lei, reînnoibilă anual. Nu are scadențar: tragi și "
                 "restitui de câte ori vrei, și plătești doar ce utilizezi.",
                 rol="Starea inițială: facilitate disponibilă, nefolosită"),
             pas(2, "Extras de cont — tragere",
                 "Se trag 10.000 lei pentru plata unui furnizor.",
                 dr=[("5121", 10000)], cr=[("5191.linia1", 10000)],
                 rol="Naște datoria pe termen scurt"),
             pas(3, "Extras de cont — restituire parțială",
                 "Se restituie 9.000 lei. Soldul rămâne 1.000 lei tras.",
                 dr=[("5191.linia1", 9000)], cr=[("5121", 9000)],
                 rol="Stingere parțială"),
             pas(4, "Extras de linie de credit, la sfârșit de lună",
                 "Documentul care se CERE clientului, separat de extrasul de cont. "
                 "Dobânda de 180 lei se citește de acolo — din extrasul obișnuit s-ar "
                 "duce, împreună cu restituirea, în 5191.",
                 dr=[("666", 180)], cr=[("5121", 180)],
                 rol="Pas revelator: fără extrasul de linie, dobânda ajunge în 5191 și "
                     "dispare din cheltuieli",
                 revelator=True),
             pas(5, "Verificare",
                 "Sold 5191.linia1 = 1.000 creditor, egal cu soldul confirmat de bancă. "
                 "⚠ 5191 NU ajunge niciodată cu sold debitor: e cont de pasiv, iar un "
                 "sold debitor înseamnă că s-a restituit mai mult decât s-a tras. "
                 "Analitic pe fiecare linie — două linii pe același cont nu se mai pot "
                 "reconcilia cu extrasele.",
                 rol="Stare terminală: sold 5191 = soldul confirmat de bancă, creditor"),
         ]),

    flux("F-89", "Tichete de masă: 5328 → 6422", didactic=True,
         roluri="Stoc de trezorerie până la acordare",
         conturi="5328, 401, 6422, 421, 4315, 444",
         note="⚠ Notițele scriau contul ca `5238`, care nu există — grupa 52 nu există "
              "deloc. Denumirea lui 5328 în OMFP e „Alte valori”: planul nu are cont "
              "dedicat tichetelor.",
         principiu="Tichetele cumpărate nu sunt cheltuială: sunt STOC DE TREZORERIE "
                   "până în ziua în care ajung la salariat. Cheltuiala se naște la "
                   "acordare, pe statul de plată, pentru că abia atunci se știe cine a "
                   "fost efectiv la lucru — nu se acordă pentru zilele de concediu.",
         pasi=[
             pas(1, "Factură de la emitentul de tichete",
                 "Se cumpără tichete de 5.000 lei. Nu e cheltuială încă: e valoare în "
                 "trezorerie, ca banii din casă.",
                 dr=[("5328.masa", 5000)], cr=[("401.emitent", 5000)],
                 rol="Intrarea în stocul de trezorerie"),
             pas(2, "Ordin de plată",
                 "Plata furnizorului de tichete.",
                 dr=[("401.emitent", 5000)], cr=[("5121", 5000)],
                 rol="Stingerea datoriei"),
             pas(3, "Stat de plată",
                 "Acordarea efectivă, la sfârșitul lunii. Se dau 4.600 lei — restul "
                 "corespunde zilelor de concediu, pentru care nu se acordă.",
                 dr=[("6422", 4600)], cr=[("5328.masa", 4600)],
                 rol="Pas revelator: cheltuiala se naște la acordare, nu la cumpărare",
                 revelator=True),
             pas(4, "Stat de plată — fiscalizarea",
                 "Tichetele intră în baza impozitului pe venit (10%) și în baza CASS "
                 "(10%), dar NU în baza CAS și NU în baza CAM. Pe 4.600 lei: 460 impozit "
                 "și 460 CASS.",
                 dr=[("421", 920)], cr=[("444", 460), ("4315", 460)],
                 rol="Rețineri din drepturile salariale"),
             pas(5, "Verificare",
                 "Sold 5328 = 400 lei — tichete cumpărate și neacordate, care se acordă "
                 "luna următoare. Contul se verifică LUNAR, nu trimestrial: la fiecare "
                 "lună trecută devine mai greu de spus cui i se cuveneau. Regula de "
                 "acordare: doar la funcția de BAZĂ — o normă de 4 ore poate fi funcție "
                 "de bază, dar dintre două contracte de 8 ore doar unul poate fi.",
                 rol="Stare terminală: 5328 = tichetele neacordate, verificat lunar"),
         ]),
]
