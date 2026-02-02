**Differential Equations**
=========================

### Introduction

Differential equations are mathematical statements that describe how a quantity changes over time or space. They are fundamental to modeling real-world phenomena, and their solutions provide insights into physical systems. In this section, we will cover the core concepts of differential equations, key formulas, problem-solving patterns, and examples with solutions.

### Core Concepts

#### Definition

A differential equation is an equation that involves an unknown function and its derivatives.

*   **Ordinary Differential Equation (ODE)**: An ODE has a derivative with respect to one independent variable.
    *   Example: $\frac{dy}{dx} = 3x^2$
*   **Partial Differential Equation (PDE)**: A PDE has derivatives with respect to multiple independent variables.
    *   Example: $\frac{\partial u}{\partial t} + c \frac{\partial u}{\partial x} = f(x,t)$

#### Types of ODEs

*   **Linear ODE**: An ODE that can be written in the form $y' + p(t)y = q(t)$.
    *   Example: $\frac{dy}{dx} - 2x y = e^{-x^2}$
*   **Nonlinear ODE**: An ODE that cannot be written in linear form.
    *   Example: $\frac{dy}{dx} + y^2 = \sin(x)$

### Key Formulas/Theorems

#### Linear Independence of Solutions

A set of solutions is said to be linearly independent if none of the solutions can be expressed as a linear combination of the others.

*   **Wronskian Test**: If the Wronskian of the solutions is nonzero, then the solutions are linearly independent.
    *   $W = \begin{vmatrix} y_1 & y_2 \\ y_1' & y_2' \end{vmatrix}$

#### Existence and Uniqueness Theorem

If a function f(t,x) satisfies certain conditions, then there exists a unique solution to the ODE.

*   **Peano's Theorem**: If $f: [a,b] \times \mathbb{R} \to \mathbb{R}$ is continuous and Lipschitz in x, then there exists a unique solution to the ODE.
    *   $\frac{\partial f}{\partial t} + f(t,x) = g(x)$

### Problem Solving Patterns

*   **Separation of Variables**: Separate the variables y and x on opposite sides of the equation.
    *   Example: $\frac{dy}{dx} = \frac{x^2 + 1}{y}$
*   **Integrating Factor Method**: Use an integrating factor to simplify the ODE.

### Examples with Solutions

#### Example 1

Solve the ODE:

$$\frac{dy}{dx} = x^2 y$$

**Solution**

Separate the variables: $$\frac{dy}{y} = x^2 dx$$
Integrate both sides: $$\ln|y| = \frac{x^3}{3} + C$$

#### Example 2

Solve the ODE:

$$\frac{d^2 y}{dx^2} - 4\frac{dy}{dx} + 4y = e^{-x}$$

**Solution**

Use Laplace transform: $$s^2 Y(s) - sy(0) - y'(0) - 4 ( sY(s) - y(0) ) + 4Y(s) = \mathcal{L}\left\{e^{-x}\right\}$$
Solve for Y(s): $$Y(s) = \frac{s+1}{(s^2-16)(s-1)}$$

### Common Pitfalls

*   **Forgetting to check the initial conditions**: Make sure to check the initial conditions carefully.
*   **Misusing the integrating factor method**: Use the integrating factor method only when necessary.

### Quick Summary

*   Differential equations are mathematical statements that describe how a quantity changes over time or space.
*   Ordinary differential equations (ODEs) have derivatives with respect to one independent variable, while partial differential equations (PDEs) have derivatives with respect to multiple independent variables.
*   Linear ODEs can be written in the form $y' + p(t)y = q(t)$, while nonlinear ODEs cannot.
*   The Wronskian test is used to check linear independence of solutions.
*   Peano's theorem provides conditions for existence and uniqueness of solutions.