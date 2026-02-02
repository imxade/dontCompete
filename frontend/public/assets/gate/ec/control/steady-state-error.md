**Steady State Error**
======================

### Introduction
-----------------

Steady state error is a crucial concept in control systems, measuring the difference between the desired output and actual output when the system has reached its steady state. It's an essential metric for evaluating the performance of a closed-loop control system.

### Core Concepts
------------------

A closed-loop control system consists of:

*   **Plant (P)**: The physical system being controlled.
*   **Controller (C)**: The component that regulates the plant.
*   **Sensor**: Measures the output of the plant.
*   **Actuator**: Implements the control action.

The block diagram of a closed-loop control system is represented as:

```mermaid
graph LR
A[Reference Input] --> B[Controller]
B --> C[Plant]
C --> D[Sensor]
D --> E[Actuator]
E --> F[Output]
```

### Key Formulas/Theorems
---------------------------

The steady state error (e) for a unit ramp input can be calculated using the following formula:

$$ e = \lim_{s \to 0} sG(s)C(s) $$

where $G(s)$ is the transfer function of the plant, and $C(s)$ is the transfer function of the controller.

For a type 1 system (i.e., one with a pole at the origin), the steady state error for a unit ramp input can be calculated as:

$$ e = \frac{1}{K} $$

where $K$ is the gain of the controller.

### Problem Solving Patterns
-----------------------------

When solving problems related to steady state error, follow these steps:

1.  **Determine the type** of system (0, 1, or 2) based on its transfer function.
2.  **Calculate the gain** of the controller ($K$).
3.  **Apply the relevant formula** for calculating the steady state error.

### Examples with Solutions
---------------------------

#### Example 1:

Consider a closed-loop control system with a plant having the following transfer function:

$$ G(s) = \frac{1}{s^2 + s + 1} $$

The controller has a transfer function of:

$$ C(s) = K(s + 1) $$

If the steady state error for a unit ramp input is 0.1, find the value of $K$.

**Solution:**

First, determine the type of system (in this case, it's a type 2 system since there are two poles at the origin).

Next, calculate the gain ($K$) using the formula:

$$ e = \frac{1}{K} $$

Rearranging for $K$, we get:

$$ K = \frac{1}{e} $$

Substituting the given value of steady state error (0.1):

$$ K = \frac{1}{0.1} = 10 $$

#### Example 2:

Consider a type 1 system with a plant having the following transfer function:

$$ G(s) = \frac{1}{s^3 + s^2 + 2s + 1} $$

The controller has a transfer function of:

$$ C(s) = K(s + 1)^2 $$

If the steady state error for a unit ramp input is 0.05, find the value of $K$.

**Solution:**

Determine the type of system (in this case, it's a type 1 system since there is one pole at the origin).

Next, calculate the gain ($K$) using the formula:

$$ e = \frac{1}{K} $$

Rearranging for $K$, we get:

$$ K = \frac{1}{e} $$

Substituting the given value of steady state error (0.05):

$$ K = \frac{1}{0.05} = 20 $$

### Common Pitfalls
-------------------

*   Failing to determine the type of system based on its transfer function.
*   Incorrectly applying formulas for calculating steady state error.
*   Neglecting the gain ($K$) in calculations.

### Quick Summary
-----------------

*   Steady state error is a measure of the difference between desired and actual output at steady state.
*   Type 1, 2, and 0 systems have different formulas for calculating steady state error.
*   Gain ($K$) plays a crucial role in determining steady state error.

By mastering these concepts and techniques, you'll be well-equipped to tackle GATE questions on steady state error.