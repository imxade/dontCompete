**Power Measurement**
======================

### Introduction

Power measurement is a crucial aspect of electrical engineering, involving the quantification of the rate at which electrical energy is transferred by an electrical circuit. This topic is essential for engineers to understand and measure power consumption in various systems.

### Core Concepts

*   **Power**: The rate at which electrical energy is transferred by an electric circuit. It is measured in watts (W).
*   **Voltage** ($V$): The potential difference between two points in a circuit, measured in volts (V).
*   **Current** ($I$): The flow of electrons through a conductor, measured in amperes (A).
*   **Power Factor** ($PF$): The ratio of real power to apparent power, measured in decimal form.

### Key Formulas/Theorems

1.  **Wattmeter Formula**: $P = V \times I \times \cos\phi$
    *   Where:
        *   $P$: Power (in watts)
        *   $V$: Voltage (in volts)
        *   $I$: Current (in amperes)
        *   $\phi$: Power factor angle
2.  **Power Factor Formula**: $\cos\phi = \frac{P}{VI}$

### Problem Solving Patterns

1.  **Wattmeter Reading Interpretation**:
    *   Identify the type of wattmeter used (e.g., LPF, moving iron).
    *   Determine the maximum power factor for a given load.
2.  **Power Factor Angle Calculation**:
    *   Use trigonometry to calculate $\cos\phi$ from the given values.

### Examples with Solutions

**Example 1**

A 300 V, 5 A LPF wattmeter has a full scale of 300 W. Determine the maximum power factor for loads supplied by 300 V AC mains.

## Step 1: Identify the type of wattmeter and its rating
The wattmeter is an LPF (Low-Power Factor) type with a full-scale rating of 300 W.

## Step 2: Calculate the apparent power
Apparent power = $VI$ = 300 V \* 5 A = 1500 VA

## Step 3: Determine the maximum power factor
Maximum power factor, $\cos\phi_{max} = \frac{P}{VI}$ = $\frac{300 W}{1500 VA}$ = 0.2 (rounded off to one decimal place)

The final answer is: $\boxed{0.2}$

### Common Pitfalls

*   Failing to identify the type of wattmeter and its rating.
*   Not calculating apparent power correctly.
*   Not using the correct formula for maximum power factor.

### Quick Summary

*   Power measurement involves quantifying electrical energy transfer rate.
*   Wattmeter formula: $P = V \times I \times \cos\phi$.
*   Power factor angle calculation: $\cos\phi = \frac{P}{VI}$.
*   Maximum power factor depends on the type of wattmeter and load characteristics.

By mastering these concepts, formulas, and problem-solving patterns, you'll be well-prepared to tackle GATE CS exam questions related to power measurement.