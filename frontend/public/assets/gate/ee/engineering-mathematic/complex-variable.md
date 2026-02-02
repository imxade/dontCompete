**Complex Variables**
=====================

### Introduction

Complex variables are an essential tool in mathematics and engineering for solving problems involving frequency, resonance, and oscillations. The study of complex variables allows us to extend our understanding of functions from real numbers to complex numbers, which enables us to model a wide range of phenomena.

### Core Concepts

A **complex variable** is a mathematical expression that can take on complex values. It is denoted by the letter `z` and can be expressed as:

`z = x + jy`

where `x` and `y` are real numbers, and `j` is the imaginary unit satisfying `j^2 = -1`.

A **complex function** is a mathematical expression that takes complex variables as input and produces complex values as output. It can be expressed as:

`f(z) = u(x,y) + jv(x,y)`

where `u` and `v` are real-valued functions of the real variables `x` and `y`.

A **complex function is said to be analytic** if it satisfies the Cauchy-Riemann equations, which are a set of partial differential equations that relate the partial derivatives of the real and imaginary parts of the function:

```latex
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}
```

```latex
\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
```

### Key Formulas/Theorems

* Cauchy-Riemann Equations:

  ```latex
  \frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}
```

```latex
\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
```

* Analyticity of a complex function implies that:

  ```latex
  f(z) = \int \frac{f(\zeta)}{(\zeta-z)^n} d\zeta + C
```

where `C` is the constant of integration.

### Problem Solving Patterns

When solving problems involving complex variables, follow these steps:

1. Identify the type of problem: Is it related to analyticity, contour integration, or partial differential equations?
2. Express the complex function in terms of its real and imaginary parts.
3. Check if the Cauchy-Riemann equations are satisfied.
4. Use the formula for the integral of a complex function over a contour.

### Examples with Solutions

**Example 1: Analyticity**

Determine if the following complex functions are analytic:

```latex
f(z) = e^z
```

```latex
g(z) = \frac{e^z}{z}
```

* For `f(z)`:

We can write `f(z)` as:

```latex
f(z) = \cos z + j\sin z
```

The real and imaginary parts are:

```latex
u(x,y) = \cos x - y
```

```latex
v(x,y) = \sin x + y
```

Taking partial derivatives, we get:

```latex
\frac{\partial u}{\partial x} = -\sin x - y = \frac{\partial v}{\partial y}
```

```latex
\frac{\partial u}{\partial y} = -1 = -\frac{\partial v}{\partial x}
```

Since the Cauchy-Riemann equations are satisfied, `f(z)` is analytic.

* For `g(z)`:

We can write `g(z)` as:

```latex
g(z) = \cos z + j\sin z
```

The real and imaginary parts are:

```latex
u(x,y) = \frac{e^x}{z}
```

```latex
v(x,y) = \frac{\sin x}{z} + y
```

Taking partial derivatives, we get:

```latex
\frac{\partial u}{\partial x} = \frac{e^x}{z} \neq \frac{\partial v}{\partial y}
```

Since the Cauchy-Riemann equations are not satisfied, `g(z)` is not analytic.

### Common Pitfalls

* Failing to check if the complex function satisfies the Cauchy-Riemann equations.
* Not expressing the complex function in terms of its real and imaginary parts.
* Assuming that a non-analytic function can still be integrated over a contour.

### Quick Summary

* Complex variables are essential tools for solving problems involving frequency, resonance, and oscillations.
* A complex function is analytic if it satisfies the Cauchy-Riemann equations.
* The integral of an analytic complex function over a contour can be expressed as:

```latex
\int \frac{f(\zeta)}{(\zeta-z)^n} d\zeta + C
```

where `C` is the constant of integration.