**Differential Equations**
=========================

**Introduction**
---------------

Differential equations are a fundamental tool for modeling and analyzing various phenomena in engineering, physics, and other disciplines. They describe how quantities change over time or space, making them indispensable for problem-solving and optimization.

**Core Concepts**
-----------------

A differential equation is an equation that involves an unknown function and its derivatives. The general form of a first-order differential equation is:

$$\frac{dy}{dx} = f(x,y)$$

where $f(x,y)$ is a function of $x$ and $y$. Higher-order differential equations involve higher-order derivatives.

**Types of Differential Equations**
---------------------------------

1.  **Ordinary Differential Equation (ODE)**: Involves ordinary derivatives with respect to one independent variable.
2.  **Partial Differential Equation (PDE)**: Involves partial derivatives with respect to multiple independent variables.

**Key Formulas/Theorems**
-------------------------

### First-Order Linear ODE

The general solution of a first-order linear ODE is given by:

$$\frac{dy}{dx} + P(x)y = Q(x) \quad \implies \quad y = \int e^{\int P(x) dx}Q(x) dx + C$$

### Second-Order Linear Homogeneous ODE

The general solution of a second-order linear homogeneous ODE is given by:

$$ay'' + by' + cy = 0 \quad \implies \quad y = c_1 e^{r_1x} + c_2 e^{r_2x}$$

### Laplace Transform

The Laplace transform of a function $f(x)$ is defined as:

$$\mathcal{L}\{f(x)\} = F(s) = \int_0^\infty f(x)e^{-sx} dx$$

**Problem Solving Patterns**
---------------------------

1.  **Separation of Variables**: Separate the variables in the differential equation and integrate both sides separately.
2.  **Integration Factor Method**: Use an integration factor to simplify the differential equation and then integrate.
3.  **Euler's Method**: Numerically approximate the solution using Euler's method.

**Examples with Solutions**
---------------------------

### Example 1: First-Order Linear ODE

Consider the differential equation:

$$\frac{dy}{dx} + P(x)y = Q(x) \quad \implies \quad y' + P(x)y = Q(x)$$

The general solution is given by:

$$y = e^{\int P(x) dx} \left( \int e^{-\int P(x) dx}Q(x) dx + C \right)$$

### Example 2: Second-Order Linear Homogeneous ODE

Consider the differential equation:

$$ay'' + by' + cy = 0 \quad \implies \quad y'' + \frac{b}{a}y' + \frac{c}{a}y = 0$$

The general solution is given by:

$$y = c_1 e^{r_1x} + c_2 e^{r_2x}$$

**Common Pitfalls**
------------------

1.  **Misunderstanding the type of differential equation**: Ensure you understand whether it's an ODE or PDE.
2.  **Incorrect application of formulas**: Double-check your work to ensure correct application of formulas and theorems.
3.  **Insufficient practice**: Regularly practice solving different types of differential equations.

**Quick Summary**
-----------------

*   First-order linear ODE: General solution given by $y = \int e^{\int P(x) dx}Q(x) dx + C$
*   Second-order linear homogeneous ODE: General solution given by $y = c_1 e^{r_1x} + c_2 e^{r_2x}$
*   Laplace transform: $\mathcal{L}\{f(x)\} = F(s) = \int_0^\infty f(x)e^{-sx} dx$

### Source Questions

**ce\_2023-N\_36**
-------------------

Given the differential equation:

$$\frac{dy}{dx} + P(x)y = Q(x) \quad \implies \quad 2.5y'' - y' - \frac{9.5}{x^2}y = 0$$

The solution is expressed as $y = Ce^{1/x} + De^{-2.5/x}$.

What are the values of $\alpha$ and $\beta$?

A) 1 and 2
B) -1 and -2
C) 2 and 3
D) -2 and -3

**ce\_2020-M\_9**
------------------

In a two-dimensional stress analysis, the state of stress at a point P is given by:

$$\begin{bmatrix} \sigma_{xx} & \tau_{xy} \\ \tau_{yx} & \sigma_{yy} \end{bmatrix} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$$

What is the necessary and sufficient condition for existence of the state of pure shear at the point P?

A) $0 = \sigma_{xx}\sigma_{yy} - \tau_{xy}^2$
B) $0 = \tau_{xy}$
C) $0 = \sigma_{xx}\sigma_{yy} - \tau_{xy}^2 + 1$
D) $0 = \sigma_{xx}\sigma_{yy} - 4\tau_{xy}^2$

**ce\_2024-M\_11**
------------------

The smallest positive root of the equation:

$$x^5 - x^4 - x^3 + x^2 - 10x + 50 = 0$$

lies in the range:

A) $0 \leq x < 2$
B) $2 \leq x \leq 4$
C) $6 \leq x \leq 8$
D) $10 \leq x \leq 100$

**ce\_2024-M\_12**
------------------

The second-order differential equation in an unknown function u(x, y):

$$\frac{\partial^2 u}{\partial x^2} = f(x,y)\frac{\partial u}{\partial y} + g(x)u$$

Assuming $f(x,y)$ and $g(x)$ are known functions, what is the general solution of the above differential equation?

A) $u(x,y) = \int e^{x}\left( \int f(x,y)e^{-x}dy\right)dx + C$
B) $u(x,y) = \int x f(y) \left(\int g(x)e^{-y}dy\right) dx + C$
C) $u(x,y) = \int x f(y)\left( \int e^{x}g(x) dx\right) dy + C$
D) $u(x,y) = \int y g(x) \left(\int f(x,y)e^{-y}dy\right) dx + C$