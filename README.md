# Zadania z przedmiotu Logika Matematyczna w Informatyce


* ZADANIE 2  
  Implementacja liczebników Churcha w Pythonie 2.  
  Więcej informacji w pliku md w folderze Zadanie2.  
  Żeby uruchomić prezentację/test:
  ```bash
  python test_church.py
  ```

* ZADANIE 3, czesc 1  
  Proste programy logiczne w Pythonie 2.  
  main.py - prosty program sprawdzajacy parzystość 6 liczb podanych jako argumenty w wierszu poleceń.  
  main_negated.py - wersja programu main.py z zanegowanym warunkiem  
  test_script.py - skrypt testowy do powyższych programów  
  Żeby uruchomić programy: python [main.py main_negated.py] n1 n2 n3 n4 n5 n6, gdzie n1..n6 to liczby podawane jako argumenty do programu  
  Żeby uruchomić skrypt testowy: python test\_script.py [main.py main_negated.py]  
  Przykładowe uruchomienia:
  ```bash
  python main.py 2 4 6 8 10 12
  echo $?
  ```
  ```
  python test_script.py main.py
  ```

* ZADANIE 3, czesc 2  
  Prosta gra logiczna w Pythonie 2.  
  Żeby uruchomić: python game.py, opcjonalnie z parametrem --help lub --format.  
  Parametr --help wyświetla więcej informacji na temat użytkowania programu, w tym inne dostępne parametry.  
  Parametr --format wyświetla informacje o obsługiwanym formacie plików wejściowych z wartościami dla funkcji logicznych.  
  Uruchamianie gry:
  ```
  python game.py
  ```
  Uzyskiwanie pomocy:
  ```
  python game.py --help
  ```
