**Thermodynamics Study Note**
==========================

### Introduction
---------------

Thermodynamics is a branch of physics that deals with heat, work, temperature, and their relation to energy, radiation, and physical properties of matter. This note covers key concepts in fluid mechanics and thermal science relevant for the GATE CS exam.

### Core Concepts
-----------------

#### 1. Polytropic Process

A polytropic process is a thermodynamic process where the relationship between pressure (P) and volume (V) is given by:

$$ PV^n = C $$

where $n$ is the polytropic index, and $C$ is a constant.

The work done in a polytropic process can be calculated using the formula:

$$ W = \frac{P_1 V_1 - P_2 V_2}{n-1} $$

#### 2. Equations of State

The equation of state for an ideal gas is given by:

$$ PV = nRT $$

where $n$ is the number of moles, $R$ is the gas constant, and $T$ is the temperature in Kelvin.

For a real gas, we can use the virial equation:

$$ \frac{PV}{RT} = 1 + B(T)P + C(T)P^2 $$

where $B(T)$ and $C(T)$ are functions of temperature.

#### 3. Phase Diagrams

A phase diagram is a graphical representation of the phases present in a system as a function of temperature and pressure. For a pure substance, we can plot the liquid-vapor boundary using the Clapeyron equation:

$$ \frac{dP}{dT} = \frac{\Delta H_{vap}}{\Delta V_{vap}} $$

### Key Formulas/Theorems
-------------------------

* **First Law of Thermodynamics**: $\Delta U = Q - W$
* **Second Law of Thermodynamics**: $T_s = T_r$ (Carnot cycle)
* **Ideal Gas Equation**: $PV = nRT$

### Problem Solving Patterns
-----------------------------

1.  **Polytropic Process**:
    *   Use the formula for work done in a polytropic process.
    *   Identify the polytropic index and the initial and final states.
2.  **Phase Diagrams**:
    *   Plot the liquid-vapor boundary using the Clapeyron equation.
    *   Identify the triple point and its properties.

### Examples with Solutions
---------------------------

1.  **Polytropic Process Example**

    Given: $P_1 = 110$ kPa, $V_1 = 5$ m³, $V_2 = 2.5$ m³, $n = 1.2$

    Find: Work done in the process

    Solution:

    \begin{align*}
    W &= \frac{P_1 V_1 - P_2 V_2}{n-1} \\
    &\approx \frac{(110)(5) - (1)(2.5)}{1.2-1} \\
    &\approx 408.912 \text{ kJ}
    \end{align*}

2.  **Phase Diagram Example**

    Given: Liquid-vapor boundary equation:

    $$ \ln \frac{P}{T} = - \frac{3063}{24.38} $$

    Solid-vapour boundary equation:

    $$ \ln \frac{P}{T} = - \frac{3754}{27.92} $$

    Find: Triple point temperature

    Solution:

    Equating the two equations:

    $$ \frac{3754}{27.92} = \frac{3063}{24.38} $$

    Solving for $T$:

    $$ T = 195.19 \text{ K} $$

### Common Pitfalls
-------------------

1.  **Polytropic Process**:
    *   Don't forget to identify the polytropic index.
    *   Be careful with units and dimensions.

2.  **Phase Diagrams**:
    *   Plot the correct boundaries.
    *   Identify the triple point correctly.

### Quick Summary
-----------------

*   Polytropic process: $PV^n = C$
*   Equations of state: ideal gas, real gas (virial equation)
*   Phase diagrams: liquid-vapor boundary, solid-vapour boundary

This note covers key concepts in thermodynamics relevant for the GATE CS exam.