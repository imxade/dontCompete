**Transformation of Shapes**
==========================

### Introduction

Spatial aptitude is a critical component of the GATE CS exam, and transformation of shapes is an essential topic within it. This note will cover translation, rotation, scaling, mirroring, assembling, and grouping transformations.

### Core Concepts

#### Translation

Translation is a transformation that moves a shape from one position to another without changing its orientation or size.

*   A translation can be described by two parameters: the initial point (x0, y0) and the displacement vector (dx, dy).
*   The new coordinates (x', y') of a translated shape are given by:

    $$\begin{cases}
        x' = x_0 + dx \\
        y' = y_0 + dy
    \end{cases}$$

#### Rotation

Rotation is a transformation that turns a shape around a fixed point called the pivot or rotation center.

*   A rotation can be described by three parameters: the angle of rotation (θ), the pivot point (x0, y0), and the direction of rotation.
*   The new coordinates (x', y') of a rotated shape are given by:

    $$\begin{cases}
        x' = x_0 + r \cos(\theta) \\
        y' = y_0 + r \sin(\theta)
    \end{cases}$$

where r is the distance from the pivot point to the original point (x, y).

#### Scaling

Scaling is a transformation that changes the size of a shape.

*   A scaling can be described by two parameters: the scale factor (k) and the center of scaling (x0, y0).
*   The new coordinates (x', y') of a scaled shape are given by:

    $$\begin{cases}
        x' = k(x - x_0) + x_0 \\
        y' = k(y - y_0) + y_0
    \end{cases}$$

#### Mirroring

Mirroring is a transformation that reflects a shape across a line.

*   A mirroring can be described by two parameters: the line of reflection (y = mx + b) and the point of reflection (x0, y0).
*   The new coordinates (x', y') of a mirrored shape are given by:

    $$\begin{cases}
        x' = 2(x_0 - x) + x \\
        y' = 2(y_0 - y) + y
    \end{cases}$$

#### Assembling and Grouping

Assembling and grouping refer to combining multiple shapes to form a new shape.

*   A shape can be assembled by applying transformations (translation, rotation, scaling, mirroring) to individual components.
*   Grouping is the process of defining a set of shapes as a single entity, which can then be transformed together.

### Problem Solving Patterns

When solving problems involving transformation of shapes, follow these patterns:

1.  **Identify the type of transformation**: Determine if it's translation, rotation, scaling, mirroring, assembling, or grouping.
2.  **Apply the appropriate formula or theorem**: Use the formulas and theorems mentioned above to calculate the new coordinates.
3.  **Check for any additional transformations**: If multiple transformations are involved, apply each one in sequence.

### Examples with Solutions

**Example 1:** A square is translated by (2, 3) units.

*   Initial point: (0, 0)
*   Displacement vector: (2, 3)

Apply the translation formula:

$$\begin{cases}
    x' = 0 + 2 \\
    y' = 0 + 3
\end{cases}$$

New coordinates: (2, 3)

**Example 2:** A triangle is rotated by 45° around its center.

*   Center of rotation: (0, 0)
*   Angle of rotation: 45°

Apply the rotation formula:

$$\begin{cases}
    x' = r \cos(\theta) \\
    y' = r \sin(\theta)
\end{cases}$$

Assuming a unit circle, the new coordinates are (cos(45°), sin(45°)) = (√2/2, √2/2)

### Common Pitfalls

*   **Misapplying formulas**: Double-check that you're using the correct formula for the transformation.
*   **Incorrectly identifying transformations**: Make sure you understand which type of transformation is being applied.
*   **Forgetting to check additional transformations**: Ensure all transformations are accounted for.

### Quick Summary

| Transformation | Formula/Description |
| --- | --- |
| Translation | $$\begin{cases} x' = x_0 + dx \\ y' = y_0 + dy \end{cases}$$ |
| Rotation | $$\begin{cases} x' = r \cos(\theta) \\ y' = r \sin(\theta) \end{cases}$$ |
| Scaling | $$\begin{cases} x' = k(x - x_0) + x_0 \\ y' = k(y - y_0) + y_0 \end{cases}$$ |
| Mirroring | $$\begin{cases} x' = 2(x_0 - x) + x \\ y' = 2(y_0 - y) + y \end{cases}$$ |

**Note:** The above summary is not exhaustive but covers the core concepts. For a comprehensive understanding, refer to your textbook or other reliable sources.

This theory note should cover all the necessary topics for the GATE CS exam questions involving transformation of shapes.