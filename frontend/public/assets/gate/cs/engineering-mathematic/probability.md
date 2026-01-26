**Probability Theory Notes**
==========================

### Introduction
-----------------

Probability theory provides a mathematical framework for quantifying and analyzing uncertainty and randomness. It's a crucial tool in engineering mathematics, enabling us to make informed decisions and predictions about complex systems.

### Core Concepts
------------------

#### 1. Sample Space and Events

*   The **sample space** is the set of all possible outcomes of an experiment.
*   An **event** is any subset of the sample space.

#### 2. Probability Measures

*   A **probability measure**, denoted as P, assigns a non-negative real number to each event in the sample space, representing its likelihood of occurrence.
*   The probability of an event A occurring is written as P(A).
*   Key properties:
    *   Normalization: P(S) = 1, where S is the sample space.
    *   Countable Additivity: For mutually exclusive events A1, A2, ..., P(∪Ai) = ∑P(Ai).

#### 3. Conditional Probability

*   The **conditional probability** of an event A occurring given that event B has occurred is written as P(A|B).
*   It satisfies the property: P(B|A) = P(A|B) / (1 - P(A)), by Bayes' theorem.

#### 4. Independence

*   Two events A and B are **independent** if P(A ∩ B) = P(A)P(B).

### Key Formulas/Theorems
-------------------------

#### 1. Probability of Union

*   The probability of the union of two events A and B is:
    ```latex
    P(A \cup B) = P(A) + P(B) - P(A \cap B)
    ```
    This formula generalizes to any finite number of mutually exclusive events.

#### 2. Bayes' Theorem

*   For events A and B, the conditional probability of A given B is:
    ```latex
    P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
    ```

### Problem Solving Patterns
---------------------------

1.  **Identify Independent Events**: When asked if events are independent, recall the definition and check for equality of their intersection and product probabilities.
2.  **Apply Bayes' Theorem**: Use the theorem to compute conditional probabilities when given probabilities of other events.

### Examples with Solutions
-------------------------

#### Example 1: Permutations

Consider a permutation sampled uniformly at random from the set of all permutations of {1, 2, ..., n} for some n ≥ 4. Let X be the event that 1 occurs before 2 in the permutation, and Y the event that 3 occurs before 4.

We are given that P(X ∩ Y) = 0.5P(X)P(Y). This implies that events X and Y are **independent** because their intersection probability is equal to the product of their individual probabilities.

#### Example 2: Engineering College

A college has 10,000 students. 1,500 like neither their core branches nor other branches. The number of students who like their core branches is 1/4th of the number of students who like other branches. The number of students who like both their core and other branches is 500.

Let's denote C as the set of students who like their core branches, O as those who like other branches. We are given that |C| = 3/4|O|.

We can calculate the total number of students who like either their core or other branches (or both) by using the principle of inclusion-exclusion:

|C ∪ O| = |C| + |O| - |C ∩ O|

Substituting values, we get:
```markdown
|C ∪ O| = 3/4|O| + |O| - |C ∩ O|
       = (7/4)|O| - |C ∩ O|
       = (7/4)(15000) - 500
       = 15750 - 500
       = 15250
```

### Common Pitfalls
-------------------

1.  **Misinterpreting Independence**: Be cautious when applying independence criteria to events.
2.  **Forgetting Conditional Probability Formulae**