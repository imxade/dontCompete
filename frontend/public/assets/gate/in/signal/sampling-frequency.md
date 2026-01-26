**Sampling Frequency**
=======================

### Introduction
The sampling frequency, also known as the Nyquist rate, is a fundamental concept in signal processing that determines the minimum rate at which samples of a continuous-time signal can be taken to accurately reconstruct the original signal. This note will cover the theoretical concepts and formulas required to solve questions related to sampling frequency.

### Core Concepts

#### Sampling Theorem
The sampling theorem states that if a continuous-time signal $x(t)$ is band-limited to $\frac{f_s}{2}$, where $f_s$ is the sampling frequency, then the original signal can be perfectly reconstructed from its samples using an ideal low-pass filter. Mathematically, this can be represented as:

$$\mathrm{Sampling\ Theorem:}\quad x(t) = \sum_{n=-\infty}^{\infty}x[n]\mathrm{sinc}\left(\frac{t-nT_s}{T_s}\right),$$

where $\mathrm{sinc}(x) = \frac{\sin(\pi x)}{\pi x}$ and $T_s$ is the sampling period.

#### Nyquist Frequency
The Nyquist frequency, denoted by $f_N$, is half of the sampling frequency:

$$\mathrm{Nyquist\ Frequency:}\quad f_N = \frac{f_s}{2}.$$

### Key Formulas/Theorems

**Sampling Period and Frequency**

*   Sampling period: $T_s = \frac{1}{f_s}$
*   Sampling frequency: $f_s = \frac{1}{T_s}$

**Nyquist Frequency**

*   Nyquist frequency: $f_N = \frac{f_s}{2}$

### Problem Solving Patterns

When solving questions related to sampling frequency, consider the following patterns:

*   **Band-limited signals**: Determine if the signal is band-limited and identify the maximum frequency component.
*   **Sampling rate**: Calculate the minimum required sampling rate based on the Nyquist criterion.
*   **Reconstruction**: Understand that perfect reconstruction is possible only when the sampling rate is greater than or equal to twice the highest frequency component.

### Examples with Solutions

**Example 1:**

Find the minimum required sampling frequency for a signal $x(t) = \sin(200\pi t)$.

## Step 1: Determine if the signal is band-limited
The signal $x(t) = \sin(200\pi t)$ has a highest frequency component of 100 Hz.

## Step 2: Calculate the minimum required sampling rate
Apply the Nyquist criterion to determine that the minimum sampling rate should be at least twice the highest frequency component, which is 200 Hz.

**Answer:** The minimum required sampling frequency is 400 Hz (rounded off to the nearest integer).

### Common Pitfalls

*   **Insufficient sampling**: Failing to account for all frequency components of a signal can lead to aliasing and inaccurate reconstruction.
*   **Inadequate Nyquist rate**: Not considering the Nyquist criterion when determining the minimum required sampling rate.

### Quick Summary
*   Sampling theorem: Band-limited signals can be perfectly reconstructed from samples taken at a rate greater than twice the highest frequency component.
*   Nyquist frequency: Half of the sampling frequency, denoted as $f_N = \frac{f_s}{2}$.
*   Minimum required sampling rate: At least twice the highest frequency component.

This comprehensive theory note covers all theoretical concepts and formulas related to sampling frequency, ensuring that students are well-prepared for similar questions in future exams.