**Pulse Code Modulation (PCM) Theory Note**
======================================

**Introduction**
---------------

Pulse Code Modulation (PCM) is a digital modulation technique used to convert an analog signal into a digital signal. It involves sampling the analog signal at regular intervals, quantizing the samples into a finite number of levels, and representing each level as a binary code.

**Core Concepts**
-----------------

### Sampling Theorem

The Nyquist-Shannon sampling theorem states that a continuous-time signal can be perfectly reconstructed from its samples if the sampling rate is greater than twice the bandwidth of the signal. Mathematically, this is represented by:

$$f_s > 2B_w$$

where $f_s$ is the sampling frequency and $B_w$ is the bandwidth of the signal.

### Quantization

Quantization is the process of converting an analog signal into a digital signal by dividing it into discrete levels. The number of levels, or resolution, determines the accuracy of the quantized signal. In PCM, each sample is represented as a binary code that corresponds to one of the possible levels.

**Key Formulas/Theorems**
-------------------------

### Sampling Frequency

The sampling frequency $f_s$ must be greater than twice the bandwidth of the signal:

$$f_s > 2B_w$$

### Bit Rate

The bit rate of PCM is given by:

$$b_s = n \times f_s \log_2(L)$$

where $n$ is the number of bits per sample, $f_s$ is the sampling frequency, and $L$ is the number of possible levels.

**Problem Solving Patterns**
---------------------------

1.  **Identify Sampling Rate**: Determine the minimum sampling rate required for the signal based on its bandwidth.
2.  **Determine Quantization Levels**: Calculate the number of quantization levels (L) given the desired resolution (n bits).
3.  **Calculate Bit Rate**: Use the formula $b_s = n \times f_s \log_2(L)$ to calculate the bit rate.

**Examples with Solutions**
-------------------------

### Example 1

A signal has a bandwidth of 5 MHz and is sampled at a rate 50% above the Nyquist rate. The signal is quantized into 256 levels. Calculate the binary pulse rate in Mbits per second.

#### Step 1: Identify Sampling Rate
The Nyquist rate is $2 \times 5 = 10$ MHz. Since the sampling rate is 50% above the Nyquist rate, the sampling frequency is:

$$f_s = 1.5 \times 10 = 15\text{ MHz}$$

#### Step 2: Determine Quantization Levels
The number of quantization levels (L) is given by $2^n$, where n is the number of bits per sample.

$$256 = 2^n \Rightarrow n = 8$$

#### Step 3: Calculate Bit Rate
Using the formula for bit rate:

$$b_s = n \times f_s \log_2(L) = 8 \times 15 \log_2(256) = 120\text{ Mbits per second}$$

### Example 2

A signal has a bandwidth of 3 MHz and is sampled at a rate twice the Nyquist rate. The signal is quantized into 1024 levels. Calculate the binary pulse rate in Mbits per second.

#### Step 1: Identify Sampling Rate
The Nyquist rate is $2 \times 3 = 6$ MHz. Since the sampling rate is twice the Nyquist rate, the sampling frequency is:

$$f_s = 2 \times 6 = 12\text{ MHz}$$

#### Step 2: Determine Quantization Levels
The number of quantization levels (L) is given by $2^n$, where n is the number of bits per sample.

$$1024 = 2^n \Rightarrow n = 10$$

#### Step 3: Calculate Bit Rate
Using the formula for bit rate:

$$b_s = n \times f_s \log_2(L) = 10 \times 12 \log_2(1024) = 240\text{ Mbits per second}$$

**Common Pitfalls**
------------------

1.  **Incorrect Sampling Rate**: Failure to calculate the minimum sampling rate required for the signal.
2.  **Inaccurate Quantization Levels**: Incorrect calculation of the number of quantization levels (L).
3.  **Miscalculated Bit Rate**: Error in applying the formula for bit rate.

**Quick Summary**
----------------

*   Sampling Theorem: $f_s > 2B_w$
*   Quantization: Division of analog signal into discrete levels
*   Bit Rate: $b_s = n \times f_s \log_2(L)$