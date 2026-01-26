**Equations of State**
=====================

### Introduction
-----------------

In thermodynamics and process calculations, equations of state (EOS) describe the relationship between pressure, volume, and temperature of a system. A widely used EOS is the truncated virial equation, which we'll explore in this note.

### Core Concepts
------------------

#### Truncated Virial Equation
The truncated virial equation is given by:

$$\frac{PV}{RT} = 1 + \frac{B}{V}$$

where:
- $P$ is pressure,
- $V$ is molar volume,
- $T$ is absolute temperature, and
- $B$ is the second virial coefficient.

#### Universal Gas Constant
The universal gas constant $R$ is a fundamental physical constant that relates the energy of an ideal gas to its properties. In this note, we'll use the value:

$$R = 83.14 \text{ bar} \cdot \text{m}^3 \text{ mol}^{-1} \text{ K}^{-1}$$

### Key Formulas/Theorems
-------------------------

To solve problems involving EOS, we'll need to differentiate the equation with respect to $P$ and $T$. Let's derive the relevant formulas:

* **Compressibility Factor**: The compressibility factor is defined as:

$$Z = \frac{PV}{RT}$$

Differentiating $Z$ with respect to $P$, we get:

$$\left(\frac{\partial Z}{\partial P}\right)_T = \frac{V - RT\left(\frac{\partial B}{\partial V}\right)_T}{RTP}$$

* **Molar Residual Gibbs Free Energy**: The molar residual Gibbs free energy is related to the compressibility factor by:

$$G_R = RT \ln Z + RT\left(\frac{\partial Z}{\partial P}\right)_T$$

### Problem Solving Patterns
---------------------------

When faced with a problem involving EOS, follow these steps:

1. Identify the given equation of state and any relevant constants.
2. Differentiate the equation with respect to $P$ or $T$, as required by the question.
3. Substitute values for the parameters and calculate the desired quantity.

### Examples with Solutions
---------------------------

**Example 1:**
Given the truncated virial equation, find the value of $\left(\frac{\partial P}{\partial V}\right)_T$ at $340 \text{ K}$.

**Solution:**

$$\left(\frac{\partial P}{\partial V}\right)_T = -\frac{RTP}{V^2} + \frac{RTB_T}{V^2}$$

Substituting the given values, we get:

$$\left(\frac{\partial P}{\partial V}\right)_T = -\frac{(83.14 \text{ bar} \cdot \text{m}^3 \text{ mol}^{-1} \text{ K}^{-1})(340 \text{ K})}{V^2} + \frac{(83.14 \text{ bar} \cdot \text{m}^3 \text{ mol}^{-1} \text{ K}^{-1})(340 \text{ K})B_T}{V^2}$$

**Example 2:**
Given the truncated virial equation and the value of $B$, find the molar residual Gibbs free energy at $340 \text{ K}$.

**Solution:**

Using the formula for $G_R$ derived earlier, we substitute the values:

$$G_R = RT \ln Z + RT\left(\frac{\partial Z}{\partial P}\right)_T = (83.14 \text{ bar} \cdot \text{m}^3 \text{ mol}^{-1} \text{ K}^{-1})(340 \text{ K})\ln\left(1 + \frac{B}{V}\right)$$

### Common Pitfalls
-------------------

* Failing to identify the correct equation of state or constants used in the problem.
* Not differentiating the equation with respect to the required variable ($P$ or $T$).
* Forgetting to substitute values for the parameters.

### Quick Summary
------------------

* Truncated virial equation: $\frac{PV}{RT} = 1 + \frac{B}{V}$.
* Universal gas constant: $R = 83.14 \text{ bar} \cdot \text{m}^3 \text{ mol}^{-1} \text{ K}^{-1}$.
* Compressibility factor: $Z = \frac{PV}{RT}$.
* Molar residual Gibbs free energy: $G_R = RT \ln Z + RT\left(\frac{\partial Z}{\partial P}\right)_T$.

This comprehensive theory note covers all the concepts, formulas, and insights required to solve problems involving equations of state.