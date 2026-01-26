**Working Stress and Limit State Design Concept**
=====================================================

**Introduction**
---------------

The working stress design method is a traditional approach used to design reinforced concrete structures, focusing on the permissible stresses in materials rather than their ultimate capacity. In contrast, the limit state design (LSD) approach considers the maximum load that a structure can withstand without collapsing or failing to meet its functional requirements.

**Core Concepts**
-----------------

### Working Stress Design

In working stress design, the allowable stresses in concrete and steel are assumed to be proportional to the compressive strength of concrete. The permissible stresses are divided into two categories: ultimate and serviceability limits.

*   **Ultimate limit state**: The maximum load that a structure can withstand without collapsing or failing.
*   **Serviceability limit state**: The acceptable level of deformation, crack width, or other performance criteria under normal loads.

### Limit State Design (LSD)

The LSD approach is based on the concept of limit states, which are defined as the conditions beyond which a structure would fail to meet its intended function. There are two main types of limit states:

*   **Ultimate Limit States**: These occur when a structure fails due to excessive loads or deformation, leading to collapse.
*   **Serviceability Limit States**: These relate to the structural performance under normal operating conditions, including factors like durability and user comfort.

**Key Formulas/Theorems**
-------------------------

The working stress design method is based on the following key formulas:

$$\sigma_c = \frac{f_ck}{\gamma_c}$$

$$\sigma_s = \frac{f_yk}{\gamma_s}$$

where $\sigma_c$ and $\sigma_s$ are the allowable compressive and tensile stresses in concrete, $f_{ck}$ is the characteristic compressive strength of concrete, $\gamma_c$ is a factor representing the permissible stress, $f_y$ is the yield strength of steel, and $k$ is a factor for the design strength.

The LSD approach uses the following formula to determine the design resistance:

$$R_d = \frac{f_ckA_c}{\gamma_c} + f_yA_s$$

where $R_d$ is the design resistance, $A_c$ is the area of concrete in compression, and $A_s$ is the area of steel reinforcement.

**Problem Solving Patterns**
---------------------------

When solving problems involving working stress design or LSD, follow these patterns:

1.  Identify the type of limit state (ultimate or serviceability) and the relevant factors to consider.
2.  Determine the allowable stresses in concrete and steel using the appropriate formulas.
3.  Calculate the design resistance and compare it with the applied loads.

**Examples with Solutions**
---------------------------

### Working Stress Design Example

A prismatic cantilever prestressed concrete beam has a span length of 1.5 m, a width of 200 mm, and a depth of 300 mm. The total prestressing force is 50 kN, applied at 50 mm from the top in the cross-section. If a concentrated load of 5 kN is applied, find the resultant stress experienced at point 'Q'.

Solution:

Bending moment = $P \times L = 5 \times 1.5 = 7.5$ kN-m

$$\sigma = \frac{M}{I}z = \frac{7.5 \times 1000}{200 \times 300^2} \times (0.167)$$

$$\sigma = 0.01$$ MPa

### LSD Example

A simply supported beam with a span length of 6 m has a rectangular cross-section with dimensions 200 mm x 300 mm. The beam is subjected to a uniformly distributed load of 2 kN/m. Determine the design resistance and compare it with the applied loads.

Solution:

Design resistance = $R_d = \frac{f_ckA_c}{\gamma_c} + f_yA_s$

Assuming $f_{ck} = 25$ MPa, $\gamma_c = 1.4$, $f_y = 500$ MPa, and $A_c = 200 \times 300$ mm²

$$R_d = \frac{25 \times 1400}{1.4} + 500 \times 10$$

$$R_d = 14,857 kN$$

The applied loads are $2 \times 6 = 12$ kN, which is less than the design resistance.

**Common Pitfalls**
------------------

1.  Failing to consider both ultimate and serviceability limit states.
2.  Misapplying allowable stresses or using incorrect factors.
3.  Not calculating the design resistance correctly.

**Quick Summary**
-----------------

*   Working stress design: Focuses on permissible stresses in materials.
*   Limit state design: Considers maximum loads that a structure can withstand without failing.
*   Key formulas: Allowable compressive and tensile stresses, design resistance.
*   Problem solving patterns: Identify limit states, calculate allowable stresses, determine design resistance.

This comprehensive theory note covers the essential concepts of working stress and limit state design, including core principles, key formulas, problem-solving patterns, examples with solutions, and common pitfalls.