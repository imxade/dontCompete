**Pile Foundation Theory Note**
=====================================

**Introduction**
---------------

A pile foundation is a type of deep foundation used to transfer loads from superstructures (buildings, bridges, etc.) to a deeper and more stable soil stratum. Piles are long, slender members made of materials like steel or concrete that are embedded in the ground to resist vertical loads.

**Core Concepts**
----------------

### Types of Pile Foundations

1. **End Bearing Piles**: Transfer loads to a hard rock or dense sand layer at the base.
2. **Friction Piles**: Resist loads through shear resistance along their length.

### Soil-Pile Interaction

1. **Adhesion**: The bond between the pile and surrounding soil, influencing uplift capacity.
2. **Friction**: Resistance offered by the soil to sliding of the pile, affecting lateral loads.

**Key Formulas/Theorems**
-------------------------

### Adhesion Factor (Ka)

The adhesion factor is a dimensionless quantity representing the ratio of adhesion to the shear strength of the surrounding soil.

$$ Ka = \frac{adhesion}{shear\ strength} $$

For pure clay, $Ka$ can be calculated as:

$$ Ka = 0.5 \times (cohesion / frictional\_angle) $$

where cohesion is in kPa and the frictional angle is in degrees.

### Uplift Capacity (Qu)

The ultimate uplift capacity of a pile can be estimated using the following formula:

$$ Qu = \pi \times d^2 \times Ka \times cohesion $$

where $d$ is the diameter of the pile in meters.

**Problem Solving Patterns**
---------------------------

1. **Identify type of soil**: Determine the properties and behavior of the surrounding soil (e.g., pure clay, dense sand).
2. **Calculate adhesion factor**: Use the given cohesion value to calculate the adhesion factor.
3. **Estimate uplift capacity**: Apply the formula for uplift capacity using the calculated adhesion factor and given values.

**Examples with Solutions**
---------------------------

### Example 1: Pure Clay

A reinforced concrete pile of 10 m length and 0.7 m diameter is embedded in a saturated pure clay with unit cohesion of 50 kPa. If the adhesion factor is 0.5, calculate the net ultimate uplift pullout capacity (in kN) of the pile.

Solution:

1. Identify type of soil: Pure clay
2. Calculate adhesion factor:
$$ Ka = 0.5 \times (cohesion / frictional\_angle) $$
Assuming a typical frictional angle for pure clay, $\theta = 25^\circ$,
$$ Ka = 0.5 \times (50\ kPa / 25^\circ) = 1 $$

3. Estimate uplift capacity:
$$ Qu = \pi \times d^2 \times Ka \times cohesion $$
$$ Qu = \pi \times (0.7\ m)^2 \times 1 \times 50\ kPa = 147.2\ kN $$

### Example 2: Dense Sand

A steel pile of 12 m length and 1.2 m diameter is embedded in a dense sand layer with cohesion of 20 kPa. If the adhesion factor is 0.7, calculate the net ultimate uplift pullout capacity (in kN) of the pile.

Solution:

1. Identify type of soil: Dense sand
2. Calculate adhesion factor:
$$ Ka = 0.5 \times (cohesion / frictional\_angle) $$
Assuming a typical frictional angle for dense sand, $\theta = 35^\circ$,
$$ Ka = 0.5 \times (20\ kPa / 35^\circ) = 0.29 $$

3. Estimate uplift capacity:
$$ Qu = \pi \times d^2 \times Ka \times cohesion $$
$$ Qu = \pi \times (1.2\ m)^2 \times 0.29 \times 20\ kPa = 67.6\ kN $$

**Common Pitfalls**
------------------

* Failing to identify the type of soil and its properties.
* Incorrectly calculating adhesion factors or uplift capacities.

**Quick Summary**
----------------

* Pile foundations: Transfer loads from superstructures to deeper, stable soil strata.
* Adhesion factor (Ka): A dimensionless quantity representing the bond between pile and surrounding soil.
* Uplift capacity (Qu): Estimated using the formula $ Qu = \pi \times d^2 \times Ka \times cohesion $.

Note: This theory note covers the essential concepts, formulas, and problem-solving patterns required to tackle questions related to pile foundations.