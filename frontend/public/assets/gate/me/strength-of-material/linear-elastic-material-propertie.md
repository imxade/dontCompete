**Linear Elastic Material Properties**
======================================

**Introduction**
---------------

In this note, we will cover the properties of linear elastic materials, specifically focusing on the concepts and formulas required to solve problems related to uniaxial tension. Linear elastic materials are a crucial aspect of Strength of Materials and have been tested in previous GATE exams.

**Core Concepts**
-----------------

Linear elastic materials exhibit two primary characteristics:

1. **Proportionality**: The stress (force per unit area) is directly proportional to the strain (deformation per unit length).
2. **Linearity**: The material returns to its original shape and size when the applied load is removed.

These properties are governed by Hooke's Law, which states that the stress ($\sigma$) in a linear elastic material is equal to the product of Young's modulus ($E$) and the strain ($\epsilon$):

$$\sigma = E \cdot \epsilon$$

**Key Formulas/Theorems**
------------------------

* **Young's Modulus (E)**: The ratio of stress to strain within the proportional limit.
	+ $E = \frac{\sigma}{\epsilon}$
* **Strain Energy**: The energy stored in a material due to deformation.
	+ $U = \frac{1}{2} \cdot E \cdot A \cdot \Delta L^2$

where:
- $A$ is the cross-sectional area
- $\Delta L$ is the change in length

**Problem Solving Patterns**
---------------------------

When solving problems related to linear elastic materials, consider the following patterns:

* **Calculate stress and strain**: Use Hooke's Law and the given material properties.
* **Determine the change in energy**: Apply the formula for strain energy.

**Examples with Solutions**
---------------------------

### Example 1: Calculating Stress and Strain

A bar with a length of 5 m and cross-sectional area of $10^{-2}$ m$^2$ is made of a linear elastic material with Young's modulus $E = 70 \, \text{GPa}$. If the bar experiences a tensile force of 1000 N, calculate the stress and strain.

```latex
\sigma = E \cdot \epsilon
= (70 \times 10^9) \cdot \frac{F}{A}
= (70 \times 10^9) \cdot \frac{1000}{10^{-2}}
= 7 \times 10^{11} \, \text{Pa}
```

### Example 2: Determining Strain Energy

A bar with a length of 5 m and cross-sectional area of $10^{-2}$ m$^2$ is made of a linear elastic material with Young's modulus $E = 70 \, \text{GPa}$. If the bar experiences a tensile force of 1000 N, calculate the strain energy stored in the bar.

```latex
U = \frac{1}{2} \cdot E \cdot A \cdot \Delta L^2
= \frac{1}{2} \cdot (70 \times 10^9) \cdot (10^{-2}) \cdot (5)^2
= 1.75 \times 10^7 \, \text{J}
```

**Common Pitfalls**
------------------

* **Units**: Ensure that all units are consistent when applying formulas.
* **Material properties**: Verify the given material properties and use them correctly in calculations.

**Quick Summary**
---------------

| Concept | Formula |
| --- | --- |
| Young's Modulus (E) | $E = \frac{\sigma}{\epsilon}$ |
| Strain Energy (U) | $U = \frac{1}{2} \cdot E \cdot A \cdot \Delta L^2$ |

Note: This summary is not exhaustive and you should refer to the complete note for detailed explanations.