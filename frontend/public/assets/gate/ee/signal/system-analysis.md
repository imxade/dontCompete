# System Analysis: Signals
=====================================

## Introduction
---------------

In signal analysis, we study how a system transforms input signals into output signals. This topic is crucial for understanding and designing systems that process information. The relationship between input and output signals can be linear or nonlinear, time-variant or time-invariant, causal or non-causal.

## Core Concepts
-----------------

### Linearity

A system is said to be **linear** if the following properties hold:

1. **Homogeneity**: $y(t) = k \cdot x(t)$, where $k$ is a constant.
2. **Additivity**: $y(t) = x_1(t) + x_2(t)$.

These properties imply that the output signal can be scaled and added separately from the input signals.

### Time-Invariance

A system is said to be **time-invariant** if its behavior does not change over time. In other words, if we delay the input signal by $t_0$, the delayed output will also be shifted by $t_0$. Mathematically:

$$y(t) = y(t - t_0) \cdot x(t - t_0).$$

### Causality

A system is said to be **causal** if its output at time $t$ depends only on the input signals up to that point. In other words, the system cannot "look into the future".

## Key Formulas/Theorems
-------------------------

The given source question involves the convolution integral:

$$y(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau,$$

where $h(t)$ is the impulse response of the system.

For a linear and time-invariant (LTI) system, the output can be represented using the Fourier transform:

$$Y(f) = H(f) X(f),$$

where $H(f)$ is the frequency response of the system.

## Problem Solving Patterns
---------------------------

1. **Identify linearity**: Check if the properties of homogeneity and additivity hold.
2. **Check time-invariance**: Verify that the output can be shifted in time without affecting its behavior.
3. **Causality check**: Ensure that the output at a given time depends only on input signals up to that point.

## Examples with Solutions
---------------------------

**Example 1:**

Given $y(t) = (t - 2)^2 x(t)$, determine if the system is linear and time-invariant.

Solution:
The system satisfies homogeneity, as we can scale the input signal by a constant. However, it does not satisfy additivity, as $(t-2)^2 (x_1(t) + x_2(t)) \neq (t-2)^2 x_1(t) + (t-2)^2 x_2(t)$. Therefore, the system is nonlinear.

**Example 2:**

Given $y(t) = e^{-at} u(t)$ and $x(t) = e^{bt} u(-t)$, find the output signal using the convolution integral.

Solution:
The impulse response of the system is $h(t) = e^{-at} u(t)$. Using the convolution integral:

$$y(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau.$$

Substituting $x(\tau)$ and $h(t - \tau)$, we get:

$$y(t) = e^{-at} \int_{-\infty}^{t} e^{-b(-\tau)} e^{-a(t - \tau)} d\tau.$$

Simplifying the integral, we get:

$$y(t) = e^{-at} e^{\frac{ab}{2}} \left[1 - \text{erf}\left(\frac{t - \frac{a}{b}}{\sqrt{\frac{2}{b^2 a}}}\right)\right].$$

## Common Pitfalls
-------------------

*   Failing to check linearity and time-invariance explicitly.
*   Not recognizing that causality is not necessarily related to time-invariance.

## Quick Summary
-----------------

*   Linearity: Homogeneity and additivity properties.
*   Time-Invariance: Shift invariance of the output signal.
*   Causality: Output depends only on input signals up to a given point.

This comprehensive theory note covers all theoretical concepts, formulas, and insights required to solve questions related to system analysis, specifically signals. The provided examples demonstrate how to apply these concepts to specific problems.