
# Practical No. 05
# Implementing a 5-Qubit Quantum Fourier Transform (QFT)

# Requirements:
# pip install qiskit qiskit-aer

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from math import pi

n = 5

# Function to implement Quantum Fourier Transform
def qft(qc):
    for j in range(n-1, -1, -1):
        qc.h(j)
        for k in range(j-1, -1, -1):
            qc.cp(pi / (2 ** (j-k)), k, j)

    # Swap qubits to reverse their order
    for i in range(n // 2):
        qc.swap(i, n-i-1)


# Function to implement Inverse Quantum Fourier Transform
def inverse_qft(qc):
    # Reverse the qubit order
    for i in range(n // 2):
        qc.swap(i, n-i-1)

    for j in range(n):
        for k in range(j):
            qc.cp(-pi / (2 ** (j-k)), k, j)
        qc.h(j)


# Create quantum circuit with 5 qubits and 5 classical bits
qc = QuantumCircuit(n, n)

# Define input state
input_state = "10110"

# Encode input state into qubits
for i, bit in enumerate(input_state[::-1]):
    if bit == '1':
        qc.x(i)

# Apply Quantum Fourier Transform
qft(qc)

qc.barrier()

# Apply Inverse Quantum Fourier Transform
inverse_qft(qc)

# Measure all qubits
qc.measure(range(n), range(n))

# Display quantum circuit
print(qc.draw())

# Execute circuit using simulator
sim = AerSimulator()
result = sim.run(
    transpile(qc, sim),
    shots=1024
).result()

# Display input and measurement result
print("Input state:", input_state)
print("Measurement result:", result.get_counts())


'''
# Experiment: Implementing a 5-Qubit Quantum Fourier Transform

## Aim:
To implement a 5-qubit Quantum Fourier Transform (QFT) in Qiskit using Hadamard, controlled-phase and swap gates, and verify it by applying the QFT followed by its inverse to a basis state and recovering the original input on measurement.

## Theory:

The Quantum Fourier Transform (QFT) is a quantum algorithm that transforms a quantum state from the computational basis into the Fourier basis.

It is the quantum version of the classical Discrete Fourier Transform (DFT). QFT is used in important quantum algorithms such as Shor's algorithm and quantum phase estimation.

In this experiment, we use 5 qubits to implement the Quantum Fourier Transform.

The QFT converts the input quantum state into a superposition of different quantum states with different phases.

The following quantum gates are used:

1. Hadamard Gate (H): Creates superposition by transforming a qubit into an equal combination of |0⟩ and |1⟩.

2. Controlled Phase Gate (CP): Applies a phase rotation to a target qubit depending on the state of the control qubit.

3. Swap Gate: Exchanges the positions of two qubits to reverse their order.

The Quantum Fourier Transform is applied to the input state 10110. After that, the Inverse Quantum Fourier Transform (IQFT) is applied to recover the original state.

Finally, all five qubits are measured to verify whether the original input state is recovered.

Since QFT and IQFT are inverse operations, the original input state should be obtained after applying both transformations.

## Algorithm:

1. Import QuantumCircuit, transpile, AerSimulator and pi.
2. Define the number of qubits as 5.
3. Create a quantum circuit with 5 qubits and 5 classical bits.
4. Define the input state as 10110.
5. Encode the input state using Pauli-X gates.
6. Apply Hadamard gates to create superposition.
7. Apply controlled-phase gates to introduce phase rotations.
8. Apply swap gates to reverse the qubit order.
9. Apply the Inverse Quantum Fourier Transform.
10. Measure all five qubits.
11. Execute the circuit using AerSimulator with 1024 shots.
12. Display the input state and measurement results.

## Output:

Input state: 10110

Measurement result: {'10110': 1024}

## Applications:

1. Quantum phase estimation.
2. Shor's factoring algorithm.
3. Quantum signal processing.
4. Quantum computing and information processing.
5. Period finding algorithms.

## Conclusion:

Thus, we successfully implemented a 5-Qubit Quantum Fourier Transform using Qiskit. We applied Hadamard, controlled-phase and swap gates to perform QFT, followed by its inverse. The original input state 10110 was successfully recovered after measurement.
'''
