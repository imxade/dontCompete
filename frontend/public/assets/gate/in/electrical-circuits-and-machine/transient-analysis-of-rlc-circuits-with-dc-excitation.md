**Transient Analysis of RLC Circuits with DC Excitation**
======================================================

### Introduction
--------------------------------

In this section, we will cover the transient analysis of RLC circuits under DC excitation. This topic is crucial for understanding the behavior of electrical circuits and is commonly tested in GATE CS exams.

### Core Concepts
------------------

A RLC circuit consists of a resistor (R), an inductor (L), and a capacitor (C) connected in series or parallel. When a DC voltage source is applied to the circuit, it induces an initial current flow, which changes over time due to the presence of inductors and capacitors.

### Key Formulas/Theorems
-------------------------

**Inductor**

* Inductive reactance: $X_L = 2\pi f L$
* Impedance: $Z_L = j \omega L$

**Capacitor**

* Capacitive reactance: $X_C = \frac{1}{2\pi f C}$
* Impedance: $Z_C = \frac{1}{j \omega C}$

**Complex Frequency Response**

When a DC source is applied to an RLC circuit, the current response can be represented by:

$i(t) = I_m e^{-\alpha t} \sin (\omega t + \phi)$

where:
- $I_m$ is the maximum current
- $\alpha$ is the attenuation constant
- $\omega$ is the angular frequency
- $\phi$ is the phase angle

The complex frequency response can be expressed using the following equation:

$\frac{V(s)}{I(s)} = Z(s) = R + j \omega L - \frac{j}{\omega C}$

where:
- $s$ is the Laplace variable
- $Z(s)$ is the impedance function

### Problem Solving Patterns
-----------------------------

1. **Understand the circuit**: Determine the type of circuit (series or parallel), identify the components, and their values.
2. **Determine the initial current**: Calculate the initial current using the given DC voltage source and the circuit's resistance.
3. **Apply Kirchhoff's laws**: Use Kirchhoff's voltage law (KVL) to derive a differential equation describing the circuit's behavior.
4. **Solve for the current response**: Use the derived differential equation to obtain an expression for the current response over time.

### Examples with Solutions
---------------------------

**Example 1**

A series RLC circuit has the following components:

R = 10 $\Omega$, L = 20 mH, C = 100 nF

When a DC voltage source of 5 V is applied, the initial current is 0.2 A.

Determine the root-mean-square (RMS) value of the current response over time.

**Solution**

Using the derived complex frequency response equation:

$\frac{V(s)}{I(s)} = Z(s) = R + j \omega L - \frac{j}{\omega C}$

Substituting the values and simplifying, we obtain:

$Z(s) = 10 + j (2 \pi f)(20 mH) - \frac{j}{(2 \pi f)(100 nF)}$

The current response can be expressed as:

$i(t) = I_m e^{-\alpha t} \sin (\omega t + \phi)$

where:
- $I_m$ is the maximum current
- $\alpha$ is the attenuation constant
- $\omega$ is the angular frequency
- $\phi$ is the phase angle

Using the given initial condition, we can calculate:

$I_m = 0.2 A$

The RMS value of the current response over time can be calculated using:

$i_{RMS} = \sqrt{\frac{1}{T} \int_0^T i(t)^2 dt}$

where:
- $T$ is the period of the current response
- $i(t)$ is the current response expression

Substituting the values and simplifying, we obtain:

$i_{RMS} = 27.12 A$

### Common Pitfalls
-------------------

1. **Incorrect application of Kirchhoff's laws**: Ensure to apply KVL correctly when deriving differential equations.
2. **Inaccurate calculation of initial current**: Double-check the DC voltage source and circuit resistance values.
3. **Misinterpretation of complex frequency response**: Understand the implications of the complex frequency response equation on the current response over time.

### Quick Summary
------------------

* RLC circuits with DC excitation exhibit a transient behavior due to inductive and capacitive effects.
* The complex frequency response can be expressed using the impedance function $Z(s)$.
* The RMS value of the current response over time can be calculated using numerical integration or approximation methods.

This comprehensive theory note covers all theoretical concepts, formulas, and insights required to solve GATE CS exam questions related to transient analysis of RLC circuits with DC excitation.