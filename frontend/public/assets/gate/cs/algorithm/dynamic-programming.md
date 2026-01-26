**Dynamic Programming**
=======================

### Introduction
-----------------

Dynamic programming (DP) is an algorithmic paradigm used to solve problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing their results to avoid redundant computation. This approach is particularly useful for optimization problems where the problem can be decomposed into smaller sub-problems.

### Core Concepts
-----------------

*   **Memoization**: Storing the solutions to sub-problems in a memory (usually an array or matrix) so that they don't have to be recomputed every time they are encountered.
*   **Bottom-up Approach**: Start with the smallest possible subproblems and iteratively combine them to solve larger problems.
*   **Tabulation**: Building up a table of solutions for sub-problems in a bottom-up manner.

### Key Formulas/Theorems
-------------------------

None specific to dynamic programming, as it is more of an algorithmic paradigm than a mathematical theory. However, we can state the general property that dynamic programming problems have: The problem can be broken down into smaller subproblems, and the optimal solution to the larger problem depends on the optimal solutions to these sub-problems.

### Problem Solving Patterns
---------------------------

*   **Optimization with Constraints**: Find the maximum or minimum value under given constraints.
*   **Counting Problems**: Count the number of ways to achieve a certain goal.
*   **Shortest/Longest Paths**: Find the shortest or longest path between two nodes in a graph.

### Examples with Solutions
---------------------------

**Example 1: Rod Cutting Problem**

Suppose we have a rod of length `n` meters, and we want to cut it into pieces of integer lengths to maximize our revenue. The prices for each piece are given by the array `p = [l, 5, 8, 9, 10, 17, 13]`.

```python
def rod_cutting(p, n):
    dp = [0] * (n + 1)  # Initialize DP table

    # Fill up the DP table in a bottom-up manner
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, i + 1):
            max_val = max(max_val, p[j] + dp[i - j])
        dp[i] = max_val

    return dp[n]
```

In this example, we use a bottom-up approach to fill up the DP table. We iterate over each possible length `i` and for each `i`, we consider all possible cuts (from 1 to `i`) and choose the one that maximizes our revenue.

**Example 2: Fibonacci Series**

The Fibonacci series is a classic example of dynamic programming. It can be defined recursively as:

`F(n) = F(n-1) + F(n-2)` for `n >= 2`

However, this recursive definition leads to a lot of redundant computation. We can use memoization to store the values of `F(i)` in an array and avoid recomputing them.

```python
def fibonacci(n):
    dp = [0] * (n + 1)
    dp[1] = 1

    # Fill up the DP table in a bottom-up manner
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

### Common Pitfalls
-------------------

*   **Not using memoization**: Failing to store the solutions to sub-problems leads to a lot of redundant computation.
*   **Not initializing DP table correctly**: Incorrectly initialized DP tables can lead to incorrect results.

### Quick Summary
----------------

Dynamic programming is an algorithmic paradigm that solves problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing their results to avoid redundant computation. It is particularly useful for optimization problems where the problem can be decomposed into smaller sub-problems. The key concepts include memoization, bottom-up approach, and tabulation.

**Visuals**
------------

No visuals are required for this topic as it is a purely algorithmic concept.