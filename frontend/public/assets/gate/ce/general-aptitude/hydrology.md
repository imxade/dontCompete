**Hydrology: A Comprehensive Theory Note for GATE CS Exam**
===========================================================

### Introduction
-----------------

Hydrology, a branch of geophysics, deals with the study of water on Earth's surface and beneath it. In the context of the GATE CS exam, hydrology is tested through questions that require an understanding of probability distributions, specifically Poisson's distribution.

### Core Concepts
----------------

*   **Poisson's Distribution**: This distribution models the number of events occurring in a fixed interval of time or space if these events occur with a known constant mean rate and independently of the time since the last event. The probability mass function (PMF) for Poisson's distribution is given by:

    $$ P(X = k) = \frac{e^{-\lambda} \cdot \lambda^k}{k!} $$

    where $X$ is the random variable representing the number of events, $\lambda$ is the mean rate parameter, and $k$ is a non-negative integer.

*   **Return Period**: The return period of an event is the average time between occurrences of that event. For example, if a large earthquake has a return period of 200 years, it means that on average, such an earthquake occurs once every 200 years.

### Key Formulas/Theorems
-------------------------

For this topic, we need to focus on calculating probabilities using Poisson's distribution.

### Problem Solving Patterns
-----------------------------

When solving questions related to hydrology and probability distributions, follow these patterns:

1.  Identify the type of distribution (in this case, Poisson's).
2.  Understand the parameters involved (e.g., $\lambda$ for the mean rate parameter).
3.  Use the appropriate formula from the distribution to calculate the desired probability.

### Examples with Solutions
---------------------------

**Example 1:** Given that the return period of a large earthquake is 200 years, and assuming it follows Poisson's distribution, find the probability that it will be exceeded at least once in 50 years.

## Step 1: Identify the parameters
The mean rate parameter $\lambda$ for earthquakes can be considered as the inverse of the return period. In this case, $\lambda = \frac{1}{200}$.

## Step 2: Determine the probability of exceeding the event in a year
We want to find $P(X \geq 1)$ where $X$ is the number of large earthquakes in a given year.

## Step 3: Calculate the probability using Poisson's distribution
The PMF for Poisson's distribution gives us the probability of having exactly $k$ events:

$$ P(X = k) = \frac{e^{-\lambda} \cdot \lambda^k}{k!} $$

To find the probability that at least one earthquake occurs in a year, we can use the complement rule: $P(X \geq 1) = 1 - P(X = 0)$.

## Step 4: Calculate $P(X = 0)$
$$ P(X = 0) = e^{-\lambda} $$

Substituting $\lambda = \frac{1}{200}$, we get:

$$ P(X = 0) = e^{-\frac{1}{200}} $$

## Step 5: Calculate the final probability
Now, calculate $P(X \geq 1)$ using the complement rule.

### Quick Summary
-------------------

*   Poisson's distribution models the number of events occurring in a fixed interval.
*   Return period is the average time between occurrences of an event.
*   Use the PMF for Poisson's distribution to calculate probabilities.

### Common Pitfalls
--------------------

*   Confusing return period with the mean rate parameter $\lambda$.
*   Not using the appropriate formula from the distribution to solve the problem.