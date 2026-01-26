**Root Locus Theory**
=====================

**Introduction**
---------------

The root locus plot is a graphical representation of the roots of the characteristic equation of a system as a parameter (usually a gain) varies. It is an essential tool for control system analysis, particularly in finding the stability and damping characteristics of a system.

**Core Concepts**
-----------------

### What is Root Locus?

The root locus is a plot of the roots of the characteristic equation of a system, which are the values of the variable (usually s) that satisfy the equation:

`|G(s)| = 1 / |(s + p_i)|`

where `p_i` are the poles of the open-loop transfer function.

### Types of Root Locus

There are three types of root loci:

* **Real Axis**: When all poles and zeros lie on the real axis.
* **Complex Conjugate**: When a pair of complex conjugate poles exist.
* **Multiple Roots**: When two or more roots coincide.

**Key Formulas/Theorems**
-------------------------

### Characteristic Equation

The characteristic equation is given by:

`G(s)H(s) = K / (s + p_1)(s + p_2)...`

where `p_i` are the poles of the open-loop transfer function and `K` is a gain.

### Number of Branches

The number of branches in the root locus plot is equal to the number of closed-loop poles, which is typically `n`.

### Angles of Departure and Arrival

* **Angles of Departure**: The angles at which the branches depart from the complex conjugate poles.
* **Angles of Arrival**: The angles at which the branches arrive at the real axis.

**Problem Solving Patterns**
---------------------------

### Finding Breakaway Points

To find the breakaway points, we need to differentiate the characteristic equation with respect to `s` and set it equal to zero:

`d|G(s)|^2 / ds = 0`

This will give us the values of `s` where the branches depart from or arrive at.

**Examples with Solutions**
---------------------------

### Example 1: Finding Breakaway Points

Consider the system with open-loop transfer function:

`(s + 5)(s + 10) / (s(s + 2))`

Find the breakaway points for this system.

```mermaid
graph LR
    A[Characteristic Equation] --> B[Differentiate |G(s)|^2]
    B --> C[Set d|G(s)|^2/ds = 0]
```

Solving the characteristic equation, we get:

`K / (s + 5)(s + 10) = s(s + 2)`

Differentiating with respect to `s`, we get:

`d(K / (s + 5)(s + 10)) / ds = d(s(s + 2)) / ds`

Setting the derivatives equal to zero, we get two breakaway points at `s = -3.6` and `s = -11.4`.

### Example 2: Finding Breakaway Points (Source Question Q1)

Consider the system with open-loop transfer function:

`(s^2 + 7s + 10) / (s(s + 2)(s + 5))`

Find the breakaway points for this system.

```mermaid
graph LR
    A[Characteristic Equation] --> B[Differentiate |G(s)|^2]
    B --> C[Set d|G(s)|^2/ds = 0]
```

Solving the characteristic equation, we get:

`K / (s^2 + 7s + 10) = s(s + 2)(s + 5)`

Differentiating with respect to `s`, we get:

`d(K / (s^2 + 7s + 10)) / ds = d(s(s + 2)(s + 5)) / ds`

Setting the derivatives equal to zero, we get two breakaway points at `s = -3.8` and `s = -9.2`.

**Common Pitfalls**
------------------

* **Not considering the sign of the derivative**: When differentiating the characteristic equation with respect to `s`, make sure to consider the sign of the derivative.
* **Not identifying all breakaway points**: Make sure to identify all breakaway points, not just the first one.

**Quick Summary**
----------------

* The root locus plot is a graphical representation of the roots of the characteristic equation as a parameter (usually a gain) varies.
* There are three types of root loci: real axis, complex conjugate, and multiple roots.
* To find breakaway points, differentiate the characteristic equation with respect to `s` and set it equal to zero.

Note: This is just a starting point for your study note. You can add more examples, formulas, and insights as needed to cover all theoretical concepts required to solve the source questions.