**Vector Identities**
======================

### Introduction
Vector identities are fundamental concepts in engineering mathematics that describe relationships between vectors, particularly their scalar and vector products. These identities are crucial for solving problems involving gradients, directional derivatives, and vector calculus operations.

### Core Concepts

#### Gradient Operator ($\nabla$)
The gradient operator, denoted by $\nabla$, is a vector differential operator that maps a scalar field $f(x,y,z)$ to its gradient vector:
$$
\nabla f = \frac{\partial f}{\partial x} \mathbf{i} + \frac{\partial f}{\partial y} \mathbf{j} + \frac{\partial f}{\partial z} \mathbf{k}
$$

#### Gradient of a Vector Field
Given a vector field $\vec{F}(x,y,z) = F_x(x,y,z)\mathbf{i} + F_y(x,y,z)\mathbf{j} + F_z(x,y,z)\mathbf{k}$, the gradient of $\vec{F}$ is defined as:
$$
\nabla \cdot \vec{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}
$$

### Key Formulas/Theorems

#### Gradient Theorem
The gradient theorem states that the line integral of a vector field $\vec{F}$ along a curve $C$ can be evaluated as:
$$
\int_{C} \nabla \cdot \vec{F} ds = F_x(x,y,z)dx + F_y(x,y,z)dy + F_z(x,y,z)dz
$$

#### Divergence Theorem
The divergence theorem relates the flux of a vector field $\vec{F}$ through a surface $S$ to the divergence of $\vec{F}$ in the region enclosed by $S$:
$$
\iint_{S} \nabla \cdot \vec{F} dA = \iiint_{V} \nabla \cdot \vec{F} dv
$$

#### Curl Theorem (Stokes' Theorem)
Stokes' theorem relates the circulation of a vector field $\vec{F}$ around a closed curve $C$ to the curl of $\vec{F}$ through any surface bounded by $C$:
$$
\int_{C} \nabla \times \vec{F} \cdot d\mathbf{l} = \iint_{S} (\nabla \times \vec{F}) \cdot \hat{n} dA
$$

### Problem Solving Patterns

1. **Gradient and Directional Derivative**: Use the gradient to determine the direction of maximum increase for a scalar field.
2. **Divergence Theorem**: Apply the divergence theorem to relate flux through a surface to divergence within the enclosed region.
3. **Curl and Stokes' Theorem**: Utilize Stokes' theorem to calculate circulation around a curve from curl through an enclosed surface.

### Examples with Solutions

**Example 1: Gradient of a Scalar Field**
Given $f(x,y,z) = x^2 + y^2 - z^2$, find the gradient at $(x,y,z) = (1,2,-3)$:
$$
\nabla f(1,2,-3) = \left(2x\right)\mathbf{i} + \left(2y\right)\mathbf{j} + (-2z)\mathbf{k}
$$

**Example 2: Divergence Theorem**
A vector field is given by $\vec{F}(x,y,z) = (xy^2)\mathbf{i} - (yz^2)\mathbf{j} + z^3\mathbf{k}$, with a surface $S$ bounding the region where $x^2 + y^2 + z^2 \leq 1$. Compute the flux through $S$:
$$
\nabla \cdot \vec{F} = x(2y) - y(-2z) + z(3)
$$

### Common Pitfalls

* Misinterpreting the gradient operator $\nabla$.
* Confusing divergence and curl operations.

### Quick Summary
* Gradient ($\nabla f$): Maximum increase direction for scalar fields.
* Divergence theorem: Flux through $S = \iiint_V \nabla \cdot \vec{F} dv$.
* Curl and Stokes' theorem: Circulation around curves from curl through enclosed surfaces.

![Gradient Operator](https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Nabla.png/200px-Nabla.png)

```mermaid
graph LR
  A[Scalar Field f(x,y,z)] --> B[Gradient ∇f]
  C[Divergence Theorem] --> D[Flux through S = ∫∬ ∇⋅F dA]
  E[Curl and Stokes' Theorem] --> F[Circulation around curves from curl through enclosed surfaces]
