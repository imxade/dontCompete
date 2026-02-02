**Op Amp: Theory and Applications**
=====================================

**Introduction**
---------------

An operational amplifier (op-amp) is a fundamental building block in analog electronics, used for signal conditioning, amplification, and processing. The op-amp is a high-gain electronic voltage amplifier with a differential input and a single-ended output.

**Core Concepts**
-----------------

### Ideal Op-Amp Characteristics

*   Infinite input impedance
*   Zero output impedance
*   Infinite open-loop gain (A\~)
*   Infinite bandwidth

### Non-Ideal Op-Amp Characteristics

*   Finite open-loop gain
*   Input bias current and offset voltage
*   Finite common-mode rejection ratio (CMRR)

**Key Formulas/Theorems**
-------------------------

### Voltage Gain of an Inverting Amplifier

$$V_o = -\frac{R_f}{R_i} \times V_{in}$$

### Non-Inverting Amplifier Voltage Gain

$$V_o = \left( 1 + \frac{R_f}{R_g} \right) \times V_{in}$$

**Problem Solving Patterns**
---------------------------

### Identifying Op-Amp Types

*   Inverting amplifier: Input is connected to the inverting input, and output is taken from the output terminal.
*   Non-inverting amplifier: Input is connected to the non-inverting input, and output is taken from the output terminal.

**Examples with Solutions**
---------------------------

### Example 1: Inverting Amplifier

Given:

*   $R_i = 10k\Omega$
*   $R_f = 5k\Omega$
*   $V_{in} = 2V$

Find the output voltage, $V_o$.

$$V_o = -\frac{R_f}{R_i} \times V_{in}$$

$$V_o = -\frac{5k\Omega}{10k\Omega} \times 2V$$

$$V_o = -0.5V$$

### Example 2: Non-Inverting Amplifier

Given:

*   $R_g = 20k\Omega$
*   $R_f = 10k\Omega$
*   $V_{in} = 4V$

Find the output voltage, $V_o$.

$$V_o = \left( 1 + \frac{R_f}{R_g} \right) \times V_{in}$$

$$V_o = \left( 1 + \frac{10k\Omega}{20k\Omega} \right) \times 4V$$

$$V_o = 6V$$

**Common Pitfalls**
-------------------

*   Incorrectly assuming an ideal op-amp
*   Misidentifying the type of amplifier (inverting vs. non-inverting)
*   Failing to consider input bias current and offset voltage effects

**Quick Summary**
------------------

*   Op-amps have infinite input impedance, zero output impedance, and infinite open-loop gain.
*   Non-ideal op-amp characteristics include finite open-loop gain, input bias current, and offset voltage.
*   Inverting amplifiers have a negative voltage gain, while non-inverting amplifiers have a positive voltage gain.

**References**

*   [1] Analog Devices. (2022). Operational Amplifiers.
*   [2] Texas Instruments. (2022). Op-Amps and Comparators.

Note: This note is based on the provided source questions and may require additional details or explanations to cover all relevant concepts in analog electronics.