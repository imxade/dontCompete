**Random Variables and Distribution**
=====================================

### Introduction
-----------------

Random variables are a fundamental concept in probability and statistics, used to model uncertain events or phenomena. A random variable assigns a numerical value to each outcome of an experiment or event. In this note, we will cover the basics of random variables, their distributions, and key concepts related to them.

### Core Concepts
----------------

#### What is a Random Variable?

A random variable $X$ is a function that maps outcomes from a sample space $\Omega$ to real numbers. It can be discrete or continuous, depending on its nature.

**Definition**: A random variable $X$ is said to be **discrete** if it takes on distinct values with positive probability. Otherwise, it's called **continuous**.

#### Distribution of a Random Variable

The distribution of a random variable describes the probabilities associated with each value it can take. For continuous random variables, this is typically represented using a probability density function (PDF). For discrete random variables, we use a probability mass function (PMF).

**Continuous Random Variables**: $X$ has a PDF $f(x)$ such that:

$$
\int_{-\infty}^{\infty} f(x) dx = 1 \quad \text{and} \quad f(x) \geq 0, \quad \forall x \in \mathbb{R}
$$

**Discrete Random Variables**: $X$ has a PMF $p_X(x)$ such that:

$$
\sum_{x \in \text{range}(X)} p_X(x) = 1 \quad \text{and} \quad p_X(x) \geq 0, \quad \forall x \in \text{range}(X)
$$

### Key Formulas/Theorems
-------------------------

#### Cumulative Distribution Function (CDF)

The CDF of a random variable $X$ is given by:

$$
F_X(x) = P(X \leq x) = \int_{-\infty}^{x} f(t) dt, \quad x \in \mathbb{R}
$$

for continuous variables. For discrete variables, it's the sum of PMFs up to $x$.

#### Probability Density Function (PDF)

The PDF is the derivative of the CDF:

$$
f_X(x) = F'_X(x), \quad x \in \mathbb{R}
$$

#### Normal Distribution

A random variable $X$ follows a normal distribution with mean $\mu$ and standard deviation $\sigma$, denoted as $N(\mu, \sigma^2)$, if its PDF is:

$$
f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \quad x \in \mathbb{R}
$$

### Problem Solving Patterns
---------------------------

When dealing with random variables, it's essential to identify the type of distribution (discrete or continuous) and apply the relevant formulas. Common patterns include:

1.  **Finding probability**: Use CDF or PDF as necessary.
2.  **Finding expected value**: Calculate $E[X]$ using the formula $\int_{-\infty}^{\infty} xf(x) dx$ for continuous variables, or $\sum x \cdot p_X(x)$ for discrete ones.

### Examples with Solutions
---------------------------

**Example 1: Normal Distribution**

Suppose we have a normal distribution $X \sim N(50, 10^2)$. Find the probability that $X \geq 60$:

```mermaid
graph LR
A[Normal Distribution] -->| X ~ N(50, 100) |> B[CDF]
B -->| F_X(x) = Φ((x-μ)/σ ) | C[CDF Value]
C -->| P(X ≥ 60) = 1 - F_X(60) | D[Probability]
D -->| Substitute values and solve for P(X ≥ 60) | E[Answer]
```

To find the probability, we use the CDF formula with $x=60$:

$$
P(X \geq 60) = 1 - \Phi\left(\frac{60-50}{10}\right)
$$

Using a standard normal table or calculator, we find that $\Phi(2.5) \approx 0.9938$, so the probability is approximately $1 - 0.9938 = 0.0062$.

### Common Pitfalls
------------------

*   **Mixing up discrete and continuous distributions**.
*   **Incorrect application of formulas** (e.g., using the PDF for a discrete variable).
*   **Forgetting to consider boundary values** when calculating probabilities.

### Quick Summary
-----------------

| Topic | Key Concept |
| --- | --- |
| Discrete Random Variables | PMF, CDF, $E[X]$ |
| Continuous Random Variables | PDF, CDF, $E[X]$ |
| Normal Distribution | Formula for PDF, using standard normal table/ calculator. |

By mastering these concepts and formulas, you'll be well-prepared to tackle questions like the one from the GATE CS exam.

(Note: This theory note is a work in progress. You may want to add or modify sections based on your specific needs.)