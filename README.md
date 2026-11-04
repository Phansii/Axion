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

Po uruchomieniu kodu dostalem takie srednie accuracy z 3 prob:

1 warstwa: 87.30%

2 warstwy: 84.92%

4 warstwy: 86.51%

Przejscie z 1 do 2 warstw pogorszylo wynik o 2.38 pp, natomiast z 2 do 4 poprawilo go o 1.59 pp.

Wnioski

Hipoteza potwierdzila sie tylko czesciowo. Zakladalem, ze dwie warstwy dadza lepszy wynik niz jedna, ale okazalo sie odwrotnie. Najprostszy model osiagnal najwyzsza srednia skutecznosc.

Mozliwe, ze dodatkowe parametry utrudnily trening, szczegolnie ze kazdy model mial taki sam limit optymalizacji. Nie mozna jednak stwierdzic tego na pewno na podstawie samych wynikow.

Wyglada na to, ze dodawanie kolejnych warstw nie gwarantuje lepszej klasyfikacji. Zeby lepiej to sprawdzic, przydaloby sie wykonac wiecej prob i zwiekszyc liczbe iteracji treningu.

Co by bylo gdyby?

Gdybym zwiekszyl szum w danych, punkty z obu klas bardziej by sie mieszaly, przez co klasyfikacja moglaby byc trudniejsza.

Bardziej rozbudowany model moglby wtedy mocniej dopasowywac sie do szumu w danych treningowych, zamiast uczyc sie ogolnej zaleznosci. Nie jest to jednak pewne i wymagaloby osobnego eksperymentu.
