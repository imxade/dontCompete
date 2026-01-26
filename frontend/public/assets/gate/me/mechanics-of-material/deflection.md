**Deflection of Beams**
=======================

### Introduction

Deflection of beams is a fundamental concept in Mechanics of Materials, which deals with the analysis and design of structures under various loads. Deflection refers to the displacement of a beam's neutral axis from its original position due to external loads.

### Core Concepts

When a beam is subjected to an external load, it experiences stress and strain. The flexural rigidity (EI) of a beam determines its ability to resist deflection. EI is a product of the modulus of elasticity (E) and the moment of inertia (I) of the beam's cross-section.

#### Moment of Inertia

The moment of inertia (I) is a measure of an object's resistance to changes in its rotation. For a rectangular beam with width (b) and depth (h), I is given by:

$$
I = \frac{1}{12}bh^3
$$

#### Modulus of Elasticity

The modulus of elasticity (E) represents the ratio of stress to strain within the proportional limit of a material. It can be determined experimentally or obtained from tables.

### Key Formulas/Theorems

**Bending Moment**

The bending moment (M) at any point on a beam is given by:

$$
M = F \cdot x
$$

where F is the external load and x is the distance from the point of application to the point under consideration.

**Deflection Formula**

For a cantilever beam with end moment M, the deflection (δ) at a distance x from the fixed end is given by:

$$
\delta = \frac{Mx^2}{EI}
$$

### Problem Solving Patterns

When solving problems involving deflection, follow these steps:

1.  Determine the type of beam (e.g., cantilever, simply supported) and any relevant boundary conditions.
2.  Calculate the bending moment at the point of interest using the formula: $M = F \cdot x$.
3.  Use the deflection formula to calculate the displacement at that point.

### Examples with Solutions

#### Example 1: Cantilever Beam Deflection

A cantilever beam with length L and flexural rigidity EI is subjected to an end moment M. Find the deflection at a distance x from the fixed end.

$$
\delta = \frac{Mx^2}{EI}
$$

For a cantilever beam, the bending moment (M) is equal to the applied load F times the length L:

$$
M = FL
$$

Substituting this into the deflection formula gives:

$$
\delta = \frac{FLx^2}{EI}
$$

#### Example 2: Simply Supported Beam Deflection

A simply supported beam with length L and flexural rigidity EI is subjected to a uniformly distributed load (SDL) w. Find the maximum deflection at the midpoint.

The bending moment (M) for a simply supported beam under SDL can be calculated as:

$$
M = \frac{wL^2}{8}
$$

Substituting this into the deflection formula gives:

$$
\delta_{max} = \frac{5wL^4}{384EI}
$$

### Common Pitfalls

*   Forgetting to account for boundary conditions (e.g., fixed or simply supported ends).
*   Misidentifying the type of beam (e.g., cantilever vs. simply supported).
*   Failing to use the correct formula for deflection (e.g., neglecting to include EI).

### Quick Summary

*   Deflection is a measure of a beam's displacement due to external loads.
*   Flexural rigidity (EI) determines a beam's resistance to deflection.
*   Bending moment (M) can be calculated using the formula: $M = F \cdot x$.
*   Deflection at any point on a beam is given by: $\delta = \frac{Mx^2}{EI}$.

Note: This theory note provides a comprehensive overview of deflection, including key formulas and problem-solving patterns. Make sure to practice solving problems using the concepts covered here.