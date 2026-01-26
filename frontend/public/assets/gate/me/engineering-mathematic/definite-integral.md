**Definite Integral**
=====================

**Introduction**
---------------

The definite integral is a fundamental concept in calculus, used to find the area under curves and solve various engineering problems. It is essential for GATE CS exam aspirants to have a solid understanding of this topic.

**Core Concepts**
-----------------

### Definition of Definite Integral

The definite integral of a function $f(x)$ with respect to $x$ from $a$ to $b$ is denoted by:

$$\int_{a}^{b} f(x) dx$$

### Properties of Definite Integrals

*   **Additivity**: $\int_{a}^{c} f(x) dx = \int_{a}^{b} f(x) dx + \int_{b}^{c} f(x) dx$
*   **Homogeneity**: $\int_{a}^{b} kf(x) dx = k\int_{a}^{b} f(x) dx$

### Integration Rules

*   **Linearity**: $\int_{a}^{b} (f(x) + g(x)) dx = \int_{a}^{b} f(x) dx + \int_{a}^{b} g(x) dx$
*   **Constant Multiple Rule**: $\int_{a}^{b} kf(x) dx = k\int_{a}^{b} f(x) dx$

**Key Formulas/Theorems**
-------------------------

$$\begin{aligned}
\int x^n dx &= \frac{x^{n+1}}{n+1} + C \\
\int e^x dx &= e^x + C
\end{aligned}$$

### Simpson's One-Third Rule

Simpson's one-third rule is a numerical integration technique used to approximate the definite integral. It states that:

$$\int_{a}^{b} f(x) dx \approx \frac{h}{3} \left[ f(a) + 4f\left(\frac{a+b}{2}\right) + f(b) \right]$$

where $h$ is the interval size.

**Problem Solving Patterns**
---------------------------

1.  **Recognize the Type of Integral**: Identify whether the integral can be solved using a specific rule or formula.
2.  **Apply Integration Rules**: Use properties such as additivity and homogeneity to simplify the integral.
3.  **Numerical Methods**: Employ techniques like Simpson's one-third rule for approximate solutions.

**Examples with Solutions**
-------------------------

### Example 1: Using Linearity Property

Find $\int_{0}^{2} (x^2 + x) dx$ using the linearity property.

$$\begin{aligned}
\int_{0}^{2} (x^2 + x) dx &= \int_{0}^{2} x^2 dx + \int_{0}^{2} x dx \\
&= \left[\frac{x^3}{3}\right]_0^2 + \left[\frac{x^2}{2}\right]_0^2 \\
&= \frac{8}{3} + 1
\end{aligned}$$

### Example 2: Simpson's One-Third Rule

Approximate $\int_{0}^{4} x dx$ using Simpson's one-third rule with $h = 1$.

$$\begin{aligned}
\int_{0}^{4} x dx &\approx \frac{1}{3} \left[ f(0) + 4f(2) + f(4) \right] \\
&= \frac{1}{3} \left[ 0 + 4(2) + 4 \right] \\
&= \frac{12}{3}
\end{aligned}$$

**Common Pitfalls**
-------------------

*   **Failing to Recognize Integral Type**: Not identifying the appropriate rule or formula for a particular integral.
*   **Incorrect Application of Integration Rules**: Misapplying properties like additivity and homogeneity.

**Quick Summary**
------------------

*   Definite integral definition
*   Properties (additivity, homogeneity)
*   Integration rules (linearity, constant multiple)
*   Simpson's one-third rule

This comprehensive theory note covers all the necessary concepts for solving definite integrals in GATE CS exam. By mastering these techniques and formulas, students can confidently tackle questions like Q1 (ID: me_2021-N\_10).