**Fluid Kinematics and Fluid in Relative Equilibrium**
=====================================================

### Introduction

Fluid kinematics deals with the study of motion of fluids, without considering the forces that cause this motion. Fluids can be classified as either compressible or incompressible based on their behavior under changing pressure conditions.

### Core Concepts

#### **Compressibility**

*   A fluid is said to be **incompressible** if its density remains constant even when subjected to a change in pressure.
*   On the other hand, a fluid is considered **compressible** if its density changes with varying pressure.

#### **Rotational and Irrotational Flows**

*   In a rotational flow, the fluid particles follow a curved path, resulting in a non-zero value of curl of velocity vector (ω ≠ 0).
*   An irrotational flow has fluid particles moving in a straight line, characterized by zero curl of the velocity vector (ω = 0).

### Key Formulas/Theorems

#### **Euler's Equation**

\[
\frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v}\cdot\nabla)\mathbf{v}=-\frac{1}{\rho}\nabla p+\nu\nabla^2\mathbf{v}
\]

#### **Bernoulli's Equation**

\[p + \frac{1}{2} \rho v^2 + \rho gy = C\]

where $C$ is a constant, and $\rho$ is the density of the fluid.

### Problem Solving Patterns

*   Identify whether the problem deals with compressible or incompressible fluids.
*   Determine if the flow is rotational or irrotational based on the velocity field.
*   Use Euler's equation for inviscid flows (no viscosity) and Bernoulli's equation for steady, incompressible flows.

### Examples with Solutions

**Example 1:**

Given a flow represented by:

\[\mathbf{v} = \begin{pmatrix} u \\ v \end{pmatrix} = \begin{pmatrix} x^2 - y^2 \\ xy \end{pmatrix}\]

Is the flow irrotational or rotational?

**Solution:**

To check if the flow is irrotational, we need to find the curl of the velocity vector:

\[\nabla \times \mathbf{v} = \begin{vmatrix} i & j & k \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ u & v & 0 \end{vmatrix}\]

Substituting the given values:

\[\nabla \times \mathbf{v} = (x^2 - y^2)j - (xy)i\]

Since the curl is non-zero, the flow is rotational.

**Example 2:**

A fluid with a density of $1000 kg/m^3$ flows through a pipe. If the pressure at point A is $10^5 Pa$, and at point B is $20^5 Pa$, find the change in velocity if the flow is steady, incompressible, and irrotational.

**Solution:**

Using Bernoulli's equation:

\[p + \frac{1}{2} \rho v^2 = C\]

At point A:

\[10^5 + 0 = C\]

At point B:

\[20^5 + \frac{1}{2}\rho v_B^2 = C\]

Substituting the constant and rearranging terms gives us the velocity at point B.

### Common Pitfalls

*   Misidentifying compressible or incompressible fluids.
*   Failing to recognize rotational or irrotational flows.
*   Incorrect application of Euler's or Bernoulli's equations.

### Quick Summary

*   Compressibility: Incompressible (constant density) vs. Compressible (variable density).
*   Rotational and Irrotational Flows: Determined by the curl of velocity vector.
*   Key Formulas: Euler's Equation, Bernoulli's Equation.