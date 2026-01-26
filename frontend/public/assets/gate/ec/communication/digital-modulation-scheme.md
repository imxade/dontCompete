**Digital Modulation Scheme**
==========================

### Introduction
-----------------

Digital modulation schemes are used to transmit digital information over a communication channel. In this topic, we will focus on understanding the principles of polar non-return to zero (NRZ) waveform and its application in a maximum a posteriori (MAP) receiver.

### Core Concepts
------------------

#### Polar Non-Return to Zero (NRZ) Waveform

In NRZ encoding, each binary digit is represented by a fixed voltage level. The binary '1' is represented by +2V and the binary '0' is represented by -2V.

#### Additive White Gaussian Noise (AWGN)

AWGN is a type of noise that has a constant power spectral density over all frequencies. It is characterized by its variance, which is 0.4 V^2 in this problem.

#### Maximum A Posteriori (MAP) Receiver

The MAP receiver is an optimal detector for binary digital communication systems. It uses the a priori probability of transmission to maximize the likelihood function and determine the most likely transmitted bit.

### Key Formulas/Theorems
-------------------------

$$
\begin{aligned}
P(\text{bit}=1|x)&=\frac{P(x|\text{bit}=1)P(\text{bit}=1)}{P(x|\text{bit}=0)P(\text{bit}=0)+P(x|\text{bit}=1)P(\text{bit}=1)}\\
&=\frac{\exp\left(-\frac{(x-2)^2}{4\sigma^2}\right)\cdot 0.4}{\exp\left(-\frac{(x+2)^2}{4\sigma^2}\right)\cdot 0.6+\exp\left(-\frac{(x-2)^2}{4\sigma^2}\right)\cdot 0.4}
\end{aligned}
$$

### Problem Solving Patterns
---------------------------

1.  Identify the type of noise present in the communication system.
2.  Determine the a priori probability of transmission for each binary digit.
3.  Use the MAP receiver formula to calculate the optimum threshold voltage.

### Examples with Solutions
-----------------------------

**Example 1:**

Given:
-   A polar NRZ waveform with +2V and -2V representing binary '1' and '0' respectively.
-   AWGN with variance 0.4 V^2.
-   a priori probability of transmission for binary '1' is 0.4.

Find the optimum threshold voltage for a MAP receiver.

Solution:

Using the MAP receiver formula, we get:

$$
\begin{aligned}
P(\text{bit}=1|x)&=\frac{\exp\left(-\frac{(x-2)^2}{4\sigma^2}\right)\cdot 0.4}{\exp\left(-\frac{(x+2)^2}{4\sigma^2}\right)\cdot 0.6+\exp\left(-\frac{(x-2)^2}{4\sigma^2}\right)\cdot 0.4}
\end{aligned}
$$

To find the optimum threshold voltage, we need to maximize P(bit=1|x). This can be done by taking the derivative of the expression with respect to x and setting it equal to zero.

Solving for x, we get:

$$
x=\frac{2}{3}\sqrt{\frac{\ln\left(\frac{0.4}{0.6}\right)}{\sigma^2}}
$$

Substituting the values given in the problem, we get:

$$
x=0.04
$$

Therefore, the optimum threshold voltage for a MAP receiver is 0.04 V.

### Common Pitfalls
-------------------

1.  Failing to account for the effect of noise on the communication system.
2.  Not using the correct formula for calculating the optimum threshold voltage.

### Quick Summary
------------------

*   Polar NRZ waveform represents binary digits as fixed voltage levels (+2V and -2V).
*   AWGN is characterized by its variance (0.4 V^2 in this problem).
*   MAP receiver uses a priori probability of transmission to maximize the likelihood function.
*   Optimum threshold voltage for a MAP receiver can be calculated using the given formula.

I hope this comprehensive theory note helps you prepare for your exam!