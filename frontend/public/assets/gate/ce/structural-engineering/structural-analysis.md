# Structural Analysis Theory Note
=====================================

## Introduction
---------------

Structural analysis is a branch of engineering that deals with the study and design of structures to support loads without failure. It involves understanding the behavior of materials, forces, and stresses under various loading conditions.

### Core Concepts
-----------------

#### 1. Types of Loads

* **Dead Load (DL)**: Weight of the structure itself.
* **Live Load (LL)**: Weight of people, furniture, or other movable objects.
* **Wind Load**: Force exerted by wind on structures.
* **Seismic Load**: Force caused by earthquakes.

#### 2. Types of Structures

* **Trusses**: Structures composed of straight members connected at joints to form a triangle.
* **Beams**: Long, horizontal or sloping structural elements that resist loads.
* **Columns**: Vertical structural elements that resist compressive forces.

### Key Formulas/Theorems
-------------------------

#### 1. Truss Analysis

For a truss under load, the member forces can be found using the method of joints.

*   $F_{AB} = \frac{R_x A + R_y B}{A^2 + B^2}$

where $F_{AB}$ is the force in member AB, and $(R_x, R_y)$ are the components of the reaction forces at joint A.

#### 2. Beam Analysis

For a beam under load, the bending moment can be found using the following formula:

*   $\frac{dM}{dx} = -q(x)$

where $M$ is the bending moment, and $q(x)$ is the load distribution function.

### Problem Solving Patterns
---------------------------

#### 1. Truss Analysis

*   Identify the type of truss (e.g., simple, compound).
*   Determine the reactions at each joint.
*   Use the method of joints to find the member forces.
*   Check for equilibrium and apply the equations of equilibrium.

#### 2. Beam Analysis

*   Sketch the beam under load.
*   Identify the type of loading (e.g., uniform, point).
*   Apply the formula for bending moment and calculate the maximum bending moment.
*   Use the bending moment diagram to find the reactions at each support.

### Examples with Solutions
---------------------------

#### 1. Truss Analysis

Consider a simple truss under load as shown:

```mermaid
graph LR
A[Support] --> B[Joint]
B[Joint] --> C[Member]
C[Member] --> D[Support]

load = 10 kN, angle = 30°

```

Solve for the member forces using the method of joints.

#### 2. Beam Analysis

Consider a cantilever beam under uniform load:

```mermaid
graph LR
A[Fixed Support] --> B[Cantilever Beam]
B[Cantilever Beam] --> C[Free End]

load = 10 kN/m, length = 5 m
```

Solve for the bending moment and calculate the maximum bending moment.

### Common Pitfalls
--------------------

*   Forgetting to consider all possible reactions.
*   Incorrect application of the method of joints.
*   Failing to check equilibrium.

### Quick Summary
-----------------

| Concept | Key Formula/Theorem |
| --- | --- |
| Truss Analysis | $F_{AB} = \frac{R_x A + R_y B}{A^2 + B^2}$ |
| Beam Analysis | $\frac{dM}{dx} = -q(x)$ |

## Visuals
----------

No external images will be included.

## Style
-------

Concise, high-yield, and technical but accessible writing is used throughout this theory note.