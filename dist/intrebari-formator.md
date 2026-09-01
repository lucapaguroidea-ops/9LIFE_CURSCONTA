# Întrebări rămase deschise după trainingurile 2, 3 și 4

Cele **21 de întrebări** de mai jos s-au acumulat la revizuirea notițelor din 07.08.2026 (capitaluri), 12.08.2026 (imobilizări) și 14.08.2026 (stocuri și TVA).

Sunt grupate pe **temă contabilă**, nu pe training, ca să nu răspundeți de trei ori la aceeași chestiune în trei contexte diferite. Fiecare întrebare vine cu contextul din notițe, ca să nu fie nevoie de recitire.

Sub fiecare întrebare, **„Ce am presupus”** spune ce am ales acolo unde a trebuit să aleg ca să pot merge mai departe. Acelea sunt exact locurile unde un răspuns diferit schimbă ce e deja construit.

---

## Dacă aveți timp doar pentru trei

- **Ne puteți da procedura scrisă de reconciliere, pentru cazul în care analiticul din balanța contabilă nu corespunde cu registrul mijloacelor fixe?**  
  Blochează singurul flux de procedură din sistem (F-214) și corelația C-15.

- **Care este temeiul legal al termenului de 3 ani pentru a decide ce se face cu soldul rămas în 1171?**  
  F-103 (repartizarea rezultatului) și MOD_CAPITALURI.

- **În exemplul cu rezerva legală, profitul era 250 sau 2.500 lei?**  
  F-103 și MOD_CAPITALURI folosesc exemplul ca test.

---

# Partea I — rămase deschise

**13 întrebări de drept sau de practică la care n-am găsit răspuns cu certitudine.** Astea sunt cele care se trimit.

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


## Corectarea erorilor din exerciții anterioare

### 4. Cum se tratează o factură a exercițiului anterior, descoperită neînregistrată în anul curent — și când se folosește 1174 în loc de 628 cu semn schimbat?

**Context.** Notițele conțineau întrebarea ca atare, fără răspuns, plus observația că 1174 „a fost introdus ca să nu mai denaturăm profitul anilor” și că „lucrurile se complică atunci când nu mai am sold în 1171, pentru că proprietarul a decis să ia dividende”.

**De ce contează.** F-105 (corecția erorilor prin 1174) și MOD_CAPITALURI. Pragul de semnificație din politicile contabile decide între cele două căi, dar nu știu ce prag folosește cabinetul.

**Ce am presupus.** Am construit arborele de decizie pe pragul de semnificație, cu 1174 pentru erorile semnificative din exerciții închise și corecția pe cheltuiala curentă sub prag. C-18 cere ca 1174 să ajungă la zero la 31.12.

<sub>sursa: training 07.08.2026, întrebarea 5</sub>


## Imobilizări — control și raportare

### 5. În secțiunea Active din D406 (SAF-T) se raportează și 231 (investiții neterminate), și 261 (imobilizări financiare)?

**Context.** Notițele menționau că informația din modulul de imobilizări „merge în 406”, fără să delimiteze ce anume intră.

**De ce contează.** Coloana Declarativ a fluxurilor F-208 (imobilizări în curs) și F-213 (imobilizări financiare). Azi nu marchez D406 pe ele, ca să nu afirm ceva greșit.

**Ce am presupus.** Le-am lăsat nemarcate în coloana Declarativ.

<sub>sursa: training 12.08.2026, întrebarea 4</sub>


## Material lipsă din notițe

### 6. Ce fișier și ce sarcină erau în spatele notițelor „Fișierul atașat arată corelații importante între conturi” și „task”?

**Context.** Ambele au rămas fără conținut în notițele originale — un rând care trimite la un atașament și un rând cu un singur cuvânt, „task”.

**De ce contează.** Fișierul cu corelații ar putea conține exact materialul din foaia „Corelații de control”, care azi are 22 de corelații construite de mine. Dacă există o listă a formatorului, merită confruntată cu a mea.

**Ce am presupus.** Am construit corelațiile din notițe și din practică, fără fișierul original.

<sub>sursa: training 14.08.2026, întrebarea 6</sub>


## Trezorerie — convenții de înregistrare

### 7. Dobânda de plătit trece obligatoriu prin 5186, sau `666 = 5121` direct e acceptat în cabinet?

**Context.** Notițele descriu ambele variante fără să spună care e standardul: „5186 = 5121, și, 666 = 5186, în caz că nu vreau să fac direct 666 = 5121”.

**De ce contează.** F-505 arată ambele căi, deci cine îl citește nu află care se folosește. Consecința practică e la verificare: cu 5186, dobânda datorată și neplătită se vede în balanță; direct pe 666, nu se vede deloc până la plată.

**Ce am presupus.** Am scris fluxul cu 5186 ca variantă principală, pentru că păstrează vizibilă datoria, și am notat varianta directă ca alternativă acceptată. Dacă cabinetul are altă convenție, F-505 se ajustează.

<sub>sursa: training 28.08.2026, punctul 5</sub>


### 8. Consumabilele auto nestocate — lichid de parbriz, aditivi — merg pe 6022 împreună cu combustibilul, sau pe 604?

**Context.** Notițele descriu cazul concret al unui bon cu benzină și lichid de parbriz, și lasă alegerea deschisă: „fiecare firmă decide ce și cum, că nu îți ia nimeni gâtul dacă pui lichidul în 6022; corect ar fi lichid de parbriz în 604”.

**De ce contează.** Convenția de înregistrare pe bonurile mixte, care apar lunar la orice firmă cu mașini. Fără o regulă fixată, același bon se înregistrează diferit de la o lună la alta, iar rulajul lui 6022 nu mai spune nimic despre consumul de combustibil.

**Ce am presupus.** Am scris în document criteriul general — se stochează sau nu — care duce lichidul spre 604. Dar formatorul spune explicit că e alegere de firmă, deci convenția trebuie fixată de cabinet, nu dedusă de mine.

<sub>sursa: training 28.08.2026, punctul 7</sub>


## Gestiuni, bonuri de consum și compensări

### 9. Care e monografia completă a răscumpărării de obligațiuni — preț de emisiune vs. preț de răscumpărare, primă sau discount, și curs valutar dacă emisiunea e în valută?

**Context.** Notița spune doar că obligațiunea „se cumpără la un anumit preț, se răscumpără la un anumit preț + cheltuieli la un anumit curs valutar”, cu mențiunea „de detaliat” adresată mie. N-am putut să o detaliez din notițe: nu sunt cifre.

**De ce contează.** Documentul de trezorerie descrie distincția acțiuni/obligațiuni și conturile (505, 506, 161), dar nu are monografie. Fără cifre nu se poate scrie un flux care să treacă porțile 1 și 2.

