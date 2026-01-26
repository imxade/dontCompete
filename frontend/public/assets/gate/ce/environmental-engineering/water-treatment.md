**Water Treatment Theory Note**
=============================

### Introduction
-----------------

Water treatment is a crucial aspect of environmental engineering, involving various processes to remove contaminants and pollutants from water sources. This note will cover the theoretical concepts related to water treatment, focusing on multimedia filters, which are used for removing particulate matter from water.

### Core Concepts
----------------

#### Multimedia Filters
A multimedia filter consists of multiple layers of different particles, each with unique properties. The goal is to design a filter where each layer settles in a specific order, depending on the size and density of the particles.

#### Slow Discrete Settling (Stoke's Law)
The settling velocity of particles under gravity can be calculated using Stoke's law:

$$v = \frac{d^2g(\rho_p - \rho_f)}{18\mu}$$

where:
- $v$ is the settling velocity
- $d$ is the diameter of the particle
- $g$ is the acceleration due to gravity
- $\rho_p$ and $\rho_f$ are the densities of the particle and fluid, respectively
- $\mu$ is the dynamic viscosity of the fluid

#### Particle Properties
The properties of particles in a multimedia filter, such as size, density, and shape, affect their settling behavior.

### Key Formulas/Theorems
---------------------------

**Stoke's Law**: $v = \frac{d^2g(\rho_p - \rho_f)}{18\mu}$

### Problem Solving Patterns
-----------------------------

When solving problems related to multimedia filters, consider the following steps:

1.  Identify the particles and their properties (size, density).
2.  Determine the settling velocity of each particle using Stoke's law.
3.  Compare the settling velocities to determine the order in which the particles will settle.

### Examples with Solutions
---------------------------

**Example:**

A multimedia filter consists of anthracite particles with a diameter of $0.5$ mm and density of $1.50$ g/cm$^3$, silica sand with a diameter of $0.2$ mm and density of $2.60$ g/cm$^3$, and ilmenite sand with a diameter of $0.1$ mm and density of $4.20$ g/cm$^3$. Assuming the fluid is water (density $\approx 1.00$ g/cm$^3$) and viscosity $\approx 1.00$ mPa·s, determine the settling order.

**Solution:**

Calculate the settling velocity for each particle using Stoke's law:

$$v_{anthracite} = \frac{(0.5)^2(9.81)(1.50 - 1.00)}{18(1.00 \times 10^{-3})} \approx 0.026\,m/s$$

$$v_{silica} = \frac{(0.2)^2(9.81)(2.60 - 1.00)}{18(1.00 \times 10^{-3})} \approx 0.041\,m/s$$

$$v_{ilmenite} = \frac{(0.1)^2(9.81)(4.20 - 1.00)}{18(1.00 \times 10^{-3})} \approx 0.083\,m/s$$

The settling order is: ilmenite sand at the bottom, silica sand in the middle, and anthracite particles at the top.

### Common Pitfalls
-------------------

*   Students often forget to consider the properties of the fluid (density and viscosity) when applying Stoke's law.
*   Incorrect particle size or density values can lead to incorrect settling velocities and order.
*   Neglecting the shape of particles (assuming they are spherical) can introduce errors in calculations.

### Quick Summary
-------------------

| Concept | Description |
| --- | --- |
| Multimedia filters | Particles settle in a specific order depending on their size and density. |
| Stoke's Law | Settling velocity of particles under gravity, given by $v = \frac{d^2g(\rho_p - \rho_f)}{18\mu}$. |
| Particle properties | Size, density, and shape affect settling behavior. |

This comprehensive note covers the theoretical concepts required to solve water treatment-related problems in the GATE CS exam. By mastering these concepts, you will be well-prepared to tackle similar questions and excel in your exam performance.