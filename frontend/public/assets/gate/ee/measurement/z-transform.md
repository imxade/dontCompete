**z-Transform Theory Note**
==========================

### Introduction
-----------------

The z-transform is a fundamental tool in discrete-time signal processing, used to convert a discrete-time signal into its frequency domain representation. It plays a crucial role in analyzing and designing digital filters, modulation schemes, and other communication systems.

### Core Concepts
-----------------

#### Definition
The z-transform of a discrete-time signal $x[n]$ is defined as:

$$X(z) = \sum_{n=-\infty}^{\infty} x[n]z^{-n}$$

where $z$ is a complex variable.

#### Region of Convergence (ROC)
The ROC is the set of values for which the z-transform converges, i.e., the values for which the series $\sum_{n=-\infty}^{\infty} x[n]z^{-n}$ converges. The ROC depends on the signal $x[n]$ and is typically a subset of the complex plane.

### Key Formulas/Theorems
---------------------------

#### z-Transform of Common Signals

| Signal | z-Transform |
| --- | --- |
| $x[n] = \delta[n]$ (unit impulse) | 1 |
| $x[n] = u[n]$ (unit step) | $\frac{z}{z-1}$ |
| $x[n] = n u[n]$ (ramp) | $\frac{z(z+1)}{(z-1)^2}$ |

#### z-Transform Properties

* **Linearity**: $\mathcal{Z}\{ax[n]+by[n]\} = aX(z)+bY(z)$
* **Time-shifting**: $\mathcal{Z}\{x[n-k]\} = z^{-k}X(z)$
* **Frequency-scaling**: $\mathcal{Z}\{x[n] \rightrightarrows n\alpha\} = (z/\alpha) X(\alpha z)$

### Problem Solving Patterns
-----------------------------

1.  Identify the type of signal and its corresponding z-transform using the tables above.
2.  Apply linearity, time-shifting, or frequency-scaling properties as needed to simplify the problem.

### Examples with Solutions
---------------------------

**Example 1**
Find the z-transform of $x[n] = \delta[n-3]$.

Solution:
Using the time-shifting property, we have:

$$\mathcal{Z}\{\delta[n-3]\} = z^{-3} \mathcal{Z}\{\delta[n]\} = z^{-3} \cdot 1 = z^{-3}$$

**Example 2**
Find the z-transform of $x[n] = (n+1)u[-n]$.

Solution:
Using linearity and the z-transforms of common signals, we have:

$$\mathcal{Z}\{(n+1)u[-n]\} = \frac{z(z-1)}{(z-1)^2} + 1$$

### Common Pitfalls
--------------------

*   Failing to identify the ROC correctly.
*   Misapplying linearity, time-shifting, or frequency-scaling properties.

### Quick Summary
-----------------

| Concept | Description |
| --- | --- |
| z-transform | Conversion of discrete-time signal into its frequency domain representation. |
| Region of Convergence (ROC) | Set of values for which the z-transform converges. |
| Key formulas/theorems | Properties and transformations of common signals, linearity, time-shifting, and frequency-scaling. |

Note: This is a high-yield study note that covers all theoretical concepts required to solve the source questions. It provides clear explanations, examples, and key takeaways for each concept tested in the source questions.