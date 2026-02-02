**Matrix Algebra**
================

### Introduction
---------------

Matrix algebra is a fundamental tool for solving systems of linear equations and analyzing linear transformations. In this note, we will cover the key concepts and formulas required to tackle GATE CS exam questions on matrix algebra.

### Core Concepts
-----------------

*   **Matrix Representation**: A matrix is a rectangular array of numbers, symbols, or expressions arranged in rows and columns.
*   **Matrix Operations**:
    *   **Addition**: Two matrices can be added if they have the same dimensions. The resulting matrix has elements that are the sum of corresponding elements in the original matrices.
    *   **Scalar Multiplication**: A scalar (a number) can be multiplied with a matrix, which scales each element of the matrix by the scalar value.
    *   **Matrix Multiplication**: Given two matrices A and B, if the number of columns in A is equal to the number of rows in B, then the product AB is defined. The resulting matrix has dimensions determined by the input matrices.

### Key Formulas/Theorems
---------------------------

*   **Rank of a Matrix**:
    $$
    \text{rank}(A) = n - \text{nullity}(A)
    $$
    where $\text{nullity}(A)$ is the dimension of the null space of A.
*   **Matrix Inverse**:
    $$
    A^{-1} = \frac{1}{\det(A)} \text{adj}(A)
    $$
    where $\det(A)$ is the determinant of matrix A and $\text{adj}(A)$ is the adjugate (also known as the classical adjugate) of A.

### Problem Solving Patterns
---------------------------

*   **Reducing a Matrix to Row Echelon Form**:
    *   Interchange rows to get a 1 in the top left corner.
    *   Multiply a row by a scalar and add it to another row to eliminate elements below the leading entry.
*   **Determining the Rank of a Matrix**:
    *   Count the number of linearly independent rows (or columns).

### Examples with Solutions
---------------------------

**Example 1**

Given matrix A, find its rank:

$$
A = \begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{bmatrix}
$$

To find the rank of A, we can reduce it to row echelon form. After performing elementary row operations:

$$
\begin{bmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
0 & 0 & 0 \\
\end{bmatrix} \quad\Rightarrow\quad
\begin{bmatrix}
1 & 2 & 3 \\
0 & 1 & 2 \\
0 & 0 & 0 \\
\end{bmatrix}
$$

We can see that the first two rows are linearly independent, so the rank of A is 2.

**Example 2**

Find the inverse of matrix B:

$$
B = \begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{bmatrix}
$$

To find the inverse, we need to calculate the determinant and adjugate of B. After performing calculations:

$$
\det(B) = -20 \quad\text{and}\quad \text{adj}(B) = \begin{bmatrix}
-5 & 2 & 1 \\
4 & -1 & 0 \\
3 & -2 & 1 \\
\end{bmatrix}
$$

So, the inverse of B is:

$$
B^{-1} = \frac{1}{-20} \text{adj}(B) = \begin{bmatrix}
\frac{-5}{20} & \frac{2}{20} & \frac{1}{20} \\
\frac{4}{20} & -\frac{1}{20} & 0 \\
\frac{3}{20} & -\frac{2}{20} & \frac{1}{20} \\
\end{bmatrix}
$$

### Common Pitfalls
-------------------

*   When calculating the rank of a matrix, don't forget to count the number of linearly independent rows (or columns).
*   When finding the inverse of a matrix, make sure to calculate the determinant and adjugate correctly.

### Quick Summary
------------------

*   Matrix operations: addition, scalar multiplication, and matrix multiplication.
*   Rank of a matrix: determined by the number of linearly independent rows (or columns).
*   Inverse of a matrix: calculated using the determinant and adjugate.

This comprehensive note covers all theoretical concepts and formulas required to solve GATE CS exam questions on matrix algebra.