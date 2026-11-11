import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from scipy.optimize import minimize
import matplotlib.pyplot as plt

#Import make moons
from sklearn.datasets import make_moons
coords, labels = make_moons(n_samples=1000, noise=0.15, random_state=47)

#Make moons visualisation to decide if noise is not too big
plt.scatter(coords[:,0],coords[:,1],c=labels)
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("make_moons.png", dpi=300)
plt.show(block=False)
plt.pause(1)

# Separating training data from test data
from sklearn.model_selection import train_test_split
train_coords, test_coords, train_labels, test_labels = train_test_split(coords, labels, test_size=0.2, random_state=47, stratify=labels)
#Min-Max scaling
minimum = train_coords.min(axis=0)
maximum = train_coords.max(axis=0)

train_coords = np.pi * (train_coords - minimum) / (maximum - minimum)
test_coords = np.pi * (test_coords - minimum) / (maximum - minimum)

# Quantum circuit
def quantum_model(point, trainable_angles, layers):
    qc = QuantumCircuit(2)

    # Encoding
    qc.ry(point[0], 0)
    qc.ry(point[1], 1)

    # Ansatz
    for i in range(layers):
        qc.ry(trainable_angles[2*i], 0)
        qc.ry(trainable_angles[2*i+1], 1)
        qc.cx(0, 1)

    qc.ry(trainable_angles[-1], 1)

    state = Statevector.from_instruction(qc)
    p = state.probabilities([1])

    return p[0] - p[1]

# Cost function
def cost_function(trainable_angles, layers):
    total_error = 0

    for i in range(len(train_coords)):
        prediction = quantum_model(train_coords[i], trainable_angles, layers)
        target = 1 - 2 * train_labels[i]

        total_error += (prediction - target)**2

    return total_error / len(train_coords)

def accuracy(trainable_angles, layers):
    correct = 0

    for i in range(len(test_coords)):
        prediction = quantum_model(test_coords[i], trainable_angles, layers)

        if int(prediction < 0) == test_labels[i]:
            correct += 1

    return 100 * correct / len(test_coords)

mean_accuracies = []

for layers in [1, 2, 4]:
    run_accuracies = []

    for seed in [3, 11, 29]:
        np.random.seed(seed)
        trainable_angles = np.random.uniform(-np.pi, np.pi, 2*layers+1)

        print(f"Training: {layers} layers, seed {seed}", flush=True)

        training = minimize(
            cost_function, trainable_angles,
            args=(layers,),
            method="COBYLA",
            options={"maxiter": 120}
        )

        score = accuracy(training.x, layers)
        run_accuracies.append(score)

        print(f"Accuracy: {score:.2f}%", flush=True)

    mean_accuracy = sum(run_accuracies) / len(run_accuracies)
    mean_accuracies.append(mean_accuracy)

    print(f"Mean accuracy: {mean_accuracy:.2f}%")


print("Improvement from 1 to 2 layers:", round(mean_accuracies[1] - mean_accuracies[0], 2), "pp")

print("Improvement from 2 to 4 layers:", round(mean_accuracies[2] - mean_accuracies[1], 2), "pp")



plt.plot([1, 2, 4], mean_accuracies, marker="o")

plt.xlabel("Layers")
plt.ylabel("Accuracy (%)")
plt.title("Accuracy vs Layers")

plt.xticks([1, 2, 4])
plt.ylim(75, 90)
plt.grid(True)

plt.savefig("accuracy_layers.png", dpi=300)
plt.show()