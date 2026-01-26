# Eigenvalue
================

## Introduction
-------------

Eigenvalues are scalar values that represent how much change occurs in a linear transformation. They play a crucial role in understanding the properties of matrices, including diagonalization and eigenvector decomposition.

## Core Concepts
----------------

### Definition

*   The eigenvalue ($\lambda$) is a scalar value associated with an eigenvector (v) of a matrix A, satisfying the equation:

$$Av = \lambda v$$

### Characteristic Equation

The characteristic equation is obtained by det(A - λI) = 0, where I is the identity matrix.

$$det(A - \lambda I) = 0$$

### Eigenvectors and Eigenvalues

Eigenvectors (v) are non-zero vectors that, when multiplied by a matrix A, result in a scaled version of themselves. The scaling factor is called the eigenvalue ($\lambda$).

## Key Formulas/Theorems
-------------------------

*   **Characteristic Equation**: det(A - λI) = 0

    $$det(A - \lambda I) = (-\lambda)^n + b_{n-1}(-\lambda)^{n-1} + ... + b_1(-\lambda) + b_0$$

    Where n is the dimension of the matrix, and $b_i$ are coefficients.

*   **Eigenvalue Equation**: Av = λv

## Problem Solving Patterns
---------------------------

### Finding Eigenvalues

To find eigenvalues, we need to solve the characteristic equation det(A - λI) = 0. We can use various methods such as:

1.  **Method 1: Using the determinant**
    ```mermaid
    graph LR
    A[Matrix A] --> B[Subtract λI from A]
    C[Determinant of (A-λI)] --> D=0
    ```
2.  **Method 2: Finding the characteristic polynomial**

### Finding Eigenvectors

Once we have found the eigenvalues, we can find the corresponding eigenvectors by solving the equation Av = λv.

## Examples with Solutions
---------------------------

### Example 1: Find the eigenvalues of matrix A = [[2, 1], [3, 4]]

We first need to find the characteristic equation:

```latex
det(A - λI) =
| (2-λ)  1 |
| 3     (4-λ) |
= -(λ^2 - 6λ + 5)
```

Setting det(A - λI) = 0, we get:

$$-(λ^2 - 6λ + 5) = 0$$

Solving for λ, we get two eigenvalues: λ1 = 3 and λ2 = 5/2.

### Example 2: Find the eigenvectors of matrix A corresponding to the eigenvalue λ = 3

To find the eigenvector, we need to solve the equation Av = λv:

$$Av = \begin{bmatrix} 2 & 1 \\ 3 & 4 \end{bmatrix} v = 3v$$

Let v = [x, y]. Then:

$$\begin{bmatrix} 2 & 1 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = 3 \begin{bmatrix} x \\ y \end{bmatrix}$$

Solving for x and y, we get:

v = [1, -2]

## Common Pitfalls
------------------

*   **Incorrect calculation of the determinant**
*   **Failure to identify the correct eigenvalues**
*   **Insufficient or incorrect solving of eigenvectors**

## Quick Summary
-----------------

*   **Definition**: Eigenvalue is a scalar value associated with an eigenvector.
*   **Characteristic Equation**: det(A - λI) = 0
*   **Finding Eigenvalues**: Solve the characteristic equation to find eigenvalues.
*   **Finding Eigenvectors**: Solve the equation Av = λv for each eigenvalue.

Note: This is a comprehensive theory note on eigenvalues and eigenvectors. It covers the core concepts, key formulas/theorems, problem-solving patterns, examples with solutions, common pitfalls, and quick summary.