**Circuit Analysis**
=====================

### Introduction
-----------------

Circuit analysis is a fundamental topic in network theory that deals with the study of electric circuits to determine their electrical behavior. It involves using mathematical techniques and formulas to analyze and solve various circuit problems.

### Core Concepts
------------------

#### Kirchhoff's Laws
--------------------

Kirchhoff's laws are two fundamental principles used in circuit analysis:

1.  **Kirchhoff's Current Law (KCL)**: The sum of currents entering a node is equal to the sum of currents leaving the node.
2.  **Kirchhoff's Voltage Law (KVL)**: The sum of voltage changes around a closed loop is zero.

**Mathematical Representation**

*   KCL can be represented mathematically as:
    *   $I_1 + I_2 + ... + I_n = I_{total}$
*   KVL can be represented mathematically as:
    *   $\sum V_i = 0$

#### Thevenin's Theorem
------------------------

Thevenin's theorem states that any complex network can be replaced by a single voltage source (Vth) in series with a resistance (Rth).

**Mathematical Representation**

*   $V_{th} = V_a - I \cdot R_a$
*   $R_{th} = R_a$

#### Norton's Theorem
----------------------

Norton's theorem states that any complex network can be replaced by a single current source (In) in parallel with a resistance (Ron).

**Mathematical Representation**

*   $I_n = V_{in} / R_{in}$
*   $R_{n} = R_{in}$

### Key Formulas/Theorems
---------------------------

#### Ohm's Law
-----------------

Ohm's law relates the voltage, current, and resistance of an electric circuit.

**Mathematical Representation**

*   $V = I \cdot R$

#### Power Formula
-------------------

The power formula calculates the power dissipated in a resistor.

**Mathematical Representation**

*   $P = V \cdot I$ or $P = I^2 \cdot R$

### Problem Solving Patterns
------------------------------

1.  **Identify the circuit type**: Determine whether it's a series, parallel, or combination circuit.
2.  **Apply Kirchhoff's laws**: Use KCL and KVL to analyze the circuit.
3.  **Use Thevenin/Norton's theorem**: Convert complex networks into simpler equivalents.

### Examples with Solutions
---------------------------

1.  **Example 1: Series Circuit**

    *   Find the current flowing through a series circuit consisting of two resistors (R1 = 2kΩ, R2 = 3kΩ) and a voltage source (V = 5V).
    *   Solution:

        ```mermaid
        graph LR
        V -- "5V" --> |R1| (2kΩ) -- I --> |R2| (3kΩ)
        ```
    *   Applying Ohm's law to the circuit, we get:
        *   $I = \frac{V}{R_1 + R_2}$
        *   $I = \frac{5}{(2000+3000)}$
        *   $I = 0.66 mA$

    2.  **Example 2: Parallel Circuit**

        *   Find the current flowing through a parallel circuit consisting of two resistors (R1 = 10Ω, R2 = 20Ω) and a voltage source (V = 3V).
        *   Solution:

            ```mermaid
            graph LR
            V -- "3V" --> |R1| (10Ω) --- I1 --> |R2| (20Ω)
            ```
        *   Applying Ohm's law to the circuit, we get:
            *   $I_1 = \frac{V}{R_1}$
            *   $I_1 = \frac{3}{10}$
            *   $I_2 = \frac{V}{R_2}$
            *   $I_2 = \frac{3}{20}$
        *   The total current is the sum of the individual currents:
            *   $I_{total} = I_1 + I_2$

### Common Pitfalls
----------------------

*   **Incorrect application of Kirchhoff's laws**: Failing to apply KCL and KVL correctly can lead to incorrect results.
*   **Ignoring Thevenin/Norton's theorem**: Not converting complex networks into simpler equivalents can make problems harder to solve.

### Quick Summary
-------------------

Circuit analysis involves applying mathematical techniques and formulas to analyze electric circuits. Key concepts include Kirchhoff's laws, Thevenin's theorem, and Norton's theorem. By understanding these principles and practicing problem-solving skills, students can develop a strong foundation in circuit analysis.