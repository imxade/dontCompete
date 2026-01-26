**Numerical Ability (General Aptitude)**
=====================================

**Introduction**
---------------

Numerical Ability in GATE CS exam tests your problem-solving skills under time pressure. It involves solving problems that require logical reasoning, pattern recognition, and mathematical calculations. In this theory note, we'll cover the key concepts, formulas, and techniques required to tackle numerical ability questions.

**Core Concepts**
-----------------

### 1. Functions

*   A function is a relation between a set of inputs (called the domain) and a set of possible outputs (called the range).
*   It's denoted by `f(x)` or `g(x)`, where `x` represents the input.

**Key Formulas/Theorems**
-------------------------

### 1. Composition of Functions

Given two functions `f(x)` and `g(x)`, the composition is defined as:

`f(g(x)) = f(u)`

where `u = g(x)`

### 2. Multiplication of Functions

For non-negative integers `p` and `q`,

`f(p,q) = ∑[f(q,p)]up to terms`

`g(p,q) = ∏[g(q,p)]up to terms`

**Problem Solving Patterns**
---------------------------

### 1. Composition of Functions

*   When evaluating `f(g(x))`, focus on identifying the inner function first.
*   Apply the outer function to the result.

**Examples with Solutions**
-------------------------

### 1. Example 1:

`f(p,q) = p^2 + q^2`
`g(p,q) = pq`

Find `f(g(2,3))`.

```mermaid
graph LR
A[Start] --> B[f(g(2,3))]
B --> C[pq]
C --> D[= 2*3 = 6]
D --> E[p^2+q^2]
E --> F[= 4 + 9]
F --> G[=13]
```

`f(g(2,3)) = 4 + 9 = 13`

### 2. Example 2:

`f(p,q) = pq`
`g(p,q) = p^2 + q^2`

Find `f(g(1,2)).`

```mermaid
graph LR
A[Start] --> B[f(g(1,2))]
B --> C[pq]
C --> D[= 1*2 = 2]
D --> E[p^2+q^2]
E --> F[= 1 + 4]
F --> G[=5]
```

`f(g(1,2)) = 5`

**Common Pitfalls**
-------------------

### 1. Incorrect Composition

*   Make sure to identify the inner function correctly.
*   Apply the outer function to the result.

### 2. Missing Terms

*   Double-check for missing terms in the summation or product.

**Quick Summary**
-----------------

| Concept | Description |
| --- | --- |
| Functions | Relation between inputs and outputs |
| Composition of Functions | `f(g(x)) = f(u)` where `u = g(x)` |
| Multiplication of Functions | `f(p,q) = ∑[f(q,p)]up to terms` |

Note: This is a high-yield theory note covering the key concepts, formulas, and techniques required to tackle numerical ability questions. It's essential to practice problems regularly to reinforce your understanding and develop problem-solving skills under time pressure.