**Ce am presupus.** Am scris distincția conceptuală și diferența 505 / 506, fără să inventez cifre. UPDATE: fluxul F-115 există acum, cu un exemplu AUTOCONSISTENT construit de mine (emisiune sub par la 95/100, primă 5.000 pe 169, cupon 10%, răscumpărarea și anularea a 200 de titluri proprii cu pierdere de 200 pe 668, plus un tranșon în valută cu diferența de curs pe 665). Trece porțile 1–3, dar cifrele și tratamentul sunt ilustrative, nu dictate de formator — de aceea întrebarea rămâne deschisă până le confirmă.

<sub>sursa: training 28.08.2026, punctul 9</sub>


## Acte de control — 4423 sau 4481

### 10. Sumele stabilite prin decizie de impunere pe TVA se înregistrează în 4423 cu analitic distinct, sau în 4481?

**Context.** Cele două traininguri spun exact invers, la cinci zile distanță. 21.08: „se înregistrează în 4423 cu analitic distinct, tocmai ca să nu ajungă din greșeală în decontul lunii următoare”. 26.08: „nu mă duc prin 4423, pentru că denaturează rulajul curent — și mă duc prin 4481”.

**De ce contează.** F-421 în întregime, corelațiile C-29 și C-33, și structura analitică a lui 4423. Nu e o nuanță de stil: cele două variante dau solduri diferite pe contul pe care decontul de TVA îl reconciliază.

**Ce am presupus.** Am adoptat varianta din 26.08, pentru că e singura care dă un motiv verificabil: un analitic separă EVIDENȚA, dar nu separă SOLDUL, iar decontul se compară pe soldul sintetic al lui 4423. F-421 e rescris pe 4481, cu ❓ pe el. Dacă formatorul confirmă varianta din 21.08, fluxul se întoarce — dar atunci trebuie explicat cum rămâne corelația decont ↔ balanță valabilă, pentru că azi nu văd cum.

<sub>sursa: training 26.08.2026, punctul 3</sub>


## Decontul de TVA și fișa de rol

### 11. Ce rânduri din D300 sunt preluate în fișa de rol: 36 și 37, sau 44 și 45?

**Context.** Notițele afirmă amândouă variantele, în două locuri diferite. Numerele de rând se schimbă între versiunile formularului, deci una dintre ele e dintr-o versiune anterioară.

**De ce contează.** Corelația decont ↔ fișă de rol ↔ balanță. Fără numerele corecte, corelația nu se poate scrie ca formulă, ci doar descrie.

**Ce am presupus.** Am scris corelația pe SOLD, care nu depinde de numerotarea rândurilor, și am marcat rândurile ca deschise.

<sub>sursa: training 21.08.2026, punctul 5</sub>


### 12. La declarațiile care admit rectificare, contează ordinea cronologică a înregistrării facturilor la redepunere?

**Context.** Întrebarea era notată ca presupunere: dacă facturile nu sunt înregistrate cronologic, poate că redepunerea nu mai e posibilă și ar trebui altă metodă de corecție.

**De ce contează.** Procedura de corecție după depunere, pe toate declarațiile care admit rectificativă. Decontul de TVA nu admite, deci acolo întrebarea nu se pune — dar la celelalte, da.

**Ce am presupus.** N-am implementat nimic pe presupunerea asta.

<sub>sursa: training 21.08.2026, punctul 6</sub>


### 13. Care sunt corelațiile complete între D300 și fișa de rol la TVA?

**Context.** Temă lăsată explicit la training. Notițele dau două fragmente: fișa preia rulajul lunii, nu soldul; și ANAF încarcă doar suma lunii, de unde greșeala de a omite TVA-ul neachitat din perioadele precedente.

**De ce contează.** Corelațiile de control pe TVA. Ce avem acum se verifică pe sold; corelația pe rulaj, rând cu rând, are nevoie de structura exactă a fișei de rol.

**Ce am presupus.** Am scris corelația pe sold și am lăsat-o pe cea pe rulaj ca gol declarat — n-am fișă de rol de citit.

<sub>sursa: training 21.08.2026, punctul 7</sub>


# Partea a II-a — decizii de cabinet

**7 întrebări la care nicio sursă publică nu poate răspunde.** Nu sunt lucruri neaflate, sunt alegeri: ce cont folosim, ce prag intern stabilim, ce documente cerem clientului. Răspunsul e o decizie, nu o informație.

---

## Capital social și activ net

### 14. Verificăm sistematic pragul de capital social minim (500 / 5.000 lei) pe tot portofoliul de clienți, sau doar la firmele noi?

**Context.** Pragurile noi din 2026: 500 lei la înființare, 5.000 lei la cifră de afaceri netă peste 400.000 lei. Al doilea prag prinde firme existente, nu doar noi.

**De ce contează.** F-101 (constituirea capitalului) și checklistul de deschidere de dosar. Dacă verificarea e sistematică, intră în checklistul lunar, nu în cel de deschidere.

**Ce am presupus.** Am pus-o în checklistul de deschidere a dosarului.

<sub>sursa: training 07.08.2026, întrebarea 8</sub>


## Imobilizări — control și raportare

### 15. Ne puteți da procedura scrisă de reconciliere, pentru cazul în care analiticul din balanța contabilă nu corespunde cu registrul mijloacelor fixe?

**Context.** Ultimul punct al trainingului 3, rămas nefinalizat: „am verificat analiticul cu sinteticul → am verificat firma X, avem în 212 x lei, dar în balanța contabilă / imobilizări am x, y, z → să vedem o procedură, ce e de făcut.” Formatorul a promis-o și sesiunea s-a încheiat înainte.

**De ce contează.** F-214 este singurul flux de PROCEDURĂ din tot sistemul — nu produce note contabile, descrie un control lunar. Azi se oprește la „dacă soldurile nu corespund”, fără pașii de rezolvare. C-15 depinde de aceeași procedură.

**Ce am presupus.** Am scris pașii de identificare (listing, comparare pe perechi 21x↔28x, fișă de cont), dar NU și pașii de corecție — aceia sunt procedura promisă.

<sub>sursa: training 12.08.2026, întrebarea 6 — PUNCTUL CEL MAI IMPORTANT</sub>


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


## Comportamentul softului la încasarea în plus

### 18. Programul de contabilitate extrage automat TVA-ul din diferența trecută pe 419 la o încasare mai mare decât factura, sau trebuie forțat manual?

**Context.** Suma încasată în plus e TVA-inclusivă: din 5.000 lei ies 4.132,23 bază și 867,77 TVA. Dacă softul nu face extragerea, TVA-ul rămâne necolectat fără ca nimic să semnaleze.

