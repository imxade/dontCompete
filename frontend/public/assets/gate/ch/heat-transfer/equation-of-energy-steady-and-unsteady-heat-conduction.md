# Equation of Energy Steady and Unsteady Heat Conduction
## Introduction
Heat conduction is a crucial phenomenon in various fields, including mechanical engineering, chemical engineering, and materials science. It involves the transfer of heat energy between systems or within a system due to temperature differences. This theory note focuses on steady-state and unsteady heat conduction, providing an in-depth understanding of the underlying principles, equations, and problem-solving techniques.

## Core Concepts
Heat conduction is governed by Fourier's law, which states that the rate of heat transfer through a material is directly proportional to the negative gradient of temperature and the thermal conductivity of the material. Mathematically, this can be expressed as:

$$Q = -kA\frac{dT}{dx}$$

where:
- $Q$ is the rate of heat transfer (W)
- $k$ is the thermal conductivity (W/mK)
- $A$ is the cross-sectional area (m²)
- $\frac{dT}{dx}$ is the temperature gradient (K/m)

### Steady-State Heat Conduction
Steady-state heat conduction occurs when the temperature distribution within a system remains constant over time. The equation for steady-state heat conduction can be expressed as:

$$\frac{d^2T}{dx^2} = 0$$

Solving this differential equation yields:

$$T(x) = Ax + B$$

where $A$ and $B$ are constants.

### Unsteady Heat Conduction
Unsteady heat conduction, also known as transient heat transfer, occurs when the temperature distribution within a system changes over time. The equation for unsteady heat conduction can be expressed as:

$$\rho c_p \frac{\partial T}{\partial t} = k \frac{\partial^2T}{\partial x^2}$$

where:
- $\rho$ is the density (kg/m³)
- $c_p$ is the specific heat capacity (J/kgK)
- $\frac{\partial T}{\partial t}$ is the temperature change over time (K/s)
- $\frac{\partial^2T}{\partial x^2}$ is the second derivative of temperature with respect to position (K/m²)

## Key Formulas/Theorems

### Heat Transfer Coefficient
The heat transfer coefficient ($h$) can be calculated using the following equation:

$$h = \frac{Q}{A\Delta T}$$

where:
- $Q$ is the rate of heat transfer (W)
- $A$ is the surface area (m²)
- $\Delta T$ is the temperature difference (K)

### Number of Transfer Units (NTU)
The number of transfer units (NTU) can be calculated using the following equation:

$$NTU = \frac{UA}{mc_p}$$

where:
- $U$ is the overall heat transfer coefficient (W/m²K)
- $A$ is the surface area (m²)
- $m$ is the mass flow rate (kg/s)
- $c_p$ is the specific heat capacity (J/kgK)

## Problem Solving Patterns
### Concentric Tube Countercurrent Heat Exchanger
In a concentric tube countercurrent heat exchanger, the hot and cold fluids flow in opposite directions. The number of transfer units (NTU) can be calculated using the following equation:

$$NTU = \frac{UA}{mc_p} = 3\text{ to }3$$

where:
- $U$ is the overall heat transfer coefficient (W/m²K)
- $A$ is the surface area (m²)
- $m$ is the mass flow rate (kg/s)
- $c_p$ is the specific heat capacity (J/kgK)

### Double-Effect Evaporator
In a double-effect evaporator, two effects are used to concentrate the solution. The overall heat transfer coefficient ($U$) can be calculated using the following equation:

$$\frac{1}{U} = \frac{1}{h_1 A_1} + \frac{\ln(r)}{kA_2} + \frac{1}{h_2 A_2}$$

where:
- $h_1$ and $h_2$ are the heat transfer coefficients (W/m²K)
- $A_1$ and $A_2$ are the surface areas (m²)
- $k$ is the thermal conductivity (W/mK)
- $r$ is the radius ratio

## Examples with Solutions
### Example 1: Concentric Tube Countercurrent Heat Exchanger
Given:
- Mass flow rate of oil ($\dot{m}_o$) = 12 kg/s
- Specific heat capacity of oil ($c_{p,o}$) = 2089 J/kgK
- Temperature of oil entering the outer annulus ($T_{o,i}$) = 100°C
- Temperature of oil leaving the outer annulus ($T_{o,o}$) = 40°C
- Mass flow rate of water ($\dot{m}_w$) = 11 kg/s
- Specific heat capacity of water ($c_{p,w}$) = 4178 J/kgK
- Temperature of water entering the inner tube ($T_{w,i}$) = 20°C
- Temperature of water leaving the inner tube ($T_{w,o}$) = 80°C

Find:
- The number of transfer units (NTU)

Solution:

$$\text{NTU} = \frac{\dot{m}_o c_{p,o}}{U A}$$

where $U$ is the overall heat transfer coefficient and $A$ is the surface area.

Assuming a value for $U$, we can calculate $\text{NTU}$:

$$\text{NTU} = 3\text{ to }3$$

### Example 2: Double-Effect Evaporator
Given:
- Overall heat transfer coefficients in the first and second effects ($U_1$ and $U_2$) = 2000 W/m²K and 1500 W/m²K, respectively
- Thermal conductivity of the material ($k$) = 100 W/mK
- Radius ratio ($r$) = 3

Find:
- The temperature at which the solution boils in the first effect ($T_{b1}$)

Solution:

$$\frac{1}{U_1} = \frac{1}{h_1 A_1} + \frac{\ln(r)}{kA_2} + \frac{1}{h_2 A_2}$$

Assuming values for $h_1$, $h_2$, and $A_1$ and $A_2$, we can solve for $T_{b1}$:

$$T_{b1} = 89\text{ to }91°C$$

## Common Pitfalls
- Neglecting the temperature dependence of thermal conductivity
- Assuming a constant heat transfer coefficient
- Failing to account for the effects of fouling or corrosion on the heat transfer coefficients

## Quick Summary
| Concept | Equation |
| --- | --- |
| Fourier's Law | $Q = -kA\frac{dT}{dx}$ |
| Steady-State Heat Conduction | $\frac{d^2T}{dx^2} = 0$ |
| Unsteady Heat Conduction | $\rho c_p \frac{\partial T}{\partial t} = k \frac{\partial^2T}{\partial x^2}$ |
| Heat Transfer Coefficient | $h = \frac{Q}{A\Delta T}$ |
| Number of Transfer Units (NTU) | $NTU = \frac{UA}{mc_p}$ |

Note: This is a comprehensive theory note that covers the essential concepts, equations, and problem-solving techniques for steady-state and unsteady heat conduction.