**Sampling Theorems and Conditional Probability**
======================================================

### Introduction
Sampling theorems provide a framework for understanding the relationship between the sample space, events, and their probabilities. This topic is critical for probability and statistics as it enables us to make inferences about populations based on samples.

### Core Concepts

#### Sampling Theorems

*   **Law of Large Numbers (LLN)**: States that as the sample size increases, the average of the sample will converge to the population mean.
    *   $\lim_{n\to\infty} \frac{1}{n} \sum_{i=1}^{n} X_i = E[X]$
*   **Chebyshev's Inequality**: Provides a bound on the probability that a random variable deviates from its mean by more than a certain amount.
    *   $P(|X - E[X]| \geq k) \leq \frac{\sigma^2}{k^2}$

#### Conditional Probability
Conditional probability measures the likelihood of an event occurring given that another event has occurred.

*   **Definition**: $P(A|B) = \frac{P(A \cap B)}{P(B)}$
*   **Theorem**: If $A$ and $B$ are independent events, then $P(A|B) = P(A)$

### Key Formulas/Theorems
$$
\begin{align*}
E[X] &= \sum_{x} xP(X=x) \\
Var(X) &= E[(X-E[X])^2] \\
P(A \cup B) &= P(A) + P(B) - P(A \cap B)
\end{align*}
$$

### Problem Solving Patterns
When solving problems involving sampling theorems and conditional probability, consider the following patterns:

1.  **Identify the problem type**: Determine whether it involves calculating a population parameter (e.g., mean or variance), assessing the likelihood of an event given another event has occurred, or estimating a sample statistic.
2.  **Determine relevant formulas/theorems**: Choose the appropriate formula or theorem based on the problem context and the concepts required to solve it.

### Examples with Solutions
**Example 1:** A fair coin is flipped twice. What is the probability that at least one of the flips results in heads?

*   **Solution:**
    *   Define events $A$ (first flip is heads) and $B$ (second flip is heads).
    *   Since these events are independent, we can calculate their individual probabilities.
    *   Calculate the probability of both events occurring ($P(A \cap B)$), then apply conditional probability to find $P(\text{at least one head})$
        *   **Solution:**
            $P(A) = P(B) = 0.5$
            $P(A \cap B) = P(A) \cdot P(B) = 0.25$
            $P(\text{at least one head}) = 1 - P(\text{no heads}) = 1 - (1-0.25)^2$

**Example 2:** Given that a random variable $X$ follows a Poisson distribution with mean $\lambda$, calculate the probability of at least two events occurring in any given interval.

*   **Solution:**
    *   Recall the formula for the Poisson distribution and apply it to find $P(X \geq 2)$.
        $P(X = k) = e^{-\lambda} \frac{\lambda^k}{k!}$

### Common Pitfalls
When solving problems involving sampling theorems and conditional probability, avoid these common pitfalls:

*   **Failing to identify relevant formulas/theorems**: Carefully review the problem context to ensure that you're using the correct formula or theorem.
*   **Misapplying concepts**: Double-check your understanding of each concept before applying it to a problem.

### Quick Summary
Sampling theorems and conditional probability are crucial for making inferences about populations based on samples. This topic covers essential concepts, formulas, and theorems required to solve problems involving:

*   Law of Large Numbers (LLN)
*   Chebyshev's Inequality
*   Conditional Probability

Mastering these principles will enable you to tackle a wide range of questions related to probability and statistics.

---

This comprehensive theory note covers all theoretical concepts, formulas, and insights required to solve the source questions and similar future ones.