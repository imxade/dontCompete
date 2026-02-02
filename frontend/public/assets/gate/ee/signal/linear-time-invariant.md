**Linear Time-Invariant (LTI) Systems**
=====================================

### Introduction

A linear time-invariant (LTI) system is a fundamental concept in signal processing and control systems. It represents a broad class of systems that are characterized by their ability to process signals while preserving the linearity and time-invariance properties.

### Core Concepts

#### Linearity

*   **Homogeneity**: A system satisfies the homogeneity property if, for any input $x(t)$, scaling it by a constant $\alpha$ results in an output scaled by the same constant: $y(t) = \alpha x(t)$.
*   **Additivity**: A system satisfies the additivity property if, for any two inputs $x_1(t)$ and $x_2(t)$, the corresponding outputs are the sum of the individual outputs: $y(t) = x_1(t) + x_2(t)$.

#### Time-Invariance

*   **Shift Invariance**: A system is time-invariant if a time shift in the input signal results in an identical time shift in the output signal. Mathematically, this can be expressed as: $y(t - \tau) = y'(t)$, where $\tau$ is the time shift.

### Key Formulas/Theorems

*   **Convolution Theorem**: The response of an LTI system to a periodic input can be expressed as the product of the Fourier transform of the input and the transfer function of the system: $Y(f) = H(f)X(f)$.
*   **Superposition Principle**: For any two inputs, the corresponding outputs are the sum of the individual outputs.

### Problem Solving Patterns

1.  **Check Linearity**: Verify that the system satisfies both homogeneity and additivity properties.
2.  **Verify Time-Invariance**: Check if a time shift in the input signal results in an identical time shift in the output signal.
3.  **Apply Convolution Theorem**: Use the convolution theorem to find the response of an LTI system to a periodic input.

### Examples with Solutions

**Example 1**

Find the output of an LTI system with transfer function $H(s) = \frac{1}{s + 1}$ for an input signal $x(t) = e^{-2t}u(t)$.

**Solution**

Using the convolution theorem, we have:

$$Y(s) = H(s)X(s) = \frac{1}{s + 1} \cdot \frac{1}{s + 2} = \frac{1}{(s + 1)(s + 2)}$$

To find the output in the time domain, we can use partial fraction expansion:

$$\frac{1}{(s + 1)(s + 2)} = \frac{A}{s + 1} + \frac{B}{s + 2}$$

Solving for A and B, we get:

$$A = -1, B = 1$$

So,

$$Y(s) = -\frac{1}{s + 1} + \frac{1}{s + 2}$$

Taking the inverse Laplace transform, we get:

$$y(t) = e^{-t}u(t) - e^{-2t}u(t)$$

### Common Pitfalls

*   **Missing Linearity Property**: Failing to verify homogeneity and additivity properties.
*   **Incorrect Time-Invariance Assumption**: Assuming a time-invariant system when it is not.

### Quick Summary

*   LTI systems are characterized by linearity and time-invariance properties.
*   Convolution theorem can be used to find the response of an LTI system to a periodic input.
*   Verify homogeneity, additivity, and time-invariance properties before applying formulas.