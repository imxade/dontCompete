**Damping Ratio and Undamped Natural Frequency**
=====================================================

**Introduction**
---------------

The damping ratio and undamped natural frequency are essential concepts in control systems, describing how a system responds to external inputs. In this note, we'll explore these concepts, their mathematical representation, and practical implications.

**Core Concepts**
-----------------

*   **Damping Ratio (ζ)**: A dimensionless quantity that characterizes the damping of a system. It ranges from 0 (undamped) to 1 (critically damped).
*   **Undamped Natural Frequency (ωn)**: The frequency at which an undamped system would oscillate if it were not subject to any external forces.

**Key Formulas/Theorems**
-------------------------

*   **Transfer Function**: The transfer function of a system is given by:
    $$
    G(s) = \frac{C(s)}{R(s)}
    $$

*   **Closed-Loop Transfer Function**: For a closed-loop system with negative feedback, the transfer function becomes:
    $$
    T(s) = \frac{G(s)}{1 + G(s)}
    $$

*   **Damping Ratio (ζ)**: The damping ratio can be calculated from the transfer function as:
    $$
    \zeta = \frac{\sqrt{1 - (\omega_n^2/\omega_d^2)}}{\omega_n}
    $$

*   **Undamped Natural Frequency (ωn)**: ωn is related to the system's natural frequency and damping ratio by:
    $$
    \omega_n = \sqrt{\frac{k}{m}}
    $$

**Problem Solving Patterns**
---------------------------

1.  Identify the transfer function of the given system.
2.  Use the closed-loop transfer function formula to calculate the overall gain.
3.  Analyze the system's poles and zeros to determine stability and natural frequency.
4.  Calculate the damping ratio using the transfer function.

**Examples with Solutions**
-------------------------

### Example 1

Given a system with the following transfer function:
$$
G(s) = \frac{10}{s^2 + 10s + 100}
$$

*   Determine the undamped natural frequency and damping ratio.
*   Calculate the closed-loop transfer function.

Solution:

*   Transfer Function Analysis:
    -   Compare with standard form: $G(s) = \frac{k}{s^2 + bs + k}$
    -   Identify coefficients: b = 10, k = 100
    -   ωn = √k = √100 = 10 rad/s
*   Calculate damping ratio:
    -   ζ = √(1 – (ωn^2/ω_d^2)) / ω_n
    -   Since the system is not explicitly given to be critically damped, assume it's underdamped for simplicity. Thus, we'll use this formula in a more general context.
*   Closed-Loop Transfer Function:
    -   Given G(s), calculate T(s) = G(s) / (1 + G(s))

### Example 2

Given the following block diagram, find the transfer function and determine the damping ratio.

```mermaid
graph LR
A[Input] --> B[G(s)]
B --> C[1]
C --> D[Integrator(s)]
D --> E[Output]
```

Solution:

*   Identify the system's components:
    -   G(s) is the forward path transfer function.
    -   The feedback loop involves a gain of 10 and an integrator (1/s).
*   Calculate the closed-loop transfer function using the formula T(s) = G(s)/(1 + G(s)).

### Common Pitfalls
--------------------

-   **Incorrect application of formulas**: Double-check that you're using the correct formulas for each step.
-   **Misinterpretation of system components**: Carefully identify and label all components in the transfer function or block diagram.
-   **Oversimplification**: Avoid assuming critical damping without proper evidence from the question.

**Quick Summary**
------------------

*   Damping ratio (ζ) and undamped natural frequency (ωn) are crucial for understanding system behavior.
*   Transfer functions describe how a system responds to inputs, while closed-loop transfer functions account for feedback.
*   Use formulas correctly, considering each component's contribution to the overall system.

This comprehensive note covers all theoretical concepts required to solve questions related to damping ratio and undamped natural frequency.