**De ce contează.** F-415 (încasare peste factură) și C-23. Notițele cer explicit contraverificarea lui 4427 după simulare — deci nici formatorul nu presupune că softul o face.

**Ce am presupus.** Am scris fluxul cu extragerea explicită a TVA-ului, ca pas separat, tocmai ca să nu depindă de comportamentul softului.

<sub>sursa: training 19.08.2026, punctul 3</sub>


## Convenții de analitic rămase de fixat

### 19. Care e structura analitică exactă pe 4428 — pe situație și pe cotă?

**Context.** 4428 apare în trei situații cu sensuri diferite: debitor la achiziția pe aviz (4428 = 408), creditor la livrarea pe aviz (418 = 4428) și creditor la mărfuri la preț cu amănuntul (371 = 4428). Notițele cer analitice pe fiecare situație ȘI pe fiecare cotă, dar nu dau nomenclatorul.

**De ce contează.** F-316, F-408 și analiticul Tier A al lui 4428. Workbook-ul folosește azi 4428.AM (amănunt) și 4428.INC (la încasare); pentru avizul de intrare nu există convenție scrisă.

**Ce am presupus.** Am folosit convenția existentă din training 4 și am lăsat avizul de intrare fără analitic propriu — vizibil ca gol în foaia „Închideri periodice”.

<sub>sursa: training 19.08.2026, punctul 4</sub>


### 20. Facturile nesosite pentru imobilizări se țin pe 408 cu analitic sau direct pe 404 cu analitic?

**Context.** Exemplul din notițe folosește 231 = 408, dar furnizorul de imobilizări e 404. Notițele semnalează singure problema și cer stabilirea unei convenții consecvente.

**De ce contează.** F-408 și F-207. Alegerea decide dacă furnizorii de exploatare se amestecă sau nu cu cei de imobilizări în balanța analitică — adică dacă 401/404 mai pot fi verificate separat.

**Ce am presupus.** Am păstrat 408 cu analitic, ca în exemplul din notițe, semnalând alternativa în observația contului.

<sub>sursa: training 19.08.2026, punctul 5</sub>


# Partea a III-a — răspunsuri verificate, de confirmat

**26 întrebări la care am găsit răspuns pe surse publice**, fiecare cu actul normativ citat și data verificării. Nu înlocuiesc confirmarea — o scurtează: în loc de „care e regula?”, întrebarea devine „am citit bine?”.

---

## Repartizarea rezultatului și rezultatul reportat

### 21. Care este actul normativ care a permanentizat termenul de 25 iunie pentru D101?

**Răspuns.** Termenul de 25 iunie **nu a fost de la început permanent**: a venit prin **OUG 153/2020**, care l-a prelungit pentru perioada 2021–2025, odată cu bonificațiile pentru capital propriu pozitiv și în creștere. 2025 a fost ultimul an de aplicare a acelui mecanism, iar termenul uniform de 25 iunie a anului următor se aplică de la 2026. ❓ Actul care l-a permanentizat nu l-am putut identifica cu certitudine — surse îl descriu ca măsură adoptată în 2026, dar fără să-l numească. De confirmat înainte de a-l cita unui client.

**Temei.** OUG 153/2020, art. I — aplicabil 2021–2025. Permanentizarea: act neidentificat.

<sub>verificat pe surse publice la 21.08.2026 — confirmă sau corectează</sub>

**Context.** Notițele anunțau pentru 2027 „101 în Martie, bilanț în mai”. Termenul s-a mutat însă la 25 iunie, iar în documentul revizuit am marcat asta ca schimbare — dar fără să pot cita actul care o face permanentă, nu doar valabilă pentru un an.

**De ce contează.** Checklistul de închidere din documentele revizuite și calendarul din foaia Legendă. Un termen greșit aici se propagă la toți clienții.

<sub>sursa: training 07.08.2026, întrebarea 6</sub>


## Capital social și activ net

### 22. Cum se documentează reîntregirea activului net cerută de Legea 239/2025 — prin conversia creanței asociatului în capital sau prin aport nou?

**Răspuns.** Legea 239/2025 (în vigoare din 18.12.2025), care modifică Legea 31/1990, impune reîntregirea activului net la minimul legal ÎNAINTE de a distribui dividende sau de a restitui creditări/împrumuturi către asociați. Dacă activul net rămâne sub 50% din capitalul subscris și nu se reîntregește în 2 ani de la exercițiul următor celui cu pierderi, societatea are OBLIGAȚIA de a majora capitalul prin CONVERSIA datoriilor către asociați în capital, cu respectarea drepturilor celorlalți asociați. Deci la „conversie sau aport nou”: legea prevede conversia creanței ca remediu implicit obligatoriu; aportul nou e alternativa voluntară de dinainte de a se ajunge acolo. Amendă ANAF 10.000–200.000 lei dacă AGA nu decide.

**Temei.** Legea 239/2025, care modifică Legea 31/1990 (activul net sub 1/2 din capitalul subscris).

<sub>verificat pe surse publice la 01.09.2026 — confirmă sau corectează</sub>

**Context.** Legea condiționează dividendele și restituirile de împrumuturi de un activ net de cel puțin jumătate din capitalul social. Notițele semnalau problema, fără procedura de ieșire din blocaj.

**De ce contează.** C-20 (testul de activ net) și MOD_CAPITALURI, care azi doar semnalează blocajul. Ca să propună o cale de rezolvare, are nevoie de varianta preferată a cabinetului.

<sub>sursa: training 07.08.2026, întrebarea 7</sub>


## Leasing și vehicule

### 23. TVA nedeductibilă de pe rata de capital la leasingul financiar: se capitalizează în valoarea mijlocului fix (2133) sau se trece pe cheltuială (635 / 6588)?

**Răspuns.** **Cheltuială, nu capitalizare.** La leasing, tratamentul diferă de achiziția directă: la cumpărarea internă a unui autoturism, TVA-ul nedeductibil de 50% intră în costul de achiziție, dar la leasing **nu** intră în valoarea mijlocului fix. Se înregistrează pe cheltuială, defalcat după componenta ratei: `635 = 4426` pentru 50% din TVA aferent ratei de capital, `666 = 4426` pentru cel aferent dobânzii, `628 = 4426` pentru cel aferent comisionului.

**Temei.** Cod fiscal art. 298 (limitarea la 50%) coroborat cu OMFP 1802/2014 privind costul de achiziție; tratamentul distinct al leasingului față de achiziția directă.

<sub>verificat pe surse publice la 21.08.2026 — confirmă sau corectează</sub>

**Context.** Notițele arătau capitalizarea TVA nededuse de pe AVANS în valoarea de intrare (150.000 + 5.250 = 155.250), dar pentru ratele lunare foloseau 6588. Practica e împărțită și în literatură.

