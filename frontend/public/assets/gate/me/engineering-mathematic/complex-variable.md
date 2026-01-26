# Complex Variables Theory Note
===========================

## Introduction

Complex variables are a fundamental concept in mathematics and engineering, providing a powerful tool for analyzing systems that involve periodic or rotational motion. The study of complex variables involves functions and integrals on the complex plane.

## Core Concepts

*   **Complex Numbers**: A complex number $z$ is defined as $x + iy$, where $x$ and $y$ are real numbers, and $i = \sqrt{-1}$. The set of all complex numbers is denoted by $\mathbb{C}$.
*   **Conjugate**: The conjugate of a complex number $z = x + iy$ is defined as $\overline{z} = x - iy$.

## Key Formulas/Theorems

### 1. Cauchy-Riemann Equations

The Cauchy-Riemann equations are a fundamental tool for analyzing functions on the complex plane. Given a function $f(z) = u(x, y) + iv(x, y)$, where $z = x + iy$, the Cauchy-Riemann equations are given by:

$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
$$

### 2. Cauchy's Integral Theorem

Cauchy's integral theorem states that if a function $f(z)$ is analytic within a region $R$ and on its boundary, then the contour integral of $f(z)$ over any simple closed curve within $R$ is zero.

$$
\oint_R f(z) \, dz = 0
$$

### 3. Cauchy's Integral Formula

Cauchy's integral formula states that if a function $f(z)$ is analytic at and within a region bounded by a simple closed curve $C$, then for any point $z_0$ within the region:

$$
\oint_C \frac{f(z)}{z - z_0} \, dz = 2\pi i f(z_0)
$$

## Problem Solving Patterns

### Pattern 1: Contour Integration

To solve contour integrals of the form $\int_{C} f(z) \, dz$, where $f(z)$ is analytic within and on the boundary of a region bounded by a simple closed curve $C$:

*   Use Cauchy's integral formula or theorem to evaluate the integral.
*   Choose an appropriate parameterization for the curve.

### Pattern 2: Analytic Functions

To determine if a function $f(z)$ is analytic within a region, use the Cauchy-Riemann equations and check for differentiability.

## Examples with Solutions

### Example 1: Contour Integration

Let $C$ be the unit circle centered at the origin in the complex plane. Evaluate the contour integral $\oint_C \frac{1}{z^2} dz$, where integration is taken counter-clockwise.

```math
\begin{aligned}
& \oint_C \frac{1}{z^2} dz \\
= & \oint_C z^{-2} dz \\
= & \int_{0}^{2\pi} i e^{i\theta} d\theta \\
= & i \left[ e^{i\theta} \right]_0^{2\pi} \\
= & 0
\end{aligned}
```

### Example 2: Analytic Functions

Determine if the function $f(z) = z^2 + 1$ is analytic within a region bounded by the unit circle.

Using the Cauchy-Riemann equations, we have:

$$
\begin{aligned}
& \frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} \\
\end{aligned}
$$

where $u(x, y) = (x^2 + 1) + y^2$, and $v(x, y) = 0$.

Solving for the partial derivatives:

$$
\begin{aligned}
& \frac{\partial u}{\partial x} = 2x, \qquad \frac{\partial u}{\partial y} = 2y \\
& \frac{\partial v}{\partial x} = 0, \qquad \frac{\partial v}{\partial y} = 0
\end{aligned}
$$

Since the Cauchy-Riemann equations are satisfied within and on the unit circle, $f(z) = z^2 + 1$ is analytic within this region.

## Common Pitfalls

*   Not checking if a function satisfies the Cauchy-Riemann equations.
*   Incorrectly parameterizing a curve for contour integration.

## Quick Summary

| Concept | Key Points |
| --- | --- |
| Complex Numbers | $z = x + iy$; $\overline{z} = x - iy$ |
| Conjugate | $\overline{z} = x - iy$ |
| Cauchy-Riemann Equations | $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$ |
| Cauchy's Integral Theorem | $\oint_R f(z) \, dz = 0$ if $f(z)$ is analytic within and on the boundary of $R$ |
| Cauchy's Integral Formula | $\oint_C \frac{f(z)}{z - z_0} \, dz = 2\pi i f(z_0)$ for any point $z_0$ within a region bounded by a simple closed curve $C$ |

I hope this comprehensive theory note helps you in your preparation for the GATE CS exam!