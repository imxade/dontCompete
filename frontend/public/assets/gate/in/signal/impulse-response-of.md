**Impulse Response of LTI Systems**
=====================================

### Introduction

The impulse response of a Linear Time-Invariant (LTI) system is a fundamental concept in signal processing. It describes the output of the system when the input is an unit impulse signal. Understanding the impulse response is crucial for analyzing and designing LTI systems.

### Core Concepts

An LTI system satisfies two key properties:

*   **Linearity**: The system's output to a linear combination of inputs is the same as the linear combination of the individual outputs.
*   **Time Invariance**: A time shift in the input signal causes an equal time shift in the output signal.

The unit impulse signal $\delta(t)$ is defined as:

$$
\delta(t) = \begin{cases}
0, & t \neq 0 \\
\infty, & t = 0
\end{cases}
$$

and satisfies the following properties:

*   $$\int_{-\infty}^{\infty} \delta(t) f(t) dt = f(0)$$
*   $$\mathcal{F}\{\delta(t)\} = 1$$

where $\mathcal{F}$ denotes the Fourier Transform.

### Key Formulas/Theorems

The Impulse Response of an LTI System:

$$
h(t) = \mathcal{L}^{-1}\{H(s)\}
$$

where $H(s)$ is the Transfer Function of the system, and $\mathcal{L}^{-1}$ denotes the inverse Laplace Transform.

The Convolution Theorem:

$$
\begin{aligned}
y(t) &= h(t) \ast x(t) \\
&= \int_{-\infty}^{\infty} h(\tau) x(t - \tau) d\tau
\end{aligned}
$$

### Problem Solving Patterns

1.  **Understand the System**: Identify the type of system (LTI, Linear, Time-Invariant).
2.  **Determine the Impulse Response**: Find the Laplace Transform of the Transfer Function or use the Convolution Theorem.
3.  **Apply Linearity and Time Invariance**: Use these properties to simplify calculations.

### Examples with Solutions

**Example 1**

Given:

$$
\begin{aligned}
h(t) &= \frac{1}{2} \delta(t - 4) + \frac{1}{2} \delta(t + 4) \\
x(t) &= \cos(4t)
\end{aligned}
$$

Find the output $y(t)$:

```mermaid
graph LR
A[Input] --> B[LTI System]
B --> C[Impulse Response]
C --> D[Convolution]
D --> E[Output]
```

Solving this problem involves applying the Convolution Theorem.

**Solution**

$$
\begin{aligned}
y(t) &= h(t) \ast x(t) \\
&= \int_{-\infty}^{\infty} h(\tau) x(t - \tau) d\tau \\
&= \frac{1}{2} \int_{-\infty}^{\infty} \delta(\tau - 4) \cos(4(t - \tau)) d\tau + \frac{1}{2} \int_{-\infty}^{\infty} \delta(\tau + 4) \cos(4(t - \tau)) d\tau \\
&= \frac{1}{2} \cos(4t - 16) + \frac{1}{2} \cos(4t + 16)
\end{aligned}
$$

### Common Pitfalls

*   **Incorrect Transfer Function**: Double-check the Laplace Transform of the Transfer Function.
*   **Misapplication of Linearity and Time Invariance**: Verify these properties before simplifying calculations.

### Quick Summary

*   Impulse Response: $h(t) = \mathcal{L}^{-1}\{H(s)\}$
*   Convolution Theorem: $y(t) = h(t) \ast x(t)$
*   Linearity and Time Invariance: Apply these properties to simplify calculations