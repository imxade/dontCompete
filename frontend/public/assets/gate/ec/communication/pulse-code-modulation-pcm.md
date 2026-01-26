**Pulse Code Modulation (PCM)**
==========================

### Introduction
Pulse Code Modulation (PCM) is a method of encoding analog signals into digital signals. It is widely used in communication systems, including telephony and audio transmission. PCM converts an analog signal into a series of pulses that represent the signal's amplitude at regular intervals.

### Core Concepts

* **Sampling**: The process of converting an analog signal into discrete values at regular intervals.
* **Quantization**: The process of mapping the sampled values to digital values, also known as code words.
* **Uniform Quantizer**: A quantizer that divides the range of input values into equal-sized intervals.

### Key Formulas/Theorems

The quantization error in PCM is uniformly distributed. Let $E_q$ be the quantization error and $\Delta$ be the quantization step size. Then, the signal-to-quantization-noise ratio (SQNR) is given by:

$$ SQNR = 10\log_{10}\left(\frac{\Delta^2}{2 \sigma_q^2} \right) dB $$

where $\sigma_q^2$ is the variance of the quantization error.

### Problem Solving Patterns

When solving PCM-related problems, consider the following steps:

1. **Determine the sampling rate**: The sampling rate is typically given or can be calculated using the Nyquist-Shannon sampling theorem.
2. **Calculate the number of bits per sample**: The number of bits per sample depends on the quantization step size and the desired SQNR.
3. **Calculate the transmission rate**: The transmission rate is equal to the number of bits per sample multiplied by the sampling rate.

### Examples with Solutions

**Example 1**

A message signal has a peak-to-peak value of 2 V, root mean square (RMS) value of 0.1 V, and bandwidth of 5 kHz. It is sampled at a rate of 10 kHz and fed to a PCM system that uses a uniform quantizer with 8 bits per sample.

(a) Calculate the quantization step size.
(b) Calculate the SQNR of the PCM system.

**Solution**

(a) The RMS value is given by:

$$ V_{RMS} = \frac{V_{PP}}{\sqrt{2\pi}} $$

where $V_{PP}$ is the peak-to-peak value. Therefore, $V_{RMS} = 0.1$ V.

The quantization step size $\Delta$ can be calculated using:

$$ \Delta = \frac{V_{RMS}}{2^{n/2}-1} $$

where n is the number of bits per sample (in this case, 8). Therefore,

$$ \Delta = \frac{0.1}{2^4-1} = 6.25 \times 10^{-3} V $$

(b) The SQNR can be calculated using:

$$ SQNR = 10\log_{10}\left(\frac{\Delta^2}{2 \sigma_q^2} \right) dB $$

Assuming a uniform distribution of the quantization error, we have:

$$ \sigma_q^2 = \frac{1}{12} V_{RMS}^2 = \frac{(0.1)^2}{12} = 8.33 \times 10^{-4} V^2 $$

Therefore,

$$ SQNR = 10\log_{10}\left(\frac{(6.25 \times 10^{-3})^2}{2(8.33 \times 10^{-4})} \right) dB = 30.72 dB $$

### Common Pitfalls

* Failing to calculate the correct quantization step size.
* Not using the correct formula for SQNR.

### Quick Summary

* PCM converts analog signals into digital signals using sampling and quantization.
* The quantization error is uniformly distributed, and its variance can be used to calculate the SQNR.
* The number of bits per sample depends on the desired SQNR and quantization step size.

**References**

* Wikipedia: Pulse Code Modulation
* Signals & Systems by Oppenheim & Willsky (6th ed.)