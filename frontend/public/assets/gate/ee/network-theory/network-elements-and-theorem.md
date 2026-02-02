**Network Theory: Network Elements and Theorems**
=====================================================

### Introduction
---------------

Network theory is a fundamental subject in electrical engineering that deals with the analysis and design of electrical networks. It involves the study of circuit elements, such as resistors, capacitors, and inductors, and their interactions. This note will cover the essential concepts, formulas, and theorems required to solve problems related to network theory.

### Core Concepts
----------------

*   **Circuit Elements**:
    *   Resistors (R): A resistor is a component that opposes the flow of current.
    *   Capacitors (C): A capacitor stores energy in an electric field.
    *   Inductors (L): An inductor stores energy in a magnetic field.
*   **Kirchhoff's Laws**:
    *   Kirchhoff's Current Law (KCL): The sum of currents entering a node is equal to the sum of currents leaving the node.
    *   Kirchhoff's Voltage Law (KVL): The sum of voltage changes around a closed loop is zero.

### Key Formulas/Theorems
-------------------------

*   **Ohm's Law**: $V = IR$
*   **Kirchhoff's Laws**:
    *   KCL: $\sum I_i = \sum I_o$
    *   KVL: $\sum V_{ij} = 0$
*   **Impedance**:
    *   Impedance ($Z$) is a measure of the total opposition to current flow in an AC circuit.
    *   $Z = R + jX$, where $R$ is resistance and $X$ is reactance.

### Problem Solving Patterns
-----------------------------

*   **Solve for Currents**: Use KCL to solve for currents in a circuit.
*   **Solve for Voltages**: Use KVL to solve for voltages in a circuit.
*   **Use Impedance**: Calculate impedance using Ohm's Law and reactance.

### Examples with Solutions
---------------------------

**Example 1:** Find the current through a resistor (R = 10Ω) in a series circuit with a voltage source (V = 20V).

```markdown
Solution:

Using Ohm's Law, we can find the current through the resistor:
I = V/R
= 20V / 10Ω
= 2A

The answer is I = 2A.
```

### Common Pitfalls
-------------------

*   **Forget to apply KCL or KVL**: Always apply Kirchhoff's Laws when solving circuit problems.
*   **Not accounting for impedance**: Consider impedance when analyzing AC circuits.

### Quick Summary
-----------------

*   Circuit elements: resistors, capacitors, inductors
*   Kirchhoff's Laws: KCL and KVL
*   Impedance: a measure of opposition to current flow
*   Problem solving patterns: solve for currents and voltages using KCL and KVL

**Mermaid Diagrams**

```mermaid
graph LR;
    A[Node] -->|I1|> B[Resistor];
    A -->|I2|> C[Capacitor];
```

Note: This diagram illustrates the flow of current through a node, resistor, and capacitor.

References:

*   Wikipedia: Network theory
*   Wikipedia: Kirchhoff's laws