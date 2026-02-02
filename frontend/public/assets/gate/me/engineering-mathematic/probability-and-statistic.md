**Probability and Statistics**
==========================

### Introduction
-----------------

This section provides an overview of probability and statistics, two fundamental concepts in engineering mathematics. Probability deals with the measure of uncertainty or likelihood of events occurring, while statistics involves the collection and analysis of data to draw conclusions.

### Core Concepts
------------------

#### 1. **Binomial Distribution**

The binomial distribution is a discrete probability distribution that models the number of successes in n independent trials, where each trial has a constant probability p of success.

*   The mean (μ) of a binomial distribution is given by: $\mu = np$
*   The variance ($\sigma^2$) of a binomial distribution is given by: $\sigma^2 = np(1-p)$

#### 2. **Continuous Random Variables**

A continuous random variable takes on any value within a given interval or range.

*   The probability density function (pdf) of a continuous random variable is a non-negative function that describes the relative likelihood of observing different values.
*   The cumulative distribution function (cdf) of a continuous random variable is the integral of its pdf, representing the probability that the random variable takes on a value less than or equal to x.

### Key Formulas/Theorems
-------------------------

*   **Law of Large Numbers**: As the number of trials increases, the observed frequency of an event approaches its theoretical probability.
*   **Chebyshev's Inequality**: For any random variable X with mean μ and variance σ^2, the probability that |X - μ| > kσ is less than or equal to 1/k^2.

### Problem Solving Patterns
-----------------------------

#### 1. **Binomial Approximation**

When n is large and p is close to zero or one, the binomial distribution can be approximated by a normal distribution with mean np and variance np(1-p).

*   Example: Given a binomial random variable X with n = 1000 trials and p = 0.01, approximate the distribution of Y = (X - np) / √(np(1-p)).

Solution:

```latex
Y = (X - np) / \sqrt{np(1-p)}
\approx N(0, 1)
```

#### 2. **Maximum Likelihood Estimation**

To estimate the parameters of a probability distribution, use maximum likelihood estimation by maximizing the likelihood function.

*   Example: Given a sample from a normal distribution with unknown mean μ and variance σ^2, find the maximum likelihood estimates for μ and σ^2.

Solution:

```latex
\hat{\mu} = \bar{x}
\hat{\sigma}^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2
```

### Examples with Solutions
---------------------------

#### 1. **Binomial Distribution**

Find the mean and variance of a binomial distribution with n = 10 trials and p = 0.5.

Solution:

```latex
\mu = np = 10(0.5) = 5
\sigma^2 = np(1-p) = 10(0.5)(0.5) = 2.5
```

#### 2. **Continuous Random Variable**

Find the probability density function of a continuous random variable X that takes on values between 0 and 2, with pdf f(x) = 2x for 0 ≤ x ≤ 1 and f(x) = 3 - 2x for 1 < x ≤ 2.

Solution:

```latex
f(x) = \begin{cases}
2x & 0 \leq x \leq 1 \\
3-2x & 1 < x \leq 2
\end{cases}
```

### Common Pitfalls
-------------------

*   Confusing the mean and variance of a binomial distribution.
*   Failing to consider boundary conditions when working with continuous random variables.

### Quick Summary
---------------

| Concept | Formula/Property |
| --- | --- |
| Mean (μ) of Binomial Distribution | μ = np |
| Variance ($\sigma^2$) of Binomial Distribution | $\sigma^2 = np(1-p)$ |
| Chebyshev's Inequality | P(|X - μ| > kσ) ≤ 1/k^2 |

Note: This is a basic outline, and you should expand on each concept with more detail and examples. Additionally, make sure to format your text according to Markdown rules.