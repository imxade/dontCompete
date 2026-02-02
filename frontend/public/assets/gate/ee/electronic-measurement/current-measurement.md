**Current Measurement Theory Note**
=====================================

**Introduction**
---------------

Current measurement is a crucial aspect of electronic measurement, enabling us to quantify the flow of electric charge through a circuit. This note covers the theoretical concepts and formulas required for solving questions related to current measurement.

**Core Concepts**
-----------------

### Current Measurement Basics

*   **Current**: The flow of electric charge through a conductor.
*   **Resistance**: Opposition to the flow of current in a conductor.
*   **Ohm's Law**: $I = \frac{V}{R}$, where $I$ is current, $V$ is voltage, and $R$ is resistance.

### Diode Current Equation

The diode current equation is given by:

$$I_D = I_S \left( e^{\frac{V_D}{\eta V_T}} - 1 \right)$$

where $I_D$ is the diode current, $I_S$ is the reverse saturation current, $V_D$ is the voltage across the diode, $\eta$ is the ideality factor, and $V_T$ is the thermal voltage.

### Thermal Voltage

The thermal voltage is given by:

$$V_T = \frac{k_B T}{e}$$

where $k_B$ is the Boltzmann constant, $T$ is the temperature in Kelvin, and $e$ is the elementary charge.

**Key Formulas/Theorems**
-------------------------

### Diode Current Equation (Logarithmic Form)

Applying logarithms to both sides of the diode current equation gives:

$$\ln(I_D) = \frac{V_D}{\eta V_T} - 1 + \ln(I_S)$$

Differentiating partially with respect to $V_T$ yields:

$$\frac{\partial \ln(I_D)}{\partial V_T} = -\frac{V_D}{\eta V_T^2}$$

### Percentage Uncertainty in Measured Current

Given the resolution of the voltage source as $\Delta V$, the percentage uncertainty in the measured current is:

$$\frac{\Delta I}{I} \times 100\% = \left| \frac{\partial \ln(I_D)}{\partial V_T} \right| \times \frac{\Delta V}{V_T}$$

**Problem Solving Patterns**
---------------------------

### Diode Current Equation Problems

*   Identify the given parameters and the desired quantity (e.g., diode current, percentage uncertainty).
*   Apply the diode current equation in logarithmic form.
*   Differentiate partially with respect to $V_T$ as required.

### Example 1: Q42 from ee_2020_42

Given:

*   Non-ideal Si-based pn junction diode
*   Bias applied across terminals from -5 V to +5 V
*   Effective thermal voltage $\eta V_T = (29.2) \pm mV$
*   Resolution of voltage source: 1mV
*   Desired quantity: percentage uncertainty in measured current at a bias voltage of 0.02 V

Solution:

1.  Apply the diode current equation in logarithmic form:
    $$\ln(I_D) = \frac{V_D}{\eta V_T} - 1 + \ln(I_S)$$
2.  Differentiate partially with respect to $V_T$:
    $$\frac{\partial \ln(I_D)}{\partial V_T} = -\frac{V_D}{\eta V_T^2}$$
3.  Evaluate the partial derivative at the desired bias voltage ($V_D = 0.02 V$):
    $$\left| \frac{\partial \ln(I_D)}{\partial V_T} \right|_{V_D=0.02 V} = -\frac{0.02}{(29.2) \pm 10^{-3}}$$
4.  Calculate the percentage uncertainty in measured current:
    $$\frac{\Delta I}{I} \times 100\% = \left| \frac{\partial \ln(I_D)}{\partial V_T} \right|_{V_D=0.02 V} \times \frac{10^{-3}}{(29.2) \pm 10^{-3}}$$

**Common Pitfalls**
------------------

*   Failing to apply the diode current equation in logarithmic form.
*   Not differentiating partially with respect to $V_T$ as required.

**Quick Summary**
-----------------

*   Diode current equation: $I_D = I_S \left( e^{\frac{V_D}{\eta V_T}} - 1 \right)$
*   Thermal voltage: $V_T = \frac{k_B T}{e}$
*   Percentage uncertainty in measured current:
    $$\frac{\Delta I}{I} \times 100\% = \left| \frac{\partial \ln(I_D)}{\partial V_T} \right| \times \frac{\Delta V}{V_T}$$