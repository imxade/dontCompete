**Partial Differential Equations (PDEs)**
=====================================

**Introduction**
---------------

A partial differential equation (PDE) is a mathematical equation that describes how a function of several variables changes over time and space. PDEs are used to model a wide range of phenomena, from fluid dynamics and heat transfer to wave propagation and population dynamics.

**Core Concepts**
-----------------

### What is a PDE?

A PDE is an equation involving an unknown function u(x,y) that depends on the independent variables x and y. It typically has derivatives with respect to both x and y, making it distinct from ordinary differential equations (ODEs).

### Classification of PDEs

PDEs can be classified into several types based on their order and linearity:

* **Linear PDEs**: Linear in the dependent variable u(x,y) and its derivatives.
* **Nonlinear PDEs**: Nonlinear in the dependent variable u(x,y) or its derivatives.

### Key Formulas/Theorems

LaTeX notation will be used to display mathematical formulas.

**Laplace Equation**

$$\nabla^2u = \frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} = 0$$

**Wave Equation**

$$\frac{\partial^2u}{\partial t^2} = c^2\nabla^2u$$

**Heat Equation**

$$\frac{\partial u}{\partial t} = \alpha \nabla^2u$$

### Problem Solving Patterns

1. **Identify the type of PDE**: Determine if it's linear or nonlinear, and identify the order.
2. **Apply separation of variables**: Assume a solution of the form u(x,y) = X(x)Y(y) and separate the variables.
3. **Solve the resulting ODEs**: Solve for X(x) and Y(y) separately.

**Examples with Solutions**

### Example 1: Laplace Equation

Given $\nabla^2u = 0$ in a square domain, find u(x,y).

Solution:

* Assume u(x,y) = X(x)Y(y)
* Separate variables: $X''(x)Y(y) + Y''(y)X(x) = 0$
* Solve ODEs: $X''(x) = -\lambda^2X(x)$ and $Y''(y) = \lambda^2Y(y)$
* Apply boundary conditions: u(0,y) = u(l,y) = 0, u(x,0) = u(x,l) = 0

### Example 2: Heat Equation

Given $\frac{\partial u}{\partial t} = \alpha \nabla^2u$ in a square domain with initial condition u(x,y,0) = f(x,y), find u(x,y,t).

Solution:

* Assume u(x,y,t) = U(x,y)e^{-\lambda^2t}
* Separate variables: $U''(x)Y(y)e^{-\lambda^2t} + Y''(y)U(x)e^{-\lambda^2t} = -\alpha \lambda^2 U(x,y)e^{-\lambda^2t}$
* Solve ODEs: $U''(x) + \lambda^2 U(x) = 0$ and $Y''(y) - \lambda^2 Y(y) = 0$

**Common Pitfalls**

1. **Incorrect identification of PDE type**: Be careful to distinguish between linear and nonlinear PDEs.
2. **Insufficient application of boundary conditions**: Always apply the correct boundary conditions for each problem.

**Quick Summary**
-----------------

* Understand the classification of PDEs (linear, nonlinear)
* Apply separation of variables
* Solve resulting ODEs
* Use Laplace Equation, Wave Equation, and Heat Equation formulas
* Apply boundary conditions correctly

Note: This is just a starting point. Please let me know if you'd like me to elaborate or add more content!