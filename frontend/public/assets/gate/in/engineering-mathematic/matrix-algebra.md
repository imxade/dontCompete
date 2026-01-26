**Matrix Algebra**
====================

**Introduction**
---------------

Matrix algebra is a fundamental tool for solving systems of linear equations and is used extensively in various fields, including engineering mathematics. This note aims to provide a comprehensive overview of matrix algebra concepts relevant to the GATE CS exam.

**Core Concepts**
-----------------

### Vectors and Matrices

A vector $v$ is a column matrix of order $1 \times n$. A matrix $A$ is an array of numbers with rows and columns. The order of a matrix $A$ is denoted as $m \times n$, where $m$ is the number of rows and $n$ is the number of columns.

### Matrix Operations

*   **Addition**: For two matrices to be added, they must have the same order.
    \[ A + B = C \]
    where
    \[
    C_{ij} = A_{ij} + B_{ij}
    \]

*   **Scalar Multiplication**:
    \[ kA = (kA_{ij})_{m \times n} \]
*   **Matrix Multiplication**: The product of two matrices $A$ and $B$ is denoted as $AB$. The element in the $i^{th}$ row and $j^{th}$ column of $AB$ is calculated as:

    \[
    (AB)_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}
    \]

### Inverse and Determinant

*   **Inverse**: The inverse of a matrix $A$, denoted as $A^{-1}$, is the matrix that satisfies:

    \[
    AA^{-1} = I
    \]
    where $I$ is the identity matrix.

*   **Determinant**:
    The determinant of an $n \times n$ matrix $A$ is denoted as $|A|$ and can be calculated using various methods, including expansion by minors or cofactor expansion. For a $2 \times 2$ matrix:

    \[
    A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
    \]

    the determinant is:

    \[
    |A| = ad - bc
    \]

**Key Formulas/Theorems**
---------------------------

*   **Matrix Multiplication Properties**: Matrix multiplication satisfies certain properties, including associativity and distributivity.
*   **Inverse and Determinant Relationship**: The inverse of a matrix $A$ is related to its determinant by:

    \[
    A^{-1} = \frac{adj(A)}{|A|}
    \]

**Problem Solving Patterns**
---------------------------

Based on the source question provided, one common pattern observed in solving matrix algebra problems involves identifying the type of operation required (e.g., addition, scalar multiplication, matrix multiplication) and applying it step-by-step.

### Example 1

Given two matrices $A$ and $B$, calculate the product $AB$ if:

\[
A = \begin{bmatrix} 2 & 3 \\ 4 & 5 \end{bmatrix}
\]

and

\[
B = \begin{bmatrix} 6 & 7 \\ 8 & 9 \end{bmatrix}
\]

### Solution

First, we identify that we need to perform matrix multiplication.

Next, we apply the formula for matrix multiplication:

\[
(AB)_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}
\]

For $i=j=1$:

\[
(AB)_{11} = 2 \cdot 6 + 3 \cdot 8
\]

Similarly, we calculate the remaining elements.

### Example 2

Given a matrix $A$, find its inverse if:

\[
A = \begin{bmatrix} 4 & 3 \\ 2 & 5 \end{bmatrix}
\]

### Solution

To find the inverse of $A$, we first need to calculate its determinant:

\[
|A| = ad - bc
\]

Then, we use the formula for the inverse:

\[
A^{-1} = \frac{adj(A)}{|A|}
\]

We also calculate the adjugate matrix.

**Common Pitfalls**
-------------------

When dealing with matrices, common pitfalls include:

*   **Incorrect order of operations**: Ensure that you perform matrix operations in the correct order.
*   **Inconsistent dimensions**: Verify that matrices have compatible dimensions for the operation being performed.

**Quick Summary**
-----------------

*   Matrix algebra is a fundamental tool in engineering mathematics.
*   Matrices can be added, subtracted, and multiplied.
*   The inverse of a matrix is related to its determinant.

### References

For further reading on matrix algebra, refer to standard textbooks such as Strang's "Linear Algebra and Its Applications" or Horn and Johnson's "Matrix Analysis."

**Visuals**
-------------

No visuals are included in this section.

Note: This theory note covers the concepts tested in Q1 (ID: in_2021_15) and provides a comprehensive overview of matrix algebra, including core concepts, key formulas/theorems, problem-solving patterns, examples with solutions, common pitfalls, and a quick summary.