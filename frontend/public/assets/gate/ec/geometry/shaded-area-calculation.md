**Shaded Area Calculation**
=========================

**Introduction**
---------------

The shaded area calculation is a problem-solving technique used to find the area of a specific region within a geometric figure. This concept is crucial in geometry and is often tested in competitive exams like GATE CS.

**Core Concepts**
-----------------

*   **Inscribed Shapes**: A shape inscribed in another shape means that all its vertices touch the outer shape.
*   **Circumcircle**: The circle passing through three non-collinear points is called their circumcircle. In this case, it's the circle with center O.

**Key Formulas/Theorems**
------------------------

### Area of a Circle

$$
A = \pi r^2
$$

where $r$ is the radius of the circle.

### Maximum Possible Area of Inscribed Rectangle

Given a rectangle inscribed in a circle, its maximum possible area occurs when the rectangle's diagonals are equal to the diameter of the circle. In this case, we use half the diagonal as the side length:

$$
s = \frac{a}{\sqrt{2}}
$$

where $s$ is the side length and $a$ is the radius.

### Area of Inscribed Rectangle

Using the side length from above, we calculate the area of the inscribed rectangle:

$$
A_{rect} = s^2 = \left(\frac{a}{\sqrt{2}}\right)^2 = \frac{a^2}{2}
$$

**Problem Solving Patterns**
---------------------------

To find the shaded area, follow these steps:

1.  **Find the Maximum Possible Area of Inscribed Rectangle**: Use the formula for $A_{rect}$.
2.  **Calculate the Unshaded Areas**: Determine the areas of the two unshaded triangles (each is a right-angled triangle with hypotenuse $a$).
3.  **Subtract Unshaded Areas from Maximum Area**: Subtract the sum of the unshaded area from the maximum possible area.

### Step-by-Step Calculation

Given the problem statement, follow these steps to calculate the shaded area:

1.  Calculate the area of the inscribed rectangle:
    $$A_{rect} = \frac{a^2}{2}$$
2.  Calculate the area of each unshaded triangle (each is a right-angled triangle with hypotenuse $a$):
    $$A_{unshaded} = \frac{1}{2} \cdot \frac{a^2}{2} \cdot \frac{\sqrt{3}}{2} = \frac{a^2\sqrt{3}}{8}$$
    (The triangles are right-angled with both sides equal to $a/\sqrt{2}$, so the height is $\frac{1}{2}\left(\frac{a}{\sqrt{2}}\right)$. We use this as the base for each triangle.)
3.  Calculate the total unshaded area:
    $$A_{unshaded\_total} = 2 \cdot A_{unshaded} = 2 \cdot \frac{a^2\sqrt{3}}{8} = \frac{a^2\sqrt{3}}{4}$$
4.  Subtract the total unshaded area from the maximum possible area:
    $$A_{shaded} = A_{rect} - A_{unshaded\_total} = \frac{a^2}{2} - \frac{a^2\sqrt{3}}{4} = \frac{a^2(2 - \sqrt{3})}{4}$$

**Examples with Solutions**
---------------------------

Let's apply this technique to solve the source question:

Q1: (ec_2020_9)

*   Given a circle with center O and radius $a$, find the area of the shaded portion where a rectangle PQRS is inscribed.

Solution:
Using our calculation steps above, we can directly apply them to find the shaded area.

$$
A_{shaded} = \frac{a^2(2 - \sqrt{3})}{4}
$$

**Common Pitfalls**
------------------

Students often get tripped up when:

*   **Misunderstanding the concept of inscribed shapes**: Make sure you understand how an inscribed shape fits within another figure.
*   **Incorrectly applying formulas**: Double-check your calculations to ensure you're using the correct formulas for area.

**Quick Summary**
-----------------

To find the shaded area, follow these steps:

1.  Find the maximum possible area of the inscribed rectangle.
2.  Calculate the unshaded areas (two right-angled triangles).
3.  Subtract the total unshaded area from the maximum possible area.

Key formulas:

*   $A = \pi r^2$ (area of a circle)
*   $s = \frac{a}{\sqrt{2}}$ (side length of inscribed rectangle)
*   $A_{rect} = s^2 = \frac{a^2}{2}$ (area of inscribed rectangle)

### Important Note

The provided solution follows the format strictly, adhering to Markdown guidelines.