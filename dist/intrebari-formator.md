# Întrebări rămase deschise după trainingurile 2, 3 și 4

Cele **21 de întrebări** de mai jos s-au acumulat la revizuirea notițelor din 07.08.2026 (capitaluri), 12.08.2026 (imobilizări) și 14.08.2026 (stocuri și TVA).

Sunt grupate pe **temă contabilă**, nu pe training, ca să nu răspundeți de trei ori la aceeași chestiune în trei contexte diferite. Fiecare întrebare vine cu contextul din notițe, ca să nu fie nevoie de recitire.

Sub fiecare întrebare, **„Ce am presupus”** spune ce am ales acolo unde a trebuit să aleg ca să pot merge mai departe. Acelea sunt exact locurile unde un răspuns diferit schimbă ce e deja construit.

---

## Dacă aveți timp doar pentru trei

- **Ne puteți da procedura scrisă de reconciliere, pentru cazul în care analiticul din balanța contabilă nu corespunde cu registrul mijloacelor fixe?**  
  Blochează singurul flux de procedură din sistem (F-214) și corelația C-15.

- **TVA nedeductibilă de pe rata de capital la leasingul financiar: se capitalizează în valoarea mijlocului fix (2133) sau se trece pe cheltuială (635 / 6588)?**  
  Schimbă valoarea de intrare a mijlocului fix, deci amortizarea și impozitul pe profit pe toată durata contractului.

- **Care este baza legală exactă pentru a trata ca nedeductibilă diferența dintre valoarea rămasă și prețul de vânzare, față de art. 28 alin. (17)?**  
  E testul central al MOD_IESIRE_MF; azi semnalează un risc fără să poată cita articolul pe care se sprijină.

---

## Repartizarea rezultatului și rezultatul reportat

### 1. Care este temeiul legal al termenului de 3 ani pentru a decide ce se face cu soldul rămas în 1171?

**Context.** Notițele spuneau: „1171 → decis, în curs de 3 ani, ce face cu diferența dintre 250 și 125 lei” — deci profitul reportat ar trebui repartizat într-un interval de trei ani. Nu am găsit termenul ăsta în Legea 31/1990 și nici în Codul fiscal.

**De ce contează.** F-103 (repartizarea rezultatului) și MOD_CAPITALURI. Dacă termenul există, modulul ar trebui să semnaleze soldurile 1171 mai vechi de 3 ani; dacă nu, semnalarea ar fi un fals pozitiv la fiecare client cu profit nerepartizat.

**Ce am presupus.** Nu l-am implementat. MOD_CAPITALURI raportează soldul 1171 pe an, prin C-21, fără să-l judece după vechime.

<sub>sursa: training 07.08.2026, întrebarea 1</sub>


### 2. În exemplul cu rezerva legală, profitul era 250 sau 2.500 lei?

**Context.** Notițele au „121 = 250 lei” și imediat „129 - 1061 = 125 lei”. Dar 5% din 250 înseamnă 12,50 lei, nu 125. Cifrele se leagă doar dacă profitul era 2.500.

**De ce contează.** F-103 și MOD_CAPITALURI folosesc exemplul ca test. Am nevoie să știu dacă a fost o scăpare de notare sau dacă mi-a scăpat mie o regulă de calcul.

**Ce am presupus.** Am folosit 2.500 lei, singura variantă în care 5% dau 125. Dacă profitul chiar era 250, atunci procentul aplicat nu era 5% și trebuie relămurit.

<sub>sursa: training 07.08.2026, întrebarea 2</sub>


### 3. Pierderile nedeductibile fiscal se urmăresc pe analitic al lui 1171 sau pe alt cont?

**Context.** Notițele: „sunt anumite pierderi care nu sunt deductibile fiscal — astea se înregistrează într-un cont separat”. Nu s-a spus care.

**De ce contează.** C-21 cere ca 1171 să aibă analitic pe an, cu sensul debitor/creditor explicit. Dacă pierderea nedeductibilă are cont propriu, corelația trebuie extinsă, iar recuperarea în 5 ani (70% din profitul impozabil) se urmărește altfel.

**Ce am presupus.** Am lăsat 1171 cu analitic pe an, fără separare a pierderii nedeductibile.

<sub>sursa: training 07.08.2026, întrebarea 4</sub>


### 4. Care este actul normativ care a permanentizat termenul de 25 iunie pentru D101?

**Context.** Notițele anunțau pentru 2027 „101 în Martie, bilanț în mai”. Termenul s-a mutat însă la 25 iunie, iar în documentul revizuit am marcat asta ca schimbare — dar fără să pot cita actul care o face permanentă, nu doar valabilă pentru un an.

