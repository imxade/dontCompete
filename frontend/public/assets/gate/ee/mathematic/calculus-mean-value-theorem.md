**Calculus Mean Value Theorem**
================================

### Introduction

The Calculus Mean Value Theorem (MVT) is a fundamental concept in calculus that establishes a relationship between the average rate of change and the instantaneous rate of change of a function. It has numerous applications in various fields, including physics, engineering, economics, and more.

### Core Concepts

#### Definition

Let $f(x)$ be a continuous function on the closed interval $[a, b]$. Then, there exists a point $c$ in $(a, b)$ such that:

$$\frac{f(b) - f(a)}{b - a} = f'(c)$$

This is known as Rolle's Theorem.

#### Mean Value Theorem

Let $f(x)$ be a function that satisfies the following conditions:

*   Continuous on the closed interval $[a, b]$
*   Differentiable on the open interval $(a, b)$
*   $f(a) = f(b)$

Then, there exists a point $c$ in $(a, b)$ such that:

$$\frac{f'(c)}{b - a} = \frac{f(b) - f(a)}{b - a}$$

#### Geometric Interpretation

The MVT states that if a function is continuous on a closed interval and differentiable on the open interval, then there exists a point where the instantaneous rate of change equals the average rate of change.

### Key Formulas/Theorems

*   Rolle's Theorem: If $f(x)$ is continuous on $[a, b]$ and differentiable on $(a, b)$ with $f(a) = f(b)$, then there exists a point $c$ in $(a, b)$ such that $f'(c) = 0$
*   Mean Value Theorem: If $f(x)$ is continuous on $[a, b]$ and differentiable on $(a, b)$ with $f(a) = f(b)$, then there exists a point $c$ in $(a, b)$ such that $\frac{f'(c)}{b - a} = \frac{f(b) - f(a)}{b - a}$

### Problem Solving Patterns

1.  **Identify the conditions**: Check if the function is continuous on the closed interval and differentiable on the open interval.
2.  **Apply Rolle's Theorem or Mean Value Theorem**: Use the appropriate theorem to establish the existence of the point $c$ where the instantaneous rate of change equals the average rate of change.

### Examples with Solutions

**Example 1**

Find a point $c$ in $(0, 3)$ such that $\frac{f'(c)}{3 - 0} = \frac{f(3) - f(0)}{3 - 0}$ for the function $f(x) = x^2 + 1$

**Solution**

Since $f(x)$ is continuous on $[0, 3]$ and differentiable on $(0, 3)$ with $f(0) = f(3) = 4$, we can apply the Mean Value Theorem:

$$\frac{f'(c)}{3 - 0} = \frac{f(3) - f(0)}{3 - 0}$$

Since $\frac{d}{dx}(x^2 + 1) = 2x$,

$$f'(c) = 6$$

Therefore, the point $c$ is $\boxed{3/2}$.

**Example 2**

Show that if $f(x)$ is continuous on $[a, b]$ and differentiable on $(a, b)$ with $f(a) = f(b)$, then there exists a point $c$ in $(a, b)$ such that $f'(c) = \frac{f(b) - f(a)}{b - a}$.

**Solution**

This is Rolle's Theorem. Let $g(x) = f(x) - (f(b) - f(a))/(b-a)(x-b)$. Then $g(a) = g(b)$, and by Rolle's Theorem, there exists a point $c$ in $(a, b)$ such that $g'(c) = 0$, which implies $f'(c) = \frac{f(b) - f(a)}{b - a}$.

### Common Pitfalls

*   Failing to check if the function is continuous on the closed interval and differentiable on the open interval.
*   Not applying the correct theorem (Rolle's Theorem or Mean Value Theorem).

### Quick Summary

*   Rolle's Theorem: If $f(x)$ is continuous on $[a, b]$ and differentiable on $(a, b)$ with $f(a) = f(b)$, then there exists a point $c$ in $(a, b)$ such that $f'(c) = 0$
*   Mean Value Theorem: If $f(x)$ is continuous on $[a, b]$ and differentiable on $(a, b)$ with $f(a) = f(b)$, then there exists a point $c$ in $(a, b)$ such that $\frac{f'(c)}{b - a} = \frac{f(b) - f(a)}{b - a}$