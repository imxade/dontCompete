**Matrix Algebra**
=====================

**Introduction**
---------------

Matrix algebra is a fundamental tool for solving systems of linear equations and manipulating linear transformations. In this note, we'll cover the key concepts, formulas, and problem-solving patterns required to tackle GATE CS exam questions.

**Core Concepts**
-----------------

### Matrices and Operations

A matrix is a rectangular array of numbers:

$$
\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{bmatrix}
$$

Matrices can be added, subtracted, multiplied (both scalar and matrix), and transposed.

### Matrix Multiplication

Matrix multiplication is a fundamental operation in linear algebra. Given two matrices A and B with dimensions m x n and n x p respectively:

$$
AB = \begin{bmatrix} c_{11} & c_{12} & \dots & c_{1p} \\ c_{21} & c_{22} & \dots & c_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ c_{m1} & c_{m2} & \dots & c_{mp} \end{bmatrix}
$$

where $c_{ij}$ is computed as the dot product of row i of A and column j of B.

### Inverse and Determinant

The inverse of a matrix A, denoted by $A^{-1}$, is a matrix that satisfies:

$$
AA^{-1} = A^{-1}A = I
$$

where I is the identity matrix. The determinant of a square matrix A, denoted by det(A) or |A|, is computed as the product of its eigenvalues.

### Vector Operations

Vectors can be multiplied by matrices using the outer product:

$$
AB = \begin{bmatrix} b_1a_{11} & b_1a_{12} & \dots & b_1a_{1n} \\ b_2a_{21} & b_2a_{22} & \dots & b_2a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ b_ma_{m1} & b_ma_{m2} & \dots & b_ma_{mn} \end{bmatrix}
$$

### Complex Numbers

Complex numbers are represented in the form $a + bi$, where a and b are real numbers, and i is the imaginary unit.

**Key Formulas/Theorems**
-------------------------

*   Matrix multiplication: $AB = C$ where $c_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}$.
*   Inverse of a matrix: $A^{-1} = \frac{1}{\det(A)}\text{adj}(A)$.
*   Determinant of a 2x2 matrix: $\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$.

**Problem Solving Patterns**
---------------------------

### Pattern 1: Matrix Multiplication

When solving problems involving matrix multiplication, ensure the dimensions match and apply the formula for $c_{ij}$.

### Pattern 2: Inverse and Determinant

When finding the inverse or determinant of a matrix, use the formulas provided above and be mindful of the properties of determinants (e.g., $\det(AB) = \det(A)\det(B)$).

**Examples with Solutions**
---------------------------

### Example 1: Matrix Multiplication

Given matrices A and B:

$$
A = \begin{bmatrix} 2 & 3 \\ 4 & 5 \end{bmatrix}, B = \begin{bmatrix} 6 & 7 \\ 8 & 9 \end{bmatrix}
$$

Compute AB.

```latex
\begin{align*}
AB &= \begin{bmatrix} (2)(6) + (3)(8) & (2)(7) + (3)(9) \\ (4)(6) + (5)(8) & (4)(7) + (5)(9) \end{bmatrix}\\
&= \begin{bmatrix} 12 + 24 & 14 + 27 \\ 24 + 40 & 28 + 45 \end{bmatrix}\\
&= \begin{bmatrix} 36 & 41 \\ 64 & 73 \end{bmatrix}
\end{align*}
```

### Example 2: Inverse of a Matrix

Given matrix A:

$$
A = \begin{bmatrix} 3 & 0 \\ 0 & 4 \end{bmatrix}
$$

Compute the inverse of A.

```latex
\begin{align*}
\det(A) &= (3)(4) - (0)(0)\\
&= 12
\end{align*}

A^{-1} = \frac{1}{\det(A)}\text{adj}(A)
$$

Computing the adjugate of A:

```latex
\begin{align*}
\text{adj}(A) &= \begin{bmatrix} (4)^2 & 0 \\ 0 & (3)^2 \end{bmatrix}\\
&= \begin{bmatrix} 16 & 0 \\ 0 & 9 \end{bmatrix}
\end{align*}

$$

Therefore:

```latex
\begin{align*}
A^{-1} &= \frac{1}{12}\begin{bmatrix} 16 & 0 \\ 0 & 9 \end{bmatrix}\\
&= \begin{bmatrix} \frac{4}{3} & 0 \\ 0 & \frac{3}{4} \end{bmatrix}
\end{align*}
```

**Common Pitfalls**
------------------

*   Failing to check the dimensions of matrices before multiplying.
*   Forgetting to transpose or take the conjugate when working with complex numbers.

**Quick Summary**
-----------------

*   Matrix multiplication: $AB = C$ where $c_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}$.
*   Inverse of a matrix: $A^{-1} = \frac{1}{\det(A)}\text{adj}(A)$.
*   Determinant of a 2x2 matrix: $\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$.

By mastering these concepts and formulas, you'll be well-equipped to tackle the GATE CS exam questions and other challenges in engineering mathematics.