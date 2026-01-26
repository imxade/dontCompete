**Asymptotic Worst Case Time and Space Complexity**
=====================================================

### Introduction

In the analysis of algorithms, it's essential to understand how an algorithm's time and space complexity grow as the input size increases. Asymptotic notation provides a concise way to express these complexities.

### Core Concepts

#### Big O Notation

Big O notation represents the upper bound of an algorithm's time or space complexity. It describes the worst-case scenario, which is the maximum amount of resources (time or space) required by the algorithm as the input size grows.

*   Big O notation is denoted using the "O" symbol, followed by a function of n (e.g., O(n), O(log n)).
*   Big O notation is used to express an upper bound on the time or space complexity of an algorithm.
*   To determine the big O notation of an algorithm, we must identify the term with the highest degree of n.

#### Big Ω Notation

Big Ω notation represents the lower bound of an algorithm's time or space complexity. It describes the best-case scenario, which is the minimum amount of resources (time or space) required by the algorithm as the input size grows.

*   Big Ω notation is denoted using the "Ω" symbol, followed by a function of n (e.g., Ω(n), Ω(log n)).
*   Big Ω notation is used to express a lower bound on the time or space complexity of an algorithm.
*   To determine the big Ω notation of an algorithm, we must identify the term with the lowest degree of n.

#### Theta Notation

Theta notation represents the exact time or space complexity of an algorithm. It describes both the upper and lower bounds of the algorithm's resources requirements as the input size grows.

*   Theta notation is denoted using the "θ" symbol, followed by a function of n (e.g., θ(n), θ(log n)).
*   To determine the theta notation of an algorithm, we must identify both the highest and lowest degrees of n.

### Key Formulas/Theorems

*   **Master Theorem**: A formula used to solve recurrence relations.
    $$
    T(n) = \begin{cases}
        O(n^d) & \text{if } f(n) = \Theta(n^d \log^n), \text{ where } d > 0 \\
        O(n^d) & \text{if } f(n) = O(n^d), \text{ and } T(n/f(n)) = O(1) \\
        O(f(n)^{log_f n d}) & \text{otherwise}
    \end{cases}$$
*   **Recurrence Relations**: A formula that defines a function recursively.

### Problem Solving Patterns

When solving problems related to asymptotic notation, follow these steps:

1.  Identify the type of problem: big O, big Ω, or theta.
2.  Determine the input size (n).
3.  Analyze the algorithm's time and space complexity.
4.  Use big O notation to express an upper bound on the time or space complexity.
5.  If necessary, use big Ω notation to express a lower bound.

### Examples with Solutions

#### Example 1: Big O Notation

Suppose we have an algorithm that iterates over an array of size n, and for each element, it performs a constant number of operations. What is the big O notation of this algorithm?

*   **Step 1:** Identify the type of problem: big O.
*   **Step 2:** Determine the input size (n): The size of the array.
*   **Step 3:** Analyze the algorithm's time complexity: Since each element requires a constant number of operations, the total time complexity is directly proportional to the size of the array.
*   **Step 4:** Use big O notation to express an upper bound on the time complexity.

The final answer is: $\boxed{O(n)}$

#### Example 2: Recurrence Relations

Consider the recurrence relation:

$$
T(n) = \begin{cases}
    T(n/2) + n & \text{if } n \geq 1 \\
    c & \text{otherwise}
\end{cases}$$

*   **Step 1:** Identify the type of problem: solving a recurrence relation using the Master Theorem.
*   **Step 2:** Determine the input size (n): The value of n in the recurrence relation.
*   **Step 3:** Analyze the recurrence relation: We have a function that calls itself recursively, and each call adds a term proportional to n.
*   **Step 4:** Use the Master Theorem to solve the recurrence relation.

The final answer is: $\boxed{O(n \log n)}$

### Common Pitfalls

When working with asymptotic notation:

*   Be careful when using big O notation, as it represents an upper bound on the time or space complexity.
*   When solving recurrence relations, make sure to identify the correct pattern and apply the Master Theorem correctly.

### Quick Summary

| Notation | Description |
| --- | --- |
| Big O (O) | Upper bound on time or space complexity |
| Big Ω (Ω) | Lower bound on time or space complexity |
| Theta (θ) | Exact time or space complexity |

Asymptotic notation is a powerful tool for analyzing algorithms' time and space complexities. By understanding big O, big Ω, and theta notations, you can write more efficient code and make informed decisions about algorithm design.