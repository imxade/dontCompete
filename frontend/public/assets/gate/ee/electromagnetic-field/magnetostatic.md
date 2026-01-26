**Magnetostatic Theory Note**
==========================

**Introduction**
---------------

The magnetostatic field is a fundamental concept in electromagnetism, describing the behavior of magnetic fields and their interaction with electric charges. In this note, we'll cover the key principles, formulas, and problem-solving strategies to help you tackle questions on this topic.

**Core Concepts**
----------------

### 1. Magnetic Field

A magnetic field $\mathbf{B}$ is a vector field that describes the magnetic influence on moving charges. It's defined as:

$$\mathbf{B} = \mu_0 (\mathbf{H} + \mathbf{M})$$

where $\mu_0$ is the magnetic constant, $\mathbf{H}$ is the magnetic field strength, and $\mathbf{M}$ is the magnetization.

### 2. Lorentz Force Law

The Lorentz force law describes the force exerted on a charge $q$ by electric and magnetic fields:

$$\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$$

where $\mathbf{E}$ is the electric field, $\mathbf{v}$ is the velocity of the charge, and $\times$ denotes the cross product.

### 3. Electromagnetic Induction

Electromagnetic induction occurs when a magnetic field changes in time, inducing an electric field:

$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

**Key Formulas/Theorems**
-------------------------

### 1. Ampere's Law

Ampere's law relates the magnetic field to the current distribution:

$$\nabla \times \mathbf{B} = \mu_0 \mathbf{J}$$

where $\mathbf{J}$ is the current density.

### 2. Gauss's Law for Magnetism

Gauss's law for magnetism states that the magnetic field has no sources or sinks:

$$\nabla \cdot \mathbf{B} = 0$$

**Problem Solving Patterns**
---------------------------

When solving problems on magnetostatics, keep in mind:

1. **Identify the given information**: Carefully read and understand the problem statement.
2. **Determine the relevant equations**: Choose the correct formulas and laws to apply to the problem.
3. **Apply symmetry arguments**: Use geometric symmetries to simplify calculations.

**Examples with Solutions**
---------------------------

### 1. A positive charge $q$ is released from rest at the origin in a region where $\mathbf{E} = E\mathbf{\hat{x}}$ and $\mathbf{B} = B\mathbf{\hat{z}}$. Determine the trajectory of the charge.

Solution:

Since $\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$, we have:

$$\mathbf{F} = q(E\mathbf{\hat{x}})$$

The force is constant and parallel to the $x$-axis, so the charge will move in the $x$-direction. Since there's no magnetic field component perpendicular to $\mathbf{v}$, there's no acceleration in the $y$ or $z$ direction.

### 2. A current-carrying wire is placed along the $z$-axis. If a point charge $q$ is released at $(x,y,z)$ with initial velocity $\mathbf{v} = v\mathbf{\hat{x}}$, determine the trajectory of the charge.

Solution:

The magnetic field due to the current-carrying wire is:

$$\mathbf{B} = \frac{\mu_0 I}{2\pi r}\mathbf{\hat{\phi}}$$

where $r$ is the radial distance from the wire and $\mathbf{\hat{\phi}}$ is the unit vector in the azimuthal direction.

Applying Ampere's law, we get:

$$\nabla \times \mathbf{B} = \mu_0 I\delta(\mathbf{r})$$

where $\delta(\mathbf{r})$ is the Dirac delta function.

The Lorentz force law gives us:

$$\mathbf{F} = q(v\mathbf{\hat{x}}) \times (\frac{\mu_0 I}{2\pi r}\mathbf{\hat{\phi}})$$

Simplifying, we find that the force is perpendicular to $\mathbf{v}$ and has magnitude:

$$F = q\frac{\mu_0 I v}{2\pi r}$$

This force will accelerate the charge in a circular trajectory.

**Common Pitfalls**
------------------

* Failing to apply symmetry arguments
* Incorrectly identifying relevant equations or laws
* Not considering the direction of magnetic fields and currents

**Quick Summary**
-----------------

* Magnetic field $\mathbf{B}$ is defined as $\mu_0 (\mathbf{H} + \mathbf{M})$
* Lorentz force law describes the force on a charge due to electric and magnetic fields
* Electromagnetic induction occurs when a magnetic field changes in time
* Ampere's law relates magnetic field to current distribution
* Gauss's law for magnetism states that magnetic fields have no sources or sinks

This comprehensive theory note covers all key concepts, formulas, and problem-solving strategies required to tackle questions on magnetostatics. Practice problems and examples will help you reinforce your understanding and improve your exam performance.