**Transfer Function**
=====================

### Introduction
---------------

The transfer function of a system is a mathematical representation of the system's behavior, describing how it responds to inputs. It's a crucial concept in control systems, used to analyze and design systems that can achieve desired performance.

### Core Concepts
-----------------

A transfer function is a ratio of the output signal (Y(s)) to the input signal (R(s)), expressed in terms of complex frequency s:

$$G(s) = \frac{Y(s)}{R(s)}$$

Given a system with transfer function G(s), we can analyze its behavior by applying various inputs, such as step functions or sine waves.

### Key Formulas/Theorems
-------------------------

1. **Final Value Theorem**: For a stable system, the final value of the output (y(t)) is equal to the limit of the output at s=0:

$$\lim_{t \to \infty} y(t) = \lim_{s \to 0} G(s)R(s)$$

2. **Transfer Function for a System with a Step Input**: For a unit step function input (r(t)=μ), we have:

$$R(s) = \frac{1}{s}$$

Substituting this into the transfer function equation gives us:

$$Y(s) = G(s)\frac{1}{s}$$

### Problem Solving Patterns
-----------------------------

When solving problems involving transfer functions, follow these steps:

1. **Identify the Transfer Function**: Determine the system's transfer function (G(s)) from the given problem.
2. **Apply Input Signal**: Apply the input signal (R(s)) to the system and calculate the output (Y(s)).
3. **Use Key Formulas/Theorems**: Utilize key formulas, such as the final value theorem, to analyze the system's behavior.

### Examples with Solutions
---------------------------

**Example 1:**

Consider a system with transfer function:

$$G(s) = \frac{2}{s+1}$$

A unit step function is applied to the system. What is the final value of the output?

* Identify the transfer function: $G(s) = \frac{2}{s+1}$
* Apply input signal: $R(s) = \frac{1}{s}$
* Use key formulas/theorems: Final Value Theorem

$$\lim_{t \to \infty} y(t) = \lim_{s \to 0} G(s)R(s)$$

Substituting the transfer function and input signal, we get:

$$\lim_{t \to \infty} y(t) = \lim_{s \to 0} \frac{2}{s+1} \cdot \frac{1}{s}$$

Evaluating this limit gives us:

$$\lim_{t \to \infty} y(t) = \boxed{1}$$

### Common Pitfalls
-------------------

* **Incorrectly applying the final value theorem**: Make sure to check if the system is stable (i.e., has no poles in the right half of the s-plane) before applying the final value theorem.
* **Ignoring transfer function properties**: Be aware of the properties of transfer functions, such as linearity and time-invariance.

### Quick Summary
-----------------

* Transfer function: $G(s) = \frac{Y(s)}{R(s)}$
* Final Value Theorem: $\lim_{t \to \infty} y(t) = \lim_{s \to 0} G(s)R(s)$

Note: This theory note is designed to provide a comprehensive understanding of the transfer function concept, focusing on exam requirements. Practice problems and examples are essential for mastery.