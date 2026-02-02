**Theory Note: PI Control**
==========================

**Introduction**
---------------

PI (Proportional-Integral) control is a type of feedback control widely used in various industrial and engineering applications. It's essential for maintaining stability, regulating process variables, and improving system performance. In this theory note, we'll delve into the core concepts of PI control, key formulas, problem-solving patterns, and examples.

**Core Concepts**
----------------

### Overview of PI Control

PI control combines proportional (P) and integral (I) terms to provide both short-term and long-term corrections. The P term responds immediately to changes in the process variable, while the I term accumulates errors over time to eliminate steady-state errors.

### Block Diagram Representation

A PI controller can be represented using a block diagram as follows:

```mermaid
graph LR
    A[Process] --> B[PI Controller]
    C[Error (e)] --> D[Integrator]
    E[Proportional Gain (Kp)] --> F[Gain]
    G[Integral Gain (Ki)] --> H[Gain]
```

### PI Control Formula

The transfer function of a PI controller is given by:

$$G(s) = K_p + \frac{K_i}{s}$$

where $K_p$ and $K_i$ are the proportional and integral gains, respectively.

**Key Formulas/Theorems**
------------------------

1. **PI Controller Transfer Function**: $G(s) = K_p + \frac{K_i}{s}$
2. **Characteristic Equation of Unity Feedback System**: $1 + G(s)F(s) = 0$

where $F(s)$ is the process transfer function.

**Problem Solving Patterns**
---------------------------

### Stability Analysis

To analyze stability, we need to determine the roots of the characteristic equation:

$1 + G(s)F(s) = 0$

If all roots have negative real parts, the system is stable. Otherwise, it's unstable or marginally stable.

### PI Control Parameter Tuning

The maximum value of $K_i$ can be chosen by ensuring stability or marginal stability:

$$\frac{K_i}{s} < -\frac{s^3 + s^2 + 4s + 5}{s^2(s+2)}$$

**Examples with Solutions**
---------------------------

### Example: Unity Feedback System Stability Analysis

Given a unity feedback system with PI control parameters $P = 2$ and $I = 1.25$, determine the maximum value of $K_i$ that keeps the overall system stable.

Characteristic equation:

$$s^3 + s^2 + 4s + 5 + \frac{2}{s} + \frac{1.25}{s(s+2)} = 0$$

Solving for roots, we find that the maximum value of $K_i$ is approximately $\boxed{3.125}$.

**Common Pitfalls**
------------------

*   Forgetting to account for process dynamics when selecting PI control parameters.
*   Ignoring stability analysis and solely relying on trial-and-error tuning methods.
*   Incorrectly applying derivative terms in PI control formulas.

**Quick Summary**
----------------

*   PI control combines proportional and integral terms for short-term and long-term corrections.
*   Characteristic equation of unity feedback system is $1 + G(s)F(s) = 0$.
*   Stability analysis involves determining roots of the characteristic equation.
*   Maximum value of $K_i$ can be chosen by ensuring stability or marginal stability.