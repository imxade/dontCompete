**System Analysis: Signal Topic**
=====================================

**Introduction**
---------------

In this topic, we will delve into the fundamental concepts of signals and systems, specifically focusing on linearity and time-invariance. A system's behavior can be described using these properties, which are essential for understanding how a system responds to an input signal.

**Core Concepts**
-----------------

### Linearity

A system is said to be **linear** if its output response to a linear combination of inputs is equal to the same linear combination of individual responses. In other words:

Given two input signals x(t) and y(t), a system is linear if:

$$y(t) = Ax_1(t) + By_2(t) \iff y(t) = A\hat{y}_1(t) + B\hat{y}_2(t)$$

where $\hat{y}$ represents the output of the system for each individual input.

**Time-Invariance**
-------------------

A system is **time-invariant** if a time shift in the input signal results in an identical time shift in the output signal. Mathematically, this can be expressed as:

Given an input signal x(t) and its shifted version $x(t-\tau)$, a system is time-invariant if:

$$y(t) = x(t) \iff y(t-\tau) = x(t-\tau)$$

**Key Formulas/Theorems**
-------------------------

### Convolution Integral

For a linear time-invariant (LTI) system, the output y(t) can be expressed as the convolution of the input signal x(t) with the impulse response h(t):

$$y(t) = \int_{-\infty}^{\infty} x(\tau)h(t-\tau)d\tau$$

### Fourier Transform

The Fourier transform is a crucial tool for analyzing signals and systems. The inverse Fourier transform can be used to find the original signal from its frequency domain representation:

$$x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(\omega)e^{j\omega t}d\omega$$

**Problem Solving Patterns**
---------------------------

When faced with a system analysis question, follow these steps:

1.  Determine whether the system is linear and/or time-invariant based on the given information.
2.  Use the convolution integral formula to relate the input signal x(t) to the output signal y(t).
3.  Apply the Fourier transform to analyze the frequency domain behavior of the signals.

**Examples with Solutions**
---------------------------

### Example: Linearity

Suppose we have a system that is linear, and its input-output relationship can be described as:

$$y(t) = x^2(t) + x(t)$$

If we apply two input signals, $x_1(t)$ and $x_2(t)$, to the system, what will be the output?

Solution:

Since the system is linear, we can write:

$$y(t) = A\hat{y}_1(t) + B\hat{y}_2(t) \iff y(t) = Ax_1^2(t) + Ax_1(t) + Bx_2^2(t) + Bx_2(t)$$

This shows that the system's output is a linear combination of the individual outputs for each input signal.

### Example: Time-Invariance

Consider an LTI system with an impulse response h(t). If we apply a time-shifted version of the input signal $x(t-\tau)$ to the system, what will be the resulting output?

Solution:

Since the system is time-invariant, we can write:

$$y(t) = x(t) \iff y(t-\tau) = x(t-\tau)$$

This demonstrates that a time shift in the input signal results in an identical time shift in the output signal.

**Common Pitfalls**
-------------------

When working with signals and systems, be cautious of the following common pitfalls:

*   Assuming linearity without explicit verification
*   Failing to recognize time-invariance
*   Misapplying the Fourier transform

**Quick Summary**
-----------------

*   Linearity: A system is linear if its output response to a linear combination of inputs is equal to the same linear combination of individual responses.
*   Time-Invariance: A system is time-invariant if a time shift in the input signal results in an identical time shift in the output signal.
*   Convolution Integral: For an LTI system, the output y(t) can be expressed as the convolution of the input signal x(t) with the impulse response h(t).
*   Fourier Transform: The inverse Fourier transform can be used to find the original signal from its frequency domain representation.

### References

*   Signals and Systems by Oppenheim and Willsky (2nd ed.)
*   Discrete-Time Signal Processing by Oppenheim and Schafer (3rd ed.)

Note that this theory note is based on the provided source questions and may not cover all aspects of signals and systems. However, it should provide a solid foundation for understanding linearity and time-invariance in system analysis.