# Fluid Kinematics and Fluid in Relative Equilibrium
## Introduction
Fluid kinematics is a branch of fluid mechanics that deals with the study of motion of fluids without considering the forces causing the motion. It involves the description and analysis of fluid flow, including velocity, acceleration, and other kinematic properties.

## Core Concepts

### Incompressibility and Compressibility

A fluid is said to be incompressible if its density remains constant under a change in pressure or volume. This is often assumed for liquids, as their density changes very little with pressure.

On the other hand, a compressible fluid can undergo significant changes in density under varying pressures.

### Rotational and Irrotational Flows

A rotational flow is one where the fluid particles follow curved paths, indicating that the fluid has both velocity and angular momentum. An example of a rotational flow is when a pipe bends or converges.

An irrotational flow is one where the fluid particles follow straight paths, indicating that the fluid has no net angular momentum. This can occur in flows with low velocities or when the flow is symmetric around its axis.

### Relative Equilibrium

A fluid is said to be in relative equilibrium if it is at rest or moving with a uniform velocity relative to some reference frame. In other words, there are no forces acting on the fluid to change its motion.

## Key Formulas/Theorems

* **Continuity Equation**: $\rho_1 A_1 v_{1x} = \rho_2 A_2 v_{2x}$ (mass conservation)
* **Bernoulli's Principle**: $p + \frac{1}{2} \rho v^2 + \rho gy = \text{constant}$ (energy conservation)

```latex
\frac{\partial u}{\partial t} + u \cdot \nabla u = -\frac{1}{\rho} \nabla p + \nu \nabla^2 u
```

## Problem Solving Patterns

When dealing with fluid kinematics and relative equilibrium, follow these steps:

1.  Determine the type of flow (incompressible or compressible) based on the given information.
2.  Check if the flow is rotational or irrotational by examining the velocity field or the behavior of fluid particles.
3.  Apply relevant conservation laws (e.g., continuity equation, Bernoulli's principle).
4.  Use mathematical formulas and theorems to derive expressions for velocity, pressure, or other quantities.

## Examples with Solutions

### Example 1: Incompressible Flow
A horizontal pipe carries water at a constant flow rate of $Q = 0.05 \, \text{m}^3/\text{s}$ through a contraction from $D_1 = 10 \, \text{cm}$ to $D_2 = 5 \, \text{cm}$. If the velocity upstream is $v_1 = 2 \, \text{m}/\text{s}$ and the density of water is $\rho = 1000 \, \text{kg}/\text{m}^3$, find the velocity downstream.

## Solution
Apply the continuity equation:

$$
\rho Q = A_1 v_{1x} = A_2 v_{2x}
$$

Rearrange to solve for $v_{2x}$:

$$
v_{2x} = \frac{A_1}{A_2} v_{1x} = 4 v_{1x}
$$

Substitute the given values and calculate:

$$
v_{2x} = 4 \cdot 2 \, \text{m}/\text{s} = 8 \, \text{m}/\text{s}
$$

### Example 2: Relative Equilibrium
A tank of water has a height of $h = 10 \, \text{m}$ and a cross-sectional area of $A = 1 \, \text{m}^2$. If the tank is initially at rest, what is the pressure at the bottom of the tank due to its own weight?

## Solution
Apply the hydrostatic force equation:

$$
F_h = \rho g h A
$$

Note that since the tank is in relative equilibrium (no motion), the force due to gravity acting on the fluid must be balanced by an equal and opposite reaction force at the bottom of the tank. The pressure can thus be calculated as:

$$
p = \frac{F_h}{A} = \rho g h
$$

Substitute the given values and calculate:

$$
p = 1000 \, \text{kg}/\text{m}^3 \cdot 9.81 \, \text{m}/\text{s}^2 \cdot 10 \, \text{m} = 981000 \, \text{Pa}
$$

## Common Pitfalls

*   Overlooking the assumption of incompressibility or compressibility.
*   Misinterpreting rotational vs. irrotational flows.
*   Failing to apply relevant conservation laws.

## Quick Summary

### Fluid Kinematics and Relative Equilibrium Key Points

*   Incompressible fluids have constant density, while compressible fluids can change density with pressure.
*   Rotational flows have curved paths, while irrotational flows follow straight paths.
*   Relative equilibrium occurs when a fluid is at rest or moving uniformly relative to some reference frame.
*   Apply continuity equation and Bernoulli's principle for incompressible flows.

This comprehensive note will serve as an excellent resource for students preparing for the GATE CS exam, providing them with a solid understanding of fluid kinematics and relative equilibrium.