**De ce contează.** Checklistul de închidere din documentele revizuite și calendarul din foaia Legendă. Un termen greșit aici se propagă la toți clienții.

**Ce am presupus.** Am scris 25 iunie, marcat ca „de reconfirmat”.

<sub>sursa: training 07.08.2026, întrebarea 6</sub>


## Corectarea erorilor din exerciții anterioare

### 5. Cum se tratează o factură a exercițiului anterior, descoperită neînregistrată în anul curent — și când se folosește 1174 în loc de 628 cu semn schimbat?

**Context.** Notițele conțineau întrebarea ca atare, fără răspuns, plus observația că 1174 „a fost introdus ca să nu mai denaturăm profitul anilor” și că „lucrurile se complică atunci când nu mai am sold în 1171, pentru că proprietarul a decis să ia dividende”.

**De ce contează.** F-105 (corecția erorilor prin 1174) și MOD_CAPITALURI. Pragul de semnificație din politicile contabile decide între cele două căi, dar nu știu ce prag folosește cabinetul.

**Ce am presupus.** Am construit arborele de decizie pe pragul de semnificație, cu 1174 pentru erorile semnificative din exerciții închise și corecția pe cheltuiala curentă sub prag. C-18 cere ca 1174 să ajungă la zero la 31.12.

<sub>sursa: training 07.08.2026, întrebarea 5</sub>


## Capital social și activ net

### 6. Cum se documentează reîntregirea activului net cerută de Legea 239/2025 — prin conversia creanței asociatului în capital sau prin aport nou?

**Context.** Legea condiționează dividendele și restituirile de împrumuturi de un activ net de cel puțin jumătate din capitalul social. Notițele semnalau problema, fără procedura de ieșire din blocaj.

**De ce contează.** C-20 (testul de activ net) și MOD_CAPITALURI, care azi doar semnalează blocajul. Ca să propună o cale de rezolvare, are nevoie de varianta preferată a cabinetului.

**Ce am presupus.** Modulul semnalează blocajul și se oprește acolo — nu propune nicio soluție.

<sub>sursa: training 07.08.2026, întrebarea 7</sub>


### 7. Verificăm sistematic pragul de capital social minim (500 / 5.000 lei) pe tot portofoliul de clienți, sau doar la firmele noi?

**Context.** Pragurile noi din 2026: 500 lei la înființare, 5.000 lei la cifră de afaceri netă peste 400.000 lei. Al doilea prag prinde firme existente, nu doar noi.

**De ce contează.** F-101 (constituirea capitalului) și checklistul de deschidere de dosar. Dacă verificarea e sistematică, intră în checklistul lunar, nu în cel de deschidere.

**Ce am presupus.** Am pus-o în checklistul de deschidere a dosarului.

<sub>sursa: training 07.08.2026, întrebarea 8</sub>


## Leasing și vehicule

### 8. TVA nedeductibilă de pe rata de capital la leasingul financiar: se capitalizează în valoarea mijlocului fix (2133) sau se trece pe cheltuială (635 / 6588)?

**Context.** Notițele arătau capitalizarea TVA nededuse de pe AVANS în valoarea de intrare (150.000 + 5.250 = 155.250), dar pentru ratele lunare foloseau 6588. Practica e împărțită și în literatură.

**De ce contează.** F-108 și MOD_LEASING_FIN. E singura variabilă a modulului care schimbă valoarea de intrare a mijlocului fix, deci și amortizarea, deci și impozitul pe profit pe toată durata contractului.

**Ce am presupus.** Am făcut din ea o OPȚIUNE DE CONFIGURARE în modul (CAPITALIZEAZA / CHELTUIALA), cu implicit „capitalizează”, coerent cu tratamentul avansului. Nu am tranșat-o ca regulă.

<sub>sursa: training 07.08.2026, întrebarea 3</sub>


## Imobilizări — prag și amortizare

### 9. Recomandați alinierea pragului contabil de recunoaștere la cel fiscal (5.000 lei), sau menținerea unui prag intern mai mic pentru control de gestiune?

**Context.** OUG 8/2026 a urcat pragul fiscal la 5.000 lei. Pragul contabil rămâne la latitudinea entității, prin politici contabile.

**De ce contează.** MOD_IMOBILIZARI face un test de prag la intrare. Dacă cele două praguri diferă, apar diferențe temporare de urmărit în registrul de evidență fiscală — un lucru pe care modulul nu îl tratează azi.

**Ce am presupus.** Am folosit un singur prag, cel fiscal, și am semnalat în notițe că divergența produce diferențe temporare.

<sub>sursa: training 12.08.2026, întrebarea 1</sub>


### 10. Excepția de la cumulul cu profitul reinvestit (art. 22 alin. 9) acoperă doar amortizarea accelerată, sau și pe cea superaccelerată de 65%?

