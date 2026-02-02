**Theory Note: Sampling Theorems and Conditional Probability**
===========================================================

**Introduction**
---------------

Probability and Statistics are fundamental subjects in computer science, with applications in data analysis, machine learning, and artificial intelligence. This note focuses on sampling theorems and conditional probability, crucial concepts that have been tested in previous GATE exams.

**Core Concepts**
----------------

### 1. Cumulative Distribution Function (CDF)

The CDF of a random variable X is defined as:

$$F(x) = P(X \leq x)$$

where $P(X \leq x)$ represents the probability that X takes on a value less than or equal to x.

### 2. Gaussian Distribution

A Gaussian distribution, also known as the normal distribution, is characterized by its mean (μ) and standard deviation (σ):

$f(x | \mu, \sigma) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$

The cumulative distribution function of a Gaussian distribution is:

$F(x | \mu, \sigma) = \Phi \left( \frac{x-\mu}{\sigma} \right)$

where $\Phi(z)$ is the cumulative distribution function of the standard normal distribution.

### 3. Conditional Probability

Conditional probability measures the probability of an event occurring given that another event has occurred:

$P(A|B) = \frac{P(A \cap B)}{P(B)}$

**Key Formulas/Theorems**
-------------------------

* **Sampling Theorem**: A signal can be reconstructed from its samples if the sampling rate is greater than twice the highest frequency component of the signal.
* **Conditional Probability Formula**: $P(A|B) = \frac{P(A \cap B)}{P(B)}$
* **Gaussian Distribution PDF and CDF**: $f(x | \mu, \sigma)$ and $F(x | \mu, \sigma) = \Phi \left( \frac{x-\mu}{\sigma} \right)$

**Problem Solving Patterns**
---------------------------

1. **Identify the distribution**: Recognize whether a problem involves a uniform, Gaussian, or other distributions.
2. **Apply conditional probability**: Use the formula $P(A|B) = \frac{P(A \cap B)}{P(B)}$ to solve problems involving conditional events.
3. **Use the sampling theorem**: Apply the sampling theorem to determine whether a signal can be reconstructed from its samples.

**Examples with Solutions**
-------------------------

### Example 1: Gaussian Distribution CDF

Find the cumulative distribution function of a Gaussian distribution with mean 0 and standard deviation 1 for x = 2.

$F(2 | \mu=0, \sigma=1) = \Phi(2)$

Using a standard normal distribution table or calculator:

$F(2 | \mu=0, \sigma=1) \approx 0.9773$

### Example 2: Conditional Probability

Find the conditional probability of event A occurring given that event B has occurred.

$P(A|B) = \frac{P(A \cap B)}{P(B)}$

Suppose $P(A \cap B) = 0.6$, $P(B) = 0.8$. Then:

$P(A|B) = \frac{0.6}{0.8} = 0.75$

**Common Pitfalls**
-------------------

* **Misapplying the sampling theorem**: Failing to recognize that a signal cannot be reconstructed from its samples if the sampling rate is not sufficient.
* **Forgetting to account for conditional probability**: Omitting to use the formula $P(A|B) = \frac{P(A \cap B)}{P(B)}$ in problems involving conditional events.

**Quick Summary**
----------------

* Cumulative distribution function (CDF): $F(x) = P(X \leq x)$
* Gaussian distribution: $f(x | \mu, \sigma) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
* Conditional probability: $P(A|B) = \frac{P(A \cap B)}{P(B)}$
* Sampling theorem: A signal can be reconstructed from its samples if the sampling rate is greater than twice the highest frequency component of the signal.