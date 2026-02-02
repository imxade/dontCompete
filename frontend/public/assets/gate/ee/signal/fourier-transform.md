# Fourier Transform Theory Note
==========================

## Introduction
---------------

The Fourier transform is a mathematical tool used to decompose a signal into its constituent frequencies. It's a fundamental concept in signal processing and has numerous applications in various fields, including engineering, physics, and computer science.

## Core Concepts
-----------------

### Definition of the Fourier Transform

Given a continuous-time signal $x(t)$, the Fourier transform is defined as:

$$X(\omega) = \int_{-\infty}^{\infty} x(t)e^{-j\omega t}dt$$

### Inverse Fourier Transform

The inverse Fourier transform is used to reconstruct the original signal from its frequency domain representation. It's defined as:

$$x(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} X(\omega)e^{j\omega t}d\omega$$

### Linearity Property

The Fourier transform is a linear operator, meaning that the Fourier transform of a sum of signals is equal to the sum of their individual Fourier transforms.

$$\mathcal{F}\left\{\sum_{n=1}^{\infty} x_n(t)\right\} = \sum_{n=1}^{\infty} X_n(\omega)$$

## Key Formulas/Theorems
-------------------------

### Fourier Transform of Common Signals

| Signal | Fourier Transform |
| --- | --- |
| $x(t) = e^{j\omega_0t}$ | $\mathcal{F}\left\{e^{j\omega_0t}\right\} = 2\pi \delta(\omega - \omega_0)$ |
| $x(t) = \cos(\omega_0 t)$ | $\mathcal{F}\left\{\cos(\omega_0 t)\right\} = \frac{1}{2}(j\delta(\omega - \omega_0) + j\delta(\omega + \omega_0))$ |

### Parseval's Theorem

Parseval's theorem states that the energy of a signal in the time domain is equal to its energy in the frequency domain.

$$\int_{-\infty}^{\infty} |x(t)|^2dt = 2\pi \int_{-\infty}^{\infty} |X(\omega)|^2d\omega$$

## Problem Solving Patterns
---------------------------

### Finding the Fourier Transform of a Signal

1. Write down the signal $x(t)$.
2. Substitute $x(t)$ into the definition of the Fourier transform.
3. Evaluate the integral.

### Using the Linearity Property

1. Identify the individual signals in the sum.
2. Find their individual Fourier transforms using the linearity property.
3. Sum the individual Fourier transforms to find the Fourier transform of the sum.

## Examples with Solutions
-------------------------

### Example 1: Finding the Fourier Transform of a Cosine Signal

$x(t) = \cos(\omega_0 t)$

$$\mathcal{F}\left\{\cos(\omega_0 t)\right\} = \frac{1}{2}(j\delta(\omega - \omega_0) + j\delta(\omega + \omega_0))$$

### Example 2: Using the Linearity Property

$x(t) = x_1(t) + x_2(t)$

$$\mathcal{F}\left\{x(t)\right\} = X_1(\omega) + X_2(\omega)$$

## Common Pitfalls
------------------

* Forgetting to use the linearity property when finding the Fourier transform of a sum of signals.
* Misapplying Parseval's theorem.

## Quick Summary
---------------

| Concept | Description |
| --- | --- |
| Definition of the Fourier Transform | $X(\omega) = \int_{-\infty}^{\infty} x(t)e^{-j\omega t}dt$ |
| Inverse Fourier Transform | $x(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} X(\omega)e^{j\omega t}d\omega$ |
| Linearity Property | $\mathcal{F}\left\{\sum_{n=1}^{\infty} x_n(t)\right\} = \sum_{n=1}^{\infty} X_n(\omega)$ |

## References
-------------

* [1] Oppenheim, A. V., & Willsky, A. S. (1997). Signals and systems. Prentice Hall.
* [2] Papoulis, A. (1984). The Fourier integral and its applications. McGraw-Hill.

Note: The references provided are not included in the output as they are external sources. You can include them if you need to cite specific information.