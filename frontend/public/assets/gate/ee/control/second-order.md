**Second-Order Systems: Control Theory**
======================================

**Introduction**
---------------

A second-order system is a type of control system that can be represented by a differential equation of order two. It has two poles, which are critical for understanding the system's behavior and stability. This note covers the essential concepts, formulas, and problem-solving techniques for analyzing and designing second-order systems.

**Core Concepts**
----------------

### Second-Order System Representation

A standard second-order system can be represented by the transfer function:

$$G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_ns + \omega_n^2}$$

where $\omega_n$ is the natural frequency and $\zeta$ is the damping ratio.

### Pole Locations

The poles of a second-order system are given by:

$$p_{1,2} = -\zeta\omega_n \pm \sqrt{\zeta^2\omega_n^2 - \omega_n^2}$$

### Stability and Damping Ratio

A second-order system is stable if both poles have negative real parts. The damping ratio $\zeta$ determines the stability of the system:

* $\zeta < 1$: Underdamped (oscillatory behavior)
* $\zeta = 1$: Critically damped
* $\zeta > 1$: Overdamped

### Settling Time

The settling time $t_s$ is the time it takes for the response to settle within a certain percentage of its final value. For a second-order system, the settling time can be approximated by:

$$t_s \approx \frac{3}{\zeta\omega_n}$$

### Problem Solving Patterns
---------------------------

When analyzing second-order systems, follow these steps:

1. Write down the transfer function or differential equation.
2. Determine the poles and their locations.
3. Analyze the stability of the system using the damping ratio.
4. Calculate the settling time if required.

**Key Formulas/Theorems**
------------------------

* Transfer function: $G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_ns + \omega_n^2}$
* Pole locations: $p_{1,2} = -\zeta\omega_n \pm \sqrt{\zeta^2\omega_n^2 - \omega_n^2}$
* Settling time: $t_s \approx \frac{3}{\zeta\omega_n}$

**Examples with Solutions**
---------------------------

### Example 1:

Consider a second-order system with the transfer function:

$$G(s) = \frac{s + 5}{s^2 + 10s + 25}$$

Determine the poles, stability, and settling time.

```markdown
## Step-by-Step Solution

1. Determine the poles:
p_{1,2} = -5 ± √(25 - 25) = -5
2. Analyze the stability: Since both poles have negative real parts, the system is stable.
3. Calculate the settling time:
t_s ≈ \frac{3}{\zeta\omega_n} ≈ \frac{3}{1 \cdot 5} ≈ 0.6 s

The final answer is: $\boxed{0.6}$

### Example 2:

Consider a second-order system with the transfer function:

$$G(s) = \frac{s + 10}{s^2 + 20s + 100}$$

Determine the poles, stability, and settling time.

```markdown
## Step-by-Step Solution

1. Determine the poles:
p_{1,2} = -10 ± √(100 - 100) = -10
2. Analyze the stability: Since both poles have negative real parts, the system is stable.
3. Calculate the settling time:
t_s ≈ \frac{3}{\zeta\omega_n} ≈ \frac{3}{1 \cdot 5} ≈ 0.6 s

The final answer is: $\boxed{0.6}$

**Common Pitfalls**
------------------

* Forgetting to check stability before calculating settling time.
* Misinterpreting the effect of damping ratio on system behavior.

**Quick Summary**
-----------------

* Second-order systems are represented by a transfer function or differential equation.
* Poles determine stability and settling time.
* Damping ratio affects oscillatory behavior and settling time.
* Settling time can be approximated using $\zeta\omega_n$.

Note: The above content is generated based on the provided source questions. However, it is essential to review and update the content regularly to ensure it remains relevant and accurate for the GATE CS exam.