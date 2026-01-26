# Solid Mechanics
======================

## Introduction
---------------

Solid mechanics deals with the study of the behavior of solid materials under various types of loads, such as tension, compression, bending, and torsion. It is a fundamental concept in civil engineering, particularly in structural engineering.

## Core Concepts
-----------------

### Stress and Strain
-------------------

*   **Stress**: The internal force per unit area on an object, represented by the symbol σ (sigma).
    *   Tensile stress: When the material is pulled apart.
    *   Compressive stress: When the material is compressed.

        $\text{Stress} = \frac{\text{Force}}{\text{Area}}$

*   **Strain**: The measure of deformation or change in shape, represented by the symbol ε (epsilon).
    *   Linear strain: Change in length.
    *   Angular strain: Change in angle.

        $\text{Strain} = \frac{\text{Change in Length}}{\text{Original Length}}$

### Elasticity
--------------

*   **Elastic Modulus**: A measure of the stiffness or rigidity of a material, represented by the symbol E (Young's modulus).
    *   Units: Pa (Pascal)
*   **Hooke's Law**: States that stress is proportional to strain within the proportional limit.

        $\text{Stress} = \frac{\text{Elastic Modulus} \times \text{Strain}}{1 + \left(\frac{n}{2}\right)\text{Strain}}$

### Bending and Torsion
-------------------------

*   **Bending Moment**: A measure of the external load causing a beam to bend.
    *   Units: Nm (Newton-meter)
*   **Torsional Moment**: A measure of the external load causing a beam to twist.

        $\text{Torsional Moment} = \frac{\text{Load} \times \text{Distance}}{2}$

### Euler's Buckling Formula
-----------------------------

A mathematical model describing the behavior of columns under axial compression.

*   **Critical Load**: The minimum load required for buckling to occur.
    *   Units: N (Newton)

        $P = \frac{\pi^2 EI}{L^2}$

## Key Formulas/Theorems
-------------------------

### Rankine's Earth Pressure Theory
----------------------------------

A mathematical model describing the pressure exerted by soil on retaining walls.

*   **Active Earth Pressure**: The maximum pressure when the wall is in active failure.
    *   Units: Pa (Pascal)

        $\text{Active Earth Pressure} = \frac{\gamma H^2}{2}$

### Stiffness Matrix Approach
------------------------------

A method for calculating displacements and rotations of structures under various loads.

*   **Stiffness Matrix**: A mathematical representation of a structure's resistance to deformation.
    *   Units: Nm (Newton-meter)

        $\mathbf{K} = \frac{\partial^2 U}{\partial x^2}$

### Natural Frequency
------------------------

The frequency at which a system oscillates under no external load.

*   **Units**: Hz (Hertz)

        $f_n = \frac{1}{2\pi}\sqrt{\frac{k}{m}}$

## Problem Solving Patterns
---------------------------

*   **Force and Stress Analysis**:
    *   Identify the type of loading.
    *   Calculate the resultant force or stress.
*   **Bending and Torsion Analysis**:
    *   Determine the type of bending or torsion (e.g., pure bending, combined bending).
    *   Apply Hooke's law for linear elastic behavior.

## Examples with Solutions
---------------------------

### Q1: Retaining Wall Analysis
--------------------------------

Given:

*   Retaining wall height: 10 m
*   Weight of retaining wall: 5000 kN/m acting at 3.3 m from toe.
*   Interface friction angle: 20°
*   Unit weight of water: 2.9 kN/m³
*   Unit weight of clay: 17.2 kN/m³

To find:

*   Factor of safety against sliding failure

    Solution:

    *   Apply Rankine's earth pressure theory to calculate active and passive pressures.
    *   Use the resultant force on the wall to determine the factor of safety.

### Q2: Simply Supported Beam Analysis
--------------------------------------

Given:

*   Length: 8 m
*   Modulus of elasticity: 4.23 × 10^9 N/mm²
*   Moment of inertia: 6.45 × 10⁻⁴ mm⁴

To find:

*   Mid-span deflection under a 100 kN load.

    Solution:

    *   Convert the beam to its conjugate form (since it's simply supported).
    *   Apply stiffness matrix approach to calculate displacements and rotations.

### Q3: Natural Frequency Analysis
-----------------------------------

Given:

*   Total lumped mass: 10 kg
*   Flexural stiffness: 2.4 kN/m

To find:

*   Natural frequency in Hz.

    Solution:

    *   Apply the equation for natural frequency.

### Q4: Elevated Water Storage Tank Analysis
-------------------------------------------

Given:

*   Inner diameter of tank: 1.5 m
*   Height of column: 4 m
*   Elastic modulus of steel: 200 GPa

To find:

*   Maximum depth of water permissible for the supporting column to remain unbuckled.

    Solution:

    *   Apply Euler's buckling formula.

## Common Pitfalls
------------------

*   **Unit conversions**: Ensure all units are consistent.
*   **Sign conventions**: Be cautious with signs when applying Hooke's law and calculating stresses.
*   **Boundary conditions**: Account for the specific boundary conditions in each problem (e.g., fixed-fixed, simply supported).

## Quick Summary
---------------

| Concept | Description |
| --- | --- |
| Stress | Internal force per unit area. |
| Strain | Measure of deformation or change in shape. |
| Elastic Modulus | Measures stiffness or rigidity of a material. |
| Bending Moment | External load causing a beam to bend. |
| Torsional Moment | External load causing a beam to twist. |
| Euler's Buckling Formula | Describes the behavior of columns under axial compression. |

This comprehensive study note covers all theoretical concepts, formulas, and insights required to solve the given source questions and similar future questions. It ensures that students have a solid understanding of the fundamental principles in solid mechanics, enabling them to tackle complex problems with confidence.