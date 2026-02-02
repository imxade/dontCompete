**Filter Design**
================

**Introduction**
---------------

In this note, we'll delve into the world of filter design, specifically focusing on electrical circuits. Filters are essential components in various electronic systems, allowing us to selectively pass or block specific frequency ranges. Understanding the underlying principles and mathematical formulations will enable you to tackle complex problems with confidence.

**Core Concepts**
-----------------

### 1. Q-Factor

The Q-factor (quality factor) is a measure of an inductor's or capacitor's ability to store energy. It's defined as:

$$Q = \frac{\omega L}{R} \text{ for inductors}$$

$$Q = \frac{1}{\omega CR} \text{ for capacitors}$$

where $\omega$ is the angular frequency, $L$ is the inductance, $C$ is the capacitance, and $R$ is the resistance.

### 2. Filter Types

There are two primary types of filters:

* **Low-pass filters** (LPF): allow low-frequency signals to pass through while attenuating high-frequency signals.
* **High-pass filters** (HPF): allow high-frequency signals to pass through while attenuating low-frequency signals.

### 3. Resonant Frequency

The resonant frequency is the frequency at which a circuit's Q-factor is maximum:

$$f_r = \frac{1}{2\pi\sqrt{LC}}$$

### 4. Cascaded Filters

In some cases, filters are connected in series or parallel to achieve desired characteristics.

**Key Formulas/Theorems**
-------------------------

* **Q-factor for a series RLC circuit**: $Q = \frac{\omega L}{R}$
* **Q-factor for a shunt RLC circuit**: $Q = \frac{1}{\omega CR}$
* **Resonant frequency**: $f_r = \frac{1}{2\pi\sqrt{LC}}$

**Problem Solving Patterns**
---------------------------

### 1. Q-Factor Calculation

To calculate the overall Q-factor of a circuit with multiple components, use the following approach:

* Calculate the individual Q-factors for each component.
* Use the correct formula to combine the Q-factors (e.g., series or parallel).

### 2. Resonant Frequency Calculation

Given an inductor and capacitor value, calculate the resonant frequency using the formula $f_r = \frac{1}{2\pi\sqrt{LC}}$.

**Examples with Solutions**
---------------------------

### Example 1: Q-Factor Calculation

An inductor has a Q-factor of 60. A capacitor is connected in series with an inductance value of 100 mH and a resistance value of 10 ohms. What is the overall Q-factor?

* Step 1: Calculate the individual Q-factors.
	+ Inductor: $Q = \frac{\omega L}{R}$
	+ Capacitor: $Q = \frac{1}{\omega CR}$
* Step 2: Combine the Q-factors using the correct formula for a series RLC circuit.

```python
import math

# Given values
L = 100e-3  # Inductance in H
R = 10      # Resistance in ohms
C = 5e-6    # Capacitance in F
Q_inductor = 60

# Calculate Q-factor for capacitor
omega = 1 / math.sqrt(L * C)
Q_capacitor = 1 / (omega * C * R)

# Calculate overall Q-factor
overall_Q = (Q_inductor * Q_capacitor) / (1 + (Q_inductor * Q_capacitor))

print("Overall Q-factor:", round(overall_Q))
```

### Example 2: Resonant Frequency Calculation

Given an inductor value of 100 mH and a capacitor value of 10 nF, what is the resonant frequency?

* Step 1: Calculate the resonant frequency using the formula $f_r = \frac{1}{2\pi\sqrt{LC}}$.

```python
import math

# Given values
L = 100e-3  # Inductance in H
C = 10e-9   # Capacitance in F

# Calculate resonant frequency
fr = 1 / (2 * math.pi * math.sqrt(L * C))

print("Resonant frequency:", round(fr, 2))
```

**Common Pitfalls**
-------------------

* Failing to consider the correct formula for combining Q-factors.
* Neglecting to account for the inductor's and capacitor's individual Q-factors.

**Quick Summary**
----------------

* Understand the concept of Q-factor and its application in filter design.
* Familiarize yourself with the different types of filters (LPF, HPF).
* Learn to calculate resonant frequency using the formula $f_r = \frac{1}{2\pi\sqrt{LC}}$.

This comprehensive theory note should provide a solid foundation for tackling filter design problems. By understanding the underlying principles and mathematical formulations, you'll be better equipped to solve complex questions like those found in previous year exams.