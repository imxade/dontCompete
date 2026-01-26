**Numerical Methods**
=====================

**Introduction**
---------------

Numerical methods are techniques used to approximate solutions to mathematical problems, often when an exact solution is not feasible. These methods are crucial in various fields of engineering and science where precise analytical solutions may be difficult or impossible to obtain.

**Core Concepts**
-----------------

### Iterative Methods

Iterative methods involve starting with an initial guess for the solution and repeatedly applying a formula or procedure until convergence or a stopping criterion is reached. The Newton-Raphson method is a popular iterative method used to find roots of functions.

#### Newton-Raphson Method

Given a function $f(x)$ and its derivative $f'(x)$, the Newton-Raphson method iteratively updates an initial guess $x_0$ using the formula:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

### Runge-Kutta Method

The Runge-Kutta method is a numerical technique used to solve ordinary differential equations (ODEs) of the form $y' = f(x,y)$ with an initial condition. The second-order Runge-Kutta method uses the following formula:

$$y_{n+1} = y_n + \frac{h}{2}(k_1 + k_2)$$

where

$$\begin{aligned}
k_1 &= f(x_n, y_n) \\
k_2 &= f(x_n + h, y_n + hk_1)
\end{aligned}$$

**Key Formulas/Theorems**
-------------------------

### Newton-Raphson Method Formula

LaTeX: $$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

### Runge-Kutta Method Formula

LaTeX: $$y_{n+1} = y_n + \frac{h}{2}(k_1 + k_2)$$

**Problem Solving Patterns**
---------------------------

* When using the Newton-Raphson method, ensure to differentiate the function with respect to $x$ and apply the iterative formula.
* For the Runge-Kutta method, calculate $k_1$ and $k_2$ separately and use them to update the solution.

**Examples with Solutions**
---------------------------

### Example 1: Newton-Raphson Method

Given $f(x) = e^x - 5x$ and an initial guess of $x_0 = 1$, find the next iterate using the Newton-Raphson method.

$$\begin{aligned}
f'(x) &= e^x - 5 \\
\text{First iteration:} \quad x_{n+1} &= x_n - \frac{f(x_n)}{f'(x_n)} \\
&= 1 - \frac{e^1 - 5}{e^1 - 5} \\
&= 0
\end{aligned}$$

### Example 2: Runge-Kutta Method

Given the ODE $y' = f(x,y)$ with an initial condition $(x_0, y_0) = (0, 1)$ and analytical solution $y = e^{x^2}$, use the second-order Runge-Kutta method to approximate $y$ at $x = 0.5$ with a step size of $h = 0.5$.

$$\begin{aligned}
k_1 &= f(0, 1) \\
&= 1 \\
k_2 &= f(0 + h, 1 + hk_1) \\
&= f(0.5, 1 + 0.5 \cdot 1) \\
y_{n+1} &= y_n + \frac{h}{2}(k_1 + k_2) \\
&= 1 + \frac{0.5}{2}(1 + f(0.5, 2)) \\
\end{aligned}$$

**Common Pitfalls**
------------------

* When applying the Newton-Raphson method, ensure to check for convergence or a stopping criterion.
* In the Runge-Kutta method, be aware of the step size and its impact on accuracy.

**Quick Summary**
-----------------

* Iterative methods (Newton-Raphson) are used to find roots of functions.
* Numerical techniques (Runge-Kutta) solve ODEs with initial conditions.
* Formulas and patterns:
	+ Newton-Raphson: $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
	+ Runge-Kutta: $y_{n+1} = y_n + \frac{h}{2}(k_1 + k_2)$