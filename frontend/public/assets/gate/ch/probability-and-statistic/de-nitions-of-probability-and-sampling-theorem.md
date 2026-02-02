**Probability and Statistics - Definitions of Probability and Sampling Theorem**
===========================================================

### Introduction
--------------

This note covers the fundamental concepts of probability, specifically focusing on the definitions of probability and the sampling theorem. Understanding these principles is crucial for tackling problems in probability and statistics.

### Core Concepts
-----------------

#### Definition of Probability
-----------------------------

Probability is a measure of the likelihood of an event occurring. It is denoted by P(A) or Pr(A). The probability of an event A can be calculated using the formula:

$$P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}$$

#### Types of Probability
-------------------------

There are two types of probabilities: **Theoretical Probability** and **Experimental Probability**.

*   Theoretical probability is a measure of how likely an event is to occur based on the total number of possible outcomes.
*   Experimental probability is a measure of how likely an event is to occur based on repeated trials or experiments.

#### Sampling Theorem
---------------------

The sampling theorem states that if a continuous-time signal x(t) has a bandwidth W, then it can be perfectly reconstructed from its samples taken at a rate greater than 2W. Mathematically, this can be represented as:

$$f(x(t)) = \sum_{n=-\infty}^{\infty} f_n e^{j(2\pi n x t)}$$

where $f_n$ are the Fourier coefficients of the signal.

### Key Formulas/Theorems
---------------------------

#### Probability Density Function (PDF)
--------------------------------------

The probability density function (PDF) of a continuous random variable X is denoted by f(x). The PDF satisfies the following properties:

*   $$\int_{-\infty}^{\infty} f(x) dx = 1$$
*   $$P(a \leq X \leq b) = \int_{a}^{b} f(x) dx$$

#### Mean and Variance of a Random Variable
---------------------------------------------

The mean (μ) and variance ($\sigma^2$) of a random variable X are given by:

*   $$\mu = E(X) = \int_{-\infty}^{\infty} x f(x) dx$$
*   $$\sigma^2 = Var(X) = E((X - \mu)^2)$$

#### Bayes' Theorem
------------------

Bayes' theorem states that the posterior probability of a hypothesis given some evidence is proportional to the prior probability of the hypothesis and the likelihood of the evidence given the hypothesis:

$$P(H|E) \propto P(E|H)P(H)$$

### Problem Solving Patterns
-----------------------------

When solving problems involving probability, follow these steps:

1.  Identify the type of problem: discrete or continuous.
2.  Determine the appropriate formula or theorem to use.
3.  Apply the formula or theorem with the given values.

### Examples with Solutions
---------------------------

**Example 1:** Given a normal distribution function $f(x) = \frac{4}{\sqrt{2\pi}} e^{-8(x+3)^2}$, find the ordered pair $(\mu, \sigma)$.

Solution:

The mean ($\mu$) and standard deviation ($\sigma$) can be calculated as follows:

$$\mu = -3$$

$$\sigma^2 = \frac{1}{32}$$

$$\sigma = \frac{1}{4}$$

Therefore, the ordered pair is $(\mu, \sigma) = (-3, 0.25)$.

**Example 2:** A fair six-sided die is rolled. What is the probability that the number obtained is greater than 4?

Solution:

The sample space for rolling a six-sided die is {1, 2, 3, 4, 5, 6}. There are 6 possible outcomes.

The favorable outcome (rolling a number greater than 4) is {5, 6}.

Therefore, the probability of obtaining a number greater than 4 is $\frac{2}{6} = \frac{1}{3}$.

### Common Pitfalls
-------------------

*   Misinterpreting the type of problem: discrete or continuous.
*   Failing to apply the correct formula or theorem.
*   Not calculating the mean and variance correctly.

### Quick Summary
-----------------

| Concept | Definition |
| --- | --- |
| Probability | A measure of the likelihood of an event occurring. |
| Theoretical Probability | Based on the total number of possible outcomes. |
| Experimental Probability | Based on repeated trials or experiments. |
| Sampling Theorem | Signals can be perfectly reconstructed from samples taken at a rate greater than 2W. |

**Note:** This is just one way to structure the content, and you may need to adjust it based on your needs.

Feel free to ask me to clarify any part of this theory note!