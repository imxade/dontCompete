**Maxwell's Equations**
=======================

### Introduction
-----------------

Maxwell's equations are a set of four fundamental equations that describe how electric and magnetic fields interact with each other. These equations form the foundation of classical electromagnetism and have been extensively tested and validated in various experiments.

### Core Concepts
-------------------

#### Electric Displacement Density Vector
----------------------------------------

The electric displacement density vector, **D**, is given by:

$$\mathbf{D} = \varepsilon_{0}\mathbf{E} + \mathbf{P}$$

where $\varepsilon_{0}$ is the electric constant (permittivity of free space), $\mathbf{E}$ is the electric field, and $\mathbf{P}$ is the polarization density.

#### Electric Field
-------------------

The electric field, **E**, is a vector field that describes the force experienced by a test charge at a given point in space. It can be expressed as:

$$\mathbf{E} = -\nabla V$$

where $V$ is the electric potential.

#### Magnetic Field
------------------

The magnetic field, $\mathbf{B}$, is a vector field that describes the force experienced by a moving charge or a current-carrying wire. It can be expressed as:

$$\mathbf{B} = \nabla \times \mathbf{A}$$

where $\mathbf{A}$ is the magnetic vector potential.

#### Gauss's Law
-----------------

Gauss's law states that the total electric flux through a closed surface is proportional to the charge enclosed within that surface:

$$\oint_{S} \mathbf{D} \cdot d\mathbf{A} = Q_{enc}$$

where $Q_{enc}$ is the charge enclosed within the surface.

### Key Formulas/Theorems
---------------------------

**Maxwell's Equations**

1. **Gauss's Law for Electric Fields**
	* $\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_{0}}$
2. **Gauss's Law for Magnetic Fields**
	* $\nabla \cdot \mathbf{B} = 0$
3. **Faraday's Law of Induction**
	* $\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$
4. **Ampère-Maxwell Law**
	* $\nabla \times \mathbf{B} = \mu_{0}\mathbf{J} + \mu_{0}\varepsilon_{0}\frac{\partial \mathbf{E}}{\partial t}$

### Problem Solving Patterns
---------------------------

1. **Identify the relevant equation**: Determine which of Maxwell's equations applies to the given problem.
2. **Sketch the situation**: Draw a diagram illustrating the electric and magnetic fields involved.
3. **Apply boundary conditions**: Consider any boundary conditions that may affect the solution.

### Examples with Solutions
---------------------------

**Example 1**

Consider a point charge $q$ located at the origin. Find the electric field $\mathbf{E}$ at a distance $r$ from the charge.

**Solution**

* Identify the relevant equation: Gauss's Law for Electric Fields
* Sketch the situation: A point charge at the origin surrounded by an imaginary sphere of radius $r$
* Apply boundary conditions: The electric field is zero outside the sphere
* Solution:
$$\mathbf{E} = \frac{q}{4\pi\varepsilon_{0}r^{2}}\hat{\mathbf{r}}$$

**Example 2**

Consider a long, straight wire carrying a current $I$. Find the magnetic field $\mathbf{B}$ at a distance $r$ from the wire.

**Solution**

* Identify the relevant equation: Ampère-Maxwell Law
* Sketch the situation: A long, straight wire surrounded by an imaginary cylinder of radius $r$
* Apply boundary conditions: The magnetic field is zero outside the cylinder
* Solution:
$$\mathbf{B} = \frac{\mu_{0}I}{2\pi r}\hat{\mathbf{\phi}}$$

### Common Pitfalls
-------------------

1. **Incorrect application of boundary conditions**: Failing to account for the effects of boundaries on the solution.
2. **Ignoring the time dependence of fields**: Failing to consider how electric and magnetic fields change over time.

### Quick Summary
-----------------

* Maxwell's equations describe how electric and magnetic fields interact with each other.
* Gauss's Law relates the electric flux through a closed surface to the charge enclosed within that surface.
* Faraday's Law of Induction describes how a changing magnetic field induces an electric field.
* Ampère-Maxwell Law relates the magnetic field to the current and the rate of change of the electric field.

Note: The provided source question is used as an example, but the solution process is not explicitly covered in this theory note.