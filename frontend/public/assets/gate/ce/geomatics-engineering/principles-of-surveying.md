**Principles of Surveying**
==========================

### Introduction
-----------------

Surveying plays a crucial role in geomatics engineering, enabling accurate measurement and mapping of the Earth's surface. This topic covers fundamental principles, laws, and algorithms essential for solving various surveying-related problems.

### Core Concepts
------------------

#### 1. **Angular Measurement**

In surveying, angles are measured between two lines or planes using instruments like theodolites. The instrument axis is related to the reference level (RL), which serves as a fundamental concept in surveying.

#### 2. **Trigonometry and Triangulation**

Surveyors employ trigonometric relationships and triangulation methods for precise measurements of distances, heights, and angles.

### Key Formulas/Theorems
-------------------------

- **Sine Rule:**
\[ \frac{a}{\sin(A)} = \frac{b}{\sin(B)} = \frac{c}{\sin(C)} \]
- **Cosine Rule:**
\[ c^2 = a^2 + b^2 - 2ab\cos(C) \]

### Problem Solving Patterns
---------------------------

1.  **Theodolite Measurement:** Given the angle of elevation to a staff and the RL, calculate the distance between stations A and B.
    Example:

    Suppose $E = (212.250)$ m, $\alpha = 7^{\circ}$, and $d = 4$ m. Calculate the RL at station B.

    \[ RL_B = E + d\sin(\alpha) = 212.250 + 4 \cdot \sin(7^{\circ}) \approx 212.281 \]
2.  **Bearing and Azimuth:** Determine the bearing of a survey given its azimuth observed from north.
    Example:

    Suppose $Az = 231^{\circ}$. Calculate the bearing.

    \[ Bearing = Az + 90^{\circ} = 321^{\circ} \]

### Examples with Solutions
---------------------------

1.  **Q1 Solution:** (Round off to three decimal places)

    We have, $E = 212.250$ m and $\alpha = 7^{\circ}$.

    The horizontal distance is given by:

    \[ d = \frac{4}{\tan(\alpha)} = \frac{4}{\tan(7^{\circ})} = 400.0 \text{ m} \]

    To find the RL at station B, we use:

    \[ RL_B = E + d\sin(\alpha) = 212.250 + (400)(\sin(7^{\circ})) = 257.360 \]

2.  **Q2 Solution:**

    Given the bearing of a survey, we can determine its azimuth observed from north.

    Suppose $Bearing = 231^{\circ}$. Then,

    \[ Azimuth = Bearing - 90^{\circ} = 231 - 90 = 141^{\circ} \]

### Common Pitfalls
-------------------

-   **Neglecting Errors:** Always consider the effects of curvature and refraction when making precise measurements.
-   **Misinterpretation of Formulas:** Ensure to use the correct trigonometric relationships for a given problem.

### Quick Summary
------------------

*   **Theodolite Measurement:**
    *   $\alpha$: Angle of elevation to staff
    *   $E$: RL of instrument axis
    *   $d$: Distance between stations A and B
*   **Bearing and Azimuth:**
    *   $Az$: Azimuth observed from north
    *   $Bearing = Az + 90^{\circ}$

Please note that the source questions provided do not directly relate to the topics of line symmetry, mirror images, or fractions. For these specific topics, refer to standard geometry and algebra textbooks.