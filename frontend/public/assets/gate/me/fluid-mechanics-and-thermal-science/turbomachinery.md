**Turbomachinery**
================

### Introduction
-----------------

Turbomachines are devices that use the energy of a fluid (liquid or gas) to produce mechanical work. They are crucial components in various industrial processes, including power generation, pumping, and compression. In this note, we will focus on turbines, which convert kinetic energy into rotational energy.

### Core Concepts
-----------------

#### **Velocity Triangle**
The velocity triangle is a fundamental concept in turbomachinery. It shows the relationship between the absolute velocity (V), relative velocity (W), and tangential velocity (u) at any point in the turbine.

```mermaid
graph LR
    V[Absolute Velocity] --> W[Relative Velocity]
    W --> u[Tangential Velocity]
```

#### **Specific Speed**
The specific speed of a turbine is defined as:

$$ N_s = \frac{N\sqrt{P}}{H^{3/4}} $$

where $N$ is the rotational speed, $P$ is the power output, and $H$ is the head.

#### **Efficiency**
Turbine efficiency can be calculated using the following formula:

$$ \eta = \frac{\text{Ideal Power Output}}{\text{Actual Power Input}} $$

### Key Formulas/Theorems
-------------------------

*   **Tangential Velocity**: $u = r\omega$
*   **Absolute Velocity**: $V = u + W$
*   **Specific Speed**: $N_s = \frac{N\sqrt{P}}{H^{3/4}}$

### Problem Solving Patterns
-----------------------------

When solving problems related to turbines, follow these steps:

1.  Identify the given parameters (e.g., head, flow rate, rotational speed).
2.  Determine the type of turbine and its specific characteristics.
3.  Calculate the ideal power output using the Euler's pump-turbine equation:
    $$ P_{\text{ideal}} = \rho Q g H $$
4.  Account for losses (e.g., friction, leakage) to find the actual power input.

### Examples with Solutions
---------------------------

**Example:**

A Francis turbine operates at 300 rpm, with an available head of 200 m. The tip speed is 40 m/s, and water leaves the runner without whirl. The velocity at the exit of the draft tube is 3.5 m/s. The flow rate through the turbine is 20 m³/s.

**Solution:**

1.  Calculate the ideal power output:
    $$ P_{\text{ideal}} = \rho Q g H $$
    $$ P_{\text{ideal}} = 1000 \times 20 \times 9.8 \times 200 = 3,920,000 W $$
2.  Account for losses in the stator, rotor, and draft tube:
    $$ P_{\text{actual}} = P_{\text{ideal}} - (5 + 10 + 2) \times Q \rho g H $$
    $$ P_{\text{actual}} = 3,920,000 - (17 \times 20 \times 1000 \times 9.8 \times 200) / 1000 $$
    $$ P_{\text{actual}} = 1,960,080 W $$
3.  Calculate the hydraulic efficiency:
    $$ \eta = \frac{P_{\text{ideal}}}{P_{\text{actual}}} \times 100\% $$
    $$ \eta = \frac{3,920,000}{1,960,080} \times 100\% = 99.73\% $$

### Common Pitfalls
--------------------

When solving problems related to turbines:

*   Be careful when applying the Euler's pump-turbine equation.
*   Don't forget to account for losses in various components.

### Quick Summary
-------------------

Key concepts:

*   Velocity triangle
*   Specific speed
*   Efficiency

Formulas:

*   Tangential velocity: $u = r\omega$
*   Absolute velocity: $V = u + W$
*   Specific speed: $N_s = \frac{N\sqrt{P}}{H^{3/4}}$

Problem-solving steps:

1.  Identify given parameters.
2.  Determine the type of turbine and its characteristics.
3.  Calculate ideal power output using Euler's equation.
4.  Account for losses.

Note: This comprehensive theory note covers all essential concepts, formulas, and problem-solving techniques required to tackle turbomachinery questions, especially those from previous year exams.