**De ce contează.** F-108 și MOD_LEASING_FIN. E singura variabilă a modulului care schimbă valoarea de intrare a mijlocului fix, deci și amortizarea, deci și impozitul pe profit pe toată durata contractului.

<sub>sursa: training 07.08.2026, întrebarea 3</sub>


## Imobilizări — prag și amortizare

### 24. Recomandați alinierea pragului contabil de recunoaștere la cel fiscal (5.000 lei), sau menținerea unui prag intern mai mic pentru control de gestiune?

**Răspuns.** De la 1 ianuarie 2026 pragul FISCAL al mijloacelor fixe a crescut de la 2.500 la 5.000 lei (OUG 8/2026, art. 28 alin. (2) Cod fiscal). Contabil, OMFP 1802/2014 NU condiționează recunoașterea unei imobilizări de o valoare minimă — doar de definiție (utilizare peste 1 an, în scop de producție/prestare/administrativ). Alinierea pragului contabil la cel fiscal (5.000) e opțională, dar evită diferențele temporare între amortizarea contabilă și cea fiscală. Un prag contabil intern mai mic, pentru control de gestiune, e legitim — dar produce diferențe temporare de urmărit.

**Temei.** OUG 8/2026 (modifică art. 28 alin. (2) Cod fiscal), de la 01.01.2026; OMFP 1802/2014 — fără prag valoric contabil.

<sub>verificat pe surse publice la 01.09.2026 — confirmă sau corectează</sub>

**Context.** OUG 8/2026 a urcat pragul fiscal la 5.000 lei. Pragul contabil rămâne la latitudinea entității, prin politici contabile.

**De ce contează.** MOD_IMOBILIZARI face un test de prag la intrare. Dacă cele două praguri diferă, apar diferențe temporare de urmărit în registrul de evidență fiscală — un lucru pe care modulul nu îl tratează azi.

<sub>sursa: training 12.08.2026, întrebarea 1</sub>


### 25. Excepția de la cumulul cu profitul reinvestit (art. 22 alin. 9) acoperă doar amortizarea accelerată, sau și pe cea superaccelerată de 65%?

**Răspuns.** Regula: cine aplică scutirea de impozit a profitului reinvestit **nu poate opta pentru amortizarea accelerată** pentru activele respective — se amortizează liniar sau degresiv. Există însă o **excepție pentru 2026**: dacă scutirea se aplică pentru subgrupa 2.1 (echipamente tehnologice — mașini, utilaje și instalații de lucru) și pentru calculatoare și echipamente periferice, contribuabilul **poate** opta pentru amortizare accelerată.

**Temei.** Cod fiscal art. 22 alin. (9), cu trimitere la art. 28 alin. (5) lit. b) pentru excepția din 2026.

<sub>verificat pe surse publice la 21.08.2026 — confirmă sau corectează</sub>

**Context.** Notițele spuneau despre amortizarea accelerată că „nu poate să mai fie aplicată o altă facilitate fiscală = reducere pentru profitul reinvestit”, cu recomandarea de a calcula ce e mai avantajos.

**De ce contează.** F-204 și MOD_IMOBILIZARI, la alegerea metodei de amortizare. Dacă excepția nu acoperă superaccelerata, calculul comparativ are altă concluzie.

<sub>sursa: training 12.08.2026, întrebarea 2</sub>


## Imobilizări — ieșiri din gestiune

### 26. Care este baza legală exactă pentru a trata ca nedeductibilă diferența dintre valoarea rămasă și prețul de vânzare, față de art. 28 alin. (17)?

**Răspuns.** **Nu există un asemenea temei — presupunerea din notițe e inversă.** La vânzarea unui mijloc fix la prețul pieței, valoarea rămasă neamortizată e cheltuială **deductibilă**, chiar dacă prețul e sub ea. Limitarea reală e alta și privește doar **autoturismele din categoria M1**: acolo valoarea rămasă e deductibilă în limita a **1.500 lei × numărul de luni rămase** de amortizat din durata normală de funcționare.

**Temei.** Cod fiscal art. 28 alin. (17) și normele metodologice aferente (limitarea M1).

<sub>verificat pe surse publice la 21.08.2026 — confirmă sau corectează</sub>

**Context.** Notițele: la vânzarea cu 50.000 a unei clădiri cu valoare rămasă 70.000, „50k cheltuieli deductibile, 20k cheltuieli nedeductibile”, cu excepția cazului în care există dovezi (clădire avariată, deviz de service). Citit strict, art. 28 alin. (17) include pierderea în rezultatul fiscal.

**De ce contează.** F-211 și MOD_IESIRE_MF. E testul central al modulului: azi calculează diferența și cere documentul justificativ, dar nu poate cita articolul pe care se sprijină.

<sub>sursa: training 12.08.2026, întrebarea 3</sub>


### 27. La o casare din care nu rezultă nici deșeuri, nici piese reutilizabile, cum se justifică deductibilitatea valorii rămase neamortizate?

**Răspuns.** **Nu se cere nici deșeu, nici piesă reutilizabilă.** Cheltuielile înregistrate ca urmare a casării unui mijloc fix cu valoare fiscală incomplet amortizată sunt, prin lege, cheltuieli efectuate în scopul desfășurării activității economice — deci deductibile. Documentația de casare rămâne necesară ca probă a operațiunii, nu ca o condiție de deductibilitate.

**Temei.** Cod fiscal art. 28 alin. (17).

<sub>verificat pe surse publice la 21.08.2026 — confirmă sau corectează</sub>

**Context.** Notițele tratau cazul cu valorificare (piese pe 3024, venit pe 7588), dar nu și pe cel fără nicio recuperare.

**De ce contează.** F-212 (casarea) și MOD_IESIRE_MF, unde valoarea pieselor recuperate poate fi zero. Fără răspuns, modulul nu poate spune dacă procesul-verbal de scoatere din funcțiune e suficient singur.

<sub>sursa: training 12.08.2026, întrebarea 5</sub>


## Stocuri și producție

### 28. Care sunt celelalte metode de calculație a costurilor acceptate de OMFP 1802/2014, și în ce situații se alege fiecare?

**Răspuns.** OMFP 1802/2014 (pct. 286 și urm.) recunoaște, pe lângă metoda pe comenzi implementată: metoda COSTULUI STANDARD (consumuri normale de materiale/manoperă, revizuite periodic); metoda PE FAZE (producție de masă — cost pe fiecare fază tehnologică, apoi pe produs); și metoda PE COMENZI (producție individuală sau serie mică — purtătorul de cost e comanda). Alegerea urmează specificul producției: pe comenzi la unicat/serie mică, pe faze la producție de masă continuă, cost standard când există norme stabile de consum.

