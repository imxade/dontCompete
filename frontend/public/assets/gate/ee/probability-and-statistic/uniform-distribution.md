**Uniform Distribution**
=========================

### Introduction
-----------------

A uniform distribution is a type of probability distribution where every possible outcome has an equal chance of occurring. In other words, each value within a given range is equally likely to be selected from a set.

### Core Concepts
------------------

#### Discrete Uniform Random Variable
--------------------------------------

Let $X$ be a discrete random variable that takes values in the set $\{a, a+1, ..., b-1, b\}$ where $a \leq b$. Then, $X$ is said to have a uniform distribution over this set.

*   The probability mass function (PMF) of a uniform distribution is given by:

$$
P(X = k) = \frac{1}{b-a+1}
$$

where $k$ ranges from $a$ to $b$.

### Key Formulas/Theorems
---------------------------

LaTeX:
$$
E[X] = \frac{a+b}{2} \\
\sigma^2 = \frac{(b-a)^2}{12} \\
P(a \leq X \leq b) = 1 - P(X < a) = 1 - \left(\frac{a-1}{b-a+1}\right)
$$

### Problem Solving Patterns
-----------------------------

*   **Uniformity of Transforms**: Identify if a variable is uniformly distributed by checking if it satisfies the PMF of a uniform distribution.
*   **Simplification of Expressions**: Simplify expressions involving uniform distributions to identify patterns and relationships.

### Examples with Solutions
---------------------------

**Example 1**
---------------

Suppose $X$ follows a uniform distribution over $\{10, 9, ..., 0, ..., 9, 10\}$. Determine the probability that $2X - 5 \leq 7$.

Solution:

Since $X$ is uniformly distributed over the given set, its PMF is:

$$
P(X = k) = \frac{1}{b-a+1}
$$

We need to find the probability that $2X - 5 \leq 7$, which simplifies to $X \geq 6$. For a uniform distribution over $\{10, 9, ..., 0, ..., 9, 10\}$, this corresponds to values of $X$ in the set $\{6, 7, ..., 9, 10\}$. There are 5 such values.

Hence, the probability is:

$$
P(2X - 5 \leq 7) = P(X \geq 6) = \frac{5}{20} = \frac{1}{4}
$$

**Example 2**
---------------

Consider a random variable $Y$ defined as $Y = \left(\frac{10}{3}\right)X^2 + \left(\frac{7}{9}\right)$. Is $Y$ uniformly distributed?

Solution:

Given that $X$ is uniformly distributed over the set $\{10, 9, ..., 0, ..., 9, 10\}$, we can calculate the PMF of $Y$ as follows:

$$
P(Y = k) = P\left(\frac{10}{3}X^2 + \frac{7}{9} = k\right)
$$

Simplifying this expression leads to a quadratic equation in terms of $X$. However, due to the specifics of the problem and the uniform distribution, we can conclude that $Y$ is not uniformly distributed.

### Common Pitfalls
---------------------

*   **Misunderstanding the Support**: Carefully identify the support (range) of the random variable for uniform distributions.
*   **Incorrect Transformation**: Verify transformations accurately when dealing with uniform distributions.

### Quick Summary
-------------------

**Uniform Distribution Key Points:**

*   Uniform PMF: $P(X = k) = \frac{1}{b-a+1}$
*   Expectation and Variance formulas:
    *   $E[X] = \frac{a+b}{2}$
    *   $\sigma^2 = \frac{(b-a)^2}{12}$

This comprehensive Theory Note provides a solid foundation for tackling uniform distribution problems in the GATE CS exam. Remember to practice solving examples and applying concepts to actual questions to reinforce your understanding.