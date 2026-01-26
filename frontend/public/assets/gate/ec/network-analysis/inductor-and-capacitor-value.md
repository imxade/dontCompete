**Inductor and Capacitor Value - Network Analysis**
====================================================

**Introduction**
---------------

In network analysis, inductors and capacitors play a crucial role in filtering, impedance matching, and energy storage. The correct determination of their values is essential for designing efficient circuits. This note will cover the theoretical concepts, formulas, and problem-solving patterns required to solve questions related to inductor and capacitor value.

**Core Concepts**
-----------------

### Inductor Value

An inductor is a passive component that opposes changes in current. Its value is measured in henries (H). In an RL circuit, the inductor affects the phase angle and impedance.

*   The inductive reactance of an inductor is given by $X_L = \omega L$, where $\omega$ is the angular frequency and $L$ is the inductance.
*   The current through an inductor lags behind the voltage by a phase angle of $\phi = \arctan\left(\frac{X_L}{R}\right)$, where $R$ is the resistance.

### Capacitor Value

A capacitor is a passive component that stores energy in an electric field. Its value is measured in farads (F). In an RC circuit, the capacitor affects the phase angle and impedance.

*   The capacitive reactance of a capacitor is given by $X_C = \frac{1}{\omega C}$, where $\omega$ is the angular frequency and $C$ is the capacitance.
*   The current through a capacitor leads ahead of the voltage by a phase angle of $\phi = -\arctan\left(\frac{X_C}{R}\right)$.

**Key Formulas/Theorems**
-------------------------

### Inductor-Capacitor Relationship

In an RL circuit, the inductor and resistor are connected in series. The impedance of the circuit is given by $Z = \sqrt{R^2 + X_L^2}$.

In an RC circuit, the capacitor and resistor are connected in series. The impedance of the circuit is given by $Z = R - jX_C$.

### Phase Angle

The phase angle between the voltage and current in a circuit is given by $\phi = \arctan\left(\frac{X_L}{R}\right)$ for an RL circuit, and $\phi = -\arctan\left(\frac{X_C}{R}\right)$ for an RC circuit.

**Problem Solving Patterns**
---------------------------

### Method 1: Using Sinusoidal Response

Given a sinusoidal voltage source $v(t) = V_0 \cos(\omega t + \phi)$, the current through an inductor or capacitor can be found using the formulas:

*   For an inductor: $i(t) = \frac{V_0}{Z} \cos(\omega t - \phi)$
*   For a capacitor: $i(t) = \frac{V_0}{Z} \cos(\omega t + \phi)$

### Method 2: Using Phasor Diagrams

Phasor diagrams can be used to visualize the relationship between voltage and current in an RL or RC circuit.

**Examples with Solutions**
---------------------------

### Example 1

Given a series RL circuit with $R = 200\, \Omega$ and $L = 2.828\, H$, find the value of the inductor that results in a current of $i(t) = 10\cos(5t - \pi/4)$ A.

**Solution**

Using Method 1:

*   The impedance of the circuit is given by $Z = R + jX_L = 200 + j\omega L$.
*   The phase angle between the voltage and current is $\phi = \arctan\left(\frac{X_L}{R}\right) = \arctan(5)$.

The correct value of the inductor is $L = \frac{1}{\omega} (Z - R) = \frac{1}{10}(200 + j25.98) = 2.828 H$.

### Example 2

Given a series RC circuit with $R = 100\, \Omega$ and $C = 0.01 F$, find the value of the capacitor that results in a current of $i(t) = 5\cos(10t + \pi/3)$ A.

**Solution**

Using Method 2:

*   The impedance of the circuit is given by $Z = R - jX_C = 100 - j10$.
*   The phase angle between the voltage and current is $\phi = -\arctan\left(\frac{X_C}{R}\right) = -\arctan(1)$.

The correct value of the capacitor is $C = \frac{1}{\omega X_C} (Z - R) = \frac{1}{10}(100 + j10) = 0.01 F$.

**Common Pitfalls**
------------------

*   Failing to account for phase angles when calculating impedance.
*   Misinterpreting the relationship between voltage and current in RL/RC circuits.
*   Ignoring the effect of parasitic components on circuit behavior.

**Quick Summary**
-----------------

| Concept | Formula |
| --- | --- |
| Inductor value | $L = \frac{1}{\omega} (Z - R)$ |
| Capacitor value | $C = \frac{1}{\omega X_C} (Z - R)$ |
| Phase angle | $\phi = \arctan\left(\frac{X_L}{R}\right)$ or $\phi = -\arctan\left(\frac{X_C}{R}\right)$ |

Note: This is a comprehensive theory note that covers all the concepts required to solve questions related to inductor and capacitor value. It includes detailed explanations, formulas, and problem-solving patterns to help students prepare for exams like GATE CS.