**Linear Algebra**
================

### Introduction

Linear algebra is a branch of mathematics that deals with the study of linear equations, vector spaces, linear transformations, and matrices. It has numerous applications in various fields such as physics, engineering, computer science, and economics.

### Core Concepts

#### Vector Spaces

A **vector space** is a set of vectors under two operations: addition and scalar multiplication. The axioms that define a vector space are:

1. Closure under addition
2. Commutativity of addition
3. Associativity of addition
4. Existence of additive identity (zero vector)
5. Existence of additive inverse
6. Distributive law for scalar multiplication over vector addition
7. Distributive law for scalar multiplication over scalar addition
8. Scalar multiplication is associative

#### Linear Transformations

A **linear transformation** is a function between vector spaces that preserves the operations of vector addition and scalar multiplication. The standard form of a linear transformation is:

f: V → W, where f(v) = Av

where A is a matrix representing the linear transformation.

#### Matrices

A **matrix** is a rectangular array of numbers. Matrices can be used to represent systems of linear equations, linear transformations, and vector spaces. The main types of matrices are:

1. Row matrix
2. Column matrix
3. Square matrix
4. Diagonal matrix
5. Scalar matrix

#### Determinants

The **determinant** of a square matrix A is denoted by |A| or det(A). It can be used to determine the invertibility of a matrix and the number of solutions to a system of linear equations.

Key Formula:

$det(A) = \sum_{i=1}^{n} (-1)^{i+j} a_{ij} M_{ij}$

where $M_{ij}$ is the minor of $a_{ij}$.

### Key Formulas/Theorems

1. **Rank-Nullity Theorem**:

$rank(A) + nullity(A) = n$

2. **Cramer's Rule**:

$x_i = \frac{det(M_i)}{det(A)}$

3. **Invertibility Criterion**:

A matrix A is invertible if and only if |A| ≠ 0.

4. **Eigenvalues and Eigenvectors**:

The eigenvalues of a matrix A are the scalars λ such that there exists a non-zero vector v satisfying Av = λv.

### Problem Solving Patterns

1. **System of Linear Equations**: Represent the system as an augmented matrix and perform row operations to transform it into reduced row echelon form.
2. **Matrix Inversion**: Use Cramer's rule or the formula for the inverse of a 2x2 matrix to find the inverse.
3. **Eigenvalues and Eigenvectors**: Find the characteristic equation, solve for λ, and find the corresponding eigenvectors.

### Examples with Solutions

**Example 1: System of Linear Equations**

Solve the system:

2x + 3y = 7
x - 2y = -3

Represent the system as an augmented matrix:

$\begin{bmatrix} 2 & 3 & | & 7 \\ 1 & -2 & | & -3 \end{bmatrix}$

Perform row operations to transform it into reduced row echelon form.

**Example 2: Matrix Inversion**

Find the inverse of the matrix A = $\begin{bmatrix} 2 & 1 \\ 4 & 3 \end{bmatrix}$

Use Cramer's rule:

$A^{-1} = \frac{1}{det(A)} \begin{bmatrix} det(M_1) & -det(M_2) \\ -det(M_3) & det(M_4) \end{bmatrix}$

**Example 3: Eigenvalues and Eigenvectors**

Find the eigenvalues and eigenvectors of the matrix A = $\begin{bmatrix} 2 & 1 \\ 4 & 3 \end{bmatrix}$

Find the characteristic equation:

$det(A - λI) = 0$

Solve for λ.

### Common Pitfalls

1. **Incorrect Row Operations**: Make sure to perform row operations correctly to avoid incorrect solutions.
2. **Invertibility Criterion**: Remember that a matrix A is invertible if and only if |A| ≠ 0.
3. **Eigenvalues and Eigenvectors**: Be careful when finding the eigenvalues and eigenvectors, as the calculations can be complex.

### Quick Summary

* Vector spaces: Define vector addition and scalar multiplication
* Linear transformations: Preserve vector addition and scalar multiplication
* Matrices: Represent systems of linear equations, linear transformations, and vector spaces
* Determinants: Used to determine invertibility and number of solutions
* Rank-Nullity Theorem: rank(A) + nullity(A) = n
* Cramer's Rule: x_i = det(M_i) / det(A)
* Invertibility Criterion: |A| ≠ 0 for a matrix A to be invertible

Note: This is not an exhaustive list, but it covers the main concepts and formulas tested in the source questions.