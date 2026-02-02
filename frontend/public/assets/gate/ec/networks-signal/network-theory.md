**Network Theory: Signal Flow in Networks**
======================================

### Introduction
-----------------

Network theory is a branch of electrical engineering that deals with the analysis and design of electronic circuits. In this topic, we focus on signal flow in networks, which is crucial for understanding how signals propagate through complex systems.

### Core Concepts
------------------

#### Nodes and Branches

A network consists of nodes (junctions) and branches (conductors). Each node can be either a current source or a voltage source. A branch has two terminals and can be either series or parallel with other branches.

#### Types of Signals

There are two types of signals in a network:

1. **Voltage signal**: The potential difference between two nodes.
2. **Current signal**: The flow of charge through a conductor.

### Key Formulas/Theorems
-------------------------

#### Ohm's Law

The resistance $R$ in ohms, current $I$ in amperes, and voltage $V$ in volts are related by:

$$V=IR \tag{1}$$

#### Kirchhoff's Laws

Kirchhoff's laws describe how signals interact at nodes.

* **Kirchhoff's Current Law (KCL)**: The sum of currents entering a node is equal to the sum of currents leaving it.
* **Kirchhoff's Voltage Law (KVL)**: The sum of voltage changes around any closed loop in a network is zero.

#### Nodal Analysis

Nodal analysis involves solving for the unknown nodes and then using KCL to find the branch currents.

### Problem Solving Patterns
---------------------------

1. **Identify the type of problem**: Determine if it's a voltage or current signal, and whether it's a series or parallel circuit.
2. **Draw a diagram**: Visualize the network using Mermaid diagrams (see below).
3. **Apply Kirchhoff's laws**: Use KCL and KVL to find unknown nodes and branch currents.

```mermaid
graph LR
  A[Node 1] -->|I1|> B[Branch]
  C[Node 2] -->|I2|> D[Node 3]
```

### Examples with Solutions
---------------------------

**Example 1: Simple Series Circuit**

Given a series circuit with a voltage source $V=10\,\text{V}$ and two resistors, one with $R_1=200\,\Omega$ and the other with $R_2=300\,\Omega$, find the current flowing through each resistor.

Using Ohm's Law (Equation 1), we can find the total resistance:

$$R_{\text{total}} = R_1 + R_2 = 500\,\Omega$$

Now, apply KVL to find the voltage across $R_2$:

$$V - IR_1 = IR_2 \Rightarrow I = \frac{10}{500} = 0.02\,\text{A}$$

**Solution:** Current through each resistor is $0.02\,\text{A}$.

### Common Pitfalls
------------------

* Failing to distinguish between series and parallel circuits.
* Misapplying Kirchhoff's laws or Ohm's Law.
* Not considering the type of signal (voltage or current) in the problem.

### Quick Summary
-----------------

* Network theory deals with signal flow in networks.
* Key concepts: nodes, branches, types of signals, Ohm's Law, and Kirchhoff's laws.
* Problem-solving involves identifying the type of circuit, applying Kirchhoff's laws, and using Ohm's Law to find unknowns.

Note: This is a comprehensive theory note covering all essential concepts for the GATE CS exam. It provides clear explanations, formulas, and examples to help students understand network signal flow in networks.