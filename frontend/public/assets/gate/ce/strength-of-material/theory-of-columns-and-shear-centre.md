**Theory of Columns and Shear Centre**
=====================================

### Introduction
The theory of columns deals with the study of columns subjected to axial compressive loads, which may cause them to buckle or fail. The shear centre is an important concept in beam theory, related to the neutral axis of a beam.

### Core Concepts

#### 1. **Buckling and Euler's Critical Load**

When a column is subjected to an axial compressive load, it may buckle if the load exceeds a critical value known as Euler's critical load (Pcr). The critical load depends on the slenderness ratio (l/r) of the column.

![Euler's Buckling Curve](https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Eulers_buckling_curve.svg/800px-Eulers_buckling_curve.svg.png)

The equation for Euler's critical load is:

$$P_{cr} = \frac{\pi^2 E I}{(k l)^2}$$

where $E$ is the modulus of elasticity, $I$ is the moment of inertia, and $k$ is a factor depending on the end conditions.

#### 2. **Slenderness Ratio**

The slenderness ratio (l/r) is defined as the ratio of the length to the radius of gyration of the column.

#### 3. **Thermal Expansion**

When a material is heated, it expands. The coefficient of thermal expansion ($\alpha$) gives the change in length per unit length per degree Celsius.

### Key Formulas/Theorems

*   Euler's critical load: $$P_{cr} = \frac{\pi^2 E I}{(k l)^2}$$
*   Slenderness ratio: $l/r$
*   Thermal expansion: $\Delta L = \alpha L_0 \Delta T$

### Problem Solving Patterns

1.  **Given values**: Identify the given values and determine what needs to be calculated.
2.  **Determine slenderness ratio**: Calculate the slenderness ratio (l/r) using the given length and radius of gyration.
3.  **Calculate critical load**: Use Euler's formula to calculate the critical load ($P_{cr}$).
4.  **Consider thermal expansion**: If applicable, calculate the change in temperature required for buckling due to thermal expansion.

### Examples with Solutions

#### Example 1: Column Buckling

A steel column of length $l = 5$ m and radius of gyration $r = 0.2$ m is subjected to an axial compressive load. The modulus of elasticity of the material is $E = 200 \times 10^9$ Pa, and the moment of inertia is $I = 100$ cm$^4$. Determine the critical load for buckling.

```python
import math

# Given values
l = 5  # length in m
r = 0.2  # radius of gyration in m
E = 200e9  # modulus of elasticity in Pa
I = 100  # moment of inertia in cm^4

# Calculate slenderness ratio
slenderness_ratio = l / r

# Calculate critical load using Euler's formula
k = 1.0  # factor depending on end conditions (for simplicity)
critical_load = math.pi**2 * E * I / ((k * l)**2)

print(f"Critical Load: {critical_load/1000:.2f} kN")
```

#### Example 2: Thermal Expansion Buckling

A steel bar of length $L_0 = 10$ m is heated by $\Delta T = 250^\circ C$. The coefficient of thermal expansion for the material is $\alpha = 6.12 \times 10^{-5}$ per degree Celsius. Determine the change in length due to thermal expansion.

```python
# Given values
L_0 = 10  # initial length in m
delta_T = 250  # temperature change in C
alpha = 6.12e-5  # coefficient of thermal expansion

# Calculate change in length using thermal expansion formula
change_in_length = alpha * L_0 * delta_T

print(f"Change in Length: {change_in_length:.2f} m")
```

### Common Pitfalls

*   **Incorrect units**: Ensure that all calculations are performed with the correct units.
*   **Neglecting end conditions**: The critical load depends on the end conditions of the column. Be sure to account for this when calculating the critical load.

### Quick Summary
• Buckling occurs when the axial compressive load exceeds Euler's critical load ($P_{cr}$).
• Slenderness ratio (l/r) affects the critical load.
• Thermal expansion can cause buckling if not accounted for.
• Critical load and thermal expansion formulas must be applied correctly.