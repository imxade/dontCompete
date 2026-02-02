**Sequences and Series - Calculus Theory Note**
=====================================================

### Introduction
-------------

A sequence is a list of numbers in a specific order, while a series is the sum of the terms of a sequence. In calculus, sequences and series are used to study functions and their behavior.

### Core Concepts
-----------------

* **Sequence**: A sequence is an ordered set of numbers, where each number is called a term. The general term of a sequence can be denoted as `a_n`, where `n` represents the position of the term in the sequence.
* **Series**: A series is the sum of the terms of a sequence. It is denoted as `S = \sum_{n=1}^{\infty} a_n`.
* **Convergence**: A sequence or series is said to converge if its limit exists.

### Key Formulas/Theorems
-------------------------

#### Sequence Convergence

LaTeX: $\lim_{n\to\infty} a_n = L$

If the limit of the sequence exists, it converges to `L`.

#### Series Convergence

The ratio test:
LaTeX: $\left| \frac{a_{n+1}}{a_n} \right| < 1$ implies convergence.

The root test:
LaTeX: $\lim_{n\to\infty} \sqrt[n]{|a_n|} < 1$ implies convergence.

### Problem Solving Patterns
-----------------------------

* **Check for convergence**: Use the ratio or root test to determine if a series converges.
* **Find the limit of a sequence**: Evaluate the general term and take the limit as `n` approaches infinity.

### Examples with Solutions
---------------------------

**Example 1**

Consider the sequence `a_n = \frac{1}{n}`. Does it converge?

Solution:

LaTeX: $\lim_{n\to\infty} \frac{1}{n} = 0$

The sequence converges to `0`.

**Example 2**

Consider the series `S = \sum_{n=1}^{\infty} \frac{1}{n^2}`. Does it converge?

Solution:

Using the ratio test:
LaTeX: $\left| \frac{\frac{1}{(n+1)^2}}{\frac{1}{n^2}} \right| = \frac{n^2}{(n+1)^2} < 1$

The series converges.

### Common Pitfalls
-------------------

* **Misapplication of convergence tests**: Be sure to apply the correct test for the given sequence or series.
* **Incorrect evaluation of limits**: Double-check your calculations when evaluating limits.

### Quick Summary
------------------

* Sequences and series are used in calculus to study functions.
* A sequence is a list of numbers, while a series is the sum of its terms.
* Convergence tests include the ratio test and root test.
* Be careful when applying convergence tests and evaluating limits.