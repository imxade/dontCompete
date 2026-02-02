**Eigenvalues and Eigenvectors**
=============================

### Introduction
Eigenvectors and eigenvalues are fundamental concepts in linear algebra that describe the behavior of linear transformations. In this note, we will explore the theoretical aspects of eigenvectors and eigenvalues.

### Core Concepts

#### Definition
*   **Eigenvector**: A non-zero vector `v` is an eigenvector of a matrix `A` if there exists a scalar λ (eigenvalue) such that `Av = λv`.
*   **Eigenvalue**: The scalar λ associated with an eigenvector `v` in the equation `Av = λv`.

#### Properties

*   **Non-zero eigenvalues**: Eigenvalues can be zero or non-zero. Non-zero eigenvalues indicate a scaling of the vector, while zero eigenvalues imply that the matrix is singular.
*   **Eigenvalue multiplicity**: An eigenvalue can have multiple associated eigenvectors, which are said to be linearly independent.

#### Diagonalization
A square matrix `A` can be diagonalized if it has a full set of distinct eigenvalues and corresponding eigenvectors. This process involves transforming the matrix into a diagonal form using its eigenvectors as a basis.

### Key Formulas/Theorems

```latex
\begin{align*}
|A - \lambda I| &= 0 \\
(A - \lambda I)v &= 0
\end{align*}
```

The first equation is the characteristic polynomial, and the second represents the eigenvector equation. Solving these equations will yield the eigenvalues and corresponding eigenvectors of `A`.

### Problem Solving Patterns

1.  **Find eigenvalues**: Solve the characteristic polynomial to obtain the eigenvalues.
2.  **Compute eigenvectors**: Use the eigenvector equation to solve for the associated vectors.

### Examples with Solutions

#### Example 1: Compute Eigenvalues and Eigenvectors
Given:
\[ A = \begin{bmatrix}
2 & 1 \\
6 & -3
\end{bmatrix} \]

*   **Step 1**: Find eigenvalues by solving the characteristic polynomial.
    \[ |A - \lambda I| = 0 \]
    Solving for λ, we get:
    \[ (\lambda + 3)(\lambda - 2) = 0 \]
    Eigenvalues: λ = -3, λ = 2

*   **Step 2**: Compute eigenvectors using the eigenvector equation.
    For λ = -3:
    \[ (A + 3I)v = 0 \]
    Solving for `v`, we get an eigenvector `(-1, -2)`.

#### Example 2: Diagonalization

Given:
\[ A = \begin{bmatrix}
4 & 2 \\
2 & 1
\end{bmatrix} \]

*   **Step 1**: Find eigenvalues by solving the characteristic polynomial.
    Eigenvalues: λ = 3, λ = 0 (zero eigenvalue indicates singularity)

*   **Step 2**: Compute eigenvectors using the eigenvector equation. For λ = 3:
    Solving for `v`, we get an eigenvector `(1, 1)`.

### Common Pitfalls

1.  **Overlooking zero eigenvalues**: Failure to recognize that a matrix is singular or has non-trivial null space.
2.  **Incorrect computation of eigenvectors**: Forgetting to normalize eigenvectors or using incorrect methods for eigendecomposition.

### Quick Summary
*   Eigenvalues are scalar values associated with linear transformations (eigenvalue equation: `Av = λv`).
*   Eigenvectors are non-zero vectors that describe the direction and magnitude of these scalars.
*   Diagonalization is possible when a matrix has distinct eigenvalues and corresponding eigenvectors.

**References**

For further study:

*   [1] **Linear Algebra and Its Applications**, Gilbert Strang
*   [2] **The Matrix Cookbook**, Paul I. Davis and Manfred Schroeder

Note: This note provides an introduction to the concepts of eigenvalues and eigenvectors, their computation, and application in linear algebra.