**Temei.** OMFP 1802/2014, pct. 286 (costul de producție și metodele de calculație).

<sub>verificat pe surse publice la 01.09.2026 — confirmă sau corectează</sub>

**Context.** Notițele menționau metoda pe comenzi ca fiind cea mai utilizată, în contextul producției de termopane. Celelalte (pe faze, pe produs, standard-cost) au rămas doar enumerate.

**De ce contează.** F-311 (producția multi-stadiu) ține gestiunea lui 331 analitic pe comandă. Pe faze, structura analitică e alta, deci și fluxul.

<sub>sursa: training 14.08.2026, întrebarea 1</sub>


## TVA — import, vamă, taxare inversă

### 29. Derogarea UE pentru taxarea inversă la cereale și electronice avea termen 31.12.2026 — a fost prelungită?

**Răspuns.** Derogarea e prelungită până la **31 decembrie 2026** și acoperă opt operațiuni: cereale și plante tehnice, certificate de emisii de gaze cu efect de seră, energie electrică și gaze naturale către comercianți persoane impozabile, certificate verzi, telefoane mobile, dispozitive cu circuite integrate, console de jocuri, tablete și laptopuri. Pentru ultimele patru categorii, taxarea inversă se aplică **doar dacă valoarea fără TVA de pe factură e cel puțin 22.500 lei**. La data verificării **nu e publicată o prelungire dincolo de 31.12.2026** — deci expiră peste patru luni dacă nu intervine una.

**Temei.** Cod fiscal art. 331; decizie a Consiliului UE de prelungire până la 31.12.2026. Reverificat la 21.08.2026.

<sub>verificat pe surse publice la 21.08.2026 — confirmă sau corectează</sub>

**Context.** Art. 331 alin. (6) limitează în timp o parte din categorii, iar Consiliul UE a prelungit derogarea succesiv. Nu se poate presupune prelungirea automată.

**De ce contează.** F-402 (taxare inversă internă) și lista de categorii din documentul revizuit. Aplicarea taxării inverse după expirare înseamnă factură greșit întocmită.

<sub>sursa: training 14.08.2026, întrebarea 7</sub>


## TVA — ajustări fără document

### 30. La lipsa la inventar, practica implicită a cabinetului este colectarea de TVA sau ajustarea dreptului de deducere? Ce set de documente se cere clientului?

**Răspuns.** Regula IMPLICITĂ la lipsa la inventar e AJUSTAREA TVA deduse (art. 304 alin. (1) lit. c) Cod fiscal), nu colectarea. Excepție — fără ajustare — pentru bunuri distruse, pierdute sau furate, DOVEDITE corespunzător (proces-verbal, dosar). La lipsuri IMPUTABILE, suma imputată nu e contravaloarea unei operațiuni supuse TVA, dar ajustarea deducerii rămâne datorată. Colectarea (nu ajustarea) apare doar când lipsa se tratează ca livrare către sine. Documente cerute clientului: proces-verbal de inventariere, decizie de imputare sau proces-verbal de scoatere din gestiune, și dovada cauzei pentru scutirea de ajustare.

**Temei.** Cod fiscal art. 304 alin. (1) lit. c) și alin. (2) (bunuri de capital: art. 305).

<sub>verificat pe surse publice la 01.09.2026 — confirmă sau corectează</sub>

**Context.** Notițele spuneau simplu „trebuie să colectez și TVA”. La revizuire am găsit că tratamentul diferă: lipsă imputabilă → colectare; neimputabilă nejustificată → ajustare; bunuri distruse cu documente → fără ajustare.

**De ce contează.** F-406 (înregistrări fără document) și corelațiile C-03 / C-04, unde ajustările care nu vin din facturi trebuie să apară în jurnale cu semnul corect. Cele două tratamente ating conturi diferite, deci și jurnale diferite.

<sub>sursa: training 14.08.2026, întrebarea 2</sub>


## Obligații de mediu

### 31. Care este termenul curent de depunere a declarației la Fondul pentru Mediu — lunar sau trimestrial?

**Răspuns.** **Lunar sau trimestrial**, după tipul de obligație, cu termen **25 a lunii următoare** perioadei de raportare. Depunerea se face exclusiv electronic, prin platforma AFM-Online, cu semnătură electronică calificată — de la 1 iulie 2022 nu se mai acceptă depunerea pe hârtie.

**Temei.** Procedura de declarare la Fondul pentru mediu; depunere electronică obligatorie din 1.07.2022.

<sub>verificat pe surse publice la 21.08.2026 — confirmă sau corectează</sub>

**Context.** Notițele nu dădeau termenul, iar acesta s-a modificat de mai multe ori. La revizuire am scris „verifică termenul curent pe afm.ro”, ceea ce nu e un răspuns.

**De ce contează.** F-310 (ambalaje și taxa AFM) și checklistul lunar. Un termen greșit produce penalități direct.

<sub>sursa: training 14.08.2026, întrebarea 5</sub>


## Plafoane de numerar și contul 455

### 32. Care sunt valorile exacte ale plafoanelor din Legea 70/2015 în forma modificată prin Legea 296/2023, la data operațiunii?

**Răspuns.** Între persoane juridice: **5.000 lei/zi și de persoană**. Magazine cash & carry: 5.000 lei de persoană, dar maximum **10.000 lei total pe zi**; plăți către ele, maximum 10.000 lei/zi. Avansuri spre decontare: **5.000 lei/zi** pentru fiecare persoană care a primit avansul. **Fragmentarea e interzisă expres** pentru facturi peste 5.000 lei, respectiv 10.000 la cash & carry. Legea 239/2025 **nu a modificat plafoanele** de la 1.01.2026, dar a eliminat pragul de 50.000 lei de la care era obligatorie acceptarea cardului și a introdus obligația unui cont de plăți deschis în România.

**Temei.** Legea 70/2015, art. 3 și art. 4, în forma modificată prin Legea 296/2023 și Legea 239/2025.

<sub>verificat pe surse publice la 21.08.2026 — confirmă sau corectează</sub>

**Context.** Notițele rețin 5.000 lei B2B, 10.000 lei încasări de la persoane fizice și 50.000 lei între persoane fizice, plus un plafon separat pentru soldul casieriei la sfârșitul zilei. Sunt și plafoane totale zilnice, peste cele per persoană.

**De ce contează.** Documentul „Control, documente și numerar”, secțiunea de plafoane. Un plafon greșit produce amendă direct, iar fragmentarea e interzisă expres — deci nici împărțirea pe tranșe nu e o ieșire.

<sub>sursa: training 19.08.2026, punctul 1</sub>


### 33. Care sunt exact operațiunile în numerar interzise pe contul 455 și care e temeiul legal?

