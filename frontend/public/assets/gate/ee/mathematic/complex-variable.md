**Complex Variables**
=====================

**Introduction**
---------------

In this note, we will cover the fundamental concepts of complex variables, focusing on the principles and techniques required to tackle problems related to limit series expansions. Complex variables play a crucial role in various fields, including physics, engineering, and mathematics.

**Core Concepts**
-----------------

### What are Complex Variables?

A complex variable is an extension of real variables that can be expressed as $z = x + iy$, where $x$ and $y$ are real numbers and $i$ is the imaginary unit. The set of all complex numbers is denoted by $\mathbb{C}$.

### Limits and Continuity

The limit of a complex function $f(z)$ as $z \to z_0$ is defined similarly to the real case:

$$\lim_{z \to z_0} f(z) = L$$

A complex function is continuous at a point $z_0$ if the limit exists and equals the value of the function at that point.

### Differentiation

The derivative of a complex function $f(z)$ with respect to $z$ is defined as:

$$\frac{df}{dz} = \lim_{\Delta z \to 0} \frac{f(z + \Delta z) - f(z)}{\Delta z}$$

**Key Formulas/Theorems**
-------------------------

### Taylor Series Expansion

The Taylor series expansion of a complex function $f(z)$ about the origin is given by:

$$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} z^n$$

where $f^{(n)}(0)$ denotes the $n$-th derivative of $f(z)$ evaluated at $z=0$.

### Cauchy-Riemann Equations

For a complex function $f(z) = u(x,y) + iv(x,y)$, the Cauchy-Riemann equations state that:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

**Problem Solving Patterns**
---------------------------

### Evaluating Coefficients in Taylor Series Expansion

When evaluating the coefficient of $z^n$ in the Taylor series expansion, we can use the following approach:

1.  Find the $n$-th derivative of the function.
2.  Evaluate the $n$-th derivative at the origin.

**Examples with Solutions**
---------------------------

### Example: Evaluating Coefficient of $z^5$

Consider the function $f(z) = \cos z$. To evaluate the coefficient of $z^5$, we need to find the 5-th derivative of $\cos z$ and evaluate it at the origin.

$$\frac{d^5}{dz^5} (\cos z) = -\cos z$$

Evaluating this at $z=0$, we get:

$$-\cos (0) = -1$$

Hence, the coefficient of $z^5$ is $-1$.

### Example: Evaluating Coefficient of $z^2$

Consider the function $f(z) = e^z$. To evaluate the coefficient of $z^2$, we need to find the 2-nd derivative of $e^z$ and evaluate it at the origin.

$$\frac{d^2}{dz^2} (e^z) = e^z$$

Evaluating this at $z=0$, we get:

$$e^0 = 1$$

Hence, the coefficient of $z^2$ is $1$.

**Common Pitfalls**
------------------

*   Failing to use the correct formula for the Taylor series expansion.
*   Not evaluating derivatives correctly.
*   Confusing real and imaginary parts in complex functions.

**Quick Summary**
-----------------

| Concept | Brief Description |
| --- | --- |
| Complex variables | Extension of real variables, $z = x + iy$ |
| Limits and continuity | Defined similarly to the real case |
| Differentiation | Defined as a limit |
| Taylor series expansion | Formula for expanding complex functions about the origin |
| Cauchy-Riemann equations | Equations relating partial derivatives in complex functions |

This comprehensive note should equip you with the knowledge required to tackle problems related to limit series expansions and complex variables.