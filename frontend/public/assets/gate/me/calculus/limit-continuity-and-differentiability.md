# Limit Continuity and Differentiability
## Introduction
In calculus, the concepts of limit continuity and differentiability are crucial for understanding how functions behave as their input values approach specific points. The limit of a function represents the value that the function approaches as its input gets arbitrarily close to a certain point. A function is said to be continuous at a point if it has no jumps or breaks at that point, meaning that its graph can be drawn without lifting the pencil from the paper. Differentiability refers to the ability of a function to have a derivative at a point, which measures the rate of change of the function at that point.

## Core Concepts
### Limits
The limit of a function f(x) as x approaches c is denoted by lim x→c f(x). If this limit exists and is equal to L, then we say that:

$$\lim_{x \to c} f(x) = L$$

If the limit does not exist or is infinite, we write:

$$\lim_{x \to c} f(x) = \pm \infty$$

### Continuity
A function f(x) is said to be continuous at a point c if the following three conditions are satisfied:

1. The function is defined at c (f(c) exists).
2. The limit of the function as x approaches c exists.
3. The limit of the function as x approaches c is equal to the value of the function at c (lim x→c f(x) = f(c)).

If a function is continuous at a point, we can draw its graph without lifting our pencil from the paper.

### Differentiability
A function f(x) is said to be differentiable at a point c if the derivative of the function exists at that point. The derivative of a function f(x) at a point c is denoted by f'(c) and represents the rate of change of the function at that point.

## Key Formulas/Theorems

$$\lim_{x \to a} f(x) = f(a)$$ (Theorem: Limits preserve continuity)

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$ (Definition of derivative)

## Problem Solving Patterns
When dealing with limit, continuity, and differentiability problems, follow these steps:

1. Check if the function is defined at the point in question.
2. Evaluate the limit of the function as x approaches the point.
3. Use the definition of derivative to find the derivative of the function.

## Examples with Solutions

### Example 1:
Find the value of $\alpha$ and the corresponding limit $p$ for which:

$$\lim_{x \to \pi} \frac{2 \sin x}{ax^2 + bx + c} = p$$

where $a, b,$ and $c$ are constants.

```mermaid
graph LR
A[Find limit] --> B[Evaluate at pi]
B --> C[Compare with given options]
```

### Solution:
To find the value of $\alpha$ and the corresponding limit $p$, we first evaluate the limit at $x = \pi$. We get:

$$\lim_{x \to \pi} \frac{2 \sin x}{ax^2 + bx + c} = \frac{0}{a\pi^2 + b\pi + c}$$

Since $\sin(\pi) = 0$, the numerator becomes zero. For the limit to exist, the denominator must also be zero.

Solving for $x$ in the equation:

$$ax^2 + bx + c = 0$$

we get:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

For the limit to exist, we must have:

$$\frac{-b + \sqrt{b^2 - 4ac}}{2a} = \pi$$

Comparing with the given options, we find that $\alpha = 3$ and $p = \pi$.

## Common Pitfalls
When dealing with limit, continuity, and differentiability problems, students often make the following mistakes:

* Forgetting to check if the function is defined at the point in question.
* Not evaluating the limit correctly.
* Not using the definition of derivative when finding derivatives.

## Quick Summary

* Limits preserve continuity (Theorem: Limits preserve continuity)
* The derivative of a function f(x) at a point c is denoted by f'(c) and represents the rate of change of the function at that point.
* To solve limit, continuity, and differentiability problems, follow the steps:
	1. Check if the function is defined at the point in question.
	2. Evaluate the limit of the function as x approaches the point.
	3. Use the definition of derivative to find the derivative of the function.

By following these concepts, formulas, and problem-solving patterns, students can master the topics of limits, continuity, and differentiability, and excel on the GATE CS exam.