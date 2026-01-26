**Linear Algebra: Matrix Algebra and Systems of Linear Equations**
===========================================================

### Introduction
Matrix algebra is a fundamental tool for solving systems of linear equations, which are ubiquitous in engineering mathematics. This note covers the essential concepts, formulas, and techniques required to tackle questions on matrix algebra and systems of linear equations.

### Core Concepts

#### Matrices and Operations
A matrix $\mathbf{A}$ is an $m \times n$ array of elements from a field (e.g., real or complex numbers). We denote $\mathbf{A} = [a_{ij}]$, where $i = 1, \ldots, m$ and $j = 1, \ldots, n$. The following operations are crucial:

*   Matrix addition: $\mathbf{A} + \mathbf{B} = [\mathbf{a}_{ij} + \mathbf{b}_{ij}]$
*   Scalar multiplication: $\alpha \mathbf{A} = [\alpha a_{ij}]$
*   Matrix multiplication: $\mathbf{AB}$ (defined below)

Matrix Multiplication
--------------------

Given matrices $\mathbf{A}$ ($m \times n$) and $\mathbf{B}$ ($n \times p$), their product is defined as:

$$\mathbf{C} = \mathbf{AB} = [c_{ij}]$$

where $c_{ij} = \sum_{k=1}^n a_{ik} b_{kj}$.

#### Matrix Multiplication Properties
The following properties are essential:

*   **Associativity**: $(\mathbf{A}\mathbf{B})\mathbf{C} = \mathbf{A}(\mathbf{B}\mathbf{C})$
*   **Distributivity**: $\mathbf{A}(\mathbf{B} + \mathbf{C}) = \mathbf{AB} + \mathbf{AC}$ and $(\mathbf{B} + \mathbf{C})\mathbf{A} = \mathbf{BA} + \mathbf{CA}$
*   **Matrix Transpose**: $\mathbf{A}^T$ is the transpose of matrix $\mathbf{A}$, obtained by interchanging rows and columns.

#### Systems of Linear Equations
Given a system of $m$ linear equations in $n$ variables:

$$\begin{align}
a_{11} x_1 + \cdots + a_{1n} x_n &= b_1 \\
&\vdots\\
a_{m1} x_1 + \cdots + a_{mn} x_n &= b_m
\end{align}$$

We can represent this system as the matrix equation $\mathbf{Ax} = \mathbf{b}$.

### Key Formulas/Theorems

#### Eigenvalues and Eigenvectors
Let $\lambda$ be an eigenvalue of a square matrix $\mathbf{A}$, and let $\mathbf{x}$ be the corresponding eigenvector. Then:

$$\mathbf{Ax} = \lambda \mathbf{x}$$

The characteristic equation is given by $|\mathbf{A} - \lambda \mathbf{I}| = 0$.

#### Rank-Nullity Theorem
Let $\mathbf{A}$ be an $m \times n$ matrix. Then:

$$\text{rank}(\mathbf{A}) + \text{nullity}(\mathbf{A}) = n$$

where the rank is the maximum number of linearly independent rows or columns, and the nullity is the dimension of the null space.

### Problem Solving Patterns

#### Finding Eigenvalues
To find the smallest eigenvalue of matrix $\begin{pmatrix} 2 & 1 \\ 6 & -2 \end{pmatrix}$:

*   Compute the characteristic equation: $|\mathbf{A} - \lambda \mathbf{I}| = (2-\lambda)^2 + 12 = 0$
*   Solve for $\lambda$: $\lambda^2 - 4\lambda + 16 = (\lambda-2)^2 = 0$, so $\lambda_1 = 2$ and $\lambda_2 = 8$
*   The smallest eigenvalue is $\lambda_1 = 2$

#### Solving Systems of Linear Equations
To solve the system:

$$\begin{align}
x + y &= 3 \\
2x - y &= -5
\end{align}$$

Represented as $\mathbf{Ax} = \mathbf{b}$ with matrix $\mathbf{A} = \begin{pmatrix} 1 & 1 \\ 2 & -1 \end{pmatrix}$:

*   Find the determinant: $|\mathbf{A}| = (1)(-1) - (-1)(2) = 3$
*   The inverse is $\mathbf{A}^{-1} = \frac{1}{3}\begin{pmatrix} -1 & -1 \\ 2 & 1 \end{pmatrix}$
*   Multiply both sides by the inverse: $x\mathbf{A}^{-1} = x + y = 3\mathbf{A}^{-1}b$

### Examples with Solutions

#### Example 1
Find the smallest eigenvalue of matrix $\begin{pmatrix} 2 & 1 \\ 6 & -2 \end{pmatrix}$.

Solution:

1.  Compute the characteristic equation: $|\mathbf{A} - \lambda \mathbf{I}| = (2-\lambda)^2 + 12 = 0$
2.  Solve for $\lambda$: $\lambda^2 - 4\lambda + 16 = (\lambda-2)^2 = 0$, so $\lambda_1 = 2$ and $\lambda_2 = 8$
3.  The smallest eigenvalue is $\lambda_1 = 2$

#### Example 2
Solve the system of linear equations:

$$\begin{align}
x + y &= 3 \\
2x - y &= -5
\end{align}$$

Solution:

*   Find the determinant: $|\mathbf{A}| = (1)(-1) - (-1)(2) = 3$
*   The inverse is $\mathbf{A}^{-1} = \frac{1}{3}\begin{pmatrix} -1 & -1 \\ 2 & 1 \end{pmatrix}$
*   Multiply both sides by the inverse: $x\mathbf{A}^{-1} = x + y = 3\mathbf{A}^{-1}b$

### Common Pitfalls

*   Forgetting to check for linear dependence between rows or columns when calculating determinant.
*   Confusing the rank and nullity of a matrix.

### Quick Summary
This note covered the essential concepts, formulas, and techniques required for solving systems of linear equations using matrix algebra. Key topics included:

*   Matrices and operations (addition, scalar multiplication, matrix multiplication)
*   Eigenvalues and eigenvectors
*   Rank-nullity theorem
*   Problem-solving patterns for finding eigenvalues and solving systems of linear equations.

By mastering these concepts, students will be well-prepared to tackle questions on linear algebra in future exams.