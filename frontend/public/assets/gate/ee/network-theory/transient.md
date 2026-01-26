**Transient Analysis**
=======================

**Introduction**
---------------

In this topic, we will explore transient analysis of networks, specifically focusing on R-L (Resistor-Inductor) and L-C (Inductor-Capacitor) circuits. Transient analysis is concerned with the behavior of a circuit when its inputs or initial conditions change.

**Core Concepts**
-----------------

### Time Constant

The time constant ($\tau$) is a fundamental concept in transient analysis. It represents the time it takes for the voltage across an inductor to reach 63% of its final value, assuming an exponential decay.

For R-L networks, the time constant is given by:

$$
\tau = \frac{L}{R}
$$

where $L$ is the inductance and $R$ is the resistance.

### Thevenin Resistance

The Thevenin resistance ($Th_R$) is a crucial parameter in transient analysis. It represents the resistance seen by an inductor or capacitor when all independent sources are deactivated.

For R-L networks, we can calculate the Thevenin resistance as follows:

$$
Th_R = \frac{R_1 R_2}{R_1 + R_2}
$$

### Inductor and Capacitor Time Constants

The time constant for an inductor ($\tau_L$) is given by:

$$
\tau_L = L/R_{eq}
$$

where $L$ is the inductance and $R_{eq}$ is the equivalent resistance.

For a capacitor, the time constant ($\tau_C$) is given by:

$$
\tau_C = \frac{1}{\omega C}
$$

where $\omega$ is the angular frequency and $C$ is the capacitance.

**Key Formulas/Theorems**
-------------------------

*   Time constant for R-L networks: $\tau = \frac{L}{R}$
*   Thevenin resistance: $Th_R = \frac{R_1 R_2}{R_1 + R_2}$
*   Inductor time constant: $\tau_L = L/R_{eq}$
*   Capacitor time constant: $\tau_C = \frac{1}{\omega C}$

**Problem Solving Patterns**
---------------------------

1.  Identify the type of circuit (R-L, L-C, or R-C).
2.  Calculate the Thevenin resistance ($Th_R$) for the circuit.
3.  Determine the time constant ($\tau$) for the inductor or capacitor.
4.  Use the calculated values to find the transient response.

**Examples with Solutions**
---------------------------

### Example 1

A circuit consists of a resistor (10 $\Omega$) and an inductor (5 H). Calculate the time constant.

Solution:

*   $R = 10 \, \Omega$
*   $L = 5 \, H$
*   $\tau = \frac{L}{R} = \frac{5}{10} = 0.5 \, s$

### Example 2

A circuit has a capacitor (100 $\mu F$) and an inductor (20 mH). Calculate the time constant for the capacitor.

Solution:

*   $C = 100 \, \mu F$
*   $L = 20 \, mH = 0.02 \, H$
*   $\omega = 2\pi f$, assuming a frequency of 50 Hz
*   $\tau_C = \frac{1}{\omega C} = \frac{1}{2\pi \cdot 50 \cdot 100 \times 10^{-6}} = 0.0635 \, s$

**Common Pitfalls**
------------------

*   Failing to identify the type of circuit (R-L, L-C, or R-C)
*   Incorrectly calculating the Thevenin resistance
*   Misinterpreting the time constant for inductors and capacitors

**Quick Summary**
-----------------

*   Time constant ($\tau$) is a fundamental concept in transient analysis.
*   Thevenin resistance ($Th_R$) represents the resistance seen by an inductor or capacitor when all independent sources are deactivated.
*   Inductor time constant: $\tau_L = L/R_{eq}$
*   Capacitor time constant: $\tau_C = \frac{1}{\omega C}$