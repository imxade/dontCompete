**Equilibrium Equations of Internal Forces in Structures**
===========================================================

### Introduction

The analysis of structures under various loads is a fundamental aspect of engineering mechanics. In this context, equilibrium equations play a crucial role in determining the internal forces within a structure. These forces can lead to stress concentrations, which may cause failure or damage to the structure. Understanding and applying equilibrium equations correctly is essential for designing safe and efficient structures.

### Core Concepts

Internal forces are the forces exerted by the structure on its elements (e.g., beams, columns) due to external loads. Equilibrium equations relate these internal forces to the external loads applied to the system. For a two-force body (a beam or column under axial load), equilibrium is achieved when:

$$\sum F_x = 0 \implies P - A = 0,$$

where $P$ is the external axial load and $A$ is the internal force.

### Key Formulas/Theorems

#### Flexural Rigidity

The flexural rigidity of a beam, denoted by $EI$, plays a critical role in determining its response to bending loads. It is defined as:

$$EI = \frac{1}{36} \int_{-h/2}^{h/2} E(y^4 - 4y^3h + 6y^2h^2) \,dy,$$

where $E$ is the modulus of elasticity and $h$ is the height of the beam.

#### Flexural Equation

The flexural equation for a beam under a uniformly distributed load (UDL) is given by:

$$M(x) = -\frac{w}{24}x^4 + \left(\frac{P}{2}-\frac{w}{24}\right)x^3,$$

where $M(x)$ is the bending moment, $w$ is the UDL intensity, and $P$ is the concentrated load.

### Problem Solving Patterns

To solve problems involving equilibrium equations of internal forces in structures:

1.  Identify the types of loads acting on the structure (e.g., external axial loads, distributed loads).
2.  Determine the reaction forces at supports.
3.  Apply the equilibrium equations to relate internal forces and external loads.
4.  Use free-body diagrams to visualize the system's equilibrium.

### Examples with Solutions

**Example: A beam of length $l$ carries a uniformly distributed load $w$ and a concentrated load $P$. Find the bending moment at a point $x$ from the left end of the beam.**

Solution:

$$M(x) = -\frac{wx^3}{24} + \left(\frac{Px}{2}-\frac{w}{24}\right)x^2.$$

**Example: A rigid bar is subjected to two equal and opposite forces $F$. Find the reaction force at each end.**

Solution:

$$R_1 = R_2 = 0,$$ since there are no net external forces.

### Common Pitfalls

*   Failure to account for moments or couples when applying equilibrium equations.
*   Incorrectly assuming a structure is statically determinate or indeterminate.
*   Neglecting the effects of external loads on internal forces.

### Quick Summary

| Topic | Key Concepts |
| --- | --- |
| Internal Forces | Equilibrium equations, free-body diagrams |
| Flexural Rigidity | Definition, formula |
| Flexural Equation | Bending moment under UDL and concentrated load |
| Problem Solving Patterns | Identify loads, reaction forces, apply equilibrium equations |
| Examples with Solutions | Beam under UDL and concentrated load, rigid bar |
| Common Pitfalls | Moments, statically determinate/indeterminate structures, external loads |

Note: The example questions provided are used to illustrate the application of equilibrium equations in various scenarios. Ensure that you have a clear understanding of these concepts before attempting similar problems on the GATE CS exam.