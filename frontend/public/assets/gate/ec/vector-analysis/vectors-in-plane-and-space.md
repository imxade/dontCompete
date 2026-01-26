# Vectors in Plane and Space
=====================================================

### Introduction

Vectors are mathematical objects that have both magnitude (length) and direction. In this note, we will cover vectors in plane and space, including their properties, operations, and applications.

### Core Concepts

#### Definition of a Vector

A vector is a quantity with both magnitude and direction. It can be represented graphically as an arrow or by its components (x, y, z) if it's in 3D space.

#### Operations on Vectors

*   **Addition**: The sum of two vectors, denoted as $u + v$.
*   **Scalar Multiplication**: A vector multiplied by a scalar, denoted as $cu$, where c is the scalar.
*   **Subtraction**: The difference between two vectors, denoted as $u - v$.

#### Properties of Vectors

*   **Magnitude (Length)**: Denoted as ||u|| or |u|.
*   **Direction**: Defined by the unit vector in the same direction as u, denoted as $\hat{u}$.
*   **Dot Product** ($\cdot$): The sum of the products of corresponding components. $u \cdot v = u_1v_1 + u_2v_2 + ...$
*   **Cross Product**: A vector resulting from the cross product operation between two vectors.

### Key Formulas/Theorems

$$
\begin{align}
||u + v||^2 &= ||u||^2 + 2(u \cdot v) + ||v||^2\\
(u \times v) \cdot w &= (u \cdot (v \times w))\\
|a(b) + c(d)| &\le |a||b| + |c||d|
\end{align}
$$

### Problem Solving Patterns

#### Analyzing Vector Sequences

When dealing with sequences of vector operations, analyze each operation separately and then combine the results.

### Examples with Solutions

Consider a square with points P(1, 0), Q(2, 0), R(2, 3), S(1, 3), T(0.5, 1.5) marked on it.

#### Example 1: Rotation of Square by 180 Degrees

Let's analyze the sequence XYZZ:

*   X: Rotate square by 180° around SQ axis.
*   Y: Rotate square by 180° around PR axis.
*   Z: Rotate square by 90° clockwise around PT axis.

Since rotation by 180° is equivalent to reflection about a point, and we have two reflections (about SQ and PR axes), they cancel each other out. The sequence becomes ZZ.

Now analyze the remaining operations:

*   Z: Rotate by 90° clockwise.
*   Z: Another 90° rotation, which results in the same direction as the first one.

This means that the final orientation of the square is equivalent to its initial position.

### Common Pitfalls

*   Failing to recognize the equivalence between different sequences of operations.
*   Not considering all possible outcomes when analyzing vector sequences.

### Quick Summary

*   Vectors have magnitude and direction.
*   Operations: addition, subtraction, scalar multiplication, dot product, cross product.
*   Key formulas include the dot product formula, the cross product formula, and the triangle inequality.
*   Analyze each operation in a sequence separately and combine results to determine final outcome.

### Visuals

No Mermaid diagrams are used for this topic. If you'd like to add one, please let me know!