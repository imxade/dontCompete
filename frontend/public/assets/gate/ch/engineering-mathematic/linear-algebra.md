# Linear Algebra Theory Note
## Introduction
Linear algebra is a branch of mathematics that deals with the study of linear equations, vector spaces, and linear transformations. It is a fundamental tool for solving systems of linear equations, finding the inverse of matrices, and determining the eigenvalues and eigenvectors of matrices.

## Core Concepts

### Vector Spaces
A vector space is a set of vectors that can be added together and scaled by numbers. The key properties of a vector space are:

* Closure under addition: For any two vectors `u` and `v`, their sum `u + v` is also in the vector space.
* Commutativity of addition: `u + v = v + u`
* Associativity of addition: `(u + v) + w = u + (v + w)`
* Existence of additive identity: There exists a vector `0` such that `u + 0 = u`
* Existence of additive inverse: For each vector `u`, there exists a vector `-u` such that `u + (-u) = 0`

### Linear Transformations
A linear transformation is a function between vector spaces that preserves the operations of vector addition and scalar multiplication. The key properties of a linear transformation are:

* Linearity: `T(u + v) = T(u) + T(v)` and `T(cu) = cT(u)`
* Injectivity: If `T(u) = T(v)`, then `u = v`
* Surjectivity: For each vector `v` in the codomain, there exists a vector `u` in the domain such that `T(u) = v`

### Matrices
A matrix is a rectangular array of numbers. The key properties of a matrix are:

* Rows and columns: A matrix has rows and columns, denoted by `m x n`
* Addition and multiplication: Matrices can be added together and multiplied by scalars or other matrices.

## Key Formulas/Theorems

### Determinant
The determinant of an `n x n` matrix `A` is denoted by `|A|`. It can be calculated using the formula:

$$
|A| = \begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix}
$$

### Rank
The rank of an `n x n` matrix `A` is denoted by `r`. It can be calculated using the formula:

$$
r = \begin{cases}
0, & \text{if } |A| = 0 \\
1, & \text{if } |A| \neq 0 \text{ and } A \text{ has a single row or column} \\
2, & \text{if } |A| \neq 0 \text{ and } A \text{ has two rows or columns} \\
\vdots & \\
n, & \text{if } |A| \neq 0 \text{ and } A \text{ is invertible}
\end{cases}
$$

## Problem Solving Patterns

### Non-Trivial Solution
For a non-trivial solution to exist in the system of equations `Ax = 0`, where `A` is an `n x n` matrix, we need to satisfy the condition:

$$
r < n
$$

This implies that the determinant of `A` must be zero:

$$
|A| = 0
$$

### Determinant Calculation
The determinant of a square matrix can be calculated using the formula:

$$
|A| = \sum_{i=1}^{n} (-1)^{i+j} a_{ij} M_{ij}
$$

where `M_ij` is the minor of element `a_ij`.

## Examples with Solutions

### Example 1: Non-Trivial Solution
Consider the system of equations:

$$
\begin{bmatrix}
2 & 3 \\
4 & 5
\end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

To find a non-trivial solution, we need to satisfy the condition:

$$
r < n
$$

Since `|A| = 10 - 12 = -2`, we have:

$$
r < 2
$$

This implies that a non-trivial solution exists.

### Example 2: Determinant Calculation
Consider the matrix:

$$
A = \begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
$$

To calculate the determinant of `A`, we can use the formula:

$$
|A| = \sum_{i=1}^{n} (-1)^{i+j} a_{ij} M_{ij}
$$

## Common Pitfalls

* Forgetting to check the rank of the matrix.
* Misinterpreting the determinant as the solution to the system of equations.

## Quick Summary

* Vector spaces: Closure under addition, commutativity of addition, associativity of addition, existence of additive identity, and existence of additive inverse.
* Linear transformations: Linearity, injectivity, and surjectivity.
* Matrices: Rows and columns, addition, and multiplication.
* Determinant: Formula for calculating the determinant.
* Rank: Formula for calculating the rank.

Note: This is a basic outline of linear algebra concepts. For more advanced topics and detailed explanations, please refer to a comprehensive linear algebra textbook.