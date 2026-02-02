**Pure Substance**
================

### Introduction
---------------

A pure substance is a homogeneous mixture of various chemical species that have the same composition and properties throughout. In engineering thermodynamics, we often deal with systems consisting of a single phase (pure substance) or multiple phases in equilibrium.

### Core Concepts
-----------------

#### Definition
A pure substance can exist in different states:

*   **Solid**: crystalline structure
*   **Liquid**: molecular arrangement without fixed shape
*   **Gas**: molecules freely moving and spreading

The thermodynamic properties of a pure substance depend on the state it is in, including its temperature (T), pressure (P), specific volume (v), and entropy (s).

#### Equations of State
Some fundamental equations describe how these variables interact:

*   **Ideal Gas Law** ($PV=nRT$): $PV=(n/M)RT$ for a pure substance, where M is molar mass.
*   **Van der Waals Equation**: $$(P + \frac{a}{v^2})(v - b) = RT$$

#### Compressibility Factor (Z)
The compressibility factor helps us account for deviations from ideal behavior. It's defined as:

$$
Z=\frac{PV}{nRT}
$$

where the term "ideal" refers to an ideal gas.

### Key Formulas/Theorems
---------------------------

#### Specific Heat Capacity
Specific heat capacity at constant volume ($c_v$) and constant pressure ($c_p$):

*   $$c_p = c_v + R$$

#### Entropy Change
The entropy change of a pure substance is given by:

$$\Delta s = \int\frac{dq_T}{T}$$

### Problem Solving Patterns
-----------------------------

1.  **State Identification**: Determine the initial and final states of the system.
2.  **Property Tables/Charts**: Use them to find property values (e.g., saturation temperature, specific volume).
3.  **Equations of State**: Apply relevant equations to relate variables.

### Examples with Solutions
---------------------------

#### Q1: Temperature Calculation

Let's solve Q1: Superheated steam at 1500 kPa has a specific volume $v = 2.75 \ m^3/kmol$ and compressibility factor $(Z) = 0.95$. The temperature of the steam is ______°C.

Using the ideal gas law ($PV = nRT$), we can find the temperature:

$$
\begin{align*}
n &= P V / (R T) \\
&= \frac{(150000 \ Pa)(2.75 \times 10^{-3} m^3)}{(8314.5 J/kmol \cdot K)}
\end{align*}
$$

Solving for $T$ yields the temperature of the steam:

```latex
\begin{align*}
T &= \frac{(150000 Pa)(2.75 \times 10^{-3} m^3)}{(8314.5 J/kmol \cdot K)Z} \\
&= \boxed{249 C} 
\end{align*}
```

#### Q2: Total Mass Calculation

To solve Q2, we'll use the given properties and find the total mass of the liquid-vapor mixture.

The specific volume of saturated vapor ($v_g$) is $0.46242 m^3/kg$, while that of saturated liquid ($v_f$) is $0.001084 m^3/kg$. The given percentage of liquid (20%) and vapor (80%) allows us to set up an equation for the total mass:

$$
m = \frac{V}{v_f} \cdot 0.2 + \frac{V}{v_g} \cdot 0.8
$$

Solving this yields the total mass of the mixture:

```latex
\begin{align*}
m &= \frac{(50 m^3)}{0.001084 m^3/kg} \cdot 0.2 + \frac{(50 m^3)}{0.46242 m^3/kg} \cdot 0.8 \\
&= \boxed{135.08 kg}
\end{align*}
```

### Common Pitfalls
------------------

1.  **State Identification**: Ensure you correctly identify the initial and final states of the system.
2.  **Equation Application**: Apply the correct equation to relate variables (e.g., ideal gas law, Van der Waals).
3.  **Unit Consistency**: Maintain unit consistency throughout calculations.

### Quick Summary
-----------------

*   Pure substance: homogeneous mixture with same composition and properties throughout
*   Equations of state:
	+   Ideal gas law ($PV=nRT$)
	+   Van der Waals Equation $$(P + \frac{a}{v^2})(v - b) = RT$$
*   Key formulas:
	+   Compressibility factor (Z): $$\frac{PV}{nRT}$$
	+   Specific heat capacity ($c_p$ and $c_v$):
		-   $$c_p = c_v + R$$