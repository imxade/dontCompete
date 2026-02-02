# Common Source Amplifier
## Introduction
The common-source amplifier is a type of electronic amplifier that uses a field-effect transistor (FET) as its active device. It is commonly used in audio and radio-frequency applications due to its high input impedance, low noise, and ability to handle large signal swings.

## Core Concepts
### Transconductance (g_m)
Transconductance is the ratio of change in drain current (I_D) to change in gate voltage (V_G). Mathematically, it can be represented as:

$$g_m = \frac{\partial I_D}{\partial V_G}$$

In the context of a common-source amplifier, transconductance is an important parameter that determines the gain and input impedance of the circuit.

### Drain Resistance (R_D)
Drain resistance is the resistance connected in series with the drain of the FET. It plays a crucial role in determining the voltage gain and stability of the common-source amplifier.

## Key Formulas/Theorems
The voltage gain of a common-source amplifier can be calculated using the following formula:

$$A_v = - \frac{g_m R_D}{1 + g_m R_D}$$

where $g_m$ is the transconductance, and $R_D$ is the drain resistance.

## Problem Solving Patterns
When solving problems related to common-source amplifiers, follow these steps:

1. Identify the type of amplifier (common-source) and its key parameters (transconductance, drain resistance).
2. Use the formula for voltage gain ($A_v = - \frac{g_m R_D}{1 + g_m R_D}$) to calculate the desired value.
3. Check your units and ensure they match the expected output.

## Examples with Solutions
### Example 1: Given a common-source amplifier with $g_m = 520 A/V\mu$ and $R_D = 4.7 k\Omega$, find its voltage gain if the power supply is 10 V.
```mermaid
graph LR
A[Given values] --> B[Calculate voltage gain]
B --> C[V_Gain = - \frac{g_m R_D}{1 + g_m R_D}]
```

Using the formula for voltage gain, we get:

$$V_{Gain} = - \frac{(520 A/V\mu) (4.7 k\Omega)}{1 + (520 A/V\mu) (4.7 k\Omega)}$$

Simplifying and evaluating the expression yields:

$$V_{Gain} = - 2.44$$

### Example 2: Given a polynomial $ax^3 + bx^2 + cx + d$, find its degree over real coefficients.

## Common Pitfalls
* Failing to use the correct formula for voltage gain.
* Misinterpreting the units of transconductance and drain resistance.
* Not considering the effect of power supply on the amplifier's operation.

## Quick Summary

* Transconductance (g_m) is the ratio of change in drain current to change in gate voltage.
* Drain resistance (R_D) affects the voltage gain and stability of the common-source amplifier.
* Voltage gain can be calculated using the formula $A_v = - \frac{g_m R_D}{1 + g_m R_D}$.
* Ensure correct units and calculation of values.