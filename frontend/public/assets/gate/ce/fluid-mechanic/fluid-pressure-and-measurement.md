**Fluid Pressure and Measurement**
=====================================

**Introduction**
---------------

Fluid pressure is a fundamental concept in fluid mechanics that deals with the force exerted by fluids (liquids or gases) on surfaces. In this note, we will cover the theoretical concepts, formulas, and insights required to solve problems related to fluid pressure and measurement.

**Core Concepts**
-----------------

### 1. Pressure Definition

Pressure is defined as the normal force per unit area on an object or surface due to a fluid. It is measured in units of Pascals (Pa) or Newtons per square meter (N/m²).

### 2. Fluid Properties

Fluid properties relevant to pressure calculation are:

* Density ($\rho$): mass per unit volume
* Viscosity ($\mu$): measure of fluid's resistance to flow
* Specific gravity: ratio of fluid density to water density

**Key Formulas/Theorems**
-------------------------

### 1. Pressure Formula

The pressure at a point in a fluid is given by:

$$P = \rho g h + P_0$$

where:
- $P$ is the pressure at the point
- $\rho$ is the fluid density
- $g$ is the acceleration due to gravity (approximately 9.81 m/s²)
- $h$ is the height of the fluid above the reference level
- $P_0$ is the atmospheric pressure (approximately 101325 Pa)

### 2. Pressure Distribution

The pressure distribution in a static fluid can be described by:

$$\frac{dP}{dh} = \rho g$$

**Problem Solving Patterns**
---------------------------

1. **Identify Reference Level**: Determine the reference level for pressure measurement.
2. **Calculate Fluid Properties**: Find or assume the necessary fluid properties (density, viscosity, specific gravity).
3. **Apply Pressure Formula**: Use the formula to calculate pressure at the desired point.

**Examples with Solutions**
-------------------------

### Example 1: Simple Pressure Calculation

A tank contains water of height $h = 5$ m. The density of water is $\rho = 1000$ kg/m³. Calculate the pressure at the bottom of the tank.

Solution:

$$P = \rho g h = 1000 \times 9.81 \times 5 = 49050 Pa$$

### Example 2: Pressure Distribution in a Pipe

A horizontal pipe has water flowing through it. The pressure distribution is given by:

$$\frac{dP}{dh} = \rho g$$

Assuming $h$ as the height of the fluid column above the reference level, calculate the pressure at $h = 10$ m.

Solution:

$$\int \frac{dP}{dh} dh = \rho g h + C$$

where $C$ is a constant. Given that atmospheric pressure is $101325 Pa$ at sea level, we can assume $C = -101325$. Therefore,

$$P(10) = 1000 \times 9.81 \times 10 - 101325 = 98100 Pa$$

**Common Pitfalls**
------------------

1. **Units**: Be mindful of units when calculating pressure.
2. **Assumptions**: Clearly define the reference level and fluid properties used.

**Quick Summary**
-----------------

* Pressure is defined as normal force per unit area due to a fluid.
* The formula for pressure calculation is $P = \rho g h + P_0$.
* Identify reference levels, calculate fluid properties, and apply the formula to solve problems.

Note: This theory note covers the essential concepts required to solve questions related to fluid pressure and measurement. Practice with examples and past year questions will further solidify understanding of these principles.