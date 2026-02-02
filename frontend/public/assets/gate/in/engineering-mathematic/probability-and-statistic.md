**Probability and Statistics**
==========================

**Introduction**
---------------

Probability and statistics are essential tools for engineers to analyze and make informed decisions about random phenomena. This note will cover the theoretical concepts, formulas, and insights required to solve problems related to probability and statistics.

**Core Concepts**
-----------------

### 1. Probability Density Function (PDF)

The PDF of a continuous random variable X is a function f(x) that satisfies:

$$f(x) = \begin{cases}
\frac{d}{dx}F(x), & \text{if }x\in(-\infty, \infty) \\
0, & \text{otherwise}
\end{cases}$$

where F(x) is the cumulative distribution function (CDF).

### 2. Cumulative Distribution Function (CDF)

The CDF of a continuous random variable X is defined as:

$$F(x) = \int_{-\infty}^{x} f(t)\,dt$$

### 3. Expectation and Variance

Given a random variable X with PDF f(x), the expectation E[X] is defined as:

$$E[X] = \int_{-\infty}^{\infty} xf(x)\,dx$$

The variance Var(X) is defined as:

$$Var(X) = E[(X-E[X])^2]$$

### 4. Conditional Probability and Independence

Given two events A and B, the conditional probability of A given B is:

$$P(A|B) = \frac{P(A\cap B)}{P(B)}$$

Two events A and B are independent if:

$$P(A\cap B) = P(A)P(B)$$

**Key Formulas/Theorems**
-------------------------

### 1. Markov's Inequality

For a non-negative random variable X, Markov's inequality states that:

$$P(X \geq a) \leq \frac{E[X]}{a}$$

### 2. Chebyshev's Inequality

For any random variable X with finite mean E[X] and variance Var(X), Chebyshev's inequality states that:

$$P(|X-E[X]| \geq k) \leq \frac{Var(X)}{k^2}$$

**Problem Solving Patterns**
---------------------------

When solving probability problems, always:

1.  Identify the type of distribution (e.g., uniform, normal)
2.  Use the corresponding PDF or CDF
3.  Apply relevant formulas and theorems (e.g., Markov's inequality)

**Examples with Solutions**
-------------------------

### Example 1: Finding the probability using a PDF

Suppose we have a random variable X with PDF:

$$f(x) = \begin{cases}
2x, & 0\leq x \leq 1 \\
0, & \text{otherwise}
\end{cases}$$

Find P(X > 3/4).

```mermaid
graph LR
A[Step 1: Find CDF] --> B[Step 2: Use CDF to find probability]
```

Solution:

First, we need to find the CDF F(x):

$$F(x) = \int_{0}^{x} t\,dt = x^2$$

Then, we can use Markov's inequality to find P(X > 3/4):

$$P(X>3/4) = 1 - P(X\leq3/4) = 1 - F(3/4) = 1 - (3/4)^2 = 0.0625$$

### Example 2: Using Chebyshev's inequality

Suppose we have a random variable X with mean E[X] = 10 and variance Var(X) = 16. Find P(|X-10| > 3).

```mermaid
graph LR
A[Step 1: Identify parameters] --> B[Step 2: Apply Chebyshev's inequality]
```

Solution:

Using Chebyshev's inequality, we get:

$$P(|X-10|\geq3) \leq \frac{Var(X)}{k^2} = \frac{16}{9} = \boxed{1.78}$$

**Common Pitfalls**
-------------------

*   Failing to identify the type of distribution
*   Not using the correct formula or theorem for a given problem
*   Misinterpreting probability values (e.g., P(X > a) vs. P(X ≥ a))

**Quick Summary**
-----------------

*   Probability density function (PDF)
*   Cumulative distribution function (CDF)
*   Expectation and variance
*   Conditional probability and independence
*   Markov's inequality and Chebyshev's inequality

This note provides an overview of the key concepts, formulas, and insights required to solve problems related to probability and statistics. By mastering these concepts, you will be better equipped to tackle a wide range of engineering mathematics problems.