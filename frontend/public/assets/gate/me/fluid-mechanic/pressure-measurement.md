**Pressure Measurement**
=======================

**Introduction**
---------------

Pressure measurement is a crucial aspect of fluid mechanics, enabling us to quantify the force exerted by fluids on surfaces. This topic covers various concepts and principles relevant to pressure measurement, including ideal gas behavior, absolute pressure, gauge pressure, and the relationship between pressure and depth.

**Core Concepts**
-----------------

### 1. Ideal Gas Behavior

For a perfect gas, the equation of state is given by:

$$pV = mRT$$

where $p$ is the absolute pressure, $V$ is the volume, $m$ is the mass, $R$ is the gas constant, and $T$ is the temperature in Kelvin.

### 2. Absolute Pressure and Gauge Pressure

*   **Absolute Pressure**: The total pressure exerted by a fluid on a surface, including atmospheric pressure.
    $$P_{abs} = P_{gauge} + P_{atm}$$
*   **Gauge Pressure**: The pressure measured relative to atmospheric pressure.

### 3. Relationship between Pressure and Depth

The pressure in a liquid at depth $h$ is given by:

$$p = \rho g h$$

where $\rho$ is the density of the fluid, $g$ is the acceleration due to gravity, and $h$ is the depth below the surface.

**Key Formulas/Theorems**
-------------------------

*   **Ideal Gas Behavior**: $pV = mRT$
*   **Absolute Pressure**: $P_{abs} = P_{gauge} + P_{atm}$
*   **Pressure at Depth**: $p = \rho g h$

**Problem Solving Patterns**
---------------------------

### 1. Unsteady Flow Problems

When solving unsteady flow problems, such as Question 1 (ID: me_2021-M_31), we must consider the mass and energy balance equations.

*   **Mass Balance Equation**: $\frac{dm}{dt} = \dot{m}_{in} - \dot{m}_{out}$
*   **Energy Balance Equation**: $\frac{dE}{dt} = \dot{E}_{in} - \dot{E}_{out}$

### 2. Pressure Measurement Problems

When solving pressure measurement problems, such as Question 2 (ID: me_2021-M_33), we must consider the relationship between pressure and depth.

*   **Pressure at Depth**: $p = \rho g h$

**Examples with Solutions**
---------------------------

### 1. Example 1 - Unsteady Flow Problem

A rigid insulated tank is initially evacuated. It is connected through a valve to supply line that carries air at a constant pressure and temperature of 250 kPa and 400 K respectively. Now the valve is opened, and air is allowed to flow into the tank until the pressure inside the tank reaches to 250 kPa at which point the valve is closed. Assume that the air behaves as a perfect gas with constant properties (c1 = 1.005 kJ/kgK, c2 = 0.718 kJ/kgK, c3 = 0.287 kJ/kgK).

*   **Step 1**: Write down the mass and energy balance equations.

    $\frac{dm}{dt} = \dot{m}_{in} - \dot{m}_{out}$

    $\frac{dE}{dt} = \dot{E}_{in} - \dot{E}_{out}$

*   **Step 2**: Solve the mass and energy balance equations to find the final temperature of the air inside the tank.

    $T_f = \frac{T_i + \frac{\Delta E}{m}}{1 + \frac{\Delta m}{m}}$

where $T_f$ is the final temperature, $T_i$ is the initial temperature, $\Delta E$ is the change in energy, and $\Delta m$ is the change in mass.

    $T_f = \frac{400 + \frac{(250-100) \times 10^{-3} \times 1.005}{(0.718+0.287)/2}}{1 + \frac{(250-100) \times 10^{-3}/(1.005/2)}}$

    $T_f = 560.5 K$

### 2. Example 2 - Pressure Measurement Problem

A pressure measurement device fitted on the surface of a submarine located at a depth of H below the surface of an ocean, reads an absolute pressure of 4.2 MPa.

*   **Step 1**: Write down the equation for pressure at depth.

    $p = \rho g h$

where $\rho$ is the density of sea water, $g$ is the acceleration due to gravity, and $h$ is the depth below the surface.

*   **Step 2**: Solve for the depth H.

    $H = \frac{P_{abs} - P_{atm}}{\rho g}$

where $P_{abs}$ is the absolute pressure, $P_{atm}$ is the atmospheric pressure, $\rho$ is the density of sea water, and $g$ is the acceleration due to gravity.

    $H = \frac{(4.2 \times 10^6 - 101) / (3.105 \times 9.8)}{1}$

    $H = 398.347 m$

**Common Pitfalls**
------------------

*   Failing to consider the mass and energy balance equations in unsteady flow problems.
*   Not accounting for atmospheric pressure when measuring absolute pressure.

**Quick Summary**
-----------------

| Concept | Formula/Equation |
| --- | --- |
| Ideal Gas Behavior | $pV = mRT$ |
| Absolute Pressure | $P_{abs} = P_{gauge} + P_{atm}$ |
| Pressure at Depth | $p = \rho g h$ |
| Mass Balance Equation (Unsteady Flow) | $\frac{dm}{dt} = \dot{m}_{in} - \dot{m}_{out}$ |
| Energy Balance Equation (Unsteady Flow) | $\frac{dE}{dt} = \dot{E}_{in} - \dot{E}_{out}$ |

Note: Please let me know if you want any changes or additions.