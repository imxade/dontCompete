**Differential Equations**
==========================

### Introduction

Differential equations are mathematical equations that describe how a quantity changes over time or space. They are essential tools for modeling and predicting real-world phenomena in various fields, including physics, engineering, economics, and biology.

### Core Concepts

#### Definition of a Differential Equation

A differential equation is an equation involving a function and its derivatives with respect to one or more variables.

*   **Ordinary Differential Equations (ODEs)**: Involves the derivative of a function with respect to a single variable.
*   **Partial Differential Equations (PDEs)**: Involves partial derivatives of a function with respect to multiple variables.

#### Types of Differential Equations

*   **Linear ODEs**: Can be written in the form $y' + P(x)y = Q(x)$, where $P$ and $Q$ are functions.
*   **Non-Linear ODEs**: Do not fit the linear form, often involving products or powers of derivatives.

#### Solution Methods

*   **Analytical Solutions**: Can be found using techniques like separation of variables, integration factors, and reduction of order.
*   **Numerical Solutions**: Use computational methods to approximate solutions when analytical ones are difficult to obtain.

### Key Formulas/Theorems

$$
\begin{aligned}
&amp;\text{Linear ODEs: } y' + P(x)y = Q(x) \\
&amp;\text{Euler's Method: } y_{n+1} = y_n + hf(y_n)
\end{aligned}
$$

### Problem Solving Patterns

*   **Separation of Variables**: Rearrange the equation to isolate variables and integrate both sides.
*   **Integration Factors**: Use a multiplying factor to make the left side of the equation exact.

### Examples with Solutions

**Example 1: Linear ODE Solution**

Solve $y' - y = 2x$ using an integrating factor.

```mermaid
graph LR
A[Linear ODE] -->|Integrate Factor|> B[Integration Factor]
B -->|Multiply Both Sides|> C[Simplified Equation]
C -->|Solve for y'|> D[Solution]
```

*   Find the integrating factor: $e^{\int -1 dx} = e^{-x}$.
*   Multiply both sides by the integrating factor: $(e^{-x})y' - (e^{-x})y = 2xe^{-x}$.
*   Recognize the left side as an exact derivative and integrate.

**Example 2: Numerical Solution**

Use Euler's method to approximate the solution of $y' = x + y$ with initial condition $y(0) = 1$. Take a step size of $h=0.5$.

```python
import numpy as np

def f(y, x):
    return x + y

x_values = [0]
y_values = [1]

for i in range(4): # we want to find the solution at 2 points (0, 1, 2, 3)
    h = 0.5
    new_x = x_values[-1] + h
    new_y = y_values[-1] + h * f(y_values[-1], x_values[-1])
    x_values.append(new_x)
    y_values.append(new_y)

print("Approximate solution at x=2:", y_values[2])
```

### Common Pitfalls

*   Forgetting to consider boundary conditions when solving PDEs.
*   Assuming a linear ODE is separable without attempting separation of variables.

### Quick Summary

*   Differential equations describe how quantities change over time or space.
*   Types include ordinary and partial, with linear and non-linear subcategories.
*   Analytical solutions can be found using various techniques; numerical methods approximate when difficult to obtain.