**Răspuns.** Nu e un plafon, e o **interdicție**. Din **11 noiembrie 2023**, încasările și plățile reprezentând împrumuturi — indiferent de sumă — de la sau către asociați, acționari, administratori și alte persoane fizice **nu se mai pot face în numerar**, ci doar prin instrumente de plată fără numerar. Înalta Curte a stabilit că amenda de 25% se calculează la **totalul operațiunilor**, nu la depășirea unui plafon.

**Temei.** Legea 70/2015 modificată prin Legea 296/2023, în vigoare din 11.11.2023. Cuantumul amenzii — jurisprudența ÎCCJ.

<sub>verificat pe surse publice la 21.08.2026 — confirmă sau corectează</sub>

**Context.** Notițele spun doar că „plățile din 455 prin casierie nu mai sunt permise în condițiile anterioare”, fără să precizeze care condiții și din ce text.

**De ce contează.** Foaia „Închideri periodice”, unde 455 e urmărit trimestrial fără flux în spate. Fără regula exactă, rândul rămâne gol declarat — nu se poate scrie o monografie pentru o restricție pe care n-o cunosc.

<sub>sursa: training 19.08.2026, punctul 2</sub>


## Salarii — praguri și baze de calcul

### 34. Care este salariul minim brut pe economie în vigoare, și de la ce dată?

**Răspuns.** **4.325 lei** brut, de la **1 iulie 2026** (anterior 4.050 lei). Minimul se aplică proporțional cu norma: 2.162,50 lei la jumătate de normă, 1.081,25 la un sfert. Tot de la 1 iulie 2026 și până la 31.12.2026, suma neimpozabilă scade de la 300 la 200 lei/lună.

**Temei.** HG 146/2026 (salariul minim). Suma neimpozabilă — Cod fiscal, cu aplicare 1.07–31.12.2026.

<sub>verificat pe surse publice la 21.08.2026 — confirmă sau corectează</sub>

**Context.** Notițele rețin 4.325 lei. Valoarea se schimbă prin hotărâre de guvern, uneori de mai multe ori pe an, iar verificarea normei parțiale se face contra ei.

**De ce contează.** Verificarea lunară a statului de plată și corelația „minim proporțional cu norma”. Un prag depășit înseamnă contracte neconforme la toți salariații cu normă parțială, nu doar la unul.

<sub>sursa: training 21.08.2026, punctul 1</sub>


### 35. Ce contribuții se datorează pentru indemnizația de concediu medical, și pe ce parte se rețin?

**Răspuns.** Din indemnizație se rețin **CAS 25%** și **impozit 10%**. **CASS 10% se datorează începând cu veniturile lunii august 2026** — până atunci nu se datora. Fac excepție indemnizațiile pentru accidente de muncă și boli profesionale, care rămân scutite de CASS. **CAM 2,25% NU se datorează** pe partea suportată din FNUASS: angajatorul datorează CAM doar pe zilele pe care le suportă el. Baza de calcul e media veniturilor brute din ultimele 6 luni, plafonată la 12 salarii minime brute pe lună.

**Temei.** CAS: Cod fiscal art. 139 alin. (1) lit. o) și art. 144. CASS: Legea 170/2026, aplicabilă veniturilor din august 2026. CAM: Cod fiscal art. 220^5. Baza: OUG 158/2005.

<sub>verificat pe surse publice la 21.08.2026 — confirmă sau corectează</sub>

**Context.** Notițele acoperă împărțirea indemnizației între angajator și FNUASS (6458 / 4382 = 423), dar nu și reținerile din ea. Regulile diferă de cele ale salariului.

**De ce contează.** Fluxul de concedii medicale și MOD_SALARII. Fără regulă, monografia se oprește la împărțire și nu ajunge la restul de plată.

<sub>sursa: training 21.08.2026, punctul 3</sub>


### 36. Care e limita de reținere prin poprire pentru obligațiile de întreținere, față de treimea aplicabilă datoriilor obișnuite?

**Răspuns.** Sunt **trei** reguli, nu una. **1/2** din venitul net lunar pentru obligații de întreținere sau alocații pentru copii; **1/3** pentru orice alte datorii. Când există mai multe popriri pe aceeași sumă, reținerea totală nu poate depăși **1/2**, indiferent de natura creanțelor. Iar dacă venitul e sub salariul minim net pe economie, se poate urmări doar partea care depășește **jumătate din salariul minim net** — prag de protecție pe care notițele nu-l aveau deloc.

**Temei.** Codul de procedură civilă, art. 729 — Limitele urmăririi veniturilor bănești.

<sub>verificat pe surse publice la 21.08.2026 — confirmă sau corectează</sub>

**Context.** Notițele rețin 33,33% din salariul net. Codul de procedură civilă prevede o limită mai mare pentru pensii de întreținere, și reguli de cumul când există mai multe popriri.

**De ce contează.** Fluxul de popriri (427). Un procent greșit înseamnă ori reținere insuficientă — firma răspunde față de executor — ori excesivă, față de salariat.

<sub>sursa: training 21.08.2026, punctul 4</sub>


### 37. Care e plafonul legal al sumei care se poate imputa unui salariat pentru o pagubă produsă, și în ce ritm se poate reține din salariu?

**Răspuns.** Codul muncii art. 254: recuperarea prejudiciului prin NOTĂ DE CONSTATARE ȘI EVALUARE, de comun acord cu salariatul, nu poate depăși echivalentul a 5 SALARII MINIME brute pe economie. Peste acest plafon sau fără acordul salariatului, recuperarea se face numai prin instanță. Reținerea efectivă din salariu e limitată de art. 169: nu se reține fără titlu executoriu, iar reținerile cumulate nu depășesc o treime din salariul net. ⚠️ Corecție la notiță: legea spune „5 salarii MINIME”, nu „5 salarii medii”.

**Temei.** Codul muncii art. 254 (plafonul de comun acord: 5 salarii minime brute) și art. 169 (reținerile din salariu).

<sub>verificat pe surse publice la 01.09.2026 — confirmă sau corectează</sub>

**Context.** Notițele din 26.08 menționează un plafon „la nivelul a 5 salarii medii”, cu observația formatorului însuși: „de verificat suma”. Separat, notițele spun că imputația nu se poate face fără ca salariatul să fie informat și de acord — Codul muncii.

**De ce contează.** F-426 pasul 5, unde reținerea din 421 stinge creanța de pe 461. Dacă plafonul e mai mic decât paguba, fluxul are nevoie de un pas de eșalonare, iar creanța rămâne pe 461 mai multe luni.

<sub>sursa: training 26.08.2026, punctul 1</sub>


## Trezorerie — diferențe de curs și plafoane

