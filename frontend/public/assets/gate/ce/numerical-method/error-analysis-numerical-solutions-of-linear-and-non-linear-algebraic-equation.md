**Error Analysis and Numerical Solutions of Linear and Non-Linear Algebraic Equations**
====================================================================

### Introduction
----------------

Numerical methods are essential tools for solving algebraic equations, particularly when analytical solutions are not feasible or impractical. In this note, we focus on error analysis and numerical solutions of linear and non-linear algebraic equations.

### Core Concepts
---------------

*   **Accuracy** refers to how close the approximate solution is to the exact solution.
*   **Precision** refers to the number of digits in the solution.
*   **Tolerance** is the acceptable range of error in the solution.

### Key Formulas/Theorems
-------------------------

*   **Trapezoidal Rule**: $\int_{a}^{b} f(x) dx \approx \frac{h}{2} [f(a) + 2\sum_{i=1}^{n-1} f(x_i) + f(b)]$, where $h = \frac{b-a}{n}$ and $x_i = a + ih$
*   **Simpson's Rule**: $\int_{a}^{b} f(x) dx \approx \frac{h}{3} [f(a) + 4\sum_{i=1}^{n/2-1} f(x_{2i}) + 2\sum_{i=1}^{n/2-1} f(x_{2i+1}) + f(b)]$, where $h = \frac{b-a}{n}$ and $x_i = a + ih$

### Problem Solving Patterns
-----------------------------

*   **Estimating Costs**: Direct cost, indirect cost, and markup rate are essential components in estimating costs for projects.
    *   Example: Q1 (ce_2021-M_12)
        ```
        Direct cost = 160000 Rs
        Indirect cost = 20000 Rs
        Markup rate = 10% of bid price

        Total estimated cost = Direct cost + Indirect cost = 180000 Rs
        Markup cost = 10% of 180000 Rs = 18000 Rs
        Quoted price = Total estimate cost + Markup cost = 198000 Rs
        ```
*   **Numerical Integration**: Use the trapezoidal rule or Simpson's rule to approximate the value of a definite integral.
    *   Example: Q2 (ce_2021-M_30)
        ```
        ∫x e^xdx = ?

        Using Trapezoidal Rule with 4 equal subintervals:
        h = (b - a) / n = 1
        x_i = a + ih = i

        f(x_i) = x_i \* e^(x_i)
        ∫x e^xdx ≈ (h / 2) [f(a) + 2\sum_{i=1}^{n-1} f(x_i) + f(b)]
        ```
*   **Error Analysis**: Consider the effects of round-off errors, truncation errors, and other numerical inaccuracies.

### Examples with Solutions
---------------------------

1.  **Estimating Costs**:
    ```markdown
    Direct cost = 160000 Rs
    Indirect cost = 20000 Rs
    Markup rate = 10% of bid price

    Total estimated cost = Direct cost + Indirect cost = 180000 Rs
    Markup cost = 10% of 180000 Rs = 18000 Rs
    Quoted price = Total estimate cost + Markup cost = 198000 Rs
    ```
2.  **Numerical Integration**:
    ```markdown
    ∫x e^xdx = ?

    Using Trapezoidal Rule with 4 equal subintervals:
    h = (b - a) / n = 1
    x_i = a + ih = i

    f(x_i) = x_i \* e^(x_i)
    ∫x e^xdx ≈ (h / 2) [f(a) + 2\sum_{i=1}^{n-1} f(x_i) + f(b)]
    ```

### Common Pitfalls
------------------

*   Inaccurate estimation of costs and markup rates can lead to incorrect quoted prices.
*   Incorrect application of numerical integration methods can result in errors.

### Quick Summary
---------------

*   **Estimating Costs**: Direct cost, indirect cost, and markup rate are essential components in estimating costs for projects.
*   **Numerical Integration**: Use the trapezoidal rule or Simpson's rule to approximate the value of a definite integral.
*   **Error Analysis**: Consider the effects of round-off errors, truncation errors, and other numerical inaccuracies.