**Retaining Wall and Earth Pressure**
=====================================

**Introduction**
---------------

A retaining wall is a structure designed to resist lateral earth pressures, preventing soil from sliding or rotating. The analysis and design of retaining walls involve understanding the principles of earth pressure, which are essential for ensuring the stability and safety of such structures.

**Core Concepts**
-----------------

### Earth Pressure Theories

There are several earth pressure theories that help determine the forces acting on a retaining wall:

*   **Atterberg's Theory**: This theory considers the shear strength of the soil and assumes a uniform distribution of normal stresses along the back of the wall.
*   **Coulomb's Theory**: Coulomb's theory is an extension of Atterberg's theory, taking into account the effect of friction between the soil and the retaining wall.
*   **Rankine's Theory**: Rankine's theory is based on the assumption that the soil behind the wall is in a state of hydrostatic pressure. It provides formulas for calculating the active and passive earth pressures.

### Active and Passive Earth Pressures

The active earth pressure (AEP) occurs when the retaining wall is subjected to external loads, causing the soil to move away from the wall. The passive earth pressure (PEP) occurs when the retaining wall is subjected to external loads in the opposite direction, causing the soil to move towards the wall.

**Key Formulas/Theorems**
-------------------------

*   **Atterberg's Formula**:

    $$
    \sigma_{av} = K \sigma_h
    $$

    where $\sigma_{av}$ is the average normal stress along the back of the wall, $K$ is the coefficient of earth pressure at rest (CPR), and $\sigma_h$ is the horizontal stress.

*   **Rankine's Formula**:

    $$
    q_A = K \gamma h
    $$

    where $q_A$ is the active earth pressure per unit height of the wall, $K$ is Rankine's coefficient of earth pressure (active), $\gamma$ is the unit weight of soil, and $h$ is the height of the retaining wall above the ground surface.

### Problem Solving Patterns
---------------------------

1.  **Identify the type of problem**: Determine whether it involves active or passive earth pressures.
2.  **Determine the coefficient of earth pressure**: Choose the correct formula for calculating the coefficient of earth pressure (CPR) or Rankine's coefficient (active or passive).
3.  **Apply the chosen formula**: Use the selected formula to calculate the active or passive earth pressure per unit height of the wall.
4.  **Consider the effect of surcharge**: If a surcharge is present, apply the corresponding correction factor.

**Examples with Solutions**
-------------------------

### Example 1: Active Earth Pressure

A vertical smooth rigid retaining wall has a height of $h = 10 \text{ m}$ and supports a dry cohesionless backfill with a friction angle $\phi = 30^\circ$. The unit weight of soil is $\gamma = 18 \text{ kN/m}^3$.

1.  **Determine the coefficient of earth pressure (active)**:

    $$
    K_A = \frac{1 - \sin \phi}{1 + \sin \phi}
    $$

    Substituting $\phi = 30^\circ$, we get:

    $$
    K_A = \frac{1 - \sin 30^\circ}{1 + \sin 30^\circ} = \frac{0.5}{1.5} = 0.3333
    $$

2.  **Apply Rankine's formula to calculate the active earth pressure**:

    $$
    q_A = K_A \gamma h
    $$

    Substituting the values of $K_A$, $\gamma$, and $h$, we get:

    $$
    q_A = (0.3333) (18)(10) = 60 \text{ kN/m}^2
    $$

### Example 2: Passive Earth Pressure

A vertical smooth rigid retaining wall has a height of $h = 15 \text{ m}$ and supports a dry cohesionless backfill with a friction angle $\phi = 30^\circ$. The unit weight of soil is $\gamma = 20 \text{ kN/m}^3$.

1.  **Determine the coefficient of earth pressure (passive)**:

    $$
    K_P = \frac{1 + \sin \phi}{1 - \sin \phi}
    $$

    Substituting $\phi = 30^\circ$, we get:

    $$
    K_P = \frac{1 + \sin 30^\circ}{1 - \sin 30^\circ} = \frac{1.5}{0.5} = 3
    $$

2.  **Apply Rankine's formula to calculate the passive earth pressure**:

    $$
    q_P = K_P \gamma h
    $$

    Substituting the values of $K_P$, $\gamma$, and $h$, we get:

    $$
    q_P = (3)(20)(15) = 900 \text{ kN/m}^2
    $$

**Common Pitfalls**
-------------------

*   **Incorrectly applying earth pressure theories**: Ensure that the chosen theory is suitable for the problem at hand.
*   **Failing to consider the effect of surcharge**: Always account for any external loads on the retaining wall.
*   **Miscalculating the coefficient of earth pressure**: Verify the correct formula and value for the coefficient.

**Quick Summary**
-----------------

*   Earth pressure theories: Atterberg, Coulomb, Rankine
*   Active and passive earth pressures: definitions and formulas
*   Problem-solving patterns: identify type of problem, determine coefficient, apply chosen formula
*   Examples with solutions: active and passive earth pressure calculations

This comprehensive theory note covers the essential concepts, formulas, and insights required to tackle questions related to retaining walls and earth pressure. By mastering these topics, you'll be well-prepared for the GATE CS exam and future geotechnical engineering challenges.