**Time Invariant Control Systems**
=====================================

**Introduction**
---------------

A time-invariant system is a control system where the output depends only on the current input and not on any external time-dependent factors. This means that if we apply the same input at different times, the system will respond in the same way.

**Core Concepts**
-----------------

*   **Time Invariance**: A system is said to be time-invariant if a delay in the input signal does not affect the output.
*   **Transfer Function**: The transfer function of a system represents its behavior in terms of the ratio of the output to the input. It's denoted by $G(s)$.

**Key Formulas/Theorems**
-------------------------

LaTeX for math:
$\frac{E=mc^2}{\text{No specific formula is required here}}$

However, we do need a basic understanding of the following concepts:

*   **Unit Step Response**: The output of a system when the input is a unit step function.
*   **Transfer Function**: The transfer function of a time-invariant system can be used to analyze its behavior.

**Problem Solving Patterns**
---------------------------

When solving problems related to time-invariant systems, follow these steps:

1.  Identify the type of input signal (e.g., unit step, sinusoidal).
2.  Determine the transfer function of the system.
3.  Use the transfer function to find the output in terms of the input.
4.  Analyze the behavior of the output in response to the input.

**Examples with Solutions**
---------------------------

Let's consider an example where we have two time-invariant systems with different transfer functions:

System 1: $G_1(s) = \frac{1}{s+1}$

System 2: $G_2(s) = \frac{s}{s^2 + 3s + 2}$

We need to find the unit step responses of these systems.

**Solution**

For System 1:

$$y_1(t) = \mathcal{L}^{-1}\left[\frac{1}{s+1}\right]u(t) = e^{-t}u(t)$$

For System 2:

$$y_2(t) = \mathcal{L}^{-1}\left[\frac{s}{s^2 + 3s + 2}\right]u(t) = (c_1e^{rt}+c_2e^{st})u(t)$$

where $r$ and $s$ are the roots of the characteristic equation, which are $-1 \pm j\sqrt{2}$.

Now we can compare the unit step responses:

*   **Peak Overshoot**: The maximum value of the output minus the steady-state value. In this case, both systems have a peak overshoot, but their magnitudes differ.
*   **Steady-State Value**: The final value that the output approaches as time increases. Both systems have the same steady-state value (1).
*   **2% Settling Time**: The time it takes for the output to reach and stay within 2% of its steady-state value. In this case, both systems have different settling times.
*   **Damped Frequency of Oscillation**: The frequency at which the oscillations decay in amplitude. Both systems have the same damped frequency of oscillation.

As a result, the correct answer is (A): $\boxed{1}$ and $\boxed{2}$ have the same percentage peak overshoot.

**Common Pitfalls**
-------------------

*   Don't confuse time-invariance with causality or stability.
*   Be careful when handling transfer functions, especially when dealing with complex poles or zeros.
*   Make sure to analyze both transient and steady-state behavior.

**Quick Summary**
----------------

*   Time-invariant systems have a response that depends only on the current input and not on external time-dependent factors.
*   Transfer functions can be used to analyze the behavior of time-invariant systems.
*   Unit step responses are useful for understanding how the system responds to a unit step input.

This theory note should help you tackle problems related to time-invariant control systems, especially those that involve transfer functions and unit step responses.