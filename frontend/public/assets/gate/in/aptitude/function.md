**Function Theory Note**
==========================

### Introduction
---------------

Functions are a fundamental concept in mathematics and computer science. They represent a relationship between inputs (domain) and outputs (range). In this note, we'll cover the theoretical aspects of functions as tested in GATE CS.

### Core Concepts
-----------------

#### Definition of Function
A function f: A → B is a relation from set A to set B that assigns each element x ∈ A exactly one element y ∈ B. It can be denoted as f(x) = y or x ↦ y.

**Mermaid Diagram**
```mermaid
graph LR;
    A[Domain] -->|f|> B[Range];
```
#### Types of Functions

*   **Injective (One-to-One)**: For every y ∈ B, there is at most one x ∈ A such that f(x) = y.
*   **Surjective (Onto)**: For every y ∈ B, there exists an x ∈ A such that f(x) = y.
*   **Bijective**: A function that is both injective and surjective.

#### Function Composition
Composition of functions g ∘ f means apply f first and then apply g to the result. This can be denoted as (g ∘ f)(x) = g(f(x)).

### Key Formulas/Theorems
---------------------------

*   **Function Equation**: If f(x) = y, then x ∈ domain of f and y ∈ range of f.
*   **Inverse Function**: A function has an inverse if it is bijective. The inverse of a function f is denoted as f⁻¹.

### Problem Solving Patterns
-----------------------------

1.  **Simplify the expression**: Before solving, simplify the given expression to make it easier to handle.
2.  **Use function properties**: Use the properties of functions like injectivity and surjectivity to simplify the problem.

### Examples with Solutions
---------------------------

**Example 1:**
Find the value of (λ(3/2, 2/3)) where λ(p, q) = p + q if p ≥ λ or λ(p, q) = pq if p < λ.

```latex
\begin{align*}
\lambda\left(\frac{3}{2}, \frac{2}{3}\right) &= \frac{3}{2} + \frac{2}{3} \\
&= \frac{9+4}{6} \\
&= \frac{13}{6} > \frac{1}{2}
\end{align*}
```

Therefore, λ(3/2, 2/3) = (3/2)(2/3) = 2/3.

**Example 2:**
Find the value of ((2, 1)) where λ(p, q) = p - q if p ≥ λ or λ(p, q) = pq if p < λ.

```latex
\begin{align*}
\lambda(2, 1) &= 2-1 \\
&= 1 > \frac{1}{2}
\end{align*}
```

Therefore, λ(2, 1) = (2)(1) = 2.

### Common Pitfalls
--------------------

*   **Forgetting to check the domain**: Always check if the input is in the domain of the function.
*   **Not checking for bijectivity**: A function must be bijective to have an inverse.

### Quick Summary
------------------

*   Definition of a function and its types (injective, surjective, bijective)
*   Function composition
*   Inverse function
*   Simplifying expressions using function properties

This note covers the theoretical aspects of functions as tested in GATE CS. It includes examples with solutions to illustrate key concepts.