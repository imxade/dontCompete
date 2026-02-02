**Linear 2-Port Network Parameters**
=====================================

### Introduction
-----------------

A linear 2-port network is a fundamental concept in network theory, which describes how two ports of an electrical network interact with each other. The parameters used to characterize this interaction are known as the 2-port network parameters.

### Core Concepts
------------------

#### Definition of 2-Port Network Parameters

The 2-port network parameters are defined by considering a linear 2-port network connected between two ports, `1` and `2`. The voltage at port `1` is denoted by $V_1$, the current at port `1$ by $I_1$, the voltage at port `2$ by $V_2$, and the current at port `2$ by $I_2$. These parameters can be classified into two categories: the z-parameters (impedance parameters) and the y-parameters (admittance parameters).

#### Z-Parameters

The z-parameters are defined as:

$$\begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} z_{11} & z_{12} \\ z_{21} & z_{22} \end{bmatrix}\begin{bmatrix} I_1 \\ I_2 \end{bmatrix}$$

where $z_{ij}$ is the z-parameter between ports `i` and `j`.

#### Y-Parameters

The y-parameters are defined as:

$$\begin{bmatrix} I_1 \\ I_2 \end{bmatrix} = \begin{bmatrix} y_{11} & y_{12} \\ y_{21} & y_{22} \end{bmatrix}\begin{bmatrix} V_1 \\ V_2 \end{bmatrix}$$

where $y_{ij}$ is the y-parameter between ports `i` and `j`.

### Key Formulas/Theorems
---------------------------

The z-parameters and y-parameters can be transformed into each other using the following formulas:

**Z-Parameters to Y-Parameters**

$$y_{11} = \frac{1}{z_{11}}, y_{12} = -\frac{z_{21}}{z_{11}}, y_{22} = \frac{z_{12} - z_{11}z_{22}}{z_{11}}$$

**Y-Parameters to Z-Parameters**

$$z_{11} = \frac{1}{y_{11}}, z_{12} = \frac{-y_{21}}{y_{11}}, z_{22} = \frac{y_{12}- y_{11}y_{22}}{y_{11}}$$

### Problem Solving Patterns
---------------------------

To solve problems involving 2-port network parameters, follow these steps:

1.  Identify the type of parameter required (z-parameters or y-parameters).
2.  Use the given circuit to calculate the desired parameter.
3.  Apply any necessary transformations between z-parameters and y-parameters.

### Examples with Solutions
---------------------------

**Example:**

A linear 2-port network is connected as shown in Fig. (a). An ideal DC voltage source of `10 V` is connected across Port `1`. A variable resistance `$R$` is connected across Port `2`.

![](https://example.com/network.png)

The measured voltage and current at Port `2` are shown in Fig. (b) as a `$V_2$` versus `$I_2$` plot.

![](https://example.com/plot.png)

When the variable resistance `$R$` is replaced by the load shown in Fig. (c), find the new value of `$I_2$`.

![](https://example.com/load.png)

**Solution:**

Using the z-parameters, we can write:

$$V_2 = z_{12} I_1 + z_{22} I_2$$

Given that $V_2 = 5 V$, $I_1 = 0 mA$, and $I_2 = -4 mA$, we can calculate:

$$z_{22} = \frac{V_2}{I_2} = \frac{5 V}{-4 mA} = -1250 \Omega$$

Now, when the variable resistance `$R$` is replaced by the load shown in Fig. (c), we need to find the new value of `$I_2$`.

Using the y-parameters, we can write:

$$I_1 = y_{11} V_1 + y_{12} V_2$$

Given that $V_1 = 10 V$, $V_2 = 4 V$, and $y_{12} = -\frac{z_{21}}{z_{11}}$, we can calculate:

$$I_2 = \left(\frac{-1250}{100}\right) I_1 + (-25) I_2$$

Solving for `$I_2$`, we get:

$$I_2 = 4.9 mA$$

Therefore, the answer is `4` (rounded off to one decimal place).

### Common Pitfalls
------------------

*   Always identify the type of parameter required (z-parameters or y-parameters).
*   Apply any necessary transformations between z-parameters and y-parameters.
*   Use the correct formulas and equations for the desired parameter.

### Quick Summary
-----------------

*   Linear 2-port network parameters: z-parameters, y-parameters.
*   Transformation between z-parameters and y-parameters:
    *   Z-Parameters to Y-Parameters: $\boxed{y_{11} = \frac{1}{z_{11}}, y_{12} = -\frac{z_{21}}{z_{11}}, y_{22} = \frac{z_{12}- z_{11}z_{22}}{z_{11}}}$
    *   Y-Parameters to Z-Parameters: $\boxed{z_{11} = \frac{1}{y_{11}}, z_{12} = \frac{-y_{21}}{y_{11}}, z_{22} = \frac{y_{12}- y_{11}y_{22}}{y_{11}}}$
*   Problem-solving patterns: identify the type of parameter required, apply transformations if necessary, and use the correct formulas.