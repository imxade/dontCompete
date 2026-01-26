**LTIS System and Impulse Response**
=====================================

**Introduction**
---------------

A Linear Time-Invariant (LTI) system is a fundamental concept in signal processing, where the output of the system depends only on the current input and not on any past inputs. In this section, we will explore the properties and characteristics of LTI systems, particularly focusing on impulse response.

**Core Concepts**
----------------

### Linearity

An LTI system satisfies two important properties:

1.  **Homogeneity**: If the input is scaled by a constant factor, the output is also scaled by the same factor.
2.  **Additivity**: The output of the system for the sum of two inputs is equal to the sum of the outputs for each individual input.

### Time Invariance

An LTI system has the property that its response to an input signal does not change with time. Mathematically, this can be represented as:

$$y(t) = h \ast x(t)$$

where $h$ is the impulse response of the system and $x(t)$ is the input signal.

**Key Formulas/Theorems**
-------------------------

### Convolution Property

The convolution property states that the output of an LTI system can be obtained by convolving the input signal with the impulse response of the system:

$$y(n) = \sum_{k=-\infty}^{\infty} h(k)x(n-k)$$

where $h$ is the impulse response and $x$ is the input signal.

### Frequency Response

The frequency response of an LTI system can be obtained using the Fourier Transform (FT):

$$H(e^{j\omega}) = \sum_{k=-\infty}^{\infty} h(k)e^{-jk\omega}$$

where $H(e^{j\omega})$ is the frequency response and $\omega$ is the angular frequency.

**Problem Solving Patterns**
-----------------------------

When solving problems related to LTI systems, follow these steps:

1.  **Check for Linearity**: Verify that the system satisfies the properties of linearity.
2.  **Determine the Impulse Response**: Identify the impulse response $h$ of the system.
3.  **Convolve the Input Signal**: Convolve the input signal with the impulse response using the convolution property.

**Examples with Solutions**
---------------------------

### Example 1

Given an LTI system with an impulse response:

$$h = \begin{cases} 2, & n = 0 \\ 1, & |n| = 1 \\ 0, & otherwise \end{cases}$$

Find the output of the system when the input signal is:

$$x(n) = \begin{cases} 3, & n = 0 \\ -1, & n = 1 \\ 2, & n = 2 \\ 0, & otherwise \end{cases}$$

Using the convolution property, we can compute the output as:

$$y(0) = h(0)x(0) + h(-1)x(1) + h(1)x(2) = (2)(3) + (1)(-1) + (1)(2) = 6 - 1 + 2 = 7$$

Similarly, we can compute the output at other time instants.

### Example 2

Given an LTI system with a frequency response:

$$H(e^{j\omega}) = \frac{1}{(e^{j\omega} + 0.5)}$$

Find the output of the system when the input signal is a sinusoid:

$$x(n) = e^{j10n}$$

Using the inverse FT, we can compute the output as:

$$y(n) = \sum_{k=-\infty}^{\infty} h(k)e^{-jk10n}$$

We can simplify this expression using the frequency response of the system.

**Common Pitfalls**
-------------------

1.  **Incorrectly assuming a non-LTI system**: Be careful to check for linearity before applying LTI properties.
2.  **Overlooking boundary conditions**: Ensure that you consider the impulse response and input signal at all time instants, including boundaries.

**Quick Summary**
-----------------

*   An LTI system satisfies homogeneity and additivity.
*   The output of an LTI system can be obtained by convolving the input signal with the impulse response.
*   The frequency response of an LTI system can be obtained using the Fourier Transform.
*   Use the convolution property to solve problems related to LTI systems.