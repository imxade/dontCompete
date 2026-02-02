**Numerical Ability Theory Note**
=====================================

**Introduction**
---------------

Numerical ability is a crucial component of the GATE CS exam, testing your ability to solve problems involving numbers, patterns, and logical reasoning. This note covers essential concepts, formulas, and problem-solving strategies to help you tackle numerical ability questions.

**Core Concepts**
-----------------

### Frequency Distribution

*   A frequency distribution is a table or chart that displays the frequency of each value in a dataset.
*   It helps identify patterns, modes, and outliers.

### Mean, Median, Mode

*   **Mean**: The average value of a dataset. Calculated by summing all values and dividing by the number of values (Σx / n).
*   **Median**: The middle value of a sorted dataset. If there are an even number of values, it's the average of the two middle values.
*   **Mode**: The most frequently occurring value in a dataset.

### Invertible Matrices

*   A square matrix is invertible if its determinant is non-zero.
*   The inverse of a 2x2 matrix [a, b; c, d] can be calculated using the formula:

$$\frac{1}{ad - bc} \begin{bmatrix}d &amp; -b \\-c &amp; a\end{bmatrix}$$

### Probability

*   The probability of an event is the number of favorable outcomes divided by the total number of possible outcomes.

**Key Formulas/Theorems**
-------------------------

### Mean, Median, Mode Relationship

Given a frequency distribution:

| Value | Frequency |
| --- | --- |
| 10    | 3        |
| 11    | 2        |
| ...   | ...      |

The mode is the value with the highest frequency. The median can be found by sorting the values and selecting the middle one (or averaging if there are an even number of values). The mean is calculated using the formula: (Σx \* f) / Σf, where x is the value and f is its frequency.

### Probability Formula

P(A or B) = P(A) + P(B) - P(A and B)

**Problem Solving Patterns**
---------------------------

### Frequency Distribution

When analyzing a frequency distribution:

1.  Identify the mode by finding the most frequent value.
2.  Sort the values to find the median (or average if there are an even number of values).
3.  Calculate the mean using the formula: (Σx \* f) / Σf.

### Invertible Matrices

When dealing with invertible matrices:

1.  Check if the determinant is non-zero.
2.  If it's non-zero, calculate the inverse using the formula:
    $$\frac{1}{ad - bc} \begin{bmatrix}d &amp; -b \\-c &amp; a\end{bmatrix}$$

### Probability

When solving probability questions:

1.  Calculate the number of favorable outcomes.
2.  Divide by the total number of possible outcomes.

**Examples with Solutions**
-------------------------

### Example 1: Frequency Distribution

| Value | Frequency |
| --- | --- |
| 10    | 3        |
| 11    | 2        |

Find the mode, median, and mean:

Mode: The value with the highest frequency is 10 (mode = 10).

Median: Sorting the values, we find the median is between 10 and 11. Since there are an even number of values, we average them: (10 + 11) / 2 = 10.5.

Mean: Using the formula (Σx \* f) / Σf:

(10 \* 3 + 11 \* 2) / (3 + 2) = (30 + 22) / 5 = 52/5 = 10.4

### Example 2: Invertible Matrices

Given the matrix [a, b; c, d]:

Calculate its inverse:

Inverse = (1 / (ad - bc)) \* [d, -b; -c, a]

### Example 3: Probability

A fair coin is flipped twice. What's the probability of getting exactly one head?

Number of favorable outcomes = 2 (HHT, HTH)

Total number of possible outcomes = 4 (HHH, HHT, THH, TTT)

Probability = Number of favorable outcomes / Total number of possible outcomes = 2/4 = 1/2

**Common Pitfalls**
------------------

*   Failing to identify the mode in a frequency distribution.
*   Calculating the mean incorrectly using the formula: (Σx) / n instead of (Σx \* f) / Σf.
*   Assuming a matrix is invertible without checking its determinant.

**Quick Summary**
----------------

*   Frequency Distribution:
    + Mode = most frequent value
    + Median = middle value (or average if an even number)
    + Mean = (Σx \* f) / Σf
*   Invertible Matrices:
    + Check determinant (ad - bc ≠ 0)
    + Calculate inverse using formula: (1 / (ad - bc)) \* [d, -b; -c, a]
*   Probability:
    + Number of favorable outcomes ÷ Total number of possible outcomes