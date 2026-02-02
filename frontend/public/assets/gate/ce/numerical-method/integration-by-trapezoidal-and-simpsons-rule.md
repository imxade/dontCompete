# Numerical Integration by Trapezoidal and Simpson's Rule
====================================================

## Introduction
---------------

Numerical integration is a method of approximating the value of a definite integral. The trapezoidal rule and Simpson's rule are two popular methods used to approximate integrals when an exact solution cannot be found analytically.

### Core Concepts
-----------------

#### Trapezoidal Rule

The trapezoidal rule approximates the area under a curve by dividing it into small trapezoids. The formula for the trapezoidal rule is:

$$\int_{a}^{b} f(x) \, dx \approx \frac{h}{2} \left[ f(a) + 2f(a+h) + 2f(a+2h) + ... + 2f(b-h) + f(b) \right]$$

where $h = (b-a)/n$ is the width of each subinterval.

#### Simpson's Rule

Simpson's rule approximates the area under a curve by dividing it into parabolic segments. The formula for Simpson's rule is:

$$\int_{a}^{b} f(x) \, dx \approx \frac{h}{3} \left[ f(a) + 4f(a+h) + 2f(a+2h) + ... + 2f(b-2h) + 4f(b-h) + f(b) \right]$$

where $h = (b-a)/n$ is the width of each subinterval.

### Key Formulas/Theorems
---------------------------

The trapezoidal rule and Simpson's rule are both approximations, so their accuracy depends on the number of subintervals used. The more subintervals, the closer the approximation will be to the exact value.

For the trapezoidal rule:

$$\text{Error} \leq \frac{(b-a)h^2}{12} f''(\xi)$$

where $f''(\xi)$ is the second derivative of $f(x)$ evaluated at some point $\xi$ in the interval $[a, b]$.

For Simpson's rule:

$$\text{Error} \leq \frac{(b-a)h^4}{180} f^{(4)}(\eta)$$

where $f^{(4)}(\eta)$ is the fourth derivative of $f(x)$ evaluated at some point $\eta$ in the interval $[a, b]$.

### Problem Solving Patterns
-----------------------------

1. **Divide and Conquer**: Divide the integral into smaller subintervals to make it easier to solve.
2. **Use a calculator or programming tool**: If possible, use a calculator or programming tool to perform numerical integration.
3. **Check for exact solutions**: Before using numerical methods, check if an exact solution is available.

### Examples with Solutions
---------------------------

**Example 1: Trapezoidal Rule**

Numerically integrate $\int_{0}^{2} x^2 \, dx$ using the trapezoidal rule with $n=5$ subintervals.

```latex
\int_{0}^{2} x^2 \, dx \approx \frac{h}{2} \left[ f(0) + 2f(h) + 2f(2h) + ... + 2f(b-h) + f(b) \right]
```

where $h = (b-a)/n = (2-0)/5 = 0.4$.

Solving for the values of $f(x)$ and plugging them into the formula, we get:

$$\int_{0}^{2} x^2 \, dx \approx 1.33$$

**Example 2: Simpson's Rule**

Numerically integrate $\int_{0}^{3} e^x \, dx$ using Simpson's rule with $n=4$ subintervals.

```latex
\int_{0}^{3} e^x \, dx \approx \frac{h}{3} \left[ f(0) + 4f(h) + 2f(2h) + ... + 2f(b-2h) + 4f(b-h) + f(b) \right]
```

where $h = (b-a)/n = (3-0)/4 = 0.75$.

Solving for the values of $f(x)$ and plugging them into the formula, we get:

$$\int_{0}^{3} e^x \, dx \approx 11.43$$

### Common Pitfalls
-------------------

1. **Incorrect evaluation of subinterval width**: Make sure to divide the interval into equal subintervals.
2. **Incorrect application of formulas**: Double-check that you are applying the correct formula for the trapezoidal rule or Simpson's rule.

### Quick Summary
------------------

*   Numerical integration is a method of approximating definite integrals using numerical methods.
*   The trapezoidal rule and Simpson's rule are two popular methods used to approximate integrals.
*   The accuracy of these methods depends on the number of subintervals used.
*   Use a calculator or programming tool if possible, and check for exact solutions before using numerical methods.

This theory note covers all the necessary concepts for solving problems involving the trapezoidal rule and Simpson's rule.