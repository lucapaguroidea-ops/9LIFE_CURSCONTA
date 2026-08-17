"""Conturi din clasele 1 și 2 promovate la Tier A, cu structura analitică justificată.

Format identic cu foaia `Analitice (Tier A)` din workbook-ul original:
Simbol · Denumire · Structură analitică recomandată · Factor(i) · Ce se rupe dacă
lipsește · Notă SAGA / Declarații · Flux legat.

Factori: D declarativ · N normativ · C corelație · F fiscal · B bilanț · V valută · O operațional.
Regula de igienă din Legendă: fără factor → fără recomandare.
"""

ANALITICE = [
    dict(simbol="456", denumire="Decontări cu acționarii/asociații privind capitalul",
         structura="456 pe fiecare ASOCIAT",
         factor="O",
         rupe="Nu poți justifica cine ce datorează; vărsămintele parțiale devin neurmăribile",
         nota="Se închide la vărsare. Sold 456 ≠ 0 la 31.12 = capital subscris nevărsat.",
         flux="F-45"),
    dict(simbol="101", denumire="Capital",
         structura="1011 subscris nevărsat / 1012 subscris vărsat [N]",
         factor="N C",
         rupe="Plafonul rezervei legale (20%) se calculează greșit — se aplică la capitalul "
              "subscris ȘI VĂRSAT, deci partea din 1011 nu intră",
         nota="Prag minim L. 239/2025: 500 lei firme noi, 5.000 lei la CA netă > 400.000 lei.",
         flux="F-45, F-46"),
    dict(simbol="105", denumire="Rezerve din reevaluare",
         structura="105 pe fiecare ACTIV și fiecare reevaluare",
         factor="C F",
         rupe="Nu poți proba impozitarea corelată cu amortizarea, nici ce sumă e distribuibilă",
         nota="Surplusul realizat trece în 1175. Nu poate majora capitalul social (art. 210 alin. 3 L. 31/1990).",
         flux="F-48"),
    dict(simbol="1061", denumire="Rezerve legale",
         structura="1061 (sintetic e suficient; plafonul se urmărește față de 1012)",
         factor="N F",
         rupe="Depășirea plafonului de 20% din capitalul vărsat sau a limitei de 5% din profitul "
              "contabil brut → partea în plus e nedeductibilă",
         nota="Bază fiscală = sold creditor 121 + rulaj 691 (art. 26 alin. 1 lit. a CF).",
         flux="F-46"),
    dict(simbol="117", denumire="Rezultatul reportat",
         structura="1171 PE AN, cu sens D/C explicit · 1174 corecții · 1175 surplus reevaluare [N]",
         factor="N F B",
         rupe="Recuperarea pierderii (70% din profitul impozabil, 5 ani) devine neurmăribilă; "
              "plafonul de dividende distribuibile iese supraevaluat",
         nota="1174 e TRANZITORIU — nu poate rămâne cu sold la 31.12 (C-18). "
              "Pentru pierderea nerecuperabilă fiscal se folosește un analitic de gestiune, "
              "nu un sintetic distinct (nu există).",
         flux="F-46, F-47, F-48"),
    dict(simbol="129", denumire="Repartizarea profitului",
         structura="129 (sintetic)",
         factor="C",
         rupe="Sold 129 rămas după repartizare = închidere omisă; corelația C-16 nu ține",
         nota="Sold DEBITOR: se închide prin creditare (`121 = 129`), nu invers.",
         flux="F-46"),
    dict(simbol="151", denumire="Provizioane",
         structura="1511 litigii · 1512 garanții clienți · 1514 restructurare · 1516 impozite · "
                   "1518 alte provizioane [N]",
         factor="N F",
         rupe="Provizionul nu poate fi utilizat pentru altă cheltuială decât cea pentru care a fost "
              "constituit — fără analitic pe motiv, regula devine neverificabilă",
         nota="Litigiile sunt NEDEDUCTIBILE (art. 26 CF, listă limitativă); reluarea pe 7812 = venit neimpozabil.",
         flux="F-51"),
    dict(simbol="162x", denumire="Credite bancare pe termen lung",
         structura="1621…1627 sunt SINTETICE distincte + analitic pe contract și pe VALUTĂ · "
                   "1682 dobânzi neajunse la scadență",
         factor="V B",
         rupe="Reevaluarea lunară se face la curs greșit; porțiunea curentă (≤ 12 luni) nu se poate "
              "reclasifica pentru bilanț",
         nota="Reevaluare LUNARĂ obligatorie (OMFP 1802/2014). Verifică soldul în valută: "
              "sold valută × curs BNR = sold lei.",
         flux="F-49"),
    dict(simbol="167", denumire="Alte împrumuturi și datorii asimilate (leasing financiar)",
         structura="167 PE CONTRACT — 1 la 1 cu contractul, indiferent câte bunuri conține — "
                   "și pe tip de VALUTĂ",
         factor="C V O",
         rupe="Nu mai știi la ce rată din scadențar te raportezi → reevaluarea soldului se face greșit; "
              "corelația C-19 nu se poate verifica",
         nota="Avansul (4093) se închide în 167 la recepție. Impozitul local e datorat de LOCATAR "
              "pe toată durata contractului.",
         flux="F-50"),
    dict(simbol="205 / 208", denumire="Concesiuni, brevete, licențe, mărci / Alte imobilizări necorporale",
         structura="205 pe titlu (marcă, licență) · 208 pe program",
         factor="O",
         rupe="Duratele diferite (mărci 10 ani, softuri uzual 3 ani) nu se pot urmări pe același sintetic",
         nota="Amortizare: 6811 = 2805 / 2808. Contul 7815 din notițe NU există.",
         flux="F-52"),
    dict(simbol="211", denumire="Terenuri și amenajări de terenuri",
         structura="2111 terenuri, pe CATEGORIE DE FOLOSINȚĂ (arabil, curți-construcții, "
                   "în curs de construcții) · 2112 amenajări [N]",
         factor="N F O",
         rupe="Tratamentul fiscal la vânzare diferă pe categorie; amenajarea (amortizabilă) se "
              "confundă cu terenul (neamortizabil)",
         nota="2111 nu are cont de amortizare. 2112 se amortizează pe 10 ani, cont pereche 2811.",
         flux="F-53"),
    dict(simbol="212 / 213 / 214 / 215", denumire="Construcții / Instalații și mijloace de transport / "
                                                  "Mobilier și birotică / Investiții imobiliare",
         structura="analitic PE MIJLOC FIX, cu COD DE CLASIFICARE din catalog și durată",
         factor="N C D O",
         rupe="Durata de amortizare se calculează greșit; oglinda cu 28x (C-14) și confruntarea cu "
              "registrul MF (C-15) devin imposibile; D406/SAF-T incomplet",
         nota="Codul de clasificare se trece în modulul de mijloace fixe — alimentează D406. "
              "Clădirile au obligatoriu amortizare liniară.",
         flux="F-54, F-55, F-56, F-59"),
    dict(simbol="223 / 224", denumire="Imobilizări corporale în curs de aprovizionare",
         structura="223 → 213 · 224 → 214 (tranzit)",
         factor="O",
         rupe="Bun facturat nerecepționat fie dispare din evidență, fie se amortizează deși nu există fizic",
         nota="Oglinda lui 32x, pe imobilizări. Se stinge la procesul-verbal de recepție.",
         flux="F-57"),
    dict(simbol="231 / 233", denumire="Imobilizări corporale / necorporale în curs de execuție",
         structura="analitic PE OBIECTIV de investiții",
         factor="C O B",
         rupe="La 31.12 nu poți spune ce e în sold (C-22); obiectivele finalizate rămân neamortizate",
         nota="Prestațiile terților merg în 231, NU pe 628. Salariile proprii se capitalizează prin "
              "722 (corporale) / 721 (necorporale). 235 = Investiții imobiliare în curs.",
         flux="F-52, F-58"),
    dict(simbol="26x", denumire="Imobilizări financiare",
         structura="261 pe entitate · 267 pe PARTENER și CONTRACT",
         factor="O B",
         rupe="Garanțiile recuperabile peste ani devin neidentificabile; ajungi să scoți fișe de cont "
              "pe 3–5 ani",
         nota="Relevant mai ales la preluarea unei firme noi care ține totul pe un singur analitic.",
         flux="F-62"),
    dict(simbol="28x", denumire="Amortizări privind imobilizările",
         structura="analitic PE MIJLOC FIX, în oglindă cu contul de activ",
         factor="C N",
         rupe="C-13 (28x ≤ 21x) și C-14 (oglinda) nu se pot verifica; amortizarea rămâne pe mijloace ieșite",
         nota="2813 deservește mai multe conturi (2131, 2132, 2133, 2134) — atenție la confruntare. "
              "Verifică nota de amortizare în PRIMA lună.",
         flux="F-54, F-59, F-60, F-61"),
    dict(simbol="4093", denumire="Avansuri acordate pentru imobilizări corporale",
         structura="4093 pe contract / furnizor",
         factor="C O",
         rupe="Avansul rămâne nestins după recepție → valoarea de intrare și soldul 167 sunt greșite",
         nota="Se închide în 167 (leasing) sau în 404 (achiziție directă) la recepție.",
         flux="F-50"),
    dict(simbol="6583 / 7583", denumire="Cheltuieli / Venituri din cedarea activelor",
         structura="analitic pe operațiune de cedare",
         factor="F",
         rupe="Testul de deductibilitate (valoare rămasă vs. venit din vânzare) nu se poate documenta",
         nota="6583 deductibil în limita venitului din vânzare; diferența e nedeductibilă fără "
              "documentarea prețului (raport de evaluare / referință de piață / deviz de service).",
         flux="F-59, F-60"),
    dict(simbol="666 / 628 / 613", denumire="Dobânzi / Comisioane / Prime de asigurare — vehicule",
         structura="analitic .NED pentru partea nedeductibilă (ex. 666.NED, 628.NED, 613.NED)",
         factor="F",
         rupe="Limitarea de 50% (art. 25 alin. 3 lit. l CF) nu se poate proba la control; "
              "D101 iese greșit",
         nota="Baza include TVA nedeductibilă deja trecută pe cheltuială. "
              "⚠ Contul nedeductibil pentru CASCO este 613.NED, NU 615 (= pregătirea personalului).",
         flux="F-50"),
    dict(simbol="665 / 765", denumire="Diferențe de curs valutar",
         structura="analitic pe tip de element (credite, furnizori, clienți, trezorerie)",
         factor="V F",
         rupe="Nu poți separa diferențele la plată de cele din reevaluarea lunară; "
              "la vehicule, diferențele intră în baza limitării de 50%",
         nota="Două momente: la plată și la reevaluarea lunară a soldului (ultima zi bancară).",
         flux="F-49, F-50"),
    dict(simbol="721 / 722", denumire="Venituri din producția de imobilizări",
         structura="721 necorporale · 722 corporale",
         factor="C F",
         rupe="Costurile capitalizate rămân pe cheltuială → rezultat și impozit pe profit denaturate",
         nota="⚠ NU 711 (variația stocurilor). Softul intern = 233 → 721 → 208; "
              "hala în regie proprie = 231 → 722 → 212.",
         flux="F-52, F-58, F-28"),
]
