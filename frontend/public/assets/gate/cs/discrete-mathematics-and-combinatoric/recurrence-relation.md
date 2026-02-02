**Recurrence Relations**
=======================

### Introduction

A recurrence relation is a mathematical equation that defines a sequence recursively by relating each term to previous terms. It's an essential tool for solving problems involving recursive sequences, such as Fibonacci numbers or Lucas sequences.

### Core Concepts

*   A recurrence relation typically has the form: $a_n = f(a_{n-1}, a_{n-2}, \ldots, a_0)$
*   The function $f$ can be linear or nonlinear.
*   The sequence $\{a_n\}$ is defined recursively by applying the recurrence relation to each term.

### Key Formulas/Theorems

The Lucas sequence given in the problem can be represented as:

$$L_n = L_{n-1} + L_{n-2}, \text{ for } n \geq 3,$$

with initial conditions $L_1 = 1$ and $L_2 = 3.$

### Problem Solving Patterns

To solve recurrence relations, we can use the following techniques:

1.  **Substitution Method**: Substitute $a_n$ in terms of previous terms into the recurrence relation.
2.  **Induction Method**: Prove the validity of a formula for all positive integers using mathematical induction.

### Examples with Solutions

#### Example 1: Lucas Sequence

The problem provides us with the Lucas sequence defined by:

$$L_n = L_{n-1} + L_{n-2}, \text{ for } n \geq 3,$$

with initial conditions $L_1 = 1$ and $L_2 = 3.$ We need to determine which of the given options is true.

```mermaid
graph LR
A[Given recurrence relation] --> B[Lucas sequence]
B --> C[Initial conditions: L1 = 1, L2 = 3]
C --> D[Option 1: Ln = 5Ln - 4L(n-1) + Ln-2]
D --> E[Option 2: Ln = 5Ln - 3L(n-1) + 2Ln-2]
E --> F[Option 3: Ln = 5Ln - 2L(n-1) + 3Ln-2]
F --> G[Option 4: Ln = 5Ln - 3L(n-1) + Ln-2]
G --> H[Validating each option using the recurrence relation]
```

We can validate each option by putting $n = 1$ and $n = 2$ in the recurrence relation.

*   Option 1:
    *   $L_1 = L_{1-1} + L_{1-2} = L_0 + L_{-1}$
    *   This is not valid since $L_0$ and $L_{-1}$ are undefined.
    *   Therefore, option 1 is incorrect.
*   Option 2:
    *   $L_2 = L_{2-1} + L_{2-2} = L_1 + L_0$
    *   This is also not valid since $L_0$ is undefined.
    *   Therefore, option 2 is incorrect.
*   Option 3:
    *   $L_2 = L_{2-1} + L_{2-2} = L_1 + L_0$
    *   This is also not valid since $L_0$ is undefined.
    *   Therefore, option 3 is incorrect.
*   Option 4:
    *   $L_1 = L_{1-1} + L_{1-2} = L_0 + L_{-1}$
    *   This is not valid since $L_0$ and $L_{-1}$ are undefined.
    *   Therefore, option 4 is incorrect.

However, we can validate the first few terms of the sequence using the recurrence relation. We find that:

$$L_n = \frac{5}{2} L(n-1) - \frac{3}{2} L(n-2).$$

Therefore, the correct answer is option (A).

### Common Pitfalls

*   Students often forget to check for initial conditions and boundary cases.
*   They may also not realize that a recurrence relation can be nonlinear.

### Quick Summary

Recurrence relations are an essential tool in solving problems involving recursive sequences. The key concepts include:

*   Recurrence relations: $a_n = f(a_{n-1}, a_{n-2}, \ldots, a_0)$
*   Substitution method and induction method for solving recurrence relations.
*   Validating each option using the recurrence relation.

By mastering these concepts, students can solve a wide range of problems involving recursive sequences.