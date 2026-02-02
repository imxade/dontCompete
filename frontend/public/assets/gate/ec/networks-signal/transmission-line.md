**Transmission Lines**
=======================

### Introduction

A transmission line is a network of two or more conductors used for carrying electrical signals between two points. It's essential to understand the behavior of these lines, especially when they are terminated with loads other than their characteristic impedance.

### Core Concepts

*   **Characteristic Impedance (Z0)**: The ratio of voltage to current in a transmission line, measured in ohms ($\Omega$). Z0 = $\sqrt{\frac{L}{C}}$, where L is the inductance and C is the capacitance per unit length.
*   **Propagation Speed**: The speed at which a signal travels through a transmission line. It's approximately equal to the speed of light (c) in free space, but it can be different in various materials.
*   **Reflection Coefficient (Γ)**: A measure of how much energy is reflected back into the line when a load impedance differs from Z0.

### Key Formulas/Theorems

*   **Transmission Line Equations**: The voltage and current at any point on a transmission line are given by:
    $$
    V(z) = V_0 \cos(\beta z + \phi)
    $$
    $$
    I(z) = I_0 \sin(\beta z + \phi)
    $$

    where $V_0$ and $I_0$ are the initial voltage and current, $\beta$ is the phase constant, and $\phi$ is the phase angle.

*   **Reflection Coefficient Formula**: 
    $$
    \Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}
    $$

### Problem Solving Patterns

1.  **Determine the Termination Impedance**: Identify whether the load impedance is greater than, less than, or equal to the characteristic impedance.
2.  **Apply Reflection Coefficient Formula**: Use the reflection coefficient formula to find the reflected voltage or current.
3.  **Calculate the Input End Impedance**: Combine the incident and reflected voltages/currents using transmission line equations.

### Examples with Solutions

**Example 1:**
Given:
*   Transmission line length (L) = $\frac{3}{4}\lambda$
*   Characteristic impedance (Z0) = $50\Omega$
*   Load impedance (ZL) = $400\Omega$

Find the input end impedance seen at the input end of the transmission line.

**Solution:**

Step 1: Determine the termination impedance.
Since ZL > Z0, it's a load greater than characteristic impedance.

Step 2: Apply Reflection Coefficient Formula:
$\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}$

$\Gamma = \frac{400 - 50}{400 + 50}$
$\Gamma ≈ 0.923$

Step 3: Calculate the Input End Impedance (Ze):
$Z_e = Z_0 \cdot \frac{1 + \Gamma}{1 - \Gamma}$

$Z_e = 50 \cdot \frac{1 + 0.923}{1 - 0.923}$
$Z_e ≈ 6.25\Omega$

**Common Pitfalls**

*   Incorrect application of reflection coefficient formula
*   Misinterpretation of termination impedance conditions
*   Failure to combine incident and reflected voltages correctly

### Quick Summary

*   Characteristic Impedance (Z0): Ratio of voltage to current in a transmission line.
*   Reflection Coefficient (Γ): Measure of energy reflected back into the line.
*   Transmission Line Equations: Voltage and current at any point on the line.
*   Determine Termination Impedance, Apply Reflection Coefficient Formula, and Calculate Input End Impedance.