**Context.** Notițele spuneau despre amortizarea accelerată că „nu poate să mai fie aplicată o altă facilitate fiscală = reducere pentru profitul reinvestit”, cu recomandarea de a calcula ce e mai avantajos.

**De ce contează.** F-204 și MOD_IMOBILIZARI, la alegerea metodei de amortizare. Dacă excepția nu acoperă superaccelerata, calculul comparativ are altă concluzie.

**Ce am presupus.** Nu am implementat comparația. Modulul propune metoda, fără să optimizeze fiscal.

<sub>sursa: training 12.08.2026, întrebarea 2</sub>


## Imobilizări — ieșiri din gestiune

### 11. Care este baza legală exactă pentru a trata ca nedeductibilă diferența dintre valoarea rămasă și prețul de vânzare, față de art. 28 alin. (17)?

**Context.** Notițele: la vânzarea cu 50.000 a unei clădiri cu valoare rămasă 70.000, „50k cheltuieli deductibile, 20k cheltuieli nedeductibile”, cu excepția cazului în care există dovezi (clădire avariată, deviz de service). Citit strict, art. 28 alin. (17) include pierderea în rezultatul fiscal.

**De ce contează.** F-211 și MOD_IESIRE_MF. E testul central al modulului: azi calculează diferența și cere documentul justificativ, dar nu poate cita articolul pe care se sprijină.

**Ce am presupus.** Modulul semnalează riscul și cere documentarea prețului, invocând art. 11 (reîncadrare) și art. 25 alin. (1) (scopul activității economice) — nu art. 28.

<sub>sursa: training 12.08.2026, întrebarea 3</sub>


### 12. La o casare din care nu rezultă nici deșeuri, nici piese reutilizabile, cum se justifică deductibilitatea valorii rămase neamortizate?

**Context.** Notițele tratau cazul cu valorificare (piese pe 3024, venit pe 7588), dar nu și pe cel fără nicio recuperare.

**De ce contează.** F-212 (casarea) și MOD_IESIRE_MF, unde valoarea pieselor recuperate poate fi zero. Fără răspuns, modulul nu poate spune dacă procesul-verbal de scoatere din funcțiune e suficient singur.

**Ce am presupus.** Modulul acceptă valoarea zero a recuperărilor și lasă deductibilitatea nejudecată, cu procesul-verbal ca singur document.

<sub>sursa: training 12.08.2026, întrebarea 5</sub>


## Imobilizări — control și raportare

### 13. În secțiunea Active din D406 (SAF-T) se raportează și 231 (investiții neterminate), și 261 (imobilizări financiare)?

**Context.** Notițele menționau că informația din modulul de imobilizări „merge în 406”, fără să delimiteze ce anume intră.

**De ce contează.** Coloana Declarativ a fluxurilor F-208 (imobilizări în curs) și F-213 (imobilizări financiare). Azi nu marchez D406 pe ele, ca să nu afirm ceva greșit.

**Ce am presupus.** Le-am lăsat nemarcate în coloana Declarativ.

<sub>sursa: training 12.08.2026, întrebarea 4</sub>


### 14. Ne puteți da procedura scrisă de reconciliere, pentru cazul în care analiticul din balanța contabilă nu corespunde cu registrul mijloacelor fixe?

**Context.** Ultimul punct al trainingului 3, rămas nefinalizat: „am verificat analiticul cu sinteticul → am verificat firma X, avem în 212 x lei, dar în balanța contabilă / imobilizări am x, y, z → să vedem o procedură, ce e de făcut.” Formatorul a promis-o și sesiunea s-a încheiat înainte.

**De ce contează.** F-214 este singurul flux de PROCEDURĂ din tot sistemul — nu produce note contabile, descrie un control lunar. Azi se oprește la „dacă soldurile nu corespund”, fără pașii de rezolvare. C-15 depinde de aceeași procedură.

**Ce am presupus.** Am scris pașii de identificare (listing, comparare pe perechi 21x↔28x, fișă de cont), dar NU și pașii de corecție — aceia sunt procedura promisă.

<sub>sursa: training 12.08.2026, întrebarea 6 — PUNCTUL CEL MAI IMPORTANT</sub>


## Stocuri și producție

### 15. Care sunt celelalte metode de calculație a costurilor acceptate de OMFP 1802/2014, și în ce situații se alege fiecare?

**Context.** Notițele menționau metoda pe comenzi ca fiind cea mai utilizată, în contextul producției de termopane. Celelalte (pe faze, pe produs, standard-cost) au rămas doar enumerate.

