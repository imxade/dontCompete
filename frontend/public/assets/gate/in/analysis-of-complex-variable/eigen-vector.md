# Eigen Vectors in Analysis of Complex Variables
====================================================

## Introduction

In the analysis of complex variables, eigen vectors play a crucial role in understanding the behavior of linear transformations. An eigen vector of a matrix A is a non-zero vector v such that Av = λv for some scalar λ, which is called an eigenvalue.

## Core Concepts

### Eigen Values and Vectors

Let A be a square matrix of size n x n. The characteristic equation of A is given by:

|A - λI| = 0

where I is the identity matrix of size n x n.

The roots of this equation are called the eigenvalues of A, denoted as λ1, λ2, ..., λn. For each eigenvalue λi, there exists an eigenvector vi such that:

Avi = λivi

### Properties of Eigen Vectors

*   The eigen vectors corresponding to distinct eigen values are linearly independent.
*   If λ is an eigen value of A, then 1/λ is also an eigen value of A-1 (inverse of A).
*   If v is an eigenvector of A corresponding to the eigenvalue λ, then c.v is also an eigenvector of A corresponding to the same eigenvalue λ, where c is a scalar.

## Key Formulas/Theorems

### Characteristic Equation

|A - λI| = 0

### Eigen Value and Eigenvector Equations

Avi = λivi

### Cayley-Hamilton Theorem

A satisfies its own characteristic equation:

|A - λI| = 0

## Problem Solving Patterns

1.  **Finding Eigen Vectors**

    *   Given the matrix A, find the characteristic equation and solve for eigen values.
    *   For each eigen value λi, find an eigenvector vi using the equation Avi = λivi.

2.  **Eigen Decomposition**

    *   Express the matrix A as a product of two matrices: Q (eigen vectors) and Λ (diagonal eigen values).
    *   This is known as eigen decomposition or eigendecomposition.

## Examples with Solutions

### Example 1:

Consider the matrix:

A = [2, -3; 4, 5]

Find an eigen vector of A corresponding to the eigen value λ = 7.

Solution:

First, we need to find the characteristic equation and solve for eigen values. The characteristic equation is given by:

|A - λI| = 0

Substituting λ = 7, we get:

|[2 - 7, -3; 4, 5 - 7]| = |[-5, -3; 4, -2]| = 10 ≠ 0

Therefore, λ = 7 is an eigen value of A.

Next, we need to find the corresponding eigenvector vi. We use the equation Avi = λivi:

[A][vi] = [7][vi]

Substituting A and λ, we get:

[2, -3; 4, 5]
|v1  v2|
= [7, 0]
|v1  v2|

From this, we can see that the first column of vi is [1, 2]. Therefore, an eigen vector corresponding to λ = 7 is:

v1 = [1; 2]

### Example 2:

Consider the matrix:

M = [1, 2; 0, 1]

One of the eigen vectors of M is given by:

v = [-1/√5; 2/√5]

Find another eigen vector of M.

Solution:

Since we already have one eigen vector v, we can use it to find another eigenvector. We know that if v is an eigenvector of A corresponding to the eigenvalue λ, then c.v is also an eigenvector of A corresponding to the same eigenvalue λ, where c is a scalar.

Let's choose c = 1 (for simplicity). Then we can use the equation Avi = λivi:

[M][vi] = [λ][vi]

Substituting M and v, we get:

[1, 2; 0, 1]
|[v11 v12]
| = [λ, 0]
|[v11 v12|

We can see that the second column of vi is [1/√5; -2/√5]. Therefore, another eigen vector of M is:

v2 = [1/√5; -2/√5]

## Common Pitfalls

*   Students often get confused between eigenvectors and eigenvalues. Eigenvectors are the non-zero vectors that when transformed by a matrix A, result in a scaled version of themselves.
*   Another common mistake is not checking for zero determinant in the characteristic equation.

## Quick Summary

### Key Points to Remember:

*   Eigen values and eigenvectors are fundamental concepts in linear algebra and analysis of complex variables.
*   The characteristic equation |A - λI| = 0 can be used to find eigen values and corresponding eigenvectors.
*   Eigenvectors and eigenvalues have several important properties, such as linearity and scaling.

### Key Equations:

|A - λI| = 0

Avi = λivi

### Key Theorems:

Cayley-Hamilton Theorem: A satisfies its own characteristic equation.