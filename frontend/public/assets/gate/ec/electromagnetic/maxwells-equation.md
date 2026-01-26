# Maxwell's Equations
## Introduction
Maxwell's equations are a set of four fundamental equations in classical electromagnetism that describe how electric and magnetic fields interact with each other. These equations were derived by James Clerk Maxwell in 1864 and are considered one of the most important achievements in physics.

## Core Concepts

### Electric Displacement Density Vector
The electric displacement density vector, denoted as $\mathbf{D}$, is a measure of the density of electric charge at a given point in space. It is related to the electric field $\mathbf{E}$ by the equation:

$$\mathbf{D} = \epsilon_0 \mathbf{E} + \frac{\rho}{c^2} \mathbf{v}$$

where $\epsilon_0$ is the electric constant (also known as the permittivity of free space), $\rho$ is the charge density, $c$ is the speed of light, and $\mathbf{v}$ is the velocity of the charged particles.

### Gauss's Law
Gauss's law states that the total electric flux through a closed surface is proportional to the charge enclosed within that surface. Mathematically, it can be expressed as:

$$\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q}{\epsilon_0}$$

where $S$ is the closed surface, $\mathbf{E}$ is the electric field, $d\mathbf{A}$ is the area vector of the surface element, and $Q$ is the charge enclosed within the surface.

### Maxwell's Equations
Maxwell's equations are a set of four fundamental equations that describe how electric and magnetic fields interact with each other. They are:

1. Gauss's law for magnetism:

$$\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$$

where $\mathbf{B}$ is the magnetic field.

2. Faraday's law of induction:

$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

3. Ampere's law with Maxwell's correction:

$$\nabla \times \mathbf{B} = \mu_0 (\mathbf{J} + \epsilon_0 \frac{\partial \mathbf{E}}{\partial t})$$

where $\mathbf{J}$ is the current density, and $\mu_0$ is the magnetic constant (also known as the permeability of free space).

4. Gauss's law for electric field:

$$\nabla \cdot \mathbf{D} = \rho$$

## Key Formulas/Theorems
LaTeX notation will be used to represent mathematical equations.

### Electric Displacement Density Vector

```latex
\mathbf{D} = \epsilon_0 \mathbf{E} + \frac{\rho}{c^2} \mathbf{v}
```

### Gauss's Law

```latex
\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q}{\epsilon_0}
```

## Problem Solving Patterns
The following patterns can be used to solve problems related to Maxwell's equations:

* When applying Gauss's law, ensure that the charge enclosed within the surface is correctly calculated.
* When using Faraday's law of induction, consider the change in magnetic flux through a closed surface.
* When applying Ampere's law with Maxwell's correction, account for both the current density and the displacement current.

## Examples with Solutions

### Example 1: Electric Displacement Density Vector
Consider a point charge $q$ located at the origin. Find the electric displacement density vector $\mathbf{D}$ at a distance $r$ from the charge.

```latex
\mathbf{D} = \frac{q}{4\pi\epsilon_0 r^2} \hat{\mathbf{r}}
```

### Example 2: Gauss's Law
A spherical surface of radius $R$ encloses a total charge $Q$. Find the electric field $\mathbf{E}$ at the surface using Gauss's law.

```latex
\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q}{\epsilon_0}
```

## Common Pitfalls

* Failing to account for the displacement current in Ampere's law.
* Incorrectly applying Gauss's law, particularly when dealing with non-spherical charges or surfaces.
* Neglecting the change in magnetic flux through a closed surface when using Faraday's law of induction.

## Quick Summary
* Electric displacement density vector $\mathbf{D}$ is related to electric field $\mathbf{E}$ by: $\mathbf{D} = \epsilon_0 \mathbf{E} + \frac{\rho}{c^2} \mathbf{v}$
* Gauss's law states that total electric flux through a closed surface is proportional to charge enclosed within the surface.
* Maxwell's equations describe how electric and magnetic fields interact with each other.

Note: The above theory note covers the essential concepts, formulas, and problem-solving patterns related to Maxwell's equations. It also highlights common pitfalls to avoid when solving problems.