**Random Variable**
====================
### Introduction
A random variable is a mathematical representation of a set of possible values that a random event can take on. In probability and statistics, it's essential to understand random variables as they form the foundation for modeling real-world phenomena.

### Core Concepts
#### Types of Random Variables
There are two types:

*   **Discrete Random Variable**: A variable that takes on distinct, countable values.
*   **Continuous Random Variable**: A variable that can take any value within a given range or interval.

#### Probability Distribution Functions (PDF)
A PDF is a mathematical function used to describe the probability distribution of a random variable. For discrete variables, it's denoted as P(X = x) and for continuous variables, it's denoted as f(x).

### Key Formulas/Theorems

**Uniform Distribution**
A uniform distribution is a special case where every value within a given range has an equal probability.

$$f(x) = \begin{cases}
\frac{1}{b-a} & \text{if }a \leq x \leq b \\
0 & \text{otherwise}
\end{cases}$$

**Expected Value (E(X))**
The expected value of a random variable is the long-run average value it's expected to take.

$$E(X) = \int_{-\infty}^{\infty} xf(x)dx$$

### Problem Solving Patterns
When dealing with continuous uniform distributions, we often need to find probabilities or values within specific ranges. The following pattern can be useful:

1.  **Identify the type of distribution**: Uniform in this case.
2.  **Determine the range**: Given as (a, b) for X and (c, d) for Y.
3.  **Apply the formula**: Use the uniform distribution PDF to calculate probabilities.

### Examples with Solutions

#### Q1 Solution
Given X ~ U(2,3) and Y ~ U(1,4), find P(Y < X).

Using the uniform distribution PDF, we can rewrite this as:

P(Y < X) = ∫[1, 4] (1/3 - 1/2) dy

= (1/6) \* (4 - 1)

= 0.5

#### Example: 
Suppose X ~ U(0,10), find E(X).

Using the uniform distribution PDF:

E(X) = ∫[0,10] x \* (1/10) dx

= (1/20) \* [x^2] from 0 to 10

= (1/20) \* (100 - 0)

= 5

### Common Pitfalls
When working with continuous distributions:

*   **Avoid confusion between discrete and continuous variables**.
*   **Use the correct PDF or CDF for each variable**.

### Quick Summary
\*   **Random Variable**: Mathematical representation of possible values for a random event
\*   **Discrete vs Continuous**: Discrete takes distinct, countable values; Continuous can take any value within a range
\*   **Probability Distribution Function (PDF)**: Describes probability distribution of a variable
\*   **Uniform Distribution**: Every value has equal probability within a given range