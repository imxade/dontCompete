# Linear Algebra Theory Note
=====================================

## Introduction
---------------

Linear algebra is a fundamental subject in engineering mathematics that deals with the study of linear equations, vector spaces, and linear transformations. It has numerous applications in various fields such as computer science, physics, and engineering.

### Objectives

* Understand the basic concepts of linear algebra.
* Familiarize yourself with key formulas and theorems.
* Learn problem-solving patterns and techniques specific to linear algebra.

## Core Concepts
-----------------

### Vector Spaces

A vector space is a set of vectors that satisfy certain properties:

1. Closure under addition: The sum of any two vectors in the set is also in the set.
2. Commutativity of addition: The order of adding vectors does not matter.
3. Associativity of addition: The order in which we add vectors does not affect the result.
4. Existence of additive identity: There exists a vector that, when added to any other vector, leaves it unchanged (zero vector).
5. Existence of additive inverse: For each vector in the set, there exists another vector such that their sum is the zero vector.

### Linear Transformations

A linear transformation is a function from one vector space to another that preserves the operations of vector addition and scalar multiplication:

1. $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ for any $\mathbf{u}, \mathbf{v}$ in the domain.
2. $T(c\mathbf{u}) = cT(\mathbf{u})$ for any scalar $c$ and vector $\mathbf{u}$ in the domain.

### Matrices

A matrix is a rectangular array of numbers:

$$
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$

### Determinants and Trace

* The determinant of an $n\times n$ matrix is denoted as $\det(A)$ or $|A|$:
```math
\det(A) = \begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{vmatrix}
```
* The trace of an $n\times n$ matrix is the sum of its diagonal elements:
```math
\text{tr}(A) = a_{11} + a_{22} + \cdots + a_{nn}
```

## Key Formulas/Theorems
-------------------------

### Matrix Multiplication

If $A$ and $B$ are matrices such that the number of columns in $A$ is equal to the number of rows in $B$, then their product is defined as:
```math
(AB)_{ij} = \sum_{k=1}^n a_{ik}b_{kj}
```
### Determinant Properties

* $\det(A) = (-1)^{i+j}\begin{vmatrix}a_{11} & \cdots & a_{1j-1} & a_{1j+1} & \cdots & a_{1n}\\a_{21} & \cdots & a_{2j-1} & a_{2j+1} & \cdots & a_{2n}\\\vdots & \ddots & \vdots & \vdots & \ddots & \vdots\\a_{m1} & \cdots & a_{mj-1} & a_{mj+1} & \cdots & a_{mn}\end{vmatrix}$ (Minor expansion)
* $\det(AB) = \det(A)\det(B)$

## Problem Solving Patterns
---------------------------

### Analyzing Statement 1 of Q1 (cs_2022_23)

When analyzing the statement $tr(AB) = tr(BA)$, we need to understand that matrix multiplication is not commutative. However, the trace of a matrix is invariant under cyclic permutations.

```mermaid
graph LR
    A[Matrix Multiplication] -->|Not Commutative| B[Trace Invariance]
```

### Analyzing Statement 2 of Q1 (cs_2022_23)

Similarly, for $tr(CD) = tr(DC)$, we need to consider the properties of determinants and trace.

```mermaid
graph LR
    C[Matrix Multiplication] -->|Determinant Properties| D[Trace Invariance]
```

## Examples with Solutions
---------------------------

### Example 1: Determinant and Trace

Suppose $A = \begin{bmatrix}2 & 3\\4 & 5\end{bmatrix}$, then what is $\det(A)$ and $\text{tr}(A)$?

```math
\det(A) = (2)(5) - (3)(4) = 10 - 12 = -2

\text{tr}(A) = 2 + 5 = 7
```

### Example 2: Matrix Multiplication

Suppose $A = \begin{bmatrix}1 & 2\\3 & 4\end{bmatrix}$ and $B = \begin{bmatrix}5 & 6\\7 & 8\end{bmatrix}$, then what is $(AB)_{12}$?

```math
(AB)_{12} = (A_{11})(B_{22}) + (A_{12})(B_{21}) = (1)(8) + (2)(7) = 8 + 14 = 22
```

## Common Pitfalls
------------------

* Confusing matrix multiplication with addition.
* Assuming the trace of a product is equal to the sum of the traces.

## Quick Summary
---------------

* Understand the definition and properties of vector spaces, linear transformations, matrices, determinants, and trace.
* Familiarize yourself with key formulas and theorems.
* Practice solving problems related to matrix operations, determinant properties, and trace calculations.