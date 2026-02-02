**Free and Forced Vibration of Single Degree of Freedom**
====================================================

### Introduction
-----------------

Vibrations are a fundamental aspect of mechanical systems, and understanding their behavior is crucial for designing safe and efficient machines. A single degree-of-freedom (SDOF) system has one mass, one spring, and one damper connected in series. The free vibration of an SDOF system occurs when the system is not subjected to any external forces, while forced vibration occurs when an external force is applied.

### Core Concepts
-----------------

#### Free Vibration

In free vibration, the system's response is governed by its natural frequency and damping ratio. The equation of motion for a damped SDOF system is:

$$m\ddot{x} + c\dot{x} + kx = 0$$

where $m$ is the mass, $c$ is the damping coefficient, and $k$ is the spring constant.

#### Forced Vibration

In forced vibration, an external force is applied to the system. The equation of motion for a damped SDOF system under forced vibration is:

$$m\ddot{x} + c\dot{x} + kx = F_0 \cos(\omega t)$$

where $F_0$ is the amplitude of the external force, and $\omega$ is its frequency.

### Key Formulas/Theorems
-------------------------

#### Undamped Natural Frequency ($\omega_n$)

The undamped natural frequency of an SDOF system is given by:

$$\omega_n = \sqrt{\frac{k}{m}}$$

#### Damping Ratio ($\zeta$)

The damping ratio of an SDOF system is defined as:

$$\zeta = \frac{c}{2 \sqrt{mk}}$$

#### Forced Steady-State Response (Amplitude)

The amplitude of the forced steady-state response of a damped SDOF system is given by:

$$X_r = \frac{\frac{F_0}{k}}{\sqrt{(1-r^2)^2 + (\zeta r)^2}}$$

where $r$ is the frequency ratio, defined as:

$$r = \frac{\omega}{\omega_n}$$

#### Peak Amplitude Frequency

The peak amplitude of the forced steady-state response occurs at a frequency given by:

$$\omega_p = \sqrt{1 - 2\zeta^2 + \sqrt{4\zeta^4 - 4\zeta^2 + 1}}$$

### Problem Solving Patterns
-----------------------------

When solving problems related to free and forced vibration, follow these steps:

1. **Identify the type of vibration**: Is it free or forced?
2. **Write down the equation of motion**: Use the correct formula based on the type of vibration.
3. **Determine the natural frequency**: Use the undamped natural frequency formula ($\omega_n$) if needed.
4. **Calculate the damping ratio**: Use the damping ratio formula ($\zeta$) if needed.

### Examples with Solutions
---------------------------

#### Example 1

Consider a damped SDOF system with $m = 2$ kg, $c = 10$ Ns/m, and $k = 1000$ N/m. The external force is applied at a frequency of $\omega = 20$ rad/s. Find the amplitude of the forced steady-state response.

**Solution**

First, calculate the damping ratio:

$$\zeta = \frac{c}{2 \sqrt{mk}} = \frac{10}{2 \sqrt{2 \times 1000}} = 0.05$$

Next, calculate the frequency ratio:

$$r = \frac{\omega}{\omega_n} = \frac{20}{\sqrt{\frac{1000}{2}}} = 1.414$$

Now, use the formula for the amplitude of the forced steady-state response:

$$X_r = \frac{\frac{F_0}{k}}{\sqrt{(1-r^2)^2 + (\zeta r)^2}}$$

Since we don't have $F_0$, assume it's 100 N. Then:

$$X_r = \frac{\frac{100}{1000}}{\sqrt{(1-1.414^2)^2 + (0.05 \times 1.414)^2}} = 0.5$$

### Common Pitfalls
-------------------

*   Forgetting to convert units correctly.
*   Misinterpreting the type of vibration (free or forced).
*   Not using the correct formula for the natural frequency, damping ratio, or amplitude.

### Quick Summary
------------------

*   **Free Vibration**: Equation of motion $m\ddot{x} + c\dot{x} + kx = 0$.
*   **Forced Vibration**: Equation of motion $m\ddot{x} + c\dot{x} + kx = F_0 \cos(\omega t)$.
*   **Undamped Natural Frequency**: $\omega_n = \sqrt{\frac{k}{m}}$.
*   **Damping Ratio**: $\zeta = \frac{c}{2 \sqrt{mk}}$.
*   **Forced Steady-State Response (Amplitude)**: $X_r = \frac{\frac{F_0}{k}}{\sqrt{(1-r^2)^2 + (\zeta r)^2}}$.

This study note should provide a comprehensive understanding of free and forced vibration of single degree-of-freedom systems. By following the problem-solving patterns, students can effectively tackle various types of questions on this topic.