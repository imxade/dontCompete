**Differential Equation Theory Note**
=====================================

**Introduction**
---------------

A differential equation (DE) is an equation that describes a relationship between a function and its derivatives. In this note, we'll focus on linear time-invariant (LTI) systems and their transfer functions.

**Core Concepts**
-----------------

* **Linear Time-Invariant Systems**: A system where the output is directly proportional to the input and the system's behavior does not change over time.
* **Transfer Function**: The ratio of the Laplace transform of the output to the Laplace transform of the input.
* **Poles**: Roots of the denominator of the transfer function.

**Key Formulas/Theorems**
-------------------------

### Laplace Transform

The Laplace transform is a powerful tool for solving differential equations. Given a function $f(t)$, the Laplace transform is defined as:

$$F(s) = \int_{0}^{\infty} f(t)e^{-st} dt$$

where $s$ is a complex number.

### Transfer Function

The transfer function of an LTI system is given by:

$$H(s) = \frac{Y(s)}{R(s)}$$

where $Y(s)$ and $R(s)$ are the Laplace transforms of the output and input, respectively.

### Poles

Poles are the roots of the denominator of the transfer function. They can be real or complex.

**Problem Solving Patterns**
---------------------------

1.  **Solve for Transfer Function**: Given a differential equation, find its transfer function using the Laplace transform.
2.  **Find Poles**: Identify the poles of the system by finding the roots of the denominator of the transfer function.
3.  **Analyze System Behavior**: Use the poles to determine the stability and behavior of the system.

**Examples with Solutions**
---------------------------

### Example 1: Differential Equation

Given the differential equation:

$$\frac{d^2y}{dt^2} + 4\frac{dy}{dt} + 6y = r(t)$$

Find the transfer function and poles of the system.

#### Solution

Taking the Laplace transform of both sides, we get:

$$(s^2 + 4s + 6)Y(s) = R(s)$$

Therefore, the transfer function is:

$$H(s) = \frac{1}{s^2 + 4s + 6}$$

The poles are found by solving for $s$ in the denominator:

$$s^2 + 4s + 6 = 0$$

Using the quadratic formula, we get:

$$s = -2 \pm j\sqrt{2}$$

### Example 2: Transfer Function

Given a transfer function:

$$H(s) = \frac{1}{s + 2}$$

Find the poles of the system.

#### Solution

The poles are found by solving for $s$ in the denominator:

$$s + 2 = 0$$

Therefore, the pole is $s = -2$.

**Common Pitfalls**
------------------

*   Forgetting to take the Laplace transform of both sides.
*   Not identifying the correct poles of the system.

**Quick Summary**
-----------------

*   Linear Time-Invariant Systems
*   Transfer Function: ratio of output to input in the Laplace domain
*   Poles: roots of the denominator of the transfer function

[Mermaid diagram]
```mermaid
graph LR
    A[LTI System] --> B[Differential Equation]
    B --> C[Laplace Transform]
    C --> D[Transfer Function]
    D --> E[Poles]
```

This note covers the key concepts and problem-solving patterns for differential equations, including linear time-invariant systems, transfer functions, and poles. The examples provided demonstrate how to apply these concepts to solve problems.