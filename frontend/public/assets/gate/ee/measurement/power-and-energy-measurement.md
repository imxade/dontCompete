**Power and Energy Measurement**
=====================================

### Introduction
-----------------

Measurement of power and energy is crucial in electrical engineering to evaluate the efficiency and performance of systems. In this note, we will cover the theoretical concepts, formulas, and insights required to solve problems related to power and energy measurement.

### Core Concepts
------------------

*   **Power**: The rate at which electrical energy is transferred by an electric circuit.
    $P = VI \cos(\theta)$

    Where:
    *   $V$ is the voltage (rms) of the circuit
    *   $I$ is the current (rms) flowing through the circuit
    *   $\theta$ is the power factor angle
*   **Energy**: The total amount of electrical work done by a system.
    $E = Pt$

### Key Formulas/Theorems
---------------------------

*   **Power Triangle**:
    $\cos(\theta) = \frac{P}{VI}$

    Where:
    *   $P$ is the power (watts)
    *   $V$ is the voltage (rms) of the circuit
    *   $I$ is the current (rms) flowing through the circuit
*   **Power Factor**: The ratio of real power to apparent power.
    $\cos(\theta)$

### Problem Solving Patterns
---------------------------

*   **Wattmeter Reading**: When a wattmeter reading is given, use it to determine the power factor of the load.
    Example: If the wattmeter reading is $-400$ W and the line current is $2$ A (rms), find the power factor of the load per phase.

### Examples with Solutions
---------------------------

**Example 1**: 
A 3-phase, star-connected, balanced load is supplied from a 3-phase, 400 V (rms), balanced voltage source. If the wattmeter reading is $-400$ W and the line current is $2$ A (rms), find the power factor of the load per phase.

**Solution:**

Given:
*   $\theta = \cos^{-1}\left(\frac{P}{VI}\right)$
*   $V = 400$ V (rms)
*   $I = 2$ A (rms)

First, determine the apparent power using the formula:
$S = VI$

Next, find the real power using the wattmeter reading:
$P_{\text{wattmeter}} = -400$ W

Since it's a balanced system, the power factor is the same for all phases.

Now, substitute the values into the power triangle equation:

$\cos(\theta) = \frac{P}{VI}$

Rearrange to solve for $\theta$:
$\cos^{-1}\left(\frac{P}{VI}\right)$

Substitute the known values:
$\theta = \cos^{-1}\left(\frac{-400}{400 \cdot 2}\right)$
$\theta = \cos^{-1}(-0.5)$

Therefore, $\cos(\theta) = -0.866$ (leading), since the power factor is negative.

The answer is: **(C)** 0.866 leading

### Common Pitfalls
-------------------

*   Confusing apparent and real power.
*   Failing to account for phase sequence.
*   Ignoring the impact of power factor on system performance.

### Quick Summary
------------------

| Key Concept | Definition |
| --- | --- |
| Power | The rate at which electrical energy is transferred. |
| Energy | The total amount of electrical work done by a system. |
| Power Factor | The ratio of real power to apparent power. |

**Note:** This summary should be reviewed before attempting the practice questions.

### References
---------------

None.

Please let me know if you need any adjustments or if this meets your requirements!