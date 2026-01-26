# Rectifier Type Digital Meter
## Introduction
A rectifier type digital meter measures the average value of an input signal, which is essential for accurate measurements in various applications. This note covers the theoretical concepts and formulas required to understand how a rectifier type digital meter works.

## Core Concepts
A rectifier type digital meter uses a full-wave rectifier circuit to convert the AC (Alternating Current) input signal into a DC (Direct Current) output signal. The meter then measures the average value of this DC signal, which represents the RMS (Root Mean Square) value of the original AC signal.

## Key Formulas/Theorems
LaTeX:

$$V_{avg} = \frac{2}{\pi} V_m$$

where $V_{avg}$ is the average value and $V_m$ is the peak value of the AC signal.

For a full-wave rectifier circuit, the output voltage is given by:

$$V_o = |V_p| + |V_n|$$

where $V_p$ and $V_n$ are the positive and negative half-cycle voltages respectively.

## Problem Solving Patterns
When solving problems involving rectifier type digital meters, follow these steps:

1. Identify the type of input signal (AC or DC).
2. Determine whether it's a full-wave or half-wave rectifier circuit.
3. Calculate the average value using the formula $V_{avg} = \frac{2}{\pi} V_m$ for a sinusoidal waveform.

## Examples with Solutions
### Example 1:
A 3½ digit rectifier type digital meter is set to read in its 2000 V range. A symmetrical square wave of frequency 50 Hz and amplitude ±100 V is measured using the meter. What will be the reading on the meter?

Solution:

Since it's a full-wave rectifier circuit, we use the formula $V_{avg} = \frac{2}{\pi} V_m$. For a square wave with amplitude ±100 V, the peak value is 100 V.

$$V_{avg} = \frac{2}{\pi} \times 100 V = 63.66 V$$

However, since the meter reads in its 2000 V range, we need to convert this value:

$$Voltage read = 100 \times \frac{63.66}{2000} = 3.18 V$$

But wait! The correct answer is actually **100 V**.

Upon re-examining the problem, we realize that for a square wave, the average value is simply the peak value, since it's a symmetrical waveform:

$$Voltage read = 100 V$$

### Example 2:
A rectifier type digital meter measures a sinusoidal AC signal with a frequency of 50 Hz and an amplitude of 200 V. What will be the reading on the meter?

Solution:

Using the formula $V_{avg} = \frac{2}{\pi} V_m$, we get:

$$V_{avg} = \frac{2}{\pi} \times 200 V = 127.3 V$$

However, this value represents the average voltage across a half-cycle of the waveform. For a full-wave rectifier circuit, the output voltage is twice this value:

$$Voltage read = 2 \times 127.3 V = 254.6 V$$

## Common Pitfalls
* Students often forget to convert the peak value to average value when using the formula $V_{avg} = \frac{2}{\pi} V_m$.
* They may also incorrectly assume that the meter reads the peak value directly.

## Quick Summary
* Rectifier type digital meters measure the average value of an input signal.
* For full-wave rectifiers, use the formula $V_{avg} = \frac{2}{\pi} V_m$ for sinusoidal waveforms.
* For square waves, the average value is equal to the peak value.

Note: This note only covers the theoretical concepts and formulas required to solve the given source questions. It's essential to practice solving problems with different types of input signals and rectifier circuits to gain a deeper understanding of this topic.