**Theory Note: LTI System Response**
=====================================

**Introduction**
---------------

A Linear Time-Invariant (LTI) system is a fundamental concept in signal processing and systems. An LTI system's input-output relationship can be represented using impulse response, which is the system's response to an impulse input.

**Core Concepts**
-----------------

* **Linearity**: An LTI system's output for a sum of inputs is the sum of its outputs for each input individually.
* **Time-Invariance**: The system's response does not change over time. If delayed by some amount, the system's response will be identical.

**Key Formulas/Theorems**
------------------------

$$h[n] = \sum_{k=-\infty}^{\infty} h[k]\delta[n-k]$$

$$H(e^{j\omega}) = \sum_{n=-\infty}^{\infty} h[n]e^{-j\omega n}$$

**Problem Solving Patterns**
---------------------------

1.  **Convolution**: The output of an LTI system is the convolution of its input with its impulse response.
    $$y[n] = x[n] \ast h[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k]$$
2.  **Discrete-Time Fourier Transform (DTFT)**: The DTFT of an LTI system's impulse response is equal to its transfer function.
    $$H(e^{j\omega}) = \sum_{n=-\infty}^{\infty} h[n]e^{-j\omega n}$$

**Examples with Solutions**
---------------------------

### Q1: GATE 2021 (ID: in_2021_28)

Given the input-output relationship of an LTI system:

| $n$ | Input ($x[n]$) | Output ($y[n]$) |
| --- | --- | --- |
| 0   | 2               | 4             |
| 1   | 1               | 3             |
| 2   | 1               | 5             |

Find the peak value of the output when $x[n] = [0, 1, 2]$ is passed through the system.

**Solution**

1.  Find the convolution of $x[n]$ and $h[n]$.
    $$y[n] = x[n] \ast h[n]$$
    | $n$ | $x[k]h[n-k]$ |
    | --- | ---         |
    | 0   | 2h[0]        |
    | 1   | h[0]+2h[1]   |
    | 2   | 3h[0]+h[1]+2h[2]|  
2.  Find the output values.
    $$y[0]=2h[0]=4$$
    $$y[1]=(h[0]+2h[1])=3$$
    $$y[2]=(3h[0]+h[1]+2h[2])=5$$  
3.  Find the peak value of the output.
    The peak value is $|y[2]| = |5|$.

### Quick Summary
-----------------

*   LTI systems have linearity and time-invariance properties.
*   Impulse response is the system's response to an impulse input.
*   Convolution of input with impulse response gives the output.
*   DTFT of impulse response equals transfer function.

**Common Pitfalls**
-------------------

1.  **Linearity and Time-Invariance**: Ensure you understand the implications of linearity and time-invariance on system behavior.
2.  **Convolution**: Double-check convolution calculations for accuracy.
3.  **Transfer Function**: Understand the relationship between the transfer function and impulse response.

This comprehensive theory note covers all key concepts, formulas, and problem-solving patterns required to tackle LTI system response problems in signal processing and systems.