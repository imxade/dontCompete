**Electrical Machine - Measurement**
=====================================

### Introduction
----------------

Measurement is a crucial aspect of electrical machines. Accurate measurement of electrical quantities such as voltage, current, power, and energy is essential for designing, testing, and maintaining electrical systems. In this note, we will focus on the measurement of electrical quantities using watt meters.

### Core Concepts
-----------------

*   **Watt Meter**: A device used to measure the power consumed by a circuit or load.
*   **Ideal Watt Meter**: An idealized model of a watt meter that assumes zero measurement error and does not affect the circuit being measured.
*   **Power Factor (PF)**: The ratio of real power (P) to apparent power (S), which indicates how effectively current is converted into useful work.

### Key Formulas/Theorems
---------------------------

$$\text{Apparent Power } S = VI \sin{\phi}$$

where $V$ is the voltage, $I$ is the current, and $\phi$ is the phase angle between voltage and current.

$$\text{Real Power } P = VI \cos{\phi}$$

$$\text{Power Factor (PF)} = \cos{\phi}$$

### Problem Solving Patterns
-----------------------------

*   **Understand the circuit**: Identify the type of load, source, and any other relevant components.
*   **Determine the measurement objective**: Clearly define what needs to be measured (e.g., power consumption).
*   **Select appropriate measurement tools**: Choose instruments capable of accurately measuring the required quantity.

### Examples with Solutions
---------------------------

**Example 1**

A three-phase 400 V source supplies a circuit with two loads, each represented by an impedance:

$$Z_1 = \sqrt{50^2 + (90 - j50)^2} = 100.03 \angle -30^\circ \Omega$$

$$Z_2 = \sqrt{200^2 + (30 - j200)^2} = 208.16 \angle -60^\circ \Omega$$

Using ideal watt meters $W_1$ and $W_2$, find the magnitude of the difference between their readings in watts.

**Solution**

1.  Calculate the power consumed by each load:

    $$P_1 = \frac{|V|^3}{|Z_1|} = \frac{400^3}{100.03} = 128,020 W$$

    $$P_2 = \frac{|V|^3}{|Z_2|} = \frac{400^3}{208.16} = 76,550 W$$
2.  The magnitude of the difference between the readings is:

    $$\Delta P = |P_1 - P_2| = |128,020 - 76,550| = 51,470 W$$

### Common Pitfalls
-------------------

*   Failing to consider the power factor and phase angle when calculating real power.
*   Not accounting for measurement errors in ideal watt meters.

### Quick Summary
-----------------

*   Understand circuit behavior (loads, sources, and other components).
*   Clearly define what needs to be measured (power consumption).
*   Select appropriate measurement tools (ideally watt meters or other instruments).
*   Calculate apparent power using $S = VI \sin{\phi}$.
*   Calculate real power using $P = VI \cos{\phi}$.

### References
---------------

For further study and reference, consider the following sources:

*   "Electric Circuits" by James W. Nilsson and Susan A. Riedel
*   "Electrical Machines and Drives" by John F. Lindsay and Stephen J. Chapman