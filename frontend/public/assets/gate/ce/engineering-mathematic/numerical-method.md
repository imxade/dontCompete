**Numerical Methods**
=====================

**Introduction**
---------------

Numerical methods are techniques used to solve mathematical problems approximately, often due to the complexity or inability to find an exact solution. This topic covers essential numerical methods for engineering mathematics, specifically in the context of GATE CS exam questions.

**Core Concepts**
-----------------

### Numerical Integration

Numerical integration approximates a definite integral by breaking it down into smaller subintervals and summing the areas of these intervals.

#### Trapezoidal Rule

The trapezoidal rule approximates an integral by treating each interval as a trapezoid and calculating the area using the formula:

$$\frac{h}{2} \left( f(x_0) + 2f(x_1) + 2f(x_2) + ... + 2f(x_{n-1}) + f(x_n) \right)$$

where $h$ is the width of each subinterval, and $f(x_i)$ are the function values at each point.

#### Simpson's Rule

Simpson's rule approximates an integral by dividing the area into parabolic segments. The formula for Simpson's rule is:

$$\frac{h}{3} \left( f(x_0) + 4f(x_1) + 2f(x_2) + ... + 4f(x_{n-1}) + f(x_n) \right)$$

when $n$ is even.

### Interpolation

Interpolation estimates a function value at an unknown point using known data points. The Newton's forward difference formula for second-order interpolation is:

$$f(x + h) = f(x_0) + hf'(x_0) + \frac{h^2}{2} f''(x_0)$$

where $f(x_i)$ are the function values at each point, and $f'$ and $f''$ are the first and second derivatives of the function.

### Central Divided Difference Formula

The central divided difference formula for a given interval is:

$$f''(x_i + h/2) = \frac{ f(x_i + h) - 2f(x_i) + f(x_i - h)}{h^2}$$

**Key Formulas/Theorems**
------------------------

### Trapezoidal Rule Formula

$E = \frac{h}{2} \left( f(x_0) + 2f(x_1) + 2f(x_2) + ... + 2f(x_{n-1}) + f(x_n) \right)$

### Simpson's Rule Formula

$E = \frac{h}{3} \left( f(x_0) + 4f(x_1) + 2f(x_2) + ... + 4f(x_{n-1}) + f(x_n) \right)$

when $n$ is even.

### Newton's Forward Difference Formula for Second-Order Interpolation

$f(x + h) = f(x_0) + hf'(x_0) + \frac{h^2}{2} f''(x_0)$

**Problem Solving Patterns**
---------------------------

*   Use the trapezoidal rule or Simpson's rule to approximate definite integrals.
*   Apply Newton's forward difference formula for second-order interpolation.

**Examples with Solutions**
-------------------------

### Example 1: Trapezoidal Rule

Find the value of $\int_0^2 e^x dx$ using the trapezoidal rule with four equal subintervals.

Solution:

| $x_i$ | $f(x_i)$ |
| --- | --- |
| 0   | $e^0 = 1$    |
| 1   | $e^1 \approx 2.71828$     |
| 2   | $e^2 \approx 7.38905$       |

The width of each subinterval is $h = (2 - 0)/4 = 0.5$. Applying the trapezoidal rule:

$$\frac{0.5}{2} \left( e^0 + 2e^1 + 2e^2 \right) \approx 3.13589$$

### Example 2: Second-Order Interpolation using Newton's Forward Difference Formula

Estimate the value of $f(1.5)$ given the following data points:

| $x_i$ | $f(x_i)$ |
| --- | --- |
| 0   | 0    |
| 1   | 0.3010     |
| 2   | 0.4771       |

Solution:

First, calculate the first and second derivatives at $x_0 = 0$. 

$$f'(0) \approx f(x_1) - f(x_0) = 0.3010 - 0 = 0.3010$$

$$f''(0) \approx \frac{f'(x_1) - f'(x_0)}{h} = \frac{0.3010}{1 - 0} = 0.3010$$

Now, apply Newton's forward difference formula for second-order interpolation:

$f(x + h) = f(x_0) + hf'(x_0) + \frac{h^2}{2} f''(x_0)$

For $f(1.5)$, we have:

$h = 1 - 0 = 1$

$$\begin{aligned} 
f(1.5) &amp;= f(0) + h \cdot f'(0) + \frac{h^2}{2} \cdot f''(0) \\
&amp;= 0 + 1 \cdot 0.3010 + \frac{1^2}{2} \cdot 0.3010\\
&amp;\approx 0.15 + 0.1505 \\
&amp;\approx 0.30 
\end{aligned}
$$

The second-order interpolation estimate of $f(1.5)$ is approximately 0.3.

### Example 3: Central Divided Difference Formula

Find the expression for the second derivative using the central divided difference formula with a step length $h$:

$$f''(x_i + h/2) = \frac{ f(x_i + h) - 2f(x_i) + f(x_i - h)}{h^2}$$

The correct answer is (A):

$\boxed{\frac{1}{12} \left[ \begin{array}{c}
\frac{ f(x_{i+1}) - 2f(x_i) + f(x_{i-1}) }{h^2}\\
\end{array} \right]}$

**Common Pitfalls**
-----------------

*   Ensure the intervals are equally spaced when using the trapezoidal rule or Simpson's rule.
*   Calculate derivatives accurately when applying Newton's forward difference formula.

**Quick Summary**
----------------

| Topic | Key Points |
| --- | --- |
| Numerical Integration | Trapezoidal Rule, Simpson's Rule |
| Interpolation | Newton's Forward Difference Formula for Second-Order Interpolation |
| Central Divided Difference Formula | Expression for the second derivative |

This comprehensive theory note covers essential numerical methods in engineering mathematics. By following these concepts and formulas, students can confidently solve GATE CS exam questions related to this topic.