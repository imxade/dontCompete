**Probability and Statistics for Chemical Engineering**
=====================================================

**Introduction**
---------------

Probability and statistics are fundamental concepts in chemical engineering, used to analyze and model real-world systems. Understanding these principles is crucial for making informed decisions in process design, optimization, and control.

**Core Concepts**
-----------------

### 1. Probability Distribution Function (PDF)

A probability distribution function represents the probability of a random variable $X$ taking on different values. The PDF is denoted as $f(x)$, where $x$ is the value of the random variable.

### 2. Expected Value ($E[X]$)

The expected value of a random variable $X$ is the mean or average value that it can take on. It is calculated using the formula:

$$E[X] = \int_{-\infty}^{\infty} xf(x)dx$$

where $f(x)$ is the probability density function (PDF).

### 3. Variance ($\sigma^2$)

The variance of a random variable $X$ measures the spread or dispersion of its values from the expected value. It is calculated using the formula:

$$\sigma^2 = E[(X-E[X])^2] = \int_{-\infty}^{\infty} (x-E[X])^2f(x)dx$$

### 4. Standard Deviation ($\sigma$)

The standard deviation of a random variable $X$ is the square root of its variance:

$$\sigma = \sqrt{\sigma^2}$$

**Key Formulas/Theorems**
------------------------

### Central Limit Theorem (CLT)

The CLT states that, given certain conditions, the distribution of the sample mean $\bar{X}$ will be approximately normal with a large enough sample size $n$:

$$\bar{X} \sim N(\mu, \frac{\sigma^2}{n})$$

where $\mu = E[X]$ is the population mean and $\sigma^2$ is the population variance.

### Chebyshev's Inequality

Chebyshev's inequality provides an upper bound for the probability that a random variable $X$ deviates from its expected value by more than a certain amount:

$$P(|X-E[X]| \geq k) \leq \frac{\sigma^2}{k^2}$$

**Problem Solving Patterns**
---------------------------

When solving problems involving probability and statistics, follow these steps:

1.  Identify the type of distribution (e.g., normal, binomial, Poisson).
2.  Calculate the expected value ($E[X]$) using the formula.
3.  Calculate the variance ($\sigma^2$) using the formula or the CLT for large samples.
4.  Use Chebyshev's inequality to estimate the probability of extreme values.

**Examples with Solutions**
---------------------------

### Example 1: Expected Value

Given a random variable $X$ with PDF:

$$f(x) = \begin{cases} 2x & \text{for } 0 \leq x \leq 1 \\ 0 & \text{otherwise} \end{cases}$$

Find the expected value of $X$, $E[X]$.

**Solution:**

```latex
E[X] = \int_{0}^{1} x(2x)dx = \left[\frac{x^3}{\cancel{\frac{1}{3}}} \right]_0^1 = \frac{1}{3}
```

### Example 2: Variance

Given a random variable $X$ with PDF:

$$f(x) = \begin{cases} \frac{1}{2} & \text{for } -1 \leq x \leq 1 \\ 0 & \text{otherwise} \end{cases}$$

Find the variance of $X$, $\sigma^2$.

**Solution:**

```latex
E[X] = \int_{-1}^{1} xf(x)dx = 0 \\
\sigma^2 = E[(X-E[X])^2] = \int_{-1}^{1} x^2f(x)dx = \frac{1}{3}
```

### Example 3: Standard Deviation

Given a random variable $X$ with PDF:

$$f(x) = \begin{cases} \frac{1}{2} & \text{for } -1 \leq x \leq 1 \\ 0 & \text{otherwise} \end{cases}$$

Find the standard deviation of $X$, $\sigma$.

**Solution:**

```latex
\sigma = \sqrt{\sigma^2} = \sqrt{\frac{1}{3}}
```

### Solution to Q1 (ID: ch\_2021\_38)

Given a probability distribution function (PDF) for a random variable $X$:

$$f(x) = \begin{cases} 0.5 & \text{for } x = 1 \\ 0 & \text{otherwise} \end{cases}$$

Find the standard deviation of the sample mean $\bar{X}$ with a sample size $n=68$.

**Solution:**

```latex
\mu = E[X] = 1 \\
\sigma^2 = Var(X) = 0 \\
\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}} = 0
```

The final answer is $\boxed{0}$.

**Common Pitfalls**
------------------

*   **Misunderstanding the CLT**: Make sure to understand that the CLT only applies when the sample size $n$ is sufficiently large (usually $n \geq 30$).
*   **Incorrect application of Chebyshev's inequality**: Ensure you use the correct formula and follow the steps carefully.
*   **Not checking units**: Always check the units of your answer to ensure they match the problem.

**Quick Summary**
-----------------

| Concept | Formula/Description |
| --- | --- |
| Probability Distribution Function (PDF) | $f(x)$ |
| Expected Value ($E[X]$) | $\int_{-\infty}^{\infty} xf(x)dx$ |
| Variance ($\sigma^2$) | $E[(X-E[X])^2] = \int_{-\infty}^{\infty} (x-E[X])^2f(x)dx$ |
| Standard Deviation ($\sigma$) | $\sqrt{\sigma^2}$ |
| Central Limit Theorem (CLT) | $\bar{X} \sim N(\mu, \frac{\sigma^2}{n})$ |
| Chebyshev's Inequality | $P(|X-E[X]| \geq k) \leq \frac{\sigma^2}{k^2}$ |

Note: This summary is meant to be a quick reference and should not replace thorough understanding of the concepts.