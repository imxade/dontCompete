**Matrix Algebra**
====================

### Introduction
Matrix algebra is a fundamental tool in linear algebra and has numerous applications in various fields such as engineering, computer science, and physics. In this note, we will cover the key concepts, formulas, and problem-solving techniques required to tackle questions related to matrix algebra.

### Core Concepts

#### Matrix Operations

*   **Addition**: The sum of two matrices A and B is defined as:
    $$A + B = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} + \begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix} = \begin{bmatrix} a_{11}+b_{11} & a_{12}+b_{12} \\ a_{21}+b_{21} & a_{22}+b_{22} \end{bmatrix}$$

*   **Scalar Multiplication**: The product of a scalar c and matrix A is defined as:
    $$cA = c\begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} = \begin{bmatrix} ca_{11} & ca_{12} \\ ca_{21} & ca_{22} \end{bmatrix}$$

*   **Matrix Multiplication**: The product of two matrices A and B is defined as:
    $$AB = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}\begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix} = \begin{bmatrix} a_{11}b_{11}+a_{12}b_{21} & a_{11}b_{12}+a_{12}b_{22} \\ a_{21}b_{11}+a_{22}b_{21} & a_{21}b_{12}+a_{22}b_{22} \end{bmatrix}$$

#### Determinant and Eigenvalues

*   **Determinant**: The determinant of a 2x2 matrix A is defined as:
    $$|A| = \begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix} = a_{11}a_{22}-a_{12}a_{21}$$

*   **Eigenvalues**: The eigenvalues of a matrix A are the values λ that satisfy the equation:
    $|A-\lambda I|=0$

#### Matrix Inversion

*   **Inverse of a 2x2 Matrix**: The inverse of a 2x2 matrix A is defined as:
    $$A^{-1} = \frac{1}{|A|}\begin{bmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{bmatrix}$$

### Key Formulas/Theorems

*   **Cayley-Hamilton Theorem**: A matrix satisfies its own characteristic equation.

### Problem Solving Patterns

*   **Determinant and Eigenvalues**: Use the determinant to find eigenvalues.
*   **Matrix Inversion**: Use the formula for the inverse of a 2x2 matrix.

### Examples with Solutions

**Example 1**

Find the value of $a$ in the following matrix:
$$A = \begin{bmatrix} -5 & a \\ -2 & -2 \end{bmatrix}$$
where the eigenvalues are $-1$ and $-6$. Use the fact that the product of eigenvalues is equal to the determinant.

**Solution**

The determinant of A is:
$$|A| = (-5)(-2) - (a)(-2) = 10 + 2a$$

Since the product of eigenvalues is equal to the determinant, we have:

$$(\text{eigenvalue}_1)(\text{eigenvalue}_2) = |A|$$
$$(-1)(-6) = 10+2a$$
$$6 = 10 + 2a$$
$$-4 = 2a$$
$$a = -2$$

### Common Pitfalls

*   **Determinant vs. Eigenvalues**: The determinant is not always equal to the product of eigenvalues.

### Quick Summary

| Topic      | Key Concepts                 |
| :--------- | :--------------------------- |
| Matrix     | Addition, Scalar Multiplication, Matrix Multiplication |
| Determinant| Calculation, Properties        |
| Eigenvalues| Calculation, Properties       |
| Inversion  | Formula for 2x2 matrices      |

### Visuals

```mermaid
graph LR
A[Matrix Algebra] --> B[Addition]
B --> C[Scalar Multiplication]
C --> D[Matrix Multiplication]
D --> E[Determinant]
E --> F[Eigenvalues]
F --> G[Inversion]
```

The above diagram shows the relationships between different concepts in matrix algebra.