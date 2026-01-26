**Soil Mechanics Three Phase System and Phase Relationships**
===========================================================

### Introduction
----------------

Soil can be classified as a three-phase system consisting of solid, liquid, and gas phases. The most common type of soil is the partially saturated one, where water fills the pores in between the solid particles. Understanding the behavior of these phases is crucial for geotechnical engineering applications.

### Core Concepts
-----------------

#### Three Phase System

A soil sample can be represented as a three-phase system with the following components:

- Solid phase: Soil particles (sand, silt, clay)
- Liquid phase: Water
- Gas phase: Air in the pore spaces

The properties of each phase are described by their respective variables:

- Solid phase: Specific gravity (G), bulk unit weight ($\gamma$)
- Liquid phase: Unit weight of water ($\omega$), density ($\rho_w$)
- Gas phase: Not considered for most geotechnical applications

#### Phase Relationships

The three phases interact with each other through various mechanisms, such as:

- Matric suction (water meniscus tension): $\psi_m = \sigma'_{vN} - u$
- Capillary pressure ($u_p$): $u_p = 2\gamma_{cw}\cos{\theta}$

### Key Formulas/Theorems
-------------------------

#### Unit Weight of Soil Sample on Full Saturation

$\gamma_{sat} = G(\omega + e_s\gamma) = 2.65(0.7565 + (18.5 \text{ kN/m}^3)(1-0.25))$

$\gamma_{sat} = 19.03 \text{ kN/m}^3$


#### Cohesion (c), Angle of Internal Friction ($\phi$)

```math
\sigma'_{vN} = c + \sigma'_{vo}\tan{\phi}
```

### Problem Solving Patterns
---------------------------

1.  **Calculate Unit Weight on Full Saturation**: Apply the formula for $\gamma_{sat}$ using given values.
2.  **Cohesion and Angle of Internal Friction**: Use the provided values to calculate the total stress ($\sigma'_{vN}$) at failure.

### Examples with Solutions
---------------------------

**Q1 (ce\_2021-M_2)**

Calculate the unit weight of soil sample on full saturation for a partially saturated soil with natural moisture content $w = 0.25$ and bulk unit weight $\gamma = 18.5 \text{ kN/m}^3$. Given: Specific gravity $G = 2.65$, unit weight of water $\omega = 9.81 \text{ kN/m}^3$.

$\gamma_{sat} = G(\omega + e_s\gamma)$

$\gamma_{sat} = 2.65(0.7565 + (18.5 \text{ kN/m}^3)(1-0.25))$

$\gamma_{sat} = 19.03 \text{ kN/m}^3$


**Q2 (ce\_2021-M_20)**

Determine the maximum depth of unsupported excavation in soil with cohesion $c = 15 \text{ kPa}$, angle of internal friction $\phi = 0^\circ$, and unit weight $\gamma = 17.5 \text{ kN/m}^3$.

$\sigma'_{vN} = c + \sigma'_{vo}\tan{\phi}$

Since $\phi = 0^\circ$, the maximum depth is given by:

$h = \frac{c}{\gamma - \rho_w}$

$h = \frac{15 \text{ kPa}}{(17.5 \text{ kN/m}^3)(1-9.81 \text{ N/kg})}$


### Common Pitfalls
------------------

-   Inadequate understanding of phase relationships and their effects on soil behavior.
-   Incorrect application of formulas and theorems, leading to miscalculation of unit weights or stresses.

### Quick Summary
----------------

-   Three-phase system: solid (soil), liquid (water), gas (air)
-   Phase relationships: matric suction, capillary pressure
-   Key formulas:
    -   $\gamma_{sat} = G(\omega + e_s\gamma)$
    -   $\sigma'_{vN} = c + \sigma'_{vo}\tan{\phi}$