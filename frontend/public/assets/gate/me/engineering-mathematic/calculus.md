**Calculus: Engineering Mathematics**
=====================================

**Introduction**
---------------

Calculus is a branch of mathematics that deals with the study of continuous change, particularly in the context of functions and limits. In engineering mathematics, calculus is used to model real-world problems involving optimization, motion, and rates of change.

**Core Concepts**
-----------------

### 1. Limits

The concept of a limit is fundamental to calculus. It represents the value that a function approaches as the input (or independent variable) gets arbitrarily close to a certain point.

**Definition**: Given a function f(x), the limit of f(x) as x approaches a is denoted by:

$$\lim_{x \to a} f(x) = L$$

where L is the value that f(x) approaches as x gets arbitrarily close to a.

### 2. Differentiation

Differentiation is the process of finding the rate of change of a function with respect to its input. It is denoted by the symbol d/dx and is used to find the derivative of a function:

$$\frac{d}{dx} f(x) = f'(x)$$

### 3. Integration

Integration is the reverse process of differentiation, which involves finding the area under a curve or the accumulation of a quantity.

**Definition**: Given a function f(x), the definite integral of f(x) from a to b is denoted by:

$$\int_{a}^{b} f(x) dx = F(b) - F(a)$$

where F(x) is the antiderivative of f(x).

### 4. Mean Value Theorem (MVT)

The MVT states that if a function f(x) is continuous on the interval [a, b] and differentiable on the open interval (a, b), then there exists a point c in (a, b) such that:

$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

### 5. Simpson's One-Third Rule

Simpson's one-third rule is an approximation method for definite integrals. It states that the integral of a function f(x) can be approximated as:

$$\int_{a}^{b} f(x) dx \approx \frac{h}{3} \left[ (y_0 + y_n) + 4(y_1 + y_2 + ... + y_{n-1}) + 2(y_3 + y_5 + ... + y_{n-2}) \right]$$

where h is the interval size and y_i are the function values at each point.

**Key Formulas/Theorems**
-------------------------

* **Fundamental Theorem of Calculus (FTC)**:
	+ If f(x) is continuous on [a, b], then the definite integral of f(x) from a to b can be evaluated as: $$\int_{a}^{b} f(x) dx = F(b) - F(a)$$
	+ Where F(x) is the antiderivative of f(x)
* **Taylor Series**: A function f(x) can be approximated using its Taylor series expansion around a point x=a:
	+ $$f(x) \approx f(a) + (x-a)f'(a) + \frac{(x-a)^2}{2!}f''(a) + ...$$

**Problem Solving Patterns**
---------------------------

### 1. Finding Limits

* Use algebraic manipulation to simplify the function
* Apply limit properties, such as the sum rule or product rule
* Use L'Hôpital's rule for indeterminate forms (e.g., 0/0)

### 2. Differentiation

* Use the power rule, product rule, and quotient rule for differentiation
* Apply the chain rule for composite functions

### 3. Integration

* Use substitution, integration by parts, or integration by partial fractions to evaluate definite integrals
* Apply the FTC to relate antiderivatives to definite integrals

**Examples with Solutions**
---------------------------

### Example 1: Finding a Limit

Find the limit of (x^2 - 4) / (x - 2) as x approaches 2.

```markdown
\begin{align*}
\lim_{x \to 2} \frac{x^2 - 4}{x - 2} &= \lim_{x \to 2} \frac{(x-2)(x+2)}{x-2}\\
&= \lim_{x \to 2} (x + 2)\\
&= 2 + 2 = 4
\end{align*}
```

### Example 2: Differentiation

Find the derivative of f(x) = x^3 - 6x^2 + 9x.

```markdown
\begin{align*}
f'(x) &= \frac{d}{dx} (x^3 - 6x^2 + 9x)\\
&= \frac{d}{dx} (x^3) - \frac{d}{dx} (6x^2) + \frac{d}{dx} (9x)\\
&= 3x^2 - 12x + 9
\end{align*}
```

**Common Pitfalls**
------------------

* **Incorrect Application of Limit Properties**: Be cautious when applying limit properties, as incorrect application can lead to errors.
* **Misuse of Differentiation Rules**: Make sure to apply differentiation rules correctly and in the correct order.

**Quick Summary**
-----------------

| Concept | Key Point |
| --- | --- |
| Limits | Approaches a value as input gets arbitrarily close |
| Differentiation | Finds rate of change with respect to input |
| Integration | Accumulates quantity or area under curve |
| Mean Value Theorem | Derivative equals average rate of change |
| Simpson's One-Third Rule | Approximates definite integrals using intervals |

Note: This is a comprehensive theory note covering all the concepts tested in the source questions.