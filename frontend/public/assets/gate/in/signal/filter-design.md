**Filter Design**
====================

### Introduction
---------------

Filter design is a crucial aspect of signal processing, aiming to modify signals while preserving certain characteristics. In this note, we'll delve into the theoretical foundations of filter design, focusing on the concepts and techniques relevant to GATE CS.

### Core Concepts
-----------------

#### Convolution
Convolution is a fundamental operation in signal processing, used to combine two signals in the time domain. The output signal is obtained by sliding one signal over the other and summing the products at each position.

*   **Discrete-Time Convolution**: $y[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k]$
    *   where:
        *   $x[n]$ is the input signal
        *   $h[n]$ is the impulse response of the filter
        *   $y[n]$ is the output signal

#### Impulse Response
The impulse response of a filter is its response to an impulse input. It characterizes the filter's behavior and is essential in filter design.

*   **Impulse Response**: $h[n] = \sum_{k=0}^{N-1} h_k \delta[n-k]$
    *   where:
        *   $h_k$ are the tap weights
        *   $\delta[n]$ is the unit impulse signal

### Key Formulas/Theorems
-------------------------

#### Convolution Theorem
The convolution theorem states that the output of a linear time-invariant (LTI) system, when convolved with an input signal, results in the same output as if the LTI system was applied directly to the input.

*   **Convolution Theorem**: $y[n] = h[n] \ast x[n]$
    *   where:
        *   $h[n]$ is the impulse response of the filter
        *   $x[n]$ is the input signal

### Problem Solving Patterns
---------------------------

1.  **Identify the Filter Structure**: Understand the given filter structure, including the tap weights and the number of taps.
2.  **Determine the Input Signal**: Analyze the input signal and identify its characteristics.
3.  **Apply Convolution or Impulse Response**: Use convolution or impulse response to find the output signal.

### Examples with Solutions
---------------------------

**Example 1**
Given a filter with tap weights $h_k = [2, -1]$ and an input signal $x[n] = [3, 2, 1, 1, 0, 0]$:

*   Find the impulse response of the filter.
*   Determine the output signal using convolution.

**Solution**

*   Impulse Response: $h[n] = \sum_{k=0}^{N-1} h_k \delta[n-k] = [2\delta[n], -\delta[n+1]]$
*   Convolution: $y[n] = x[n] \ast h[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k]$

**Example 2**
Given a filter with tap weights $h_k = [0, 2, -1]$ and an input signal $x[n] = [3, 3, 3, 3]$:

*   Find the impulse response of the filter.
*   Determine the output signal using convolution.

**Solution**

*   Impulse Response: $h[n] = \sum_{k=0}^{N-1} h_k \delta[n-k] = [0\delta[n], 2\delta[n+1], -\delta[n+2]]$
*   Convolution: $y[n] = x[n] \ast h[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k]$

### Common Pitfalls
-------------------

1.  **Misunderstanding Filter Structure**: Failing to correctly identify the filter structure and tap weights.
2.  **Incorrect Convolution or Impulse Response Application**: Applying convolution or impulse response incorrectly, leading to incorrect output signals.

### Quick Summary
---------------

*   **Convolution**: Combining two signals in the time domain using a sliding window sum.
*   **Impulse Response**: Characterizing a filter's behavior when given an impulse input.
*   **Convolution Theorem**: Output of LTI system is equal to convolution of input signal with impulse response.

Note: This note covers the theoretical concepts and techniques relevant to GATE CS questions on filter design. It provides examples with solutions, highlights common pitfalls, and offers a quick summary for revision purposes.