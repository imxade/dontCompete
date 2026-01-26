**Thevenin's Theorem**
======================

### Introduction

Thevenin's theorem is a fundamental concept in network theory, allowing us to simplify complex circuits into simpler equivalent circuits. It helps us analyze and solve problems involving voltage sources, current sources, resistances, and impedances.

### Core Concepts

#### Definition

Given a linear circuit with multiple sources and impedances, Thevenin's theorem states that we can replace the entire circuit by a single voltage source ($V_{Th}$) in series with a resistance ($R_{Th}$). This equivalent circuit has the same behavior as the original complex circuit.

#### Conditions for Applicability

Thevenin's theorem applies to linear circuits only. Non-linear elements like diodes and transistors do not satisfy this condition.

#### Key Components

*   **Thevenin Voltage ($V_{Th}$)**: The open-circuit voltage at a specific node or terminal.
*   **Thevenin Resistance ($R_{Th}$)**: The resistance measured between two terminals with all sources shorted to ground.

### Key Formulas/Theorems

$$
\begin{aligned}
E_{Th} &= V_{oc}\\
R_{Th} &= \left|\frac{\Delta V}{\Delta I}\right|
\end{aligned}
$$

*   **$E_{Th}$**: Thevenin's equivalent voltage.
*   **$V_{oc}$**: Open-circuit voltage at a specific node or terminal.

### Problem Solving Patterns

1.  Identify the circuit element you want to simplify using Thevenin's theorem.
2.  Calculate the open-circuit voltage ($V_{oc}$) at that point.
3.  Short all voltage sources and calculate the resistance ($R_{Th}$) between the two terminals.

### Examples with Solutions

**Example:**

Suppose we have a circuit containing a $8\Omega$ resistor, a $2\mu F$ capacitor in parallel, and an ideal DC voltage source of $18V$. We want to find the equivalent Thevenin resistance ($R_{Th}$) at the output terminal.

*   **Step 1:** Find the open-circuit voltage ($V_{oc}$).
    $$ V_{oc} = \frac{18}{\left(2\times10^{-6}\right)\left(8\Omega\right)^{-1}} $$
    $$ V_{oc} = 18\cdot (0.5s) $$
*   **Step 2:** Short all voltage sources and calculate the resistance ($R_{Th}$).
    $$ R_{Th} = \frac{1}{\left(2\times10^{-6}\right)\left(8\Omega\right)^{-1}}$$
    $$ R_{Th} = (0.5s) $$
*   **Step 3:** Thevenin's equivalent resistance ($R_{Th}$) is equal to the value of the capacitor in series with the resistor.

**Thevenin's Theorem Solution:**
Since we are asked for the voltage across a certain point, let us use the following formula:

$$V = V_0 - R \times I$$

Substituting the given values, we get:
$V = 18-8\times 1.875$
Thevenin's theorem allows us to simplify complex circuits by replacing them with a single voltage source in series with a resistance. To apply this theorem, first find the open-circuit voltage and short all sources to calculate the Thevenin resistance.

### Common Pitfalls

*   Students often forget to check if the circuit is linear before applying Thevenin's theorem.
*   Incorrectly calculating the open-circuit voltage or Thevenin resistance can lead to wrong answers.
*   Misinterpreting the application of Thevenin's theorem in complex circuits can result in errors.

### Quick Summary

*   **Key concepts:** Open-circuit voltage, short circuit current
*   **Theorems and Formulas:**

$$
\begin{aligned}
E_{Th} &= V_{oc}\\
R_{Th} &= \left|\frac{\Delta V}{\Delta I}\right|
\end{aligned}
$$

*   Thevenin's theorem is a powerful tool for simplifying complex circuits into equivalent simpler circuits.

**Note:** This note covers all the necessary concepts, formulas, and problem-solving techniques to solve GATE CS exam questions related to Thevenin's theorem.