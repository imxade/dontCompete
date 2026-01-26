# Error Analysis in Numerical Methods
=====================================

## Introduction
---------------

Error analysis is a crucial aspect of numerical methods, as it helps us understand and quantify the errors that arise during computations. This concept is essential for evaluating the accuracy and reliability of numerical solutions.

## Core Concepts
-----------------

*   **Numerical error**: The difference between the exact solution and the approximate solution obtained using a numerical method.
*   **Truncation error**: The error introduced by approximating an infinite series or a continuous function with a finite number of terms.
*   **Round-off error**: The error introduced due to rounding off intermediate results during computation.

### Truncation Error

The truncation error is defined as:

$$ E_T = \lim_{h \to 0} |f(x) - f_h(x)| $$

where $f(x)$ is the exact solution and $f_h(x)$ is the approximate solution obtained using a numerical method with step size $h$.

### Round-off Error

The round-off error is defined as:

$$ E_R = \lim_{n \to \infty} |x_n - x| $$

where $x_n$ is the approximated value and $x$ is the exact value.

## Key Formulas/Theorems
---------------------------

*   **Turing's formula** for estimating truncation error:

$$ E_T \leq Ch^p $$

where $C$ is a constant, $h$ is the step size, and $p$ is the order of accuracy.
```latex
\begin{align}
E_T &\leq Ch^p \\
\end{align}
```
*   **Round-off error formula**:

$$ E_R = \left| \prod_{i=1}^{n} (1 + r_i) - 1 \right| $$

where $r_i$ is the round-off factor at each step.

## Problem Solving Patterns
-----------------------------

When solving problems related to error analysis, follow these steps:

1.  **Identify the type of error**: Determine whether it's a truncation error or a round-off error.
2.  **Apply relevant formulas**: Use Turing's formula or the round-off error formula as needed.
3.  **Analyze the effect of parameters**: Consider how step size, order of accuracy, and round-off factors affect the error.

## Examples with Solutions
---------------------------

### Example 1: Truncation Error

Suppose we want to approximate $e^x$ using a Taylor series expansion up to the third term. Find the truncation error for $x = 2$.

```python
import math

def taylor_expansion(x, n):
    return sum([math.pow(x, i) / math.factorial(i) for i in range(n)])

x = 2
n = 3
approximation = taylor_expansion(x, n)
exact_value = math.exp(x)

truncation_error = abs(exact_value - approximation)
print("Truncation error:", truncation_error)
```

### Example 2: Round-off Error

Suppose we want to find the sum of an infinite geometric series with first term $a$ and common ratio $r$. Find the round-off error if we approximate the sum using a finite number of terms.

```python
import math

def geometric_series(a, r, n):
    return a * (1 - math.pow(r, n)) / (1 - r)

a = 2
r = 0.5
n = 100

approximation = geometric_series(a, r, n)
exact_value = a / (1 - r)

round_off_error = abs(exact_value - approximation)
print("Round-off error:", round_off_error)
```

## Common Pitfalls
------------------

*   **Forgetting to account for rounding errors**: Always consider the effect of rounding on intermediate results.
*   **Using an incorrect formula or algorithm**: Double-check your calculations and ensure you're using the correct formulas and algorithms.

## Quick Summary
---------------

| Concept | Description |
| --- | --- |
| Truncation Error | Difference between exact solution and approximate solution due to approximation. |
| Round-off Error | Difference between exact value and approximated value due to rounding. |
| Turing's Formula | Estimating truncation error using step size and order of accuracy. |
| Round-off Error Formula | Calculating round-off error as a product of round-off factors. |

Note: This summary is not exhaustive, but it covers the main points discussed in this theory note.

By following this comprehensive guide to error analysis in numerical methods, you'll be well-prepared to tackle questions like Q1 and Q2 from previous year exams. Remember to practice solving problems and exercises to reinforce your understanding of these concepts.