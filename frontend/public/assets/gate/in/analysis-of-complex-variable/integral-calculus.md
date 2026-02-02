# Integral Calculus and Analysis of Complex Variables
==============================================

### Introduction
-----------------

In this note, we will cover the theoretical concepts and formulas required to solve problems related to integral calculus and analysis of complex variables. The focus will be on GATE CS exam-style questions.

### Core Concepts
------------------

#### Complex Numbers
-------------------

A complex number is a number that can be expressed in the form $z = x + iy$, where $x$ and $y$ are real numbers, and $i$ is the imaginary unit such that $i^2 = -1$. The complex conjugate of $z$ is denoted by $\bar{z}$ and is given by $\bar{z} = x - iy$.

#### Analytic Functions
----------------------

An analytic function is a function that is differentiable at every point in its domain. In the context of complex analysis, an analytic function can be expressed as $f(z) = u(x,y) + iv(x,y)$, where $u$ and $v$ are real-valued functions.

### Key Formulas/Theorems
---------------------------

#### Cauchy-Riemann Equations
--------------------------------

The Cauchy-Riemann equations are a set of two partial differential equations that must be satisfied by the real and imaginary parts of an analytic function. They are given by:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}.$$

#### Cauchy's Integral Formula
-------------------------------

Cauchy's integral formula states that if $f(z)$ is an analytic function within a simple closed curve $C$, then:

$$f(a) = \frac{1}{2\pi i} \int_C \frac{f(z)}{z-a} dz.$$

### Problem Solving Patterns
---------------------------

*   Use the Cauchy-Riemann equations to determine if a function is analytic.
*   Apply Cauchy's integral formula to evaluate an integral.

### Examples with Solutions
-----------------------------

### Example 1:

Suppose we have the function $f(z) = u(x,y) + iv(x,y)$, where $u(x,y) = x^2 - y^2$ and $v(x,y) = 3xy$. Determine if this function is analytic.

**Solution:**

*   Compute the partial derivatives of $u$ and $v$ with respect to $x$ and $y$.
*   Check if the Cauchy-Riemann equations are satisfied.

```latex
\begin{align*}
\frac{\partial u}{\partial x} &= 2x, & \quad \frac{\partial v}{\partial y} &= 3x \\
\frac{\partial u}{\partial y} &= -2y, & \quad \frac{\partial v}{\partial x} &= 3y
\end{align*}
```

Since the Cauchy-Riemann equations are satisfied, $f(z)$ is an analytic function.

### Example 2:

Evaluate the integral $\int_C \frac{1}{z^2 + 4} dz$, where $C$ is a circle centered at the origin with radius 2.

**Solution:**

*   Use Cauchy's integral formula to evaluate the integral.
*   Choose an appropriate value for $a$ and compute the derivative of the function at that point.

```latex
\begin{align*}
\int_C \frac{1}{z^2 + 4} dz &= \pi i \cdot \frac{1}{-a^2+4}\\
&= \frac{\pi}{4}i
\end{align*}
```

### Common Pitfalls
---------------------

*   Failing to recognize that a function is not analytic.
*   Misapplying Cauchy's integral formula.

### Quick Summary
-------------------

| Concept | Key Points |
| --- | --- |
| Complex Numbers | $z = x + iy$, $\bar{z} = x - iy$ |
| Analytic Functions | Differentiable at every point in its domain, Cauchy-Riemann equations |
| Cauchy's Integral Formula | Evaluates an integral around a simple closed curve |

### References
---------------

*   Ahlfors, L. V. (1979). Complex Analysis: An Introduction to the Theory of Analytic Functions of One Complex Variable.
*   Brown, J. W., & Churchill, R. V. (2008). Complex Variables and Applications.

Note:
Please make sure to provide a clear, step-by-step solution for each example. Also, ensure that you cover all relevant concepts tested in the source questions.