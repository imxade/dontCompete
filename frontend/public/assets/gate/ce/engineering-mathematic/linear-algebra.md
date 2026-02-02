**Linear Algebra Theory Note**
==============================

**Introduction**
---------------

Linear algebra is a fundamental subject in mathematics and engineering that deals with the study of linear equations, vector spaces, linear transformations, and matrices. It has numerous applications in various fields such as physics, computer science, and engineering.

**Core Concepts**
-----------------

### Vector Spaces

A **vector space** over a field `F` is a set of vectors equipped with operations of addition and scalar multiplication that satisfy certain properties:

*   Closure: The sum of any two vectors is also a vector in the set.
*   Commutativity: The order of adding vectors does not matter (a + b = b + a).
*   Associativity: Adding three or more vectors follows the associative property ((a + b) + c = a + (b + c)).
*   Distributivity: Scalar multiplication distributes over vector addition (c(a + b) = ca + cb).
*   Existence of additive identity and inverse.

### Linear Transformations

A **linear transformation** is a function between vector spaces that preserves the operations of vector addition and scalar multiplication. It is represented by a matrix, which encodes the transformation's properties:

*   Matrix multiplication: The product of two matrices represents the composition of linear transformations.
*   Invertibility: A non-singular matrix has an inverse, corresponding to an invertible linear transformation.

### Eigenvalues and Eigenvectors

**Eigenvalues** are scalar values that represent how much a linear transformation stretches or compresses a vector. **Eigenvectors** are the vectors on which this stretching or compression occurs:

*   Characteristic polynomial: The characteristic equation of a matrix, obtained by det(A - λI) = 0.
*   Eigenvalue decomposition: A matrix can be decomposed into its eigenvalues and eigenvectors.

### Matrix Operations

Common matrix operations include:

*   **Matrix multiplication**: The product of two matrices.
*   **Determinant**: A scalar value that describes the invertibility of a matrix.
*   **Inverse**: The inverse of a non-singular matrix, representing an invertible linear transformation.

**Key Formulas/Theorems**
-------------------------

### Determinant

The determinant of a 2x2 matrix $\begin{bmatrix}a & b\\c & d\end{bmatrix}$ is given by:

$$
\det \begin{bmatrix}a & b\\c & d\end{bmatrix} = ad - bc.
$$

### Inverse

The inverse of a 2x2 matrix $\begin{bmatrix}a & b\\c & d\end{bmatrix}$ is given by:

$$
\begin{bmatrix}a & b\\c & d\end{bmatrix}^{-1} = \frac{1}{ad - bc}\begin{bmatrix}d & -b\\-c & a\end{bmatrix}.
$$

### Eigenvalue Decomposition

A matrix can be decomposed into its eigenvalues and eigenvectors as follows:

$$
A = PDP^{-1},
$$

where $P$ is the matrix of eigenvectors, $D$ is the diagonal matrix of eigenvalues, and $P^{-1}$ is the inverse of $P$.

**Problem Solving Patterns**
---------------------------

### Finding Eigenvalues

To find the eigenvalues of a matrix, we need to solve the characteristic equation:

$$
\det(A - \lambda I) = 0.
$$

This will give us the eigenvalues of the matrix.

### Finding Eigenvectors

Once we have found the eigenvalues, we can find the corresponding eigenvectors by solving the equation:

$$
A\mathbf{v} = \lambda\mathbf{v}.
$$

This will give us the eigenvectors of the matrix.

**Examples with Solutions**
-------------------------

### Example 1: Finding Eigenvalues and Eigenvectors

Consider the matrix $\begin{bmatrix}2 & 1\\1 & 2\end{bmatrix}$. We want to find its eigenvalues and eigenvectors.

To do this, we need to solve the characteristic equation:

$$
\det \begin{bmatrix}2 - \lambda & 1\\1 & 2 - \lambda\end{bmatrix} = (2-\lambda)^2 - 1 = 0.
$$

Solving for $\lambda$, we get:

$$
(2-\lambda)^2 - 1 = 0 \Rightarrow \lambda^2 - 4\lambda + 3 = 0.
$$

This is a quadratic equation, and solving it gives us the eigenvalues:

$$
\lambda_1 = 3, \quad \lambda_2 = 1.
$$

Now that we have found the eigenvalues, we can find the corresponding eigenvectors. To do this, we need to solve the equation:

$$
A\mathbf{v} = \lambda\mathbf{v}.
$$

For $\lambda_1 = 3$, we get:

$$
\begin{bmatrix}2 & 1\\1 & 2\end{bmatrix}\mathbf{v}_1 = 3\mathbf{v}_1.
$$

Solving for $\mathbf{v}_1$, we get:

$$
\mathbf{v}_1 = \begin{bmatrix}1\\-1\end{bmatrix}.
$$

Similarly, for $\lambda_2 = 1$, we get:

$$
\mathbf{v}_2 = \begin{bmatrix}1\\1\end{bmatrix}.
$$

Therefore, the eigenvalues and eigenvectors of the matrix are:

*   Eigenvalues: $\lambda_1 = 3, \quad \lambda_2 = 1$
*   Eigenvectors: $\mathbf{v}_1 = \begin{bmatrix}1\\-1\end{bmatrix}, \quad \mathbf{v}_2 = \begin{bmatrix}1\\1\end{bmatrix}$

### Example 2: Finding Eigenvalues of a Matrix

Consider the matrix $\begin{bmatrix}4 & 1\\1 & 2\end{bmatrix}$. We want to find its eigenvalues.

To do this, we need to solve the characteristic equation:

$$
\det \begin{bmatrix}4 - \lambda & 1\\1 & 2 - \lambda\end{bmatrix} = (4-\lambda)(2-\lambda) - 1 = 0.
$$

Solving for $\lambda$, we get:

$$
(4-\lambda)(2-\lambda) - 1 = 0 \Rightarrow \lambda^2 - 6\lambda + 7 = 0.
$$

This is a quadratic equation, and solving it gives us the eigenvalues:

$$
\lambda_1 = 5, \quad \lambda_2 = 1.
$$

Therefore, the eigenvalues of the matrix are $\lambda_1 = 5, \quad \lambda_2 = 1$.

**Common Pitfalls**
------------------

### Inconsistent Matrices

If a matrix is inconsistent (i.e., it has no solution), then its determinant will be zero. Therefore, if we find that the determinant of a matrix is zero, we should check for inconsistencies in the system.

### Inverse Matrices

When finding the inverse of a matrix, we need to make sure that the matrix is non-singular (i.e., it has an inverse). If the matrix is singular, then its inverse will not exist.

**Quick Summary**
-----------------

*   **Vector spaces**: A set of vectors equipped with operations of addition and scalar multiplication.
*   **Linear transformations**: Functions between vector spaces that preserve the operations of vector addition and scalar multiplication.
*   **Eigenvalues and eigenvectors**: Scalars and vectors on which a linear transformation acts as a stretching or compression.
*   **Matrix operations**: Common operations performed on matrices, such as matrix multiplication, determinant, and inverse.

This theory note provides an overview of the fundamental concepts in linear algebra. It covers vector spaces, linear transformations, eigenvalues, and eigenvectors, as well as common matrix operations. The examples provided demonstrate how to apply these concepts to solve problems. By mastering this material, you will be able to tackle a wide range of linear algebra problems with confidence.