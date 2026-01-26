Operational Amplifiers and Feedback Amplifier
==============================================

### Introduction

An operational amplifier (op-amp) is a high-gain electronic voltage amplifier with differential inputs and, typically, a single-ended output. It's a crucial component in analog electronics and is widely used in various applications due to its ability to amplify weak signals.

In this note, we'll cover the fundamental concepts of op-amps, their behavior as non-ideal devices, and feedback amplifiers.

### Core Concepts

#### Operational Amplifier (Op-Amp)

An op-amp consists of two input terminals: `in+` and `in-`, which are connected to a high-gain amplifier. The output terminal, `out`, is typically single-ended.

**Ideal Op-Amp Assumptions**

For simplicity, we assume the op-amp is ideal:

* Infinite gain
* Zero input offset voltage
* Infinite bandwidth
* Zero output resistance

#### Non-Ideal Op-Amp Behavior

In reality, op-amps are non-ideal. The finite gain, non-zero input offset voltage, and limited bandwidth lead to errors in circuit operation.

**Open-Loop Gain**

The open-loop gain of an op-amp is the ratio of the output voltage to the input voltage when no feedback is applied:

$$A_{OL} = \frac{V_{out}}{V_{in}}$$

#### Feedback Amplifier

Feedback amplifiers use a portion of the output signal as an input, which allows for more precise control over the system. The feedback factor, β, represents the ratio of the feedback voltage to the input voltage:

$$\beta = \frac{V_f}{V_i}$$

where $V_f$ is the feedback voltage and $V_i$ is the input voltage.

**Closed-Loop Gain**

The closed-loop gain of a feedback amplifier is given by:

$$A_{CL} = \frac{A_{OL}}{1 + A_{OL}\beta}$$

### Key Formulas/Theorems

* Open-loop gain: $A_{OL}$
* Feedback factor: $\beta = \frac{V_f}{V_i}$
* Closed-loop gain: $A_{CL} = \frac{A_{OL}}{1 + A_{OL}\beta}$

### Problem Solving Patterns

1. Identify the type of op-amp circuit (non-inverting, inverting, or differential).
2. Calculate the open-loop gain ($A_{OL}$) and feedback factor ($\beta$).
3. Use the closed-loop gain formula to determine the overall system gain.

### Examples with Solutions

**Example 1:**

An op-amp has an open-loop gain of $1000$ and a feedback factor of $\frac{1}{2}$. Calculate the closed-loop gain:

$$A_{CL} = \frac{A_{OL}}{1 + A_{OL}\beta} = \frac{1000}{1 + 1000\cdot\frac{1}{2}} = \frac{1000}{1 + 500} = \frac{1000}{501} \approx 1.99$$

**Example 2:**

Given a circuit with an op-amp having an open-loop gain of $10^4$ and a feedback factor of $\frac{1}{5}$, determine the closed-loop gain:

$$A_{CL} = \frac{A_{OL}}{1 + A_{OL}\beta} = \frac{10^4}{1 + 10^4\cdot\frac{1}{5}} = \frac{10^4}{1 + 2000} = \frac{10^4}{2001} \approx 4.99$$

### Common Pitfalls

* Failing to account for the non-ideal behavior of op-amps
* Incorrectly calculating feedback factor or open-loop gain
* Not considering the effects of circuit limitations (e.g., limited bandwidth)

### Quick Summary

* Op-amp basics: differential inputs, single-ended output, high-gain amplifier
* Non-ideal op-amp behavior: finite gain, non-zero input offset voltage, limited bandwidth
* Feedback amplifiers: feedback factor ($\beta$), closed-loop gain ($A_{CL}$)
* Key formulas:
	+ Open-loop gain: $A_{OL}$
	+ Feedback factor: $\beta = \frac{V_f}{V_i}$
	+ Closed-loop gain: $A_{CL} = \frac{A_{OL}}{1 + A_{OL}\beta}$