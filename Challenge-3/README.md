
# Challenge 3

## Hipoteza

Chcę sprawdzić, czy zwiększenie liczby warstw w obwodzie kwantowym rzeczywiście poprawia skuteczność modelu.

Moim zdaniem zwiększenie liczby warstw w obwodzie kwantowym powinno poprawić skuteczność klasyfikatora.

Spodziewam się, że model z 4 warstwami osiągnie średnie accuracy wyższe niż model z 1 warstwą.

## Wyjaśnienie

Każda dodatkowa warstwa zawiera kolejne bramki i parametry, które model może dopasować podczas treningu.

Wydaje mi się więc, że większa liczba warstw powinna pozwolić modelowi lepiej rozdzielać dane, szczególnie kiedy klasy nie są oddzielone prostą linią, tak jak w make moons.

## Jak to zrobie?

Do sprawdzenia hipotezy wykorzystam zbiór make_moons mający 1000 sampli, z noise 0.15.

## Wyniki

potem
