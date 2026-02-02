**Matrix Algebra Systems of Linear Equations Eigenvalues and Eigenvectors**
===========================================================

**Introduction**
---------------

In this note, we will cover the fundamental concepts of matrix algebra systems of linear equations eigenvalues and eigenvectors. This topic is essential for understanding various applications in computer science, including image processing, data analysis, and machine learning.

**Core Concepts**
-----------------

### Matrix Algebra

A matrix $A$ is a rectangular array of numbers, typically denoted by capital letters (e.g., $A$, $B$, $C$). Matrices can be represented as:

$$
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$

where $a_{ij}$ represents the element in the $i$-th row and $j$-th column.

### Systems of Linear Equations

A system of linear equations can be represented as:

$$
\begin{align*}
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n &= b_2 \\
\vdots & = \vdots \\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n &= b_m
\end{align*}
$$

where $A$ is the coefficient matrix, $X$ is the variable matrix, and $B$ is the constant matrix.

### Eigenvalues and Eigenvectors

An eigenvalue $\lambda$ of a square matrix $A$ is a scalar such that there exists a non-zero vector $v$ (the eigenvector) satisfying:

$$
Av = \lambda v
$$

The eigenvalue represents how much the linear transformation represented by $A$ stretches or compresses the eigenvector.

**Key Formulas/Theorems**
-------------------------

*   **Determinant**: $\det(A) = \sum_{i=1}^{n} (-1)^{i+j} a_{ij} M_{ij}$, where $M_{ij}$ is the minor of $a_{ij}$.
*   **Inverse Matrix**: $A^{-1} = \frac{1}{\det(A)} \text{adj}(A)$, where $\text{adj}(A)$ is the adjugate matrix.
*   **Eigenvalue Equation**: $(A - \lambda I)v = 0$, where $I$ is the identity matrix.

**Problem Solving Patterns**
---------------------------

### Pattern 1: Finding Eigenvalues and Eigenvectors

Given a matrix $A$, find its eigenvalues and eigenvectors by solving the characteristic equation $\det(A - \lambda I) = 0$.

### Pattern 2: System of Linear Equations

Use Gaussian elimination or LU decomposition to solve systems of linear equations represented by $AX = B$.

**Examples with Solutions**
---------------------------

### Example 1: Finding Eigenvalues and Eigenvectors

Let $A = \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}$. Find its eigenvalues and eigenvectors.

*   Solve the characteristic equation $\det(A - \lambda I) = (2-\lambda)^2 + 1 = 0$.
*   Obtain the quadratic formula: $(-\frac{\sqrt{5}}{2}, \frac{\sqrt{5}}{2})$
*   Find the corresponding eigenvectors by solving $(A - \lambda I)v = 0$.

### Example 2: System of Linear Equations

Let $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$, $X = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$ and $B = \begin{bmatrix} 5 \\ 6 \end{bmatrix}$. Solve the system of linear equations $AX = B$.

*   Use Gaussian elimination to transform $A$ into upper triangular form.
*   Back-substitute to find the values of $x_1$ and $x_2$.

**Common Pitfalls**
-------------------

*   **Inconsistent Systems**: Ensure that the number of equations is equal to the number of variables in a system of linear equations.
*   **Non-square Matrices**: Be cautious when dealing with non-square matrices, as they do not have an inverse.

**Quick Summary**
----------------

| Concept | Definition |
| --- | --- |
| Matrix Algebra | Rectangular array of numbers. |
| Systems of Linear Equations | Set of linear equations represented by $AX = B$. |
| Eigenvalues and Eigenvectors | Scalar $\lambda$ and vector $v$ satisfying $(A - \lambda I)v = 0$. |

This note provides a comprehensive overview of the fundamental concepts in matrix algebra systems of linear equations eigenvalues, and eigenvectors. The examples with solutions demonstrate how to apply these concepts to solve problems.