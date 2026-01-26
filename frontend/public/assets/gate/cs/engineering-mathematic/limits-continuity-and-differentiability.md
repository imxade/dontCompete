**Limits, Continuity, and Differentiability**
===========================================

### Introduction

This topic deals with fundamental concepts in calculus: limits, continuity, and differentiability. These ideas are crucial for understanding how functions behave, especially when working with mathematical models in engineering and computer science.

### Core Concepts

#### Limits

The limit of a function `f(x)` as `x` approaches a value `a`, denoted by `\lim_{x\to a} f(x)`, represents the behavior of the function near that point. Intuitively, it's the value the function is approaching as `x` gets arbitrarily close to `a`. If the limit exists and equals some value `L`, we say:

```math
\lim_{x\to a} f(x) = L
```

#### Continuity

A function `f(x)` is continuous at a point `a` if its left-hand limit, right-hand limit, and the function value at that point are all equal:

```math
\lim_{x\to a^-} f(x) = \lim_{x\to a^+} f(x) = f(a)
```

A function is continuous on an interval `I` if it's continuous at every point in `I`.

#### Differentiability

A function `f(x)` is differentiable at a point `a` if its derivative exists at that point:

```math
f'(a) = \lim_{h\to 0} \frac{f(a+h) - f(a)}{h}
```

### Key Formulas/Theorems

* **Continuity and Differentiability Theorem**: A function is differentiable at a point `a` if and only if it's continuous at that point.

```math
f(x) = \begin{cases} x^2 & \text{if } x\neq 0 \\ 0 & \text{if } x=0 \end{cases}
```

is not differentiable at `x=0`.

### Problem Solving Patterns

* **Direct Substitution Method**: If a function is continuous and differentiable, we can directly substitute the limit value to find the solution.

Given `\lim_{x\to 2} f(x) = L`, if `f(x)` is continuous at `x=2`:

```math
L = f(2)
```

### Examples with Solutions

**Example 1:** Suppose `f(x)` is a differentiable function on the interval `[0,3]`. If `\lim_{x\to 1} f'(x) = -2`, what is `\lim_{h\to 0} \frac{f(1+h) - f(1)}{h}`?

**Solution:**

Using the definition of derivative:

```math
\lim_{h\to 0} \frac{f(1+h) - f(1)}{h} = \lim_{h\to 0} \frac{f'(1)h + o(h)}{h}
```

Since `o(h)` is a higher-order term, it vanishes as `h` approaches 0.

Therefore:

```math
\lim_{h\to 0} \frac{f(1+h) - f(1)}{h} = f'(1)
```

Given `\lim_{x\to 2} f(x) = L`, if `f(x)` is continuous at `x=2`:

```math
L = f(2)
```

### Common Pitfalls

* **Assuming a function is differentiable without checking**: Always verify the conditions for differentiability.
* **Ignoring higher-order terms in limit calculations**: Pay attention to these when evaluating limits.

### Quick Summary

* Limits, continuity, and differentiability are fundamental concepts in calculus.
* Use direct substitution and derivative definitions to solve problems.
* Verify conditions for continuity and differentiability before applying formulas.