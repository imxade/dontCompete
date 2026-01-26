**Differential Equations**
==========================

### Introduction
A differential equation is a mathematical equation involving an unknown function and its derivatives. It's a fundamental tool for modeling real-world phenomena, making it a crucial subject in engineering mathematics.

### Core Concepts
Differential equations describe how quantities change over time or space. They can be classified into several types:

* **Ordinary Differential Equations (ODEs)**: Involving an unknown function of one independent variable and its derivatives.
* **Partial Differential Equations (PDEs)**: Involving an unknown function of multiple independent variables and its partial derivatives.

**Key Formulas/Theorems**

* **Euler's Method**: A numerical method for solving ODEs, $x_{n+1} = x_n + hf(x_n)$.
* **Separation of Variables**: For PDEs, $\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$ can be solved using this method.

### Problem Solving Patterns

#### Homogeneous vs. Nonhomogeneous ODEs
A homogeneous ODE has the form $y' = f(y/x)$, while a nonhomogeneous ODE is of the form $y' + P(x)y = Q(x)$. Use these definitions to identify the type of ODE.

#### Exact ODEs
An ODE is exact if $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$, where $M$ and $N$ are functions of $x$ and $y$.

### Examples with Solutions

**Q1 Solution**

The differential equation is:

$$u_{xx} + u_y = 0$$

Using separation of variables, we get:

$$v(x)w'(y) + v'(x)w(y) = 0$$

Integrating, we find the general solution to be:

$$u(x,y) = f(y)g(x) + h(x)$$

**Q2 Solution**

The differential equation is:

$$\frac{dy}{dx} - \frac{y}{x} - \frac{5.5}{9.5x^2} + \frac{2.5}{x^3} = 0$$

This is a nonhomogeneous ODE with $P(x) = -1/x$ and $Q(x) = (5.5/9.5)x^{-2} - 2.5x^{-3}$.

**Common Pitfalls**

* Failing to identify the type of differential equation.
* Not using separation of variables for PDEs.
* Incorrect application of Euler's method.

### Quick Summary

* Types of DEs: ODEs, PDEs
* Key formulas/theorems: Euler's method, Separation of Variables
* Problem-solving patterns:
	+ Homogeneous vs. nonhomogeneous ODEs
	+ Exact ODEs
	+ Q1 and Q2 solutions as examples