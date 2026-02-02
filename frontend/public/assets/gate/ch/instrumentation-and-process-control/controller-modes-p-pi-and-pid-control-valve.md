**Controller Modes: P, PI, and PID Control Valve**
======================================================

### Introduction

In process control systems, a controller regulates the process by adjusting the final control element (FCE), such as a control valve. The choice of controller mode depends on the system's dynamics, stability requirements, and performance specifications. This note covers the fundamental concepts of proportional (P), proportional-integral (PI), and proportional-integral-derivative (PID) controllers in the context of control valves.

### Core Concepts

#### Proportional (P) Control

A P controller adjusts its output based on the error between the setpoint and process variable. The controller's output is directly proportional to the error:

$$u(t) = K_p \cdot e(t)$$

where $u(t)$ is the control signal, $K_p$ is the proportional gain, and $e(t)$ is the error.

#### Proportional-Integral (PI) Control

A PI controller adds an integral term to the P controller's output. The integral term eliminates steady-state errors by continuously adjusting the output until the process variable reaches the setpoint:

$$u(t) = K_p \cdot e(t) + K_i \cdot \int_{0}^{t} e(\tau) d\tau$$

where $K_i$ is the integral gain.

#### Proportional-Integral-Derivative (PID) Control

A PID controller combines the P and PI controllers with a derivative term, which predicts future errors based on the rate of change of the process variable:

$$u(t) = K_p \cdot e(t) + K_i \cdot \int_{0}^{t} e(\tau) d\tau + K_d \cdot \frac{de(t)}{dt}$$

where $K_d$ is the derivative gain.

### Key Formulas/Theorems

*   The characteristic equation of a PID controller is given by:

    $$s^3 + K_p s^2 + K_i s + K_d = 0$$

    where $s$ is the Laplace variable.

*   The steady-state error for a step input is zero for P and PI controllers, while it depends on the derivative gain for PID controllers:

    $$e_{ss} = \frac{K_d}{K_p (1 + K_i)}$$

### Problem Solving Patterns

When solving problems related to controller modes, focus on the following techniques:

*   Identify the type of input (step, ramp, or impulse) and determine the expected response.
*   Analyze the system's dynamics and stability requirements to select the appropriate controller mode.
*   Use Laplace transforms to derive the characteristic equation and analyze stability.

### Examples with Solutions

**Example 1:** A temperature control system uses a PID controller with $K_p = 2$, $K_i = 3$, and $K_d = 4$. Determine the steady-state error for a step input.

Solution:

*   The characteristic equation is:

    $$s^3 + 2 s^2 + 3 s + 4 = 0$$

    The roots are complex with zero real part, indicating stability.
*   The steady-state error is:

    $$e_{ss} = \frac{4}{2 (1 + 3)} = \frac{2}{7}$$

**Example 2:** A flow control system uses a PI controller with $K_p = 5$ and $K_i = 6$. Determine the response to a step input.

Solution:

*   The characteristic equation is:

    $$s^2 + 5 s + 6 = (s + 3)(s + 2)$$

    The roots are real and positive, indicating stability.
*   The Laplace transform of the output is:

    $$Y(s) = \frac{K}{s(s + 3)(s + 2)}$$

### Common Pitfalls

*   When using a PID controller, ensure that the derivative gain does not amplify high-frequency noise.
*   Be cautious when selecting the proportional and integral gains to avoid oscillations or overshoot.

### Quick Summary

*   Proportional (P) control: $u(t) = K_p \cdot e(t)$
*   Proportional-Integral (PI) control: $u(t) = K_p \cdot e(t) + K_i \cdot \int_{0}^{t} e(\tau) d\tau$
*   Proportional-Integral-Derivative (PID) control: $u(t) = K_p \cdot e(t) + K_i \cdot \int_{0}^{t} e(\tau) d\tau + K_d \cdot \frac{de(t)}{dt}$