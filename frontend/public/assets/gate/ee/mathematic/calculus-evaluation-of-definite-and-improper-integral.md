**Calculus Evaluation of Definite and Improper Integrals**
=====================================================

**Introduction**
---------------

This note covers the evaluation of definite and improper integrals using calculus. It includes key concepts, formulas, problem-solving patterns, examples with solutions, and common pitfalls to watch out for.

**Core Concepts**
-----------------

### 1. Definite Integral

The definite integral of a function f(x) from a to b is denoted as ∫[a,b]f(x)dx and represents the area under the curve y = f(x) between x = a and x = b.

### 2. Improper Integral

An improper integral is an integral that has one or more infinite limits of integration. It can be used to calculate areas, volumes, and other quantities in problems where traditional definite integrals are not applicable.

**Key Formulas/Theorems**
-------------------------

*   **Fundamental Theorem of Calculus (FTC)**:

    ∫[a,b]f(x)dx = F(b) - F(a)

    where F(x) is the antiderivative of f(x).

*   **Power Rule for Integrals**:

    ∫x^n dx = (1/(n+1))x^(n+1) + C

    where n ≠ -1 and C is a constant.

*   **Improper Integral Formula**:

    ∫[a,∞)f(x)dx = lim(b→∞)∫[a,b]f(x)dx

    if the limit exists.

### LaTeX Code for Key Formulas/Theorems
```latex
\documentclass{article}
\begin{document}

$\int_{a}^{b} f(x) dx = F(b) - F(a)$\\
$\int x^n dx = \frac{x^{n+1}}{n+1} + C$\\
$\int_{a}^{\infty} f(x) dx = \lim_{b\to\infty} \int_{a}^{b} f(x) dx$

\end{document}
```

**Problem Solving Patterns**
---------------------------

*   **Integration by Substitution**: This method involves substituting a new variable into the integral to simplify it.
    *   Example: ∫(2x + 1)/(x^2 - 4) dx = ∫((2x + 1)/((x - 2)(x + 2))) dx
        Using substitution, let u = x^2 - 4. Then du/dx = 2x.
    *   Solution: ∫du/(u(x)) = ln|u| + C

*   **Integration by Parts**: This method involves differentiating one part of the integral and integrating the other.

**Examples with Solutions**
-------------------------

### Example 1:

Find the definite integral of x^2 from 0 to 1.

Solution:

∫[0,1]x^2 dx = ∫[0,1](x^3)/3 dx
Using the power rule for integrals,
= (1/4)x^4 | [0,1]
= (1/4) - 0
= 1/4

### Example 2:

Find the improper integral of x/(x^2 + 1) from 0 to ∞.

Solution:

∫[0,∞) x/(x^2 + 1) dx = lim(b→∞) ∫[0,b] x/(x^2 + 1) dx
Using integration by substitution,
= lim(b→∞) (1/2)ln(x^2 + 1) | [0,b]
= lim(b→∞) (1/2)ln(b^2 + 1) - 0
= ∞

**Common Pitfalls**
------------------

*   **Incorrect integration**: Be careful when integrating functions, as small mistakes can lead to incorrect results.
*   **Infinite limits**: When dealing with improper integrals, ensure that the limit exists and is finite.

**Quick Summary**
---------------

*   Definite integral: ∫[a,b]f(x)dx
*   Improper integral: ∫[a,∞)f(x)dx or ∫[-∞,b]f(x)dx
*   Power rule for integrals: ∫x^n dx = (1/(n+1))x^(n+1) + C
*   FTC: ∫[a,b]f(x)dx = F(b) - F(a)
*   Integration by substitution and parts are essential techniques.

This comprehensive note covers the key concepts, formulas, and problem-solving patterns required to evaluate definite and improper integrals using calculus. Review this material thoroughly to excel in your GATE CS exam.