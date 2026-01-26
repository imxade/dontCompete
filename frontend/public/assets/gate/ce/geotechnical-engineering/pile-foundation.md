**Pile Foundation Theory Note**
====================================

**Introduction**
---------------

A pile foundation is a type of deep foundation used to transfer loads from superstructure to stratum of soil or rock at greater depth. In this note, we will focus on the analysis of reinforced concrete piles in saturated pure clay.

**Core Concepts**
-----------------

### Adhesion Factor

The adhesion factor, denoted by α, is a dimensionless quantity that represents the ratio of the shear strength of the pile-soil interface to the undrained shear strength of the soil. It is a key parameter in determining the uplift capacity of a pile.

### Uplift Capacity

The uplift capacity of a pile is the maximum force required to lift the pile out of the ground. For a reinforced concrete pile, it can be calculated using the following formula:

$$P_u = A_p \times q_{uh} + A_s \times q_{us}$$

where $P_u$ is the uplift capacity, $A_p$ is the area of the pile, $q_{uh}$ is the ultimate horizontal adhesion stress, and $A_s$ is the area of the reinforcement.

### Ultimate Horizontal Adhesion Stress

The ultimate horizontal adhesion stress, denoted by $q_{uh}$, can be calculated using the following formula:

$$q_{uh} = c \times \alpha$$

where $c$ is the cohesion of the soil and α is the adhesion factor.

### Cohesion

Cohesion is a measure of the strength of the soil due to intermolecular forces between particles. For saturated pure clay, it can be assumed to be equal to the unit weight of water times the void ratio.

**Key Formulas/Theorems**
-------------------------

* Uplift capacity: $P_u = A_p \times q_{uh} + A_s \times q_{us}$
* Ultimate horizontal adhesion stress: $q_{uh} = c \times \alpha$

```latex
\frac{P_u}{A_p} = q_{uh}
```

**Problem Solving Patterns**
---------------------------

1.  **Identify key parameters**: Determine the cohesion, adhesion factor, and reinforcement details of the pile.
2.  **Calculate ultimate horizontal adhesion stress**: Use the formula $q_{uh} = c \times \alpha$ to determine this value.
3.  **Calculate uplift capacity**: Use the formula $P_u = A_p \times q_{uh} + A_s \times q_{us}$ to calculate the uplift capacity.

**Examples with Solutions**
---------------------------

### Example 1

A reinforced concrete pile of length 10 m and diameter 0.7 m is embedded in a saturated pure clay with unit cohesion of 50 kPa. The adhesion factor is given as 0.5. Determine the net ultimate uplift pullout capacity of the pile.

```markdown
| Parameter | Value |
| --- | --- |
| Cohesion (c) | 50 kPa |
| Adhesion Factor (α) | 0.5 |
| Pile Length (L) | 10 m |
| Pile Diameter (D) | 0.7 m |
```

### Step-by-Step Solution

*   Calculate the area of the pile: $A_p = \pi \times D^2 / 4$
*   Calculate the ultimate horizontal adhesion stress: $q_{uh} = c \times \alpha$
*   Calculate the uplift capacity: $P_u = A_p \times q_{uh}$

```latex
\frac{P_u}{A_p} = \frac{\pi \times D^2 / 4 \times c \times \alpha}{\pi \times D^2 / 4}
```

### Solution

$P_u = A_p \times q_{uh} = 0.7^2 \times \pi / 4 \times 50 \times 0.5$

Simplifying the expression gives us $P_u \approx 545 kN$

**Common Pitfalls**
-------------------

*   Failing to calculate the ultimate horizontal adhesion stress correctly
*   Not accounting for the reinforcement details in calculating the uplift capacity
*   Misinterpreting the unit cohesion value

**Quick Summary**
-----------------

*   Pile foundation is a type of deep foundation used to transfer loads from superstructure to stratum of soil or rock at greater depth.
*   The uplift capacity of a pile can be calculated using the formula $P_u = A_p \times q_{uh} + A_s \times q_{us}$.
*   The ultimate horizontal adhesion stress is given by $q_{uh} = c \times \alpha$.

**Additional Insights**
----------------------

*   The adhesion factor, α, plays a crucial role in determining the uplift capacity of a pile.
*   The cohesion value of saturated pure clay can be assumed to be equal to the unit weight of water times the void ratio.