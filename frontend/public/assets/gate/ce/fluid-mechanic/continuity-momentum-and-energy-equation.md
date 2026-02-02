**Continuity Momentum and Energy Equation Theory Note**
=====================================================

### Introduction
Fluid Mechanics is a crucial subject in various engineering disciplines, including civil, mechanical, and aerospace. The continuity momentum and energy equation form the backbone of fluid dynamics. Understanding these concepts is vital for analyzing and solving problems related to fluids.

### Core Concepts
#### Continuity Equation
The continuity equation, also known as the conservation of mass principle, states that the mass flow rate through a control volume remains constant. Mathematically, it can be expressed as:

$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0$$

where $\rho$ is the fluid density, $t$ is time, and $\mathbf{v}$ is the fluid velocity.

#### Momentum Equation
The momentum equation, also known as Newton's second law for fluids, states that the force applied to a control volume is equal to the rate of change of its momentum. Mathematically, it can be expressed as:

$$\frac{\partial (\rho \mathbf{v})}{\partial t} + \nabla \cdot (\rho \mathbf{v} \mathbf{v}) = \mathbf{F}$$

where $\mathbf{F}$ is the external force applied to the control volume.

#### Energy Equation
The energy equation, also known as the first law of thermodynamics for fluids, states that the total energy of a fluid remains constant. Mathematically, it can be expressed as:

$$\frac{\partial}{\partial t} \left( \rho \mathbf{v} \cdot \mathbf{v} + p + e \right) + \nabla \cdot \left( \rho \mathbf{v} \cdot \mathbf{v} + p + e \right) = 0$$

where $p$ is the fluid pressure, and $e$ is the internal energy per unit mass.

### Key Formulas/Theorems
#### Continuity Equation:

```latex
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0
```

#### Momentum Equation:

```latex
\frac{\partial (\rho \mathbf{v})}{\partial t} + \nabla \cdot (\rho \mathbf{v} \mathbf{v}) = \mathbf{F}
```

#### Energy Equation:

```latex
\frac{\partial}{\partial t} \left( \rho \mathbf{v} \cdot \mathbf{v} + p + e \right) + \nabla \cdot \left( \rho \mathbf{v} \cdot \mathbf{v} + p + e \right) = 0
```

### Problem Solving Patterns

* Use the continuity equation to relate fluid velocity and density.
* Apply the momentum equation to determine forces acting on a control volume.
* Utilize the energy equation to analyze energy transfer between different components of a system.

### Examples with Solutions
**Example 1**

A tank is filled with water up to a certain height. If the water level drops from $5\,\text{m}$ to $3.5\,\text{m}$, determine the time taken for this process under free discharge conditions.

```mermaid
graph LR
A[Start] --> B[Calculate flow rate]
B --> C[Determine time taken]
```

**Solution**

We can apply the continuity equation to relate the flow rate and water level:

$$\frac{Q}{A} = v \Rightarrow Q = A v$$

where $A$ is the cross-sectional area of the tank, and $v$ is the average velocity of the fluid.

Using the energy equation, we can determine the time taken for the water level to drop from $5\,\text{m}$ to $3.5\,\text{m}$:

$$t = \frac{\Delta E}{Q}$$

where $\Delta E$ is the change in energy between the initial and final states.

**Example 2**

A pipe with a diameter of $100\,\text{mm}$ is connected to a tank containing water. If the pressure drop across the pipe is $10\,\text{kPa}$, determine the flow rate through the pipe.

```mermaid
graph LR
A[Start] --> B[Calculate velocity]
B --> C[Determine flow rate]
```

**Solution**

We can apply the momentum equation to relate the pressure drop and flow rate:

$$\Delta p = \frac{1}{2} \rho v^2$$

where $\Delta p$ is the pressure drop across the pipe.

Using this equation, we can determine the flow rate through the pipe:

```latex
Q = A v = \sqrt{\frac{2 \Delta p}{\rho}}
```

### Common Pitfalls

* Failing to account for energy losses in the system.
* Incorrectly applying boundary conditions or initial conditions.
* Neglecting fluid properties, such as density and viscosity.

### Quick Summary

* Continuity equation: relates mass flow rate to fluid velocity and density.
* Momentum equation: relates forces acting on a control volume to its motion.
* Energy equation: relates energy transfer between different components of a system.

By mastering these concepts, you will be well-equipped to tackle problems related to fluids in the GATE CS exam.