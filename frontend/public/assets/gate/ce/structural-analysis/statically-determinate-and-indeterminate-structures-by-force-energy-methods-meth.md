**Statically Determinate and Indeterminate Structures by Force Energy Methods Method of Superposition**
==============================================

### Introduction
---------------

Structural analysis is a crucial aspect of engineering, dealing with the study of physical systems or structures that are subjected to various types of loads. Statically determinate and indeterminate structures are classified based on their ability to be analyzed using the principles of static equilibrium. The force energy methods provide an alternative approach to analyzing these structures by relating the internal forces and deformations to the external loads applied.

### Core Concepts
----------------

#### Statically Determinate Structures
------------------------------------

A statically determinate structure is one where the support reactions can be determined using only the equations of static equilibrium (equilibrium in all 3 planes: X, Y, and Z). The internal forces in a member can also be found using these same principles.

**Example**
```mermaid
graph LR
A[Point A] --> B[Support 1]
B --> C[Beam]
C --> D[Support 2]
```
The beam is statically determinate if the reactions at supports 1 and 2 can be determined by solving equilibrium equations only.

#### Indeterminate Structures
---------------------------

An indeterminate structure, on the other hand, has more unknowns than available equations. The internal forces cannot be found solely from static equilibrium conditions. Additional equations are required to determine these forces accurately.

**Visual Representation**
```mermaid
graph LR
A[Point A] --> B[Support 1]
B --> C[Pinned Beam]
C --> D[Support 2]
```
If the beam is pinned at both ends and has more unknowns than can be solved for by static equilibrium alone, it's an indeterminate structure.

#### Force Energy Methods
------------------------

These methods relate the internal forces in a member to the external loads through energy equations. For linear elastic systems under small deformations, the total potential energy of the system is equal to the work done by external forces minus the strain energy stored within the material.

**Key Equation**
\[ U = \frac{1}{2}Fw + \frac{1}{2}Wd \]

Where:
- \(U\) is the strain energy,
- \(F\) and \(W\) are the loads applied at a distance \(w\) and \(d\), respectively.

### Method of Superposition
---------------------------

This method involves applying external loads in sequence or simultaneously. The response (displacements, forces) can be determined by adding up individual responses due to each load applied, assuming linear behavior.

**Key Principle**
The principle states that the total displacement at a point under multiple loads is equal to the sum of displacements caused by each load applied individually.

### Key Formulas/Theorems
-------------------------

#### Castigliano's Theorem

Castigliano’s theorem relates the derivative of the potential energy with respect to any force in the structure to the deflection at that force application point.

**Key Equation**
\[ \frac{\partial U}{\partial F} = w \]

Where:
- \(w\) is the work done by load \(F\).

#### Maxwell-Betti's Reciprocal Work Theorem

This theorem relates the forces in a structure to its displacements under different loads, facilitating the use of superposition in solving indeterminate structures.

**Key Equation**
\[ \frac{F_1}{d_2} = \frac{F_2}{d_1} \]

Where:
- \(d_1\) and \(d_2\) are the deflections caused by load \(F_1\) and \(F_2\), respectively.

### Problem Solving Patterns
-----------------------------

#### Step-by-Step Solution

1.  **Understand the problem**: Identify if it involves statically determinate or indeterminate structures.
2.  **Determine the method to use**: Decide between static equilibrium equations, force energy methods (Castigliano's theorem, Maxwell-Betti’s reciprocal work theorem), and superposition for solving the structure under given loads.
3.  **Apply appropriate formulas**: Use Castigliano’s theorem or Maxwell-Betti’s theorem as needed for energy or displacement calculations in indeterminate structures.

### Examples with Solutions
---------------------------

**Example Q1**

A prismatic steel beam is shown. The plastic moment, \(M_p\), calculated for collapse mechanism using static method and kinematic method is:

\[ M_{pstatic} = \frac{PL}{2}, \quad M_{pkinematic} = \frac{3PL}{4} \]

Using Castigliano’s theorem:

\[ U = \int_0^L \frac{M^2}{EI} dx \]
We find the plastic moment where it reaches a maximum.

**Solution**
The plastic moment is given by:

\[ M_p = \sqrt{\frac{3PEIL}{S}} \]

Where:
- \(P\) is the external load,
- \(E\), \(I\), and \(L\) are the modulus of elasticity, moment of inertia, and length of the beam respectively.

Substituting known values for plastic moments:

\[ M_{pstatic} = \frac{PL}{2}, \quad M_{pkinematic} = \frac{3PL}{4} \]

And comparing both values to see which one is correct for collapse mechanism gives us our answer: \(M_p\) should equal the smaller of the two values.

### Common Pitfalls
-------------------

-   **Misunderstanding static and indeterminate structures**: Ensure you can differentiate between the two based on equations required.
-   **Incorrect application of energy methods**: Always ensure to derive formulas from first principles for accurate results.
-   **Ignoring superposition principle**: Be careful not to overlook its utility in solving complex problems.

### Quick Summary
-----------------

-   Statically determinate structures have enough equilibrium equations for finding support reactions and internal forces without additional equations.
-   Indeterminate structures need more information (e.g., displacements) in addition to static equilibrium conditions.
-   Force energy methods provide an alternative approach, focusing on the relationship between internal forces and external loads through potential energy.
-   Superposition principle allows the response to multiple loads to be found by adding responses due to each load applied individually.

Note: This content is for educational purposes only. Always consult up-to-date textbooks or professional resources for detailed information on structural analysis topics.