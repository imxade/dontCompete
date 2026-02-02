**Steady State Error**
=======================

**Introduction**
---------------

Steady state error refers to the difference between the desired output and the actual output of a control system after it has reached its steady state. It is an important concept in control systems as it indicates how well the system can track the input signal.

**Core Concepts**
-----------------

A control system consists of several components:

* **Plant**: The physical system being controlled.
* **Controller**: The device that adjusts the plant's parameters to achieve the desired output.
* **Sensor**: The device that measures the output of the plant.

The steady state error is typically measured in terms of the error between the actual output and the desired output. There are several types of steady state errors, including:

* **Position Error**: The difference between the final position of the system and the desired position.
* **Velocity Error**: The difference between the final velocity of the system and the desired velocity.
* **Acceleration Error**: The difference between the final acceleration of the system and the desired acceleration.

**Key Formulas/Theorems**
-------------------------

The steady state error can be calculated using the following formula:

$$e_{ss} = \lim_{t\to\infty} e(t)$$

where $e(t)$ is the error signal at time $t$.

For a system with a transfer function $G(s)$, the steady state error can be calculated as:

$$e_{ss} = \frac{1}{1+G(0)}$$

**Problem Solving Patterns**
---------------------------

To solve problems involving steady state errors, follow these steps:

1.  Identify the type of error (position, velocity, acceleration).
2.  Calculate the transfer function $G(s)$.
3.  Substitute $s=0$ into the transfer function to find the steady state gain.
4.  Use the formula $e_{ss} = \frac{1}{1+G(0)}$ to calculate the steady state error.

**Examples with Solutions**
---------------------------

### Example 1

Find the steady state error for a system with the following transfer function:

$$G(s) = \frac{s^2 + s + 1}{s(s+1)}$$

The steady state gain is calculated by substituting $s=0$ into the transfer function:

$$G(0) = \frac{1}{0} = \infty$$

Since $G(0)$ is infinite, the system has no steady state error.

### Example 2

Find the steady state error for a system with the following transfer function:

$$G(s) = \frac{s+1}{s^2 + s + 1}$$

The steady state gain is calculated by substituting $s=0$ into the transfer function:

$$G(0) = \frac{1}{1} = 1$$

Using the formula $e_{ss} = \frac{1}{1+G(0)}$, we get:

$$e_{ss} = \frac{1}{1+1} = \frac{1}{2}$$

**Common Pitfalls**
------------------

*   Failing to identify the type of error (position, velocity, acceleration).
*   Not calculating the transfer function correctly.
*   Substituting $s=0$ into the transfer function incorrectly.

**Quick Summary**
-----------------

*   Steady state error is the difference between the desired output and the actual output after the system has reached its steady state.
*   There are several types of steady state errors (position, velocity, acceleration).
*   The steady state error can be calculated using the formula $e_{ss} = \lim_{t\to\infty} e(t)$ or $e_{ss} = \frac{1}{1+G(0)}$.
*   To solve problems involving steady state errors, follow the steps outlined above.

**Reference**
--------------

This theory note has been updated based on previous year questions from the GATE CS exam. The reference question used for this update is:

Q: Question 20
The closed loop transfer function of control system is given by

$$\frac{C(s)}{R(s)} = \frac{1}{s+1}$$

For the input $r(t) = \sin(2t)$, the steady state response $c(t)$ is _______

(25)
 
(D)
 
(B)

Sol.

Given:

$$x[n] = \frac{1}{\pi}\sin(2n)u(n)$$

where $u(n)$ is a unit step function.