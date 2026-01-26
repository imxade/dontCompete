**Steady and Unsteady State Mass and Energy Balance**
=====================================================

**Introduction**
---------------

In this topic, we will discuss the fundamental concepts of mass and energy balance in both steady and unsteady state processes. Understanding these principles is crucial for designing and optimizing various chemical engineering systems.

**Core Concepts**
-----------------

### Steady State

A system is said to be at a steady state when there are no changes in its properties over time, i.e., the system is in equilibrium. The mass and energy balance equations can be written as:

* **Mass Balance:**

∑(in) = ∑(out)

where ∑(in) represents the total mass entering the system, and ∑(out) represents the total mass leaving the system.

* **Energy Balance:**

Q - W = ΔE

where Q is the net heat transfer, W is the work done on the system, and ΔE is the change in energy of the system.

### Unsteady State

A system is said to be at an unsteady state when there are changes in its properties over time. The mass and energy balance equations can be written as:

* **Mass Balance:**

ρ = ρ0 \* e^(-(∫(u dx) / (∫(v dx))

where ρ is the density of the system, ρ0 is the initial density, u is the velocity of the system, and v is the volumetric flow rate.

* **Energy Balance:**

dE/dt = Q - W

where dE/dt represents the change in energy over time.

**Key Formulas/Theorems**
-------------------------

### Energy Balance

The first law of thermodynamics states that energy cannot be created or destroyed, only converted from one form to another. Mathematically, this can be represented as:

∑(Q - W) = ∆E

where Q is the net heat transfer, W is the work done on the system, and ΔE is the change in energy of the system.

### Mass Balance

The mass balance equation can be written as:

∑(in) = ∑(out)

where ∑(in) represents the total mass entering the system, and ∑(out) represents the total mass leaving the system.

**Problem Solving Patterns**
---------------------------

* **Heat Exchanger Analysis:** When analyzing heat exchangers, we need to consider the heat transfer between the hot and cold fluids. We can use the following formula:

Q = U \* A \* ΔT

where Q is the heat transfer rate, U is the overall heat transfer coefficient, A is the heat transfer area, and ΔT is the temperature difference.

* **Steady State Analysis:** When analyzing systems at steady state, we need to consider the mass and energy balance equations. We can use the following formula:

∑(in) = ∑(out)

and

Q - W = ΔE

**Examples with Solutions**
---------------------------

### Example 1: Heat Exchanger Analysis

Hot oil at 110°C heats water from 30°C to 70°C in a counter-current double-pipe heat exchanger. The flow rates of water and oil are 50 kg/min-1 and 100 kg/min-1, respectively, with specific heat capacities of 4.2 kJ/kg-K-1 and 2.0 kJ/kg-K-1, respectively. Assume the heat exchanger is at steady state. If the overall heat transfer coefficient is 200 W/m²-C-1, find the heat transfer area.

Solution:

First, we need to calculate the heat transfer rate using the energy balance equation:

Q - W = ΔE

Since the system is at steady state, W = 0. Therefore,

Q = ∑(out) \* C_p \* (T_out - T_in)

where Q is the heat transfer rate, ∑(out) is the mass flow rate of water, C_p is the specific heat capacity of water, and T_out and T_in are the outlet and inlet temperatures of water.

Q = 50 kg/min-1 \* 4.2 kJ/kg-K-1 \* (70°C - 30°C)
= 11,700 W

Next, we can use the heat transfer equation to find the heat transfer area:

Q = U \* A \* ΔT

Rearranging the equation to solve for A, we get:

A = Q / (U \* ΔT)

Substituting the values, we get:

A = 11,700 W / (200 W/m²-C-1 \* (70°C - 30°C))
= 17.9 m²

### Example 2: Steady State Analysis

Consider a tank filled with three immiscible liquids A, B, and C at static equilibrium, as shown in the figure.

At 2 cm below the liquid A – liquid B interface, a tube is connected from the side of the tank. Both the tank and the tube are open to the atmosphere.

The specific gravities of liquids A, B, and C are 1, 2, and 4, respectively. Neglect any surface tension effects in the calculations. Find the length of the tube L that is wetted by liquid B.

Solution:

First, we need to calculate the pressure at the interface between liquids A and B using the formula:

P = ρ \* g \* h

where P is the pressure, ρ is the density of the liquid, g is the acceleration due to gravity, and h is the height of the liquid.

Since the specific gravity of liquid A is 1, its density is equal to that of water (approximately 1000 kg/m³). Therefore,

P = 1000 kg/m³ \* 9.81 m/s² \* 2 cm
= 196 Pa

Next, we can use the pressure at the interface between liquids A and B to calculate the length of the tube L that is wetted by liquid B.

Since the specific gravity of liquid B is 2, its density is twice that of water. Therefore,

L = P / (ρ \* g)
= 196 Pa / (2000 kg/m³ \* 9.81 m/s²)
= 10 cm

However, this is not the correct answer since the tube is open to the atmosphere. We need to consider the pressure at the interface between liquids B and C.

The specific gravity of liquid C is 4, so its density is four times that of water. Therefore,

P = ρ \* g \* h
= 4000 kg/m³ \* 9.81 m/s² \* (2 cm + L)
= P

Simplifying the equation, we get:

L = 8 cm

**Common Pitfalls**
-------------------

* **Incorrect Assumptions:** Be careful when making assumptions about the system, especially in unsteady state problems.
* **Incorrect Calculations:** Double-check your calculations to ensure you are using the correct formulas and values.

**Quick Summary**
------------------

* Steady state: ∑(in) = ∑(out) and Q - W = ΔE
* Unsteady state: dE/dt = Q - W
* Energy balance: ∑(Q - W) = ΔE
* Mass balance: ∑(in) = ∑(out)
* Heat transfer equation: Q = U \* A \* ΔT