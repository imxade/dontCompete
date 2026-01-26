**Integration Theory Note**
==========================

### Introduction
-----------------

Integration is a fundamental concept in Calculus that deals with finding the area under curves, volumes of solids, and other quantities. It's essential to understand the theoretical aspects of integration to tackle problems effectively.

### Core Concepts
-----------------

#### Definition of Integration

$$\int_{a}^{b} f(x) \, dx = F(b) - F(a)$$

where $F$ is the antiderivative (indefinite integral) of $f(x)$.

#### Types of Integrals

*   **Definite Integral**: $\int_{a}^{b} f(x) \, dx$
*   **Indefinite Integral** (Antiderivative): $F(x)$ such that $F'(x) = f(x)$
*   **Improper Integral**: Used for functions with infinite limits or discontinuities

### Key Formulas/Theorems
---------------------------

#### Fundamental Theorem of Calculus

$$\int_{a}^{b} f(x) \, dx = F(b) - F(a)$$

where $F$ is the antiderivative (indefinite integral) of $f(x)$.

#### Mean Value Theorem for Integrals

If a function $f(x)$ is continuous on the interval $[a,b]$, then there exists a number $c \in [a,b]$ such that:

$$\int_{a}^{b} f(x) \, dx = f(c)(b-a)$$

### Problem Solving Patterns
-----------------------------

1.  **Recognize the Function**: Identify the function for which you need to find the integral.
2.  **Choose a Method**:
    *   **Substitution Method**: Use $u$-substitution to simplify the integrand.
    *   **Integration by Parts**: Apply the product rule in reverse to integrate products of functions.
    *   **Partial Fractions**: Break down rational functions into simpler fractions.
3.  **Solve the Integral**:
    *   Evaluate the antiderivative at the given limits.

### Examples with Solutions
-----------------------------

#### Example 1: Evaluating a Definite Integral

Find $\int_{0}^{2} x^2 \, dx$

*   **Step 1**: Choose a method (substitution)
*   **Step 2**: Apply substitution $u = x^3$
*   **Step 3**: Evaluate the antiderivative at the given limits
$$\int_{0}^{2} x^2 \, dx = \left[\frac{x^3}{3}\right]_0^2 = \frac{8}{3} - 0 = \frac{8}{3}$$

#### Example 2: Using Integration by Parts

Find $\int x \cdot e^x \, dx$

*   **Step 1**: Choose a method (integration by parts)
*   **Step 2**: Apply the product rule in reverse
*   **Step 3**: Evaluate the antiderivative at the given limits
$$\int x \cdot e^x \, dx = xe^x - \int e^x \, dx = xe^x - e^x + C$$

### Common Pitfalls
--------------------

1.  **Incorrect Limits of Integration**: Double-check that you're integrating over the correct interval.
2.  **Misidentifying the Function**: Ensure you understand the function for which you need to find the integral.

### Quick Summary
-------------------

*   Understand the concept of integration as finding areas under curves or volumes of solids.
*   Recall key formulas and theorems (Fundamental Theorem of Calculus, Mean Value Theorem).
*   Recognize common problem-solving patterns: substitution method, integration by parts, partial fractions.

This comprehensive theory note should equip you with a solid understanding of integration concepts, enabling you to tackle questions like CS_2022_59 effectively.