**Solid Mechanics: Bending Moment and Shear Force in Statically Determinate Beams**
====================================================================================

### Introduction
Structural analysis of beams under various loads is a fundamental concept in solid mechanics. This note covers the theoretical aspects of bending moment, shear force, simple stress and strain relationships, simple bending theory, flexural and shear stresses, shear center, uniform torsion, transformation of stress, and buckling of columns.

### Core Concepts

#### Bending Moment and Shear Force
---------------------------

The bending moment (`M`) and shear force (`V`) are the primary forces acting on a beam under load. The bending moment is defined as the product of the force applied to the beam and the distance from the point of application to the section being analyzed.

LaTeX Equation: $M = F \times d$

#### Simple Stress and Strain Relationships
----------------------------------------

The relationship between stress (`σ`) and strain (`ε`) for a material under uniaxial loading is given by Hooke's Law:

LaTeX Equation: $\sigma = E \cdot \varepsilon$

where `E` is the modulus of elasticity.

#### Simple Bending Theory
-------------------------

For a beam subjected to bending, the maximum stress occurs at the neutral axis. The bending stress (`σ`) can be calculated using the following equation:

LaTeX Equation: $\sigma = \frac{M \cdot y}{I}$

where `y` is the distance from the neutral axis to the point of interest and `I` is the moment of inertia.

#### Flexural and Shear Stresses
------------------------------

Flexural stresses occur due to bending, while shear stresses occur due to shearing forces. The maximum flexural stress (`σ_f`) and shear stress (`τ_s`) can be calculated using the following equations:

LaTeX Equation: $\sigma_f = \frac{M}{I} \cdot y$

LaTeX Equation: $\tau_s = \frac{V \cdot z}{I}$

where `z` is the distance from the neutral axis to the point of interest.

#### Shear Center
-----------------

The shear center is a point in a beam where the sum of the bending moments and shear forces applied to the beam is zero. The location of the shear center depends on the cross-sectional geometry of the beam.

### Key Formulas/Theorems

*   Bending moment: $M = F \times d$
*   Simple stress and strain relationship: $\sigma = E \cdot \varepsilon$
*   Flexural stress: $\sigma_f = \frac{M}{I} \cdot y$
*   Shear stress: $\tau_s = \frac{V \cdot z}{I}$

### Problem Solving Patterns

*   Identify the type of load (tension, compression, bending) and its magnitude
*   Determine the neutral axis and calculate the distance to the point of interest
*   Calculate the moment of inertia (`I`) for the beam's cross-section
*   Use the formulas for flexural and shear stresses to calculate the maximum stress at various points in the beam

### Examples with Solutions

**Example 1:** A simply supported beam with a point load at its midspan has a length of 10 m, a width of 0.2 m, and a height of 0.5 m. The point load is 500 N.

1.  Calculate the bending moment (`M`) at the midpoint.
    $M = F \times d = 500 \text{ N} \times 5 \text{ m} = 2500 \text{ Nm}$
2.  Determine the distance from the neutral axis to the top and bottom fibers for a rectangular beam:
    $y_{top} = \frac{h}{2} = \frac{0.5 \text{ m}}{2} = 0.25 \text{ m}$
    $y_{bottom} = h - y_{top} = 0.5 \text{ m} - 0.25 \text{ m} = 0.25 \text{ m}$
3.  Calculate the maximum flexural stress at the top and bottom fibers:
    $\sigma_f = \frac{M}{I} \cdot y$

**Example 2:** A beam with a rectangular cross-section is subjected to a shearing force of 100 N and has dimensions: length (`l`) = 10 m, width (`b`) = 0.2 m, height (`h`) = 0.5 m.

1.  Determine the distance from the neutral axis to the point where the maximum shear stress occurs:
    $z = \frac{h}{2} = \frac{0.5 \text{ m}}{2} = 0.25 \text{ m}$
2.  Calculate the maximum shear stress at that point:
    $\tau_s = \frac{V \cdot z}{I}$

### Common Pitfalls

*   Forgetting to account for the sign of bending moment and shear force
*   Incorrectly determining the neutral axis or distance to the point of interest
*   Failing to calculate the moment of inertia (`I`) correctly

### Quick Summary

*   Bending moment: $M = F \times d$
*   Flexural stress: $\sigma_f = \frac{M}{I} \cdot y$
*   Shear stress: $\tau_s = \frac{V \cdot z}{I}$
*   Moment of inertia (`I`): depends on the cross-sectional geometry
*   Neutral axis and distance to point of interest depend on beam's geometry