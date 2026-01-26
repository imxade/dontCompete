**Linear Time-Invariant Discrete Time Systems**
==============================================

### Introduction
A linear time-invariant (LTI) discrete-time system is a mathematical model that describes a physical system, where the output depends on the input and not on any external variable. The system's behavior can be described using difference equations.

### Core Concepts
An LTI system has two main properties:

1.  **Linearity**: The system satisfies the principle of superposition, meaning that if we have multiple inputs, the response to each input is identical in form but scaled by a factor equal to the input value.
2.  **Time Invariance**: The system's behavior does not change with time; it remains invariant.

**Impulse Response**
--------------------

The impulse response of an LTI system is defined as the output when the input is a unit impulse ($\delta[n]$). It represents the system's response to a sudden, brief disturbance. Let $h[n]$ be the impulse response of the system.

### Key Formulas/Theorems
$\boxed{\text{Convolution Property:} y[n] = \sum_{k=-\infty}^{\infty} h[k]x[n-k]}$

This formula shows that the output $y[n]$ can be obtained by convolving the impulse response $h[n]$ with the input signal $x[n]$.

### Problem Solving Patterns
When solving LTI system problems, follow these steps:

1.  Identify the type of problem (e.g., finding the impulse response or the output for a given input).
2.  Use the difference equation to describe the system's behavior.
3.  Apply the convolution property or other relevant formulas.

### Examples with Solutions
**Example 1:** Find the impulse response of an LTI system described by the difference equation:

$$y[n] - \frac{1}{2} y[n-1] = x[n]$$

## Solution
Using the definition of the impulse response, we have:

$$h[n] - \frac{1}{2} h[n-1] = \delta[n]$$

To solve for $h[n]$, we can use the following approach:

*   For $n=0$, we get: $$h[0] = 1$$
*   For $n>0$, we get: $$h[n] = 2^n h[0] = 2^n$$

Therefore, the impulse response of the system is:

$$h[n] = \begin{cases} 1 & n=0 \\ 2^n & n>0 \end{cases}$$

### Common Pitfalls
*   Failing to check for linearity and time invariance.
*   Incorrectly applying the convolution property or other formulas.

### Quick Summary
*   LTI systems are linear and time-invariant.
*   The impulse response represents the system's response to a unit impulse.
*   Convolution property: $y[n] = \sum_{k=-\infty}^{\infty} h[k]x[n-k]$