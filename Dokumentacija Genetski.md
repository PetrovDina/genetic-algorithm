![](Aspose.Words.9f929165-1679-4eb9-a44a-0d118558ce7f.001.png)![](Aspose.Words.9f929165-1679-4eb9-a44a-0d118558ce7f.002.png)![](Aspose.Words.9f929165-1679-4eb9-a44a-0d118558ce7f.003.png)


![](Aspose.Words.9f929165-1679-4eb9-a44a-0d118558ce7f.004.png)













Studenti:                          	Jelena Miletić  SW45-2018 ,   Dina Petrov SW52-2018

Predmet:                        	Nelinearno programiranje i evolutivni algoritmi

Broj zadatka: 		11

Tema zadatka:		Genetski algoritam, “black-box optimizacija”

neuronska mreža

![](Aspose.Words.9f929165-1679-4eb9-a44a-0d118558ce7f.005.jpeg)

`	`U projektu rešavamo problem optimizacije date neuronske mreže. Kao izlaz neuronske mreže dobijamo njenu grešku i pokušavamo da optimizujemo izlaz pomoću genetskog algoritma tj. da što više smanjimo vrednost (da bude što bliža nuli). Neuronskoj mreži prosleđujemo vektor od 60 vrednosti pomoću kojih ona dobija težine na svakoj od grana unutar nje. Ovakvom optimizacijom tražimo minimum funkcije.




![](Aspose.Words.9f929165-1679-4eb9-a44a-0d118558ce7f.006.png)

Genetski algoritam predstavlja optimizacioni metod koji dolazi do rešenja oponašajući osnovne mehanizme evolucije iz prirode kao što su selekcija, ukrštanje, mutacija..

Svaka iteracija genetskog algoritma odgovara jednoj ‘generaciji jedinki’, odnosno trenutnoj populaciji. Svaka jedinka neke generacije predstavlja potencijalno rešenje našeg problema. One imaju niz osobina (karakteristika), kao i svoj stepen prilagodjenosti (engl. *fitness*). U našim numeričkim metodama on odgovara vrednosti funkcije, odnosno vrednosti kriterijuma optimalnosti f(x). Ove vrednosti nam pomažu da procenimo koliko nam je korisna neka jedinka kao rešenje problema. Pošto tražimo minimum funkcije, bolje je prilagođena jedinka čija je vrednost kriterijuma optimalnosti *manja*. 

U toku rada genetskog algoritma dolazi do smenjivanja generacija jedinki sa ciljem povećavanja njihove prilagođenosti. Samim tim dolazi i do poboljšanja vrednosti kriterijuma optimalnosti.


Algoritam ukratko:

1. Inicijalno se generiše skup jedinki koji predstavljaju početnu populaciju
1. Za svaku jedinku iz početne populacije računa se njena prilagođenost
1. Vrši se proces *selekcije* nad početnom populacijom - biraju se one jedinke koje će ući u proces reprodukcije, odnosno *ukrštanja.* Jedinka se može više puta odabrati za proces ukrštanja. Veće šanse za odabir pri selekciji imaju one jedinke koje su bolje prilagođene. 
1. Nad dve selektovane jedinke (roditelji) vrši se *ukrštanje -* dolazi do kombinacije osobina roditelja i stvaraju se nove jedinke - *potomci*.
1. Nad nekim, slučajno odabranim potomcima vrši se *mutacija* sa veoma malom verovatnoćom. Mutacija obuhvata izmenu nekih osobina (gena)  potomka. Mutacije su neophodne jer sprečavaju prevremenu konvergenciju i zaglavljivanje u lokalnom ekstremu.
1. Kada se procesom reprodukcije stvori dovoljan broj potomaka, oni se ubacuju u populaciju i zamenjuju sve ili samo neke jedinke prethodne, roditeljske populacije. 
1. Stvaranjem nove populacije se završava jedna iteracija (generacija) algoritma, a zatim se ciklično ponavlja proces dok se ne dostigne predodređen broj generacija. 
##

- #### **Struktura programa![](Aspose.Words.9f929165-1679-4eb9-a44a-0d118558ce7f.007.png)**
Program sadrži klasu *Individual* koja predstavlja jednu jedinku u populaciji. Ona sadrži vektor svih svojih karakteristika 

