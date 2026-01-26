**Radiative Heat Transfer**
==========================

**Introduction**
---------------

Radiative heat transfer is the transfer of energy through electromagnetic waves, also known as radiation. It is an important mode of heat transfer that occurs between objects at different temperatures. In this theory note, we will cover the principles and formulas required to solve problems related to radiative heat transfer.

**Core Concepts**
-----------------

### 1. Stefan-Boltzmann Law

The Stefan-Boltzmann law describes the total energy radiated per unit surface area of a blackbody across all wavelengths per unit time. It is given by:

$$E = \sigma T^4$$

where $E$ is the total energy radiated, $\sigma$ is the Stefan-Boltzmann constant ($5.669 \times 10^{-8} W/m^{2}K^{-4}$), and $T$ is the absolute temperature of the blackbody.

### 2. Absorptivity

Absorptivity is a measure of how much radiation is absorbed by an object. It is defined as the ratio of the absorbed energy to the incident energy. For a flat plate, the absorptivity is given by:

$$\alpha = \frac{E_{abs}}{E_{inc}}$$

### 3. Emissivity

Emissivity is a measure of how much radiation an object emits compared to a blackbody. It is defined as the ratio of the emitted energy to the energy radiated by a blackbody at the same temperature.

### 4. Radiative Heat Transfer Coefficient

The radiative heat transfer coefficient (h_r) is a measure of the rate of heat transfer between two objects due to radiation. It is given by:

$$h_r = \frac{\sigma (T_1^4 - T_2^4)}{L}$$

where $L$ is the distance between the objects.

**Key Formulas/Theorems**
-------------------------

### 1. Stefan-Boltzmann Law

$$E = \sigma T^4$$

### 2. Absorptivity

$$\alpha = \frac{E_{abs}}{E_{inc}}$$

### 3. Emissivity

$$e = \frac{E_{emitted}}{\sigma T^4}$$

**Problem Solving Patterns**
---------------------------

1. Calculate the total energy radiated by an object using the Stefan-Boltzmann law.
2. Determine the absorptivity of an object and calculate the absorbed energy.
3. Use the radiative heat transfer coefficient to calculate the rate of heat transfer between two objects.

**Examples with Solutions**
-------------------------

### 1. Example 1

A flat plate made of cast iron is exposed to a solar flux of $600 W/m^{2}$ at an ambient temperature of $25^{\circ}C$. Assume that the entire solar flux is absorbed by the plate. Cast iron has a low temperature absorptivity of $0.21$. Use the Stefan-Boltzmann constant ($5.669 \times 10^{-8} W/m^{2}K^{-4}$). Neglect all other modes of heat transfer except radiation.

Solve for the radiation equilibrium temperature of the plate:

```mermaid
graph LR
A[Given Data] --> B[Ambient Temp = 25°C, Solar Flux = 600 W/m^2]
B --> C[Absorptivity (α) = 0.21]
C --> D[E = σ(T^4)]
D --> E[T = (E / σ)^{1/4}]
```

The final answer is $\boxed{218.33}$.

**Common Pitfalls**
------------------

* Not using the correct units for temperature.
* Forgetting to use the Stefan-Boltzmann constant.
* Not neglecting other modes of heat transfer.

**Quick Summary**
----------------

* Radiative heat transfer: energy transferred through electromagnetic waves
* Stefan-Boltzmann law: $E = \sigma T^4$
* Absorptivity: $\alpha = \frac{E_{abs}}{E_{inc}}$
* Emissivity: $e = \frac{E_{emitted}}{\sigma T^4}$
* Radiative heat transfer coefficient: $h_r = \frac{\sigma (T_1^4 - T_2^4)}{L}$