# Linear Algebra Theory Notes
=====================================

## Introduction
---------------

Linear algebra is a branch of mathematics that deals with the study of linear equations, vector spaces, and linear transformations. It plays a crucial role in many fields such as engineering, physics, computer science, and data analysis.

## Core Concepts
-----------------

### Vector Spaces
---------------

A set of vectors `V` equipped with operations of addition (+) and scalar multiplication (•) is called a vector space if it satisfies the following properties:

* Closure under addition: For any two vectors `u,v ∈ V`, their sum `u+v` is also in `V`.
* Commutativity of addition: For any two vectors `u,v ∈ V`, `u+v = v+u`.
* Associativity of addition: For any three vectors `u,v,w ∈ V`, `(u+v)+w = u+(v+w)`.
* Existence of additive identity: There exists a vector `0 ∈ V` such that for any vector `u ∈ V`, `u + 0 = u`.
* Existance of additive inverse: For each vector `u ∈ V`, there exists a vector `-u ∈ V` such that `u + (-u) = 0`.

### Linear Transformations
-------------------------

A linear transformation is a function `T: V → W` between two vector spaces that preserves the operations of addition and scalar multiplication. It satisfies the following properties:

* Linearity: For any vectors `u,v ∈ V`, `T(u+v) = T(u)+T(v)` and for any scalar `c`, `T(cu) = cT(u)`.

### Matrices
-------------

A matrix is a rectangular array of numbers with rows and columns. It can be used to represent linear transformations between vector spaces.

## Key Formulas/Theorems
-------------------------

* **Rank-Nullity Theorem**: For any linear transformation `T: V → W`, the rank of `T` (the dimension of its image) plus the nullity of `T` (the dimension of its kernel) is equal to the dimension of `V`.
* **Inverse Matrix Formula**: Given a square matrix `A`, if it has an inverse, then its inverse is given by:
$$A^{-1} = \frac{1}{\det(A)} \mathrm{adj}(A),$$
where $\det(A)$ is the determinant of $A$ and $\mathrm{adj}(A)$ is the adjugate matrix of $A$.
* **Cramer's Rule**: Given a square matrix `A` with entries `a_{ij}`, the value of its inverse at position `(i,j)` is given by:
$$[A^{-1}]_{ij} = \frac{\det(A^{(j)})}{\det(A)},$$
where $A^{(j)}$ is the matrix obtained from $A$ by replacing the `j`-th column with the standard basis vector `e_i`.

## Problem Solving Patterns
-----------------------------

### Finding Inverse Matrices
---------------------------

* Check if the determinant of the matrix is non-zero. If it is, then the matrix has an inverse.
* Use Cramer's Rule or the formula for the inverse matrix to find the inverse.

### Linear Transformations and Matrix Representation
---------------------------------------------------

* Find the standard matrix representation of the linear transformation using the images of the basis vectors.
* Use this representation to find the effect of the linear transformation on any vector in the domain.

## Examples with Solutions
---------------------------

### Example 1: Finding the Inverse of a Matrix
------------------------------------------

Consider the matrix:
$$A = \begin{pmatrix} 4 & 3 \\ 5 & 5 \end{pmatrix}.$$
Find its inverse using Cramer's Rule.

Solution:

* Find the determinant of `A`: $\det(A) = (4)(5)-(3)(5) = -5$.
* Find the adjugate matrix of `A`:
$$\mathrm{adj}(A) = \begin{pmatrix} 5 & -3 \\ -5 & 4 \end{pmatrix}.$$
* Find the inverse of `A` using Cramer's Rule:
$$[A^{-1}]_{11} = \frac{\det(A^{(1)})}{\det(A)} = \frac{(5)(5)-(0)(3)}{-5} = -2,$$
$$[A^{-1}]_{12} = \frac{\det(A^{(2)})}{\det(A)} = \frac{(-5)(5)-(4)(3)}{-5} = 3,$$
$$[A^{-1}]_{21} = \frac{\det(A^{(3)})}{\det(A)} = \frac{(4)(0)-(3)(-5)}{-5} = -2,$$
$$[A^{-1}]_{22} = \frac{\det(A^{(4)})}{\det(A)} = \frac{(-5)(0)-(5)(-3)}{-5} = 3.$$

The inverse of `A` is:
$$A^{-1} = \begin{pmatrix} -2 & 3 \\ -2 & 3 \end{pmatrix}.$$

### Example 2: Finding the Image of a Linear Transformation
------------------------------------------------------

Consider the linear transformation represented by the matrix:
$$T = \begin{pmatrix} 4 & 3 \\ 5 & 5 \end{pmatrix}.$$
Find the image of the vector `u = (1,0)` under this linear transformation.

Solution:

* Find the product of `T` and `u`: $Tu = (4)(1)+(3)(0) = 4$.
* The image of `u` is the column vector `(4,0)`.

## Common Pitfalls
-------------------

* **Determinant**: Don't forget to check if the determinant of a matrix is non-zero before trying to find its inverse!
* **Cramer's Rule**: Make sure to apply Cramer's Rule correctly by finding the correct columns for each position.
* **Matrix Representation**: Remember that the standard matrix representation of a linear transformation can be used to find the effect of the transformation on any vector in the domain.

## Quick Summary
-----------------

* Vector spaces have operations of addition and scalar multiplication that satisfy certain properties.
* Linear transformations between vector spaces preserve these operations and can be represented by matrices.
* The rank-nullity theorem relates the dimension of a linear transformation's image to the dimensions of its kernel and domain.
* Inverse matrices exist if and only if the determinant is non-zero, and can be found using Cramer's Rule or the formula for the inverse matrix.

[TOC]

Note: I've used Markdown headers, emphasized key concepts with bold text, and included examples with step-by-step solutions to illustrate the application of linear algebra concepts.