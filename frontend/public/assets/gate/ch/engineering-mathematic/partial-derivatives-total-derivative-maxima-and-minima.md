**Partial Derivatives, Total Derivative, Maxima and Minima**
===========================================================

### Introduction
-----------------

In this topic, we will cover fundamental concepts of multivariable calculus, including partial derivatives, total derivative, and maxima/minima. These concepts are crucial in solving problems that involve change of variables, optimization, and thermodynamics.

### Core Concepts
------------------

*   **Partial Derivatives**: A partial derivative of a function f(x,y) with respect to x is denoted by ∂f/∂x or fx, while the partial derivative with respect to y is denoted by ∂f/∂y or fy.
    
    ```
    ∂f/∂x = fx = lim(h → 0) [f(x+h,y) - f(x,y)]/h
    ```

*   **Total Derivative**: The total derivative of a function f(x,y) with respect to x is given by:

    ```
    df = (∂f/∂x)(dx) + (∂f/∂y)(dy)
    ```
    
*   **Maxima and Minima**: These refer to the maximum or minimum values of a function. The necessary condition for a maxima or minima at a point (a, b) is that ∂f/∂x = 0 and ∂f/∂y = 0 at (a, b).

### Key Formulas/Theorems
-------------------------

*   **Chain Rule**: If f(x,y) = g(h(x,y)), then:

    ```
    df/dx = (∂g/∂h)(dh/dx)
    ```

*   **Total Derivative Formula**: The total derivative of a function f(x,y) with respect to x is given by:

    ```
    df = (∂f/∂x)(dx) + (∂f/∂y)(dy)
    ```

### Problem Solving Patterns
---------------------------

1.  **Identify the Function**: Clearly identify the function for which you are finding partial derivatives or total derivative.
2.  **Compute Partial Derivatives**: Compute ∂f/∂x and ∂f/∂y using the definition of a partial derivative.
3.  **Apply the Chain Rule**: If necessary, apply the chain rule to find the total derivative.

### Examples with Solutions
---------------------------

### Example 1

Find the partial derivatives of f(x,y) = x^2 y^2.

Solution:
∂f/∂x = 2xy^2 and ∂f/∂y = 2x^2 y

### Example 2

Find the total derivative of f(x,y) = x^3 - y^3 at (a, b).

Solution:

df = (∂f/∂x)(dx) + (∂f/∂y)(dy)
= (3x^2)(dx) - (3y^2)(dy)

### Common Pitfalls
------------------

*   **Confusing Partial Derivatives with Total Derivative**: Make sure to use the correct notation and formula for partial derivatives or total derivative.
*   **Incorrectly Applying the Chain Rule**: Double-check that you are applying the chain rule correctly.

### Quick Summary
---------------

*   **Partial Derivatives**:
    *   ∂f/∂x = fx = lim(h → 0) [f(x+h,y) - f(x,y)]/h
    *   ∂f/∂y = fy = lim(h → 0) [f(x,y+h) - f(x,y)]/h
*   **Total Derivative**:
    *   df = (∂f/∂x)(dx) + (∂f/∂y)(dy)
*   **Maxima and Minima**: ∂f/∂x = 0 and ∂f/∂y = 0 at (a, b)

### Source Question Analysis
---------------------------

*   Q1: The molar heat capacity at constant pressure for n-pentane as a function of temperature is given by:

    pC_T = 2.46 + 45.4 × 10^(-3)T - 14.1 × 10^(-6)T^2

    At 1000 K, the rate of change of molar entropy of n-pentane with respect to temperature at constant pressure is _______

Solution:

pC_T = 2.46 + 45.4 × 10^(-3)T - 14.1 × 10^(-6)T^2

To find the rate of change of molar entropy, we need to find ∂pC_T/∂T.

∂pC_T/∂T = 45.4 × 10^(-3) - 28.2 × 10^(-6)T

At T = 1000 K:

∂pC_T/∂T ≈ 45.4 × 10^(-3)

Note that the rate of change of molar entropy is equal to ∂pC_T/∂T.

ANSWER: 0.0454