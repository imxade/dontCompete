**Integral and Differential Calculus**
=====================================

### Introduction
----------------

Integral calculus deals with finding the accumulation of quantities, such as area under curves, volumes of solids, and other physical quantities. It involves integrating functions to find the total or the result of a function over an interval. On the other hand, differential calculus is concerned with rates of change and slopes of curves at specific points.

### Core Concepts
----------------

#### Limits
---------------

The concept of limits is crucial in both integral and differential calculus. A limit represents the behavior of a function as the input or independent variable approaches a certain value.

*   **One-sided limits**: 
    ```
\lim_{x \to c^-} f(x) = L
```
    *   The limit exists if there is a finite number `L` that `f(x)` approaches as `x` gets arbitrarily close to `c` from the left side.

#### Differentiation
------------------

Differentiation rules are essential in differential calculus. They help us find the derivative of functions, which represents the rate of change of the function with respect to its input variable.

*   **Power Rule**:
    ```
\frac{d}{dx} x^n = nx^{n-1}
```

#### Integration
----------------

Integration is a process of finding the antiderivative (indefinite integral) or definite integral of a function. It's used extensively in both pure mathematics and engineering applications.

*   **Fundamental Theorem of Calculus**:
    ```
\int_{a}^{b} f(x) \,dx = F(b) - F(a)
```

### Key Formulas/Theorems
-------------------------

*   **Integrals of standard functions**
    ```
\int x^n \,dx = \frac{x^{n+1}}{n+1}
\int e^x \,dx = e^x + C
\int \sin(x) \,dx = -\cos(x) + C
\int \cos(x) \,dx = \sin(x) + C
```

### Problem Solving Patterns
---------------------------

#### Integrals of the form $\int \frac{f'(x)}{f(x)} dx$
--------------------------------------------------------

These types of integrals can often be solved using logarithmic functions.

*   **Solving $\int \frac{f'(x)}{f(x)} dx$**

    Let `u = f(x)`, then `du/dx = f'(x)` and the integral becomes:

    ```
\int \frac{1}{u} du
```

    This can be integrated directly as follows:

    ```
\ln |u| + C
```

#### Using substitution in integrals
--------------------------------------

Substitution is a powerful technique for solving complex integrals.

*   **Using `u`-substitution**
    
    Let `u = g(x)`, then `du/dx = g'(x)` and the integral becomes:

    ```
\int f(g(x)) \cdot g'(x) dx
```

### Examples with Solutions
---------------------------

#### Example 1: Evaluating $\int_{0}^{2} x^2 dx$

*   Using the power rule, we have:
    ```
\int_{0}^{2} x^2 dx = \left[\frac{x^3}{3}\right]_{0}^{2}
```

#### Example 2: Evaluating $\int \sin(x) dx$

*   We can use the following formula:

    ```
\int \sin(x) dx = -\cos(x) + C
```

### Common Pitfalls
-------------------

1.  **Missing limits**: Make sure to include all necessary limits when solving integrals.
2.  **Incorrect substitution**: Ensure that your `u`-substitution is correct, as small mistakes can lead to incorrect answers.

### Quick Summary
----------------

*   Limits are a crucial concept in both integral and differential calculus.
*   Differentiation rules help us find the rate of change of functions.
*   Integration is used extensively in both pure mathematics and engineering applications.
*   Standard integrals of functions like `x^n`, `e^x`, `sin(x)`, and `cos(x)` can be memorized for quick reference.

Note: This document aims to provide a comprehensive overview of integral and differential calculus. The examples provided are meant to illustrate key concepts, but they should not be considered exhaustive.