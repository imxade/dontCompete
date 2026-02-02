**Strength of Materials**
=======================

### Introduction
-----------------

The study of strength of materials deals with the behavior of solids under various types of loads and stresses, including compressive stress, tensile stress, shear stress, bending moment, torsion, etc. It is an essential topic in civil engineering as it helps engineers design structures that are safe, efficient, and cost-effective.

### Core Concepts
-----------------

#### Stress

Stress is a measure of the internal forces acting on an object or material. It can be defined as the ratio of the force applied to the area over which the force acts.

$$\sigma = \frac{F}{A}$$

where $\sigma$ is stress, $F$ is force, and $A$ is area.

#### Strain

Strain is a measure of deformation or change in shape of an object or material under load. It can be defined as the ratio of the change in length to the original length.

$$\epsilon = \frac{\Delta L}{L_0}$$

where $\epsilon$ is strain, $\Delta L$ is change in length, and $L_0$ is original length.

#### Principal Stress and Strain

When a material is subjected to three-dimensional stresses, it can be represented by a stress tensor. The principal stresses are the maximum and minimum normal stresses on an imaginary plane passing through the point of interest.

$$\begin{bmatrix}
\sigma_{xx} & \tau_{xy} & \tau_{xz} \\
\tau_{yx} & \sigma_{yy} & \tau_{yz} \\
\tau_{zx} & \tau_{zy} & \sigma_{zz} \\
\end{bmatrix}$$

The principal strains are related to the principal stresses by:

$$\epsilon_1 = \frac{\sigma_1}{E} - \nu \frac{\sigma_2 + \sigma_3}{E}$$
$$\epsilon_2 = \frac{\sigma_2}{E} - \nu \frac{\sigma_3 + \sigma_1}{E}$$
$$\epsilon_3 = \frac{\sigma_3}{E} - \nu \frac{\sigma_1 + \sigma_2}{E}$$

where $\epsilon_1$, $\epsilon_2$, and $\epsilon_3$ are principal strains, $\sigma_1$, $\sigma_2$, and $\sigma_3$ are principal stresses, $E$ is modulus of elasticity, and $\nu$ is Poisson's ratio.

### Key Formulas/Theorems
-------------------------

*   Beam deflection: $$\delta = \frac{5wl^4}{384EI}$$
*   Bending stress: $$\sigma_b = \frac{M}{I}y$$
*   Shear stress: $$\tau_s = \frac{3QJ}{It^2}$$

### Problem Solving Patterns
---------------------------

1.  **Determine the type of problem**: Identify whether it is a tension/compression, bending, or shear problem.
2.  **Calculate stresses/strains**: Use relevant formulas to calculate principal stresses and strains.
3.  **Apply failure criteria**: Determine if the material has failed based on the calculated stresses and strains.

### Examples with Solutions
---------------------------

1.  A rectangular beam is subjected to a bending moment of 100 Nm. If the modulus of elasticity is 200 GPa, the cross-sectional area is 0.01 m², and the distance from the neutral axis to the extreme fiber is 0.05 m, determine the maximum bending stress.

    $$\sigma_b = \frac{M}{I}y$$
    $$= \frac{100 Nm}{(200 GPa) (0.01 m^2) (0.05 m)}$$
    $$= 5 MPa$$

2.  A circular shaft is subjected to a torsional moment of 50 Nm. If the polar moment of inertia is 10 × 10⁻⁴ m⁴, and Poisson's ratio is 0.3, determine the maximum shear stress.

    $$\tau_s = \frac{3QJ}{It^2}$$
    $$= \frac{(50 Nm) (10 \times 10^{-4} m^4)}{(0.01 m^2) (0.05 m)^2}$$
    $$= 1.5 MPa$$

### Common Pitfalls
-------------------

*   **Failure to identify the type of problem**: Make sure to determine whether it is a tension/compression, bending, or shear problem.
*   **Incorrect application of formulas**: Double-check units and ensure that the correct formula is used for each problem.

### Quick Summary
------------------

*   Stress: $\sigma = \frac{F}{A}$
*   Strain: $\epsilon = \frac{\Delta L}{L_0}$
*   Principal stress and strain:
    *   $$\begin{bmatrix}
        \sigma_{xx} & \tau_{xy} & \tau_{xz} \\
        \tau_{yx} & \sigma_{yy} & \tau_{yz} \\
        \tau_{zx} & \tau_{zy} & \sigma_{zz} \\
        \end{bmatrix}$$
    *   $$\epsilon_1 = \frac{\sigma_1}{E} - \nu \frac{\sigma_2 + \sigma_3}{E}$$
*   Beam deflection: $\delta = \frac{5wl^4}{384EI}$
*   Bending stress: $\sigma_b = \frac{M}{I}y$
*   Shear stress: $\tau_s = \frac{3QJ}{It^2}$