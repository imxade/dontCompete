**Combinatorial Probability**
==========================

**Introduction**
---------------

Combinatorial probability deals with counting and calculating probabilities of events in experiments involving random selection, arrangements, or combinations. This topic is crucial for understanding various real-world applications, including statistical analysis, data science, and engineering.

**Core Concepts**
-----------------

### Independent Events

Two events A and B are independent if the occurrence or non-occurrence of one does not affect the probability of the other.

*   Probability of A and B: P(A ∩ B) = P(A) × P(B)

### Dependent Events

Two events A and B are dependent if the occurrence or non-occurrence of one affects the probability of the other.

*   Probability of A and B: P(A ∩ B) ≠ P(A) × P(B)

**Key Formulas/Theorems**
-------------------------

### Probability Mass Function (PMF)

The PMF of a random variable X is defined as:

P(X = x) = P(x)

where x is the outcome, and P(x) is the probability of that outcome.

### Binomial Coefficient

The binomial coefficient is used to calculate the number of ways to choose k items from n items without repetition:

C(n, k) = n! / (k!(n-k)!)

### Combinations and Permutations

*   Number of combinations: C(n, k) = n! / (k!(n-k)!)
*   Number of permutations: P(n, k) = n! / (n-k)!

**Problem Solving Patterns**
---------------------------

When dealing with combinatorial probability, consider the following steps:

1.  Identify the type of problem (independent or dependent events)
2.  Determine the total number of outcomes
3.  Calculate the probability of each outcome
4.  Combine probabilities using the multiplication rule for independent events

**Examples with Solutions**
---------------------------

### Example 1: Independent Events

A box contains 5 red balls and 3 blue balls. If one ball is randomly selected, what is the probability that it is red?

Solution:

*   Total number of outcomes = 8 (5 red + 3 blue)
*   Probability of selecting a red ball = P(R) = 5/8

### Example 2: Dependent Events

A coin has two sides: heads and tails. If one side lands facing up, what is the probability that the other side will also land facing up?

Solution:

*   Let's denote the event of the first side landing facing up as A.
*   The probability of the second side landing facing up given that A occurred = P(B|A) = 1/2 (since it's a fair coin)

**Common Pitfalls**
------------------

*   Assuming independent events are always mutually exclusive
*   Failing to consider dependent events

**Quick Summary**
-----------------

*   Combinatorial probability deals with counting and calculating probabilities of events in experiments involving random selection, arrangements, or combinations.
*   Independent events: P(A ∩ B) = P(A) × P(B)
*   Dependent events: P(A ∩ B) ≠ P(A) × P(B)
*   Key formulas include PMF, binomial coefficient, and combinations/permutations.

Note:
Please let me know if you need any adjustments or want to proceed with the next topic.