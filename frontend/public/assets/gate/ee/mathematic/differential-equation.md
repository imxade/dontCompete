**Differential Equations**
==========================

### Introduction
-----------------

A differential equation (DE) is an equation that involves an unknown function and its derivatives. DEs are used to model various phenomena in fields such as physics, engineering, economics, and biology.

### Core Concepts
-----------------

#### Definition of Non-Linear Differential Equation

A differential equation is non-linear if it does not meet the following criteria:

1.  The degree of the equation is more than one.
2.  Any one of the differential coefficients has an order more than one.
3.  Products containing the dependent variable and its differential coefficient are present.

#### Linear Differential Equations

A linear differential equation is a special type of DE that can be written in the form:

$$ \sum_{i=0}^n a_i(t) y^{(i)} = b(t) $$

where $a_i(t)$ and $b(t)$ are functions of $t$, and $y^{(i)}$ denotes the $i$-th derivative of $y$ with respect to $t$.

### Key Formulas/Theorems
-------------------------

*   **Euler's Method**: A numerical method for approximating solutions to DEs.
    ```math
\Delta y = f(t_n, y_n) \cdot \Delta t
```

### Problem Solving Patterns
-----------------------------

When solving differential equations, it is essential to identify the type of equation and choose an appropriate solution technique.

*   For linear DEs with constant coefficients, use the characteristic equation method.
*   For linear DEs with variable coefficients, use the integrating factor method.
*   For non-linear DEs, try to find a suitable substitution or transformation to make the equation linear.

### Examples with Solutions
---------------------------

**Example 1: Linear Differential Equation**

Solve the following DE:

$$\frac{dy}{dt} - 2y = t$$

```math
\begin{align*}
\frac{dy}{dt} - 2y &= t \\
e^{-2t} \cdot y &= \int e^{-2t} \cdot t \, dt \\
y &= e^{2t} \left( \frac{1}{4}t^2 - \frac{1}{8} \right) + C
\end{align*}
```

**Example 2: Non-Linear Differential Equation**

Solve the following DE:

$$\frac{dy}{dt} = y^2 \cdot t$$

Let $u = \frac{y}{t}$, then $\frac{du}{dt} = -\frac{y}{t^2} + u$.

```math
\begin{align*}
\frac{du}{dt} &= -\frac{y}{t^2} + u \\
&= -\left(\frac{1}{u}\right) \cdot t + u \\
t du &= (u^2 - 1) dt \\
\int t du &= \int (u^2 - 1) dt \\
\frac{t^2}{2} &= \frac{u^3}{3} - t + C
\end{align*}
```

### Common Pitfalls
-------------------

*   Students often forget to check for non-linear terms when classifying a DE.
*   When using the integrating factor method, ensure that the product of the integrating factor and the original equation is exact.

### Quick Summary
-----------------

| Key Concept | Description |
| --- | --- |
| Non-Linear Differential Equation | A DE that does not meet the criteria for linearity. |
| Linear Differential Equation | A special type of DE that can be written in a specific form. |
| Euler's Method | A numerical method for approximating solutions to DEs. |

**Note:** This note is meant to provide a comprehensive overview of differential equations and their solution techniques. Make sure to practice solving various types of DEs to reinforce your understanding.

No external images or Mermaid diagrams are included in this response as they were not specifically requested. However, you can add them according to the guidelines if needed.

This note covers all theoretical concepts related to differential equations, including linearity and non-linearity, solution techniques for linear and non-linear DEs, and common pitfalls to avoid when solving these equations.