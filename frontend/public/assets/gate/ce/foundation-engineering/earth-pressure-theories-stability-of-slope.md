**Earth Pressure Theories and Stability of Slope**
==============================================

**Introduction**
---------------

Earth pressure theories are essential for analyzing the stability of retaining walls, slopes, and embankments. In this note, we will focus on Rankine's earth pressure theory and its application to a retaining wall with clay backfill.

**Core Concepts**
-----------------

### Stress Distribution

When a retaining wall is subjected to external loads, it experiences stress distribution in three dimensions: horizontal (x), vertical (y), and depth (z). The stresses can be resolved into normal (σ) and shear (τ) components.

### Rankine's Earth Pressure Theory

Rankine's theory assumes that the soil behaves as an elastic material under loading. It considers two types of soil behavior:

1.  **Active earth pressure**: When the wall is subjected to external loads, the soil behind it moves towards the wall, causing a reduction in the normal stress (σ'). The active earth pressure coefficient (Ka) is defined as:
    $$
    K_a = \frac{1 - sin(\phi)}{1 + sin(\phi)}
    $$
    where φ is the angle of internal friction.
2.  **Passive earth pressure**: When a force is applied to the wall, the soil behind it moves away from the wall, causing an increase in the normal stress (σ'). The passive earth pressure coefficient (Kp) is defined as:
    $$
    K_p = \frac{1 + sin(\phi)}{1 - sin(\phi)}
    $$

**Key Formulas/Theorems**
-------------------------

### Active Earth Pressure

The active earth pressure (Pa) can be calculated using the following formula:

$$
P_a = \gamma H^2 \left[ K_a \tan^2(45 + \phi/2) + K_a' \tan(45 + \phi/2) \right]
$$

where γ is the unit weight of soil, H is the height of the wall, and Ka', Ka are coefficients.

### Passive Earth Pressure

The passive earth pressure (Pp) can be calculated using the following formula:

$$
P_p = \gamma H^2 \left[ K_p \tan^2(45 + \phi/2) + K_p' \tan(45 + \phi/2) \right]
$$

**Problem Solving Patterns**
---------------------------

### Case Study 1: Retaining Wall with Clay Backfill (Q1)

*   Identify the type of soil behind the retaining wall (clay).
*   Determine the angle of internal friction (φ) for clay.
*   Calculate the active earth pressure coefficient (Ka) using the formula:
    $$
    K_a = \frac{1 - sin(\phi)}{1 + sin(\phi)}
    $$
*   Ignore passive earth pressure and focus on active earth pressure.
*   Use the following formula to calculate the factor of safety against sliding failure:
    $$
    F_s = \frac{W}{P_a}
    $$
    where W is the weight of the retaining wall.

### Example with Solution

Q1: A retaining wall with a height of 10 m and clay backfill has an interface friction angle of 20° between the base of the retaining wall and the base soil. The unit weight of water (γw) is 9.81 kN/m³, the unit weight of clay (γclay) is 17.2 kN/m³, and the cohesion (c) is 30 kN/m². Assuming that the tension crack is filled with water, use Rankine's earth pressure theory to calculate the factor of safety against sliding failure.

Solution:

1.  Calculate Ka:
    $$
    K_a = \frac{1 - sin(20)}{1 + sin(20)} = 0.8333
    $$
2.  Calculate Pa:
    $$
    P_a = 9.81 H^2 [K_a tan^2(45 + \phi/2) + K_a' tan(45 + \phi/2)] \\
    P_a = 9.81 (10)^2 [0.8333 tan^2(55) + 1 tan(55)]\\
    P_a = 9795 kN/m
    $$
3.  Calculate the weight of the retaining wall:
    $$
    W = \gamma H^2 \\
    W = 5000 (10)^2\\
    W = 50,000 kN
    $$
4.  Calculate the factor of safety against sliding failure:
    $$
    F_s = \frac{W}{P_a} \\
    F_s = \frac{50,000}{9795}\\
    F_s ≈ 5.10
    $$

However, this solution is incorrect as we must take into account the weight acting at a distance of 3.3 m from the toe of the retaining wall and not directly above it.

To calculate the factor of safety against sliding failure correctly, we need to use the correct formula for Pa considering the load distribution:

$$
P_a = \gamma H^2 [K_a \tan^2(45 + \phi/2) + K_a' \tan(45 + \phi/2)] \\
P_a = \gamma (H - x)^2 [K_a \tan^2(45 + \phi/2) + K_a' \tan(45 + \phi/2)]
$$

where x is the distance between the load and the toe of the retaining wall.

**Common Pitfalls**
------------------

*   Incorrectly assuming that passive earth pressure is negligible.
*   Failing to consider the correct load distribution on the retaining wall.
*   Not using the correct formula for calculating Pa.

**Quick Summary**
-----------------

*   Rankine's earth pressure theory assumes elastic behavior of soil under loading.
*   Active and passive earth pressures are defined by Ka and Kp, respectively.
*   The factor of safety against sliding failure can be calculated using Pa and W.

By following these guidelines and carefully analyzing the problem, you should be able to solve questions related to earth pressure theories and stability of slopes with confidence.