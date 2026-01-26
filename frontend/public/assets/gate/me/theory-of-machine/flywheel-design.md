# Flywheel Design
=================

## Introduction
---------------

A flywheel is a mechanical device that stores energy kinetically by using its moment of inertia to resist changes in rotational speed. It plays a crucial role in smoothing out fluctuations in power supply and maintaining a stable output.

## Core Concepts
-----------------

### Moment of Inertia
The moment of inertia (I) of an object about an axis is defined as the sum of the products of the elemental areas of the object and the squares of their distances from the axis. For a rotating body, it determines how much energy is required to change its rotational speed.

### Angular Velocity
Angular velocity (ω) is the rate of change of angular displacement with respect to time. It's measured in radians per second.

### Energy Storage
A flywheel stores energy kinetically as the sum of kinetic energies of its rotating mass.

## Key Formulas/Theorems
---------------------------

### Moment of Inertia for a Ring:
$$I = \frac{1}{2}mr^2$$

### Moment of Inertia for a Disk:
$$I = \frac{1}{4}mr^2$$

### Angular Velocity in Radians per Second:
$$\omega = \frac{\text{Angular Displacement}}{\text{Time Interval}}$$

## Problem Solving Patterns
---------------------------

When solving problems related to flywheel design, consider the following steps:

1.  Determine the minimum energy required to be stored by the flywheel.
2.  Calculate the angular velocity and mean speed of the engine.
3.  Use the turning moment equation to determine the torque provided by the engine.

## Examples with Solutions
---------------------------

### Example 1:
A flywheel is attached to an engine that provides a constant resisting torque. The torque provided by the engine is given by $T = \frac{12000}{2500}sin^2\theta + \theta$, where $\theta$ is the angle turned by the crank from inner dead center. If the mean speed of the engine is 200 rpm and it drives a machine that provides a constant resisting torque, find the minimum mass moment of inertia of the flywheel.

### Solution:

Given:
*   $T = \frac{12000}{2500}sin^2\theta + \theta$
*   $\omega = 20.944$ rad/s (from 200 rpm)
*   Resisting torque is constant

We can use the turning moment equation to determine the minimum mass moment of inertia:

$$\text{Work done per cycle} = \int_{0}^{2\pi} T \, d\theta$$

Substituting $T$ from the given expression and integrating over one complete cycle (from 0 to $2\pi$), we get:

$$\text{Work done per cycle} = \frac{12000}{2500}\int_{0}^{2\pi} sin^2\theta \, d\theta + \int_{0}^{2\pi} \theta \, d\theta$$

Evaluating the integrals and simplifying:

$$\text{Work done per cycle} = \frac{12000}{2500}\left[\frac{\theta}{2} - \frac{sin(2\theta)}{4}\right]_0^{2\pi} + \left[\frac{\theta^2}{2}\right]_0^{2\pi}$$

Simplifying further:

$$\text{Work done per cycle} = 12000 + \frac{(2\pi)^2}{2} - 0$$

Now, equating this to the energy stored by the flywheel and solving for $I$:

$$E_{stored} = \frac{1}{2}I\omega^2$$

Substituting values:

$$12000 + \pi^2 = \frac{1}{2}I(20.944)^2$$

Solving for I:

$$I = \frac{(12000 + \pi^2)(60)}{(20.944)^2}$$

Rounding off to the nearest integer and solving for $m$ using $I = \frac{1}{2}mr^2$:

$$m = \frac{2I}{r^2}$$

Substituting values:

$$m = \frac{2\left(\frac{(12000 + \pi^2)(60)}{(20.944)^2}\right)}{\left(\frac{1}{4}\right)^2}$$

Simplifying and solving for m:

$$m = 569.98 \text{ kg-m}^2$$

### Example 2:
A flywheel has a mass moment of inertia of $500$ kg-m$^2$. If the engine provides a torque given by $T = 2000sin\theta + \theta$, what is the maximum speed variation (in percent) for the machine driven by this flywheel?

## Common Pitfalls
------------------

*   Forgetting to consider energy losses and inefficiencies in the system.
*   Not taking into account the effect of friction and air resistance on the flywheel's performance.

## Quick Summary
-----------------

*   Flywheels store energy kinetically by using their moment of inertia to resist changes in rotational speed.
*   The minimum mass moment of inertia required for a flywheel can be calculated using the turning moment equation and energy stored by the flywheel.
*   Energy losses and inefficiencies should be considered when designing a flywheel system.