**Linear 2-Port Network**
========================

### Introduction

A linear 2-port network is a fundamental concept in network theory, describing how electrical energy can be transferred between two ports. It is crucial to understand these networks to analyze and design various electronic circuits.

### Core Concepts

#### Definition of Linear 2-Port Network

A linear 2-port network is defined as a system with two ports, where each port has two terminals. The relationship between the voltage and current at one port can be described by the following equation:

$$V_1 = R_{11} I_1 + R_{12} I_2$$
$$I_1 = Y_{11} V_1 + Y_{12} V_2$$

where $R_{11}$, $R_{12}$ are the forward and reverse resistance parameters, and $Y_{11}$, $Y_{12}$ are the forward and reverse admittance parameters.

#### Scattering Parameters (S-Parameters)

Scattering parameters, also known as S-parameters, are a set of parameters used to describe the behavior of a 2-port network. They are defined as follows:

$$S_{11} = \frac{V_1}{I_1}\bigg|_{I_2=0}$$
$$S_{12} = \frac{V_1}{I_2}\bigg|_{I_1=0}$$

#### Example (Q1)

In the given problem, we have a linear 2-port network with an ideal DC voltage source of 10 V connected across Port 1. A variable resistance $R$ is connected across Port 2.

To solve this problem, we need to analyze the behavior of the network and find the current at Port 2 when the load shown in Fig. (c) is replaced by the variable resistance $R$.

### Key Formulas/Theorems

LaTeX formulas will be used for math notation.

#### Scattering Parameters

$$S_{11} = \frac{V_1}{I_1}\bigg|_{I_2=0}$$
$$S_{12} = \frac{V_1}{I_2}\bigg|_{I_1=0}$$

### Problem Solving Patterns

When solving problems involving linear 2-port networks, the following steps can be followed:

1. **Identify the network parameters**: Determine the forward and reverse resistance/admittance parameters.
2. **Analyze the behavior of the network**: Use scattering parameters or other methods to analyze the behavior of the network.
3. **Solve for the desired quantity**: Find the current at Port 2, voltage across a component, etc.

### Examples with Solutions

#### Example 1 (Q1)

Given:

*   Linear 2-port network with an ideal DC voltage source of 10 V connected across Port 1
*   Variable resistance $R$ connected across Port 2
*   Measured voltage and current at Port 2 shown in Fig. (b) as a 2V versus I-plot

Find the current at Port 2 when the variable resistance $R$ is replaced by the load shown in Fig. (c).

Solution:

From the given data, we can find the values of $S_{11}$ and $S_{12}$. Using these values, we can determine the current at Port 2.

$$V_1 = 10\, \text{V}$$
$$I_1 = 0\,\text{mA}\quad I_2=-4\,\text{mA}$$

$$S_{11} = \frac{V_1}{I_1}\bigg|_{I_2=0}=\infty\quad S_{12} = \frac{V_1}{I_2}\bigg|_{I_1=0}= 5\,\Omega$$

Now, using the scattering parameters, we can find the current at Port 2:

$$S_{21}=\frac{I_2}{V_1}\bigg|_{I_1=0}=-\frac{4}{10}=-0.4$$
$$I_2 = S_{21} V_1 = -0.4 \times 10 = -4\, \text{mA}$$

When the variable resistance $R$ is replaced by the load shown in Fig. (c), we can find the current at Port 2 using the same method:

$$I_2= S_{21} V_1=-0.4\times10 =-4\,\text{mA}$$

Therefore, the correct answer is **-4**.

### Common Pitfalls

*   Not identifying the network parameters correctly.
*   Not analyzing the behavior of the network properly.
*   Not using the correct formulas or theorems to solve the problem.

### Quick Summary

*   Linear 2-port networks are defined by their forward and reverse resistance/admittance parameters.
*   Scattering parameters (S-parameters) can be used to analyze the behavior of these networks.
*   When solving problems, identify the network parameters, analyze the behavior of the network, and solve for the desired quantity.

This comprehensive theory note covers all theoretical concepts, formulas, and insights required to solve the questions below and similar future questions. It is designed to provide a high-yield study material for students preparing for the GATE CS exam.