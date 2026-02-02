**Heat Transfer Theory Note**
==========================

**Introduction**
---------------

Heat transfer is a fundamental concept in fluid mechanics and thermal science, involving the exchange of heat between systems. It plays a crucial role in various engineering applications, such as cooling systems, heating systems, and refrigeration.

**Core Concepts**
-----------------

### 1. Modes of Heat Transfer

There are three primary modes of heat transfer:

*   **Conduction**: Direct transfer of energy between particles or bodies in physical contact.
*   **Convection**: Transfer of energy through a fluid (gas or liquid) due to motion.
*   **Radiation**: Transfer of energy through electromagnetic waves.

### 2. Heat Transfer Coefficients

Heat transfer coefficients play a vital role in determining the rate of heat transfer between systems.

*   **Convective Heat Transfer Coefficient**: Represents the amount of heat transferred per unit area per unit time due to convection.
*   **Conductive Heat Transfer Coefficient**: Represents the amount of heat transferred per unit area per unit time due to conduction.
*   **Radiative Heat Transfer Coefficient**: Represents the amount of heat transferred per unit area per unit time due to radiation.

### 3. Dimensionless Numbers

Dimensionless numbers help engineers analyze and compare different systems, reducing the need for laboratory experiments.

*   **Biot Number (Bi)**: Ratio of internal thermal resistance to external thermal resistance.
*   **Fourier Number (Fo)**: Measures the ratio of thermal diffusion time to physical time.
*   **Nusselt Number (Nu)**: Measures convective heat transfer enhancement relative to conduction.
*   **Prandtl Number (Pr)**: Measures momentum diffusivity-to-thermal diffusivity ratio.
*   **Grashof Number (Gr)**: Measures buoyancy-driven flow effects.

### 4. Heat Exchangers

Heat exchangers are devices designed for efficient heat transfer between systems.

*   **Types**: Shell and tube, plate fin, spiral, etc.
*   **Performance Parameters**: Overall heat transfer coefficient, log mean temperature difference (LMTD), etc.

**Key Formulas/Theorems**
-------------------------

### 1. Heat Transfer Rate

Heat transfer rate is given by:

$$Q = hA(T_s - T_{\infty})$$

where:

*   $h$ = convective heat transfer coefficient
*   $A$ = surface area
*   $T_s$ = surface temperature
*   $T_{\infty}$ = ambient temperature

### 2. Biot Number

Biot number is given by:

$$Bi = \frac{hL}{k}$$

where:

*   $h$ = convective heat transfer coefficient
*   $L$ = characteristic length
*   $k$ = thermal conductivity

**Problem Solving Patterns**
---------------------------

1.  **Identify the mode of heat transfer**: Conduction, convection, or radiation.
2.  **Determine relevant dimensionless numbers**: Biot number, Fourier number, Nusselt number, Prandtl number, etc.
3.  **Analyze system performance**: Heat transfer rate, overall heat transfer coefficient, log mean temperature difference (LMTD), etc.

**Examples with Solutions**
---------------------------

### Example 1: Uninsulated Cylindrical Wire

A cylindrical wire of radius 1 mm produces electric heating at a rate of 5 W/m. The surface temperature is 75°C when placed in air at 25°C. When coated with PVC of thickness 1 mm, the surface temperature reduces to 55°C.

Given:
*   $Q = 5 W/m$
*   $T_s = 75°C$ (initial)
*   $T_{\infty} = 25°C$
*   $t_{PVC} = 1 mm$

Find: Thermal conductivity of PVC ($k_{PVC}$)

Solution:
$$hA(T_s - T_{\infty}) = h(2 \pi r L) (T_s - T_{\infty})$$
Assuming same heat generation rate and convective heat transfer coefficient for both uninsulated wire and coated wire, we get:
$$Q = h(2 \pi r L) (T_s - T_{\infty})$$
$$5 W/m = h(2 \pi 1 mm 10^{-3} m) (75°C - 25°C)$$
Solving for $h$, we get:
$$h = 4.68 × 10^{6} W/m K$$

Now, using the Biot number equation:

$$Bi = \frac{hL}{k}$$
Rearranging to solve for $k$:

$$k_{PVC} = \frac{hL}{Bi}$$

### Example 2: Shell and Tube Heat Exchanger

A shell and tube heat exchanger is used as a steam condenser. Coolant water enters the tube at 300 K and at a rate of 100 kg/s. The overall heat transfer coefficient is 1500 W/m K, and the total heat transfer area is 240 m.

Given:
*   $T_c = 300 K$
*   $\dot{m}_c = 100 kg/s$
*   $U = 1500 W/m K$
*   $A_{HT} = 240 m$

Find: Temperature of coolant water coming out of the condenser ($T_{co}$)

Solution:

Assuming steam condenses at a saturation temperature of 350 K, we can use the log mean temperature difference (LMTD) equation:

$$\Delta T_{LM} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)}$$
where:
*   $\Delta T_1$ = initial temperature difference between steam and coolant water
*   $\Delta T_2$ = final temperature difference between steam and coolant water

Now, we can use the heat transfer rate equation:

$$Q = U A_{HT} \Delta T_{LM}$$
Substituting values and solving for $T_{co}$, we get:
$$T_{co} ≈ 338.8434 K$$

**Common Pitfalls**
-------------------

1.  **Incorrect assumption of mode of heat transfer**: Make sure to identify the correct mode (conduction, convection, or radiation).
2.  **Ignoring dimensionless numbers**: Use relevant dimensionless numbers to analyze system performance.
3.  **Inaccurate calculation of heat transfer rate**: Double-check calculations for heat transfer coefficients and surface areas.

**Quick Summary**
------------------

*   **Heat Transfer Modes**: Conduction, convection, and radiation
*   **Dimensionless Numbers**: Biot number, Fourier number, Nusselt number, Prandtl number, etc.
*   **Heat Exchangers**: Shell and tube, plate fin, spiral, etc.
*   **Problem Solving Patterns**: Identify mode of heat transfer, determine relevant dimensionless numbers, analyze system performance.

This comprehensive theory note covers all essential concepts in heat transfer, including modes of heat transfer, dimensionless numbers, and heat exchangers. By following the problem solving patterns and examples provided, students can develop a solid understanding of heat transfer principles and improve their ability to tackle challenging problems on this topic.