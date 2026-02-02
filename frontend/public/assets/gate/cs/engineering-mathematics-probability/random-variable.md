**Random Variables**
======================

### Introduction

A random variable is a measurable function from a probability space to the real numbers. It represents a quantity whose value is determined by chance or uncertainty. In this note, we will focus on discrete and continuous random variables.

### Core Concepts

*   **Probability Distribution**: A probability distribution assigns a non-negative real number (called the probability) to each possible value of the random variable.
*   **Expected Value** ($E(X)$): The expected value is a measure of the central tendency of the random variable. It is calculated by summing up the product of each possible value and its corresponding probability.

### Key Formulas/Theorems

#### Discrete Random Variables

$$
E(X) = \sum_{x} xP(X=x)
$$

where $x$ represents the values that $X$ can take, and $P(X=x)$ is the probability of $X$ taking on the value $x$.

#### Continuous Random Variables

$$
E(X) = \int_{-\infty}^{\infty} xf(x)dx
$$

where $f(x)$ is the probability density function (PDF) of the random variable $X$.

### Problem Solving Patterns

When solving problems involving random variables, follow these steps:

1.  **Understand the question**: Identify what information is given and what is being asked.
2.  **Determine the type of distribution**: Decide whether the problem involves discrete or continuous random variables.
3.  **Apply relevant formulas/theorems**: Use the appropriate formula to calculate the expected value, variance, or other quantities.

### Examples with Solutions

**Example 1: Discrete Random Variable**

Suppose we have a random variable $X$ that can take on values $\{0, 1\}$ with probabilities $\frac{1}{2}$ each. Find the expected value of $X$.

$$
E(X) = (0)\left(\frac{1}{2}\right) + (1)\left(\frac{1}{2}\right) = \frac{1}{2}
$$

**Example 2: Continuous Random Variable**

Consider a random variable $X$ that follows an exponential distribution with parameter $\lambda$. Find the expected value of $X$.

$$
E(X) = \int_{0}^{\infty} x\lambda e^{-\lambda x}dx = \frac{1}{\lambda}
$$

### Common Pitfalls

*   **Misunderstanding probability distributions**: Make sure to understand the difference between discrete and continuous random variables.
*   **Incorrect application of formulas/theorems**: Double-check your calculations when using formulas like $E(X)$ or $\text{Var}(X)$.

### Quick Summary

*   Random variables can be either discrete or continuous.
*   The expected value ($E(X)$) is a measure of the central tendency of the random variable.
*   Formulas for expected value vary depending on whether the random variable is discrete or continuous.

[Mermaid Diagram: No specific logic, flow, or structure applies here.]

### References

For further reading and practice problems, refer to:

*   "Probability Theory" by E.T. Jaynes
*   "Random Variables and Probability Distributions" by Khan Academy