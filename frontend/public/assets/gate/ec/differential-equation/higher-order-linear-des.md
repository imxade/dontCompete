**Higher Order Linear Differential Equations**
=============================================

### Introduction
----------------

A higher-order linear differential equation is a mathematical equation involving an unknown function and its derivatives, with coefficients that are functions of the independent variable. These equations play a crucial role in modeling real-world phenomena in fields like physics, engineering, and economics.

### Core Concepts
-----------------

*   **Linear Differential Equation**: A differential equation is said to be linear if it can be written in the form

$$\sum_{i=0}^{n} P_i(x)y^{(i)} = Q(x)$$

where $P_i(x)$ and $Q(x)$ are functions of $x$.
*   **Order of a Differential Equation**: The order of a differential equation is the highest derivative present in it. For example, the order of $\frac{d^2y}{dx^2} - \frac{dy}{dx} + y = 0$ is two.

### Key Formulas/Theorems
-------------------------

*   **General Solution**: The general solution of a homogeneous linear differential equation of order $n$ is given by

$$y = c_1y_1(x) + c_2y_2(x) + \dots + c_ny_n(x)$$

where $c_i$ are arbitrary constants and $\{y_i\}$ are the linearly independent solutions.
*   **Particular Solution**: A particular solution is a specific solution to the differential equation. To find a particular solution, we need additional initial conditions.

### Problem Solving Patterns
-----------------------------

1.  **Understand the Question**: Before diving into solving the problem, carefully read and understand what's being asked.
2.  **Identify the Type of Differential Equation**: Determine if it's homogeneous or non-homogeneous and identify its order.
3.  **Solve the Homogeneous Part**: First solve the homogeneous part using characteristic equations or other methods to find the complementary function.
4.  **Find a Particular Solution**: Use the method of undetermined coefficients, variation of parameters, or any suitable technique to find a particular solution.

### Examples with Solutions
---------------------------

**Example 1:**

Solve $\frac{d^2y}{dx^2} - 5\frac{dy}{dx} + 6y = e^{3x}$

*   **Step 1**: Find the complementary function using characteristic equation $r^2-5r+6=0$. This gives us roots $r=2$ and $r=3$, so the complementary function is $c_1e^{2x} + c_2e^{3x}$.
*   **Step 2**: Find a particular solution using the method of undetermined coefficients. Assume that the particular solution has the form $y_p = Axe^Bx$. Substituting this into the differential equation and equating coefficients, we find that the particular solution is $y_p = x^3e^{3x}$.

**Solution:**

The general solution is

$$y = c_1e^{2x} + c_2e^{3x} + x^3e^{3x}.$$

### Common Pitfalls
------------------

*   **Forget to Check if the Particular Solution Satisfies the Original Differential Equation**
*   **Incorrectly Identify the Type of Differential Equation**

### Quick Summary
-----------------

*   Higher-order linear differential equations are used to model real-world phenomena.
*   Linear differential equation: $\sum_{i=0}^{n} P_i(x)y^{(i)} = Q(x)$
*   General solution: $y = c_1y_1(x) + c_2y_2(x) + \dots + c_ny_n(x)$