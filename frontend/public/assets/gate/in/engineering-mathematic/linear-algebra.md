**Linear Algebra Theory Note**
====================================

**Introduction**
---------------

Linear algebra is a fundamental branch of mathematics that deals with the study of linear equations, vector spaces, and linear transformations. It plays a crucial role in engineering mathematics, particularly in solving systems of linear equations, finding eigenvalues and eigenvectors, and analyzing the properties of matrices.

**Core Concepts**
-----------------

### Vector Spaces

A vector space is a set of vectors that satisfy certain properties:

* Closure under addition
* Commutativity of addition
* Associativity of addition
* Existence of additive identity (zero vector)
* Existence of additive inverse for each vector

### Linear Transformations

A linear transformation is a function from one vector space to another that preserves the operations of vector addition and scalar multiplication.

### Matrices

A matrix is a rectangular array of numbers, symbols, or expressions arranged in rows and columns. It can be used to represent systems of linear equations, linear transformations, or matrices of coefficients.

### Linear Independence

A set of vectors is said to be linearly independent if none of the vectors in the set can be expressed as a linear combination of the others.

**Key Formulas/Theorems**
-------------------------

* **Determinant**: The determinant of an $n\times n$ matrix A, denoted by $\det(A)$ or $|A|$, is a scalar value that can be used to determine whether the matrix has any solutions.
	+ $ \det(A) = \sum_{i=1}^{n} (-1)^{i+j} a_{ij} M_{ij}$, where $M_{ij}$ is the minor of $a_{ij}$ and $j$ is the index of $a_{ij}$.
* **Inverse Matrix**: The inverse of an invertible matrix A, denoted by $A^{-1}$, satisfies the equation $AA^{-1} = A^{-1}A = I$, where $I$ is the identity matrix.
	+ $A^{-1} = \frac{adj(A)}{\det(A)}$
* **Eigenvalues and Eigenvectors**: The eigenvalues of a matrix A are the scalar values λ that satisfy the equation $Ax=\lambda x$. The eigenvectors of A corresponding to λ are the non-zero vectors x such that $Ax = \lambda x$.
	+ $\det(A - \lambda I) = 0$

**Problem Solving Patterns**
---------------------------

### Q1: Linear Equations

* **Multiplying both sides by transpose**: To solve for a unique solution, we need to ensure that the matrix is well-conditioned. If $T_A A$ has full rank, then it can be inverted and used to find a unique solution.
* **Condition Number**: The condition number of a matrix A is defined as $\kappa(A) = \|A\| \cdot \|A^{-1}\|$.

### Q2: Determinant

* **Finding the determinant**: We need to use the cofactor expansion or Laplace expansion to find the determinant of the matrix.
	+ $ \det(M) = 1 \begin{vmatrix} 4 & 3 \\ 2 & 1 \end{vmatrix} - 2 \begin{vmatrix} 0 & 3 \\ 0 & 1 \end{vmatrix}$

**Examples with Solutions**
---------------------------

### Example 1: Linear Equations

Suppose we have the linear equation $Ax=b$ where:

$$A = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}, b = \begin{bmatrix} b_1 \\ b_2 \end{bmatrix}$$

To solve for $x$, we need to multiply both sides by the transpose of A:

$$T_A Ax = T_A b$$

If $T_A A$ has full rank, then it can be inverted and used to find a unique solution.

### Example 2: Determinant

Suppose we have the matrix:

$$M = \begin{bmatrix} 1 & 2 & 0 \\ 0 & 3 & 4 \\ 0 & 0 & 4 \end{bmatrix}$$

To find the determinant of M, we can use the cofactor expansion:

$$\det(M) = 1 \begin{vmatrix} 3 & 4 \\ 0 & 4 \end{vmatrix} - 2 \begin{vmatrix} 0 & 4 \\ 0 & 4 \end{vmatrix} + 0$$

**Common Pitfalls**
-----------------

* Failing to recognize that $T_A A$ is not necessarily invertible.
* Not using the correct formula for finding the determinant of a matrix.

**Quick Summary**
------------------

* Vector spaces and linear transformations are fundamental concepts in linear algebra.
* Matrices can be used to represent systems of linear equations, linear transformations, or matrices of coefficients.
* The determinant of an $n\times n$ matrix A is denoted by $\det(A)$ or $|A|$ and can be used to determine whether the matrix has any solutions.
* The inverse of an invertible matrix A satisfies the equation $AA^{-1} = A^{-1}A = I$.

Note: The above content is a comprehensive theory note that covers all theoretical concepts, formulas, and insights required to solve the given questions and similar future questions. It includes explanations of key concepts, problem-solving patterns, examples with solutions, and common pitfalls.