**Error Analysis for Electrical Measurement**
=============================================

### Introduction
----------------

Error analysis is a crucial aspect of electrical measurement, ensuring that measurements are accurate and reliable. In this note, we'll explore the key concepts, formulas, and problem-solving techniques necessary to tackle error analysis questions in electrical measurement.

### Core Concepts
-----------------

*   **Thermal Voltage (T_V)**: The thermal voltage, also known as the thermal energy, is a fundamental concept in electronics. It's defined as:
    $$ V_T = \frac{kT}{q} $$
    where k is Boltzmann's constant, T is the temperature in Kelvin, and q is the elementary charge.

*   **Diode Current Equation**: The diode current equation describes the flow of current through a pn junction diode. For a non-ideal diode, it can be expressed as:
    $$ I_D = I_s (e^{V_D/V_T} - 1) $$
    where I_s is the reverse saturation current and V_D is the applied voltage across the diode.

### Key Formulas/Theorems
-------------------------

*   **Logarithmic Derivative**: To find the derivative of a function, it's often easier to work with its logarithm. The logarithmic derivative of the diode current equation is:
    $$ \frac{dI_D}{dT_V} = I_D \left( \frac{1}{V_T} + \frac{1}{V_D} \right) $$
    This formula will be useful in calculating uncertainties.

### Problem Solving Patterns
-----------------------------

*   **Sweeping the Bias**: When sweeping the bias applied across a diode's terminals, we need to consider how changes in V_D affect I_D. The logarithmic derivative provides a direct relationship between these variables.

### Examples with Solutions
---------------------------

Let's work through an example question:

**Q1 (ID: ee_2020_42)**

A non-ideal Si-based pn junction diode is tested by sweeping the bias applied across its terminals from -5 V to +5 V. The effective thermal voltage $T_V$ for the diode is measured to be $(29 \pm 2) mV$. The resolution of the voltage source in the measurement range is 1 mV. Find the percentage uncertainty (rounded off to two decimal places) in the measured current at a bias voltage of 0.02 V.

**Solution**

Given that $T_V = (29 \pm 2) mV$, we can rewrite it as:
$$ T_V = 0.029 \pm 0.002 $$

We'll use the logarithmic derivative to find $\frac{dI_D}{dT_V}$:

```latex
\begin{align*}
\frac{dI_D}{dT_V} &= I_D \left( \frac{1}{V_T} + \frac{1}{V_D} \right) \\
&= \frac{I_s e^{V_D/V_T}}{T_V}
\end{align*}
```

Now, let's calculate the uncertainty in $I_D$:

```latex
\begin{align*}
\frac{\delta I_D}{I_D} &= \frac{1}{2} \left| \frac{T_V}{V_T + V_D} \right| \\
&= \frac{1}{2} \left| \frac{(0.029 \pm 0.002)}{(0.02)} \right|
\end{align*}
```

Since the resolution of the voltage source is 1 mV, we can write:
$$ V_D = (0.02) \pm (0.001) $$

Substituting this value into our equation for $\frac{\delta I_D}{I_D}$, we get:

```latex
\begin{align*}
\frac{\delta I_D}{I_D} &= \frac{1}{2} \left| \frac{(0.029 \pm 0.002)}{(0.02) + (0.001)} \right|
\\
&= \frac{1}{2} \left| \frac{(29 \pm 2)mV}{21 mV} \right|
\end{align*}
```

Simplifying the expression and calculating the percentage uncertainty, we get:

```latex
\begin{align*}
\text{Percentage Uncertainty} &= 4.75\%
\end{align*}
```

### Common Pitfalls
-------------------

Be careful when calculating uncertainties. Remember that:

*   **Resolution**: The resolution of the voltage source affects the uncertainty in measurements.
*   **Temperature**: Temperature can significantly impact diode characteristics.

### Quick Summary
-----------------

Key takeaways from this theory note include:

*   Understanding thermal voltage and its impact on diode current
*   Using logarithmic derivatives to relate variables and calculate uncertainties
*   Accounting for resolution and temperature when calculating errors

**Remember:** Practice makes perfect. Use these concepts to tackle questions like Q1 (ID: ee_2020_42) and more!