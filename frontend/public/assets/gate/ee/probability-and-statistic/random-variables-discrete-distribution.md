**Random Variables and Discrete Distributions**
=====================================================

### Introduction
---------------

A random variable is a function that assigns a numerical value to each possible outcome of an experiment. In this note, we will focus on discrete random variables and their distributions.

### Core Concepts
-----------------

*   **Discrete Random Variable**: A random variable that can take on only distinct, isolated values.
*   **Uniform Distribution**: A probability distribution where every possible outcome has an equal chance of occurring.

### Key Formulas/Theorems
-------------------------

*   **Probability Mass Function (PMF)**: The PMF of a discrete random variable X is denoted by $P(X=x)$ and gives the probability that X takes on the value x.
    \[ P(X=x) = \begin{cases} p & \text{if } x = k \\ 0 & \text{otherwise} \end{cases} \]
*   **Cumulative Distribution Function (CDF)**: The CDF of a discrete random variable X is denoted by $F(x)$ and gives the probability that X takes on a value less than or equal to x.
    \[ F(x) = \sum_{k=-\infty}^{x} P(X=k) \]
*   **Uniform Distribution**: If X has a uniform distribution over the set {a, a+1,...,b}, then its PMF is given by:
    \[ P(X=x) = \frac{1}{b-a+1} \quad \text{for } x \in \{a,a+1,...,b\} \]

### Problem Solving Patterns
---------------------------

*   **Uniform Distribution Identification**: To identify if a random variable has a uniform distribution, check if its PMF is constant for all possible values.
*   **Transformation of Random Variables**: When transforming a random variable X to get another random variable Y, the new distribution can be determined by applying the transformation to the original distribution.

### Examples with Solutions
---------------------------

**Example 1**

Let X be a discrete random variable that is uniformly distributed over the set {0,1,...,9}. Find P(X=5).

**Solution**: Since X has a uniform distribution, its PMF is given by:

\[ P(X=x) = \frac{1}{10} \quad \text{for } x \in \{0,1,...,9\} \]

Substituting x = 5 into the PMF gives us:

\[ P(X=5) = \frac{1}{10} = 0.1 \]

**Example 2**

Let Y be a discrete random variable defined as Y = 3X - 5, where X is uniformly distributed over the set {0,1,...,9}. Find the distribution of Y.

**Solution**: First, we find the PMF of Y by substituting x into the transformation:

\[ P(Y=y) = P(3X-5=y) = \frac{1}{10} \quad \text{for } y \in \{ -15,-14,...,21\} \]

This means that Y is also uniformly distributed over the set {-15,-14,...,21}.

### Common Pitfalls
-------------------

*   **Assuming Uniform Distribution**: Do not assume a uniform distribution without checking its PMF.
*   **Misapplying Transformation**: Make sure to apply transformations correctly when finding new distributions.

### Quick Summary
----------------

*   Discrete random variables can take on distinct, isolated values.
*   The probability mass function (PMF) gives the probability of each possible outcome.
*   Uniform distribution: every possible outcome has an equal chance of occurring.
*   Transforming a random variable changes its distribution.