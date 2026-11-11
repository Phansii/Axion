
import numpy as np

# Quantum states
state_0 = np.array([1.0, 0.0], dtype=complex)
state_1 = np.array([0.0, 1.0], dtype=complex)

# Quantum gates
X = np.array([
    [0, 1],
    [1, 0]
], dtype=complex)

Z = np.array([
    [1,  0],
    [0, -1]
], dtype=complex)

H = (1 / np.sqrt(2)) * np.array([
    [1,  1],
    [1, -1]
], dtype=complex)

# Rotation gate
def ry(theta):
    return np.array([
        [np.cos(theta / 2), -np.sin(theta / 2)],
        [np.sin(theta / 2),  np.cos(theta / 2)]
    ], dtype=complex)

# CNOT gate
CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
], dtype=complex)

# Quantum measurement
def measure(state, shots=1000):
    probabilities = np.abs(state)**2

    if len(state) == 2:
        outcomes = ["0", "1"]
    else:
        outcomes = ["00", "01", "10", "11"]

    samples = np.random.choice(outcomes, size=shots, p=probabilities)

    results = {}
    for outcome in outcomes:
        count = np.sum(samples == outcome)

        if count > 0:
            results[outcome] = int(count)

    return results


# Test 1: H * H |0>
test_state = H @ (H @ state_0)

print("H * H |0> =", np.round(test_state, 3))
print("Equal to |0>:", np.allclose(test_state, state_0))


# Test 2: Bell state
state_after_h = H @ state_0
initial_state = np.kron(state_after_h, state_0)

bell_state = CNOT @ initial_state

print("Bell state:", np.round(bell_state, 3))

measurement_results = measure(bell_state, shots=1000)
print("Measurement results:", measurement_results)