**De ce contează.** F-311 (producția multi-stadiu) ține gestiunea lui 331 analitic pe comandă. Pe faze, structura analitică e alta, deci și fluxul.

**Ce am presupus.** Am implementat doar metoda pe comenzi.

<sub>sursa: training 14.08.2026, întrebarea 1</sub>


## TVA — import, vamă, taxare inversă

### 16. La decontarea cu comisionarul vamal folosiți 446 sau 462? Care e standardul cabinetului și de ce?

**Context.** Notițele foloseau 446, cu observația proprie că „e o înregistrare puțin forțată, pentru că e un cont de pasiv”. Unele cabinete folosesc 461/462.

**De ce contează.** F-319 (import prin comisionar) și analiticul 446.VAMA din foaia Analitice. Contul ales determină unde apare soldul în bilanț: datorie la buget vs. datorie către un terț.

**Ce am presupus.** Am păstrat 446.VAMA, ca în notițe, și am notat 461/462 ca alternativă.

<sub>sursa: training 14.08.2026, întrebarea 3</sub>


### 17. Verificăm sistematic dacă clienții importatori îndeplinesc condițiile pentru certificatul de amânare de la plata TVA în vamă?

**Context.** Certificatul înlocuiește plata efectivă a TVA în vamă cu taxare inversă (4426 = 4427) — avantaj mare de cash-flow. Notițele nu îl menționau deloc; l-am adăugat eu la revizuire.

**De ce contează.** F-320 (import cu plată directă) capătă o a treia variantă dacă certificatul există. Ar trebui să intre în checklistul de deschidere a dosarului.

**Ce am presupus.** L-am adăugat ca variantă în documentul revizuit, dar nu în checklist.

<sub>sursa: training 14.08.2026, întrebarea 4</sub>


### 18. Derogarea UE pentru taxarea inversă la cereale și electronice avea termen 31.12.2026 — a fost prelungită?

**Context.** Art. 331 alin. (6) limitează în timp o parte din categorii, iar Consiliul UE a prelungit derogarea succesiv. Nu se poate presupune prelungirea automată.

**De ce contează.** F-402 (taxare inversă internă) și lista de categorii din documentul revizuit. Aplicarea taxării inverse după expirare înseamnă factură greșit întocmită.

**Ce am presupus.** Am marcat termenul în document cu avertisment de reverificare.

<sub>sursa: training 14.08.2026, întrebarea 7</sub>


## TVA — ajustări fără document

### 19. La lipsa la inventar, practica implicită a cabinetului este colectarea de TVA sau ajustarea dreptului de deducere? Ce set de documente se cere clientului?

**Context.** Notițele spuneau simplu „trebuie să colectez și TVA”. La revizuire am găsit că tratamentul diferă: lipsă imputabilă → colectare; neimputabilă nejustificată → ajustare; bunuri distruse cu documente → fără ajustare.

**De ce contează.** F-406 (înregistrări fără document) și corelațiile C-03 / C-04, unde ajustările care nu vin din facturi trebuie să apară în jurnale cu semnul corect. Cele două tratamente ating conturi diferite, deci și jurnale diferite.

**Ce am presupus.** Am descris toate patru situațiile, fără să declar una ca implicită.

<sub>sursa: training 14.08.2026, întrebarea 2</sub>


## Obligații de mediu

### 20. Care este termenul curent de depunere a declarației la Fondul pentru Mediu — lunar sau trimestrial?

**Context.** Notițele nu dădeau termenul, iar acesta s-a modificat de mai multe ori. La revizuire am scris „verifică termenul curent pe afm.ro”, ceea ce nu e un răspuns.

**De ce contează.** F-310 (ambalaje și taxa AFM) și checklistul lunar. Un termen greșit produce penalități direct.

**Ce am presupus.** Am lăsat termenul nespecificat, cu trimitere la sursa oficială.

<sub>sursa: training 14.08.2026, întrebarea 5</sub>


## Material lipsă din notițe

### 21. Ce fișier și ce sarcină erau în spatele notițelor „Fișierul atașat arată corelații importante între conturi” și „task”?

**Context.** Ambele au rămas fără conținut în notițele originale — un rând care trimite la un atașament și un rând cu un singur cuvânt, „task”.

**De ce contează.** Fișierul cu corelații ar putea conține exact materialul din foaia „Corelații de control”, care azi are 22 de corelații construite de mine. Dacă există o listă a formatorului, merită confruntată cu a mea.

**Ce am presupus.** Am construit corelațiile din notițe și din practică, fără fișierul original.

<sub>sursa: training 14.08.2026, întrebarea 6</sub>


---

*21 de întrebări, 12 teme. Generat din notițele revizuite; fiecare întrebare se poate urmări înapoi la training și la numărul ei original.*
