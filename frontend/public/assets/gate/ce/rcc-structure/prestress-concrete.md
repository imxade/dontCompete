**Prestress Concrete**
=====================

### Introduction

Prestress concrete (PC) is a type of reinforced concrete that has been subjected to compressive stresses prior to the application of external loads. This is achieved by tensioning the prestressing tendons embedded in the concrete, which induces compressive forces on the surrounding concrete. Prestressed concrete structures are known for their high strength-to-weight ratio, durability, and resistance to cracking.

### Core Concepts

#### Principles of Prestress Concrete

The fundamental principle behind prestress concrete is the application of a compressive force to the concrete through the tensioning of tendons or cables made of materials like steel. This compressive force counteracts the tensile stresses induced by external loads, thereby increasing the resistance of the structure to cracking and deformation.

#### Types of Prestress Concrete

There are several types of prestress concrete, including:

* **Pre-tensioned PC**: In this type, the tendons are tensioned before casting the concrete.
* **Post-tensioned PC**: In this type, the tendons are tensioned after the concrete has set.

### Key Formulas/Theorems

The following formulas and theorems are essential for understanding prestress concrete:

$$F = A \times f_{pu}$$
$$f_{pe} = \frac{F}{A_e}$$
$$M_{cr} = \frac{\sigma_{cu}}{2} \cdot b \cdot d^2$$

where:
- $F$ is the force in the tendon,
- $A$ is the area of the tendon,
- $f_{pu}$ is the ultimate strength of the tendon material,
- $f_{pe}$ is the effective prestressing force per unit area,
- $\sigma_{cu}$ is the compressive strength of the concrete at 28 days,
- $b$ is the width of the section, and
- $d$ is the effective depth of the section.

### Problem Solving Patterns

When solving problems involving prestress concrete, consider the following:

* Determine whether the structure is pre-tensioned or post-tensioned.
* Identify the type of loads acting on the structure (e.g., point loads, uniformly distributed loads).
* Calculate the additional cracking moment that can be carried by the prestressed beam compared to an identical non-prestressed beam.

### Examples with Solutions

**Example 1: Additional Cracking Moment**

Given:

* Effective prestressing force = 1000 kN
* Beam dimensions (B): 300 mm x 500 mm
* Concrete grade: M30

Calculate the additional cracking moment that can be carried by a pre-tensioned beam compared to an identical non-prestressed beam.

Solution:
Using the formula for effective prestressing force, we get:

$$f_{pe} = \frac{1000}{300 \times 500} = 6.67 MPa$$

The additional cracking moment can be calculated as:

$$M_{cr} = \frac{\sigma_{cu}}{2} \cdot b \cdot d^2 - \frac{f_{pe}}{2} \cdot A_e \cdot d^2$$

where $A_e$ is the effective area of the beam.

Substituting values, we get:

$$M_{cr} = \frac{30}{2} \times 300 \times 500^2 - \frac{6.67}{2} \times 300 \times 400 \times 500^2$$

Simplifying, we get:

$$M_{cr} = 299.99 kNm$$

Therefore, the additional cracking moment that can be carried by the prestressed beam is approximately **299 kNm**.

### Common Pitfalls

* Failing to account for the effective area of the beam when calculating the additional cracking moment.
* Not considering the compressive strength of the concrete at 28 days in calculations involving prestress forces.
* Incorrectly determining whether a structure is pre-tensioned or post-tensioned.

### Quick Summary

* Prestress concrete is a type of reinforced concrete that has been subjected to compressive stresses prior to external loads.
* The fundamental principle behind prestress concrete is the application of a compressive force to the concrete through tensioning tendons.
* Key formulas and theorems include $F = A \times f_{pu}$, $f_{pe} = \frac{F}{A_e}$, and $M_{cr} = \frac{\sigma_{cu}}{2} \cdot b \cdot d^2$.
* Consider whether a structure is pre-tensioned or post-tensioned when solving problems involving prestress concrete.