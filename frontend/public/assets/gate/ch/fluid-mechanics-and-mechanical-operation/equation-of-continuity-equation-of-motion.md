**Equation of Continuity and Equation of Motion in Fluid Mechanics**
===========================================================

**Introduction**
---------------

The equation of continuity and the equation of motion are fundamental concepts in fluid mechanics that describe the behavior of fluids under various conditions. These equations are essential in understanding and solving problems related to fluid flow, including pipe flows, pumps, and turbines.

**Core Concepts**
-----------------

### Equation of Continuity

The equation of continuity states that the mass flow rate of a fluid remains constant throughout a pipe or channel, assuming no accumulation or depletion of mass within the system. Mathematically, it is expressed as:

$$\rho_1 A_1 v_1 = \rho_2 A_2 v_2$$

where:

* $\rho$ is the fluid density
* $A$ is the cross-sectional area of the pipe
* $v$ is the velocity of the fluid

### Equation of Motion (Navier-Stokes Equations)

The equation of motion, also known as the Navier-Stokes equations, describes the motion of fluids under various forces. For an incompressible fluid, the equations are:

$$\frac{\partial v}{\partial t} + v \cdot \nabla v = -\frac{1}{\rho} \nabla p + \nu \nabla^2 v$$

where:

* $v$ is the velocity of the fluid
* $p$ is the pressure of the fluid
* $\rho$ is the fluid density
* $\nu$ is the kinematic viscosity of the fluid

**Key Formulas/Theorems**
-------------------------

### Continuity Equation (LaTeX)

$$\rho_1 A_1 v_1 = \rho_2 A_2 v_2$$

### Bernoulli's Equation (LaTeX)

$$P_1 + \frac{1}{2} \rho v_1^2 + \rho g z_1 = P_2 + \frac{1}{2} \rho v_2^2 + \rho g z_2$$

where:

* $P$ is the pressure of the fluid
* $\rho$ is the fluid density
* $v$ is the velocity of the fluid
* $g$ is the acceleration due to gravity
* $z$ is the elevation of the fluid

**Problem Solving Patterns**
---------------------------

### Pattern 1: Applying Continuity Equation

When solving problems involving pipe flows, apply the continuity equation to find the relationship between the velocities and cross-sectional areas at different points in the pipe.

### Pattern 2: Applying Bernoulli's Equation

When solving problems involving fluid flow under various pressures and elevations, apply Bernoulli's equation to relate the pressure, velocity, and elevation of the fluid.

**Examples with Solutions**
---------------------------

### Example 1: Continuity Equation

A pipe has a diameter of 0.1 m at one end and 0.2 m at the other end. If the flow rate is constant and the fluid density is 1000 kg/m³, find the velocity at each end.

```markdown
# Continuity Equation Example

## Given Values

* Diameter (end 1): 0.1 m
* Diameter (end 2): 0.2 m
* Flow rate: constant
* Fluid density: 1000 kg/m³

## Solution

Let $v_1$ be the velocity at end 1 and $v_2$ be the velocity at end 2.

Using continuity equation:

$$\rho A_1 v_1 = \rho A_2 v_2$$

Substituting values:

$$(1000 \text{ kg/m}^3) (\pi (0.05)^2) v_1 = (1000 \text{ kg/m}^3) (\pi (0.1)^2) v_2$$

Simplifying and solving for $v_2$:

$$v_2 = 4 v_1$$

Thus, the velocity at end 2 is four times the velocity at end 1.

### Example 2: Bernoulli's Equation

A pump increases the pressure of a fluid from 100 kPa to 200 kPa. If the flow rate is constant and the elevation remains the same, find the change in kinetic energy per unit mass.

```markdown
# Bernoulli's Equation Example

## Given Values

* Initial pressure: 100 kPa
* Final pressure: 200 kPa
* Flow rate: constant
* Elevation: same at both points

## Solution

Using Bernoulli's equation:

$$P_1 + \frac{1}{2} \rho v_1^2 = P_2 + \frac{1}{2} \rho v_2^2$$

Substituting values and simplifying:

$$(100 \text{ kPa}) + 0 = (200 \text{ kPa}) - \frac{1}{2} \rho (v_2)^2$$

Rearranging to solve for $(v_2)^2$:

$$(v_2)^2 = \frac{(P_2 - P_1)}{\frac{1}{2} \rho}$$

Substituting values and simplifying:

$$(v_2)^2 = 4000 \text{ m}^2/\text{s}^2$$

Thus, the change in kinetic energy per unit mass is $2000 \text{ J/kg}$.

**Common Pitfalls**
-------------------

* Failing to apply the correct equation (continuity or Bernoulli's)
* Ignoring the effects of elevation and pressure
* Not considering the fluid density and viscosity

**Quick Summary**
-----------------

| Concept | Formula |
| --- | --- |
| Continuity Equation | $\rho_1 A_1 v_1 = \rho_2 A_2 v_2$ |
| Bernoulli's Equation | $P_1 + \frac{1}{2} \rho v_1^2 + \rho g z_1 = P_2 + \frac{1}{2} \rho v_2^2 + \rho g z_2$ |

Remember to always apply the correct equation and consider all relevant factors when solving problems in fluid mechanics.