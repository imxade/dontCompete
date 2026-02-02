**Probability and Statistics**
==========================

**Introduction**
---------------

Probability and statistics are fundamental concepts in mathematics that play a crucial role in engineering. The former deals with measuring uncertainty, while the latter involves collecting and analyzing data to draw conclusions. In this note, we will cover the key concepts, formulas, and problem-solving patterns related to probability and statistics.

**Core Concepts**
-----------------

### Probability

Probability is a measure of the likelihood of an event occurring. It ranges from 0 (impossible) to 1 (certain). The probability of an event A is denoted by P(A).

*   **Experiment**: A repeatable process with a well-defined outcome.
*   **Event**: A specific outcome or set of outcomes in an experiment.
*   **Sample Space**: The set of all possible outcomes in an experiment.

### Statistical Distributions

Statistical distributions are probability functions that describe the likelihood of observing different values within a sample. Some common distributions include:

*   **Bernoulli Distribution**: Models binary events (e.g., heads or tails).
*   **Binomial Distribution**: Describes the number of successes in n independent trials.
*   **Normal Distribution** (Gaussian): A continuous distribution that models many real-world phenomena.

### Conditional Probability

Conditional probability is a measure of the likelihood of an event occurring given that another event has occurred. It's denoted by P(A|B).

\[ P(A|B) = \frac{P(A \cap B)}{P(B)} \]

**Key Formulas/Theorems**
------------------------

### Probability Rules

1.  **Commutative Property**: \( P(A \cup B) = P(B \cup A) \)
2.  **Associative Property**: \( P((A \cup B) \cup C) = P(A \cup (B \cup C)) \)
3.  **Distributive Property**: \( P(A \cap (B \cup C)) = P((A \cap B) \cup (A \cap C)) \)

### Expectation and Variance

Given a random variable X, the expectation (mean) is denoted by E(X), while variance is σ²(X).

\[ E(X) = \sum xP(x) \]
\[ \sigma^2(X) = E[(X - E(X))^2] \]

**Problem Solving Patterns**
---------------------------

### Example 1

A box contains three coins: a fair coin, a coin with heads on both sides, and a coin with tails on both sides. One coin is picked randomly and tossed. If the first toss results in a head, what's the probability of getting a head in the second toss?

#### Solution

Let's denote the events as follows:

*   A: The coin with heads on both sides is chosen.
*   B: The fair coin is chosen.
*   C: The coin with tails on both sides is chosen.

The sample space can be represented as:

| Coin | Heads on 1st Toss |
| --- | --- |
| A    | 1               |
| B    | 0.5             |
| C    | 0               |

Given that the first toss results in a head, we need to find P(C|A). Using the formula for conditional probability:

\[ P(C|A) = \frac{P(A \cap C)}{P(A)} \]

We know P(A ∩ C) is 1/3 (since there's only one coin with tails on both sides), and P(A) is 1/3. Therefore,

\[ P(C|A) = \frac{\frac{1}{3}}{\frac{1}{3}} = \frac{1}{3} \]

### Example 2

Suppose we have a fair six-sided die. If the first roll results in an even number, what's the probability that the second roll will also be even?

#### Solution

Let A be the event "the first roll is even," and B be the event "the second roll is even."

We know P(A) = 1/2 (since there are three even numbers out of six possible outcomes), and we want to find P(B|A).

Using the formula for conditional probability:

\[ P(B|A) = \frac{P(A \cap B)}{P(A)} \]

Since the rolls are independent, P(A ∩ B) is equal to P(A). Therefore,

\[ P(B|A) = \frac{\frac{1}{2}}{\frac{1}{2}} = 1 \]

**Common Pitfalls**
-------------------

*   Failing to apply the correct probability rule (e.g., using the product rule instead of the sum rule).
*   Not accounting for conditional probabilities or dependencies between events.
*   Misinterpreting statistical distributions or failing to check assumptions.

**Quick Summary**
-----------------

### Probability

*   Measure of likelihood: 0 ≤ P(A) ≤ 1
*   Conditional probability: P(A|B)
*   Rules:
	+ Commutative property
	+ Associative property
	+ Distributive property

### Statistical Distributions

*   Bernoulli distribution
*   Binomial distribution
*   Normal (Gaussian) distribution

### Expectation and Variance

*   E(X): Mean of a random variable X
*   σ²(X): Variance of a random variable X