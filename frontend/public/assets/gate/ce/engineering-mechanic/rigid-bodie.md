**Rigid Body**
===============

**Introduction**
---------------

A rigid body is a solid object that maintains its shape and size under external forces. It is an essential concept in Engineering Mechanics, particularly in statics and dynamics. In this note, we will delve into the core concepts of rigid bodies, key formulas and theorems, problem-solving patterns, and examples with solutions.

**Core Concepts**
----------------

A rigid body can be described by its position, velocity, and acceleration. The following are essential principles:

### 1. **Position**

The position of a point in a rigid body is defined by its coordinates $(x, y, z)$ in a Cartesian coordinate system.

### 2. **Velocity**

The velocity of a point in a rigid body is the rate of change of its position with respect to time. It can be represented as:

$$\vec{v} = \frac{d\vec{r}}{dt}$$

where $\vec{r}$ is the position vector.

### 3. **Acceleration**

The acceleration of a point in a rigid body is the rate of change of its velocity with respect to time. It can be represented as:

$$\vec{a} = \frac{d\vec{v}}{dt}$$

**Key Formulas/Theorems**
-------------------------

1. **Newton's Second Law**

For an object with mass $m$ and acceleration $\vec{a}$, the force $\vec{F}$ applied is:

$$\vec{F} = m\vec{a}$$

2. **Euler's First Law (Rigid Body Rotation)**

The rotation of a rigid body about its center of mass can be described by Euler's first law:

$$\vec{\alpha} = \dot{\vec{\omega}}$$

where $\vec{\alpha}$ is the angular acceleration and $\vec{\omega}$ is the angular velocity.

**Problem Solving Patterns**
---------------------------

### 1. **FBD (Free Body Diagrams)**

When solving problems involving rigid bodies, it's essential to create a FBD of the object under consideration. This involves drawing the forces acting on the object, including gravity and any other applied forces.

### 2. **Force Vectors**

To solve problems involving rigid bodies, we often need to resolve force vectors into their components. This can be done using trigonometry or vector analysis.

**Examples with Solutions**
---------------------------

### 1. **Example 1: Rigid Body Rotation**

A 3 m long rod is rotating about its center of mass. If the angular velocity is $\omega = 2 \text{ rad/s}$ and the moment of inertia $I$ is $5 \text{ kg m}^2$, find the torque $\tau$ applied to the rod.

```mermaid
graph LR
A[Given] --> B[Torque]
B[Torque] --> C[Solve]
C[Solve] --> D[Answer]
```

Solution:

The moment of inertia $I$ is related to the angular velocity $\omega$ and torque $\tau$ by:

$$\tau = I \alpha = I \frac{d\omega}{dt}$$

Substituting the values given, we get:

$$\tau = 5 \text{ kg m}^2 \times (2 \text{ rad/s}) = 10 \text{ Nm}$$

### 2. **Example 2: Rigid Body Translation**

A 2 kg block is moving with a velocity of $v = 4 \text{ m/s}$ under the influence of gravity. If the acceleration due to gravity is $g = 9.8 \text{ m/s}^2$, find the force $F$ applied to the block.

```mermaid
graph LR
A[Given] --> B[Force]
B[Force] --> C[Solve]
C[Solve] --> D[Answer]
```

Solution:

The force $F$ is related to the mass $m$ and acceleration $a$ by Newton's second law:

$$F = m \times a = 2 \text{ kg} \times (-9.8 \text{ m/s}^2) = -19.6 \text{ N}$$

**Common Pitfalls**
------------------

*   Failing to consider the rotation of an object when solving problems involving rigid bodies.
*   Incorrectly applying Newton's second law to objects with variable mass.
*   Neglecting the effects of gravity on the motion of objects.

**Quick Summary**
-----------------

*   A rigid body is a solid object that maintains its shape and size under external forces.
*   The position, velocity, and acceleration of a point in a rigid body can be described mathematically.
*   Key formulas and theorems include Newton's second law and Euler's first law (rigid body rotation).
*   Problem-solving patterns involve creating FBDs, resolving force vectors, and applying key formulas.

Note: This note is intended to provide a comprehensive introduction to the concept of rigid bodies in Engineering Mechanics. It is essential to practice problems and review additional resources for a deeper understanding of the subject.