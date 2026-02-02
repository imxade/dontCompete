**Calculus: Theory Notes**

**Introduction**
Calculus is a branch of mathematics that deals with the study of continuous change, particularly in the context of functions and limits. It has widespread applications in physics, engineering, economics, and other fields. In this theory note, we will cover the essential concepts, formulas, and problem-solving strategies for tackling calculus-related questions on the GATE exam.

**Core Concepts**

* **Limits**: The concept of a limit is fundamental to calculus. A limit represents the value that a function approaches as the input (or independent variable) gets arbitrarily close to a certain point.
* **Derivatives**: Derivatives measure the rate of change of a function with respect to its input. They are used to study the behavior of functions, including maxima and minima.
* **Integrals**: Integrals represent the accumulation of a quantity over an interval or region.

**Key Formulas/Theorems**

* **Fundamental Theorem of Calculus (FTC)**: $\int_{a}^{b} f(x) dx = F(b) - F(a)$, where $F$ is the antiderivative of $f$.
* **Power Rule**: If $f(x) = x^n$, then $f'(x) = nx^{n-1}$.
* **Sum Rule**: If $f(x) = g(x) + h(x)$, then $f'(x) = g'(x) + h'(x)$.

**Problem Solving Patterns**

* **Integration by Substitution**: This technique involves substituting a new variable into the integral to simplify it. For example:
$\int \frac{1}{x^2} dx = \int x^{-2} dx$
* **Integration by Parts**: This technique involves differentiating one function and integrating the other.

**Examples with Solutions**

### Example 1: Evaluating a Definite Integral

Evaluate $\int_{0}^{4} (x+1) dx$

**Solution**

$\int_{0}^{4} (x+1) dx = \left[ \frac{x^2}{2} + x \right]_0^4$
$= \left( \frac{4^2}{2} + 4 \right) - \left( \frac{0^2}{2} + 0 \right)$
$= \frac{16}{2} + 4 = 8 + 4 = 12$

### Example 2: Finding the Derivative of a Function

Find the derivative of $f(x) = x^3 + 2x - 1$

**Solution**

$f'(x) = \frac{d}{dx}(x^3 + 2x - 1)$
$= 3x^2 + 2$ (using the power rule)

### Example 3: Evaluating a Double Integral

Evaluate $\int_{D} xy dxdy$, where $D$ is the triangular region shown in the diagram.

**Solution**

$\int_{D} xy dxdy = \int_0^4 \left( \int_y^4 x dx \right) dy$
$= \int_0^4 \left[ \frac{x^2}{2} \right]_y^4 dy$
$= \int_0^4 \left( \frac{16}{2} - \frac{y^2}{2} \right) dy$
$= 8 \cdot y \Big|_0^4 = 32$

**Common Pitfalls**

* Not considering the limits of integration.
* Failing to simplify the integral before solving it.
* Confusing the order of operations.

**Quick Summary**

* Limits: fundamental concept in calculus
* Derivatives: measure rate of change
* Integrals: accumulation of quantity over interval or region
* Key formulas:
	+ FTC
	+ Power rule
	+ Sum rule
* Problem-solving strategies:
	+ Integration by substitution
	+ Integration by parts

Note: The solution to the source question (Q1) is based on evaluating the double integral over the triangular region.