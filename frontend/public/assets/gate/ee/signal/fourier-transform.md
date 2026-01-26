# Fourier Transform
====================

## Introduction
---------------

The Fourier Transform (FT) is a mathematical tool used to decompose a function or a signal into its constituent frequencies. It's a fundamental concept in signal processing, and its applications range from filtering and modulation analysis to image compression.

## Core Concepts
-----------------

### Definition of the Fourier Transform

Given a function $x(t)$ defined for $-\infty < t < \infty$, the Fourier Transform is defined as:

$$X(\omega) = \int_{-\infty}^{\infty} x(t)e^{-j\omega t}dt$$

where $\omega$ is the frequency domain variable.

### Properties of the Fourier Transform

1.  **Linearity**: The FT is linear, meaning that it preserves the linearity of operations on the original signal.
2.  **Time-Shifting Property**: If $x(t)$ is shifted by a time $t_0$, its FT is also shifted in frequency by $\omega_0 = -\frac{1}{t_0}$.

### Key Formulas/Theorems
-------------------------

*   Convolution Theorem: $x(t) \ast y(t) \Leftrightarrow X(\omega)Y(\omega)$
*   Modulation Theorem: $e^{jat}x(t) \Leftrightarrow X(\omega-a)$

### Problem Solving Patterns
---------------------------

1.  **Direct Computation**: Evaluate the integral directly.
2.  **Inverse Fourier Transform (IFT)**: Use the IFT to find the time-domain representation of a given FT.

## Examples with Solutions
-------------------------

### Example 1:

Given $x(t) = \cos(4t)e^{-|t|}$, find its derivative at $\omega=0$.

Solution:
We first compute the FT of $x(t)$ using the definition:

$$X(\omega) = \int_{-\infty}^{\infty} x(t)e^{-j\omega t}dt = \int_{-\infty}^{0} -te^{-|t|}e^{-j\omega t}dt + \int_{0}^{\infty} te^{-|t|}e^{-j\omega t}dt$$

To evaluate the derivative of $X(\omega)$ at $\omega=0$, we can use L'Hôpital's rule:

$$\frac{d}{d\omega} X(\omega) \bigg|_{\omega=0} = \lim_{\omega \to 0} \frac{\int_{-\infty}^{\infty} t e^{-j\omega t}x(t) dt}{1/j}$$

Simplifying and evaluating the limit yields:

$$\left.\frac{d}{d\omega} X(\omega)\right|_{\omega=0} = \lim_{\omega \to 0} \int_{-\infty}^{\infty} t e^{-j\omega t}x(t) dt = 0.3$$

### Example 2:

Given that $f(t)$ is an even function and its FT is defined as $\mathcal{F}\{f(t)\} = F(\omega)$, and if $dF/d\omega = -\omega$ for all $\omega$, then evaluate $\int_{-\infty}^{\infty} f(t) e^{j\omega t} dt$ at $\omega=0$.

Solution:
Since $f(t)$ is even, we can use the fact that the FT of an even function is real-valued:

$$F(\omega) = \mathcal{F}\{f(t)\} = \int_{-\infty}^{\infty} f(t)e^{-j\omega t} dt$$

Since $dF/d\omega = -\omega$ for all $\omega$, we have:

$$F'(\omega) = -\omega F(\omega)$$

Evaluating this at $\omega=0$ and noting that $F(0)=1$, we obtain:

$$F'(0) = 0$$

## Common Pitfalls
-------------------

*   **Incorrect application of the linearity property**.
*   **Failure to consider even/odd properties**.

## Quick Summary
---------------

*   The Fourier Transform decomposes a signal into its constituent frequencies.
*   Linearity, time-shifting properties, and convolution theorem are essential concepts in FT analysis.
*   Understanding problem-solving patterns, such as direct computation and inverse Fourier transform, is crucial for tackling challenging questions.