**Linear Algebra Theory Note**
=====================================

**Introduction**
---------------

Linear algebra is a fundamental branch of mathematics that deals with the study of linear equations, vector spaces, and linear transformations. It provides an essential framework for solving systems of equations, finding vectors and matrices, and analyzing the properties of linear transformations.

**Core Concepts**
-----------------

### Vectors and Vector Operations

*   **Vector Addition**: Given two vectors $\mathbf{u}$ and $\mathbf{v}$ in a vector space $V$, their sum is defined as $\mathbf{u} + \mathbf{v}$.
*   **Scalar Multiplication**: For any scalar $c$ and vector $\mathbf{v}$, the product $c\mathbf{v}$ is defined.
*   **Dot Product**: The dot product of two vectors $\mathbf{u}$ and $\mathbf{v}$ is denoted as $\mathbf{u} \cdot \mathbf{v}$.

### Matrices and Matrix Operations

*   **Matrix Addition**: Given two matrices $A$ and $B$, their sum is defined as $A + B$.
*   **Scalar Multiplication**: For any scalar $c$ and matrix $A$, the product $cA$ is defined.
*   **Matrix Multiplication**: The product of two matrices $A$ and $B$ is denoted as $AB$.

### Linear Transformations

*   **Linear Transformation**: A linear transformation $T: V \to W$ between vector spaces $V$ and $W$ is a function that preserves the operations of vector addition and scalar multiplication.
*   **Kernel and Image**: The kernel (or null space) of $T$ is the set of all vectors in $V$ that are mapped to the zero vector in $W$, while the image (or range) of $T$ is the set of all vectors in $W$ that are reached by $T$.

### Determinants and Orthogonality

*   **Determinant**: The determinant of a square matrix $A$ is denoted as $\det(A)$ and can be used to determine the invertibility of $A$.
*   **Orthogonal Vectors**: Two vectors $\mathbf{u}$ and $\mathbf{v}$ are orthogonal if their dot product is zero, i.e., $\mathbf{u} \cdot \mathbf{v} = 0$.

**Key Formulas/Theorems**
-------------------------

*   **Vector Addition Formula**: $\mathbf{u} + \mathbf{v} = (\mathbf{u}_1 + \mathbf{v}_1, \ldots, \mathbf{u}_n + \mathbf{v}_n)$
*   **Scalar Multiplication Formula**: $c\mathbf{v} = (c\mathbf{v}_1, \ldots, c\mathbf{v}_n)$
*   **Dot Product Formula**: $\mathbf{u} \cdot \mathbf{v} = u_1v_1 + \ldots + u_nv_n$
*   **Matrix Multiplication Formula**: $(AB)_{ij} = \sum_k a_{ik}b_{kj}$

```latex
\begin{align*}
    (AB)_{ij} &= \sum_k a_{ik}b_{kj}\\
    &= \left( \sum_k a_{ik}b_{kj} \right)
\end{align*}
```

**Problem Solving Patterns**
---------------------------

### Finding the Normal Vector to a Plane

To find the normal vector $\mathbf{n}$ to a plane defined by two vectors $\mathbf{u}$ and $\mathbf{v}$, we can use the cross product formula:

$$\mathbf{n} = \mathbf{u} \times \mathbf{v}$$

### Finding the Image of a Linear Transformation

To find the image of a linear transformation $T$, we need to determine which vectors in the domain are mapped to non-zero vectors in the range.

**Examples with Solutions**
---------------------------

### Example 1: Finding the Normal Vector to a Plane

Find the normal vector $\mathbf{n}$ to the plane defined by the two vectors $\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$ and $\begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}$.

Solution:

```latex
\begin{align*}
    \mathbf{n} &= \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \times \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}\\
    &= \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 3 \\ 4 & 5 & 6 \end{vmatrix}\\
    &= (12-15)\mathbf{i} - (6-12)\mathbf{j} + (5-8)\mathbf{k}\\
    &= \begin{pmatrix} -3 \\ 6 \\ -3 \end{pmatrix}
\end{align*}
```

### Example 2: Finding the Image of a Linear Transformation

Find the image of the linear transformation $T$ that maps $\begin{pmatrix} x \\ y \\ z \end{pmatrix}$ to $\begin{pmatrix} 2x-3y+z \\ -4x+5y-2z \\ 7x-y+z \end{pmatrix}$.

Solution:

To find the image of $T$, we need to determine which vectors in the domain are mapped to non-zero vectors in the range. Let's choose some vectors and apply the transformation:

$$\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \mapsto \begin{pmatrix} 2-3+0 \\ -4+0-0 \\ 7-0+0 \end{pmatrix} = \begin{pmatrix} -1 \\ -4 \\ 7 \end{pmatrix}$$

Since the resulting vector is non-zero, we can conclude that the image of $T$ contains all vectors in $\mathbb{R}^3$.

**Common Pitfalls**
------------------

*   Failing to recognize the importance of linear independence when working with matrices and linear transformations.
*   Making errors when computing determinants or applying matrix operations.

**Quick Summary**
-----------------

*   **Vectors**: addition, scalar multiplication, dot product
*   **Matrices**: addition, scalar multiplication, matrix multiplication
*   **Linear Transformations**: kernel, image, composition
*   **Determinants and Orthogonality**: properties and applications

This comprehensive theory note covers all the essential concepts in linear algebra that are tested in GATE exams. The detailed explanations, examples, and formulas will help students develop a deep understanding of these topics and prepare them for future questions.