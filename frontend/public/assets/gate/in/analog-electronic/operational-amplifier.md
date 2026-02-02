**Operational Amplifier (Op-Amp)**
===========================

### Introduction
---------------

The operational amplifier, commonly referred to as the Op-Amp, is a crucial component in analog electronic circuits. It plays a vital role in signal processing, amplification, and filtering. An ideal Op-Amp has infinite input impedance, zero output impedance, and infinite gain.

### Core Concepts
-----------------

*   **Inverting Amplifier**: The most common configuration of an Op-Amp is the inverting amplifier.
    *   The input voltage is applied to the inverting terminal (−) through a resistor.
    *   The output voltage is taken from the non-inverting terminal (+).
    *   The gain of the amplifier is determined by the ratio of the feedback resistor to the input resistor.

### Key Formulas/Theorems
-------------------------

LaTeX formula: $$V_{out} = -\left( \frac{R_f}{R_i} \right) V_{in}$$

where:

*   $V_{out}$ is the output voltage
*   $V_{in}$ is the input voltage
*   $R_f$ is the feedback resistor value
*   $R_i$ is the input resistor value

### Problem Solving Patterns
---------------------------

1.  **Inverting Amplifier**: Apply the formula above to find the output voltage.
2.  **Non-Inverting Amplifier**: Use a non-inverting amplifier configuration, and apply Ohm's law.

### Examples with Solutions
---------------------------

Q: Find the output voltage of an inverting amplifier with a gain of 3 and input voltage of 5 V.

```markdown
### Solution

Given:
Gain (A) = 3
Input Voltage ($V_{in}$) = 5 V

Using the formula above:

$$V_{out} = -\left( \frac{R_f}{R_i} \right) V_{in}$$

Since gain (A) = $\frac{R_f}{R_i}$, we can rewrite the equation as:

$$V_{out} = -A V_{in}$$

Substituting A = 3 and $V_{in}$ = 5 V:

$$V_{out} = -(3)(5)$$
$$V_{out} = -15 \text{ V}$$
```

### Common Pitfalls
------------------

1.  **Incorrect Assumptions**: Make sure to identify the type of amplifier (inverting or non-inverting).
2.  **Wrong Resistor Values**: Verify that the resistor values are correctly identified and applied.

### Quick Summary
---------------

*   Ideal Op-Amp properties: infinite input impedance, zero output impedance, infinite gain.
*   Inverting Amplifier formula: $V_{out} = -\left( \frac{R_f}{R_i} \right) V_{in}$.
*   Non-Inverting Amplifier configuration and application of Ohm's law.

This comprehensive theory note covers the fundamental concepts of operational amplifiers, including inverting amplifier configurations, key formulas, problem-solving patterns, examples with solutions, and common pitfalls to avoid.