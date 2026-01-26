**Linear 2-Port Network Parameters**
=====================================

### Introduction
A linear 2-port network is a circuit with two terminals where each terminal can be connected to an external circuit or another port. The network parameters describe its behavior under small-signal conditions.

### Core Concepts
The most commonly used network parameters for 2-port networks are:

* **Z-parameters (Impedance Parameters)**: describe the input impedance of a 2-port network at each port.
* **Y-parameters (Admittance Parameters)**: describe the input admittance of a 2-port network at each port.
* **h-parameters (Hybrid Parameters)**: describe the input impedance and current gains of a 2-port network.

### Key Formulas/Theorems
**Z-Parameters**
----------------

$$Z_{11} = Z_1 \bigg|_{V_2=0}$$
$$Z_{12} = -\frac{\partial V_1}{\partial I_2} \bigg|_{I_1=0}$$
$$Z_{21} = \frac{\partial V_2}{\partial I_1} \bigg|_{I_2=0}$$
$$Z_{22} = Z_2 \bigg|_{V_1=0}$$

**Y-Parameters**
-----------------

$$Y_{11} = Y_1 \bigg|_{V_2=0}$$
$$Y_{12} = -\frac{\partial I_1}{\partial V_2} \bigg|_{I_2=0}$$
$$Y_{21} = \frac{\partial I_2}{\partial V_1} \bigg|_{I_1=0}$$
$$Y_{22} = Y_2 \bigg|_{V_1=0}$$

**h-Parameters**
-----------------

$$h_{11} = Z_1 + \frac{Z_2 Z_{12}}{Z_2 + Z_{22}}$$
$$h_{12} = -\frac{Z_2}{Z_2 + Z_{22}}$$
$$h_{21} = \frac{Z_2 Y_{11}}{\Delta}$$
$$h_{22} = \frac{Y_1 + Y_2 + h_{12} Y_{11}}{\Delta}$$

where $\Delta = 1 + h_{12} h_{21}$.

### Problem Solving Patterns
When solving problems involving network parameters, follow these steps:

1. Identify the type of parameter required (Z, Y, or h).
2. Write down the relevant formulas and substitute the given values.
3. Simplify and solve for the desired quantity.

**Example 1:**
Given $h_{11} = 10 \Omega$, $h_{12} = -5$, $h_{21} = 0.05 A/V$, and $h_{22} = 50 m\Omega$, find the input impedance at port 1.

### Examples with Solutions
**Example 2:**
Given a 2-port network with $Z_1 = 10 \Omega$ and $Z_2 = 20 \Omega$, find the Z-parameters using the formulas above.