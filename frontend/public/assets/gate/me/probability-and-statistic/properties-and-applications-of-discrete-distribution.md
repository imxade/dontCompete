**Discrete Distribution: Properties and Applications**
======================================================

**Introduction**
---------------

A discrete distribution is a probability distribution that describes the behavior of a random variable that can take on only distinct, countable values. These distributions are used to model phenomena where the outcome is restricted to a finite set of possible values.

**Core Concepts**
-----------------

### 1. Probability Mass Function (PMF)

The PMF of a discrete random variable $X$ is given by:

$$P(X = x) = p(x), \quad x \in S,$$

where $S$ is the sample space and $p(x)$ is the probability mass function.

### 2. Cumulative Distribution Function (CDF)

The CDF of a discrete random variable $X$ is defined as:

$$F_X(x) = P(X \leq x), \quad x \in R.$$

**Key Formulas/Theorems**
-------------------------

### 1. Poisson Distribution

The PMF of a Poisson distribution with parameter $\lambda$ is given by:

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \ldots.$$

### 2. Binomial Distribution

The PMF of a binomial distribution with parameters $n$ and $p$ is given by:

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, 2, \ldots, n.$$

**Problem Solving Patterns**
---------------------------

### 1. Using the Poisson Distribution

When solving problems involving the Poisson distribution, follow these steps:

1. Identify the parameter $\lambda$.
2. Use the PMF formula to find the probability of interest.
3. Simplify the expression and round off to the required decimal places.

**Examples with Solutions**
-------------------------

### Example 1: Poisson Distribution

Suppose $X \sim P(\lambda = 5)$, and we want to find $P(X = 2)$. Using the PMF formula:

$$P(X = 2) = \frac{5^2 e^{-5}}{2!} = \frac{25e^{-5}}{2}.$$

Evaluating this expression gives us:

$$P(X = 2) \approx 0.085.$$

### Example 2: Binomial Distribution

Suppose $X \sim B(n = 10, p = 0.3)$, and we want to find $P(X = 4)$. Using the PMF formula:

$$P(X = 4) = \binom{10}{4} (0.3)^4 (1-0.3)^{6}.$$

Evaluating this expression gives us:

$$P(X = 4) \approx 0.243.$$

**Common Pitfalls**
-----------------

* When using the Poisson distribution, ensure that $\lambda$ is a positive real number.
* When using the binomial distribution, ensure that $n$ is a non-negative integer and $p$ is between 0 and 1.

**Quick Summary**
----------------

* Discrete distributions model phenomena with distinct, countable outcomes.
* The PMF and CDF are essential concepts in discrete probability theory.
* Poisson and Binomial distributions are commonly used discrete distributions.

Note: This content will be updated based on future source questions.