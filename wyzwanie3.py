
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from scipy.optimize import minimize


# generujemy 120 punktow w dwa polksiezyce
punkty, klasy = make_moons(n_samples=120, noise=0.17, random_state=2026)

# dzielimy punkty na trening i test
x_train, x_test, y_train, y_test = train_test_split(
    punkty, klasy, test_size=0.35, random_state=42, stratify=klasy
)

# skalujemy wspolrzedne do katow od 0 do pi
minimum = x_train.min(axis=0)
maksimum = x_train.max(axis=0)

x_train = np.pi * np.clip((x_train - minimum) / (maksimum - minimum), 0, 1)
x_test = np.pi * np.clip((x_test - minimum) / (maksimum - minimum), 0, 1)


# nasz obwod kwantowy
def obwod(punkt, katy, warstwy):
    qc = QuantumCircuit(2)

    # encoding
    qc.ry(punkt[0], 0)
    qc.ry(punkt[1], 1)

    # ansatz
    for i in range(warstwy):
        qc.ry(katy[2*i], 0)
        qc.ry(katy[2*i+1], 1)
        qc.cx(0, 1)

    qc.ry(katy[-2], 0)
    qc.ry(katy[-1], 1)

    # liczymy prawdopodobienstwa pomiaru kubitu 1
    stan = Statevector.from_instruction(qc)
    p = stan.probabilities([1])

    return p[0] - p[1]


# liczymy blad modelu
def blad(katy, warstwy):
    suma = 0

    for i in range(len(x_train)):
        wynik = obwod(x_train[i], katy, warstwy)
        poprawny = 1 - 2 * y_train[i]

        suma += (wynik - poprawny)**2

    return suma / len(x_train)


# sprawdzamy ile punktow model rozpoznal poprawnie
def skutecznosc(katy, warstwy):
    dobrze = 0

    for i in range(len(x_test)):
        wynik = obwod(x_test[i], katy, warstwy)

        if int(wynik < 0) == y_test[i]:
            dobrze += 1

    return 100 * dobrze / len(x_test)


# testujemy 1, 2 i 4 warstwy
srednie = []

for warstwy in [1, 2, 4]:
    wyniki = []

    for seed in [3, 11, 29]:
        np.random.seed(seed)
        katy = np.random.uniform(-np.pi, np.pi, 2*warstwy+2)

        trening = minimize(
            blad, katy,
            args=(warstwy,),
            method="COBYLA",
            options={"maxiter": 120}
        )

        accuracy = skutecznosc(trening.x, warstwy)
        wyniki.append(accuracy)

        print(warstwy, "warstw, proba", seed, ":", round(accuracy, 2), "%")

    srednia = sum(wyniki) / len(wyniki)
    srednie.append(srednia)

    print("Srednia:", round(srednia, 2), "%\n")


# porownanie wynikow z hipoteza
print("Poprawa 1 do 2 warstw:", round(srednie[1] - srednie[0], 2), "pp")
print("Poprawa 2 do 4 warstw:", round(srednie[2] - srednie[1], 2), "pp")