*W = [w1, w2, w3, ..., w59, w60]* i vrednost svoje prilagođenosti koju dobijamo od izlaza iz neuronske mreže.

Neke od vrednosti algoritma koje su postavljen na početku su:

![](Aspose.Words.9f929165-1679-4eb9-a44a-0d118558ce7f.008.png)

*characteristics\_num - broj vrednosti u vektoru svake jednike*

*min\_range* i *max\_range -*  minimalna i maksimalna vrednost težina u vektoru karakteristika jedinki

`   `mutation\_genes\_num - broj karakteristika jedinke koje  menjamo u slučaju mutacije               





- #### **Selekcija jedinki za ukrštanje (roditelji)**
  - Za odabir kandidata za ukrštanje koristile smo koncept elitizma Ideja je da roditelji imaju priliku da budu ubačeni u narednu generaciju umesto svoje dece ako su bolje prilagođeni od njih. Postiže se sortiranjem roditelja i potomaka po njihovoj prilagođenosti.
  - Nakon sortiranja, odaberemo dvadeset najprilagođenijih jedinki. Kako ne bismo imali prevremenu konvergenciju algoritma, takođe ubacujemo i nasumično odabrane jedinke koje nisu u najboljih 20 i njima popunjavamo ostatak nove populacije. 

- #### **Ukrštanje jedinki** 
  - Kako su vrednosti karakteristika jedinki realni brojevi, iskoristile smo ideju da će vrednost jedne karakteristike jedinke biti kombinacija vrednosti iste te karakteristike oba roditelja jedinke. 

![](Aspose.Words.9f929165-1679-4eb9-a44a-0d118558ce7f.009.png)

- Uzimamo svaki “gen” (karakteristiku) iz vektora od 60 vrednosti oba roditelja. Na primer, uzimamo prvu vrednost od prvog roditelja i prvu vrednost od drugog roditelja. Prva vrednost u vektoru potomka će tada biti u opsegu ograničenim vrednostima koje imaju roditelji. 

![](Aspose.Words.9f929165-1679-4eb9-a44a-0d118558ce7f.010.png)

- #### **Mutacija jedinki**
  - Definisale smo vrednost promenljive **mutation\_chance** koja iznosi 0.1. To znači da svaka jedinka ima 10% šanse da se nad njom obavi mutacija. Takođe smo odredile vrednost promenljive mutation\_genes\_num = 3 koja govori da prilikom mutacije menjamo tri vrednosti unutar vektora karakteristika jedinke. 
  - Korišćenjem *numpy* biblioteke i funkcije *random.uniform()* postigle smo slučajni odabir jedinki koje će se mutirati, osobina unutar vektora karakteristika čije će vrednosti menjati, kao i generisanje novih vrednosti tih karakteristika. 
#### ![](Aspose.Words.9f929165-1679-4eb9-a44a-0d118558ce7f.011.png)

- #### **Odabir parametara algoritma** 
  - Prilikom testiranja projekta zaključile smo da je za postizanje najoptimalnijeg odnosa vremena izvršavanja i tačnosti rešenja idealan broj generacija 50 (čije dostizanje je i ujedno kriterijum zaustavljanja). 
  - Veličina jedne populacije iznosi 200 jedinki.
  - Šansa za mutaciju je 10% (<= 0.1) kako bismo smanjile šansu da algoritam upadne u lokalni minimum funkcije.

- #### **Rezultati algoritma**

![](Aspose.Words.9f929165-1679-4eb9-a44a-0d118558ce7f.012.png)

- Razlika u rezultatima kada u populaciji imamo 200 i 300 jedinki je zanemarljivo mala, ali se u slučaju sa 200 jedinki program izvršava značajno brže.

- Implementacijom koncepta elitizma, vreme izvršavanja programa je osetno duže nego što bi bilo koristeći neki drugi metod selekcije. Glavni razlog jeste postupak sortiranja svake populacije kako bi se izvukle najprilagođenije jedinke, što je dugotrajan proces sa velikim brojem generacija. Uprkos tome, svesno smo odabrale upravo taj metod kako bi naš algoritam bio što ‘sličniji’ prirodnim procesima evolucije koje oponaša. 







