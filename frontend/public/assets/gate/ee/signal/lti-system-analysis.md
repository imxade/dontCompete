**LTi System Analysis**
=======================

**Introduction**
---------------

Linear Time-Invariant (LTI) systems are a fundamental concept in signal processing and analysis. An LTI system is characterized by its ability to process inputs in a linear and time-invariant manner, meaning that the output is directly proportional to the input and does not depend on any initial conditions.

**Core Concepts**
-----------------

### Linearity

An LTI system satisfies the following two properties:

1.  **Homogeneity**: If $x(t)$ is an input signal and $a$ is a scalar, then the output of the system for input $ax(t)$ is equal to $ax(t)$.
2.  **Additivity**: If $x_1(t)$ and $x_2(t)$ are two input signals, then the output of the system for inputs $x_1(t) + x_2(t)$ is equal to the sum of the outputs for individual inputs.

### Time-Invariance

An LTI system satisfies the following property:

*   **Shift-invariance**: If $x(t)$ is an input signal and $h(t)$ is the impulse response of the system, then the output of the system for input $x(t + \tau)$ is equal to $h(t) * x(t)$.

**Key Formulas/Theorems**
-------------------------

### Convolution Theorem

The convolution theorem states that if an LTI system has an impulse response $h(t)$ and an input signal $x(t)$, then the output of the system can be expressed as:

$$y(t) = h(t) \ast x(t)$$

where $\ast$ denotes the convolution operation.

### Fourier Transform Properties

The following properties of the Fourier transform are useful in analyzing LTI systems:

*   **Linearity**: $X(f) \to aX(f)$ and $X(f) \to X(f) + Y(f)$
*   **Time-Shifting**: $e^{j\omega_0t}x(t) \to X(f - f_0)$
*   **Frequency-Shifting**: $x(t)e^{j\omega_0t} \to X(f + f_0)$

**Problem Solving Patterns**
---------------------------

When solving problems involving LTI systems, the following patterns are commonly encountered:

1.  **Impulse Response**: The impulse response of an LTI system is used to determine its output for a given input signal.
2.  **Convolution**: The convolution operation is used to find the output of an LTI system for a given input signal.
3.  **Fourier Transform**: The Fourier transform is often used to analyze the frequency content of signals and the response of LTI systems.

**Examples with Solutions**
-------------------------

### Example 1

Let $x(t) = 2\sin(10t) + 5\cos(15t) + 7\sin(42t) + 4\cos(45t)$ be an input signal and let the impulse response of an LTI system be $h(t) = \frac{1}{\pi}(\sin(10t) - \cos(40t))$. Find the output of the system.

Solution:

$$y(t) = h(t) \ast x(t) = (\frac{1}{\pi}\sin(10t) - \frac{1}{\pi}\cos(40t)) \ast (2\sin(10t) + 5\cos(15t) + 7\sin(42t) + 4\cos(45t))$$

Using the convolution theorem and the linearity property of the Fourier transform, we can express the output as:

$$y(t) = \frac{1}{2}(\sin(10t) - \cos(40t)) \ast (2\sin(10t) + 5\cos(15t) + 7\sin(42t) + 4\cos(45t))$$

Simplifying, we get:

$$y(t) = 7\sin(42t) + 4\cos(45t)$$

### Example 2

Let $x(t) = \frac{1}{\pi}(\sin(10t) - \cos(40t))$ be an input signal and let the impulse response of an LTI system be $h(t) = 2\sin(10t) + 5\cos(15t)$. Find the output of the system.

Solution:

Using the convolution theorem, we can express the output as:

$$y(t) = h(t) \ast x(t) = (2\sin(10t) + 5\cos(15t)) \ast (\frac{1}{\pi}\sin(10t) - \frac{1}{\pi}\cos(40t))$$

Simplifying, we get:

$$y(t) = 5\cos(15t)$$

**Common Pitfalls**
------------------

*   Failing to apply the linearity and time-invariance properties of LTI systems.
*   Not using the convolution theorem correctly.
*   Ignoring the initial conditions of the system.

**Quick Summary**
-----------------

*   Linearity: The output is directly proportional to the input.
*   Time-Invariance: The response does not depend on any initial conditions.
*   Convolution Theorem: $y(t) = h(t) \ast x(t)$
*   Fourier Transform Properties:
    *   Linearity: $X(f) \to aX(f)$ and $X(f) \to X(f) + Y(f)$
    *   Time-Shifting: $e^{j\omega_0t}x(t) \to X(f - f_0)$
    *   Frequency-Shifting: $x(t)e^{j\omega_0t} \to X(f + f_0)$