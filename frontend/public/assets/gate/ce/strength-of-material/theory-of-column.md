**Theory of Columns**
=====================

**Introduction**
---------------

The Theory of Columns deals with the study of compressive strength of columns under various types of loading, including axial loads, bending moments, and torsion. It is a crucial aspect of structural analysis in civil engineering, particularly in designing tall buildings, bridges, and other structures that support heavy loads.

**Core Concepts**
-----------------

### Slenderness Ratio

The slenderness ratio (λ) of a column is defined as the ratio of its effective length (L) to its radius of gyration (r):

$$\lambda = \frac{L}{r}$$

A high slenderness ratio indicates that the column is more prone to buckling.

### Euler's Critical Load

Euler's critical load (Pcr) is the minimum axial load required to cause a column to buckle. It can be calculated using the formula:

$$P_{cr} = \frac{\pi^2 E I}{L^2}$$

where:
- $E$ is the modulus of elasticity
- $I$ is the moment of inertia
- $L$ is the effective length

### Thermal Expansion

When a material undergoes thermal expansion, its temperature increases or decreases. The coefficient of thermal expansion (α) represents the change in temperature per unit change in length:

$$\alpha = \frac{\Delta L}{L_0 \Delta T}$$

where:
- $\Delta L$ is the change in length
- $L_0$ is the original length
- $\Delta T$ is the change in temperature

**Key Formulas/Theorems**
------------------------

### Column Buckling Load

The column buckling load (Pb) can be calculated using the formula:

$$P_b = \frac{\pi^2 E I}{\lambda^2}$$

where:
- $E$ is the modulus of elasticity
- $I$ is the moment of inertia
- $\lambda$ is the slenderness ratio

### Thermal Load

The thermal load (Pt) due to temperature change can be calculated using the formula:

$$P_t = \alpha E A \Delta T$$

where:
- $\alpha$ is the coefficient of thermal expansion
- $E$ is the modulus of elasticity
- $A$ is the cross-sectional area
- $\Delta T$ is the change in temperature

**Problem Solving Patterns**
---------------------------

### Step 1: Determine the Effective Length

The effective length (L) of a column can be obtained by dividing the actual length by a factor that depends on the boundary conditions.

### Step 2: Calculate the Slenderness Ratio

Use the formula $\lambda = \frac{L}{r}$ to calculate the slenderness ratio.

### Step 3: Determine the Critical Load

Calculate Euler's critical load (Pcr) using the formula $P_{cr} = \frac{\pi^2 E I}{L^2}$.

### Step 4: Consider Thermal Expansion

If thermal expansion is a concern, calculate the thermal load (Pt) using the formula $P_t = \alpha E A \Delta T$.

**Examples with Solutions**
---------------------------

### Example 1:

A steel column has an effective length of 5 m and a radius of gyration of 0.2 m. If the modulus of elasticity is 200 GPa, determine the critical load using Euler's formula.

```latex
P_{cr} = \frac{\pi^2 E I}{L^2}
= \frac{\pi^2 \cdot 200 \cdot 10^9 \cdot (0.1)^4}{(5)^2}
≈ 3.18 kN
```

### Example 2:

A steel column has a coefficient of thermal expansion of $6 \times 10^{-12}$ K$^{-1}$. If the temperature increases by 100°C, calculate the thermal load per unit area.

```latex
P_t = \alpha E A \Delta T
= (6 \cdot 10^{-12}) \cdot 200 \cdot 10^9 \cdot 0.01 \cdot 100
≈ 1.2 kPa
```

**Common Pitfalls**
------------------

*   **Neglecting boundary conditions**: Always consider the actual boundary conditions when calculating effective length.
*   **Incorrect values for material properties**: Verify that you are using the correct values for modulus of elasticity, coefficient of thermal expansion, etc.
*   **Misapplication of formulas**: Make sure to apply the correct formula and units.

**Quick Summary**
-----------------

*   Effective length (L) = actual length / boundary condition factor
*   Slenderness ratio ($\lambda$) = L/r
*   Euler's critical load (Pcr) = $\frac{\pi^2 E I}{L^2}$
*   Thermal load (Pt) = $\alpha E A \Delta T$

This comprehensive study note covers the theoretical concepts of column buckling, thermal expansion, and the key formulas required to solve problems in this area. The provided examples demonstrate how to apply these principles to calculate critical loads and thermal loads.