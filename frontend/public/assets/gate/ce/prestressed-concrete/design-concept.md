Design Concept: Prestressed Concrete
=====================================

Introduction
------------

Prestressed concrete (PC) is a form of reinforced concrete where the concrete is subjected to compressive stresses before being exposed to external loads. This is achieved through the use of high-strength tendons made of steel or other materials that are stretched and then anchored within the concrete.

Core Concepts
--------------

### Principles of Prestressing

Prestressed concrete relies on the principle of superposition, where the prestressing forces and the external loads combine to produce a state of equilibrium. The prestressing force is designed to counteract the tensile stresses caused by the external loads, thus preventing cracking and enhancing durability.

#### Types of Prestressing

There are two primary types of prestressing:

1.  **Internal Prestressing**: Where tendons are embedded within the concrete.
2.  **External Prestressing**: Where pre-stressed members are connected to each other using anchorages.

### Behavior of Prestressed Concrete

Under external loads, prestressed concrete exhibits several behaviors:

*   **Initial Deformation**: The concrete undergoes a small deformation due to the prestressing force before being subjected to external loads.
*   **Stress Redistribution**: As the external load is applied, stresses redistribute within the concrete, resulting in compressive stresses in regions where tensile stresses were initially present.

Key Formulas/Theorems
----------------------

### Bending Moment Calculation

Given:

*   External Load: P (kN)
*   Distance from Support to Point Q: L (m)
*   Depth of Section: d (mm)
*   Width of Section: b (mm)

The bending moment at point Q can be calculated using the formula:

$$M_Q = \frac{P \cdot L}{2} + P \left(\frac{d^2}{4}\right) - W \left(\frac{L^3}{24}\right)$$

where $W$ is the self-weight of the section.

Problem Solving Patterns
-------------------------

### Analyzing Prestressed Concrete Beams

When solving problems involving prestressed concrete beams, follow these steps:

1.  **Draw a Diagram**: Visualize the beam and prestressing tendon.
2.  **Identify Forces**: Calculate the forces acting on the beam due to the external load and prestressing force.
3.  **Calculate Stresses**: Determine the stresses at critical points using formulas like those above.

Examples with Solutions
-----------------------

### Example: Q1 (ID: ce_2021-M_43)

Given:

*   Prismatic Cantilever Beam with Span Length L = 1.5 m
*   Straight Tendon with Total Prestressing Force of 50 kN Applied at 50 mm from Top
*   Concentrated Load P = 5 kN

To find the resultant stress experienced at point 'Q':

1.  Calculate the bending moment:

    $$M_Q = \frac{P \cdot L}{2} + P \left(\frac{d^2}{4}\right) - W \left(\frac{L^3}{24}\right)$$

    Given values:

    *   $P$ = 5 kN
    *   $L$ = 1.5 m
    *   $d$ = 300 mm (depth of section)
    *   $W$ = self-weight of the section

2.  Determine the stress at point Q using the formula:

    $$\sigma_Q = \frac{M_Q}{I}$$

where $I$ is the moment of inertia of the section.

Common Pitfalls
-----------------

*   **Incorrect Calculation**: Double-check calculations for bending moments and stresses.
*   **Misinterpretation of Diagrams**: Clearly understand the orientation and placement of prestressing tendons and external loads.

Quick Summary
--------------

*   Prestressed concrete relies on superposition to counteract tensile stresses caused by external loads.
*   Bending moment calculation is critical in determining stresses at various points within a beam.
*   Analyze forces, calculate stresses, and ensure clear understanding of diagrams when solving problems involving prestressed concrete beams.