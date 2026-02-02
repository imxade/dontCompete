**Linear Algebra Theory Note**
==========================

**Introduction**
---------------

Linear algebra is a branch of mathematics that deals with the study of linear equations, vector spaces, and linear transformations. It has numerous applications in fields such as engineering, physics, computer science, and economics.

**Core Concepts**
-----------------

### Vectors and Vector Operations

A **vector** is a mathematical object that represents a quantity with both magnitude (length) and direction.

* **Magnitude**: The length of the vector.
* **Direction**: The direction of the vector in space.
* **Scalar multiplication**: Multiplying a vector by a scalar changes its magnitude but not its direction. `v \cdot c = |c| \cdot v`
* **Vector addition**: Adding two vectors results in a new vector whose components are the sums of corresponding components.

### Matrix Operations

A **matrix** is a rectangular array of numbers.

* **Matrix multiplication**: Multiplying two matrices results in another matrix whose elements are determined by the dot product of rows and columns. `A \cdot B = C`
* **Identity matrix**: A square matrix with ones on the main diagonal and zeros elsewhere, used to represent the identity transformation. `I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}`

### Linear Transformations

A **linear transformation** is a function that maps one vector space to another while preserving linear combinations.

* **Kernel**: The set of vectors that are mapped to the zero vector. `Ker(T) = \{v: T(v) = 0\}`
* **Image**: The set of vectors that are mapped from some other vector. `Im(T) = \{T(v): v \in V\}`

**Key Formulas/Theorems**
------------------------

### Linear Independence and Basis

A set of vectors is **linearly independent** if none of the vectors can be expressed as a linear combination of the others.

* **Span**: The span of a set of vectors is the set of all possible linear combinations. `span(V) = \{v: v = \sum_{i} c_i v_i, c_i \in \mathbb{R}\}`
* **Basis**: A basis for a vector space is a set of linearly independent vectors that span the entire space.

### Determinants

The **determinant** of a square matrix is a scalar value that can be used to determine the solvability of a system of linear equations.

* **Determinant of a 2x2 matrix**: `det(\begin{bmatrix} a & b \\ c & d \end{bmatrix}) = ad - bc`
* **Determinant of an n x n matrix**: Can be calculated using various methods such as Laplace expansion or LU decomposition.

**Problem Solving Patterns**
---------------------------

### Q1 (ee_2023_7)

Given the graph, which one of the following options represents the given function?

* **Step 1**: Analyze the graph to determine its characteristics.
* **Step 2**: Identify the type of function represented by the graph (e.g., linear, quadratic, exponential).
* **Step 3**: Match the characteristics and type of function with the options provided.

### Q2 (ee_2023_11)

Find the vector normal to the plane defined by `T \cdot W = 0`.

* **Step 1**: Identify the equation defining the plane.
* **Step 2**: Recognize that the normal vector is perpendicular to any vector in the plane.
* **Step 3**: Use the given vector `[1,2,3]` as a vector in the plane and find its dot product with itself.

**Examples with Solutions**
-------------------------

### Example 1

Find the determinant of `A = \begin{bmatrix} 2 & 3 \\ 4 & 5 \end{bmatrix}`

* **Step 1**: Use the formula for a 2x2 matrix: `det(A) = (2)(5) - (3)(4)`
* **Step 2**: Simplify the expression to find the determinant.

### Example 2

Find the vector normal to the plane defined by `T \cdot W = 0`, given that `[1,2,3]` is a vector in the plane.

* **Step 1**: Recognize that any vector perpendicular to `[1,2,3]` will be normal to the plane.
* **Step 2**: Find the cross product of `[1,2,3]` with itself to get a vector perpendicular to it.
* **Step 3**: Simplify the result.

**Common Pitfalls**
------------------

* Failing to recognize linear independence and basis in vector spaces.
* Misapplying determinant properties (e.g., swapping rows or columns).
* Confusing kernel and image of linear transformations.

**Quick Summary**
----------------

### Key Concepts:

* Vectors and vector operations
* Matrix operations
* Linear transformations
* Determinants
* Basis and span of a set of vectors

### Key Formulas/Theorems:

* Scalar multiplication: `v \cdot c = |c| \cdot v`
* Vector addition: `a + b = (a_1 + b_1, a_2 + b_2)`
* Matrix multiplication: `A \cdot B = C`
* Determinant of 2x2 matrix: `det(A) = ad - bc`

### Tips and Tricks:

* Pay attention to scalar multiplication when working with vectors.
* Use the correct notation for linear transformations (e.g., `T(v)` instead of `Tv`).
* Verify that the basis is linearly independent.