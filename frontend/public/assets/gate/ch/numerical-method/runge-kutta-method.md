**Runge-Kutta Method**
======================

### Introduction

The Runge-Kutta method is a popular numerical technique for solving ordinary differential equations (ODEs) of the form $y' = f(x, y)$ with an initial condition $y(0) = y_0$. It's a second-order method that uses four function evaluations to compute an approximate solution at each time step. The Runge-Kutta method is widely used in various fields due to its high accuracy and stability.

### Core Concepts

The basic idea behind the Runge-Kutta method is to approximate the derivative $y'$ using Taylor series expansion up to the second order. This involves evaluating the function $f(x, y)$ at four different points: the current point $(x_n, y_n)$, two intermediate points, and the next point $(x_{n+1}, y_{n+1})$. The four intermediate points are:

*   $k_1 = f(x_n, y_n)$
*   $k_2 = f(x_n + \frac{h}{2}, y_n + \frac{k_1h}{2})$
*   $k_3 = f(x_n + \frac{h}{2}, y_n + \frac{k_2h}{2})$
*   $k_4 = f(x_n + h, y_n + k_3h)$

The Runge-Kutta method uses these four function evaluations to compute an approximate solution at the next time step using the following formula:

$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$

### Key Formulas/Theorems

*   The Runge-Kutta method is based on Taylor series expansion up to the second order:
    $y(x+h) = y(x) + hy'(x) + \frac{h^2}{2}y''(x) + O(h^3)$
    *   Note: This formula uses big-O notation, indicating that the error term is bounded by a constant times the cube of the step size $h$.
*   The Runge-Kutta method uses the following weights to compute an approximate solution:
    $\frac{1}{6}, \frac{2}{6}, \frac{2}{6}, \frac{1}{6}$

### Problem Solving Patterns

When applying the Runge-Kutta method, follow these steps:

1.  Evaluate the function $f(x, y)$ at four different points: $(x_n, y_n), (x_n + \frac{h}{2}, y_n + \frac{k_1h}{2}), (x_n + \frac{h}{2}, y_n + \frac{k_2h}{2}),$ and $(x_n + h, y_n + k_3h)$
2.  Compute the intermediate points $k_1, k_2, k_3,$ and $k_4$
3.  Use the weights to compute an approximate solution at the next time step:
    $y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$

### Examples with Solutions

**Example 1**

Solve the ODE $\frac{dy}{dx} = 2x^2y$ with an initial condition $y(0) = 1$ using a step size of $h=0.5$ and compute the approximate solution at $x=0.5$

```markdown
## Solution

First, evaluate the function f(x,y) at four different points:

k_1 = f(x_n, y_n) = f(0, 1) = 2(0)^2(1) = 0
k_2 = f(x_n + \frac{h}{2}, y_n + \frac{k_1h}{2}) = f(0.25, 1.25) ≈ 2(0.25)^2(1.25) ≈ 0.15625
k_3 = f(x_n + \frac{h}{2}, y_n + \frac{k_2h}{2}) = f(0.25, 1.0625) ≈ 2(0.25)^2(1.0625) ≈ 0.140625
k_4 = f(x_n + h, y_n + k_3h) = f(0.5, 1.28125) ≈ 2(0.5)^2(1.28125) ≈ 0.25625

Next, compute the intermediate points:

y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)
≈ 1 + \frac{0.5}{6}(0 + 2(0.15625) + 2(0.140625) + 0.25625)
≈ 1.2404167
```

**Example 2**

Solve the ODE $\frac{dy}{dx} = x^3y$ with an initial condition $y(0) = 2$ using a step size of $h=0.5$ and compute the approximate solution at $x=0.5$

```markdown
## Solution

First, evaluate the function f(x,y) at four different points:

k_1 = f(x_n, y_n) = f(0, 2) = 0^3(2) = 0
k_2 = f(x_n + \frac{h}{2}, y_n + \frac{k_1h}{2}) = f(0.25, 2) ≈ (0.25)^3(2) ≈ 0.015625
k_3 = f(x_n + \frac{h}{2}, y_n + \frac{k_2h}{2}) = f(0.25, 2.00078125) ≈ (0.25)^3(2.00078125) ≈ 0.014765625
k_4 = f(x_n + h, y_n + k_3h) = f(0.5, 2.000390625) ≈ (0.5)^3(2.000390625) ≈ 0.0390625

Next, compute the intermediate points:

y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)
≈ 2 + \frac{0.5}{6}(0 + 2(0.015625) + 2(0.014765625) + 0.0390625)
≈ 2.0003125
```

### Common Pitfalls

*   **Incorrect function evaluations**: Make sure to evaluate the function $f(x, y)$ at all four points correctly.
*   **Rounding errors**: Be careful with rounding errors when computing intermediate points and weights.
*   **Step size selection**: Choose an appropriate step size $h$ for the problem.

### Quick Summary

*   Runge-Kutta method is a second-order numerical technique for solving ODEs.
*   Use Taylor series expansion up to the second order to approximate derivative $y'$.
*   Evaluate function $f(x, y)$ at four points and compute intermediate points using weights.
*   Apply the formula $y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$ to get an approximate solution.

**Practice Questions**

Try solving the following problems using the Runge-Kutta method:

1.  Solve the ODE $\frac{dy}{dx} = x^2y$ with an initial condition $y(0) = 1$ using a step size of $h=0.5$ and compute the approximate solution at $x=0.5$
2.  Solve the ODE $\frac{dy}{dx} = xy^2$ with an initial condition $y(0) = 2$ using a step size of $h=0.5$ and compute the approximate solution at $x=0.5$

**Source Questions**

*   Question 25 (ch_2021_25)

```markdown
## Source Question

Question 25: Use Runge-Kutta second order method to numerically integrate the ODE $\frac{dy}{dx} = 2x^2y$ with an initial condition $y(0) = 1$. Compute the approximate solution at $x=0.5$ using a step size of $h=0.5$.

## Solution

First, evaluate the function f(x,y) at four different points:

k_1 = f(x_n, y_n) = f(0, 1) = 2(0)^2(1) = 0
k_2 = f(x_n + \frac{h}{2}, y_n + \frac{k_1h}{2}) = f(0.25, 1.25) ≈ 2(0.25)^2(1.25) ≈ 0.15625
k_3 = f(x_n + \frac{h}{2}, y_n + \frac{k_2h}{2}) = f(0.25, 1.0625) ≈ 2(0.25)^2(1.0625) ≈ 0.140625
k_4 = f(x_n + h, y_n + k_3h) = f(0.5, 1.28125) ≈ 2(0.5)^2(1.28125) ≈ 0.25625

Next, compute the intermediate points:

y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)
≈ 1 + \frac{0.5}{6}(0 + 2(0.15625) + 2(0.140625) + 0.25625)
≈ 1.2404167
