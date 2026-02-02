**Complex Variables: Theory Notes**
=====================================

### Introduction
-------------

Complex variables are a fundamental aspect of engineering mathematics, with applications in fields such as electrical engineering, control systems, and signal processing. This note will cover the essential concepts and formulas required to tackle problems involving complex variables.

### Core Concepts
-----------------

A **complex number** is an extension of the real numbers, represented as $z = x + iy$, where $x$ and $y$ are real numbers, and $i$ is the imaginary unit defined by $i^2 = -1$. The **conjugate** of a complex number $z = x + iy$ is denoted by $\overline{z} = x - iy$.

### Key Formulas/Theorems
-------------------------

#### 1. Modulus and Argument

The **modulus** (or magnitude) of a complex number $z = x + iy$ is given by:

$$|z| = \sqrt{x^2 + y^2}$$

The **argument** of a complex number $z = x + iy$ is the angle $\theta$ it makes with the positive real axis, measured counterclockwise:

$$\arg(z) = \tan^{-1}\left(\frac{y}{x}\right)$$

#### 2. Complex Exponential and Logarithm

The **complex exponential** function is defined as:

$$e^z = e^{x+iy} = e^x (\cos(y) + i\sin(y))$$

The **complex logarithm** function is a multi-valued function, but we can restrict it to the principal branch:

$$\log(z) = \ln|z| + i(\arg(z) + 2k\pi), \quad k \in \mathbb{Z}$$

#### 3. Contour Integrals

A **contour integral** of a function $f(z)$ over a curve $C$ is defined as:

$$\int_C f(z) dz = \oint f(z) dz$$

where the integration is taken in the counterclockwise direction.

### Problem Solving Patterns
---------------------------

#### 1. Evaluating Contour Integrals

To evaluate a contour integral, we can use the following patterns:

*   If $f(z)$ is analytic within and on the contour $C$, then $\int_C f(z) dz = 0$ (Cauchy's Theorem).
*   If $f(z)$ has poles inside the contour $C$, we can apply the Residue Theorem to evaluate the integral.

#### 2. Simplifying Complex Expressions

To simplify complex expressions, we can use the following patterns:

*   Use trigonometric identities (e.g., $\sin^2(x) + \cos^2(x) = 1$).
*   Apply De Moivre's Theorem for complex exponentials.

### Examples with Solutions
---------------------------

**Example 1: Contour Integral**

Evaluate the contour integral $\int_C e^{z^2} dz$, where $C$ is the unit circle centered at the origin in the complex plane.

**Solution**

Since $e^{z^2}$ is analytic within and on the contour $C$, we can apply Cauchy's Theorem:

$$\int_C e^{z^2} dz = 0$$

**Example 2: Complex Exponential**

Simplify the expression $(1 + i)^8$.

**Solution**

Apply De Moivre's Theorem for complex exponentials:

$$(1 + i)^8 = (\sqrt{2})^8 (\cos(\pi/4) + i\sin(\pi/4))^8$$

Use trigonometric identities to simplify the expression:

$$(1 + i)^8 = 16 (i - \sqrt{3})$$

### Common Pitfalls
-------------------

*   Students often forget that contour integrals are taken in the counterclockwise direction.
*   Be careful when applying De Moivre's Theorem for complex exponentials; ensure you use the correct argument and modulus.

### Quick Summary
-----------------

| Concept | Description |
| --- | --- |
| Complex number | $z = x + iy$ |
| Modulus | $|z| = \sqrt{x^2 + y^2}$ |
| Argument | $\arg(z) = \tan^{-1}\left(\frac{y}{x}\right)$ |
| Contour integral | $\int_C f(z) dz = \oint f(z) dz$ (counterclockwise direction) |

This note covers the essential concepts and formulas required to tackle problems involving complex variables. Make sure to practice solving example problems to solidify your understanding!