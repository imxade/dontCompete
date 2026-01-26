# Retaining Wall and Earth Pressure
=====================================================

## Introduction
---------------

A retaining wall is a structure designed to resist the forces exerted by soil or rock, preventing it from sliding or overturning. Understanding earth pressure is crucial for designing safe and efficient retaining walls. This theory note covers key concepts, formulas, and problem-solving strategies related to retaining walls and earth pressure.

## Core Concepts
----------------

### Types of Earth Pressure

There are two primary types of earth pressure:

1.  **Active Earth Pressure**: The pressure exerted on a wall by the soil when it is in motion or has already moved.
2.  **Passive Earth Pressure**: The pressure exerted on a wall by the soil when it is being pushed or pulled.

### Rankine's Theory

Rankine's theory provides formulas for calculating active and passive earth pressures. It assumes that the soil behind the wall behaves as an isotropic elastic material.

*   $K_a = \frac{1 - \sin^2\phi}{1 + \sin^2\phi}$
*   $K_p = \frac{1 + \sin\phi}{1 - \sin\phi}$

where:

*   $K_a$ is the active earth pressure coefficient,
*   $K_p$ is the passive earth pressure coefficient, and
*   $\phi$ is the angle of internal friction.

## Key Formulas/Theorems
------------------------

### Earth Pressure Coefficients

The earth pressure coefficients for Rankine's theory are given by:

*   Active: $K_a = \frac{1 - \sin^2\phi}{1 + \sin^2\phi}$
*   Passive: $K_p = \frac{1 + \sin\phi}{1 - \sin\phi}$

### Wall Friction Angle

The wall friction angle is the angle at which the wall and soil interface resists movement. It can be calculated using:

*   $\alpha_w = \tan^{-1}\left(\frac{\tan\phi}{\mu_w}\right)$

where:

*   $\alpha_w$ is the wall friction angle,
*   $\phi$ is the angle of internal friction, and
*   $\mu_w$ is the wall-soil interface coefficient.

## Problem Solving Patterns
-------------------------

### Analyzing Failure Planes

To analyze failure planes for active and passive earth pressure conditions, follow these steps:

1.  Determine the inclination of the major principal plane.
2.  Calculate the angle between the major principal plane and the normal to the wall surface using:
    *   $\theta_a = \frac{\phi}{2}$
    *   $\theta_p = \frac{90^{\circ} - \phi}{2}$
3.  The inclinations of failure planes with respect to the major principal plane are:
    *   Active: $0^\circ$ and $60^\circ$ for dry cohesionless backfill.
    *   Passive: $30^\circ$ and $60^\circ$ for dry cohesionless backfill.

### Analyzing Wall Friction

When a rough retaining wall moves toward the backfill, the wall friction force/resistance mobilizes in an upward direction along the wall. This is because the normal stress on the wall increases as it moves toward the soil, causing the frictional resistance to increase.

## Examples with Solutions
-------------------------

### Example 1: Calculating Active Earth Pressure Coefficient

Given $\phi = 30^\circ$, calculate $K_a$ using Rankine's theory:

*   $K_a = \frac{1 - \sin^2\phi}{1 + \sin^2\phi}$
*   $K_a = \frac{1 - \sin^2(30^\circ)}{1 + \sin^2(30^\circ)}$
*   $K_a = \frac{0.75}{1.25}$
*   $K_a = 0.6$

### Example 2: Analyzing Wall Friction

A rough retaining wall with $\phi = 20^\circ$ and $\mu_w = 0.5$ is subjected to a normal stress of $10 kPa$. Calculate the wall friction angle $\alpha_w$:

*   $\alpha_w = \tan^{-1}\left(\frac{\tan\phi}{\mu_w}\right)$
*   $\alpha_w = \tan^{-1}\left(\frac{\tan(20^\circ)}{0.5}\right)$
*   $\alpha_w = 26.6^\circ$

## Common Pitfalls
------------------

### Incorrectly Applying Formulas

Make sure to use the correct formulas for calculating earth pressure coefficients and wall friction angle.

### Failing to Consider Soil Properties

Be aware of the soil properties, such as cohesionless or cohesive backfill, when analyzing retaining walls.

### Ignoring Boundary Conditions

Consider the boundary conditions, such as free drainage or impermeable surfaces, when designing retaining walls.

## Quick Summary
-----------------

*   Key concepts:
    *   Active and passive earth pressure
    *   Rankine's theory for calculating earth pressure coefficients
    *   Wall friction angle calculation
*   Formulas:
    *   $K_a = \frac{1 - \sin^2\phi}{1 + \sin^2\phi}$
    *   $K_p = \frac{1 + \sin\phi}{1 - \sin\phi}$
    *   $\alpha_w = \tan^{-1}\left(\frac{\tan\phi}{\mu_w}\right)$
*   Problem-solving strategies:
    *   Analyze failure planes for active and passive earth pressure conditions
    *   Consider wall friction when designing retaining walls