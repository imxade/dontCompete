**Op Amp Circuit**
====================

**Introduction**
---------------

An operational amplifier (op-amp) is a high-gain electronic circuit that uses one or more feedback mechanisms to control its output voltage. In this note, we'll cover the key concepts and formulas for op amp circuits with an emphasis on theory and problem-solving techniques.

**Core Concepts**
----------------

### Ideal Op Amp Assumptions

* The op-amp has infinite input resistance.
* The op-amp has zero output resistance.
* The op-amp has infinite gain (ideally).
* The op-amp is inverting or non-inverting.

### Feedback Mechanisms

* **Positive Feedback**: increasing the output increases the input.
* **Negative Feedback**: decreasing the output decreases the input.

**Key Formulas/Theorems**
-------------------------

The **voltage gain** of an inverting amplifier is given by:

$$A_V = -\frac{R_f}{R_i}$$

where $R_f$ is the feedback resistor and $R_i$ is the input resistor.

For a non-inverting amplifier, the voltage gain is:

$$A_V = 1 + \frac{R_f}{R_i}$$

**Problem Solving Patterns**
---------------------------

### Non-Inverting Schmitt Trigger (NIST)

In this circuit, we have a positive feedback loop that causes the output to switch between two states when the input crosses a certain threshold.

**Example:**

Suppose we have an NIST with $R_1 = R_2 = 1k\Omega$ and a sine wave input of amplitude 1V. What is the output voltage?

```mermaid
graph LR
A[Input (sinusoidal)] --> B[Non-Inverting Schmitt Trigger]
B --> C[Output (switching between +5V and -5V)]
```

### Solution:

We can assume that when $V_{NI} > 0$, the output is at its maximum value of $+5V$. Using the voltage gain formula, we get:

$$\frac{V_o}{V_i} = 1 + \frac{R_f}{R_i} = 1 + \frac{1k\Omega}{1k\Omega} = 2$$

Therefore, $V_o = 2V_i$. Since the input is a sine wave of amplitude 1V, we have:

$$V_o = 2(1V) = 2V$$

So, the output voltage is a non-inverted sine wave with an amplitude of 2V.

**Common Pitfalls**
------------------

* Failing to account for the effects of positive feedback.
* Not using the correct formula for the desired op-amp configuration (inverting or non-inverting).
* Assuming the op-amp has finite gain or resistance.

**Quick Summary**
-----------------

* Ideal op amp assumptions: infinite input resistance, zero output resistance, and infinite gain.
* Feedback mechanisms: positive and negative feedback.
* Key formulas:
	+ Inverting amplifier: $A_V = -\frac{R_f}{R_i}$
	+ Non-inverting amplifier: $A_V = 1 + \frac{R_f}{R_i}$