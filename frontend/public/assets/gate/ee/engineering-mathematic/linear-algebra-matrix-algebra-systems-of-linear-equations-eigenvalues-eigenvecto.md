**Linear Algebra: Matrix Algebra and Systems of Linear Equations**
===========================================================

### Introduction

Linear algebra is a branch of mathematics that deals with the study of linear equations, vector spaces, linear transformations, and matrices. It has numerous applications in various fields such as engineering, physics, computer science, and economics.

In this theory note, we will cover the key concepts, formulas, and problem-solving techniques required to tackle questions related to matrix algebra, systems of linear equations, eigenvalues, and eigenvectors.

### Core Concepts

#### Matrices

A **matrix** is a rectangular array of numbers or expressions. It can be represented as:

$$
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$

where $a_{ij}$ represents the element in the $i^{th}$ row and $j^{th}$ column.

#### Matrix Operations

Matrix addition, subtraction, multiplication, and transpose are defined as follows:

*   Addition: $$ A + B = \begin{bmatrix} a_{11}+b_{11} & \cdots \\ \vdots & \ddots \end{bmatrix} $$
*   Subtraction: $$ A - B = \begin{bmatrix} a_{11}-b_{11} & \cdots \\ \vdots & \ddots \end{bmatrix} $$
*   Multiplication: $$ AB = \begin{bmatrix} c_{11} & \cdots \\ \vdots & \ddots \end{bmatrix}, \quad c_{ij} = \sum_{k=1}^n a_{ik}b_{kj} $$
*   Transpose: $$ A^T = \begin{bmatrix} a_{11} & a_{21} & \cdots \\ a_{12} & a_{22} & \cdots \\ \vdots & \vdots & \ddots \end{bmatrix} $$

#### Inverse of a Matrix

The **inverse** of a matrix $A$, denoted as $A^{-1}$, is defined such that:

$$
AA^{-1} = A^{-1}A = I
$$

where $I$ is the identity matrix.

### Key Formulas/Theorems

*   **Determinant**: $$ \det(A) = \sum_{i=1}^n (-1)^{i+j} a_{ij}M_{ij} $$ where $M_{ij}$ is the minor of element $a_{ij}$.
*   **Inverse**: $$ A^{-1} = \frac{1}{\det(A)} \mathrm{Adj}(A) $$
*   **Eigenvalues and Eigenvectors**: For a matrix $A$, an eigenvalue $\lambda$ and corresponding eigenvector $v$ satisfy:

$$
Av = \lambda v
$$

### Problem Solving Patterns

#### Identifying Invertible Matrices

To determine if a matrix is invertible, check the following conditions:

*   The matrix must be square.
*   The determinant of the matrix must be non-zero.

If both conditions are met, then the matrix has an inverse.

#### Finding Eigenvalues and Eigenvectors

Use the characteristic equation to find eigenvalues:

$$
\det(A - \lambda I) = 0
$$

Then, solve for $\lambda$.

For each eigenvalue, find the corresponding eigenvector by solving the equation:

$$
Av = \lambda v
$$

### Examples with Solutions

**Example 1:** Find the inverse of matrix $A = \begin{bmatrix} 2 & 4 \\ -1 & 3 \end{bmatrix}$.

## Step 1: Calculate the determinant of A.
$\det(A) = (2)(3) - (-1)(4) = 10$

## Step 2: Find the adjugate matrix $Adj(A)$.
$Adj(A) = \begin{bmatrix} 3 & 4 \\ -1 & 2 \end{bmatrix}$

## Step 3: Calculate the inverse of A using the formula.
$A^{-1} = \frac{1}{\det(A)} Adj(A) = \frac{1}{10}\begin{bmatrix} 3 & 4 \\ -1 & 2 \end{bmatrix}$

**Example 2:** Find the eigenvalues and eigenvectors of matrix $A = \begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix}$.

## Step 1: Solve the characteristic equation to find eigenvalues.
$\det(A - \lambda I) = (2-\lambda)(3-\lambda) = 0$

## Step 2: Find the corresponding eigenvectors for each eigenvalue.
For $\lambda_1 = 2$, solve $(A - 2I)v = 0$:
$\begin{bmatrix} 0 & 1 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$

For $\lambda_2 = 3$, solve $(A - 3I)v = 0$:
$\begin{bmatrix} -1 & 1 \\ 0 & 0 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$

### Common Pitfalls

*   Failing to check for invertibility of a matrix.
*   Not calculating the determinant correctly.
*   Overlooking eigenvectors corresponding to repeated eigenvalues.

### Quick Summary

| Concept | Description |
| --- | --- |
| Matrices | Rectangular arrays of numbers or expressions. |
| Inverse | Non-singular square matrices have an inverse. |
| Eigenvalues and Eigenvectors | Solve the characteristic equation to find eigenvalues, then solve for corresponding eigenvectors. |

I hope this meets your requirements!