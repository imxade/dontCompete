**Bending Stresses**
=====================

### Introduction
Bending stress is a type of stress that occurs in materials when they are subjected to external loads that cause them to deform by bending. Bending stresses can be either compressive (compressing) or tensile (stretching), depending on the direction of the load.

### Core Concepts
When an object is bent, it experiences a combination of shear and normal stresses. The maximum bending stress occurs at the surface of the material, where the distance from the neutral axis is greatest.

#### Neutral Axis
The neutral axis is an imaginary line that passes through the center of the cross-section of the material. At this point, there is no net bending moment (normal or shear), and the material does not deform.

#### Bending Moment (BM)
The bending moment is a measure of the external load applied to the object that causes it to bend. It can be calculated using the following formula:

$$ BM = \int P d(\sin \theta) $$

where $P$ is the external load and $\theta$ is the angle between the load and the horizontal.

### Key Formulas/Theorems
#### Maximum Bending Stress ($\sigma_b$)
The maximum bending stress occurs at the surface of the material, where the distance from the neutral axis is greatest. It can be calculated using the following formula:

$$ \sigma_b = \frac{M}{I} y $$

where $M$ is the bending moment, $I$ is the second moment of area (also known as the moment of inertia), and $y$ is the distance from the neutral axis to the surface.

#### Bending Stress in Beams
For beams subjected to external loads, the maximum bending stress can be calculated using the following formulas:

* For a simply supported beam with a uniformly distributed load: $$ \sigma_b = \frac{q L^2}{8 I} y $$
* For a cantilever beam with a point load at the free end: $$ \sigma_b = \frac{P L}{I} y $$

where $q$ is the uniform load, $L$ is the length of the beam, and $y$ is the distance from the neutral axis to the surface.

### Problem Solving Patterns
When solving problems involving bending stresses, follow these steps:

1. Draw a free-body diagram (FBD) of the object.
2. Identify the external loads applied to the object.
3. Calculate the bending moment using the formula above.
4. Calculate the maximum bending stress using the formulas above.

### Examples with Solutions
**Example 1:** A simply supported beam with a uniformly distributed load has a length of 2m and a width of 0.24m. The uniform load is 20kN/m. Calculate the maximum bending stress at the surface of the beam.

* FBD:
```mermaid
graph LR
A[Simply Supported Beam] --> B[Uniform Load]
```
* Calculation: $$ \sigma_b = \frac{q L^2}{8 I} y $$
$$ \sigma_b = \frac{(20kN/m) (2m)^2}{8 (0.24m)^3} (0.12m) $$
$$ \sigma_b = 250 MPa $$

**Example 2:** A cantilever beam with a point load at the free end has a length of 1m and a width of 0.12m. The point load is 45kN. Calculate the maximum bending stress at the surface of the beam.

* FBD:
```mermaid
graph LR
A[Cantilever Beam] --> B[Point Load]
```
* Calculation: $$ \sigma_b = \frac{P L}{I} y $$
$$ \sigma_b = \frac{(45kN) (1m)}{(0.12m)^3} (0.06m) $$
$$ \sigma_b = 250 MPa $$

### Common Pitfalls
* Failing to identify the external loads applied to the object.
* Failing to calculate the bending moment correctly.
* Using incorrect formulas or values for the second moment of area.

### Quick Summary
* Bending stress occurs in materials when subjected to external loads that cause them to deform by bending.
* The maximum bending stress occurs at the surface of the material, where the distance from the neutral axis is greatest.
* Bending stresses can be calculated using the formulas above.

**References**

* [1] "Mechanics of Materials" by R. C. Hibbeler
* [2] "Strength of Materials" by S. Timoshenko

Note: The above references are for illustration purposes only and may not reflect actual textbooks or resources used in the GATE exam.