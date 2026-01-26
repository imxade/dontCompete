# Analysis of Complex Variable
=====================================

## Introduction
---------------

Complex variables are mathematical objects that extend the real numbers to a two-dimensional plane. This topic deals with the analysis of complex functions, which are functions whose domain and range are subsets of the complex numbers.

## Core Concepts
-----------------

### Definition of Complex Numbers

A **complex number** is an expression of the form $z = x + iy$, where $x$ and $y$ are real numbers and $i$ is the imaginary unit, satisfying $i^2 = -1$. The set of complex numbers is denoted by $\mathbb{C}$.

### Geometric Representation

Complex numbers can be represented geometrically as points in the **complex plane**, where the x-axis represents the real part and the y-axis represents the imaginary part. This representation allows us to visualize operations on complex numbers, such as addition and multiplication.

## Key Formulas/Theorems
-------------------------

### Modulus and Argument

*   The **modulus** of a complex number $z = x + iy$ is given by $|z| = \sqrt{x^2 + y^2}$.
*   The **argument** of a complex number $z = x + iy$ is given by $\arg(z) = \tan^{-1}\left(\frac{y}{x}\right)$.

### Multiplication

The product of two complex numbers $z_1 = x_1 + iy_1$ and $z_2 = x_2 + iy_2$ is given by:

$$
\begin{aligned}
(z_1)(z_2) &= (x_1 + iy_1)(x_2 + iy_2) \\
&= (x_1x_2 - y_1y_2) + i(x_1y_2 + x_2y_1)
\end{aligned}
$$

## Problem Solving Patterns
---------------------------

### Analyzing the Given Circuit

To solve question ID: `in_2023_39`, we need to analyze the given circuit and understand how it relates to complex numbers.

Given that $z^{-1} = \frac{1}{z}$, where $z$ denotes a complex number, let:

$$
\begin{aligned}
f(z) &= jz \\
&= i(x + iy) \\
&= ix - y
\end{aligned}
$$

The inverse function $f^{-1}(z)$ maps the real axis to the **unit circle with centre at the origin**, as it satisfies the equation:

$$
\begin{aligned}
|f(z)| &= |ix - y| \\
&= \sqrt{x^2 + (-y)^2} \\
&= \sqrt{x^2 + y^2} \\
&= 1
\end{aligned}
$$

### Solving for Inverse Function

To solve the inverse function $f^{-1}(z)$, we need to find a value of $x$ such that:

$$
\begin{aligned}
y &= f(z) \\
&= ix - x \\
&= 0
\end{aligned}
$$

This gives us $x = y$, which is the equation of the **unit circle**.

## Examples with Solutions
---------------------------

### Example 1: Finding Modulus and Argument

Find the modulus and argument of the complex number $z = 3 + 4i$.

*   The modulus is given by:

$$
\begin{aligned}
|z| &= \sqrt{x^2 + y^2} \\
&= \sqrt{3^2 + 4^2} \\
&= 5
\end{aligned}
$$

*   The argument is given by:

$$
\begin{aligned}
\arg(z) &= \tan^{-1}\left(\frac{y}{x}\right) \\
&= \tan^{-1}\left(\frac{4}{3}\right)
\end{aligned}
$$

### Example 2: Multiplication of Complex Numbers

Find the product of the complex numbers $z_1 = 2 + 3i$ and $z_2 = 4 - 5i$.

Using the formula for multiplication:

$$
\begin{aligned}
(z_1)(z_2) &= (x_1x_2 - y_1y_2) + i(x_1y_2 + x_2y_1) \\
&= (2 \cdot 4 - 3 \cdot (-5)) + i(2 \cdot (-5) + 4 \cdot 3) \\
&= 23 - 14i
\end{aligned}
$$

## Common Pitfalls
-------------------

*   Confusing the modulus and argument of a complex number.
*   Misapplying the formula for multiplication of complex numbers.

## Quick Summary
-----------------

### Key Concepts:

*   Complex numbers: $z = x + iy$
*   Modulus: $|z| = \sqrt{x^2 + y^2}$
*   Argument: $\arg(z) = \tan^{-1}\left(\frac{y}{x}\right)$
*   Multiplication: $(z_1)(z_2) = (x_1x_2 - y_1y_2) + i(x_1y_2 + x_2y_1)$

### Key Formulas:

*   Modulus: $|z|$
*   Argument: $\arg(z)$
*   Multiplication: $(z_1)(z_2)$