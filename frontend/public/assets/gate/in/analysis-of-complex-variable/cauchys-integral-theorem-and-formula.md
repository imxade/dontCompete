**Cauchy's Integral Theorem and Formula**
=====================================

### Introduction

Cauchy's Integral Theorem (CIT) and Formula are fundamental concepts in complex analysis, providing powerful tools for evaluating definite integrals of analytic functions. This note will cover the core principles, key formulas, problem-solving patterns, examples, common pitfalls, and a quick summary to help you excel in the GATE CS exam.

### Core Concepts

#### Analytic Functions

An analytic function is a function that can be represented as a power series within a region of the complex plane. The concept of analyticity is crucial for CIT and Formula.

#### Simply Connected Regions

A simply connected region is one where every closed curve can be continuously shrunk to a point without leaving the region. This concept is essential for CIT.

### Key Formulas/Theorems

$$\oint_{C} f(z) \, dz = 0$$

**Cauchy's Integral Theorem (CIT)**: If $f(z)$ is analytic in a simply connected region and $C$ is any closed curve within that region, then the integral of $f(z)$ over $C$ is zero.

$$\oint_{C} \frac{f(z)}{(z - z_0)^n} \, dz = 2\pi i \cdot \text{Res}(f, z_0)$$

**Cauchy's Integral Formula (CIF)**: If $f(z)$ is analytic in a simply connected region except for a point $z_0$ within the region, and $n$ is a positive integer, then the integral of $\frac{f(z)}{(z - z_0)^n}$ over any closed curve containing $z_0$ is equal to $2\pi i$ times the residue of $f$ at $z_0$.

### Problem Solving Patterns

1.  **Identify Analyticity**: Check if the function is analytic in the given region.
2.  **Apply CIT or CIF**: Based on the problem, apply either CIT or CIF to evaluate the integral.
3.  **Residue Calculation**: If applying CIF, calculate the residue of the function at the singular point.

### Examples with Solutions

**Example 1**

Evaluate $\oint_{C} \frac{1}{z^2 + 1} dz$, where $C$ is the unit circle centered at the origin.

Solution:

The integrand can be written as $\frac{1}{(z - i)(z + i)} = \frac{A}{z - i} + \frac{B}{z + i}$ for some constants $A, B$. Solving for $A, B$ and applying CIT yields the answer.

**Example 2**

Evaluate $\oint_{C} e^z dz$, where $C$ is a circle of radius $1$ centered at $0$.

Solution:

Applying CIT directly gives the answer, as $e^z$ is analytic in any region except possibly for a branch point, which does not exist here.

### Common Pitfalls

*   Misidentifying the type of singularities (pole vs. essential)
*   Failing to check if the function is analytic within the given region
*   Incorrect application of CIT or CIF

### Quick Summary

*   **Analytic Functions**: Can be represented as power series in a region.
*   **Simply Connected Regions**: Every closed curve can be shrunk to a point without leaving the region.
*   **Cauchy's Integral Theorem (CIT)**: $\oint_{C} f(z) \, dz = 0$ for analytic $f(z)$ and simply connected region.
*   **Cauchy's Integral Formula (CIF)**: $\oint_{C} \frac{f(z)}{(z - z_0)^n} \, dz = 2\pi i \cdot \text{Res}(f, z_0)$.

This note should equip you with a solid understanding of CIT and CIF, enabling you to tackle problems in the GATE CS exam with confidence.