# Synchronous Machine
======================

### Introduction

A synchronous machine is an electrical machine that operates at a constant speed and frequency, producing a synchronized output. It consists of two main parts: the stator (stationary part) and the rotor (rotating part). The rotor is connected to a prime mover such as a turbine or engine, which drives the rotation.

### Core Concepts

#### Principles of Operation

A synchronous machine operates on the principle of electromagnetic induction between the stator windings and the rotor. The rotating magnetic field produced by the stator induces a current in the rotor, causing it to rotate at the same speed as the stator.

#### Key Features

*   **Constant Speed**: Synchronous machines operate at a constant speed, which is determined by the frequency of the output.
*   **No Slip**: Unlike induction motors, synchronous machines do not experience slip (the difference between the rotor and stator speeds).
*   **High Power Rating**: Synchronous machines are designed for high-power applications and can be used as generators or motors.

### Key Formulas/Theorems

#### Per-Unit System

The per-unit system is a method of normalizing quantities such as voltage, current, and impedance to a common base. It is commonly used in power systems to simplify calculations and comparisons.

$$E_{pu} = \frac{E}{V_{base}}$$
$$X_{s,pu} = \frac{X_s}{X_{base}}$$

#### Synchronous Reactance

Synchronous reactance is a measure of the opposition to current flow in a synchronous machine. It is represented by the symbol $X_s$.

$$X_s = \frac{E}{I}$$

### Problem Solving Patterns

#### Analyzing Short Circuit Faults

When analyzing short circuit faults in synchronous machines, it's essential to consider the subtransient and transient reactances.

*   **Subtransient Reactance**: The subtransient reactance is the opposition to current flow immediately after a fault occurs. It is represented by the symbol $X''_{d}$.
*   **Transient Reactance**: The transient reactance is the opposition to current flow after the initial response has subsided. It is represented by the symbol $X'_{d}$.

#### Sequence Voltages

Sequence voltages are used to analyze the behavior of three-phase systems. They can be represented as:

$$\begin{bmatrix} V_{a}\\ V_{b}\\ V_{c}\end{bmatrix} = \begin{bmatrix} 1 & 1 & 1\\ 1 & a & a^2\\ 1 & a^2 & a\end{bmatrix} \begin{bmatrix} V_0\\ V_1\\ V_2\end{bmatrix}$$

where $a = e^{j120^\circ}$.

### Examples with Solutions

#### Example 1: Short Circuit Fault Analysis

A synchronous generator has a steady-state synchronous reactance of 0.7 pu and subtransient reactance of 0.2 pu. It is operating at (1+0) pu terminal voltage with an internal emf of (1-0.7) pu. Following a 3-phase solid short circuit fault at the terminal of the generator, the magnitude of the subtransient internal emf (rounded off to 2 decimal places) is _______pu.

Solution:

The subtransient reactance is given by $X''_{d} = \frac{V}{I}$.

$$\begin{aligned}
E_{s,pu} &= E_{0,pu} + I X_{d,pu}\\
&= (1-0.7) + I(0.2)\\
&= 0.3 + 0.2I
\end{aligned}$$

The subtransient internal emf is given by:

$$E_{s,pu} = \frac{(V_{t,pu})^2}{X''_{d}}$$

Substituting the values, we get:

$$E_{s,pu} = \frac{(1+0)^2}{0.2} = 5 pu$$

Therefore, the magnitude of the subtransient internal emf is ___________pu.

#### Example 2: Sequence Voltages Analysis

A three-phase network has phase voltages $p V$ and $q V$. Express these in terms of sequence voltages $\begin{bmatrix} V_{0}\\ V_{1}\\ V_{2}\end{bmatrix}$.

Solution:

The sequence voltages can be represented as:

$$\begin{aligned}
V_0 &= \frac{1}{3}(V_a + V_b + V_c)\\
V_1 &= \frac{1}{3}(V_a + aV_b + a^2V_c)\\
V_2 &= \frac{1}{3}(V_a + a^2V_b + aV_c)
\end{aligned}$$

where $a = e^{j120^\circ}$.

### Common Pitfalls

*   **Misunderstanding of Per-Unit System**: The per-unit system is a powerful tool for normalizing quantities. However, it requires careful attention to ensure that the base values are correctly chosen.
*   **Incorrect Analysis of Short Circuit Faults**: Synchronous machines exhibit complex behavior during short circuit faults. It's essential to consider both subtransient and transient reactances.

### Quick Summary

*   **Synchronous Machines Operate at Constant Speed**.
*   **No Slip in Synchronous Machines**.
*   **High Power Rating in Synchronous Machines**.
*   **Per-Unit System Used for Normalizing Quantities**.
*   **Subtransient and Transient Reactances Important in Short Circuit Fault Analysis**.