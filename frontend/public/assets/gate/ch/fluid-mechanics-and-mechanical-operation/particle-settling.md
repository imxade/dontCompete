**Particle Settling**
====================

### Introduction
---------------

Particle settling is a fundamental concept in fluid mechanics that describes how particles or objects settle at the bottom of a fluid under gravity. This phenomenon occurs when a particle or object is denser than the surrounding fluid, causing it to experience an upward buoyant force and a downward gravitational force.

### Core Concepts
-----------------

#### 1. Archimedes' Principle

Archimedes' principle states that the buoyant force on an object submerged in a fluid is equal to the weight of the fluid displaced by the object.

$$F_b = \rho V g$$

where:

* $F_b$ is the buoyant force
* $\rho$ is the density of the fluid
* $V$ is the volume of the fluid displaced
* $g$ is the acceleration due to gravity

#### 2. Stokes' Law

Stokes' law relates the drag force on a particle settling through a fluid to its velocity, size, and density.

$$F_d = 6 \pi \mu r v$$

where:

* $F_d$ is the drag force
* $\mu$ is the dynamic viscosity of the fluid
* $r$ is the radius of the particle
* $v$ is the velocity of the particle

#### 3. Reynolds Number

The Reynolds number is a dimensionless quantity that characterizes the nature of fluid flow around an object.

$$Re = \frac{\rho v r}{\mu}$$

where:

* $\rho$ is the density of the fluid
* $v$ is the velocity of the fluid
* $r$ is the radius of the particle
* $\mu$ is the dynamic viscosity of the fluid

### Key Formulas/Theorems
---------------------------

#### 1. Terminal Velocity

The terminal velocity of a particle settling through a fluid is reached when the drag force equals the weight of the particle.

$$v_t = \frac{2}{9} \frac{\rho r^2 g (\rho_p - \rho)}{\mu}$$

where:

* $v_t$ is the terminal velocity
* $\rho$ is the density of the fluid
* $r$ is the radius of the particle
* $g$ is the acceleration due to gravity
* $\rho_p$ is the density of the particle
* $\mu$ is the dynamic viscosity of the fluid

### Problem Solving Patterns
---------------------------

When solving problems involving particle settling, follow these steps:

1.  Identify the type of flow: laminar or turbulent.
2.  Calculate the Reynolds number to determine the nature of flow.
3.  Apply Stokes' law to calculate the drag force on the particle.
4.  Use Archimedes' principle to calculate the buoyant force on the particle.
5.  Equate the drag force and weight of the particle to find the terminal velocity.

### Examples with Solutions
---------------------------

**Example 1**

A spherical particle with a radius of 0.05 m settles through water at a velocity of 0.01 m/s. The density of the particle is 2500 kg/m³, and the density of water is 1000 kg/m³. Calculate the drag force on the particle.

**Solution**

First, calculate the Reynolds number:

$$Re = \frac{\rho v r}{\mu} = \frac{1000 \times 0.01 \times 0.05}{1 \times 10^{-3}} = 5$$

Since $Re < 2$, the flow is laminar.

Next, apply Stokes' law:

$$F_d = 6 \pi \mu r v = 6 \pi \times 1 \times 10^{-3} \times 0.05 \times 0.01 = 9.42 \times 10^{-4} N$$

**Example 2**

A particle with a density of 5000 kg/m³ and radius of 0.02 m settles through oil at a terminal velocity of 0.005 m/s. The viscosity of the oil is 0.01 Pa·s, and the density of the oil is 900 kg/m³. Calculate the drag force on the particle.

**Solution**

First, calculate the Reynolds number:

$$Re = \frac{\rho v r}{\mu} = \frac{900 \times 0.005 \times 0.02}{0.01} = 9$$

Since $Re < 2$, the flow is laminar.

Next, use Archimedes' principle to calculate the buoyant force:

$$F_b = \rho V g = 900 \times \frac{4}{3} \pi (0.02)^3 \times 9.81 = 1.11 N$$

Now, equate the drag force and weight of the particle:

$$F_d = F_w - F_b$$

Substitute values to find $F_d$.

### Common Pitfalls
------------------

*   **Incorrect calculation of Reynolds number**: Ensure you use the correct units for density, velocity, radius, and viscosity.
*   **Misapplication of Stokes' law**: Verify that the flow is laminar by checking the Reynolds number value.
*   **Inconsistent units**: Be careful when converting between different units (e.g., from Pa to N/m²).

### Quick Summary
------------------

Key concepts:

*   Archimedes' principle: buoyant force = weight of fluid displaced
*   Stokes' law: drag force = 6 \pi \mu r v
*   Reynolds number: Re = ρ v r / μ

Key formulas:

*   Terminal velocity: v_t = (2/9) \frac{\rho r^2 g (\rho_p - \rho)}{\mu}

Key steps for problem solving:

1.  Identify the type of flow (laminar or turbulent)
2.  Calculate the Reynolds number
3.  Apply Stokes' law to calculate drag force
4.  Use Archimedes' principle to calculate buoyant force

By following this comprehensive theory note, you'll be well-prepared to tackle problems on particle settling and related concepts in fluid mechanics.