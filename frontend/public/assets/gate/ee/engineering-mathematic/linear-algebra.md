# Linear Algebra
======================

## Introduction
---------------

Linear algebra is a branch of mathematics that deals with the study of linear equations, vector spaces, and linear transformations. It is a fundamental subject in engineering and computer science, with applications in data analysis, machine learning, computer graphics, and more.

## Core Concepts
-----------------

### Vectors
------------

* A **vector** is an ordered set of numbers that can be thought of as an arrow in n-dimensional space.
* The **magnitude** or **length** of a vector is the distance from the origin to the point represented by the vector.
* Two vectors are **equal** if they have the same magnitude and direction.

### Vector Operations
---------------------

#### Addition

* The sum of two vectors is another vector whose components are the sums of corresponding components of the original vectors.

LaTeX:
$$\mathbf{a} + \mathbf{b} = (a_1 + b_1, a_2 + b_2, ..., a_n + b_n)$$

#### Scalar Multiplication

* The product of a scalar and a vector is another vector whose components are the products of corresponding components of the original vector and the scalar.

LaTeX:
$$c\mathbf{a} = (ca_1, ca_2, ..., ca_n)$$

### Matrix Operations
---------------------

#### Matrix Addition

* The sum of two matrices is another matrix whose elements are the sums of corresponding elements of the original matrices.

LaTeX:
$$\mathbf{A} + \mathbf{B} = (a_{ij} + b_{ij})_{m\times n}$$

#### Scalar Multiplication

* The product of a scalar and a matrix is another matrix whose elements are the products of corresponding elements of the original matrix and the scalar.

LaTeX:
$$c\mathbf{A} = (ca_{ij})_{m\times n}$$

### Determinants
-----------------

* A **determinant** is a scalar value that can be computed from the elements of a square matrix.
* The determinant of a 2x2 matrix [a, b; c, d] is ad - bc.

LaTeX:
$$\det \begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc$$

## Key Formulas/Theorems
-------------------------

* **Eigenvalues and Eigenvectors**: If A is an nxn matrix, then λ is an eigenvalue of A if there exists a non-zero vector v such that Av = λv.
* **Cayley-Hamilton Theorem**: Every square matrix satisfies its own characteristic equation.

LaTeX:
$$\mathbf{A}^n + \mathbf{B}^{n-1}\mathbf{A} + ... + \mathbf{I} = 0$$

## Problem Solving Patterns
---------------------------

### Finding Eigenvalues and Eigenvectors

* To find the eigenvalues of a matrix, compute its characteristic polynomial.
* To find the eigenvectors of a matrix, solve the equation Av = λv for v.

Example:
Suppose we want to find the eigenvalues and eigenvectors of the matrix A = [[2, 1; 1, 0]].
First, compute the characteristic polynomial: det(A - λI) = -λ^2 + 2λ.
Then, solve for λ: λ^2 - 2λ = 0 => λ(λ - 2) = 0 => λ = 0 or λ = 2.
Finally, find the eigenvectors by solving Av = λv for each value of λ.

### Linear Transformations

* To find a linear transformation matrix A that maps vectors u to v, express the coordinates of v in terms of the coordinates of u.

Example:
Suppose we want to find a linear transformation matrix A that maps the vector (x, y) to the vector (2x + 3y, x - 2y).
Expressing the coordinates of the new vector in terms of the old vector, we get:

LaTeX:
$$\begin{bmatrix} 2 & 3 \\ 1 & -2 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 2x + 3y \\ x - 2y \end{bmatrix}$$

## Examples with Solutions
---------------------------

### Example 1: Finding Eigenvalues and Eigenvectors

Suppose we want to find the eigenvalues and eigenvectors of the matrix A = [[1, 2; 0, 1]].
Computing the characteristic polynomial: det(A - λI) = -(λ^2 - λ).
Solving for λ: λ^2 - λ = 0 => λ(λ - 1) = 0 => λ = 0 or λ = 1.
Finding the eigenvectors by solving Av = λv for each value of λ.

### Example 2: Linear Transformations

Suppose we want to find a linear transformation matrix A that maps the vector (x, y) to the vector (3x + 4y, x - 2y).
Expressing the coordinates of the new vector in terms of the old vector:

LaTeX:
$$\begin{bmatrix} 3 & 4 \\ 1 & -2 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 3x + 4y \\ x - 2y \end{bmatrix}$$

## Common Pitfalls
------------------

* Not checking the dimension of a matrix before computing its determinant or inverse.
* Not ensuring that the vectors being added or multiplied are compatible.

## Quick Summary
---------------

* Vectors: ordered sets of numbers, magnitude and direction.
* Vector operations: addition, scalar multiplication.
* Matrix operations: addition, scalar multiplication, matrix multiplication.
* Determinants: scalars computed from square matrices.
* Eigenvalues and eigenvectors: non-zero vectors and scalars that satisfy Av = λv.

Mermaid diagram for linear transformations:
```mermaid
graph LR
A[Vector (x, y)] --> B[Linear Transformation A]
B --> C[Vector (3x + 4y, x - 2y)]
```
This note covers the fundamental concepts of linear algebra, including vector operations, matrix operations, determinants, eigenvalues and eigenvectors. The examples with solutions illustrate how to apply these concepts to real-world problems.