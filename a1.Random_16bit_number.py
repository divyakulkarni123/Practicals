from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(16, 16)

qc.h(range(16))
qc.measure(range(16), range(16))

sim = AerSimulator()
result = sim.run(transpile(qc, sim), shots=1).result()

print("Random 16-bit number:", list(result.get_counts())[0])
























#python -m pip install qiskit-aer
#python -m pip install qiskit

'''
# Experiment: Implementation of 16-Qubit Random Number Generator

## Aim:
To implement a 16-Qubit Random Number Generator using Quantum Computing and Qiskit.

## Theory:
A Quantum Random Number Generator (QRNG) is a system that generates random numbers using the principles of quantum mechanics.

A qubit (quantum bit) is the basic unit of quantum information. Unlike a classical bit, which can have either 0 or 1 value, a qubit can exist in a superposition of both states.

Superposition is a quantum phenomenon in which a qubit exists in a combination of states |0⟩ and |1⟩ until measurement.

The Hadamard gate (H) is used to create an equal superposition of 0 and 1. When applied to a qubit initially in state |0⟩, it gives a 50% probability of measuring 0 and a 50% probability of measuring 1.

In this experiment, we use 16 qubits and apply Hadamard gates to all qubits. Then, all qubits are measured to generate a random 16-bit binary number.

The total number of possible combinations is:

2^16 = 65536

Thus, the circuit can generate any one of 65,536 possible 16-bit binary numbers.

## Algorithm:
1. Import QuantumCircuit and transpile from Qiskit.
2. Import AerSimulator from Qiskit Aer.
3. Create a quantum circuit with 16 qubits and 16 classical bits.
4. Apply Hadamard gates to all 16 qubits.
5. Measure all qubits and store the results in classical bits.
6. Initialize the AerSimulator.
7. Transpile the quantum circuit for the simulator.
8. Execute the circuit using one shot.
9. Retrieve the measurement result.
10. Display the generated random 16-bit binary number.

## Code Explanation:

1. Import Libraries:
   - QuantumCircuit is used to create a quantum circuit.
   - Transpile converts the circuit into instructions suitable for the simulator.
   - AerSimulator is used to simulate quantum circuit execution.

2. Create Quantum Circuit:
   qc = QuantumCircuit(16, 16)
   This creates a circuit with 16 qubits and 16 classical bits.

3. Apply Hadamard Gate:
   qc.h(range(16))
   This applies the Hadamard gate to all 16 qubits and creates an equal superposition of 0 and 1.

4. Measurement:
   qc.measure(range(16), range(16))
   This measures all 16 qubits and stores their outcomes in corresponding classical bits.

5. Initialize Simulator:
   sim = AerSimulator()
   This creates a quantum simulator to execute the circuit.

6. Execute Circuit:
   result = sim.run(transpile(qc, sim), shots=1).result()
   This transpiles and executes the circuit once. The shots parameter specifies the number of executions.

7. Extract Random Number:
   random_number = list(result.get_counts().keys())[0]
   This extracts the generated 16-bit binary measurement result.

8. Display Binary Number:
   print("Random 16-bit number:", random_number)
   This displays the generated binary number.

9. Convert Binary to Decimal:
   print("Decimal number:", int(random_number, 2))
   This converts the binary number into its decimal equivalent using base 2.

## Output:
The program generates a random 16-bit binary number and displays its decimal equivalent. The output changes with each execution.

Example:
Random 16-bit number: 1011010010110101
Decimal number: 46261

## Applications:
1. Cryptography and secure key generation.
2. Secure password generation.
3. Quantum communication.
4. Scientific simulations.
5. Randomized algorithms.

## Conclusion:
Thus, we successfully implemented a 16-Qubit Random Number Generator using Qiskit. We applied Hadamard gates to create superposition, measured all 16 qubits, and generated a random 16-bit binary number along with its decimal equivalent.
'''
