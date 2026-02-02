**Random Processes in Communications**
=====================================

### Introduction

In communications systems, random processes play a crucial role in understanding how signals are transmitted and received. A random process is a mathematical description of a sequence of random events or signals that occur over time. In this note, we will cover the key concepts, formulas, and techniques required to solve problems related to random processes in communications.

### Core Concepts

#### Additive White Gaussian Noise (AWGN)

AWGN is a type of noise that is added to a signal during transmission. It has the following characteristics:

* **Zero-mean**: The expected value of the noise is zero.
* **White**: The power spectral density of the noise is constant across all frequencies.
* **Gaussian**: The noise follows a Gaussian distribution.

#### Probability of Error

The probability of error in a communications system is defined as the probability that the received signal is different from the transmitted signal. It can be calculated using the following formula:

$$P_e = \int_{-\infty}^{\infty} p(x|0) Q\left(\frac{x-\mu}{\sigma}\right) dx$$

where $p(x|0)$ is the probability density function of the noise when a 0 is transmitted, $\mu$ is the mean of the noise, and $\sigma$ is the standard deviation of the noise.

#### Maximum A Posteriori (MAP) Receiver

A MAP receiver is a type of receiver that uses the a posteriori probability to make decisions about the transmitted signal. The a posteriori probability is given by:

$$p(s|x) = \frac{p(x|s)p(s)}{p(x)}$$

where $p(x|s)$ is the likelihood function, $p(s)$ is the prior probability of the transmitted signal, and $p(x)$ is the marginal probability of the received signal.

### Key Formulas/Theorems

#### MAP Receiver Threshold

The threshold for a MAP receiver can be calculated using the following formula:

$$\gamma = \frac{1}{2} \log_2 \left(\frac{p(0)}{p(1)}\right)$$

where $p(0)$ and $p(1)$ are the prior probabilities of transmitting a 0 or a 1, respectively.

### Problem Solving Patterns

When solving problems related to random processes in communications, follow these steps:

1. **Identify the type of noise**: Determine whether the noise is AWGN or another type.
2. **Calculate the probability of error**: Use the formula for the probability of error to calculate the desired quantity.
3. **Use the MAP receiver threshold**: Apply the formula for the MAP receiver threshold to determine the optimal decision boundary.

### Examples with Solutions

**Example 1:**

A binary communication system uses a polar NRZ waveform with +2V and -2V to represent binary '1' and '0', respectively. The a priori probability of transmission of a binary '1' is 0.4, and the variance of the AWGN is 0.4 V^2. Find the optimum threshold voltage for a MAP receiver.

**Solution:**

Using the formula for the MAP receiver threshold:

$$\gamma = \frac{1}{2} \log_2 \left(\frac{p(0)}{p(1)}\right)$$

Substituting $p(0)=0.6$ and $p(1)=0.4$, we get:

$$\gamma = \frac{1}{2} \log_2 \left(\frac{0.6}{0.4}\right) = 0.04$$

**Example 2:**

A binary communication system uses a polar NRZ waveform with +2V and -2V to represent binary '1' and '0', respectively. The variance of the AWGN is 0.8 V^2, and the probability of transmission of a binary '1' is 0.3. Find the probability of error.

**Solution:**

Using the formula for the probability of error:

$$P_e = \int_{-\infty}^{\infty} p(x|0) Q\left(\frac{x-\mu}{\sigma}\right) dx$$

Substituting $p(x|0)=\frac{1}{\sqrt{2\pi 0.8}}e^{-\frac{(x-0)^2}{2(0.8)}}$ and $\sigma=\sqrt{0.8}$, we get:

$$P_e = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi 0.8}}e^{-\frac{(x-0)^2}{2(0.8)}} Q\left(\frac{x-0}{\sqrt{0.8}}\right) dx$$

Evaluating the integral, we get:

$$P_e = 0.3$$

### Common Pitfalls

* Failing to identify the type of noise and its characteristics.
* Not using the correct formula for the probability of error or MAP receiver threshold.
* Not considering the prior probabilities of transmission.

### Quick Summary

* Random processes play a crucial role in communications systems.
* AWGN is a type of noise that has zero-mean, white, and Gaussian properties.
* The probability of error can be calculated using the formula:
$$P_e = \int_{-\infty}^{\infty} p(x|0) Q\left(\frac{x-\mu}{\sigma}\right) dx$$
* The MAP receiver threshold can be calculated using the formula:
$$\gamma = \frac{1}{2} \log_2 \left(\frac{p(0)}{p(1)}\right)$$