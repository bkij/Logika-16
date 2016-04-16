# Liczebniki Churcha

Liczebniki Churcha to sposób na zakodowanie liczb naturalnych przy pomocy funkcji wyższego rzędu.
Liczebnik Churcha odpowiadający liczbie N przyjmuje jako argumenty funkcję i jej argument i aplikuję ją N razy do argumentu.
Przykładowo, oznaczając liczebnik Churcha liczby N przez churchN:
  - Przyjmijmy f(x) = 3*x, wtedy church2(f, 2) == f(f(2)) == 18
  - Przyjmijmy f(x) = x^2, wtedy church4(f, 3) == f(f(f(f(3)))) == 3^16 == 43046721
  
Tradycyjnie definiuje się liczebniki Churcha przy pomocy:
* liczebnika zerowego - funkcja zaaplikowana zero razy do argumentu po prostu zwraca argument, church0(f, x) == x
* funkcji następnika, która przyjmuje jako argument liczebnik Churcha i zwraca liczebnik o jeden większy. W ten sposób oczywiście mamy dostęp do dowolnej liczby naturalnej
  
Na liczebnikach Churcha możemy zdefiniować operacje analogiczne jak na zwykłych liczbach naturalnych:

* Dodawanie: jeśli pierwszy liczebnik Churcha koduje liczbę N, a drugi liczbę M, to musimy N razy zaaplikować do liczebnika M funkcję następnika. Ponieważ liczebnik Churcha to funkcja wyższego rzędu, może przyjąć funkcję następnika, a więc:
dodaj(church1, church2) == church1(nastepnik, church2)      <---- proszę zauważyć, że to i kolejne operacje na liczebnikach churcha zwracają liczebnik churcha, a więc **funkcję wyższego rzędu**, która przyjmuje jako swoje argumenty jakąś funkcję i argument dla niej

* Mnozenie: przy oznaczeniach jak wyżej, aplikujemy N razy drugi liczebnik Churcha, bo f<sup>m*n</sup> ==  f<sup>m</sup>(f<sup>m</sup>(...))) n razy
pomnoz(church1, church2) == church1(church2)

* Potegowanie: korzystając z identyczności m<sup>n</sup> == 1\*m\*m\*...\*m (mnożenie jedynki przez m n razy) mozemy zaaplikować N razy mnożenie drugiego liczebnika przez jeden, spoteguj(church1, church2) == church1(pomnoz(liczebnik1, church2))


* Odejmowanie i funkcja poprzednika: Zeby moc odejmowac liczebniki Churcha, musimy zdefiniowac funkcje poprzednika liczby i zaaplikowac ja 
M razy do N (jesli chcemy wykonac dzialanie N - M). Funkcje poprzedznika tworzymy, operując na parach liczebników kodujących liczby
(n + 1, n). Wtedy, przy pomocy funkcji następnej pary przekształcającej parę (liczebnikN, liczebnikN-1) na parę (nastepnik(liczebnikN), liczebnikN-1)
mozemy znaleźc liczbę N-1, aplikując funkcję następnej pary N razy do pary poczatkowej (liczebnik0, liczebnik0).

Przykłady użycia liczebników Churcha i jednocześnie dowód, że działają są w pliku test_church.py. Implementacja z opisami wykorzystującymi rachunek lambda
w pliku church.py

Przydatny odnośnik: http://palmstroem.blogspot.com/2012/05/lambda-calculus-for-absolute-dummies.html
