
# Practical No. 04
# Implementation of Quantum Teleportation Algorithm using Qiskit

# Requirements:
# pip install qiskit qiskit-aer

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create quantum circuit with 3 qubits and 3 classical bits
qc = QuantumCircuit(3, 3)

# Step 1: Prepare the quantum state to be teleported
qc.h(0)
qc.t(0)

# Step 2: Create an entangled Bell pair
qc.h(1)
qc.cx(1, 2)

# Step 3: Perform Bell-state measurement operations
qc.cx(0, 1)
qc.h(0)

# Step 4: Measure the first two qubits
qc.measure(0, 0)
qc.measure(1, 1)

# Step 5: Apply conditional corrections
# Apply X gate if classical bit 1 is 1
with qc.if_test((qc.clbits[1], 1)):
    qc.x(2)

# Apply Z gate if classical bit 0 is 1
with qc.if_test((qc.clbits[0], 1)):
    qc.z(2)

# Step 6: Measure the teleported qubit
qc.measure(2, 2)

# Display quantum circuit
print(qc.draw())

# Step 7: Execute using quantum simulator
sim = AerSimulator()
result = sim.run(
    transpile(qc, sim),
    shots=1
).result()

# Step 8: Display measurement result
print("Measurement result:", list(result.get_counts().keys())[0])


















'''# Practical No. 04: Implementation of Quantum Teleportation Algorithm in Python

## Aim:
To implement the Quantum Teleportation Algorithm in Python using Qiskit, transferring the quantum state of one qubit to another using an entangled Bell pair, classical measurement and conditional corrections.

## Theory:

Quantum Teleportation is a quantum communication technique used to transfer the quantum state of one qubit to another distant qubit without physically transferring the original qubit.

It uses three qubits, quantum entanglement, classical communication and quantum gates to achieve state transfer.

In this experiment, three qubits are used:
- Qubit 0: Contains the original quantum state to be teleported.
- Qubit 1: Alice's entangled qubit.
- Qubit 2: Bob's qubit, which receives the teleported quantum state.

First, the original quantum state is prepared using Hadamard and T gates. Then, an entangled Bell pair is created between qubits 1 and 2 using a Hadamard gate and a CNOT gate.

Next, Bell-state measurement operations are performed using CNOT and Hadamard gates on qubits 0 and 1. These two qubits are measured, and the measurement results are sent through classical bits.

Based on the measurement results, conditional X and Z gates are applied to qubit 2 to correct its state.

Finally, qubit 2 is measured to verify the teleportation process.

The quantum teleportation algorithm demonstrates how quantum information can be transferred using entanglement and classical communication.

## Important Quantum Gates Used:

1. Hadamard Gate (H): Creates superposition of quantum states.
2. T Gate: Applies a phase rotation of 45 degrees to a qubit.
3. CNOT Gate: Performs a controlled bit-flip operation and helps create entanglement.
4. Pauli-X Gate: Performs bit-flip correction.
5. Pauli-Z Gate: Performs phase-flip correction.

## Algorithm:

1. Import QuantumCircuit, transpile and AerSimulator from Qiskit.
2. Create a quantum circuit with 3 qubits and 3 classical bits.
3. Prepare the original quantum state using Hadamard and T gates.
4. Create an entangled Bell pair using a Hadamard gate and CNOT gate.
5. Apply a CNOT gate between the original qubit and Alice's qubit.
6. Apply a Hadamard gate to the original qubit.
7. Measure the first two qubits and store the results in classical bits.
8. Apply a conditional X gate based on the measurement result.
9. Apply a conditional Z gate based on the measurement result.
10. Measure Bob's qubit to verify the teleported state.
11. Execute the circuit using AerSimulator.
12. Display the measurement result.

## Output:

The program displays the quantum circuit and the final measurement result.

Example:
Measurement result: 010

The measurement result may vary because quantum measurement is probabilistic.

## Applications:

1. Quantum communication.
2. Quantum networking.
3. Quantum information transfer.
4. Quantum cryptography.
5. Distributed quantum computing.

## Conclusion:

Thus, we successfully implemented the Quantum Teleportation Algorithm using Python and Qiskit. We prepared a quantum state, created an entangled Bell pair, performed Bell-state measurements and applied conditional X and Z corrections to transfer the quantum state to another qubit.
'''