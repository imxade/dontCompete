**Conditional Probability**
=========================

### Introduction

Conditional probability is a crucial concept in probability and statistics that deals with the probability of an event occurring given that another event has occurred. It's essential to understand this concept, as it's frequently used in various fields, including machine learning, data analysis, and decision-making.

### Core Concepts

**Definition**: The conditional probability of an event A given that event B has occurred is denoted by P(A|B) and is defined as:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

where $P(A \cap B)$ represents the probability of both events A and B occurring, and $P(B)$ represents the probability of event B occurring.

**Key Principle**: The conditional probability formula can be rearranged to obtain:

$$P(A|B) = \frac{P(A \cap B)}{P(B)} = P(A) \cdot P(B|A)$$

where $P(B|A)$ represents the probability of event B given that A has occurred.

**Example**: Consider two events, A and B. Suppose we want to find the conditional probability of A given that B has occurred. Using the formula above, we can write:

$$P(A|B) = \frac{P(A \cap B)}{P(B)} = P(A) \cdot P(B|A)$$

### Key Formulas/Theorems

* **Multiplication Rule**: The probability of two events A and B occurring is given by:
$$P(A \cap B) = P(A) \cdot P(B|A)$$
* **Law of Total Probability**: If we have a set of mutually exclusive events {A, B, C}, then the probability of any one of them occurring is given by:
$$P(A \text{ or } B \text{ or } C) = P(A) + P(B) + P(C)$$

### Problem Solving Patterns

**Case Analysis**: When solving conditional probability problems, it's often helpful to break down the problem into cases and analyze each case separately.

*   Identify all possible combinations of events.
*   Compute the probability of each combination using the multiplication rule.
*   Add up the probabilities of all combinations that satisfy the given condition.

### Examples with Solutions

**Example 1**: Indian Premier League has divided the sixteen cricket teams into two equal pools: Pool-A and Pool-B. Four teams of Pool-A have blue logo jerseys, while the rest four have red logo jerseys. Five teams of Pool-B have blue logo jerseys, while the rest three have red logo jerseys.

If one team from each pool reaches the final, what is the probability that one team has a blue logo jersey and another has a red logo jersey?

**Solution**:

Let A be the event that the team from Pool-A has a blue logo jersey, and B be the event that the team from Pool-B has a red logo jersey. We want to compute P(A|B).

Using the definition of conditional probability:

$$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{\frac{1}{2} \cdot \frac{3}{8}}{\frac{5}{8}} = \frac{3}{10}$$

Therefore, the probability that one team has a blue logo jersey and another has a red logo jersey is 0.3.

### Common Pitfalls

*   Failing to identify all possible combinations of events.
*   Misunderstanding the definition of conditional probability.
*   Not using the correct formula for calculating probabilities.

### Quick Summary

*   Definition: P(A|B) = P(A \cap B)/P(B)
*   Key Principle: P(A|B) = P(A) \cdot P(B|A)
*   Multiplication Rule: P(A \cap B) = P(A) \cdot P(B|A)
*   Law of Total Probability
*   Case Analysis: break down the problem into cases and analyze each case separately.

### References

*   None