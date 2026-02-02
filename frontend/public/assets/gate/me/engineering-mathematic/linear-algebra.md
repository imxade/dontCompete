**Linear Algebra Theory Note**
=====================================

### Introduction
---------------

Linear algebra is a fundamental branch of mathematics that deals with the study of linear equations, vector spaces, and linear transformations. It has numerous applications in various fields such as engineering, physics, computer science, and economics.

### Core Concepts
------------------

#### Vector Spaces
-------------------

A **vector space** is a set of vectors that can be added together and scaled by numbers, satisfying certain properties.

*   **Closure under addition**: The sum of any two vectors in the set must also be in the set.
*   **Commutativity of addition**: The order of adding vectors does not matter.
*   **Associativity of addition**: Adding three or more vectors can be done in any order.
*   **Existence of additive identity**: There exists a zero vector that, when added to any other vector, leaves it unchanged.
*   **Existence of additive inverse**: For every vector, there exists an opposite vector such that their sum is the zero vector.

#### Linear Transformations
---------------------------

A **linear transformation** is a function between vector spaces that preserves linear combinations. It can be represented by a matrix.

*   **Linearity**: A linear transformation must satisfy two properties:
    *   $T(a \mathbf{x} + b \mathbf{y}) = a T(\mathbf{x}) + b T(\mathbf{y})$, where $\mathbf{x}$ and $\mathbf{y}$ are vectors, and $a$ and $b$ are scalars.
    *   $T(c\mathbf{x}) = cT(\mathbf{x})$, where $c$ is a scalar.

#### Eigenvalues and Eigenvectors
-----------------------------------

*   **Eigenvalue**: A scalar $\lambda$ such that the linear transformation $T$ satisfies $T(\mathbf{v}) = \lambda \mathbf{v}$ for some nonzero vector $\mathbf{v}$. The vector $\mathbf{v}$ is called an eigenvector.
*   **Eigenspace**: The set of all vectors that are mapped to a multiple of themselves by the linear transformation.

### Key Formulas/Theorems
---------------------------

*   **Determinant**: The determinant of a square matrix $A$ is denoted as $\det(A)$ or $|A|$. It can be used to find the inverse of a matrix and is also related to the concept of eigenvalues.
    \[ \det(A) = \sum_{i=1}^{n} (-1)^{i+j} M_{ij} \]
*   **Inverse of a Matrix**: The inverse of a square matrix $A$ is denoted as $A^{-1}$ and satisfies the property $AA^{-1} = A^{-1}A = I$, where $I$ is the identity matrix.
    \[ A^{-1} = \frac{1}{\det(A)} \text{adj}(A) \]
*   **Eigenvalue Equation**: The equation $\mathbf{Av} = \lambda \mathbf{v}$, where $\mathbf{v}$ is an eigenvector and $\lambda$ is the corresponding eigenvalue.

### Problem Solving Patterns
-----------------------------

#### Finding Eigenvalues and Eigenvectors

To find the eigenvalues and eigenvectors of a matrix $A$, we need to solve the equation $\det(A - \lambda I) = 0$. This will give us the characteristic polynomial, whose roots are the eigenvalues.

*   **Step 1**: Set up the equation $\det(A - \lambda I) = 0$.
*   **Step 2**: Solve for $\lambda$ to find the eigenvalues.
*   **Step 3**: Substitute each eigenvalue into the matrix $A - \lambda I$ and solve for the corresponding eigenvectors.

#### Orthogonality of Eigenvectors

Eigenvectors of a symmetric matrix are orthogonal. This means that if we have two eigenvectors $\mathbf{v}_1$ and $\mathbf{v}_2$ with eigenvalues $\lambda_1$ and $\lambda_2$, then the dot product of these vectors is zero: $\mathbf{v}_1 \cdot \mathbf{v}_2 = 0$.

#### Diagonalization

A square matrix $A$ can be diagonalized if it has a set of orthogonal eigenvectors. The diagonalizing matrix is formed by taking the normalized eigenvectors as its columns, and the resulting diagonal matrix has the eigenvalues on its main diagonal.

*   **Step 1**: Find the eigenvalues and eigenvectors of $A$.
*   **Step 2**: Normalize each eigenvector to form an orthonormal set of vectors.
*   **Step 3**: Arrange these normalized eigenvectors as columns in a matrix, call it $P$. The diagonalizing matrix is then given by $D = P^{-1}AP$.

### Examples with Solutions
---------------------------

#### Example 1: Finding Eigenvalues and Eigenvectors

Find the eigenvalues and eigenvectors of the matrix $\begin{bmatrix} 2 & -1 \\ 3 & 4 \end{bmatrix}$.

**Solution**

