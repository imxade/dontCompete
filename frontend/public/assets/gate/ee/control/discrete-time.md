# Discrete Time Control Systems
## Introduction
Discrete time control systems are a fundamental topic in control engineering, focusing on systems where inputs and outputs are discrete in time. This means that the system operates on a set of distinct, evenly spaced time intervals, as opposed to continuous-time systems.

## Core Concepts
A discrete-time system is described by its difference equation, which relates the output at each time step to past inputs and states.

### Difference Equation
The general form of a linear, time-invariant (LTI) discrete-time system's difference equation is:

$$y[n] = ay[n-1] + bx[n]$$

where $y[n]$ is the output at time $n$, $x[n]$ is the input at time $n$, and $a$ and $b$ are constants.

### LTI Systems
A discrete-time system is considered linear if it satisfies the following properties:

* **Homogeneity**: If the input is scaled by a constant, the output is also scaled by that same constant.
* **Superposition**: The response to multiple inputs is the sum of their individual responses.

A system is time-invariant if its response to an input shifted in time is the same as the original response but shifted by the same amount.

## Key Formulas/Theorems
### Transfer Function

The transfer function of a discrete-time LTI system can be obtained by taking the z-transform of the difference equation:

$$H(z) = \frac{Y(z)}{X(z)} = \frac{b}{a - az^{-1}}$$

where $z$ is the complex variable, and $a$ and $b$ are constants from the difference equation.

### Impulse Response
The impulse response of a discrete-time system is the output when the input is an unit impulse $\delta[n]$:

$$h[n] = \left\{\begin{matrix} 1 & n=0 \\ 0 & n>0 \end{matrix}\right.$$

## Problem Solving Patterns

### Question Analysis
From question [ee_2020_43], we can deduce the following patterns:

* **Option analysis**: Eliminate options that are obviously incorrect, and use the knowledge of LTI systems to justify the correct answer.
* **System properties**: Understand the implications of linearity and time-invariance on system behavior.

### Example

Consider a discrete-time system described by the difference equation:

$$y[n] = 0.5y[n-1] + x[n]$$

Find the transfer function $H(z)$.

## Solution

Take the z-transform of both sides of the equation:

$$Y(z) = 0.5z^{-1}Y(z) + X(z)$$

Rearrange to isolate $Y(z)/X(z)$:

$$\frac{Y(z)}{X(z)} = \frac{1}{1 - 0.5z^{-1}}$$

This is the transfer function of the system.

## Common Pitfalls

* **Misunderstanding of linearity and time-invariance**: Make sure to understand how these properties affect system behavior.
* **Incorrect application of z-transforms**: Double-check your calculations when taking the z-transform.

## Quick Summary
- Discrete-time systems are described by difference equations.
- Linear, time-invariant (LTI) discrete-time systems have specific properties and a transfer function.
- Understand the implications of linearity and time-invariance on system behavior.

This comprehensive theory note should provide a solid foundation for tackling questions related to discrete-time control systems.