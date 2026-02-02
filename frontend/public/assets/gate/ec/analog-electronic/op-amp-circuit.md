**Op-Amp Circuit Theory Notes**
=====================================

### Introduction
---------------

An operational amplifier (op-amp) is a fundamental component in analog electronics, widely used for signal amplification and processing. This note provides an overview of op-amp circuits, focusing on theoretical concepts, formulas, and problem-solving patterns relevant to the GATE CS exam.

### Core Concepts
-----------------

#### Ideal Op-Amp Assumptions

* Infinite input impedance
* Zero output impedance
* Infinite gain (when ideal)

#### Op-Amp Equations

$$V_o = A(V_+ - V_-)$$

where $A$ is the open-loop gain, and $V_+$ and $V_-$ are the inverting and non-inverting input voltages.

### Key Formulas/Theorems
-------------------------

#### Differential Amplifier

For a differential amplifier with resistors $R_1$, $R_2$, $R_{f1}$, and $R_{f2}$:

$$\frac{V_o}{V_i} = \frac{\left(\frac{R_f1 + R_f2}{R_1 + R_2}\right) - 1}{1 - \frac{R_f1}{R_1} - \frac{R_f2}{R_2}}$$

#### Integrator and Differentiator Circuits

* Integrator: $$V_o = -\int V_i dt$$
* Differentiator: $$V_o = \frac{dV_i}{dt}$$

### Problem Solving Patterns
---------------------------

1. **Identify the op-amp configuration**: inverting, non-inverting, or differential.
2. **Determine the input and output voltages**.
3. **Apply the relevant op-amp equation**.

### Examples with Solutions
-----------------------------

#### Example 1: Differential Amplifier

| Input Voltage | Output Voltage |
| --- | --- |
| $V_+ = 10\, \text{mV}$, $V_- = -5\, \text{mV}$ | $\frac{10-(-5)}{100}\times 10^3 = 150\, \text{mV}$ |

#### Solution:

Apply the differential amplifier equation with $R_1=R_2=50\, \Omega$, $R_{f1}=500\, \Omega$, and $R_{f2}=200\, \Omega$.

```latex
\frac{V_o}{V_i} = \frac{\left(\frac{500+200}{50+50}\right) - 1}{1 - \frac{500}{50} - \frac{200}{50}} 
= \frac{(700-100)}{(2\times 50)\times (5-10)} 
= \frac{600}{(-40)}
= -15
```

### Common Pitfalls
-------------------

* Forgetting to consider the op-amp's ideal assumptions.
* Misapplying formulas or equations for non-ideal cases.
* Failing to identify the correct op-amp configuration.

### Quick Summary
------------------

* Op-amps are fundamental in analog electronics, used for signal amplification and processing.
* Ideal op-amp assumptions include infinite input impedance and zero output impedance.
* Key formulas and theorems include differential amplifier equations and integrator/differentiator circuits.
* Problem-solving patterns involve identifying the op-amp configuration, determining input and output voltages, and applying relevant equations.

**Note:** This content is intended to be a starting point for your studies. Make sure to practice with sample problems and past year questions to reinforce your understanding.