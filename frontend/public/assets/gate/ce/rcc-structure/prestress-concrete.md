**Prestress Concrete**
=====================

**Introduction**
---------------

Prestressed concrete (PC) is a type of reinforced concrete where high-strength tendons are subjected to compressive forces before the concrete hardens. This process reduces tensile stresses in the concrete, increasing its durability and load-carrying capacity.

**Core Concepts**
-----------------

### Tendon Forces

The effective prestressing force (EPF) applied to a tendon is given by:

$$ F_{ep} = f_p \times A_t $$

where $f_p$ is the prestress force per unit area of the tendon and $A_t$ is the cross-sectional area of the tendon.

### Cracking Moment

The cracking moment ($M_c$) for a beam with prestressing force is given by:

$$ M_c = (F_{ep} \times d') - (f_c' \times b \times d') $$

where $d'$ is the distance from the centroidal axis to the neutral axis, $f_c'$ is the compressive strength of the concrete, and $b$ is the breadth of the beam.

### Equivalent Tendon Forces

For a simply supported beam with uniform load ($w$), the equivalent tendon force ($F_{eq}$) can be calculated using:

$$ F_{eq} = \frac{w \times L^2}{8} $$

where $L$ is the length of the beam.

**Key Formulas/Theorems**
-------------------------

* Effective prestressing force: $F_{ep} = f_p \times A_t$
* Cracking moment for a prestressed beam: $M_c = (F_{ep} \times d') - (f_c' \times b \times d')$

**Problem Solving Patterns**
----------------------------

When solving problems involving prestress concrete, follow these steps:

1. Identify the given parameters and the objective.
2. Calculate the effective prestressing force ($F_{ep}$).
3. Determine the cracking moment for both prestressed and non-prestressed beams.
4. Compare the cracking moments to find the additional cracking moment that can be carried by the prestressed beam.

**Examples with Solutions**
---------------------------

### Example 1: Inverted T-Shaped Concrete Beam

Given:

* Effective prestressing force ($F_{ep}$) = 1000 kN
* Centroidal axis at $X - X$
* Compressive strength of concrete ($f_c'$) = 25 MPa
* Breadth of beam ($b$) = 300 mm
* Depth of beam ($d'$) = 500 mm

Calculate the additional cracking moment that can be carried by the prestressed beam.

Solution:

1. Calculate $F_{ep} \times d' = 1000 \times 10^3 \times 0.5 = 500 \times 10^6$ Nmm
2. Calculate $f_c' \times b \times d' = 25 \times 300 \times 0.5 = 3750 \times 10^3$ Nmm
3. Calculate cracking moment for prestressed beam: $M_c = (500 \times 10^6) - (3750 \times 10^3) = 495250 \times 10^3$ Nmm
4. Cracking moment for non-prestressed beam: $M_c = \frac{w \times L^2}{8}$
5. Additional cracking moment that can be carried by prestressed beam: $\Delta M_c = (495250 - 196000) \times 10^3$ Nmm

### Answer:

Additional cracking moment = **299,000** Nmm (approximately)

**Common Pitfalls**
-------------------

* Failing to account for the centroidal axis and neutral axis in calculations.
* Not considering the effect of prestress on the compressive strength of the concrete.

**Quick Summary**
-----------------

* Effective prestressing force: $F_{ep} = f_p \times A_t$
* Cracking moment for a prestressed beam: $M_c = (F_{ep} \times d') - (f_c' \times b \times d')$

[Back to GATE CS exam prep](back_to_gate_cs_exam_prep)