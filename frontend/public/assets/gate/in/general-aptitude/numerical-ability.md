**Numerical Ability - General Aptitude**
=====================================

### Introduction
-----------------

This section covers essential concepts and techniques for solving numerical ability problems in the GATE CS exam. Numerical ability tests one's ability to reason and solve mathematical problems, particularly those involving algebraic manipulations, geometry, and spatial reasoning.

### Core Concepts
------------------

#### 1. Functions and Graphs

A function $f(x)$ is a relation between a set of inputs (called the domain) and a set of possible outputs (called the range). It assigns to each input exactly one output.

*   **Domain**: The set of all possible input values for which the function is defined.
*   **Range**: The set of all possible output values that the function can produce.

#### 2. Differentiation

Differentiation is a mathematical operation used to find the derivative of a function, representing the rate of change of the function with respect to one of its variables.

*   Given a function $f(x)$, its derivative $f'(x)$ represents the instantaneous rate of change of $f$ at the point $x$.

### Key Formulas/Theorems
-------------------------

#### 1. Differentiation Rules

| Rule | Formula |
| --- | --- |
| Power Rule | $\frac{d}{dx}(x^n) = nx^{n-1}$ |
| Product Rule | $\frac{d}{dx}(uv) = u'v + uv'$ |
| Quotient Rule | $\frac{d}{dx}\left(\frac{u}{v}\right) = \frac{u'v - uv'}{v^2}$ |

### Problem Solving Patterns
-----------------------------

#### 1. Min/Max Problems

To find the minimum or maximum value of a function subject to certain constraints, we can use Lagrange multipliers.

*   **Lagrange Multiplier Method**: This method involves introducing a new variable (the Lagrange multiplier) and forming a Lagrangian function.
    ```mermaid
    graph LR
    A[Min/Max Problem] --> B[Lagrangian Function]
    ```
    Example: Find the minimum value of $f(x,y) = x^2 + y^2$ subject to $x+y=1$. 
    The Lagrangian function is given by: 
    $L(x,y,\lambda) = f(x,y) - \lambda (x+y-1)$.
    We then differentiate the Lagrangian with respect to $x$, $y$, and $\lambda$, and set each of them equal to zero.

### Examples with Solutions
---------------------------

#### 1. Q1: Question 42

Consider the function $f(x,y) = \frac{2}{x} + \frac{1}{y}$, subject to the constraint $x+y=1$. Find the minimum value of this function on the line $x=y-1$.

*   We start by substituting $y=1-x$ into the function:
    $\begin{aligned}
    f(x,y) &= \frac{2}{x} + \frac{1}{y} \\
    &=\frac{2}{x} +\frac{1}{1-x}\\
    & = \left(\frac{x+1}{x(1-x)}\right)
    \end{aligned}$.
*   Differentiating the function with respect to $x$, we get:
    $\begin{aligned}
    f'(x) &= \frac{(1-x)(-1)-x(x+1)}{\left[x(1-x)\right]^2}\\
    & =\frac{-1+x-(x^2+x)}{\left[x(1-x)\right]^2} \\
    & = \frac{x^2 - 2 x + 1}{[x(1-x)]^2}.
    \end{aligned}$.
*   Setting $f'(x)=0$, we find that the minimum value of the function occurs at $x=\frac{-1\pm\sqrt{3}}{2}$.

### Common Pitfalls
---------------------

#### 1. Inadequate Use of Constraints

When solving optimization problems subject to constraints, it is essential to correctly apply these constraints in the problem-solving process.

*   Misinterpretation or misapplication of constraints can lead to incorrect solutions.

### Quick Summary
------------------

| Concept | Description |
| --- | --- |
| Functions | Relations between inputs and outputs |
| Differentiation | Finding the derivative of a function |
| Min/Max Problems | Solving optimization problems subject to constraints |

Note: In the above, we have covered the basic concepts needed for solving the specific question.