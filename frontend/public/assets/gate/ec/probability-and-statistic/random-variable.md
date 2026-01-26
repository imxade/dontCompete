**Random Variables**
======================

**Introduction**
---------------

A random variable is a mathematical representation of a set of possible outcomes from an experiment, where each outcome has an associated probability. In this note, we will cover the fundamental concepts and formulas related to random variables.

**Core Concepts**
-----------------

### Discrete Random Variables

*   A discrete random variable takes on a countable number of distinct values.
*   The probability distribution of a discrete random variable is given by:

    $$P(X = x) = P(x)$$

    where $x$ is the value of the random variable and $P(x)$ is its associated probability.

### Continuous Random Variables

*   A continuous random variable can take on any value within a given interval or range.
*   The probability distribution of a continuous random variable is given by:

    $$f_X(x) = \frac{d}{dx}F_X(x)$$

    where $f_X(x)$ is the probability density function (PDF) and $F_X(x)$ is the cumulative distribution function (CDF).

### Transformation of Random Variables

*   Given a random variable $X$ with PDF $f_X(x)$, we can find the PDF of a new random variable $Y = g(X)$ using:

    $$f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy}g^{-1}(y) \right|$$

**Key Formulas/Theorems**
-------------------------

### Expected Value

*   The expected value of a random variable $X$ is given by:

    $$E[X] = \int_{-\infty}^{\infty} xf_X(x)dx$$

### Variance

*   The variance of a random variable $X$ is given by:

    $$Var(X) = E[(X-E[X])^2]$$

**Problem Solving Patterns**
---------------------------

1.  **Identify the type of random variable**: Discrete or continuous.
2.  **Find the probability distribution**: Use the PDF or CDF to determine the probability of each outcome.
3.  **Apply transformation rules**: Use the formula for transforming random variables.

**Examples with Solutions**
-------------------------

### Example 1

Suppose we have a discrete random variable $X$ with values $\{-2, -1, 0, 1\}$ and probabilities $P(-2) = 0.3$, $P(-1) = 0.2$, $P(0) = 0.4$, and $P(1) = 0.1$. Find the expected value of $X$.

```mermaid
graph LR
    X[Random Variable] -->|Values| >-2, -1, 0, 1
    X -->|Probabilities| P(-2)=0.3, P(-1)=0.2, P(0)=0.4, P(1)=0.1
    style X fill:#f9f,stroke:rgb(0,0,0)
```

Solution:

$$E[X] = (-2)(0.3) + (-1)(0.2) + (0)(0.4) + (1)(0.1) = -0.6$$

### Example 2

Consider a continuous random variable $X$ with PDF $f_X(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$. Find the expected value of $X^2$.

Solution:

$$E[X^2] = \int_{-\infty}^{\infty} x^2 f_X(x) dx = \int_{-\infty}^{\infty} x^2 \frac{1}{\sqrt{2\pi}}e^{-x^2/2} dx$$

Using integration by parts, we get:

$$E[X^2] = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} x e^{-x^2/2} dx = 1$$

**Common Pitfalls**
-------------------

*   Confusing the PDF and CDF of a random variable.
*   Failing to apply transformation rules correctly.

**Quick Summary**
-----------------

*   Discrete and continuous random variables have different probability distributions.
*   The expected value and variance can be calculated using specific formulas.
*   Transformation rules are essential for working with composite random variables.