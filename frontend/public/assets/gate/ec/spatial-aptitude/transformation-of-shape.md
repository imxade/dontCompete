**Transformation of Shape**
==========================

**Introduction**
---------------

In geometry, shape transformation refers to a change in the position or orientation of a geometric figure without altering its size or shape. Understanding these transformations is crucial for spatial reasoning and problem-solving skills. This note will cover the theoretical concepts, formulas, and insights required to tackle questions related to shape transformation.

**Core Concepts**
-----------------

### Rotations

A rotation is a transformation that turns a figure around a fixed point called the axis of rotation.

*   **180° Rotation**: A 180° rotation is equivalent to reflecting a figure across its axis.
*   **90° Clockwise/Counterclockwise Rotation**: A 90° rotation is equivalent to rotating a figure by a quarter turn clockwise or counterclockwise around its axis.

### Axes of Rotation

An axis of rotation can be any line passing through the center of the shape. The most common axes are:

*   **S-Q Axis**: An axis passing through points S and Q.
*   **P-R Axis**: An axis passing through points P and R.
*   **T-Axis**: An axis perpendicular to the screen and passing through point T.

**Key Formulas/Theorems**
-------------------------

### Rotation Matrix

The rotation matrix is a mathematical representation of a rotation transformation:

$$
\begin{bmatrix}
cos(\theta) & -sin(\theta) \\
sin(\theta) & cos(\theta)
\end{bmatrix}
$$

where $\theta$ is the angle of rotation.

**Problem Solving Patterns**
---------------------------

### Analyzing Sequences of Operations

When analyzing sequences of operations, consider the following:

*   **Composition of Transformations**: Each operation can be represented as a matrix. When composing transformations, multiply the matrices.
*   **Determine the Net Effect**: Analyze the sequence to determine the net effect on the shape.

**Examples with Solutions**
---------------------------

### Example 1: Rotation by 180°

Suppose we have a square ABCD and want to rotate it by 180° around point O.

| Point | Original Position | Rotated Position |
| --- | --- | --- |
| A    | (x, y)           | (-x, -y)        |
| B    | (x', y')         | (-x', -y')      |

### Example 2: Rotation by 90° Clockwise

Suppose we have a square ABCD and want to rotate it by 90° clockwise around point O.

| Point | Original Position | Rotated Position |
| --- | --- | --- |
| A    | (x, y)           | (-y, x)         |
| B    | (x', y')         | (-y', x')       |

### Example 3: Sequence of Operations

Suppose we have a square ABCD and want to apply the following sequence of operations:

1.  Rotate by 180° around point O.
2.  Rotate by 90° clockwise around point P.

Using the rotation matrix, we can represent each operation as a matrix:

$$
\begin{bmatrix}
cos(\theta) & -sin(\theta) \\
sin(\theta) & cos(\theta)
\end{bmatrix}
$$

where $\theta$ is the angle of rotation.

**Common Pitfalls**
-------------------

*   **Inconsistent Axis**: Ensure that all rotations are around the same axis.
*   **Incorrect Composition**: Be careful when composing transformations, as the order matters.

**Quick Summary**
-----------------

*   Rotation: a transformation that turns a figure around a fixed point called the axis of rotation.
*   180° Rotation: equivalent to reflecting a figure across its axis.
*   90° Clockwise/Counterclockwise Rotation: equivalent to rotating a figure by a quarter turn clockwise or counterclockwise around its axis.
*   Composition of Transformations: multiply matrices when composing transformations.
*   Determine the Net Effect: analyze the sequence to determine the net effect on the shape.