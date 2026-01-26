**Plastic Analysis of Beams and Frames**
=====================================

### Introduction
-------------

Plastic analysis of beams and frames is a method used to determine the ultimate load-carrying capacity of structures. It involves assuming that the material behaves in an ideal plastic manner, with no strain hardening or softening beyond the yield point.

### Core Concepts
----------------

*   **Yield Moment Capacity**: The maximum moment at which a beam section begins to yield.
*   **Plastic Moment Capacity**: The maximum moment at which a beam section can resist without any further increase in load.
*   **Shape Factor (SF)**: A factor used to determine the ratio of plastic moment capacity to yield moment capacity.

### Key Formulas/Theorems
-------------------------

*   **Yield Moment Capacity**: $M_y = \frac{\sigma_y}{f_y} S_x$
    Where:
    *   $\sigma_y$ is the yield stress,
    *   $f_y$ is the yield strength of the material, and
    *   $S_x$ is the section modulus in the x-direction.
*   **Plastic Moment Capacity**: $M_p = \frac{\sigma_y}{\phi f_c} S_x$
    Where:
    *   $\phi$ is the resistance factor,
    *   $f_c$ is the compressive strength of the material, and
    *   $S_x$ is the section modulus in the x-direction.
*   **Shape Factor (SF)**: $SF = \frac{M_p}{M_y}$

### Problem Solving Patterns
---------------------------

*   Identify the type of loading and determine if it's a simply supported or cantilever beam.
*   Calculate the yield moment capacity using the given section properties.
*   Determine the plastic moment capacity using the shape factor.

### Examples with Solutions
-------------------------

**Example 1**

A simply supported beam with a rectangular cross-section has a length of $L = 10m$, and a width of $b = 0.5m$. The material has a yield strength of $\sigma_y = 250MPa$ and a compressive strength of $f_c = 300MPa$. Determine the plastic moment capacity.

**Solution**

First, we need to calculate the section modulus in the x-direction:

$$S_x = \frac{b}{6} (h^2 + w^2)$$

Assuming $w = b$, then:

$$S_x = \frac{b}{6} (h^2 + b^2)$$

Now, we can calculate the plastic moment capacity:

$$M_p = \frac{\sigma_y}{\phi f_c} S_x$$

Substituting the values:

$$M_p = \frac{250}{0.9 \cdot 300} \cdot \frac{b}{6} (h^2 + b^2)$$

**Example 2**

A beam has a shape factor of $SF = 1.2$. If the yield moment capacity is $M_y = 500N.m$, determine the plastic moment capacity.

**Solution**

Using the formula for the shape factor:

$$SF = \frac{M_p}{M_y}$$

We can rearrange to solve for $M_p$:

$$M_p = SF \cdot M_y$$

Substituting the values:

$$M_p = 1.2 \cdot 500N.m$$

### Common Pitfalls
------------------

*   Forgetting to include the resistance factor in calculations.
*   Misinterpreting the shape factor and its relationship with plastic moment capacity.

### Quick Summary
---------------

*   Yield moment capacity: $M_y = \frac{\sigma_y}{f_y} S_x$
*   Plastic moment capacity: $M_p = \frac{\sigma_y}{\phi f_c} S_x$
*   Shape factor (SF): $SF = \frac{M_p}{M_y}$