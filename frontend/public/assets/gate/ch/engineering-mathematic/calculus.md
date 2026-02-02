**Calculus Theory Note**
=======================

### Introduction
----------------

Calculus is a branch of mathematics that deals with the study of continuous change, particularly in the context of functions and limits. It has two main branches: Differential Calculus and Integral Calculus.

### Core Concepts
-----------------

#### Limits
Limits are used to define the behavior of functions as they approach a particular point. A function $f(x)$ is said to have a limit $L$ at $x=a$, denoted by $\lim_{x\to a} f(x) = L$, if for every positive real number $\epsilon$, there exists a positive real number $\delta$ such that for all $x$, $0 < |x-a| < \delta$ implies $|f(x)-L| < \epsilon$.

#### Derivatives
Derivatives measure the rate of change of a function with respect to its input. Given a function $f(x)$, the derivative of $f$ at $x=a$, denoted by $f'(a)$, is defined as:

$$f'(a) = \lim_{h\to 0} \frac{f(a+h)-f(a)}{h}$$

#### Taylor Series
Taylor series are used to approximate a function around a given point. The Taylor series of a function $f(x)$ centered at $x=a$ is:

$$f(x) = f(a) + (x-a)f'(a) + \frac{(x-a)^2}{2!}f''(a) + ...$$

### Key Formulas/Theorems
---------------------------

#### Taylor Series Expansion around $x=0$
Given a function $f(x)$, the Taylor series expansion of $f$ around $x=0$ is:

$$f(x) = f(0) + xf'(0) + \frac{x^2}{2!}f''(0) + ...$$

#### Derivative of Sine and Cosine
The derivatives of sine and cosine functions are:

$$\frac{d}{dx}\sin x = \cos x$$
$$\frac{d}{dx}\cos x = -\sin x$$

### Problem Solving Patterns
-----------------------------

*   To find the first non-zero term in the Taylor series expansion, we need to find the lowest power of $x$ that appears in the series.
*   We can use the formula for the Taylor series expansion around $x=0$ to solve problems involving Taylor series.

### Examples with Solutions
---------------------------

**Example 1:**

Find the first non-zero term in the Taylor series expansion of $(1-x)-e^{-x}$ about $x=0$.

Solution:

Using the formula for the Taylor series expansion around $x=0$, we have:

$$f(x) = f(0) + xf'(0) + \frac{x^2}{2!}f''(0) + ...$$

We need to find the first non-zero term, so let's start by finding the derivatives of $f(x)$.

$$f(x) = (1-x)-e^{-x}$$
$$f'(x) = -1+e^{-x}$$
$$f''(x) = e^{-x}$$

Now we can evaluate the derivatives at $x=0$:

$$f(0) = 1-1 = 0$$
$$f'(0) = -1+1 = 0$$
$$f''(0) = e^{0} = 1$$

Substituting these values into the Taylor series expansion, we get:

$$f(x) = 0 + x\cdot 0 + \frac{x^2}{2!}\cdot 1 + ...$$

The first non-zero term is $\frac{x^2}{2}$.

**Quick Summary**
-----------------

*   Limits are used to define the behavior of functions as they approach a particular point.
*   Derivatives measure the rate of change of a function with respect to its input.
*   Taylor series are used to approximate a function around a given point.
*   The first non-zero term in the Taylor series expansion can be found by evaluating the derivatives at $x=0$.

### Common Pitfalls
-------------------

*   Students often forget to evaluate the derivatives at $x=0$ when finding the Taylor series expansion.
*   They may also confuse the formula for the Taylor series expansion with other formulas.