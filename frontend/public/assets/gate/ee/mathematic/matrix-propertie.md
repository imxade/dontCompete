**Matrix Properties**
======================

### Introduction

In linear algebra, matrices are used to represent systems of equations and perform various operations such as solving for unknowns, finding eigenvalues and eigenvectors. Understanding the properties of matrices is crucial in many areas of mathematics, physics, and engineering.

### Core Concepts

A matrix $A$ is a rectangular array of numbers or expressions, arranged in rows and columns. The elements of a matrix are denoted by $a_{ij}$, where $i$ represents the row number and $j$ represents the column number.

#### Types of Matrices

*   **Square Matrix**: A matrix with the same number of rows and columns.
*   **Rectangular Matrix**: A matrix with a different number of rows and columns.
*   **Symmetric Matrix**: A square matrix where $a_{ij} = a_{ji}$ for all $i$ and $j$.
*   **Skew-Symmetric Matrix**: A square matrix where $a_{ij} = -a_{ji}$ for all $i$ and $j$.

### Key Formulas/Theorems

#### Symmetric and Skew-Symmetric Matrices

A matrix is symmetric if:

$$\begin{bmatrix}
a & b \\
c & d
\end{bmatrix} \text{ is symmetric } \iff \begin{cases}
a = a \\
b = c \\
d = d
\end{cases}$$

Similarly, a matrix is skew-symmetric if:

$$\begin{bmatrix}
a & b \\
c & d
\end{bmatrix} \text{ is skew-symmetric } \iff \begin{cases}
a = -a \\
b = -c \\
d = -d
\end{cases}$$

### Problem Solving Patterns

When dealing with matrix properties, follow these patterns:

1.  **Identify the type of matrix**: Determine if the matrix is symmetric or skew-symmetric.
2.  **Apply relevant formulas/theorems**: Use the definitions and properties of symmetric and skew-symmetric matrices to solve the problem.

### Examples with Solutions

**Example 1**

Determine if the following matrix is symmetric or skew-symmetric:

$$A = \begin{bmatrix}
1 & 2 \\
3 & -4
\end{bmatrix}$$

**Solution**: To determine the type of matrix, compare each element with its corresponding mirror image.

*   $a_{12} = a_{21}$: No, since $2 \neq 3$.
*   $a_{11} = a_{22}$: Yes, since $1 = -4$, but this is not true for all elements. However, we are looking at the individual diagonal values. We need to check if they are equal or negatives of each other in a symmetric/skew-symmetric manner.

A matrix is skew-symmetric if:

$$\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix} \text{ is skew-symmetric } \iff \begin{cases}
a_{11} = -a_{11} \\
a_{12} = -a_{21} \\
a_{22} = -a_{22}
\end{cases}$$

Therefore, this matrix $A$ is neither symmetric nor skew-symmetric.

**Example 2**

Consider the following matrix:

$$B = \begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}$$

Is matrix B symmetric or skew-symmetric?

**Solution**: Now let's look at this one by one for symmetry/skewness.

*   $a_{11} = a_{22}$: Yes, since $1= (-1)$.
*   We also need to check the off-diagonals.
    *   In a symmetric matrix, we have $b_{12}= b_{21}$ and
        $b_{21} = -b_{12}$. However in skew-symmetric, we have $b_{12}=-b_{21}$ so they will cancel each other out.

Therefore, this matrix $B$ is symmetric.

### Common Pitfalls

1.  **Confusing Symmetric and Skew-Symmetric**: Make sure to understand the definitions clearly.
2.  **Not Checking Off-Diagonal Elements**: Always check if $a_{12} = a_{21}$ for skew-symmetric and if $a_{11} = a_{22}$ for both symmetric and skew-symmetric.

### Quick Summary

*   **Symmetric Matrix**: Square matrix with $a_{ij} = a_{ji}$.
*   **Skew-Symmetric Matrix**: Square matrix with $a_{ij} = -a_{ji}$.
*   Check off-diagonal elements when determining symmetry/skewness.
*   Understand the definitions clearly to avoid confusion.

### Mermaid Diagram
```mermaid
graph LR
A[Symmetric] --> B[Skew-Symmetric]
B --> C[Square Matrix]
C --> D[Rectangular Matrix]
