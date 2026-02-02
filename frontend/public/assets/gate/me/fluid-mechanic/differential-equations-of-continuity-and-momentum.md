**Differential Equations of Continuity and Momentum**
====================================================

### Introduction
Fluid mechanics is an essential branch of physics that deals with the behavior of fluids (liquids and gases) under various conditions. The differential equations of continuity and momentum are fundamental concepts in fluid dynamics, describing the relationship between the velocity field, pressure, and density of a fluid.

### Core Concepts
-----------------

#### **Continuity Equation**
The continuity equation is a statement of conservation of mass. It relates the change in fluid density to the rate of change of fluid velocity.

$$\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\mathbf{v}) = 0$$

where $\rho$ is the fluid density, $\mathbf{v}$ is the fluid velocity, and $t$ is time.

#### **Momentum Equation**
The momentum equation describes the relationship between the forces acting on a fluid and its resulting motion. It can be derived from Newton's second law of motion applied to a control volume.

$$\frac{\partial}{\partial t}(\rho\mathbf{v}) + \nabla\cdot(\rho\mathbf{vv}) = -\nabla p + \mu\nabla^2\mathbf{v} + \rho\mathbf{g}$$

where $\mathbf{g}$ is the gravitational acceleration, $p$ is the fluid pressure, and $\mu$ is the dynamic viscosity of the fluid.

#### **Navier-Stokes Equations**
The Navier-Stokes equations are a set of nonlinear differential equations that describe the motion of fluids. They combine the continuity equation with the momentum equation:

$$\frac{\partial \mathbf{v}}{\partial t} + \mathbf{v}\cdot\nabla\mathbf{v} = -\frac{1}{\rho}\nabla p + \nu\nabla^2\mathbf{v}$$

where $\nu$ is the kinematic viscosity.

### Key Formulas/Theorems
-------------------------

* **Continuity Equation**: $\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\mathbf{v}) = 0$
* **Momentum Equation**: $\frac{\partial}{\partial t}(\rho\mathbf{v}) + \nabla\cdot(\rho\mathbf{vv}) = -\nabla p + \mu\nabla^2\mathbf{v} + \rho\mathbf{g}$
* **Navier-Stokes Equations**: $\frac{\partial \mathbf{v}}{\partial t} + \mathbf{v}\cdot\nabla\mathbf{v} = -\frac{1}{\rho}\nabla p + \nu\nabla^2\mathbf{v}$

### Problem Solving Patterns
---------------------------

When solving problems involving differential equations of continuity and momentum, follow these steps:

1. **Identify the problem**: Determine whether you need to solve for velocity, pressure, or density.
2. **Choose the appropriate equation**: Select the continuity equation if the problem involves conservation of mass, or the momentum equation if it involves forces on a fluid.
3. **Simplify and rearrange**: Simplify the equation by canceling out terms or substituting known values.
4. **Integrate or solve numerically**: Use integration or numerical methods to find the solution.

### Examples with Solutions

**Example 1: Continuity Equation**

A tank has a circular cross-section of radius $R$ and is filled with water of density $\rho$. The water flows out through a small hole at the bottom. If the flow rate is constant, show that the velocity of the water in the tank decreases linearly with time.

Let $V(t)$ be the volume of water in the tank at time $t$. Then:

$$\frac{\partial V}{\partial t} + \nabla\cdot(\rho\mathbf{v}) = 0$$

Since the flow rate is constant, we have $\frac{\partial V}{\partial t} = -Q$, where $Q$ is a constant. Substituting this into the continuity equation gives:

$$-Q + \nabla\cdot(\rho\mathbf{v}) = 0$$

Solving for $\mathbf{v}$, we find that the velocity decreases linearly with time.

**Example 2: Momentum Equation**

A fluid of density $\rho$ flows through a pipe with a circular cross-section. The pipe has a diameter $D$ and is inclined at an angle $\theta$. Find the pressure drop $\Delta p$ across the pipe if the flow rate is constant.

Let $\mathbf{v}$ be the velocity of the fluid in the pipe. Then:

$$\frac{\partial}{\partial t}(\rho\mathbf{v}) + \nabla\cdot(\rho\mathbf{vv}) = -\nabla p + \mu\nabla^2\mathbf{v} + \rho\mathbf{g}$$

Since the flow rate is constant, we can neglect the time derivative. Substituting this into the momentum equation gives:

$$-\nabla p + \mu\nabla^2\mathbf{v} + \rho\mathbf{g} = 0$$

Solving for $p$, we find that the pressure drop is proportional to the flow rate and the length of the pipe.

### Common Pitfalls
-------------------

* **Forgetting to check units**: Make sure to check the units of the variables and constants in your solution.
* **Not accounting for boundary conditions**: Ensure that you have accounted for any boundary conditions, such as no-slip or free-surface conditions.
* **Making incorrect assumptions**: Be careful not to make assumptions about the flow field that are not justified by the problem statement.

### Quick Summary
------------------

* Continuity equation: $\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\mathbf{v}) = 0$
* Momentum equation: $\frac{\partial}{\partial t}(\rho\mathbf{v}) + \nabla\cdot(\rho\mathbf{vv}) = -\nabla p + \mu\nabla^2\mathbf{v} + \rho\mathbf{g}$
* Navier-Stokes equations: $\frac{\partial \mathbf{v}}{\partial t} + \mathbf{v}\cdot\nabla\mathbf{v} = -\frac{1}{\rho}\nabla p + \nu\nabla^2\mathbf{v}$