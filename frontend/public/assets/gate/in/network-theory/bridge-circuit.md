**Bridge Circuit**
=================

### Introduction
-----------------

A bridge circuit is a type of electrical network consisting of four resistors connected in a diamond shape. It is commonly used to measure unknown resistance values and is a fundamental concept in network theory.

### Core Concepts
------------------

#### Thevenin's Theorem
Thevenin's theorem states that any linear electrical network can be replaced by an equivalent circuit consisting of a single voltage source (Vth) in series with a resistance (Rth).

![Thevenin's Equivalent Circuit](https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Thevenins_equivalent_circuit.svg/300px-Thevenins_equivalent_circuit.svg.png)

#### Norton's Theorem
Norton's theorem is similar to Thevenin's theorem, but it replaces the voltage source with a current source (In) in parallel with a resistance (Rn).

### Key Formulas/Theorems
---------------------------

*   *Thevenin Resistance:* $R_{th} = \frac{\Delta V}{\Delta I}$

    where $\Delta V$ is the open-circuit voltage across the load and $\Delta I$ is the short-circuit current through the load.
*   *Thevenin Voltage:* $V_{th} = V_{AB} - I_{L} R_L$

    where $V_{AB}$ is the open-circuit voltage across the load, $I_{L}$ is the short-circuit current through the load, and $R_L$ is the load resistance.

### Problem Solving Patterns
---------------------------

1.  **Identify the type of circuit**: Determine whether it's a series, parallel, or bridge circuit.
2.  **Apply Thevenin's theorem**: Replace the network with its equivalent Thevenin circuit.
3.  **Calculate unknown values**: Use the formulas and theorems to calculate the unknown resistance values.

### Examples with Solutions
---------------------------

**Example 1:**

Given a bridge circuit with resistors R1, R2, R3, and R4 connected in a diamond shape, find the value of R4 if the voltmeter V shows zero.

Solution:

```mermaid
graph LR
A[Thevenin Equivalent Circuit] --> B[Calculate Thevenin Resistance]
B --> C[Apply Ohm's Law]
C --> D[R4 = 99 ohms]
```

Using Thevenin's theorem, we replace the bridge circuit with its equivalent Thevenin circuit. We then calculate the Thevenin resistance using the given values.

$R_{th} = \frac{1}{\frac{1}{100} + \frac{1}{110}}$

We then apply Ohm's law to find the value of R4:

$\Delta V = V_{AB}$

### Common Pitfalls
------------------

*   **Incorrect application of Thevenin's theorem**: Make sure to replace the network with its equivalent Thevenin circuit.
*   **Miscalculation of unknown values**: Double-check your calculations and apply Ohm's law correctly.

### Quick Summary
---------------

*   Bridge circuits consist of four resistors connected in a diamond shape.
*   Apply Thevenin's theorem to simplify the circuit and calculate unknown resistance values.
*   Use the formulas and theorems provided to solve problems.