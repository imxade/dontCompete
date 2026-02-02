**Linear Algebra**
=====================

### Introduction

Linear algebra is a fundamental branch of mathematics that deals with vector spaces and linear transformations. It has numerous applications in computer science, physics, engineering, and other fields. This note aims to cover the essential concepts, formulas, and problem-solving patterns required for the GATE CS exam.

### Core Concepts

#### Vector Spaces

A vector space is a set of vectors that can be added together and scaled by scalars, satisfying certain properties:

*   Closure under addition: $u + v$ must be in the vector space.
*   Commutativity of addition: $u + v = v + u$
*   Associativity of addition: $(u + v) + w = u + (v + w)$
*   Existence of additive identity: there exists a vector 0 such that $u + 0 = u$
*   Existence of additive inverse: for each vector $u$, there exists a vector $-u$ such that $u + (-u) = 0$

Some common vector spaces include:

*   $\mathbb{R}^n$: the set of all n-tuples of real numbers
*   $\mathbb{C}^n$: the set of all n-tuples of complex numbers

#### Linear Transformations

A linear transformation is a function $T: V \to W$ between two vector spaces that preserves the operations of vector addition and scalar multiplication:

$$T(u + v) = T(u) + T(v)$$
$$T(cu) = cT(u)$$

Some common types of linear transformations include:

*   Isomorphisms: bijective linear transformations between isomorphic vector spaces
*   Projections: linear transformations that project a vector onto a subspace
*   Invertible transformations: linear transformations with an inverse

### Key Formulas/Theorems

#### Matrix Representation of Linear Transformations

Let $T$ be a linear transformation from $\mathbb{R}^n$ to $\mathbb{R}^m$. Then, there exists a matrix $A \in M_{m \times n}(\mathbb{R})$ such that:

$$T(x) = Ax$$
where $x \in \mathbb{R}^n$

#### Eigenvalues and Eigenvectors

Let $A$ be an $n \times n$ matrix. Then, the eigenvalue equation is given by:

$$Ax = \lambda x$$
where $\lambda$ is the eigenvalue and $x$ is the corresponding eigenvector.

### Problem Solving Patterns

#### Finding Eigenvalues and Eigenvectors

*   Set up the characteristic polynomial: $\det(A - \lambda I) = 0$
*   Solve for the eigenvalues: find the roots of the characteristic polynomial
*   Find the corresponding eigenvectors using the equation $(A - \lambda I)x = 0$

#### Solving Systems of Linear Equations

*   Write the augmented matrix:
$$\left[ \begin{array}{cccc|c} a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\ a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} & b_m \end{array} \right]$$
*   Perform row operations to put the matrix into reduced row echelon form (RREF)
*   Read off the solution from the RREF

### Examples with Solutions

#### Example 1: Finding Eigenvalues and Eigenvectors

Suppose we want to find the eigenvalues and eigenvectors of the matrix:

$$A = \left[ \begin{array}{cc} 2 & 1 \\ 3 & 0 \end{array} \right]$$

*   Set up the characteristic polynomial: $\det(A - \lambda I) = (2-\lambda)(-3\lambda) = 0$
*   Solve for the eigenvalues: $\lambda_1 = 2$, $\lambda_2 = 0$
*   Find the corresponding eigenvectors:
	+ For $\lambda_1 = 2$: solve $(A - 2I)x = 0$ to get $x_1 = (1, 3)$
	+ For $\lambda_2 = 0$: solve $(A - 0I)x = 0$ to get $x_2 = (-1, 0)$

#### Example 2: Solving a System of Linear Equations

Suppose we want to solve the system:

$$\left[ \begin{array}{cc} 1 & 2 \\ 3 & 4 \end{array} \right] \left[ \begin{array}{c} x_1 \\ x_2 \end{array} \right] = \left[ \begin{array}{c} 7 \\ 11 \end{array} \right]$$

*   Write the augmented matrix:
$$\left[ \begin{array}{cc|c} 1 & 2 & 7 \\ 3 & 4 & 11 \end{array} \right]$$
*   Perform row operations to put the matrix into RREF:

$$\left[ \begin{array}{cc|c} 1 & 0 & 5 \\ 0 & 1 & -2 \end{array} \right]$$

*   Read off the solution: $x_1 = 5$, $x_2 = -2$

### Common Pitfalls

*   Make sure to check for consistency when solving systems of linear equations
*   Be careful with the signs and magnitudes of eigenvalues and eigenvectors

### Quick Summary

| Concept | Description |
| --- | --- |
| Vector Spaces | Sets of vectors that can be added together and scaled by scalars |
| Linear Transformations | Functions between vector spaces that preserve addition and scalar multiplication |
| Eigenvalues and Eigenvectors | Values and corresponding vectors that make a matrix have a certain form when multiplied by the identity matrix |
| Systems of Linear Equations | Equations that describe linear relationships between variables |

Note: This summary is not exhaustive, but it covers the most important concepts. Make sure to review the entire note for a comprehensive understanding.

**Theory Note Complete**

(No external images used in this response.)