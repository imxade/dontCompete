**Mean Value Theorems, Indeterminate Forms, Evaluation of Definite and Improper Integrals**
====================================================================================

### Introduction

Calculus is a vast subject that deals with the study of continuous change. This note focuses on three fundamental concepts in calculus: Mean Value Theorems (MVT), Indeterminate Forms, and evaluation of definite and improper integrals. These topics are crucial for solving various problems in mathematics and science.

### Core Concepts

#### Mean Value Theorem

The **Mean Value Theorem** states that if a function `f(x)` is continuous on the closed interval `[a, b]` and differentiable on the open interval `(a, b)`, then there exists a point `c` in `(a, b)` such that:

$$f'(c) = \frac{f(b) - f(a)}{b-a}$$

This theorem is essential for finding the maximum or minimum value of a function.

#### Indeterminate Forms

An **Indeterminate Form** arises when the limit of a function has an indeterminate form, such as `0/0` or `∞/∞`. To resolve these forms, we can use L'Hôpital's rule:

* If `lim x→a f(x)/g(x)` is in the form `0/0`, then:
$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$
* If `lim x→a f(x)/g(x)` is in the form `∞/∞`, then:
$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

#### Evaluation of Definite Integrals

A **definite integral** is used to find the area under curves. The fundamental theorem of calculus states that differentiation and integration are inverse processes:

* If `F(x)` is an antiderivative of `f(x)`, then:
$$\int_{a}^{b} f(x) dx = F(b) - F(a)$$

#### Evaluation of Improper Integrals

An **improper integral** extends the definition of definite integrals to infinite intervals. For example:

* If `f(x)` is continuous on `[a, ∞)` and:
$$\int_{a}^{\infty} f(x) dx = \lim_{b \to \infty} \int_{a}^{b} f(x) dx$$

### Key Formulas/Theorems

* **Mean Value Theorem**: $f'(c) = \frac{f(b) - f(a)}{b-a}$
* **L'Hôpital's Rule**:
	+ For `0/0` form: $\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$
	+ For `∞/∞` form: $\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$

### Problem Solving Patterns

* When dealing with indeterminate forms, apply L'Hôpital's rule until the limit converges.
* Use substitution or integration by parts to evaluate definite integrals.

### Examples with Solutions

1. **Mean Value Theorem Example**

Let `f(x) = x^2 + 3x - 4` on the interval `[0, 2]`. Find the value of `c` that satisfies the MVT.

Solution:

$$\begin{aligned}
f'(x) &= 2x + 3 \\
f(2) - f(0) &= (2^2 + 3 \cdot 2 - 4) - (0^2 + 3 \cdot 0 - 4) = 8 \\
\frac{f(2) - f(0)}{2-0} &= \frac{8}{2} = 4
\end{aligned}$$

Thus, $f'(c) = 4$, which implies `c` is a solution to the equation:

$2c + 3 = 4$

Solving for `c`, we get:

$c = \frac{1}{2}$

2. **Indeterminate Form Example**

Evaluate $\lim_{x \to 0} \frac{\sin x}{x}$.

Solution:

$$\begin{aligned}
\lim_{x \to 0} \frac{\sin x}{x} &= \lim_{x \to 0} \frac{\cos x}{1} \\
&= \frac{\cos 0}{1} = 1
\end{aligned}$$

### Common Pitfalls

* When applying L'Hôpital's rule, ensure that the resulting limit is not an indeterminate form.
* Be cautious when evaluating limits of functions with multiple discontinuities.

### Quick Summary

* Mean Value Theorem: $f'(c) = \frac{f(b) - f(a)}{b-a}$
* L'Hôpital's Rule:
	+ For `0/0` form: $\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$
	+ For `∞/∞` form: $\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$
* Definite Integrals: $\int_{a}^{b} f(x) dx = F(b) - F(a)$
* Improper Integrals: Extend the definition of definite integrals to infinite intervals.