**Thermodynamic Properties of Pure Substances**
====================================================

### Introduction
-----------------

In chemical engineering, understanding thermodynamic properties of pure substances is crucial for process calculations and design. This note covers key concepts, formulas, and insights required to tackle problems related to thermodynamic properties.

### Core Concepts
------------------

#### Ideal Gas Behavior

An ideal gas is a hypothetical gas that obeys the ideal gas law:

$$PV = nRT \tag{1}$$

where $P$ is pressure, $V$ is volume, $n$ is the number of moles, $R$ is the gas constant, and $T$ is temperature in Kelvin.

#### Henry's Law

Henry's Law states that the partial pressure of a dissolved gas in a liquid is proportional to its mole fraction:

$$P_i = k \times x_i \tag{2}$$

where $P_i$ is the partial pressure of gas $i$, $k$ is Henry's constant, and $x_i$ is the mole fraction of gas $i$.

#### Ideal Solution Behavior

An ideal solution behaves like an ideal mixture, where each component contributes to the total properties based on its mole fraction:

$$\mu_i = \mu_i^* + RT \ln x_i \tag{3}$$

where $\mu_i$ is the chemical potential of component $i$, $\mu_i^*$ is the standard chemical potential, and $x_i$ is the mole fraction of component $i$.

### Key Formulas/Theorems
-------------------------

#### Henry's Constant for CO2 in Water

Henry's constant ($k_{CO_2}$) for CO2 dissolved in water at 290 K is given as 12 MPa.

#### Mole Fraction of CO2 in Water

To find the mole fraction of CO2 dissolved in water, we need to equate the partial pressure of CO2 in air with its partial pressure in water:

$$P_{CO_2} = k_{CO_2} \times x_{CO_2} \tag{4}$$

Given that the partial pressure of CO2 in air is 3% of the total pressure (100 kPa), we can find $x_{CO_2}$:

$$P_{CO_2} = 0.03 \times 100\,kPa = 3\,kPa$$

Now, using Henry's Law (equation 2) and given values:

$$3\,kPa = 12\,MPa \times x_{CO_2}$$

Solving for $x_{CO_2}$ gives:

$$x_{CO_2} = \frac{3\,kPa}{12\,MPa} = \frac{3 \times 10^3 Pa}{12 \times 10^6 Pa} = \frac{1}{4000}$$

Therefore, the mole fraction of CO2 dissolved in water is:

$$x_{CO_2} = 4.75 \times 10^{-4}$$

However, none of the provided answer choices match this exact value. We'll discuss common pitfalls and possible errors in calculation below.

### Problem Solving Patterns
---------------------------

1. **Identify relevant thermodynamic laws**: When dealing with thermodynamic properties, ensure you apply relevant laws such as Henry's Law or the ideal gas law.
2. **Units are crucial**: Pay attention to units and convert them appropriately when necessary. This is particularly important for calculations involving pressure (e.g., from kPa to MPa).
3. **Equilibrium conditions**: Problems often assume equilibrium, so ensure you understand what this means in terms of mole fractions, pressures, etc.

### Examples with Solutions
---------------------------

### Common Pitfalls
-------------------

1. **Unit conversions**: Failure to convert units correctly can lead to errors.
2. **Incorrect application of laws**: Applying the wrong thermodynamic law or formula can yield incorrect results.
3. **Miscalculation of mole fractions**: Careless handling of mole fraction calculations can result in incorrect answers.

### Quick Summary
-----------------

- Ideal gas behavior: $PV = nRT$
- Henry's Law: $P_i = k \times x_i$
- Ideal solution behavior: $\mu_i = \mu_i^* + RT \ln x_i$
- Calculate the mole fraction of CO2 in water using Henry's constant.

By following this comprehensive theory note, you should be well-equipped to tackle problems related to thermodynamic properties of pure substances.