*   **Step 1**: Set up the equation $\det\left(\begin{bmatrix} 2 & -1 \\ 3 & 4 \end{bmatrix} - \lambda I\right) = 0$.
*   **Step 2**: Solve for $\lambda$ to find the eigenvalues. The characteristic polynomial is $(2-\lambda)(4-\lambda)-(-1)(3)=\lambda^2-6\lambda+5=0$. Solving this quadratic equation gives us two possible values of $\lambda$: $\lambda_1 = 5, \lambda_2 = 1$.
*   **Step 3**: Substitute each eigenvalue into the matrix $A - \lambda I$ and solve for the corresponding eigenvectors.

For example, let's find an eigenvector corresponding to $\lambda_1=5$. We need to solve $(A-5I)\mathbf{v} = \mathbf{0}$, which is equivalent to $\begin{bmatrix} -3 & -1 \\ 3 & -1 \end{bmatrix}\mathbf{v}=\mathbf{0}$. The solution to this homogeneous system of equations is any nonzero multiple of the eigenvector $\mathbf{v}_1 = \begin{pmatrix} 1 \\ -3/5 \end{pmatrix}$.

#### Example 2: Diagonalizing a Matrix

Diagonalize the matrix $A=\begin{bmatrix} 2 & 3 \\ 4 & 1 \end{bmatrix}$.

**Solution**

*   **Step 1**: Find the eigenvalues and eigenvectors of $A$.
*   **Step 2**: Normalize each eigenvector to form an orthonormal set of vectors.
*   **Step 3**: Arrange these normalized eigenvectors as columns in a matrix, call it $P$. The diagonalizing matrix is then given by $D = P^{-1}AP$.

The characteristic polynomial of the given matrix is $\det(A-\lambda I)=\begin{vmatrix}2-\lambda & -3 \\-4 & 1-\lambda \end{vmatrix}=-(\lambda^2-3\lambda+13)$. The eigenvalues are found by solving this quadratic equation: $\lambda_1 = (3 + \sqrt{33})/2$ and $\lambda_2 = (3 - \sqrt{33})/2$.

We can then find the eigenvectors corresponding to these eigenvalues. For example, let's find an eigenvector corresponding to $\lambda_1 = (3+\sqrt{33})/2$. We need to solve $(A-\lambda_1 I)\mathbf{v}=\mathbf{0}$.

The solution to this homogeneous system of equations is any nonzero multiple of the eigenvector $\mathbf{v}_1=\begin{pmatrix}-4 \\ 1 \end{pmatrix}$.

We can normalize this eigenvector by dividing it by its magnitude: $||\mathbf{v}_1|| = \sqrt{(-4)^2 + (1)^2} = \sqrt{17}$. Therefore, the normalized eigenvector is $\mathbf{\hat{v}}_1=\frac{1}{\sqrt{17}}\begin{pmatrix}-4 \\ 1 \end{pmatrix}$.

Similarly, we can find another normalized eigenvector, say $\mathbf{\hat{v}}_2$, corresponding to the eigenvalue $\lambda_2 = (3-\sqrt{33})/2$.

We can then arrange these two orthonormal vectors as columns in a matrix $P$: \[P=\begin{pmatrix}-4/\sqrt{17} & 1/\sqrt{17}\\1/\sqrt{17} & -4/\sqrt{17}\end{pmatrix}.\]

The diagonalizing matrix is then given by $D=P^{-1}AP$, which we can compute as follows: \[P^{-1}AP =\begin{pmatrix}-4/\sqrt{17} & 1/\sqrt{17}\\1/\sqrt{17} & -4/\sqrt{17}\end{pmatrix}\begin{bmatrix}2&3\\4&1\end{bmatrix}\begin{pmatrix}-4/\sqrt{17}&-1/\sqrt{17}\\1/\sqrt{17}&4/\sqrt{17}\end{pmatrix}=\begin{bmatrix}(3+\sqrt{33})/2&0\\0&(3-\sqrt{33})/2\end{bmatrix}.\]

### Common Pitfalls
-------------------

*   **Incorrect Determinant**: Make sure to calculate the determinant correctly, especially when solving for eigenvalues.
*   **Miscounting Eigenvectors**: Double-check that you have found all the eigenvectors corresponding to each eigenvalue.
*   **Failure to Normalize Vectors**: Remember to normalize your vectors if necessary.

### Quick Summary
-----------------

Key concepts:

*   Vector spaces and their properties
*   Linear transformations, including matrix representation and composition
*   Eigenvalues and eigenvectors, with emphasis on diagonalization
*   Orthogonality of eigenvectors for symmetric matrices

Equations and formulas:

*   Determinant formula
*   Inverse of a matrix formula
*   Eigenvalue equation