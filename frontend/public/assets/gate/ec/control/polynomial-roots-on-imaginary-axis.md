**Polynomial Roots on Imaginary Axis**
=====================================

### Introduction
----------------

In control systems, polynomial roots play a crucial role in stability analysis. A fundamental aspect of this topic is understanding how to determine if all the roots of a given polynomial lie on the imaginary axis.

### Core Concepts
-----------------

A **polynomial** is an expression consisting of variables and coefficients combined using only addition, subtraction, and multiplication. The **roots** of a polynomial are the values that make it equal to zero. In the context of control systems, we often deal with polynomials in the form:

$$p(s) = \sum_{i=0}^n b_i s^i$$

where $s$ is the complex frequency variable.

### Key Formulas/Theorems
-------------------------

*   **Fundamental Theorem of Algebra**: A polynomial equation has as many roots as its degree, and they can be real or complex.
*   **Routh-Hurwitz Stability Criterion**: This method determines the stability of a system by analyzing the Routh array.

### Problem Solving Patterns
---------------------------

1.  To determine if all the roots of $p(s)$ lie on the imaginary axis, we need to find conditions for which all the coefficients in the polynomial satisfy certain relationships.
2.  We can use the **Descartes' Rule of Signs** or **Routh-Hurwitz Stability Criterion** to derive these conditions.

### Examples with Solutions
---------------------------

*   Given $p(s) = s^3 + 4s^2 + 5s + 1$, find the range of values for which all roots lie on the imaginary axis:

First, we apply the Routh-Hurwitz stability criterion to this polynomial. The characteristic equation is

$$s^3 + 4s^2 + 5s + 1 = 0.$$

The Routh array is given by:

| $s^3$ | $4$ |
| --- | --- |
| $s^2$ | $5$ |
| $s^1$ | $\frac{4 \cdot 5 - 4}{4} = \frac{16}{4} = 4$ |

The Routh array shows that there is a sign change in the first column, indicating at least one root lies on the real axis. Thus, the polynomial has roots both on the imaginary and real axes.

*   Consider $p(s) = s^2 + 4s + 5$. Find conditions for which all its roots lie on the imaginary axis:

The Routh array is

| $s^2$ | $4$ |
| --- | --- |

Since there are no sign changes, this polynomial has all its roots on the imaginary axis.

### Common Pitfalls
-------------------

*   **Not checking for roots on both real and imaginary axes**: Remember to verify that all coefficients satisfy the required relationships.
*   **Using incorrect Routh arrays**: Double-check your calculations when constructing the array.

### Quick Summary
---------------

*   A polynomial has its roots on the imaginary axis if it meets certain conditions.
*   Apply the Routh-Hurwitz stability criterion or Descartes' Rule of Signs to determine these conditions.
*   Use correct Routh arrays and verify sign changes for each column.