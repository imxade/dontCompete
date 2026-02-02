**Probability and Statistics**
==========================

### Introduction
-----------------

Probability and statistics are fundamental tools used to analyze and make decisions based on uncertain events. In this note, we'll cover key concepts, formulas, and problem-solving techniques required for GATE CS exam.

### Core Concepts
------------------

#### Probability

* **Experiment**: A specific action or event with a set of possible outcomes.
* **Sample Space**: The set of all possible outcomes of an experiment.
* **Event**: A subset of the sample space.
* **Probability Measure** (PM): A function that assigns a number between 0 and 1 to each event, representing its likelihood.

#### Random Variables

* **Discrete RV**: Takes on distinct values, e.g., {0, 1, 2, ...}
* **Continuous RV**: Can take any value within a range or interval
* **Probability Distribution** (PD): A function that describes the probability of each possible value of a random variable.

#### Independence

* Two events E and F are **independent** if P(E ∩ F) = P(E) \* P(F)

### Key Formulas/Theorems
---------------------------

**Conditional Probability**
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

**Multiplication Rule**
$$P(A \cap B) = P(A|B) \times P(B)$$

**Bayes' Theorem**
$$P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$$

### Problem Solving Patterns
-----------------------------

#### Probability of Independent Events

When events are independent, the probability of their intersection is simply the product of their individual probabilities.

```mermaid
graph LR
Event A --> Probability of A
Event B --> Probability of B
A ∩ B --> P(A|B) × P(B)
```

#### Poisson Distribution

The Poisson distribution models the number of events occurring within a fixed interval. Its probability mass function is:

$$P(X = k) = \frac{e^{-\lambda} \times (\lambda)^k}{k!}$$

where λ is the average rate of events.

### Examples with Solutions
---------------------------

**Q1: CE 2024-N-36**

A patient has an 80% chance of having a heart attack without medicine X. If medicine X reduces this probability by 50%, what's the probability that a randomly selected patient, out of 100 patients who took medicine X, has a heart attack?

Let A be the event "patient takes medicine X" and B be "patient has a heart attack." We want to find P(A ∩ B).

P(B|A) = 0.5 (medicine reduces probability by 50%)
P(A) = 1/2 (50 patients took medicine out of 100)

Using Bayes' Theorem, we get:

$$P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$$

However, since the patient has an 80% chance of having a heart attack without medicine X, P(B) is actually 0.8.

```python
import math

# Given probabilities
p_B_given_A = 0.5
p_A = 1/2
p_B = 0.8

# Bayes' Theorem
def bayes_theorem(p_B_given_A, p_A, p_B):
    return (p_B_given_A * p_A) / p_B

print("Probability:", bayes_theorem(p_B_given_A, p_A, p_B))
```

Running this code will give us the answer.

### Common Pitfalls
-------------------

* Failing to account for independence between events.
* Misapplying Bayes' Theorem or other probability formulas.
* Not considering the specific context of each question.

### Quick Summary
------------------

| Concept | Key Point |
| --- | --- |
| Probability Measure (PM) | Assigns a number between 0 and 1 to each event, representing its likelihood. |
| Conditional Probability | P(A|B) = P(A ∩ B) / P(B) |
| Multiplication Rule | P(A ∩ B) = P(A|B) × P(B) |
| Bayes' Theorem | P(A|B) = (P(B|A) × P(A)) / P(B) |

This note should provide a solid foundation for tackling probability and statistics questions on the GATE CS exam. Remember to practice problems and review key concepts regularly!