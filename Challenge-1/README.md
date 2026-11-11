
# Challenge 1

## Dane

kaggle.com/datasets/mlg-ulb/creditcardfraud 

## Hipoteza

Myśle że model bez wag klas osiągnie wysokie accuracy, ale będzie miał problem z wykrywaniem oszustw, ponieważ jest ich znaczniej mniej.

Myśle że dodanie class_weight="balanced" zwiększy recall dla klasy oszustw.

## Proces

Do sprawdzenia hipotezy uzyłem regresji logistycznej.

Podzieliłem dane na 80% treningowych i 20% testowych i porównałem dwa modele:
Model bez wag klas
Model z class_weight="balanced"

Oba modele trenowałem na tych samych danych, a następnie porównałem ich accuracy recall oraz balanced accuracy.

## Wyniki

```
Model without class weights
Accuracy: 99.93 %
Recall: 69.39 %
Balanced accuracy: 84.69 %

Model with balanced class weights
Accuracy: 97.67 %
Recall: 91.84 %
Balanced accuracy: 94.76 %
```

## Wnioski

Moja hipoteza się potwierdziła.

Model bez wag klas osiągnął bardzo wysokie accuracy 99,93% ale ma niski recall

Po zrobieniu class_weight="balanced" recall wzrósł z 69,39% do 91,84%

Jednocześnie accuracy spadło z 99,93% do 97,67%.

Wyniki pokazują, że przy mocno niezbalansowanych danych samo accuracy może być mylące
