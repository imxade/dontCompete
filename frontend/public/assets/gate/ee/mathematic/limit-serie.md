**Limit Series**
================

### Introduction

The Taylor series expansion of a function $f(z)$ about a point $z_0$ is a powerful tool for approximating the values of the function. In this note, we will focus on the limit series, which involves finding the coefficients of the Taylor series expansion.

### Core Concepts

**Definition**: The Taylor series expansion of a function $f(z)$ about the origin $z=0$ is given by:

$$f(z) = \sum_{n=0}^{\infty} c_n z^n,$$

where $c_n$ are the coefficients of the expansion.

The limit series, also known as the Laurent series, is a generalization of the Taylor series expansion. It is used to expand a function about any point $z_0$, not just the origin.

**Definition**: The Laurent series expansion of a function $f(z)$ about a point $z_0$ is given by:

$$f(z) = \sum_{n=-\infty}^{\infty} c_n (z-z_0)^n.$$

### Key Formulas/Theorems

#### Binomial Expansion

For any real number $a$, the binomial expansion is given by:

$$(1+x)^a = 1 + ax + \frac{a(a-1)}{2!}x^2 + \cdots$$

#### Taylor Series Expansion

The Taylor series expansion of a function $f(z)$ about the origin $z=0$ is given by:

$$f(z) = f(0) + zf'(0) + \frac{z^2}{2!}f''(0) + \cdots$$

### Problem Solving Patterns

* To find the Taylor series expansion of a function, use the formula: $$c_n = \frac{1}{n!} \left[ z^n f(z) \right]'_{z=0}$$
* Use the binomial expansion to expand $(1+z)^a$.
* For complex functions, use the Laurent series expansion.

### Examples with Solutions

**Example 1**

Find the Taylor series expansion of $f(z) = e^z$ about the origin $z=0$.

Solution:

Using the formula for the Taylor series expansion, we get:

$$c_n = \frac{1}{n!} [z^n f(z)]'_{z=0} = \frac{1}{n!} [z^n e^z]'_{z=0} = \frac{1}{n!}.$$

Therefore, the Taylor series expansion of $f(z) = e^z$ about the origin is:

$$e^z = 1 + z + \frac{z^2}{2!} + \cdots$$

**Example 2**

Find the Laurent series expansion of $f(z) = \cos z$ about the point $z_0 = i$.

Solution:

Using the binomial expansion, we can expand $(1+z)^a$ as follows:

$$(1+z)^a = 1 + az + \frac{a(a-1)}{2!}z^2 + \cdots$$

Substituting $a = -\frac{1}{2}$ and using the fact that $\cos z = (e^{iz}+e^{-iz})/2$, we get:

$$f(z) = \cos z = 1 - \frac{(1+z)^{-1/2}}{2} - \frac{(1-z)^{-1/2}}{2}.$$

Therefore, the Laurent series expansion of $f(z) = \cos z$ about the point $z_0 = i$ is:

$$\cos z = 1 + z^{-1} + \cdots$$

### Common Pitfalls

* Don't forget to use the binomial expansion for $(1+z)^a$.
* Be careful when substituting values into the Taylor series expansion formula.

### Quick Summary

* **Taylor Series Expansion**: $f(z) = \sum_{n=0}^{\infty} c_n z^n$
* **Laurent Series Expansion**: $f(z) = \sum_{n=-\infty}^{\infty} c_n (z-z_0)^n$
* **Binomial Expansion**: $(1+x)^a = 1 + ax + \frac{a(a-1)}{2!}x^2 + \cdots$

### Mermaid Diagram

```mermaid
graph LR
A[Taylor Series] --> B[Laurent Series]
B --> C[Binomial Expansion]
```

Note: This is a basic mermaid diagram showing the relationships between the Taylor series, Laurent series, and binomial expansion.