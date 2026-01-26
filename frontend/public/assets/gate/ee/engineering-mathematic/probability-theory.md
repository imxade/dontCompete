**Probability Theory**
=======================

### Introduction

Probability theory is a branch of mathematics that deals with the study of events and their likelihood of occurrence. It provides a mathematical framework for modeling random phenomena, making predictions, and quantifying uncertainty. In this note, we will focus on the essential concepts, formulas, and problem-solving techniques required to tackle GATE CS exam questions related to probability theory.

### Core Concepts

*   **Random Experiment**: A random experiment is an action or event that has a well-defined set of possible outcomes.
*   **Sample Space**: The sample space is the collection of all possible outcomes of a random experiment, denoted by Ω (Omega).
*   **Event**: An event is a subset of the sample space. For example, in a coin toss, the event of getting heads can be represented as {H}.
*   **Probability Measure**: A probability measure is a function that assigns a real number between 0 and 1 to each event, denoted by P(E).

### Key Formulas/Theorems

\[ P(E \cup F) = P(E) + P(F) - P(E \cap F) \]

where E and F are events.

\[ P(E') = 1 - P(E) \]

where E' is the complement of event E.

The **Multiplication Rule** states that for two independent events A and B:

\[ P(A \cap B) = P(A) \cdot P(B) \]

### Problem Solving Patterns

To solve probability theory problems, follow these steps:

1.  Clearly define the random experiment, sample space, and events.
2.  Identify any assumptions about independence or conditioning.
3.  Apply relevant formulas and theorems to calculate probabilities.

### Examples with Solutions

**Example 1**

A fair six-sided die is rolled repeatedly until a 6 appears for the first time. What is the expected number of rolls required?

Let X be the random variable representing the number of rolls until a 6 appears. Then:

\[ E[X] = \sum_{x=1}^{\infty} xP(X=x) \]

Since P(6th roll occurs on exactly x-th try) = (5/6)^(x-1)(1/6), we have

\[ E[X] = 1\left(\frac{5}{6}\right)^0 + 2\left(\frac{5}{6}\right)^1 + 3\left(\frac{5}{6}\right)^2 + \cdots \]

This is a geometric series with common ratio (5/6). The expected value can be calculated using the formula for an infinite geometric series:

\[ E[X] = \frac{\text{first term}}{1 - \text{common ratio}} \]

Plugging in the values, we get:

\[ E[X] = \frac{1}{\left(1-\frac{5}{6}\right)} = 6 \]

**Example 2**

Suppose the probability that a coin toss shows "head" is p, where 0 < p < 1. The coin is tossed repeatedly until the first "head" appears. What is the expected number of tosses required?

Let Y be the random variable representing the number of tosses until the first head appears. Then:

\[ E[Y] = \sum_{y=1}^{\infty} yP(Y=y) \]

Since P(head on exactly y-th try) = (1-p)^(y-1)p, we have

\[ E[Y] = 1\left(1-p\right)^0 p + 2\left(1-p\right)^1 p + 3\left(1-p\right)^2 p + \cdots \]

This is a geometric series with common ratio (1-p). The expected value can be calculated using the formula for an infinite geometric series:

\[ E[Y] = \frac{\text{first term}}{1 - \text{common ratio}} \]

Plugging in the values, we get:

\[ E[Y] = \frac{1}{p} \]

### Common Pitfalls

*   **Ignoring Independence**: Failing to recognize that events are independent can lead to incorrect calculations.
*   **Misapplying Formulas**: Incorrectly applying formulas or theorems can result in incorrect answers.

### Quick Summary

Key points:

*   Random experiment and sample space
*   Probability measure and event probability
*   Union, intersection, and complement of events
*   Multiplication rule for independent events
*   Expected value calculation for infinite geometric series