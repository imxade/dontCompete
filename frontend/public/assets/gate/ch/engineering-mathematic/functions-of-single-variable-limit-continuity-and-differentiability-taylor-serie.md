# Functions of Single Variable: Limit Continuity and Differentiability Taylor Series
====================================================================

## Introduction
The theory of functions of single variable forms a fundamental basis for various mathematical disciplines, including calculus. The concepts of limit, continuity, and differentiability are crucial to understanding these mathematical functions.

## Core Concepts

### Limit
A function f(x) has a limit L as x approaches a if the value of the function gets arbitrarily close to L when x is sufficiently close to a. This can be denoted as:

$$\lim_{x \to a} f(x) = L$$

### Continuity
A function f(x) is continuous at x=a if the following conditions are met:
1. The function is defined at x=a.
2. The limit of the function as x approaches a exists.
3. The limit equals the value of the function at x=a.

This can be represented mathematically as:

$$\lim_{x \to a} f(x) = f(a)$$

### Differentiability
A function f(x) is differentiable at x=a if the derivative of the function exists at that point. The derivative, denoted as f'(a), represents the rate of change of the function with respect to x.

### Taylor Series
The Taylor series expansion of a function f(x) around a point a is given by:

$$f(x) = f(a) + \frac{f'(a)}{1!}(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \cdots$$

## Key Formulas/Theorems

### Taylor Series Expansion
Given the function f(x), its Taylor series expansion around a point x=a is:

$$f(x) = f(a) + \sum_{n=1}^{\infty} \frac{f^{(n)}(a)}{n!}(x - a)^n$$

where $f^{(n)}(a)$ represents the nth derivative of f at point a.

### Differentiation Rules
- The derivative of a constant function is 0.
- The derivative of x^n is nx^(n-1).
- The derivative of a sum/difference/product of functions is given by the corresponding rule for derivatives (e.g., sum rule, product rule).

## Problem Solving Patterns

### Taylor Series Approximation
Given a function and its derivatives at point a, one can use the Taylor series expansion to approximate f(x) near x=a. The accuracy of this approximation increases as more terms are included in the series.

### Limit Continuity Differentiability Analysis
When dealing with functions defined on intervals or having specific domains, analyze continuity and differentiability by considering the limits as x approaches various points within the domain.

## Examples with Solutions

### Example 1: Taylor Series Approximation

Given $f(x) = \cos(x)$, find its Taylor series expansion around $x=0$ up to the fourth term.

Using derivatives of $\cos(x)$:
- $f(0) = \cos(0) = 1$
- $f'(0) = -\sin(0) = 0$
- $f''(0) = -\cos(0) = -1$
- $f'''(0) = \sin(0) = 0$

Thus, the Taylor series expansion up to the fourth term is:

$$\cos(x) \approx 1 - \frac{x^2}{2!} + \frac{x^4}{4!}$$

### Example 2: Continuity and Differentiability Analysis

For $f(x) = x^3$ on the interval $(-1, 1)$:
- Is f(x) continuous at x=0?
- Is f(x) differentiable at x=0?

The function is defined everywhere in the given interval. Since it's a polynomial, all its derivatives exist and are continuous everywhere.

At $x = 0$, $\lim_{x \to 0} x^3 = 0^3 = 0$.
Therefore, f(x) is continuous at x=0 since $\lim_{x \to 0} x^3 = f(0)$.

The derivative of $f(x) = x^3$ is given by $f'(x) = 3x^2$. Thus, $f'(0) = 3(0)^2 = 0$.

Since the limit of the derivative as x approaches 0 exists and equals f'(0), the function is differentiable at x=0.

## Common Pitfalls

- **Misapplication of Taylor Series**: Ensure you are expanding around the correct point, using derivatives correctly, and understanding the convergence of the series.
- **Confusion between Continuity and Differentiability**: Distinguish between functions that are continuous but not differentiable (e.g., |x| at x=0) versus those that are both.

## Quick Summary

* Limit: A value a function approaches as its input gets arbitrarily close to a point.
* Continuity: Function's limit equals the function's value at the point when approaching from either side.
* Differentiability: Derivative exists at a point, indicating how fast and in what direction the function changes there.
* Taylor Series: Approximates a function near a specific point using derivatives and terms of (x-a).

Note: Ensure to practice with sample questions and problems to solidify your understanding.