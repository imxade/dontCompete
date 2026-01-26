**Stress Analysis**
================

### Introduction

Stress analysis is a fundamental concept in Mechanics of Materials that deals with determining the internal stresses within a material when subjected to external loads. This note will cover the essential principles, formulas, and problem-solving techniques required for GATE CS exam.

### Core Concepts

*   **Stress**: Stress is defined as the force per unit area on an object or material.
*   **Strain**: Strain is the measure of deformation in a material under stress. It's dimensionless and represents the fractional change in length or volume of the material.
*   **Hooke's Law**: Within the proportional limit, stress (σ) is directly proportional to strain (ε): σ = E \* ε, where E is the modulus of elasticity.

### Key Formulas/Theorems

LaTeX:
```latex
\begin{align*}
E &amp;= mc^2 \\
A &amp;= \frac{I}{c} \\
M &amp;= P \cdot a \\
F &amp;= k \cdot x
\end{align*}
```

### Problem Solving Patterns

To solve stress analysis problems, follow these steps:

1.  **Identify the problem type**: Determine whether it's about finding stresses, strains, or deflections.
2.  **Draw a free-body diagram**: Visualize the forces acting on the object.
3.  **Apply equilibrium equations**: Write equations based on Newton's laws of motion (F = ma).
4.  **Use stress formulas**: Apply Hooke's Law and other relevant formulas to calculate stresses.

### Examples with Solutions

**Example 1:**

An L-shaped member ABC is clamped at end A and connected to a pin at end C. The section modulus of the member is the same in both arms. End C is subjected to a horizontal force P, and all deflections are in the plane of the figure.

Given length AB = 4a and length BC = a, find the magnitude and direction of the normal force on the pin from the slot.

**Solution:**

1.  Draw a free-body diagram:
    ```
    +---------------+
    |               |
    |  P          |
    |               |
    +---------------+
            |
            |
            v
    +---------------+
    |               |
    | (pin)        |
    |               |
    +---------------+
            |
            |
            ^
    ```
2.  Apply equilibrium equations:

    The sum of horizontal forces must be zero:
    P - F = 0

    where F is the normal force on the pin.

3.  Use stress formulas:

    We know that section modulus (Z) is the same in both arms. Since the length BC is smaller, we can assume that the moment M at point C due to the applied load P is equal to P \* a.

    Therefore, the normal force F on the pin can be calculated as:
    F = M / Z

4.  Calculate F:

    Given Z = (I / c) and I = (b \* d^3) / 12 for a rectangular section,
    F = P \* a / ((b \* d^3) / (12 \* c))

**Quick Summary**

*   **Stress**: Force per unit area
*   **Strain**: Measure of deformation
*   **Hooke's Law**: σ = E \* ε
*   **Problem-solving steps:** Identify problem type, draw FBD, apply equilibrium equations, and use stress formulas.

### Common Pitfalls

*   Incorrectly assuming that the normal force on the pin is equal to the applied load P.
*   Not considering the section modulus (Z) of the member when calculating stresses.
*   Failing to apply equilibrium equations properly.