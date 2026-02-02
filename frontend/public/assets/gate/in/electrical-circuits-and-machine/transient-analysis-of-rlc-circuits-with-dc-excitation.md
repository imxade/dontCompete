**Transient Analysis of RLC Circuits with DC Excitation**
==========================================================

### Introduction
-----------------

Transient analysis involves studying the behavior of electrical circuits when subjected to changes in their inputs, such as sudden application or removal of a voltage source. In this topic, we focus on RLC (Resistor-Inductor-Capacitor) circuits excited by a constant DC voltage.

### Core Concepts
----------------

#### Inductor and Capacitor Response

*   **Inductor:** When a voltage is applied to an inductor, current increases exponentially due to the induced back electromotive force (EMF). The time constant for this process is given by $\tau = \frac{L}{R}$, where $L$ is the inductance and $R$ is the resistance.
*   **Capacitor:** When a voltage is applied across a capacitor, charge builds up exponentially. The time constant for this process is $\tau = RC$, where $C$ is the capacitance.

#### RLC Circuit Analysis

A series RLC circuit consists of a resistor ($R$), an inductor ($L$), and a capacitor ($C$) connected in series with a voltage source ($V_{in}$). The impedance of such a circuit can be found using:

$$Z = \sqrt{R^2 + (X_L - X_C)^2}$$

where $X_L = \omega L$ is the inductive reactance and $X_C = \frac{1}{\omega C}$ is the capacitive reactance.

#### Transient Analysis

To analyze transient behavior, we consider two cases:

*   **Ramp Input:** When a voltage ramps up from 0 to its maximum value over time $t$, the current and capacitor charge also ramp up.
*   **Step Input:** When a voltage is suddenly applied at $t=0$, the current and capacitor charge change exponentially.

For both cases, we can use Kirchhoff's laws to find expressions for the circuit variables (current, voltage across components) as functions of time.

### Key Formulas/Theorems
-------------------------

$$\tau = \frac{L}{R}$$

$$\tau = RC$$

$$Z = \sqrt{R^2 + (X_L - X_C)^2}$$

### Problem Solving Patterns
-----------------------------

*   **Identify Circuit Type:** Determine if the circuit is RLC, RLCG, or another type.
*   **Apply Kirchhoff's Laws:** Use the laws to relate circuit variables over a branch or loop.
*   **Find Time Constants:** Calculate $\tau$ for inductors and capacitors.
*   **Calculate Impedance:** Compute $Z$ for series RLC circuits.

### Examples with Solutions
---------------------------

#### Example 1: Ramp Input

Consider an RLC circuit where $L = 10 mH$, $R = 100 \Omega$, and $C = 47 \mu F$. If a voltage of 12 V ramps up from 0 to its maximum value over 2 seconds, find the current at time $t=1$ second.

Solution:
*   Find $\tau$ for inductor: $\tau_L = \frac{L}{R} = \frac{10 mH}{100 \Omega} = 0.01 s$
*   Find $\tau$ for capacitor: $\tau_C = RC = (47 \mu F)(100 \Omega) = 4.7 s$
*   Since the voltage ramps up, use $V(t) = V_{in}(t/t_{max})$. At $t=1$, $V(1) = 12 \cdot (1/2) = 6$ V
*   The current is given by $I(t) = I_0 e^{-\frac{t}{\tau_L}}$, where $I_0$ can be found from initial conditions.

#### Example 2: Step Input

For the same circuit as above, if a voltage of 12 V is suddenly applied at time $t=0$, find the current at $t=1$ second.

Solution:
*   Use the formula for exponential decay to find current at $t=1$: $I(1) = I_0 e^{-\frac{1}{\tau_L}}$

### Common Pitfalls
--------------------

*   **Incorrect Time Constants:** Be sure to calculate $\tau$ correctly.
*   **Incorrect Impedance Calculation:** Double-check your impedance calculations using the formula.

### Quick Summary
-------------------

Transient analysis of RLC circuits involves understanding inductor and capacitor behavior, analyzing series RLC circuits, and applying problem-solving techniques.