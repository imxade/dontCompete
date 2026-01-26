# Fourier Transform
## Introduction

The Fourier Transform (FT) is a powerful mathematical tool used to decompose a function or a signal into its constituent frequencies. It's a fundamental concept in Signal Processing and has numerous applications in various fields, including Electrical Engineering, Computer Science, and Physics.

In this note, we'll cover the theoretical concepts, formulas, and insights required to solve questions related to Fourier Transform.

## Core Concepts

### Periodic Signals

A periodic signal is one that repeats itself at regular intervals. Mathematically, a periodic signal can be represented as:

$$x(t) = \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0t}$$

where $c_n$ are the complex coefficients and $\omega_0$ is the fundamental frequency.

### Fourier Series

The Fourier series is a mathematical representation of a periodic signal as a sum of sinusoidal functions with different frequencies. The coefficients of these sinusoidal functions can be calculated using the following formulas:

$$a_n = \frac{1}{T} \int_{-T/2}^{T/2} x(t) e^{-jn\omega_0t} dt$$

$$b_n = \frac{1}{T} \int_{-T/2}^{T/2} x(t) e^{-j(n+1)\omega_0t} dt$$

where $a_n$ and $b_n$ are the complex coefficients, $x(t)$ is the periodic signal, $\omega_0$ is the fundamental frequency, and $T$ is the period.

## Key Formulas/Theorems

### Fourier Transform of a Periodic Signal

The Fourier Transform of a periodic signal can be calculated using the following formula:

$$X(j\omega) = \frac{1}{j\omega} \sum_{n=-\infty}^{\infty} c_n \delta(\omega - n\omega_0)$$

where $X(j\omega)$ is the Fourier Transform of the signal, $c_n$ are the complex coefficients, and $\delta(\omega - n\omega_0)$ is the Dirac delta function.

### Convolution Theorem

The Convolution Theorem states that the product of two signals in the time domain corresponds to the convolution of their Fourier Transforms:

$$x(t) * h(t) \leftrightarrow X(j\omega)H(j\omega)$$

where $x(t)$ and $h(t)$ are the input and impulse response signals, respectively.

### Parseval's Theorem

Parseval's Theorem states that the energy of a signal in the time domain is equal to the sum of the energies of its frequency components:

$$E = \int_{-\infty}^{\infty} |x(t)|^2 dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} |X(j\omega)|^2 d\omega$$

## Problem Solving Patterns

* When given a periodic signal, use the Fourier series to represent it as a sum of sinusoidal functions.
* Use the Convolution Theorem to find the Fourier Transform of the product of two signals.
* Apply Parseval's Theorem to relate the energy of a signal in the time domain to its frequency components.

## Examples with Solutions

### Example 1: Fourier Series Representation of a Periodic Signal

Find the Fourier series representation of the periodic signal:

$$x(t) = \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0t}$$

where $c_n$ are the complex coefficients and $\omega_0$ is the fundamental frequency.

**Solution**

To find the coefficients, we integrate the signal with the conjugate of each harmonic:

$$a_n = \frac{1}{T} \int_{-T/2}^{T/2} x(t) e^{-jn\omega_0t} dt$$

For this example, assume that $c_n = 1$ for all n. Then:

$$a_n = \frac{1}{T} \int_{-T/2}^{T/2} e^{j(n-n)\omega_0t} dt$$

Evaluating the integral, we get:

$$a_n = \frac{\sin(n\pi)}{n\pi}$$

The Fourier series representation of the signal is:

$$x(t) = \sum_{n=-\infty}^{\infty} e^{jn\omega_0t}$$

### Example 2: Convolution Theorem

Find the Fourier Transform of the product of two signals:

$$y(t) = x(t) * h(t)$$

where $x(t)$ and $h(t)$ are the input and impulse response signals, respectively.

**Solution**

Using the Convolution Theorem, we have:

$$Y(j\omega) = X(j\omega)H(j\omega)$$

Assume that the Fourier Transforms of the two signals are known. Then:

$$X(j\omega) = \frac{1}{j\omega} \sum_{n=-\infty}^{\infty} c_n \delta(\omega - n\omega_0)$$

$$H(j\omega) = \frac{1}{j\omega} \sum_{m=-\infty}^{\infty} d_m \delta(\omega - m\omega_d)$$

where $c_n$ and $d_m$ are the complex coefficients, $\omega_0$ is the fundamental frequency of $x(t)$, and $\omega_d$ is the fundamental frequency of $h(t)$.

Evaluating the convolution product, we get:

$$Y(j\omega) = \sum_{n=-\infty}^{\infty} c_n d_n \delta(\omega - n\omega_0 - m\omega_d)$$

## Common Pitfalls

* When using the Convolution Theorem, make sure to use the correct ordering of the signals (i.e., $x(t) * h(t)$).
* Be careful when applying Parseval's Theorem, as it only holds for finite energy signals.

## Quick Summary

| Concept | Formula/Theorem |
| --- | --- |
| Fourier Transform of a Periodic Signal | $X(j\omega) = \frac{1}{j\omega} \sum_{n=-\infty}^{\infty} c_n \delta(\omega - n\omega_0)$ |
| Convolution Theorem | $x(t) * h(t) \leftrightarrow X(j\omega)H(j\omega)$ |
| Parseval's Theorem | $E = \int_{-\infty}^{\infty} |x(t)|^2 dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} |X(j\omega)|^2 d\omega$ |

This comprehensive note covers the key concepts, formulas, and insights required to solve questions related to Fourier Transform. By mastering these topics, you'll be well-prepared to tackle a wide range of problems in Signal Processing and beyond!