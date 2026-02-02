**Engineering Mechanics - Structural Engineering**
=====================================================

### Introduction
-----------------

Structural engineering involves the analysis and design of structures such as buildings, bridges, and towers to ensure their safety and stability under various loads. This topic will cover key concepts in structural engineering, including equilibrium, degrees of freedom, and static and kinematic indeterminacy.

### Core Concepts
------------------

#### Equilibrium

*   A body is said to be in equilibrium if the net force acting on it is zero.
*   For a two-dimensional problem, we need to consider only two equations of equilibrium: ΣF_x = 0 and ΣF_y = 0.
*   In three dimensions, we have six equations of equilibrium: three for forces (ΣF_x = 0, ΣF_y = 0, ΣF_z = 0) and three for moments (ΣM_x = 0, ΣM_y = 0, ΣM_z = 0).

#### Degrees of Freedom

*   The number of independent displacements required to specify the position and orientation of a body in space.
*   For a rigid body, there are six degrees of freedom: three translational (x, y, z) and three rotational (α_x, α_y, α_z).
*   The degree of indeterminacy is the difference between the number of unknowns and the number of equations.

#### Static Indeterminacy

*   A structure is said to be statically indeterminate if there are more unknown forces than equations of equilibrium.
*   The degree of static indeterminacy is equal to the difference between the number of unknown forces and the number of equations of equilibrium.

#### Kinematic Indeterminacy

*   A structure is said to be kinematically indeterminate if it can move in more ways than it actually does.
*   The degree of kinematic indeterminacy is equal to the difference between the number of degrees of freedom and the number of constraints.

### Key Formulas/Theorems
---------------------------

#### Equilibrium

$$\sum F_x = 0, \sum F_y = 0, \sum F_z = 0$$

$$\sum M_x = 0, \sum M_y = 0, \sum M_z = 0$$

#### Degrees of Freedom

*   Six degrees of freedom for a rigid body:
    *   Three translational (x, y, z)
    *   Three rotational (α_x, α_y, α_z)

### Problem Solving Patterns
---------------------------

1.  **Draw the FBD**: Draw a free-body diagram to represent the forces acting on the system.
2.  **Write down equations of equilibrium**: Write down the equations of equilibrium based on the FBD.
3.  **Solve for unknowns**: Solve for the unknown forces or displacements using the equations of equilibrium.

### Examples with Solutions
---------------------------

**Example 1: Equilibrium**

A beam is fixed at one end and hinged at the other end, with a load applied at the midpoint. Find the reaction force at the fixed end.

*   Draw the FBD:
    ```mermaid
    graph LR
    A[Fixed End] --> B[Middle Load]
    C[Hinged End] -->
    ```
*   Write down equations of equilibrium:
    $$\sum F_x = 0, \sum F_y = 0$$

**Solution**

*   Solve for the reaction force at the fixed end.

### Common Pitfalls
-------------------

1.  **Incorrectly assuming symmetry**: Don't assume that a system has symmetry if it doesn't.
2.  **Forgetting to include moments**: Include all moments when solving equilibrium problems.
3.  **Not checking units**: Check units for consistency in your calculations.

### Quick Summary
------------------

*   Equilibrium: six equations of equilibrium (three forces, three moments)
*   Degrees of freedom: six degrees of freedom for a rigid body
*   Static indeterminacy: difference between unknown forces and equations of equilibrium
*   Kinematic indeterminacy: difference between degrees of freedom and constraints

### Additional Resources
------------------------

For further study, consult the following resources:

1.  [Wikipedia - Equilibrium](https://en.wikipedia.org/wiki/Equilibrium_(physics))
2.  [Wikipedia - Degrees of Freedom](https://en.wikipedia.org/wiki/Degrees_of_freedom)
3.  [Khan Academy - Mechanics](https://www.khanacademy.org/science/mechanics)