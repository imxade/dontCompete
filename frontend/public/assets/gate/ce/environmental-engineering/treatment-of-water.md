**Treatment of Water**
======================

### Introduction
-----------------

Water treatment is a crucial aspect of environmental engineering, aiming to remove contaminants and pollutants from water supplies to make them safe for human consumption. This topic involves various concepts, including settling tank design, filtration, and mass transfer modeling.

### Core Concepts
------------------

#### Settling Tank Design

A settling tank is designed to separate solid particles from liquid suspensions through gravity-induced settling. The key parameters in designing a settling tank are:

* **Detention Period (DP)**: The time required for the fluid to pass through the tank, usually expressed as hours.
* **Surface Loading Rate (SLR)**: The volume of water flowing into the tank per unit area of the surface, typically measured in liters per square meter per day.

#### Filtration

Filtration is a process where particles are removed from a fluid by passing it through a porous medium. The key concepts in filtration include:

* **Slow Discrete Settling**: Particles settle individually due to gravity, governed by Stokes' law: $v = \frac{g d^2(\rho_p - \rho_f)}{18 \mu}$.
* **Particle Size Distribution**: Understanding the size distribution of particles is crucial in designing filters.

#### Mass Transfer Modeling

Mass transfer modeling involves describing the movement and distribution of contaminants or pollutants within a system. The key concepts include:

* **Differential Equations**: Mathematical equations that describe how a quantity changes over time, such as the mass balance equation: $\frac{dm}{dt} = r - \frac{\phi m}{V}$.
* **Boundary Conditions**: Conditions that specify the behavior of the system at its boundaries.

### Key Formulas/Theorems
---------------------------

#### Settling Tank Design

* **Detention Period (DP)**: $DP = \frac{V}{Q}$
* **Surface Loading Rate (SLR)**: $SLR = \frac{Q}{A}$

where $V$ is the volume of the tank, $Q$ is the flow rate, and $A$ is the surface area.

#### Filtration

* **Stokes' Law**: $v = \frac{g d^2(\rho_p - \rho_f)}{18 \mu}$
* **Particle Size Distribution**: $\frac{dV}{dD_p} = N_0 D_p^{3.5}$

where $v$ is the settling velocity, $g$ is the acceleration due to gravity, $d$ is the particle diameter, $\rho_p$ and $\rho_f$ are the densities of the particle and fluid respectively, $\mu$ is the dynamic viscosity of the fluid, $V$ is the volume, $D_p$ is the particle size distribution, and $N_0$ is a constant.

#### Mass Transfer Modeling

* **Mass Balance Equation**: $\frac{dm}{dt} = r - \frac{\phi m}{V}$

where $m$ is the mass of the contaminant, $r$ is the reaction rate, $\phi$ is the volumetric flow rate, and $V$ is the volume of the system.

### Problem Solving Patterns
-----------------------------

#### Settling Tank Design

* **Use given data to calculate detention period and surface loading rate**: Given a flow rate and tank dimensions, calculate DP and SLR.
* **Determine height of water column in tank**: Use DP and SLR to determine the required height.

#### Filtration

* **Calculate particle settling velocity**: Use Stokes' law to calculate the settling velocity of particles.
* **Determine diameter requirements for filter media**: Use particle size distribution to determine the required diameter for anthracite, silica sand, and ilmenite sand particles.

#### Mass Transfer Modeling

* **Solve differential equation**: Solve the mass balance equation to determine the mass of contaminant at a given time.
* **Apply boundary conditions**: Apply initial and boundary conditions to solve the differential equation.

### Examples with Solutions
---------------------------

#### Example 1: Settling Tank Design

Given:

* Flow rate = 10,000,000 liters/day
* Detention period = 2 hours
* Surface loading rate = 24,000 liters/m^2/day

Required:

* Height of water column in tank (m)

Solution:
```markdown
# Settling Tank Design Example
## Step 1: Calculate detention period and surface loading rate
DP = V / Q = 10,000,000 m^3 / (24,000 m^2/day) = 416.67 hours

SLR = Q / A = 10,000,000 liters/day / 1000 m^2 = 10 m^3/m^2/day

## Step 2: Determine height of water column in tank
Height = DP \* SLR = 416.67 hours \* 24,000 liters/m^2/day = 3.00 to 3.40 m
```

#### Example 2: Filtration

Given:

* Diameter of silica sand particles = 0.20 mm
* Specific gravity of anthracite, silica sand, and ilmenite sand = 1.50, 2.60, and 4.20 respectively

Required:

* Diameter requirements for filter media (mm)

Solution:
```markdown
# Filtration Example
## Step 1: Calculate particle settling velocity using Stokes' law
v = (9.81 m/s^2 \* (0.0002 m)^2 \* (2.60 - 1)) / (18 \* 10^-3 Pa s) = 0.0026 m/s

## Step 2: Determine diameter requirements for filter media
Diameter of anthracite particles < 0.20 mm
```

### Common Pitfalls
-------------------

#### Settling Tank Design

* **Incorrect calculation of detention period and surface loading rate**: Make sure to use the correct formulas.
* **Ignoring boundary conditions**: Always apply initial and boundary conditions when solving differential equations.

#### Filtration

* **Misapplication of Stokes' law**: Use the correct formula for particle settling velocity.
* **Incorrect assumption about particle size distribution**: Understand the particle size distribution curve to determine required diameters.

#### Mass Transfer Modeling

* **Insufficient understanding of differential equation**: Make sure to understand the mass balance equation and its solution.
* **Ignoring boundary conditions**: Always apply initial and boundary conditions when solving differential equations.

### Quick Summary
------------------

* Settling tank design involves calculating detention period, surface loading rate, and height of water column in tank.
* Filtration involves particle settling velocity calculation using Stokes' law and determining diameter requirements for filter media based on particle size distribution.
* Mass transfer modeling involves solving the mass balance equation with proper application of boundary conditions.

**References**

Please note that this is a high-yield study note, not a comprehensive textbook. For further reading, refer to standard texts on environmental engineering and water treatment.

[1] Metcalf & Eddy (2020). Wastewater Engineering: Treatment, Reuse, and Recycling (8th ed.). McGraw-Hill Education.
[2] Tchobanoglous et al. (2014). Water Resources Engineering (7th ed.). McGraw-Hill Education.

**Mermaid Diagrams**
```mermaid
graph LR;
    A[Settling Tank Design] --> B[Detention Period Calculation]
    C[Filtration] --> D[Particle Settling Velocity Calculation]
    E[Mass Transfer Modeling] --> F[Differential Equation Solution]
