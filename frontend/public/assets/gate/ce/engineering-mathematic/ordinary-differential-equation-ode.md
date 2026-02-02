**Ordinary Differential Equations (ODEs)**

### Introduction
Ordinary Differential Equations are a fundamental tool in mathematical modeling and analysis of physical systems. An ODE relates an unknown function to its derivatives, describing how quantities change over time or space.

### Core Concepts

#### Definition
An Ordinary Differential Equation is a relation between the derivative(s) of an unknown function and the function itself:

\[ \frac{dy}{dx} = f(x,y) \]

where $y$ is the dependent variable, $x$ is the independent variable, and $f(x,y)$ is a function representing the rate of change.

#### Types of ODEs

* **Linear ODE**: Has the form $\frac{dy}{dx} + P(x)y = Q(x)$.
* **Nonlinear ODE**: Does not fit the linear form.
* **Homogeneous ODE**: $f(x,y) = 0$ implies $y = 0$ is a solution.
* **Exact ODE**: Can be written as $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$ for some functions $M(x,y)$ and $N(x,y)$.

### Key Formulas/Theorems

#### Existence and Uniqueness Theorem
If $f(x,y)$ is continuous in a region containing $(x_0,y_0)$, then there exists a unique solution to the IVP:

$$ \frac{dy}{dx} = f(x,y), \quad y(x_0) = y_0 $$

#### Euler's Method
A numerical method for approximating solutions:

\[ y_{n+1} = y_n + hf(x_n, y_n) \]

where $h$ is the step size.

### Problem Solving Patterns

* **Separation of Variables**: If $\frac{dy}{dx}$ can be expressed as a function of $x$ and $y$, try separating variables.
* **Integration Factors**: Use an integrating factor to convert a linear ODE into a separable one.

### Examples with Solutions

#### Example 1: Homogeneous ODE
Solve the homogeneous ODE:

$$ \frac{dy}{dx} = y - x^2 $$

```latex
\begin{align*}
\frac{dy}{dx} &= y - x^2 \\
\Rightarrow\qquad \int \frac{dy}{y-x^2} &= \int dx \\
\Rightarrow\qquad \ln|y-x^2| &= x + C
\end{align*}
```

#### Example 2: Exact ODE
Solve the exact ODE:

$$ (x^2+y^2)\frac{dy}{dx} = 2xy $$

```latex
\begin{align*}
(x^2+y^2)\frac{dy}{dx} &= 2xy \\
\Rightarrow\qquad \int y d(x^2+y^2) &= \int 2x dx \\
\Rightarrow\qquad \frac{x^3}{3} + x^2y + \frac{y^3}{3} &= C
\end{align*}
```

### Common Pitfalls

* **Forgetting to check if an ODE is exact before trying to solve it.**
* **Misinterpreting the results of numerical methods, such as Euler's method.**

### Quick Summary
Key points for revision:

• Definition and types of ODEs
• Existence and uniqueness theorem
• Separation of variables and integration factors
• Examples with solutions (homogeneous and exact ODEs)