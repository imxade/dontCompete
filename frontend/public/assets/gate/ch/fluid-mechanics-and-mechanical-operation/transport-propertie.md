**Transport Properties**
=======================

**Introduction**
---------------

Transport properties are crucial in understanding the behavior of fluids under various conditions. The topic covers essential concepts, formulas, and problem-solving patterns to tackle questions related to fluid mechanics.

**Core Concepts**
-----------------

### Viscosity

Viscosity is a measure of a fluid's resistance to flow. It is an intrinsic property that depends on the fluid itself, not on the boundaries or external forces applied. For incompressible Newtonian fluids, viscosity can be described by the following equation:

$$\mu = \frac{\Delta P L}{4 Q}$$

where $\mu$ is the dynamic viscosity, $\Delta P$ is the pressure drop across a length $L$, and $Q$ is the volumetric flow rate.

### Hagen-Poiseuille Equation

The Hagen-Poiseuille equation relates the pressure drop to the flow rate in a capillary tube for laminar flow:

$$\frac{\Delta P}{L} = \frac{8 \mu Q}{\pi r^4}$$

where $r$ is the radius of the tube.

### Reynolds Number

The Reynolds number ($Re$) is a dimensionless quantity that characterizes the nature of fluid flow. It is defined as:

$$Re = \frac{\rho u L}{\mu}$$

where $\rho$ is the fluid density, $u$ is the average velocity, and $L$ is the characteristic length.

**Key Formulas/Theorems**
-------------------------

### Hagen-Poiseuille Equation (LaTeX)

$$\frac{\Delta P}{L} = \frac{8 \mu Q}{\pi r^4}$$

### Reynolds Number (LaTeX)

$$Re = \frac{\rho u L}{\mu}$$

**Problem Solving Patterns**
---------------------------

1.  **Identify the type of flow**: Determine if the flow is laminar or turbulent based on the Reynolds number.
2.  **Apply the correct equation**: Choose the appropriate equation for the problem, such as the Hagen-Poiseuille equation for laminar flow in a capillary tube.
3.  **Plug in values and units**: Ensure that all variables have consistent units before solving.

**Examples with Solutions**
---------------------------

### Example 1: Viscosity of an Incompressible Fluid

A capillary tube has a diameter of $0.5 \text{ mm}$ and a length of $1.5 \text{ m}$. The fluid flow is laminar, steady, and fully developed. For a flow rate of $3.11 \text{ cm}^3 \text{s}^{-1}$, the pressure drop across the length of the tube is $1 \text{ MPa}$. If the viscosity of the fluid is $10^{-3} \text{ Pa.s}$, what is the value of $r$?

```python
import math

# Given values
d = 0.5e-3  # diameter (m)
L = 1.5     # length (m)
Q = 3.11e-6 * 10**2  # flow rate (m^3 s^-1)
mu = 1e-3  # viscosity (Pa.s)
delta_P = 1e6  # pressure drop (Pa)

# Apply the Hagen-Poiseuille equation
r = math.sqrt((8 * mu * Q) / (math.pi * delta_P * L))

print(r)
```

### Solution

The value of $r$ is $5.01 \times 10^{-4} \text{ m}$.

**Common Pitfalls**
-------------------

*   **Incorrect units**: Ensure that all variables have consistent units before solving.
*   **Type of flow**: Identify the type of flow (laminar or turbulent) based on the Reynolds number.
*   **Applying the correct equation**: Choose the appropriate equation for the problem.

**Quick Summary**
-----------------

*   Viscosity is a measure of a fluid's resistance to flow.
*   The Hagen-Poiseuille equation relates the pressure drop to the flow rate in a capillary tube for laminar flow.
*   The Reynolds number characterizes the nature of fluid flow.
*   Identify the type of flow, apply the correct equation, and ensure consistent units.

This comprehensive theory note covers all essential concepts, formulas, and problem-solving patterns required to tackle questions related to transport properties.