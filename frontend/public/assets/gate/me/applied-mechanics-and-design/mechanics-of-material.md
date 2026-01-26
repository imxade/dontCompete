**Mechanics of Materials**
==========================

**Introduction**
---------------

The Mechanics of Materials is a crucial subject that deals with the behavior and properties of solid materials under various types of loads, such as tension, compression, torsion, bending, and shear. This note aims to provide a comprehensive understanding of the fundamental principles, concepts, and formulas required to solve problems in this area.

**Core Concepts**
----------------

### Stress and Strain

* **Stress**: The internal force per unit area on an object.
	+ Tensile stress: $σ = F/A$
	+ Compressive stress: $σ = -F/A$
	+ Shear stress: $τ = F/A$
* **Strain**: The measure of deformation caused by a force or load.
	+ Linear strain: $\epsilon = \Delta L/L$
	+ Angular strain (shear): $\gamma = \tan(\theta)$

### Deformation and Displacement

* **Elastic Deformation**: A material returns to its original shape after the removal of the load.
* **Plastic Deformation**: A material does not return to its original shape after the removal of the load.
* **Displacement**: The movement or change in position of an object.

### Tensile and Compressive Stress

* **Tensile Strength**: The maximum stress a material can withstand without failing under tensile loads.
	+ $σ = F/A$
* **Compressive Strength**: The maximum stress a material can withstand without failing under compressive loads.
	+ $σ = -F/A$

### Shear Stress and Strain

* **Shear Stress**: The internal force per unit area that causes a material to deform by sliding along a plane parallel to the direction of the force.
	+ $τ = F/A$
* **Shear Strain**: The measure of deformation caused by shear stress.
	+ $\gamma = \tan(\theta)$

### Bending Stress and Strain

* **Bending Moment**: A moment that causes a material to deform by bending.
	+ $M = Fd$
* **Bending Stress**: The internal force per unit area on an object under bending loads.
	+ $\sigma = M/I$
* **Bending Strain**: The measure of deformation caused by bending stress.
	+ $\epsilon = \Delta L/L$

### Torsion and Shear Stress

* **Torsional Moment**: A moment that causes a material to deform by twisting.
	+ $T = Fd$
* **Torsional Stress**: The internal force per unit area on an object under torsional loads.
	+ $\tau = T/J$
* **Torsional Strain**: The measure of deformation caused by torsional stress.
	+ $\gamma = \tan(\theta)$

**Key Formulas/Theorems**
-------------------------

### Beam Bending

* **Maximal Stress Formula**:
\[ σ_{max} = \frac{M}{I} y = \frac{6F}{\pi d^3} y \]
* **Stress Distribution**:
\[ \sigma_y = -\frac{Fy}{I} \]

### Torsion

* **Torsional Stress Formula**:
\[ τ = \frac{T}{J} r = \frac{32T}{πd^4} r \]
* **Shear Strain Formula**:
\[ γ = \tan(θ) = \frac{TL}{GJ} \]

### Rivets and Fasteners

* **Shear Stress Formula for Rivet Material**:
\[ τ_{max} = \frac{P}{2A_r} = \frac{F}{A_r} \]
* **Hole Diameter Formula for Riveted Joint**:
\[ d_h = 2a + e \]

### Cylindrical Pressure Vessel

* **Pressure-Volume Relation**:
\[ PV = nRT \]
* **Stress-Strain Relation (Lamé's Equation)**:
\[ \frac{dR}{R} = -\frac{1}{E} dP + \frac{ν}{E} dθ \]

### Problem Solving Patterns
-----------------------------

### Cylindrical Vessel with Liquid

* Calculate the pressure exerted by the liquid on the vessel walls.
* Use **Lamé's Equation** to find the circumferential and axial stresses.

### Riveted Joint

* Determine the maximum shear stress in the rivet material.
* Apply the **Tresca Yield Criterion** to check for yielding.

### Torsion of a Solid Shaft

* Calculate the torque required to twist the shaft.
* Use **St. Venant's Principle** to find the distribution of shear stresses along the shaft axis.

### Beam Bending

* Find the maximum bending moment on the beam.
* Apply **Bishop's Formula** to determine the maximum stress in the beam.

### Torsion and Buckling of a Column

* Calculate the torque required to twist the column.
* Use **Euler's Column Theory** to find the critical buckling load.

**Examples with Solutions**
---------------------------

### Example 1: Cylindrical Vessel with Liquid

A cylindrical vessel has an inner radius $r$ and wall thickness $t$. It contains a liquid of constant density $\rho$ up to height $h$ from the base. Neglect atmospheric pressure, the weight of the vessel, and bending stresses in the vessel walls.

(a) Determine the pressure exerted by the liquid on the vessel walls.

Solution:

The pressure is given by:
\[ P = \frac{W}{A} = \rho gh \]

### Example 2: Riveted Joint

A bracket is attached to a vertical column using two identical rivets $U$ and $V$. The permissible shear stress of the rivet material is $\tau_{max}$.

Determine the minimum cross-sectional area of each rivet to avoid failure under a load $P$ applied at an eccentricity $e$.

Solution:

Apply the **Tresca Yield Criterion**:
\[ \frac{P}{2A_r} = \tau_{max} \]
Solve for the area:
\[ A_r = \frac{P}{2\tau_{max}} \]

### Example 3: Torsion of a Solid Shaft

A solid shaft of diameter $d$ is subjected to a torque $T$. Determine the shear stress distribution along the shaft axis.

Solution:

Apply **St. Venant's Principle**:
\[ τ = \frac{T}{J} r = \frac{32T}{\pi d^4} r \]

### Example 4: Beam Bending

A beam of length $L$ is subjected to a bending moment $M$. Determine the maximum stress in the beam.

Solution:

Apply **Bishop's Formula**:
\[ σ_{max} = \frac{6MF}{\pi d^3} y \]

**Common Pitfalls**
-------------------

* Neglecting atmospheric pressure or the weight of the vessel in problems involving cylindrical vessels.
* Assuming the material is isotropic when applying **Lamé's Equation**.
* Using incorrect formulas for calculating stresses and strains.
* Failing to check for yielding using the **Tresca Yield Criterion**.

**Quick Summary**
-----------------

| Topic | Key Concepts | Formulas/Theorems |
| --- | --- | --- |
| Stress and Strain | Tensile, compressive, shear stress; linear strain | $σ = F/A$, $\epsilon = \Delta L/L$ |
| Deformation and Displacement | Elastic deformation; plastic deformation |  |
| Torsion and Shear Stress | Torsional moment; torsional stress | $τ = T/J r$, $γ = \tan(θ)$ |
| Beam Bending | Maximal stress formula; stress distribution | $σ_{max} = \frac{M}{I} y$ |
| Rivets and Fasteners | Shear stress in rivet material; hole diameter | $τ_{max} = \frac{P}{2A_r}$, $d_h = 2a + e$ |
| Cylindrical Pressure Vessel | Lamé's Equation; pressure-volume relation | $\frac{dR}{R} = -\frac{1}{E} dP + \frac{\nu}{E} dθ$, $PV = nRT$ |

Note: This is a comprehensive theory note covering all the concepts and formulas required to solve problems in Mechanics of Materials. It's essential to practice solving problems using this material to reinforce your understanding and prepare for the exam.