**MOSFET Characteristic**
=========================

### Introduction

A MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) is a type of transistor that uses an electric field to control the flow of current. In this note, we will focus on the characteristic of MOSFETs and how they are used in analog electronics.

### Core Concepts

A MOSFET consists of three main layers:

* **Gate**: The gate is the top layer of the MOSFET, which controls the flow of current.
* **Source**: The source is one of the bottom layers of the MOSFET, which supplies current to the drain.
* **Drain**: The drain is the other bottom layer of the MOSFET, which receives current from the source.

When a voltage is applied to the gate with respect to the source, it creates an electric field that controls the flow of current between the source and drain. If the voltage on the gate is higher than the threshold voltage (Vt), the MOSFET enters saturation mode, where the current flows freely between the source and drain.

### Key Formulas/Theorems

* **Small Signal Current Gain**:
$$\beta = \frac{g_{m}}{g_{ds}}$$
where $g_m$ is the transconductance and $g_{ds}$ is the output conductance.
For an ideal MOSFET biased in saturation, $\beta = \infty$, since there is no resistance between the gate and source.

### Problem Solving Patterns

* **Identify the operating region**: Determine whether the MOSFET is in cut-off, triode or saturation mode.
* **Use the drain-to-source current equation**: For a MOSFET in saturation mode:
$$I_{DS} = \frac{1}{2}\mu_nC_{ox}\frac{W}{L}(V_{GS}-V_t)^2$$
where $\mu_n$ is the electron mobility, $C_{ox}$ is the oxide capacitance per unit area, W is the width of the channel and L is the length of the channel.

### Examples with Solutions

**Example 1**

A MOSFET has the following parameters:

| Parameter | Value |
| --- | --- |
| $\mu_n$ | $50 cm^2/Vs$ |
| $C_{ox}$ | $10 nF/cm^2$ |
| W/L | 100:1 |
| Vt | 1V |

Calculate the drain-to-source current (I_DS) for a gate voltage of 5V.

Solution:
$$I_{DS} = \frac{1}{2}\mu_nC_{ox}\frac{W}{L}(V_{GS}-V_t)^2$$
$$I_{DS} = \frac{1}{2} \times 50 cm^2/Vs \times 10 nF/cm^2 \times 100:1 (5-1)^2$$
$$I_{DS} = 250 mA$$

**Example 2**

For an ideal MOSFET biased in saturation, the small signal current gain is infinite.

### Common Pitfalls

* **Not considering the operating region**: Make sure to identify whether the MOSFET is in cut-off, triode or saturation mode.
* **Using the wrong equation**: Use the drain-to-source current equation for a MOSFET in saturation mode.

### Quick Summary

| Concept | Formula/Equation |
| --- | --- |
| Small Signal Current Gain | $\beta = \frac{g_{m}}{g_{ds}}$ |
| Drain-to-Source Current Equation | $I_{DS} = \frac{1}{2}\mu_nC_{ox}\frac{W}{L}(V_{GS}-V_t)^2$ |

Note: The drain-to-source current equation is for a MOSFET in saturation mode.