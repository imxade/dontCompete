**Op Amp Circuit Theory Note**
==========================

### Introduction
---------------

The Op-Amp (Operational Amplifier) circuit is a fundamental component in electronic circuits, used for signal processing and amplification. In this note, we will cover the basics of op-amp circuits, focusing on the non-inverting Schmitt trigger, which is the topic of the provided source question.

### Core Concepts
-----------------

#### Ideal Op-Amp

* An ideal op-amp has infinite input impedance, zero output impedance, and infinite gain.
* It can be represented by the symbol $\boxed{\text{OP}}$.
* The op-amp has two inputs: inverting ($-$) and non-inverting ($+$).

#### Feedback
---------

Feedback is a crucial concept in op-amp circuits. There are two types:

1. **Positive feedback**: The output is connected to the input, but with opposite polarity.
2. **Negative feedback**: The output is connected to the input, with the same polarity.

### Key Formulas/Theorems
---------------------------

#### Inverting Amplifier

The inverting amplifier is a basic op-amp circuit that amplifies the input signal by a factor of $-R_f/R_i$.

$$V_o = -\frac{R_f}{R_i} V_i \tag{1}$$

where $V_o$ is the output voltage, $V_i$ is the input voltage, $R_f$ is the feedback resistor, and $R_i$ is the input resistor.

#### Non-Inverting Amplifier

The non-inverting amplifier amplifies the input signal by a factor of $(1 + R_2/R_1)$.

$$V_o = (1 + \frac{R_2}{R_1}) V_i \tag{2}$$

where $V_o$ is the output voltage, $V_i$ is the input voltage, and $R_1$ and $R_2$ are resistors connected to the non-inverting input.

### Problem Solving Patterns
---------------------------

When solving op-amp circuit problems, follow these steps:

1. Identify the type of op-amp circuit (inverting, non-inverting, or Schmitt trigger).
2. Determine the feedback configuration (positive or negative).
3. Calculate the output voltage using the relevant formula.
4. Consider the saturation limits of the op-amp.

### Examples with Solutions
---------------------------

**Example 1: Inverting Amplifier**

Given:

* Input resistor $R_i = 1 k\Omega$
* Feedback resistor $R_f = 10 k\Omega$
* Input voltage $V_i = 2 V$

Find the output voltage $V_o$.

Solution:
Using Equation (1), we get

$$V_o = -\frac{R_f}{R_i} V_i = -\frac{10k\Omega}{1k\Omega} \times 2V = -20 V$$

**Example 2: Non-Inverting Amplifier**

Given:

* Input resistor $R_1 = 2 k\Omega$
* Feedback resistor $R_2 = 4 k\Omega$
* Input voltage $V_i = 3 V$

Find the output voltage $V_o$.

Solution:
Using Equation (2), we get

$$V_o = (1 + \frac{R_2}{R_1}) V_i = (1 + \frac{4k\Omega}{2k\Omega}) \times 3V = 9 V$$

### Common Pitfalls
------------------

* Failing to identify the type of op-amp circuit.
* Incorrectly applying feedback configurations.
* Overlooking saturation limits.

### Quick Summary
-----------------

* Op-amp circuits can be classified into inverting, non-inverting, and Schmitt trigger types.
* Feedback configurations determine the circuit's behavior (positive or negative).
* Use the relevant formulas to calculate output voltages.
* Consider saturation limits for op-amp outputs.

This comprehensive theory note covers the essential concepts of op-amp circuits, focusing on the non-inverting Schmitt trigger. By following this guide, students should be well-prepared to tackle similar questions and problems in future exams.