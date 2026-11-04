from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(5, 3)

# Encode a quantum state using 3 qubits
qc.ry(1.0, 0)
qc.cx(0, 1)
qc.cx(0, 2)

# Introduce a bit-flip error on qubit 1
qc.x(1)

# Detect the error using two ancilla qubits
qc.cx(0, 3)
qc.cx(1, 3)
qc.cx(0, 4)
qc.cx(2, 4)

qc.measure(3, 0)
qc.measure(4, 1)

# Correct the error based on syndrome
with qc.if_test((qc.clbits[0], 1)):
    with qc.if_test((qc.clbits[1], 0)):
        qc.x(1)

with qc.if_test((qc.clbits[0], 0)):
    with qc.if_test((qc.clbits[1], 1)):
        qc.x(2)

with qc.if_test((qc.clbits[0], 1)):
    with qc.if_test((qc.clbits[1], 1)):
        qc.x(0)

qc.measure(0, 2)

sim = AerSimulator()
result = sim.run(transpile(qc, sim), shots=1024).result()

print("Error correction results:", result.get_counts())


















































'''
# Experiment: Tackle Noise with Error Correction

## Aim:
To implement quantum error detection and correction using a 3-Qubit Bit-Flip Error Correction Code in Qiskit.

## Theory:
Quantum computers are sensitive to noise and errors during computation. These errors can change the quantum state and affect the accuracy of the results.

Quantum Error Correction (QEC) is a technique used to detect and correct errors in quantum information without directly measuring the encoded quantum state.

In this experiment, we implement the 3-Qubit Bit-Flip Error Correction Code. It uses three data qubits and two ancilla qubits.

A bit-flip error occurs when a qubit changes from |0⟩ to |1⟩ or from |1⟩ to |0⟩. The Pauli-X gate is used to represent a bit-flip operation.

First, a quantum state is prepared using the Ry rotation gate. Then, CNOT gates are used to encode the information into three data qubits.

An artificial bit-flip error is introduced on qubit 1 using the X gate.

Two ancilla qubits are used to detect the error by measuring parity checks between the data qubits. The measurement results are called error syndromes.

Based on the syndrome, conditional X gates are applied to correct the error.

The circuit finally measures the corrected quantum information.

## Algorithm:
1. Import QuantumCircuit, transpile and AerSimulator.
2. Create a quantum circuit with 5 qubits and 3 classical bits.
3. Prepare the quantum state using the Ry gate.
4. Encode the quantum information using CNOT gates.
5. Introduce a bit-flip error using the Pauli-X gate on qubit 1.
6. Use two ancilla qubits to detect the error.
7. Measure the ancilla qubits to obtain the error syndrome.
8. Apply conditional X gates according to the syndrome.
9. Measure the corrected data qubit.
10. Execute the circuit using AerSimulator with 1024 shots.
11. Display the error correction results.

## Code Explanation:

1. Import Libraries:
   - QuantumCircuit is used to create a quantum circuit.
   - Transpile converts the circuit into instructions suitable for the simulator.
   - AerSimulator simulates quantum circuit execution.

2. Create Quantum Circuit:
   qc = QuantumCircuit(5, 3)
   Creates a circuit with 5 qubits and 3 classical bits. Three qubits store quantum information and two qubits act as ancilla qubits.

3. Prepare Quantum State:
   qc.ry(1.0, 0)
   Applies the Ry rotation gate to qubit 0 to prepare a quantum state.

4. Encode Quantum Information:
   qc.cx(0, 1)
   qc.cx(0, 2)
   Uses CNOT gates to encode information into three data qubits.

5. Introduce Bit-Flip Error:
   qc.x(1)
   Applies the Pauli-X gate to qubit 1 to intentionally introduce a bit-flip error.

6. Detect Error:
   qc.cx(0, 3)
   qc.cx(1, 3)
   qc.cx(0, 4)
   qc.cx(2, 4)
   Uses two ancilla qubits to perform parity checks and detect the location of the error.

7. Measure Error Syndrome:
   qc.measure(3, 0)
   qc.measure(4, 1)
   Measures the ancilla qubits and stores the syndrome in classical bits.

8. Correct the Error:
   Conditional X gates are applied based on the measured syndrome:
   - Syndrome 10: Correct qubit 1.
   - Syndrome 01: Correct qubit 2.
   - Syndrome 11: Correct qubit 0.
   - Syndrome 00: No error detected.

9. Final Measurement:
   qc.measure(0, 2)
   Measures the corrected data qubit and stores the result in the third classical bit.

10. Initialize Simulator:
    sim = AerSimulator()
    Creates a quantum simulator.

11. Execute Circuit:
    result = sim.run(transpile(qc, sim), shots=1024).result()
    Executes the circuit 1024 times and collects the measurement results.

12. Display Results:
    print("Error correction results:", result.get_counts())
    Displays the measurement counts obtained after error correction.

## Output:
Example output:

Error correction results: {'001': 791, '101': 233}

The output shows the measurement results obtained from 1024 circuit executions.

## Applications:
1. Reliable quantum computing.
2. Quantum communication.
3. Quantum information processing.
4. Fault-tolerant quantum computers.
5. Protection of quantum information against bit-flip errors.

## Conclusion:
Thus, we successfully implemented a 3-Qubit Bit-Flip Error Correction Code using Qiskit. We introduced an artificial bit-flip error, detected it using two ancilla qubits and corrected it using conditional Pauli-X gates.
'''
