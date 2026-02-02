**Limits and Series Expansion**
=====================================

**Introduction**
---------------

This topic covers the fundamental concepts of limits and series expansion, which are crucial for mathematical modeling and problem-solving in engineering mathematics. Limits provide a way to study how functions behave near a specific point, while series expansion enables us to approximate functions using infinite sums.

**Core Concepts**
-----------------

### Limit of a Function

The limit of a function f(x) as x approaches a is denoted by lim x→a f(x). It represents the value that f(x) approaches as x gets arbitrarily close to a.

*   **Left-hand limit**: lim x→a- f(x)
*   **Right-hand limit**: lim x→a+ f(x)

If the left-hand and right-hand limits are equal, we say that the function has a **limit** at a. Otherwise, the function may have a **jump discontinuity** or a **removable discontinuity**.

### Types of Limits

*   **One-sided limit**: lim x→a- f(x) = L or lim x→a+ f(x) = L
*   **Two-sided limit**: lim x→a f(x) = L
*   **Infinity**: lim x→a f(x) = ∞ or lim x→a f(x) = -∞

### Series Expansion

A series expansion is an infinite sum of terms that approximates a function. The most common type of series expansion is the **Taylor series**, which represents a function around a point a.

*   **Taylor series**: f(x) ≈ f(a) + (x-a)f'(a) + (x-a)^2f''(a)/2! + ...

### Important Formulas

$$
\lim_{x \to a} f(x) = L \quad \text{if and only if} \quad \forall \epsilon > 0, \exists \delta > 0 \text{ such that } |f(x) - L| < \epsilon \text{ whenever } 0 < |x-a| < \delta
$$

$$
\sum_{n=0}^{\infty} a_n = \lim_{N \to \infty} \sum_{n=0}^{N} a_n
$$

### Problem Solving Patterns

*   **Use the definition of limit**: If you're unsure about a limit, try using the definition to prove it.
*   **Recognize common limits**: Familiarize yourself with common limits like lim x→∞ f(x) = 0 or lim x→a f(x) = L.
*   **Apply series expansion formulas**: Use Taylor series or other series expansions to simplify functions.

**Examples with Solutions**

### Example 1: Evaluating a Limit

Find the limit of (x^2 - 4) / (x - 2) as x approaches 2.

Solution:

$$
\lim_{x \to 2} \frac{x^2-4}{x-2} = \lim_{x \to 2} \frac{(x+2)(x-2)}{x-2}
$$

$$
= \lim_{x \to 2} (x + 2)
$$

$$
= 4
$$

### Example 2: Series Expansion

Find the Taylor series expansion of e^x around x = 0.

Solution:

$$
e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}
$$

**Common Pitfalls**

*   **Not using the definition of limit**: Make sure to use the definition of limit when evaluating a problem.
*   **Ignoring common limits**: Familiarize yourself with common limits and apply them when possible.
*   **Forgetting series expansion formulas**: Use Taylor series or other series expansions to simplify functions.

**Quick Summary**

*   Limits represent how functions behave near a specific point.
*   Series expansion approximates functions using infinite sums.
*   Recognize common limits and use series expansion formulas to simplify functions.

Note: The above content is generated based on the provided source questions and is intended to be a comprehensive study note for GATE CS exam. However, please verify the accuracy of the content as it may not cover all possible topics related to "limits and series expansion" in engineering mathematics.