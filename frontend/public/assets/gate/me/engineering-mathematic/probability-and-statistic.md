**Probability and Statistics**
=====================================

### Introduction

Probability and statistics are fundamental concepts in engineering mathematics that help us understand and analyze random events, systems, and processes. These subjects have numerous applications in various fields, including signal processing, communication systems, machine learning, and more.

### Core Concepts

#### Random Variables

A **random variable** is a function that assigns a real value to each possible outcome of an experiment or event. There are two types:

*   **Discrete random variables**: take on distinct values (e.g., number of heads in 10 coin tosses).
*   **Continuous random variables**: can take any value within a given range (e.g., height of a person).

#### Probability Distribution

A **probability distribution** is a function that describes the probability of each possible outcome. Common distributions include:

*   **Bernoulli distribution** (discrete): models a single coin toss.
*   **Binomial distribution** (discrete): models multiple independent Bernoulli trials.
*   **Poisson distribution** (discrete): models rare events with a large number of trials.

#### Expected Value and Variance

The **expected value** ($E[X]$) is the long-run average value of a random variable. The **variance** ($Var(X)$) measures the spread or dispersion of a random variable.

$$ E[X] = \sum_{x} xP(x) $$

$$ Var(X) = E[(X - E[X])^2] $$

#### Central Limit Theorem (CLT)

The CLT states that, given certain conditions, the distribution of the sample mean will be approximately normal, regardless of the original distribution.

### Key Formulas/Theorems

*   **Binomial distribution**: $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$.
*   **Poisson distribution**: $P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$.
*   **Normal distribution**: $f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$.

### Problem Solving Patterns

*   **Approximation with CLT**: Use the CLT to approximate a binomial or Poisson distribution as normal.
*   **Combining distributions**: Combine probabilities from multiple distributions using convolution or mixture formulas.

### Examples with Solutions

**Example 1:** A coin is tossed $n$ times. What is the expected value of heads?

Solution:

$$ E[X] = \sum_{k=0}^n kP(X = k) $$

Using the binomial distribution:

$$ P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} $$

Substituting and simplifying, we get $E[X] = np$.

**Example 2:** A Poisson distribution has $\lambda = 5$. Find the probability that $X=3$.

Solution:

$$ P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!} $$

Substituting and evaluating, we get $P(X=3) = 0.18$ (rounded to 2 decimal places).

### Common Pitfalls

*   **Confusing discrete and continuous distributions**.
*   **Failing to check for conditions in the CLT**.

### Quick Summary

*   Random variables: discrete and continuous.
*   Probability distribution: Bernoulli, binomial, Poisson, normal.
*   Expected value and variance.
*   Central Limit Theorem (CLT).
*   Approximation with CLT and combining distributions.