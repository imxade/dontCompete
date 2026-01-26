**Differential Equations: First-Order Linear and Nonlinear Equations**
===========================================================

### Introduction

Differential equations are fundamental to various fields of mathematics, science, and engineering. This note focuses on first-order linear and nonlinear differential equations, a crucial topic for GATE CS exam.

### Core Concepts

A **differential equation** is an equation involving an unknown function's derivative(s) or integral(s). The goal is to find the solution (function) that satisfies the given equation.

#### Linear Differential Equations

A first-order linear differential equation has the form:

$$\frac{dy}{dx} + P(x)y = Q(x)$$

where $P(x)$ and $Q(x)$ are functions of $x$.

The general solution to a first-order linear differential equation is given by:

$$y(x) = \int\left[\frac{\exp\left(\int P(x)\,dx\right)}{1}\cdot Q(x)\right]\,dx + C$$

where $C$ is the constant of integration.

#### Nonlinear Differential Equations

Nonlinear differential equations do not satisfy the linear equation form. They often arise in real-world problems and are more challenging to solve.

### Key Formulas/Theorems

*   **Separation of Variables**: For nonlinear equations, we can separate variables by moving all terms involving $y$ to one side and integrating.
    $$\frac{dy}{dx} = f(x,y)$$
    Separating variables:
    $$\frac{dy}{f(x,y)} = dx$$
    Integrating both sides:

$$\int \frac{dy}{f(x,y)} = \int dx$$

*   **Exact Equations**: If $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$, where $M$ and $N$ are functions of $(x,y)$, the equation is exact.

    $$M(x,y)dx + N(x,y)dy = 0$$

*   **Bernoulli's Equation**: A nonlinear differential equation with the form:

    $$\frac{dy}{dx} + P(x)y = Q(x)y^n$$

    where $n$ is a constant. We can use substitution to solve this equation.

### Problem Solving Patterns

1.  **Check for Exactness**: Identify if the equation is exact by checking $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$.
2.  **Separate Variables**: For nonlinear equations, try separating variables to make integration easier.
3.  **Identify Bernoulli's Equation**: If the equation has a form resembling Bernoulli's equation, use substitution to simplify.

### Examples with Solutions

1.  **Linear Differential Equation**

    \[y' + P(x)y = Q(x)\]

    $$\frac{dy}{dx} + x^2 y = e^{x^2}\]

    General solution:

    \[y(x) = \int\left[\frac{\exp\left(\int x^2\,dx\right)}{1}\cdot e^{x^2}\right]\,dx + C\]
    $$y(x) = \int e^{x^4} dx + C$$
    Solution:

    \[y(x) = \frac{e^{x^4}}{4x^3} + C\]

2.  **Nonlinear Differential Equation (Separation of Variables)**

    $$\frac{dy}{dx} = e^{xy}\]

    Separating variables:

    $$\int y' dx = \int e^{xy} dy$$
    Integrate both sides:

    \[y \log|x| + C_1 = x e^{xy} + C_2\]

### Common Pitfalls

*   **Incorrect Identification of Equation Type**: Make sure to identify the equation type correctly (linear, nonlinear, exact) before applying solution techniques.
*   **Insufficient Integration**: Double-check your integration steps to avoid mistakes.

### Quick Summary

*   First-order linear differential equations have the form $\frac{dy}{dx} + P(x)y = Q(x)$
*   General solution for first-order linear DEs is $y(x) = \int\left[\frac{\exp\left(\int P(x)\,dx\right)}{1}\cdot Q(x)\right]\,dx + C$
*   Nonlinear differential equations can be solved using separation of variables or exact equation methods
*   Bernoulli's Equation has the form $\frac{dy}{dx} + P(x)y = Q(x)y^n$ and requires substitution for solution.