**Resonance in Network Theory**
=============================

### Introduction

Resonance occurs when an electronic circuit oscillates at a specific frequency, resulting in maximum energy transfer between components. In network theory, resonance plays a crucial role in understanding the behavior of RLC circuits.

### Core Concepts

*   **Resonant Frequency**: The frequency at which the circuit's impedance is maximum, and current is minimum.
*   **Bandwidth**: The range of frequencies over which the circuit's impedance remains within a certain tolerance (usually 3 dB).
*   **Quality Factor (Q)**: A measure of the circuit's ability to store energy. Higher Q means higher energy storage.

### Key Formulas/Theorems

\[ f_r = \frac{1}{2\pi\sqrt{LC}} \]

where $f_r$ is the resonant frequency, $L$ is the inductance, and $C$ is the capacitance.

The bandwidth (BW) can be calculated using:

\[ BW = \frac{f_r}{Q} \]

### Problem Solving Patterns

1.  **Identify Resonant Components**: Determine which components are involved in resonance (inductor, capacitor, or both).
2.  **Calculate Resonant Frequency**: Use the formula $f_r = \frac{1}{2\pi\sqrt{LC}}$ to find the resonant frequency.
3.  **Determine Bandwidth**: Calculate the bandwidth using $BW = \frac{f_r}{Q}$.

### Examples with Solutions

**Example 1**

A circuit has a resonant frequency of 150 kHz and a bandwidth of 600 Hz. Find its Q-factor.

Solution:

\[ f_r = \frac{1}{2\pi\sqrt{LC}} \]

We know $f_r$ but not $L$ or $C$. However, we can use the formula for bandwidth to find Q:

\[ BW = \frac{f_r}{Q} \]

Rearrange to solve for Q:

\[ Q = \frac{f_r}{BW} \]

Substitute given values:

\[ Q = \frac{150000}{600} = 250 \]

### Common Pitfalls

*   Forgetting to consider the bandwidth when calculating Q.
*   Misidentifying resonant components or frequencies.

### Quick Summary

*   Resonance occurs at a specific frequency, maximizing energy transfer.
*   Bandwidth determines the range of frequencies within tolerance.
*   Quality factor (Q) measures energy storage ability.