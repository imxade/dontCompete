**Network Analysis and Design**
===========================

**Introduction**
---------------

Network analysis and design is a crucial aspect of electrical engineering, enabling us to understand and optimize the performance of complex networks. This topic covers fundamental concepts, formulas, and problem-solving patterns required for network theory.

**Core Concepts**
-----------------

### 1. Network Resonance

*   A resonant circuit is an LC (inductor-capacitor) circuit that exhibits maximum impedance at a specific frequency called the resonant frequency.
*   The resonant frequency is given by:

$$f_r = \frac{1}{2\pi\sqrt{LC}}$$

### 2. Quality Factor (Q-Factor)

*   The Q-factor of an LC circuit is a measure of its energy storage capability and dissipation rate.

**Key Formulas/Theorems**
------------------------

### 1. Resonant Frequency

$$f_r = \frac{1}{2\pi\sqrt{LC}}$$

### 2. Bandwidth

$$BW = \frac{\Delta f}{Q}$$

where $\Delta f$ is the frequency range over which the circuit's behavior changes significantly.

### 3. Q-Factor

$$Q = \frac{f_r}{BW}$$

**Problem Solving Patterns**
---------------------------

### 1. Identifying Resonance and Bandwidth

*   Recognize that the network has a resonant frequency $f_r$ and bandwidth $BW$.
*   Use the given values to calculate the Q-factor using the formula: $Q = \frac{f_r}{BW}$.

**Examples with Solutions**
---------------------------

### 1. Example 1:

Given a network with a resonant frequency of 150 kHz and a bandwidth of 600 Hz, find its Q-factor.

```python
import math

# Given values
fr = 150e3  # Resonant frequency in Hz
BW = 600     # Bandwidth in Hz

# Calculate Q-factor
Q = fr / BW
print(Q)
```

### Solution:

The Q-factor is calculated using the formula $Q = \frac{f_r}{BW}$. Substituting the given values yields: $Q = \frac{150e3}{600} ≈ 250$.

**Common Pitfalls**
-------------------

*   **Rounding errors**: When working with large numbers, be cautious of rounding errors during calculations.
*   **Significant figures**: Ensure that the calculated Q-factor has sufficient significant figures for the given precision.
*   **Incorrect units**: Verify that all values are in compatible units (e.g., Hz for frequency).

**Quick Summary**
----------------

*   Resonant frequency: $f_r = \frac{1}{2\pi\sqrt{LC}}$
*   Bandwidth: $BW = \frac{\Delta f}{Q}$
*   Q-factor: $Q = \frac{f_r}{BW}$