### 38. Există un plafon de sold de casă separat, de 500.000 lei, pentru magazinele de tip cash & carry, supermagazine și hipermagazine?

**Răspuns.** DA. Legea 70/2015 stabilește un sold de casă maxim de 50.000 lei la sfârșitul zilei, iar pentru magazinele de tip cash & carry, supermagazine și hipermagazine plafonul e 500.000 lei la sfârșitul zilei. Excedentul se depune în conturi bancare în 2 zile lucrătoare. Deci C-38 are nevoie de un al doilea prag, după tipul unității — la un client cu magazin mare, pragul de 50.000 ar semnala greșit o depășire în fiecare zi.

**Temei.** Legea 70/2015, art. 4^1 (plafonul soldului de casă; 500.000 lei pentru cash & carry / supermagazine / hipermagazine).

<sub>verificat pe surse publice la 01.09.2026 — confirmă sau corectează</sub>

**Context.** Nu era în notițele de la curs. O a doua revizuire a acelorași notițe îl afirmă, alături de plafonul general de 50.000 lei.

**De ce contează.** C-38, care azi are un singur prag. Dacă se confirmă, corelația are nevoie de un al doilea prag, după tipul unității — iar la un client cu magazin mare, pragul de 50.000 ar fi semnalat greșit ca depășire în fiecare zi.

<sub>sursa: training 28.08.2026, punctul 8</sub>


### 39. Care e articolul din OMFP 1802/2014 care spune că elementele NEMONETARE (inclusiv avansurile în valută) nu se reevaluează la cursul de închidere?

**Răspuns.** Confirmat: avansurile în valută (409, 419, 4093, 4094) sunt elemente NEMONETARE și NU se reevaluează la cursul de închidere — regulă aplicată din 2015, odată cu OMFP 1802/2014. Reevaluarea lunară privește doar elementele MONETARE (disponibilități, creanțe și datorii care se sting în bani). Distincția monetar/nemonetar și evaluarea la data bilanțului sunt în OMFP 1802/2014, secțiunea de evaluare la bilanț (pct. 319 și urm.). ❓ Numărul exact al punctului rămâne de confirmat pe textul ordinului — regula e fermă, referința aproximativă.

**Temei.** OMFP 1802/2014, secțiunea de evaluare la data bilanțului (pct. 319 și urm.); avansurile în valută nereevaluate din 2015.

<sub>verificat pe surse publice la 01.09.2026 — confirmă sau corectează</sub>

**Context.** Regula a apărut la contraverificarea cu revizuirile paralele: avansurile în valută rămân la cursul plății, nu se reevaluează lunar ca disponibilul și creanțele monetare.

**De ce contează.** F-107 și MOD_CREDIT_VALUTA: dacă un avans în valută ar fi reevaluat, ar produce diferențe de curs pe un cont care n-are ce diferență să genereze. Regula e scrisă în §4.1 al documentului de trezorerie ca ➕.

<sub>sursa: training 28.08.2026, punctul 10</sub>


### 40. Reevaluarea de sfârșit de lună a conturilor în valută se înregistrează pe 665/765 sau pe 668/768?

**Răspuns.** Confirmat: diferențele din reevaluarea lunară a elementelor MONETARE în valută (disponibilități, creanțe, datorii) se înregistrează pe 665/765, NU pe 668/768. Unele cabinete folosesc analitice distincte (ex. 6651/7651) exact pentru a separa reevaluarea de decontare — ceea ce validează abordarea cu analitice .DEC/.REV din repo. Varianta 668/768 din notiță e greșită pentru valuta propriu-zisă; 668/768 se folosesc pentru creanțe/datorii exprimate în LEI dar decontabile după cursul unei valute — alt caz.

**Temei.** OMFP 1802/2014 — funcțiunea conturilor 665/765 (diferențe de curs, inclusiv la evaluarea de sfârșit de lună a disponibilităților în valută).

<sub>verificat pe surse publice la 01.09.2026 — confirmă sau corectează</sub>

**Context.** Notițele din 28.08 spun: diferențele de curs curente prin 665/765, iar reevaluarea de la sfârșitul lunii prin 668/768, cu observația „să fie clară diferența de curs din reevaluare, și cea de la furnizori”.

**De ce contează.** F-107 pasul de reevaluare, MOD_CREDIT_VALUTA în întregime, și structura analitică a lui 665/765. Nu e nuanță de stil: cele două variante pun aceeași sumă în conturi care se raportează diferit.

<sub>sursa: training 28.08.2026, punctul 1</sub>


### 41. Plafonul de 50.000 lei la soldul de casă e per societate sau per casierie / punct de lucru?

**Răspuns.** Plafonul de sold (50.000 lei, respectiv 500.000 la retail) vizează soldul de casă al PERSOANEI JURIDICE la sfârșitul zilei. Deschiderea unei a doua casierii „ca să mai am 50.000” nu ține la control: un punct de lucru fără activitate reală de încasări cade la testul substanței economice. ❓ Formularea literală „per entitate vs. per punct de lucru” din textul art. 4^1 rămâne de citit pe lege (sursele cu textul integral erau inaccesibile), dar practica clientului nu rezistă indiferent de formulare.

**Temei.** Legea 70/2015, art. 4^1 — plafonul soldului de casă al persoanei juridice.

<sub>verificat pe surse publice la 01.09.2026 — confirmă sau corectează</sub>

**Context.** Notițele spun „50.000 lei pe fiecare punct de lucru” și povestesc un client care, aflând de plafon, „a mai făcut rost de o casierie cu 50.000 lei”. Notițele nu spun dacă practica aceea rezistă la control.

**De ce contează.** C-38 și cadența pe 5311. Dacă limita e per societate, o a doua casierie nu rezolvă nimic și clientul e în neregulă; dacă e per casierie, orice societate poate multiplica plafonul deschizând puncte de lucru, ceea ce ar goli restricția de sens.

<sub>sursa: training 28.08.2026, punctul 2</sub>


## Trezorerie — convenții de înregistrare

### 42. Ce documentație face diferența, la un control, între „rate contractuale” și fragmentarea unei plăți?

**Răspuns.** Legea 70/2015 interzice expres fragmentarea unei plăți pentru a ocoli plafonul. Un contract cu plata în rate, cu scadențar și date fixe, scoate operațiunea de sub acuzație — fiecare rată e o operațiune la data ei. Apărarea cade dacă ratele se încasează la alte date sau sume decât scadențarul. Nu există o cerință legală explicită de „dată certă” a contractului; ce contează la control e ca plata efectivă să urmeze fidel scadențarul încheiat ANTERIOR operațiunilor. Recomandat: contract scris, cu scadențar, datat înainte de prima rată.

