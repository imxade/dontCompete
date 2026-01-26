# Solutions of Linear Algebraic Equations
=====================================

## Introduction
---------------

Linear algebraic equations are a fundamental aspect of numerical methods, and solving them is crucial for various applications. This topic focuses on finding solutions to systems of linear equations in real-valued variables x and y.

## Core Concepts
-----------------

A system of linear equations can be represented as:

Ax = b

where A is the coefficient matrix, x is the variable vector, and b is the constant vector.

### Cramer's Rule

For a 2x2 matrix:

|a11  a12|
|a21  a22|

Cramer's rule states that the solution for x1 and x2 can be found using:

x1 = (Δx1) / Δ
x2 = (Δx2) / Δ

where Δ is the determinant of the coefficient matrix:

Δ = a11*a22 - a12*a21

and Δx1, Δx2 are determinants obtained by replacing the corresponding column with b.

### Determinant and Inverse

The determinant of an n x n matrix A can be calculated using various methods. For a 2x2 matrix:

Δ = a11*a22 - a12*a21

The inverse of a 2x2 matrix A can be found using:

A^{-1} = (1/Δ) * [[a22, -a12], [-a21, a11]]

### System of Linear Equations with Infinite Solutions

For a system of linear equations to have infinite solutions, the coefficient matrix must have two identical rows. This leads to an equation of the form:

Ax = λx

where λ is a scalar.

## Key Formulas/Theorems
-------------------------

\[ \det(A) = \begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix} = a_{11}a_{22} - a_{12}a_{21} \]

\[ A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{bmatrix} \]

## Problem Solving Patterns
---------------------------

### Method 1: Cramer's Rule

Use Cramer's rule to find the solutions. Replace the corresponding column with b and calculate the determinants.

### Method 2: Determinant and Inverse

Calculate the determinant of the coefficient matrix and its inverse using the formulas above.

## Examples with Solutions
-------------------------

**Example 1**

Find the solution for the system:

| 2   | -2 |
| --- | --- |
| x   | y  |

Using Cramer's rule, we get:

Δ = (2)(-2) - (-2)(0) = -4

Δx = ((0)(-2) - (-2)(2)) / -4 = 1
Δy = ((2)(2) - (-2)(0)) / -4 = -1/2

Therefore, the solution is x = 1 and y = -1/2.

**Example 2**

Find the value of α for which the system:

| 5-2α | 10 |
| --- | --- |
| x    | y  |

has infinite solutions.

Since there are two identical rows, we get:

(5-2α)x + 10y = 0

Solving for α, we get α = 1.

## Common Pitfalls
-------------------

*   Not checking the determinant of the coefficient matrix before applying Cramer's rule.
*   Not calculating the inverse correctly.
*   Not considering the special case when the system has infinite solutions.

## Quick Summary
-----------------

### Key Concepts

*   System of linear equations
*   Determinant and inverse of a 2x2 matrix
*   Cramer's rule for finding solutions
*   Infinite solutions: identical rows in the coefficient matrix

### Key Formulas

*   Determinant of a 2x2 matrix
*   Inverse of a 2x2 matrix

### Key Techniques

*   Using Cramer's rule to find solutions
*   Calculating determinant and inverse