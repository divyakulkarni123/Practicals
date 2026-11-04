# Tarrataca's Quantum Production System for the 3-puzzle (2x2 board, 0 = blank) - Qiskit version
# Register: 2 qubits per step (the production rule: 0=up 1=down 2=left 3=right) x DEPTH steps.
# Hadamards -> superposition of all rule sequences; oracle marks sequences that reach the goal; Grover diffusion.
# pip install qiskit qiskit-aer
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

START, GOAL, DEPTH = (3, 1, 0, 2), (1, 2, 3, 0), 3     # board cells: [0 1 / 2 3]
NAMES, SHIFT = ["up", "down", "left", "right"], [-2, 2, -1, 1]

def apply(state, rule):                                 # production rule (None = not applicable)
    b = state.index(0); n = b + SHIFT[rule]
    if not 0 <= n < 4 or (rule >= 2 and n // 2 != b // 2): return None
    s = list(state); s[b], s[n] = s[n], s[b]
    return tuple(s)

def decode(k):                                          # basis state k -> list of rules (2 bits each)
    return [(k >> (2 * i)) & 3 for i in range(DEPTH)]

def reaches_goal(k):
    s = START
    for r in decode(k):
        s = apply(s, r)
        if s is None: return False
    return s == GOAL

n = 2 * DEPTH
marked = [k for k in range(2 ** n) if reaches_goal(k)]  # classical check used to build the oracle
print("Solutions (basis states):", marked)

# Oracle: phase flip (-1) on every marked basis state, built from X + multi-controlled Z gates
oracle = QuantumCircuit(n)
for k in marked:
    zeros = [i for i in range(n) if not (k >> i) & 1]
    if zeros: oracle.x(zeros)
    oracle.h(n - 1); oracle.mcx(list(range(n - 1)), n - 1); oracle.h(n - 1)   # multi-controlled Z
    if zeros: oracle.x(zeros)

# Diffusion: H, X, multi-controlled Z, X, H  (inversion about the mean)
diffusion = QuantumCircuit(n)
diffusion.h(range(n)); diffusion.x(range(n))
diffusion.h(n - 1); diffusion.mcx(list(range(n - 1)), n - 1); diffusion.h(n - 1)
diffusion.x(range(n)); diffusion.h(range(n))

# Grover circuit
qc = QuantumCircuit(n)
qc.h(range(n))                                          # superposition of all rule sequences
iters = int(np.pi / 4 * np.sqrt(2 ** n / len(marked)))
for _ in range(iters):
    qc.compose(oracle, inplace=True)                    # 1) oracle
    qc.compose(diffusion, inplace=True)                 # 2) diffusion
qc.measure_all()

counts = AerSimulator().run(transpile(qc, AerSimulator()), shots=1024).result().get_counts()
best = max(counts, key=counts.get)
print("Grover iterations:", iters, "| top results:", dict(sorted(counts.items(), key=lambda x: -x[1])[:3]))
print("Solution moves:", [NAMES[r] for r in decode(int(best, 2))])






'''Experiment: Implementation of Tarrataca's Quantum Production System with the 3-Puzzle Problem
Your code implements a quantum-inspired search approach using Grover's Algorithm to find a sequence of production rules that transforms the initial 3-puzzle configuration into the goal configuration.
Output matches the code's expected solution
1. Aim
To implement Tarrataca's Quantum Production System for solving the 3-Puzzle Problem using Qiskit and Grover's Search Algorithm.
2. Theory
Tarrataca's Quantum Production System is a quantum computing approach used to solve problems by representing production rules as quantum states and searching for a solution using quantum algorithms.

The 3-Puzzle Problem consists of a 2×2 board containing three numbered tiles (1, 2, 3) and one blank space (0). The objective is to transform the initial state into the goal state by moving the blank space.

The system uses four production rules:
1. Up – Move the blank space upward.
2. Down – Move the blank space downward.
3. Left – Move the blank space left.
4. Right – Move the blank space right.
Each production rule is represented using 2 qubits because 2 qubits can represent four possible actions (00, 01, 10, 11).

For a search depth of 3, a total of 6 qubits are required to represent three consecutive production rules.

Hadamard gates are applied to create a superposition of all possible rule sequences. An oracle identifies the sequences that reach the goal state by applying a phase flip to the valid solutions.

Grover's diffusion operator amplifies the probability of measuring the correct solution sequences.

Finally, the quantum simulator executes the circuit and returns measurement results. The sequence with the highest measurement count is selected as the solution.
3. Algorithm
1. Import NumPy and Qiskit libraries.
2. Define the initial state, goal state and search depth.
3. Define four production rules: Up, Down, Left and Right.
4. Create a function to apply the production rules to the puzzle.
5. Encode each production rule using 2 qubits.
6. Generate all possible production rule sequences.
7. Identify sequences that reach the goal state.
8. Create an oracle to mark valid solution sequences.
9. Create the Grover diffusion operator.
10. Apply Hadamard gates to create superposition.
11. Execute Grover's algorithm for the calculated number of iterations.
12. Measure the quantum circuit.
13. Run the circuit using AerSimulator.
14. Display the solution moves and measurement results.
4. Code Explanation
1. Import Libraries
- numpy: Used for mathematical calculations.
- QuantumCircuit: Used to create quantum circuits.
- AerSimulator: Used to simulate quantum circuit execution.
- transpile: Converts the circuit into instructions suitable for the simulator.
2. Define Initial and Goal States
START, GOAL, DEPTH = (3, 1, 0, 2), (1, 2, 3, 0), 3



- START represents the initial puzzle configuration.
- GOAL represents the required final configuration.
- DEPTH specifies the number of production rule steps.
3. Define Production Rules
NAMES, SHIFT = ["up", "down", "left", "right"], [-2, 2, -1, 1]



Defines four possible movements of the blank space in the 2×2 puzzle.

4. Apply Production Rules
def apply(state, rule):



This function applies a selected movement to the puzzle. It checks whether the movement is valid and returns the updated puzzle state. If the movement is invalid, it returns None.

5. Decode Production Rules
def decode(k):    return [(k >> (2 * i)) & 3 for i in range(DEPTH)]



Converts a binary basis-state number into a sequence of three production rules using 2 bits per rule.

6. Check Goal State
def reaches_goal(k):



Checks whether a particular sequence of production rules transforms the initial puzzle state into the goal state.

7. Calculate Marked States
marked = [k for k in range(2 ** n) if reaches_goal(k)]



Checks all possible rule sequences and stores the sequences that reach the goal state.

8. Create Oracle

The oracle marks valid solution sequences by applying a phase flip to their quantum states. It uses X gates and multi-controlled Z operations.

9. Create Diffusion Operator

The diffusion operator amplifies the probability of marked solution states using Hadamard gates, X gates and multi-controlled operations. It performs inversion about the mean.

10. Create Grover Circuit
qc = QuantumCircuit(n)qc.h(range(n))



Creates a quantum circuit and applies Hadamard gates to all qubits to generate a superposition of possible rule sequences.

11. Calculate Grover Iterations
iters = int(np.pi / 4 * np.sqrt(2 ** n / len(marked)))



Calculates the approximate number of Grover iterations required to amplify the probability of measuring a valid solution.

12. Apply Oracle and Diffusion
for _ in range(iters):    qc.compose(oracle, inplace=True)    qc.compose(diffusion, inplace=True)



Repeatedly applies the oracle and diffusion operator to increase the probability of obtaining valid solutions.

13. Measure Quantum Circuit
qc.measure_all()



Measures all qubits and stores the results in classical bits.

14. Execute Circuit
counts = AerSimulator().run(    transpile(qc, AerSimulator()), shots=1024).result().get_counts()



Executes the quantum circuit 1024 times using the AerSimulator and collects the measurement counts.

15. Display Solution
best = max(counts, key=counts.get)



Finds the measurement result with the highest occurrence.
print("Solution moves:", [NAMES[r] for r in decode(int(best, 2))])



Converts the selected result into production rule names and displays the solution moves.
5. Output
Example output:
Solutions (basis states): [28]

Grover iterations: 6 | top results:
{'011100': 1018, '010100': 2, '000111': 1}

Solution moves: ['up', 'right', 'down']


The solution moves transform the initial puzzle configuration into the goal configuration.
6. Applications
1. Artificial Intelligence and problem-solving.
2. Quantum search algorithms.
3. State-space search.
4. Planning and decision-making systems.
5. Optimization problems.
7. Conclusion
Thus, we successfully implemented Tarrataca's Quantum Production System for the 3-Puzzle Problem using Qiskit. We represented production rules using qubits, created an oracle to identify valid solutions, and used Grover's Search Algorithm to amplify the probability of obtaining the solution sequence.
'''