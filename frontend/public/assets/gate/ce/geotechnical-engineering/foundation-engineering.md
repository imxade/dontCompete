**Theory Note: Geotechnical Engineering - Foundation Engineering**
===========================================================

**Introduction**
---------------

Geotechnical engineering, a subdiscipline of civil engineering, deals with the behavior of earth materials. Foundation engineering is concerned with designing and constructing foundations that transfer loads from structures to the ground safely. This theory note focuses on key concepts related to pile foundation design.

**Core Concepts**
----------------

### Pile Group Efficiency

Pile groups are often used in deep foundation construction when individual piles cannot support the load. The efficiency of a pile group, denoted by η, is influenced by various factors including:

*   **Group efficiency (η):** A measure of how well the piles work together.
*   **Spacing between piles:** Center-to-center spacing between piles influences the effectiveness of the pile group.

### Pile Group Capacity

The capacity of a pile group is determined by considering both individual pile capacities and interaction effects. The design value of the pile group capacity (Q_g) can be estimated using the following formula:

$$
\begin{aligned}
Q_g &= \sum_{i=1}^{n_p} Q_i \eta \\
&= n_p E P_d N_c N_q A V_s \\
&= 16 \cdot 1000 \cdot 1.2 \cdot 10 \\
&= 19200
\end{aligned}
$$

where:

*   $Q_g$: Design value of pile group capacity (kN)
*   $n_p$: Number of piles in the group
*   $E$: Modulus of elasticity of soil (in Pa)
*   $P_d$: Average pressure on the pile tip (in kPa)
*   $N_c$ and $N_q$: Bearing capacity factors for axial loads
*   $A$ and $V_s$: Shape factors

### Evapotranspiration

Evapotranspiration is the total amount of water evaporated from the Earth's surface, including plants, into the atmosphere. It is a key factor in designing foundations that account for moisture migration.

The actual evapotranspiration (ETa) can be estimated using:

$$
ET_a = ET_o \times K_c \times S_c \\
= 6 \times 1.2 \times 0.8 \\
= 5.76 mm/day
$$

where:

*   $ET_a$: Actual evapotranspiration (mm/day)
*   $ET_o$: Potential evapotranspiration (PE) or reference ET (in mm/day)
*   $K_c$ and $S_c$: Crop coefficient and soil coefficient, respectively

### Sucker Rod Pump

A sucker rod pump is a type of positive displacement pump used in oil wells. The inside diameter (ID) of the sampling tube can be estimated using:

$$
\begin{aligned}
D_i &= D_o - 2c \\
&= 50 - 1.0 \times 10^{-3} \cdot 49.5 \\
&= 48.995 mm
\end{aligned}
$$

where $D_i$ is the inside diameter (ID) of the sampling tube in mm.

**Key Formulas/Theorems**
-------------------------

### Pile Group Capacity Formula

The design value of the pile group capacity (Q_g) can be estimated using:

$$
\begin{aligned}
Q_g &= \sum_{i=1}^{n_p} Q_i \eta \\
&= n_p E P_d N_c N_q A V_s
\end{aligned}
$$

### Actual Evapotranspiration Formula

The actual evapotranspiration (ETa) can be estimated using:

$$
ET_a = ET_o \times K_c \times S_c
$$

### Sampling Tube Diameter Formula

The inside diameter (ID) of the sampling tube can be estimated using:

$$
D_i = D_o - 2c
$$

**Problem Solving Patterns**
---------------------------

*   When estimating pile group capacity, ensure that you consider individual pile capacities and interaction effects.
*   When calculating actual evapotranspiration, use the given values for potential evapotranspiration (PE) or reference ET, crop coefficient, and soil coefficient.
*   When determining the inside diameter of a sampling tube, subtract twice the clearance ratio from the outside diameter.

**Examples with Solutions**
---------------------------

### Example 1: Pile Group Capacity

Suppose we have a group of 16 piles in a square grid with center-to-center spacing (s) between piles equal to 3m. The diameter and length of embedment are 1m and 20m, respectively. The design capacity of each pile is 1000 kN in the vertical direction.

Using the formula for pile group capacity:

$$
\begin{aligned}
Q_g &= \sum_{i=1}^{n_p} Q_i \eta \\
&= n_p E P_d N_c N_q A V_s \\
&= 16 \cdot 1000 \cdot 1.2 \cdot 10 \\
&= 19200
\end{aligned}
$$

### Example 2: Actual Evapotranspiration

Given:

*   Potential evapotranspiration (PE) or reference ET = 6 mm/day
*   Crop coefficient (K_c) = 1.2
*   Soil coefficient (S_c) = 0.8

Using the formula for actual evapotranspiration:

$$
ET_a = ET_o \times K_c \times S_c \\
= 6 \times 1.2 \times 0.8 \\
= 5.76 mm/day
$$

### Example 3: Sampling Tube Diameter

Given:

*   Outside diameter (D_o) = 50 mm
*   Clearance ratio = 1.0%

Using the formula for inside diameter of sampling tube:

$$
\begin{aligned}
D_i &= D_o - 2c \\
&= 50 - 1.0 \times 10^{-3} \cdot 49.5 \\
&= 48.995 mm
\end{aligned}
$$

**Common Pitfalls**
------------------

*   When estimating pile group capacity, ensure that you consider individual pile capacities and interaction effects.
*   When calculating actual evapotranspiration, use the given values for potential evapotranspiration (PE) or reference ET, crop coefficient, and soil coefficient.
*   When determining the inside diameter of a sampling tube, subtract twice the clearance ratio from the outside diameter.

**Quick Summary**
----------------

### Pile Group Efficiency

*   η = \frac{1}{(1 + tan \theta)^2}  where θ is the spacing angle between piles

### Actual Evapotranspiration

*   ET_a = ET_o × K_c × S_c
*   ET_a = 5.76 mm/day