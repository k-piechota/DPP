### Gra Fill-a-Pix
W celu uruchomienia gry w pierwszej kolejności należy upewnić się, że zainstalowane są odpowiednie moduły.
Znajdując się w katalogu z grą można to zrobić komendą

``` pip install -r requirements.txt ```

Brakujące moduły zostaną pobrane.


Następnie można włączyć grę za pomocą komendy:
``` python -m game.play ```

![Instalacja](installation.png)


Zostanie uruchomione menu gry, w którym należy wprowadzić - liczbę kolumn i wierszy (liczby całkowite), oraz lokalizację dowolnego pliku graficznego, za pomocą przycisku 'Wybierz plik'. Można wykorzystać przykładowe obrazy: tree.png lub house.png.

Zasady gry:

https://www.conceptispuzzles.com/index.aspx?uri=mobile/100001

Wskazywanie zamalowanego pola odbywa się poprzez kliknecie lewym przyciskiem myszy w odpowiednia komórkę.

Próba zamalowania nieodpowiedniej komórki poskutkuje pojawieniem się komunikatu o błędzie.

Gdy wszystkie komórki zostaną zamalowane pojawi się informacja o końcu gry.


Przykład uzupełnionej planszy:

![Gra](filled.png)