**Engineering Fluid Mechanics**
==============================

### Introduction
Fluid mechanics and thermal science are crucial for understanding various engineering applications. This note focuses on key concepts, formulas, and problem-solving strategies relevant to GATE CS exam questions.

### Core Concepts
#### Rotational Motion of a Rigid Body
A rigid body can rotate about its center of mass under the influence of external forces. The angular velocity ($\omega$) is related to the linear velocity (v) by:
\[ v = \omega r \]
where $r$ is the radius of rotation.

#### Frictional Forces
When a rigid body rotates and comes into contact with a surface, frictional forces act perpendicular to the surface. The coefficient of friction ($\mu$) determines the magnitude of these forces.

### Key Formulas/Theorems

#### Angular Momentum
The angular momentum (L) of a rotating object is given by:
\[ L = I \omega \]
where $I$ is the moment of inertia about the axis of rotation.

#### Moment of Inertia
For a cylindrical disc, the moment of inertia ($I$) about its central axis is:
\[ I = \frac{1}{2} m r^2 \]

### Problem Solving Patterns

#### Example 1: Q41 (me_2022-M_41)
A cylindrical disc spins at $\omega = 5$ rad/s and has a radius of $r = 0.15$ m. It is placed on a flat surface with a coefficient of friction $\mu$. Find the horizontal velocity of the center of the disc when it starts rolling without slipping.

Solution:
1. Calculate the moment of inertia: $I = \frac{1}{2} \cdot 1 \cdot (0.15)^2 = 0.01125$ kg m^2
2. Apply the condition for rolling without slipping: $\mu F_N = I \alpha$
3. Use the equation for frictional force ($F_f = \mu N$) and substitute values.

```mermaid
graph LR
A[Given Values] --> B[Calculate Moment of Inertia]
B --> C[Apply Rolling Without Slipping Condition]
C --> D[Solve for Frictional Force]
D --> E[Find Horizontal Velocity]
```

### Examples with Solutions

#### Example 2: Q15 (me_2022-M_15)
In the two-dimensional momentum equation, identify the term that represents the buoyancy force per unit mass.

Solution:
1. Analyze the given equation and identify relevant terms.
2. Recognize that the buoyancy force is proportional to the volumetric thermal expansion coefficient ($\beta$) and the temperature difference between the fluid and its surroundings.

```mermaid
graph LR
A[Given Equation] --> B[Identify Relevant Terms]
B --> C[Recognize Buoyancy Force Term]
```

### Common Pitfalls

* Failing to account for all relevant forces in a problem.
* Misapplying formulas or equations from different physical contexts.
* Neglecting the effects of frictional forces.

### Quick Summary
| Concept | Description |
| --- | --- |
| Rotational Motion | Rigid body rotation about its center of mass. |
| Frictional Forces | Forces acting perpendicular to a surface due to contact with a rigid body. |
| Angular Momentum | Moment of inertia ($I$) times angular velocity ($\omega$). |
| Moment of Inertia | $I = \frac{1}{2} m r^2$ for a cylindrical disc. |

This comprehensive theory note covers key concepts, formulas, and problem-solving strategies relevant to GATE CS exam questions on fluid mechanics and thermal science. It provides detailed explanations, examples with solutions, and common pitfalls to help students prepare effectively for the exam.