# Statically Determinate and Indeterminate Structures by Force Energy Method
===========================================================

### Introduction

Structural analysis is a crucial aspect of civil engineering, focusing on determining the forces within structures like beams, frames, and trusses. The force energy method is an approach used to analyze statically indeterminate structures. This note covers the fundamental concepts and principles required to tackle problems in this area.

### Core Concepts

#### Statically Determinate Structures

A structure is said to be statically determinate if it can be analyzed using only the equilibrium equations without requiring any compatibility or strain energy considerations. This means that for a determinate structure, we can find all the internal forces by solving the equilibrium equations.

#### Strain Energy Method (Force Energy Method)

The force energy method, also known as the strain energy method, is used to analyze statically indeterminate structures. It is based on the concept of strain energy stored in the members due to bending and axial loads. The total potential energy of a structure is equated with its internal work done by external forces, leading to the compatibility equations.

#### Potential Energy

Potential energy can be defined as the capacity for doing work possessed by an object or system due to its position, configuration, or state. It has two components:

- **Strain Energy**: The energy stored in a member due to bending and axial loads.
- **Potential Energy Due to External Forces**: The potential energy of external forces.

#### Work Done by External Forces

The work done by an external force is given by the product of its magnitude and the displacement of its point of application. For external forces acting on a structure, the total work done is equated with the change in strain energy or potential energy.

### Key Formulas/Theorems

\[
U = \frac{1}{2} \int_{0}^{L} EI \left( \frac{d^2 y}{dx^2} \right)^2 dx
\]

Strain Energy of a Beam Due to Bending:

\[
U_b = \frac{1}{2} \sum F_i y_i
\]

### Problem Solving Patterns

When tackling problems related to statically indeterminate structures using the force energy method, consider the following steps:

1.  **Draw and label the structure**: Ensure all forces and supports are clearly identified.
2.  **Determine the type of problem**: Whether it is a beam, frame, or truss problem, each has its unique analysis approach.
3.  **Apply the strain energy method**: Use the formula for strain energy to find the unknown reactions or stresses in the structure.

### Examples with Solutions

1.  A simply supported beam of length $L$ and flexural rigidity $EI$ carries a uniformly distributed load of intensity $w$. Find the maximum bending moment.

    Solution:

    The maximum bending moment occurs at the midpoint, given by $\frac{wL^2}{8}$.

2.  A frame is subjected to two external loads acting on opposite sides of the frame. Determine the reactions at the supports.

    Solution:

    Apply the strain energy method and equate it with the work done by the external forces to find the unknown reactions.

### Common Pitfalls

-   **Incorrect application of formulas**: Ensure that you apply the correct formula for the problem type.
-   **Neglecting self-weight or axial stiffening**: Always consider these factors in structural analysis unless explicitly stated otherwise.
-   **Not accounting for redundant members**: Identify and remove redundant members to avoid incorrect solutions.

### Quick Summary

*   Statically determinate structures can be analyzed using equilibrium equations only.
*   The force energy method (strain energy method) is used for statically indeterminate structures.
*   Potential energy has two components: strain energy and potential energy due to external forces.
*   Work done by external forces is equated with the change in strain energy or potential energy.

**Additional References**

For a more comprehensive understanding of structural analysis, refer to:

1.  Timoshenko, S., & Young, D. H. (1965). *Theory of Structures*. McGraw-Hill.
2.  Popov, E. P. (1959). *Engineering Mechanics of Solids*.

This note provides a solid foundation for understanding statically determinate and indeterminate structures by the force energy method. Practice problems and more advanced topics in structural analysis are recommended for further study.