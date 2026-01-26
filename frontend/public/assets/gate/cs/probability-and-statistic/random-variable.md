**Random Variable Theory**
==========================

**Introduction**
---------------

A random variable is a mathematical representation of a set of possible values that a random experiment can take. It assigns a numerical value to each outcome of an experiment, providing a way to quantify and analyze uncertainty.

**Core Concepts**
-----------------

### Definition

*   A **random variable** $X$ is a function that maps the outcomes of a random experiment to real numbers.
*   The set of possible values that $X$ can take is called the **range** or **support** of $X$, denoted as $\text{Range}(X)$.

### Types

*   **Discrete Random Variable**: $X$ takes on distinct, countable values. Examples: number of heads in a coin toss, number of defective products.
*   **Continuous Random Variable**: $X$ can take any value within a given interval or range. Examples: temperature, height, weight.

### Probability Distribution

*   The **probability distribution** of a random variable $X$ is a function that assigns a probability to each possible value of $X$. It satisfies two important properties:
    *   Non-negativity: $P(X=x) \geq 0$
    *   Normalization: $\sum P(X=x) = 1$

### Expected Value

*   The **expected value** or **mean** of a random variable $X$ is denoted as $E[X]$ and is calculated using the probability distribution:
\[ E[X] = \sum_{x} xP(X=x) \]

### Variance and Standard Deviation

*   The **variance** of a random variable $X$ measures the spread or dispersion of its values. It is denoted as $\text{Var}(X)$ and calculated as:
\[ \text{Var}(X) = E[(X - E[X])^2] \]
*   The **standard deviation** is the square root of the variance, denoted as $\sigma_X$.

### Independence

*   Two random variables $X$ and $Y$ are said to be **independent** if the occurrence or non-occurrence of one does not affect the probability of the other. This implies that:
\[ P(X=x, Y=y) = P(X=x)P(Y=y) \]

**Key Formulas/Theorems**
-------------------------

\[ E[X] = \sum_{x} xP(X=x) \]
\[ \text{Var}(X) = E[(X - E[X])^2] \]
\[ \sigma_X = \sqrt{\text{Var}(X)} \]
\[ P(X=x, Y=y) = P(X=x)P(Y=y) \]

**Problem Solving Patterns**
---------------------------

1.  **Discrete vs Continuous**: Identify the type of random variable and choose the correct distribution (e.g., binomial for discrete, normal for continuous).
2.  **Expected Value**: Use the formula $E[X] = \sum xP(X=x)$ to calculate the mean.
3.  **Variance and Standard Deviation**: Apply the formulas $\text{Var}(X) = E[(X - E[X])^2]$ and $\sigma_X = \sqrt{\text{Var}(X)}$.

**Examples with Solutions**
---------------------------

### Example 1: Expected Value

Suppose $X$ is a discrete random variable taking values $x_1, x_2, ..., x_n$ with probabilities $p_1, p_2, ..., p_n$. Calculate the expected value of $X$:

\[ E[X] = \sum_{i=1}^{n} x_i P(X=x_i) \]

### Example 2: Variance and Standard Deviation

Given a continuous random variable $X$ with probability density function (PDF) $f(x)$, calculate the variance and standard deviation:

\[ \text{Var}(X) = E[(X - E[X])^2] = \int_{-\infty}^{\infty} (x-E[X])^2 f(x) dx \]
\[ \sigma_X = \sqrt{\text{Var}(X)} \]

**Common Pitfalls**
-------------------

*   Confusing discrete and continuous random variables.
*   Misunderstanding the concept of independence between variables.

**Quick Summary**
-----------------

*   Random variable: a function assigning numerical values to experiment outcomes.
*   Types: discrete, continuous.
*   Probability distribution: assigns probabilities to possible values.
*   Expected value, variance, and standard deviation are key concepts.
*   Independence is crucial for understanding joint probability distributions.