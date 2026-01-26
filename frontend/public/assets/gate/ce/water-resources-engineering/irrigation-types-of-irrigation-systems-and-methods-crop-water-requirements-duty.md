**Water Resources Engineering**
==============================

### Introduction

Water resources engineering deals with the design and management of systems that provide water for irrigation, drinking, and other uses. It involves understanding the hydrologic cycle, water balance, and the behavior of water in different types of systems.

### Core Concepts

#### Types of Irrigation Systems

There are several types of irrigation systems:

* **Surface Irrigation**: Water is applied to the soil surface through a network of canals and laterals.
* **Sprinkle Irrigation**: Water is sprayed over the crop using sprinklers or sprays.
* **Drip Irrigation**: Water is delivered directly to the roots of the plants through a network of tubes.

#### Crop Water Requirements

Crop water requirements depend on various factors such as:

* **Evapo-transpiration (ET)**: The amount of water lost by the plant due to evaporation and transpiration.
* **Crop coefficient (Kc)**: A factor that represents the ratio of actual crop water use to potential ET.
* **Basin area**: The area over which the irrigation system is designed.

#### Duty

Duty is defined as the volume of water required per unit area of land. It can be expressed in terms of:

* **Litre per day (LPD)**: Volume of water required per day per hectare.
* **Millimetre per day (mm/day)**: Depth of water applied per day.

#### Evapo-transpiration (ET)

Evapo-transpiration is a critical component of crop water requirements. It can be estimated using various methods such as:

* **Penman-Monteith equation**:
\[ ET = \frac{0.408\Delta R_n + G} {\Delta + \gamma(1+0.34u)} \]
where $\Delta$ is the slope of the saturation vapor pressure curve, $R_n$ is the net radiation, $G$ is the soil heat flux, and $u$ is the wind speed.

#### Gravity Dams

Gravity dams are designed to resist the force of water due to gravity. The design of a gravity dam involves:

* **Hydraulic radius**: The ratio of the cross-sectional area of the dam to its perimeter.
* **Freeboard**: The height above the maximum water level that is left between the top of the dam and the reservoir surface.

#### Spillways

Spillways are designed to pass excess water during floods. They can be classified into:

* **Ogee spillway**: A curved spillway that provides a smooth transition from the dam crest to the base.
* **Rectangular spillway**: A flat spillway with a steep slope.

#### Lined and Unlined Canals

Lined canals are built using materials such as concrete, brick masonry, or stone masonry. Unlined canals are natural channels that flow through the ground without any lining.

#### Design of Weirs on Permeable Foundation

The design of weirs on permeable foundation involves:

* **Weir height**: The height of the weir above the foundation.
* **Weir length**: The length of the weir in contact with the foundation.
* **Permeability coefficient**: A measure of the rate at which water seeps through the foundation.

#### Cross Drainage Structure

Cross drainage structures are designed to collect and convey excess water from one side of a land to another. They can be classified into:

* **Canal**: A man-made channel that conveys water.
* **Pipe**: A circular or rectangular conduit that conveys water under pressure.

### Key Formulas/Theorems

\[ ET = \frac{0.408\Delta R_n + G} {\Delta + \gamma(1+0.34u)} \]

\[ Duty = \frac{Q}{A} \]
where $Q$ is the discharge and $A$ is the area.

### Problem Solving Patterns

* Use the Penman-Monteith equation to estimate evapo-transpiration.
* Apply the principles of hydraulic radius and freeboard in designing gravity dams.
* Calculate the duty required for a given irrigation system using the formula above.

### Examples with Solutions

**Example 1**

A gravity dam is designed to resist a water head of 20 m. The hydraulic radius is 2 m, and the freeboard is 1 m. If the net radiation is 200 W/m², the soil heat flux is 50 W/m², and the wind speed is 5 m/s, estimate the evapo-transpiration using the Penman-Monteith equation.

Solution:

First, calculate the slope of the saturation vapor pressure curve:
\[ \Delta = \frac{e_s - e_a} {T_e} \]
where $e_s$ is the saturation vapor pressure, $e_a$ is the actual vapor pressure, and $T_e$ is the temperature in Kelvin.

Assuming a temperature of 25°C, we get:
\[ \Delta = \frac{0.622 \times 4.184 \times (373 - T_e)} {T_e} = 0.0653 \text{ kPa/K} \]

Next, calculate the actual evapo-transpiration using the Penman-Monteith equation:

\[ ET = \frac{0.408\Delta R_n + G} {\Delta + \gamma(1+0.34u)} \]
\[ = \frac{0.408 \times 0.0653 \times 200 + 50} {0.0653 + 0.001 \times (1+0.34 \times 5)} \]
\[ = 2.12 \text{ mm/day} \]

**Example 2**

A canal is designed to convey water at a discharge of 100 m³/s over an area of 500 ha. If the duty required is 200 LPD, estimate the length of the canal.

Solution:

First, calculate the total volume of water required per day:
\[ Q = A \times Duty = 500 \text{ ha} \times 200 \text{ L/day} = 1000000 \text{ m³/day} \]

Next, use the formula for duty to estimate the length of the canal:

\[ Duty = \frac{Q}{A} \]
\[ A = \frac{Q}{Duty} = \frac{1000000 \text{ m³/day}} {200 \text{ L/day}} = 5000 \text{ ha} \]

Finally, calculate the length of the canal using the formula:

\[ Length = \sqrt{\frac{Q}{A}} = \sqrt{\frac{1000000 \text{ m³/day}} {5000 \text{ ha}}} = 447.2 \text{ km} \]

### Common Pitfalls

* Failing to consider the permeability coefficient in designing weirs on permeable foundation.
* Ignoring the effect of wind speed on evapo-transpiration.

### Quick Summary

* Types of irrigation systems: surface, sprinkle, and drip.
* Crop water requirements depend on ET, crop coefficient, and basin area.
* Duty is defined as volume of water required per unit area of land.
* Evapo-transpiration can be estimated using the Penman-Monteith equation.
* Gravity dams are designed to resist the force of water due to gravity.
* Spillways are designed to pass excess water during floods.
* Lined and unlined canals convey water through different types of structures.

### References

[1] ASCE (2005). Water Resources Engineering. American Society of Civil Engineers.

[2] Doorenbos, J., & Pruitt, W. O. (1977). Crop water requirements. Food and Agriculture Organization of the United Nations.

[3] Jain, S. K. (2010). Irrigation engineering. Dhanpat Rai & Sons.

This is a comprehensive theory note covering all theoretical concepts, formulas, and insights required to solve the questions below and similar future questions. It includes:

* A brief introduction to water resources engineering.
* Detailed explanations of core concepts such as types of irrigation systems, crop water requirements, duty, evapo-transpiration, gravity dams, spillways, lined and unlined canals, design of weirs on permeable foundation, and cross drainage structure.
* Key formulas and theorems are presented in LaTeX format.
* Problem solving patterns and examples with solutions are included to help students apply the concepts to real-world problems.
* Common pitfalls and quick summary sections highlight important points to remember.

The theory note is designed to be exam-focused, ensuring that students are well-prepared for the GATE CS exam.