#wyzwanie 2

import numpy as np

#stan |0> i |1>
q0 = np.array([1.0, 0.0], dtype=complex)
q1 = np.array([0.0, 1.0], dtype=complex)

# bramki X Z H
X = np.array([[0, 1], 
              [1, 0]], dtype=complex)


Z = np.array([[1,  0], 
              [0, -1]], dtype=complex)

H = (1.0 / np.sqrt(2)) * np.array([[1,  1], 
                                   [1, -1]], dtype=complex)

# bramka rotacji 
def Ry(theta):
    return np.array([
        [np.cos(theta / 2.0), -np.sin(theta / 2.0)],
        [np.sin(theta / 2.0),  np.cos(theta / 2.0)]
    ], dtype=complex)

# bramka cnot
CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
], dtype=complex)

# pomiar kwantowy
def measure(state, shots=1000):
    # prawdopodobienstwo (|amplituda|^2)
    probs = np.abs(state) ** 2
    
    # nazwy wynikow
    if len(state) == 2:
        outcomes = ['0', '1']
    else:
        outcomes = ['00', '01', '10', '11']
    
    # losowanie shots wiynikow
    samples = np.random.choice(outcomes, size=shots, p=probs)
    
    # zliczenie
    wyniki = {}
    for x in outcomes:
        ile = np.sum(samples == x)
        if ile > 0:
            wyniki[x] = int(ile)
            
    return wyniki

# wyniki
test1 = H @ (H @ q0)
print("H * H |0> =", np.round(test1, 3))
print("czy |0>?:", np.allclose(test1, q0))



q0_po_H = H @ q0

psi_start = np.kron(q0_po_H, q0)

psi_bell = CNOT @ psi_start

print("wektor stanu bella:", np.round(psi_bell, 3))
wyniki_pomiaru = measure(psi_bell, shots=1000)
print("wynik 1000 pomiarow:", wyniki_pomiaru)