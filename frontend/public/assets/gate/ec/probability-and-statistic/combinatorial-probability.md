**Combinatorial Probability**
==========================

**Introduction**
---------------

Combinatorial probability deals with counting and calculating probabilities for various combinations of events. It's a fundamental concept in probability theory, with numerous applications in science, engineering, and finance.

**Core Concepts**
-----------------

### Basic Principles

*   Combinations are the ways to choose items from a set without regard to order.
*   Permutations are the arrangements of items where order matters.
*   Events can be independent or dependent, which affects their probabilities.

### Key Formulas/Theorems

\[
P(A \cup B) = P(A) + P(B) - P(A \cap B)
\]

\[
P(A') = 1 - P(A)
\]

\[
P(\text{at least one of } A, B) = P(A) + P(B) - P(A \cap B)
\]

### Combinatorial Probability

For a random variable $X$ with possible values $\{x_1, x_2, ..., x_n\}$, the probability mass function (PMF) is defined as:

\[P(X=x_i) = p_i\]

where $p_i \geq 0$ and $\sum_{i=1}^{n} p_i = 1$

**Entropy**

The entropy of a random variable $X$, denoted by $H(X)$, measures the uncertainty or randomness in the distribution. It's defined as:

\[H(X) = -\sum_{i=1}^{n} p_i \log_2 p_i\]

For binary random variables like the one in question 22 of GATE 2020, we can simplify this expression:

\[H(X) = -p \log_2 p - (1-p) \log_2 (1-p)\]

### Problem Solving Patterns

When dealing with combinatorial probability problems:

*   Identify the type of problem: combinations or permutations.
*   Use formulas and theorems to calculate probabilities.
*   Consider independence and dependence between events.

**Examples with Solutions**

### Example 1: Binary Random Variable

Suppose we have a binary random variable $X$ that takes values +2 or -2, with probability $\alpha$ for each. We want to find the value of $\alpha$ that maximizes the entropy of $X$.

\[H(X) = -\alpha \log_2 \alpha - (1-\alpha) \log_2 (1-\alpha)\]

To find the maximum, we take the derivative with respect to $\alpha$ and set it equal to zero:

\[\frac{dH}{d\alpha} = -\frac{\ln 2}{\alpha} + \frac{\ln 2}{1-\alpha} = 0\]

Solving for $\alpha$, we get:

\[\alpha = 0.5\]

### Example 2: High School Students

In a high school with equal numbers of boy and girl students, 75% study science and 25% study commerce. Commerce students are two times more likely to be boys than science students.

Let's calculate the probability that a randomly selected girl student studies commerce.

## Step 1
First, we need to find the number of girls studying commerce.

## Step 2
Let's assume there are x girls studying science and y girls studying commerce. Then we have:

\[x + y = 0.25 \times (n/2)\]

where n is the total number of students.

## Step 3
Since commerce students are two times more likely to be boys than science students, we can write an equation based on this information.

## Step 4
Now, let's calculate the probability that a randomly selected girl student studies commerce.

\[P(\text{girl studies commerce}) = \frac{\text{number of girls studying commerce}}{\text{total number of girls}}\]

### Quick Summary

*   Combinatorial probability deals with counting and calculating probabilities for various combinations of events.
*   Entropy measures the uncertainty or randomness in a distribution.
*   Binary random variables can be used to model different types of problems.

This concludes our comprehensive theory note on combinatorial probability.