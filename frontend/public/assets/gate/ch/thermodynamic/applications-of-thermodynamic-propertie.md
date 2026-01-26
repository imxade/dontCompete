**Applications of Thermodynamic Properties**
=============================================

**Introduction**
---------------

Thermodynamics is a branch of physics that deals with heat, temperature, and their relation to energy, work, and properties of matter. In this note, we will focus on the applications of thermodynamic properties, specifically entropy, in solving problems related to constant pressure.

**Core Concepts**
-----------------

### Entropy (S)

Entropy is a measure of disorder or randomness in a system. It can be thought of as a measure of the number of possible microstates in a system. The change in entropy (ΔS) is related to the heat transferred (Q) and the temperature (T):

$$\Delta S = \frac{Q}{T}$$

### Molar Heat Capacity at Constant Pressure ($C_p$)

Molar heat capacity at constant pressure is defined as the amount of heat required to raise the temperature of one mole of a substance by one degree Kelvin at constant pressure.

### Ideal Gas Law

The ideal gas law relates the pressure (P), volume (V), and temperature (T) of an ideal gas:

$$PV = nRT$$

where $n$ is the number of moles, and $R$ is the gas constant ($8.314 J/mol·K$).

**Key Formulas/Theorems**
-------------------------

### Molar Heat Capacity at Constant Pressure ($C_p$)

The molar heat capacity at constant pressure for n-pentane as a function of temperature (T) is given by:

$$\frac{dC_p}{dT} = 3.6 + \frac{45.4}{T^2} - \frac{14.1}{T^5}$$

where $T$ is in Kelvin.

**Problem Solving Patterns**
---------------------------

### Finding the Rate of Change of Molar Entropy

To find the rate of change of molar entropy (ΔS) with respect to temperature at constant pressure, we can use the following steps:

1. Find the derivative of the heat capacity at constant pressure ($C_p$) with respect to temperature (T).
2. Evaluate the derivative at the given temperature (T).
3. Use the equation $\Delta S = \frac{Q}{T}$ to find the change in entropy.

**Examples with Solutions**
-------------------------

### Example 1

Find the rate of change of molar entropy of n-pentane with respect to temperature at constant pressure at 1000 K.

## Step 1: Find the derivative of $C_p$ with respect to T
$$\frac{dC_p}{dT} = 3.6 + \frac{45.4}{T^2} - \frac{14.1}{T^5}$$

## Step 2: Evaluate the derivative at T = 1000 K
$$\frac{dC_p}{dT}(1000) = 3.6 + \frac{45.4}{10^{12}} - \frac{14.1}{10^{15}}$$

## Step 3: Simplify the expression
$$\frac{dC_p}{dT}(1000) ≈ 3.6$$

### Example 2

Find the change in entropy of n-pentane when heated from 298 K to 500 K at constant pressure.

## Step 1: Find the average heat capacity at constant pressure
Average $C_p$ = $\frac{1}{500 - 298} \int_{298}^{500} C_p dT$

## Step 2: Evaluate the integral
Average $C_p ≈ 3.6 + 45.4 × 10^{-9} K^{-1}$

## Step 3: Find the change in entropy
ΔS = Average $C_p$ × (500 - 298)

**Common Pitfalls**
------------------

* Forgetting to use the correct units for the gas constant ($R$).
* Not evaluating the derivative at the given temperature.
* Confusing $\Delta S$ with $\frac{dS}{dT}$.

**Quick Summary**
---------------

* Thermodynamics is a branch of physics that deals with heat, temperature, and their relation to energy, work, and properties of matter.
* Entropy (S) is a measure of disorder or randomness in a system.
* Molar heat capacity at constant pressure ($C_p$) is the amount of heat required to raise the temperature of one mole of a substance by one degree Kelvin at constant pressure.
* The ideal gas law relates the pressure, volume, and temperature of an ideal gas.

### Reference Diagram
```mermaid
graph LR
A[Entropy (S)] --> B[Molar Heat Capacity at Constant Pressure ($C_p$)]
C[Ideal Gas Law] --> D[Pressure (P) Volume (V), Temperature (T)]
```
Note: The above Mermaid diagram is a simple representation of the relationships between entropy, molar heat capacity, and the ideal gas law.