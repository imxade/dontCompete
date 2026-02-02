**Sampling Theorem**
=====================

### Introduction

The sampling theorem, also known as the Whittaker-Kotelnikov-Shannon (WKS) sampling theorem, states that a continuous-time signal can be perfectly reconstructed from its samples if the sampling rate is greater than twice the highest frequency component of the signal. This theorem has far-reaching implications in the field of signal processing and is crucial for understanding the fundamental limits of digital signal processing.

### Core Concepts

#### Nyquist Rate

The Nyquist rate, also known as the Nyquist frequency, is the minimum sampling rate required to reconstruct a continuous-time signal from its samples without aliasing. It is given by:

$$f_s = 2 \times f_{max}$$

where $f_s$ is the sampling rate and $f_{max}$ is the highest frequency component of the signal.

#### Sampling and Reconstruction

The process of converting a continuous-time signal into discrete-time samples is called sampling, while the reverse process of reconstructing the original signal from its samples is called reconstruction. The reconstruction process can be represented mathematically as:

$$x(t) = \sum_{n=-\infty}^{\infty} x[n] \text{sinc}(t - nT_s)$$

where $x(t)$ is the continuous-time signal, $x[n]$ are the discrete-time samples, $\text{sinc}(t)$ is the sinc function, and $T_s$ is the sampling period.

### Key Formulas/Theorems

*   **Nyquist Theorem**: A continuous-time signal can be perfectly reconstructed from its samples if the sampling rate is greater than twice the highest frequency component of the signal.
*   **Sampling Period** ($T_s$): $T_s = \frac{1}{f_s}$, where $f_s$ is the sampling rate.

### Problem Solving Patterns

When dealing with sampling theorem problems, follow these steps:

1.  Identify the highest frequency component of the signal.
2.  Calculate the Nyquist rate using the formula: $f_s = 2 \times f_{max}$.
3.  Check if the given sampling rate is greater than or equal to the Nyquist rate.

### Examples with Solutions

**Example 1**

A real-valued base-band signal $x(t)$, band-limited to 10 kHz, is sampled at a rate of 20 kHz. Determine whether the signal can be perfectly reconstructed from its samples.

**Solution**

Since the sampling rate (20 kHz) is greater than twice the highest frequency component (10 kHz), the Nyquist theorem states that the signal can be perfectly reconstructed from its samples.

### Common Pitfalls

*   Failing to identify the highest frequency component of the signal.
*   Calculating the wrong Nyquist rate or sampling period.
*   Not checking if the given sampling rate is sufficient for perfect reconstruction.

### Quick Summary

*   Sampling theorem states that a continuous-time signal can be perfectly reconstructed from its samples if the sampling rate is greater than twice the highest frequency component of the signal.
*   Nyquist rate: $f_s = 2 \times f_{max}$, where $f_s$ is the sampling rate and $f_{max}$ is the highest frequency component of the signal.
*   Sampling period: $T_s = \frac{1}{f_s}$