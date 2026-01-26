**Rotation and Torque**
=======================

**Introduction**
---------------

Torque and rotation are fundamental concepts in fluid mechanics, governing the behavior of spinning objects and fluids under various forces. Understanding these principles is crucial for analyzing complex systems and making accurate predictions.

**Core Concepts**
-----------------

### 1. Rotational Kinematics

Rotational kinematics deals with the motion of an object as it rotates around a fixed axis. The key parameters are:

* **Angular velocity (ω)**: the rate of change of angular displacement, measured in radians per second (rad/s).
* **Angular acceleration (α)**: the rate of change of angular velocity.
* **Moment of inertia (I)**: a measure of an object's resistance to changes in its rotational motion.

**Key Formulas**
---------------

* **Moment of inertia**: $I = \frac{1}{2}mr^2$ for a point mass, where m is the mass and r is the radius.
* **Torque (τ)**: the rotational equivalent of force, causing an object to rotate. $τ = Iα$
* **Rotational kinetic energy (KE_rot)**: $KE_{rot} = \frac{1}{2}Iω^2$

### 2. Rotational Dynamics

When a torque is applied to an object, it causes the object to accelerate rotationally. The key parameters are:

* **Torque**: $τ = r × F$, where r is the radius of the axis of rotation and F is the force applied.
* **Rotational inertia (I)**: affects the response of an object to a torque.

**Key Formulas**
---------------

* **Torque (τ)**: $τ = r × F$
* **Angular acceleration (α)**: $α = \frac{τ}{I}$

### 3. Rolling Motion

When a rotating object is in contact with another surface, it can experience rolling motion. The key parameters are:

* **Coefficient of friction (μ)**: affects the force opposing the rotation.
* **Torque**: causes the object to accelerate rotationally.

**Key Formulas**
---------------

* **Rolling resistance torque (τ_roll)**: $τ_{roll} = μrF_n$, where r is the radius, F_n is the normal force.

### 4. Conservation of Angular Momentum

When an external torque is applied to a system, the total angular momentum remains conserved. The key parameters are:

* **Angular momentum (L)**: the product of moment of inertia and angular velocity.
* **Torque**: causes changes in angular momentum.

**Key Formulas**
---------------

* **Conservation of angular momentum**: $∑τ = \frac{dL}{dt} = 0$

### 5. Rotation and Friction

When a rotating object is subject to friction, energy is dissipated as heat. The key parameters are:

* **Coefficient of friction (μ)**: affects the force opposing rotation.
* **Torque**: causes the object to accelerate rotationally.

**Key Formulas**
---------------

* **Frictional torque (τ_f)**: $τ_f = μrF_n$

### 6. Rotational Equilibrium

When an object is rotating under the influence of various forces, it can reach rotational equilibrium. The key parameters are:

* **Torque**: causes changes in rotational motion.
* **Moment of inertia (I)**: affects the response to a torque.

**Key Formulas**
---------------

* **Rotational equilibrium**: $∑τ = 0$

### Problem Solving Patterns
-------------------------

* Analyze the system and identify key parameters such as mass, radius, angular velocity, and coefficients.
* Use conservation of angular momentum and rotational kinematics principles to solve problems.
* Identify forces acting on an object and determine their effects on rotation.

### Examples with Solutions
---------------------------

**Example 1: Rotational Kinetics**

A point mass m is rotating around a fixed axis with initial angular velocity ω_i. The moment of inertia I is given by $I = \frac{1}{2}mr^2$. Calculate the final angular velocity ω_f after a torque τ is applied.

Solution:
```latex
\begin{aligned}
τ &= Iα \\
&= (\frac{1}{2}mr^2)\alpha \\
ω_f &= ω_i + αt
\end{aligned}
```

**Example 2: Rolling Motion**

A cylinder of mass m and radius r is rolling on a surface with coefficient of friction μ. The initial angular velocity is ω_i. Calculate the final angular velocity ω_f after a time t.

Solution:
```latex
\begin{aligned}
τ_{roll} &= μrF_n \\
&= μrmg \\
ω_f &= ω_i + \frac{τ_{roll}}{I}t
\end{aligned}
```

### Common Pitfalls
-------------------

* Failing to account for friction and energy dissipation.
* Incorrectly applying conservation of angular momentum.
* Neglecting rotational kinematics principles.

### Quick Summary
---------------

| Concept | Formula |
| --- | --- |
| Moment of Inertia (I) | $I = \frac{1}{2}mr^2$ |
| Torque (τ) | $τ = r × F$ |
| Rotational Kinetic Energy (KE_rot) | $KE_{rot} = \frac{1}{2}Iω^2$ |
| Angular Acceleration (α) | $α = \frac{τ}{I}$ |
| Rolling Resistance Torque (τ_roll) | $τ_{roll} = μrF_n$ |

This comprehensive study note covers all the theoretical concepts, formulas, and insights required to solve rotation and torque problems in fluid mechanics. By following this guide, students will be well-prepared for the GATE CS exam and other competitive tests.