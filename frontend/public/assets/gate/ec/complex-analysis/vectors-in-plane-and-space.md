# Vectors in Plane and Space
=====================================

## Introduction
---------------

Vectors are mathematical objects that have both magnitude (length or size) and direction. In this note, we will focus on vectors in plane and space, which are crucial concepts in complex analysis.

## Core Concepts
----------------

### Vector Operations

*   **Addition**: Two vectors $\mathbf{a}$ and $\mathbf{b}$ can be added by simply adding their corresponding components: $\mathbf{a} + \mathbf{b} = (a_1+b_1, a_2+b_2)$.
*   **Scalar Multiplication**: A vector $\mathbf{a}$ multiplied by a scalar $c$ results in a new vector whose magnitude is scaled by the absolute value of $c$: $c\mathbf{a} = (ca_1, ca_2)$.

### Vector Magnitude and Direction

*   **Magnitude**: The magnitude or length of a vector $\mathbf{a}$ is given by: $|\mathbf{a}| = \sqrt{a_1^2 + a_2^2}$.
*   **Direction**: A unit vector in the direction of $\mathbf{a}$ can be obtained by dividing $\mathbf{a}$ by its magnitude: $\hat{\mathbf{a}} = \frac{\mathbf{a}}{|\mathbf{a}|}$.

### Vector Cross Product

The cross product of two vectors $\mathbf{a} = (a_1, a_2)$ and $\mathbf{b} = (b_1, b_2)$ is given by:

$$
\begin{aligned}
\mathbf{a} \times \mathbf{b} &= a_1b_2 - a_2b_1 \\
&= \begin{vmatrix}
a_1 & a_2 \\
b_1 & b_2
\end{vmatrix}
\end{aligned}
$$

## Key Formulas/Theorems
-------------------------

*   **Vector Addition Formula**: $\mathbf{a} + \mathbf{b} = (a_1+b_1, a_2+b_2)$.
*   **Scalar Multiplication Formula**: $c\mathbf{a} = (ca_1, ca_2)$.
*   **Magnitude Formula**: $|\mathbf{a}| = \sqrt{a_1^2 + a_2^2}$.

## Problem Solving Patterns
---------------------------

When dealing with complex integrals like $\oint_C z^2 dz$, where $z$ is a complex variable and $C$ is a closed path in the complex plane, we can apply techniques such as:

*   **Partial Fractions**: Break down a rational function into simpler fractions.
*   **Residue Theorem**: Evaluate a contour integral by finding residues at poles enclosed by the contour.

## Examples with Solutions
---------------------------

### Example 1: Evaluating a Complex Integral

Evaluate $\oint_C z^2 dz$, where $C$ is the unit circle centered at the origin in the complex plane.

Solution:

Since $z$ is a complex variable, we can let $z = x + iy$ and substitute this into the integral. We get:

$$
\begin{aligned}
\oint_C (x+iy)^2 (dx + idy) &= \int_0^{2\pi} (x^2-y^2 + i(2xy)) dx \\
&= \left[ x^3 - xy^2 - i(x^2 y - y^3) \right]_{0}^{2\pi} \\
&= 8\pi^3
\end{aligned}
$$

## Common Pitfalls
-------------------

*   **Overlooking symmetries**: Make sure to consider the symmetry of the problem when dealing with complex integrals.
*   **Miscalculating residues**: Double-check your residue calculations to avoid errors.

## Quick Summary
-----------------

| Concept | Formula/Description |
| --- | --- |
| Vector Addition | $\mathbf{a} + \mathbf{b} = (a_1+b_1, a_2+b_2)$ |
| Scalar Multiplication | $c\mathbf{a} = (ca_1, ca_2)$ |
| Magnitude | $|\mathbf{a}| = \sqrt{a_1^2 + a_2^2}$ |
| Vector Cross Product | $\mathbf{a} \times \mathbf{b} = a_1b_2 - a_2b_1$ |

This note should provide a comprehensive overview of vectors in plane and space, covering key concepts, formulas, and problem-solving patterns. By reviewing this material, students should be well-prepared to tackle questions like the one from GATE 2022, question 32.