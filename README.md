# Axion challenge 3

## Co chce sprawdzic?

Chce sprawdzic, czy dodawanie kolejnych warstw do obwodu kwantowego faktycznie poprawia jego skutecznosc.

Do tego wykorzystam make_moons, czyli zbior punktow ulozonych w dwa polksiezyce. Model bedzie musial nauczyc sie rozpoznawac, do ktorego z nich nalezy dany punkt.

Zrobie 3 wersje tego samego klasyfikatora, z 1, 2 i 4 warstwami ansatzu, i porownam ich wyniki.

## Hipoteza

Zakladam, ze zwiekszenie liczby warstw z 1 do 2 poprawi accuracy na danych testowych o przynajmniej 5 punktow procentowych, ale przejscie z 2 do 4 warstw da juz mniej niz 3 punkty procentowe poprawy.

## Dlaczego tak mysle?

Kazda kolejna warstwa to dodatkowe rotacje RY i bramki CNOT. Daje to modelowi wiecej parametrow do trenowania i mozliwosc tworzenia bardziej zlozonych zaleznosci miedzy danymi.

Z drugiej strony wiecej warstw nie musi oznaczac lepszych wynikow. Mozliwe, ze po pewnym momencie dodatkowe parametry niewiele juz pomoga.

## Jak to sprawdze?

- Wygeneruje 120 punktow za pomoca make_moons
- Uzyje 2 kubitow, po jednym na kazda wspolrzedna punktu
- Zbuduje 3 modele w Qiskicie, rozniace sie liczba warstw
- Kazdy model wytrenuje 3 razy z roznymi poczatkowymi katami
- Porownam srednia skutecznosc na tych samych danych testowych i zrobie wykres

## Co by bylo gdyby?

Ciekawe, czy przy wiekszym szumie w danych dodatkowe warstwy nadal by pomagaly, czy moze bardziej rozbudowany model zaczalby sie gorzej sprawdzac na nowych punktach.

## Wyniki

Uzupelnie po eksperymencie.
