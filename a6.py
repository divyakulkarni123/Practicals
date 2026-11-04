from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import QFT
from qiskit_aer import AerSimulator

qc = QuantumCircuit(5, 5)

qc.h(0)
qc.x(1)

qc.compose(QFT(5), inplace=True)
qc.measure(range(5), range(5))

sim = AerSimulator()
result = sim.run(transpile(qc, sim), shots=1024).result()

print("QFT results:", result.get_counts())






















'''
# Practical No. 06: Implementation of Quantum Fourier Transform using Qiskit

## Aim:
To implement the Quantum Fourier Transform (QFT) on a 5-qubit quantum circuit using Qiskit and observe the measurement results using a quantum simulator.

## Theory:

The Quantum Fourier Transform (QFT) is a quantum algorithm that transforms a quantum state from the computational basis into the Fourier basis.

It is the quantum equivalent of the classical Discrete Fourier Transform (DFT). It is widely used in quantum computing algorithms such as Shor's factoring algorithm and Quantum Phase Estimation.

In this experiment, we use 5 qubits to implement the Quantum Fourier Transform.

Initially, a quantum circuit with 5 qubits and 5 classical bits is created. Hadamard and Pauli-X gates are applied to prepare the initial quantum state.

The QFT is then applied using Qiskit's built-in QFT function. It transforms the input quantum state into a superposition of different quantum states with different phases.

The QFT uses the following quantum gates:

1. Hadamard Gate (H): Creates superposition of quantum states.
2. Controlled Phase Gate (CP): Introduces phase rotations depending on the state of another qubit.
3. Swap Gate: Reverses the order of qubits when required.

After applying QFT, all five qubits are measured and the results are stored in classical bits.

The quantum circuit is executed using the AerSimulator with 1024 shots. The measurement counts represent the frequency of different output states.

## Algorithm:

1. Import QuantumCircuit and transpile from Qiskit.
2. Import QFT from qiskit.circuit.library.
3. Import AerSimulator from qiskit_aer.
4. Create a quantum circuit with 5 qubits and 5 classical bits.
5. Apply a Hadamard gate to qubit 0.
6. Apply a Pauli-X gate to qubit 1.
7. Apply the 5-qubit Quantum Fourier Transform.
8. Measure all five qubits.
9. Initialize the AerSimulator.
10. Transpile and execute the circuit using 1024 shots.
11. Retrieve the measurement counts.
12. Display the QFT measurement results.

## Code Explanation:

1. Import Libraries:
   - QuantumCircuit is used to create a quantum circuit.
   - Transpile converts the circuit into instructions suitable for the simulator.
   - QFT is used to perform the Quantum Fourier Transform.
   - AerSimulator simulates quantum circuit execution.

2. Create Quantum Circuit:
   qc = QuantumCircuit(5, 5)
   Creates a quantum circuit containing 5 qubits and 5 classical bits.

3. Apply Hadamard Gate:
   qc.h(0)
   Applies a Hadamard gate to qubit 0 and creates superposition.

4. Apply Pauli-X Gate:
   qc.x(1)
   Applies a bit-flip operation to qubit 1, changing its state from |0⟩ to |1⟩.

5. Apply Quantum Fourier Transform:
   qc.compose(QFT(5), inplace=True)
   Applies the 5-qubit Quantum Fourier Transform to the quantum circuit.

6. Measurement:
   qc.measure(range(5), range(5))
   Measures all five qubits and stores the results in classical bits.

7. Initialize Simulator:
   sim = AerSimulator()
   Creates a quantum simulator for executing the circuit.

8. Execute Circuit:
   result = sim.run(transpile(qc, sim), shots=1024).result()
   Transpiles and executes the quantum circuit 1024 times.

9. Display Results:
   print("QFT results:", result.get_counts())
   Displays the measurement outcomes and their occurrence counts.

## Output:

The program displays the measurement counts of different 5-bit binary states after applying the Quantum Fourier Transform.

The output may contain multiple binary states with different measurement counts because QFT produces a superposition of quantum states.

## Applications:

1. Quantum Phase Estimation.
2. Shor's Factoring Algorithm.
3. Period Finding.
4. Quantum Signal Processing.
5. Quantum Information Processing.

## Conclusion:

Thus, we successfully implemented a 5-Qubit Quantum Fourier Transform using Qiskit. We prepared the initial quantum state using Hadamard and Pauli-X gates, applied the QFT operation, and measured the output using AerSimulator with 1024 shots.
'''
