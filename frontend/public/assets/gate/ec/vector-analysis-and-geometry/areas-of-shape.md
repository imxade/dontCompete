**Areas of Shapes: Vector Analysis and Geometry**
======================================================

### Introduction
The area of a shape can be determined using various methods, including vector analysis and geometry. This topic covers essential concepts and formulas to calculate areas of different shapes.

### Core Concepts
*   **Vector Representation**: Vectors are used to represent points, lines, and planes in space.
    *   A vector $\vec{a}$ can be represented as $(x, y)$ or $(x, y, z)$ depending on the dimensionality of the space.
*   **Distance Formula**: The distance between two points $P(x_1, y_1)$ and $Q(x_2, y_2)$ in a 2D plane is given by:
    $$\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

### Key Formulas/Theorems
*   **Area of a Circle**: The area of a circle with radius $r$ is given by: 
    \[\pi r^2\]

### Problem Solving Patterns
When solving problems involving areas of shapes, consider the following steps:

1.  **Visualize the problem**: Understand the geometric configuration and identify relevant shapes.
2.  **Choose the appropriate formula**: Select a formula that applies to the specific shape or scenario.
3.  **Apply the formula**: Substitute values into the chosen formula to calculate the area.

### Examples with Solutions

**Example 1: Area of a Circle**
A circle has a radius of 4 units. Find its area.

Solution:
\[\text{Area} = \pi r^2\]
\[= \pi (4)^2\]
\[= 16\pi\]

**Example 2: Rectangle in a Circle**

Given the figure below, where $O$ is the center of the circle and $PQRS$ is a rectangle inscribed in the circle with maximum possible area:

A) $\frac{1}{2}a^2 \pi - 4$
B) $\frac{1}{2}a^2 \pi - 3\sqrt{2}$
C) $\frac{1}{2}a^2 \pi - 8$
D) $\frac{1}{2}a^2 \pi - 16$

To find the area of the shaded portion, we first need to find the area of the rectangle and subtract it from the area of the circle.

The diameter of the circle is $2r$, where $r$ is the radius. The diagonal of the rectangle is equal to the diameter of the circle.

Using the Pythagorean theorem on the right-angled triangle formed by the radius, half of the rectangle's side, and half of the rectangle's other side:

\[a^2 = (x/2)^2 + (y/2)^2\]

Solving for $x$ and $y$, we get:
\[ x = \frac{a}{\sqrt{2}} \]
\[ y = \frac{a}{\sqrt{2}} \]

Thus, the area of the rectangle is given by: 
\[ xy = \left(\frac{a}{\sqrt{2}}\right) \left(\frac{a}{\sqrt{2}}\right)\]
\[ = \frac{1}{2} a^2 \]

The area of the shaded region is the difference between the area of the circle and the area of the rectangle:

\[ A_{\text{shaded}} = A_{\text{circle}} - A_{\text{rectangle}} \]
\[ = \pi r^2 - \frac{1}{2} a^2 \]
\[ = \pi a^2 - \frac{1}{2} a^2 \]
\[ = \left(\pi - \frac{1}{2}\right) a^2\]

Hence, the correct answer is $\boxed{\left(\pi - \frac{1}{2}\right) a^2}$.

However, none of the options match this expression. Let's re-evaluate our solution:

The area of the rectangle $PQRS$ can be found using the formula for the area of a square:
\[ A_{\text{rectangle}} = xy \]
Given that $O$ is the center and $a$ is the radius, the diagonals are equal to $2r$, which implies that $x= y = \sqrt{2} r$. Therefore,
\[ A_{\text{rectangle}} = (\sqrt{2}r)^2 \]
\[ = 2r^2 \]

The area of the shaded region is the difference between the area of the circle and twice the area of the rectangle:
\[ A_{\text{shaded}} = \pi r^2 - 2(2r^2) \]
\[ = \pi r^2 - 4r^2 \]
\[ = (\pi-4)r^2 \]

Thus, the correct answer is $\boxed{\left(\pi-4\right)a^2}$.

Since $a$ is the radius of the circle and equal to $r$, we can express this as:
\[ A_{\text{shaded}} = (\pi - 4) a^2 \]

### Common Pitfalls
*   Misunderstanding the geometric configuration.
*   Applying the wrong formula for the specific shape or scenario.

### Quick Summary

*   **Key Formulas:**
    *   Area of a circle: $\pi r^2$
*   **Problem Solving Patterns:**
    1.  Visualize the problem
    2.  Choose the appropriate formula
    3.  Apply the formula
*   **Common Pitfalls:** Misunderstanding geometric configurations and applying incorrect formulas.

### Additional Resources

For further study, refer to standard geometry and trigonometry textbooks or online resources that cover vector analysis and geometry.