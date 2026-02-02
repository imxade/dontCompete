**Control Theory**
================

### Introduction
-----------------

Control theory is a branch of mathematics that deals with the behavior of dynamical systems and the design of control systems to achieve desired objectives. It has numerous applications in various fields, including engineering, economics, and biology.

### Core Concepts
------------------

#### 1. Transfer Function
------------------------

The transfer function of a system is a mathematical representation of its input-output behavior. It describes how the system responds to different inputs and is used to analyze the stability and performance of the system.

Let $G(s)$ be the transfer function of a system, then:

$$G(s) = \frac{Y(s)}{U(s)}$$

where $Y(s)$ is the output and $U(s)$ is the input.

#### 2. Root Locus
-------------------

The root locus is a graphical representation of the poles of the closed-loop transfer function as a parameter (usually gain, $K$) varies. It is used to determine the stability of the system and the location of the poles.

Given a characteristic equation:

$$1 + G(s)H(s) = 0$$

The root locus can be plotted using the following rules:

*   The number of branches in the root locus is equal to the number of poles in the open-loop transfer function, $G(s)H(s)$.
*   The angles at which the branches leave and enter the real axis are $\frac{(2k+1)\pi}{|m-n|}$, where $m$ and $n$ are the numbers of poles and zeros to the left of the real axis.

### Key Formulas/Theorems
---------------------------

#### 1. Routh-Hurwitz Stability Criterion
-------------------------------------------------

The Routh-Hurwitz stability criterion is a method for determining the stability of a system based on its characteristic equation.

Given a characteristic equation:

$$a_n s^n + a_{n-1} s^{n-1} + \ldots + a_0 = 0$$

The Routh array can be formed as follows:

| $s^0$ | $a_0$ |
| --- | --- |
| $s^1$ | $a_1$ |
| $s^2$ | $\frac{a_1}{a_0}$ |

... (continued in the next block)

### Key Formulas/Theorems (Continued)
---------------------------------------

#### 2. Routh-Hurwitz Stability Criterion (Continued)
---------------------------------------------------

The Routh array is used to determine the number of sign changes in each column, which indicates the stability of the system.

*   If there are no sign changes, the system is stable.
*   If there is one sign change, the system is marginally stable.
*   If there are two or more sign changes, the system is unstable.

### Problem Solving Patterns
---------------------------

#### 1. Analyzing Stability Using Root Locus
--------------------------------------------

To analyze the stability of a system using root locus:

1.  Plot the open-loop poles and zeros on the complex plane.
2.  Draw the root locus branches, following the rules mentioned earlier.
3.  Determine the number of sign changes in each column of the Routh array.

### Examples with Solutions
---------------------------

#### Example 1: Analyzing Stability Using Root Locus

Given a system with a characteristic equation:

$$s^2 + 2s + K = 0$$

Plot the root locus as $K$ varies from 0 to $\infty$. Determine the break-away or break-in point(s).

Solution:

The open-loop poles are at $s=0$ and $s=-\infty$.

As $K$ varies from 0 to $\infty$, the root locus branches move towards the real axis, with one branch leaving the imaginary axis at a finite value of $K$. The break-away or break-in point lies within the region where the root locus crosses the imaginary axis.

### Common Pitfalls
-------------------

*   Students often miss that the number of sign changes in each column of the Routh array determines the stability of the system.
*   Failure to plot the open-loop poles and zeros on the complex plane can lead to incorrect analysis of the root locus.

### Quick Summary
-----------------

*   Transfer function: $G(s) = \frac{Y(s)}{U(s)}$
*   Root locus:
    *   Number of branches: equal to the number of poles in the open-loop transfer function.
    *   Angles at which branches leave and enter the real axis: $\frac{(2k+1)\pi}{|m-n|}$.
*   Routh-Hurwitz stability criterion:
    *   No sign changes: stable.
    *   One sign change: marginally stable.
    *   Two or more sign changes: unstable.