**Temei.** Legea 70/2015 (interdicția fragmentării); forma contractului — practică, fără cerință legală de dată certă.

<sub>verificat pe surse publice la 01.09.2026 — confirmă sau corectează</sub>

**Context.** Notițele spun că un contract cu plata în rate scoate operațiunea de sub acuzația de fragmentare: „am scadențar, am o dată fixă pe care încasez ratele”. Nu spun ce se prezintă efectiv.

**De ce contează.** C-38 și secțiunea de plafoane din documentul de control. Diferența dintre legal și amendabil stă în ce poți arăta, nu în ce ai făcut.

<sub>sursa: training 28.08.2026, punctul 6</sub>


## Gestiuni, bonuri de consum și compensări

### 43. Care e forma obligatorie a bonului de consum, și în ce cazuri poate fi înlocuit cu alt document?

**Răspuns.** Bonul de consum e documentul reglementat de OMFP 2634/2015, obligatoriu la eliberarea din gestiune pentru consum. ⚠️ „Fișa limită de consum” pe care o propuneam ca alternativă a fost ELIMINATĂ din formularele reglementate prin OMFP 2634/2015 — nu mai e o opțiune validă. La transferul între gestiuni se folosește bonul de transfer (aviz intern). Deci: bon de consum la consum, bon de transfer la mutarea între gestiuni; fișa limită de consum nu mai există ca formular obligatoriu.

**Temei.** OMFP 2634/2015 privind documentele financiar-contabile (bonul de consum; eliminarea fișei limită de consum).

<sub>verificat pe surse publice la 01.09.2026 — confirmă sau corectează</sub>

**Context.** Notițele stabilesc ordinea — întâi se creează gestiunea, apoi se pune problema consumului — și spun că orice ieșire din gestiune se face pe bon de consum. Formatorul a marcat însă explicit subiectul ca „de contraverificat, de clarificat detaliat”.

**De ce contează.** F-321 pasul 3 și regula „consumul trece prin gestiune” din documentul de stocuri. De forma documentului depinde ce i se cere clientului să aducă lunar — iar cerința se face o dată, la preluare, sau nu se mai face.

<sub>sursa: training 28.08.2026, punctul 3</sub>


### 44. Ce document susține compensarea 4091 ↔ 419 la același partener, și de la ce prag trebuie făcută prin sistemul reglementat?

**Răspuns.** Compensarea creanțelor și datoriilor reciproce cu același partener se face pe formular de compensare, cu acord scris între părți. Pragul: pentru facturi peste 10.000 lei restante peste 30 de zile, compensarea se face OBLIGATORIU prin sistemul reglementat (IMI — Institutul de Management și Informatică), conform OUG 77/1999 și HG 685/1999. Sub 10.000 lei sau sub 30 de zile de la scadență, compensarea se face direct între client și furnizor, pe același formular, fără IMI. TVA-ul NU se compensează odată cu avansurile — regularizarea lui se face la facturile finale, prin stornarea fiecărui avans.

**Temei.** OUG 77/1999 și HG 685/1999 (compensarea prin IMI peste 10.000 lei restanți peste 30 de zile).

<sub>verificat pe surse publice la 01.09.2026 — confirmă sau corectează</sub>

**Context.** Notițele scriu doar „4091 - 419 <=> să faci compensări ulterior”, cu mențiunea „de analizat” adresată mie.

**De ce contează.** Dacă apare un flux de compensare, el are nevoie de documentul justificativ ca stare inițială. Fără el, compensarea e o decizie unilaterală asupra unor solduri care aparțin la două raporturi juridice diferite.

<sub>sursa: training 28.08.2026, punctul 4</sub>


## Dividende — CASS, declarații și termene

### 45. CASS pe dividende se datorează la dividendele DISTRIBUITE sau la cele efectiv RIDICATE?

**Răspuns.** CASS pe dividende se datorează în funcție de dividendele ÎNCASATE (ridicate) în cursul anului, nu de cele doar distribuite — confirmă notița formatorului. Dividendele încasate intră în baza de analiză a plafoanelor de 6/12/24 salarii minime brute: sub 6 salarii minime cumulat (cu alte venituri nesalariale) nu se datorează CASS; între 6–12 baza e 6 salarii minime; între 12–24 baza e 12; peste 24 baza e 24. Se declară prin Declarația Unică (D212), până la 25 mai a anului următor. Distincția cheie: impozitul de 16% e la DISTRIBUIRE (termen 25.01), CASS e la ÎNCASARE, pe plafoane anuale.

**Temei.** Cod fiscal art. 170 (baza CASS pe venituri din investiții — dividende încasate) și art. 174 (declararea prin D212).

<sub>verificat pe surse publice la 01.09.2026 — confirmă sau corectează</sub>

**Context.** Notițele din 26.08 spun explicit: „la dividendele ridicate se plătește sănătate, nu la cele distribuite”. Formatorul a legat asta de cele două rubrici distincte din D205 — dividende distribuite și dividende ridicate.

**De ce contează.** Momentul în care se naște obligația de CASS și, prin el, ce arată Declarația Unică față de soldul lui 457. Un 457 cu sold creditor la 31.12 înseamnă dividende distribuite și neridicate: dacă baza CASS e distribuirea, obligația există deja; dacă e ridicarea, nu.

<sub>sursa: training 26.08.2026, punctul 2</sub>


## Microîntreprindere — prag și cotă

### 46. Care sunt pragul de venituri și cota de impozit pentru microîntreprinderi, în vigoare la data operațiunii?

**Răspuns.** Prag **100.000 EUR** venituri totale, din 2026 (era 250.000 în 2025 și 500.000 până în 2024). Cotă unică **1%** — cota de 3% pentru firmele fără salariat a fost **eliminată** de la 1 ianuarie 2026. Echivalentul în lei se determină la cursul de la închiderea exercițiului financiar anterior.

**Temei.** Cod fiscal, Titlul IV — Impozitul pe veniturile microîntreprinderilor.

<sub>verificat pe surse publice la 21.08.2026 — confirmă sau corectează</sub>

**Context.** Notițele rețin 100.000 EUR și 1%. Pragul a fost coborât în trepte în anii anteriori, iar cota a avut două paliere. Ambele sunt din Codul fiscal, deci se pot schimba prin ordonanță.

**De ce contează.** Fluxul de impozit micro (698 = 4418) și avertizarea clientului care se apropie de prag. Trecerea se face din trimestrul depășirii, deci un prag greșit înseamnă o declarație greșită, nu doar o estimare.

<sub>sursa: training 21.08.2026, punctul 2</sub>


---

*46 de întrebări în total: 13 deschise, 7 decizii de cabinet, 26 cu răspuns verificat. Fiecare se poate urmări înapoi la training și la numărul ei original.*
