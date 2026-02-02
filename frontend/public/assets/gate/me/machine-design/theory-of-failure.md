**Theory of Failure**
======================

**Introduction**
---------------

The Theory of Failure is a fundamental concept in Machine Design, which deals with predicting the likelihood of failure in mechanical components under various loading conditions. This note will cover the key concepts, formulas, and problem-solving strategies related to the theory of failure.

**Core Concepts**
-----------------

### 1. Stress States

A stress state at a point in a body is defined by three principal stresses ($\sigma_1$, $\sigma_2$, $\sigma_3$). The Von-Mises stress is a measure of the equivalent stress, which combines these principal stresses into a single value.

### 2. Distortional Strain Energy

The distortional strain energy per unit volume is given by:

$$U = \frac{1}{6E} \left[ (\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2 \right]$$

where $E$ is the modulus of elasticity.

**Key Formulas/Theorems**
-------------------------

### 1. Von-Mises Stress

The Von-Mises stress is proportional to the square root of the distortional strain energy:

$$\sigma_{VM} = \sqrt{\frac{2}{3}U}$$

### 2. Failure Criteria

Several failure criteria are used in Machine Design, including:

* Maximum shear stress criterion
* Maximum principal stress criterion
* Von-Mises criterion (most commonly used)

**Problem Solving Patterns**
---------------------------

1. **Identify the loading conditions**: Determine the type of loading (tension, compression, bending, torsion) and the orientation of the loads.
2. **Determine the principal stresses**: Calculate the principal stresses ($\sigma_1$, $\sigma_2$, $\sigma_3$) from the loading conditions.
3. **Apply failure criteria**: Choose an appropriate failure criterion (e.g., Von-Mises) and apply it to the principal stresses.

**Examples with Solutions**
---------------------------

### Example 1: Von-Mises Stress Calculation

A bar is subjected to a tensile force of 100 N, resulting in a stress of 200 MPa. Calculate the distortional strain energy per unit volume:

$$U = \frac{1}{6E} \left[ (\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2 \right]$$

Assuming $E = 200 GPa$ and $\sigma_1 = 200 MPa$, we get:

$$U = \frac{1}{6(200 GPa)} \left[ (200 MPa - 0)^2 + (0 - 0)^2 + (0 - 200 MPa)^2 \right]$$

Simplifying, we get $U = 8.33 \times 10^{-3} J/m^3$.

### Example 2: Failure Criterion Application

A beam is subjected to a bending moment of 100 Nm and a torsional moment of 50 Nm. Calculate the Von-Mises stress:

$$\sigma_{VM} = \sqrt{\frac{2}{3}U}$$

Assuming $E = 200 GPa$ and using the formula for distortional strain energy, we get:

$$\sigma_{VM} = \sqrt{\frac{2}{3} \left( \frac{1}{6E} \right) \left[ (\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2 \right]}$$

Substituting values, we get $\sigma_{VM} = 245.9 MPa$.

**Common Pitfalls**
-------------------

* Failing to consider the effects of stress concentrations
* Ignoring the impact of material anisotropy on failure criteria
* Incorrectly applying failure criteria to complex loading conditions

**Quick Summary**
------------------

* Von-Mises stress is proportional to the square root of distortional strain energy.
* Failure criteria include maximum shear stress, maximum principal stress, and Von-Mises criteria.
* Problem-solving involves identifying loading conditions, determining principal stresses, and applying failure criteria.

This note covers the essential concepts and formulas for the Theory of Failure in Machine Design. By mastering these topics, students will be well-prepared to tackle problems related to failure prediction and analysis.