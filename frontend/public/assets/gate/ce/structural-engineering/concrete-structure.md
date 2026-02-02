**Concrete Structures**
=======================

### Introduction
-----------------

Prestressed concrete structures are a type of reinforced concrete where tendons or cables are tensioned to counteract tensile stresses and improve structural integrity. This topic covers the basics of prestressed concrete beams, including calculations for cable force loss due to friction.

### Core Concepts
----------------

#### Prestress Forces
The prestressing force ($P$) in a cable is given by:

$$P = A \sigma_{cu}$$

where $A$ is the area of the cable and $\sigma_{cu}$ is the ultimate tensile strength of the cable material.

#### Friction Loss
Friction loss occurs due to the resistance offered by the surrounding concrete to the movement of the cable. The coefficient of friction ($\mu_f$) for a parabolic cable can be taken as 0.35 (given in the question).

The friction force per unit length is given by:

$$F_f = P \cdot \mu_f \cdot e^{i}$$

where $e^i$ is the eccentricity of the tendon at point $i$. The total friction force ($F_{f,t}$) can be calculated as:

$$F_{f,t} = \int F_f dl$$

#### Wave Effect
The wave effect refers to the additional load on the cable due to its own weight and the weight of the surrounding concrete. The coefficient of wave effect is given as 0.0015 per meter.

### Key Formulas/Theorems
-------------------------

* Prestress force: $P = A \sigma_{cu}$
* Friction force per unit length: $F_f = P \cdot \mu_f \cdot e^{i}$
* Total friction force: $F_{f,t} = \int F_f dl$

### Problem Solving Patterns
---------------------------

1.  **Calculate Prestress Force**: Use the formula $P = A \sigma_{cu}$ to calculate the prestress force.
2.  **Calculate Friction Loss**: Use the formula $F_f = P \cdot \mu_f \cdot e^{i}$ to calculate the friction force per unit length and then integrate over the entire cable to find the total friction force.
3.  **Account for Wave Effect**: Multiply the tension in the cable by the coefficient of wave effect (0.0015 per meter) to account for the additional load due to its own weight.

### Examples with Solutions
---------------------------

**Example 1:**

A concrete beam with a span of 15 m, width of 150 mm, and depth of 350 mm is prestressed with a parabolic cable. The coefficient of friction is 0.35, and the coefficient of wave effect is 0.0015 per meter.

If the cable is tensioned from one end only, calculate the percentage loss in the cable force due to friction.

**Solution:**

1.  Calculate prestress force:

$$P = A \sigma_{cu}$$

Assuming $\sigma_{cu}$ = 1500 MPa and $A$ = 100 mm² (area of the cable), we get $P$ = 150,000 N.

2.  Calculate friction loss:

Using the formula for friction force per unit length:

$$F_f = P \cdot \mu_f \cdot e^{i}$$

Assuming $e^i$ = 50 mm (eccentricity at point $i$), we get:

$$F_f = 150,000 \cdot 0.35 \cdot 50 = 26,250 N/m$$

Integrating over the entire cable:

$$F_{f,t} = \int F_f dl = 15m \cdot 26,250 = 393,750 N$$

3.  Account for wave effect:

$$Wave\,Effect = P \cdot Coefficient\,of\,wave\,effect$$

$$= 150,000 \cdot 0.0015 = 225 N$$

Now, calculate the percentage loss in cable force due to friction:

$$Percentage\,Loss = \frac{F_{f,t}}{P} \cdot 100 = \frac{393,750}{150,000} \cdot 100 = 4.49\%$$

### Common Pitfalls
------------------

*   **Incorrect calculation of prestress force**: Make sure to use the correct formula and values for $\sigma_{cu}$ and $A$.
*   **Neglecting wave effect**: Always account for the additional load due to the cable's own weight.

### Quick Summary
---------------

*   Prestress force: $P = A \sigma_{cu}$
*   Friction loss: $F_f = P \cdot \mu_f \cdot e^{i}$, $F_{f,t} = \int F_f dl$
*   Wave effect: Multiply tension by coefficient of wave effect (0.0015 per meter)
*   Calculate prestress force and friction loss using given formulas
*   Account for wave effect when calculating percentage loss

Note: This theory note is based on the provided question ID: ce\_2020-N\_38. The concepts and calculations may need to be adapted or expanded upon for other questions or scenarios.