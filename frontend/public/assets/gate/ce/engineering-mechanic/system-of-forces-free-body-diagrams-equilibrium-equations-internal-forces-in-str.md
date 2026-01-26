**System of Forces, Free Body Diagrams, Equilibrium Equations, Internal Forces, Frictions and its Application**
===========================================================

### Introduction

This theory note covers the fundamental concepts of mechanics related to systems of forces, free body diagrams, equilibrium equations, internal forces, and friction. These topics are crucial for understanding various engineering problems, particularly in structural analysis.

### Core Concepts

#### System of Forces

A system of forces is a collection of forces acting on an object or a set of objects. The system can be isolated by drawing a boundary around the objects, allowing us to analyze the internal and external forces separately.

#### Free Body Diagrams (FBD)

An FBD is a simplified representation of a system, showing only the external forces acting on it. It is essential for analyzing the equilibrium of the system and determining the reactions at various points.

#### Equilibrium Equations

The equilibrium equations describe the balance between the internal and external forces in a system. They are based on Newton's laws of motion:

* First law (inertia): The acceleration of an object is directly proportional to the net force acting on it.
* Second law (FBD): Force = mass × acceleration
* Third law (action-reaction pairs): Forces always occur in pairs, with one force acting on each object.

#### Internal Forces

Internal forces are those that act within a system, such as stresses and strains in structures. They can be classified into two types:

* **Tensile forces** (stretching or compressive)
* **Shear forces** (sliding or torsion)

#### Friction and its Application

Friction is the force opposing motion between two surfaces in contact. There are two primary types of friction:

* **Static friction**: Prevents an object from moving when a force is applied.
* **Kinetic friction**: Opposes the motion of an object once it has started.

The coefficient of friction (μ) depends on the surface roughness and material properties. For dry surfaces, μ ranges between 0.1 to 0.5.

### Key Formulas/Theorems

#### Equilibrium Equations

* ∑F = ma (Newton's second law)
* ∑M = Iα (rotational equilibrium)

#### Friction

* Ff = μN (frictional force, where N is the normal force)
* a = μg (acceleration due to friction, assuming negligible air resistance)

### Problem Solving Patterns

1. **Isolate the system**: Draw a clear boundary around the objects of interest.
2. **Draw an FBD**: Represent only the external forces acting on the system.
3. **Apply equilibrium equations**: Use Newton's laws to describe the balance between internal and external forces.
4. **Consider friction**: Account for frictional forces in your analysis, especially when dealing with inclined surfaces.

### Examples with Solutions

**Example 1: Free Body Diagrams**

A 2 kg block is suspended from a horizontal rope, with an angle of 30° between the rope and the vertical. Find the tension (T) in the rope.

```mermaid
graph LR
  A[Block] -->|T| B[Rope]
  style B fill:#ff0,stroke:#333
```

Solution: Draw an FBD showing only the external forces acting on the block:

| Force | Magnitude |
| --- | --- |
| T | ? |
| W (weight) | 2 kg × 9.81 m/s² |

Apply equilibrium equations to find T:

∑F = ma ⇒ T cos(30°) - W sin(30°) = 0

Solve for T: T ≈ 17.67 N

**Example 2: Friction**

A block with a mass of 5 kg is placed on an inclined surface with a coefficient of friction (μ) of 0.3. Find the maximum force (F) that can be applied to the block without causing it to slip.

| Force | Magnitude |
| --- | --- |
| F | ? |
| N (normal force) | 5 kg × 9.81 m/s² |

Apply friction equation: F = μN

Solve for F: F ≈ 14.85 N

### Common Pitfalls

* **Incorrectly identifying internal and external forces**: Make sure to draw a clear boundary around the system and only include external forces in your analysis.
* **Neglecting frictional forces**: Always account for friction when dealing with inclined surfaces or static systems.

### Quick Summary

| Concept | Key Points |
| --- | --- |
| System of Forces | Isolate the system, draw an FBD, apply equilibrium equations |
| Free Body Diagrams | Represent only external forces acting on the system |
| Equilibrium Equations | Apply Newton's laws to describe internal-external force balance |
| Internal Forces | Tensile and shear forces within a structure |
| Friction | Static and kinetic friction, coefficient of friction (μ) |

### Sources

* GATE 2021 Question ID: ce_2021-M_22
* Wikipedia: Mechanics