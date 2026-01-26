**Torque Speed Characteristic**
=====================================

**Introduction**
---------------

The torque-speed characteristic of an induction motor is a crucial aspect of its control and operation. This note aims to provide a comprehensive understanding of this concept, covering the theoretical principles, key formulas, problem-solving patterns, examples with solutions, common pitfalls, and quick summary.

**Core Concepts**
-----------------

### Induction Motor Basics

An induction motor consists of two main parts: the stator (stationary part) and the rotor (rotating part). The stator has a three-phase winding that produces a rotating magnetic field. The rotor is an electromagnet that interacts with the stator's magnetic field.

### Torque-Speed Characteristics

The torque-speed characteristic of an induction motor describes how the motor's torque output changes as its speed varies. It is typically represented by a graph, where the x-axis represents the slip (s) and the y-axis represents the torque (T).

**Key Formulas/Theorems**
-------------------------

LaTeX notation for equations:

### Slip-Torque Equation

$$T = \frac{K \cdot V^2}{s^2 + \left(\frac{s_n}{s_{sl}}\right)^2}$$

where:
- T: torque
- K: constant of proportionality
- V: stator voltage
- s: slip
- $s_n$: synchronous speed
- $s_{sl}$: starting slip

### Torque at Maximum Slip (Tm)

$$T_m = \frac{K \cdot V^2}{\left(\frac{s_n}{s_{sl}}\right)^2}$$

**Problem Solving Patterns**
---------------------------

### Q1 Analysis

For the three-phase squirrel-cage induction motor, we are given that the starting torque is 100% of the full-load torque and the maximum torque is 300% of the full-load torque.

*   We need to find the slip at the maximum torque.
*   Since the stator impedance is neglected, we can assume a simplified model for the motor.
*   The maximum torque occurs when the rotor speed is equal to the synchronous speed ($s=0$).

### Q2 Analysis

We are given two magnetically coupled coils with different inductances when connected in series-aiding and series-opposing configurations.

*   We need to find the coupling coefficient (k).
*   The self-inductance of both coils is assumed to be equal.
*   Using the given equations, we can solve for k.

**Examples with Solutions**
---------------------------

### Example 1: Torque-Speed Characteristic

Given a three-phase induction motor with the following parameters:

| Parameter | Value |
| --- | --- |
| Starting torque (T_s) | 100% of full-load torque |
| Maximum torque (T_m) | 300% of full-load torque |

Find the slip at the maximum torque.

**Solution**

Using the slip-torque equation, we can write:

$$T = \frac{K \cdot V^2}{s^2 + \left(\frac{s_n}{s_{sl}}\right)^2}$$

Since T_m occurs when s=0, we can substitute this into the equation and solve for k.

### Example 2: Coupling Coefficient

Given two magnetically coupled coils with inductances L_1 and L_2 when connected in series-aiding and series-opposing configurations:

| Configuration | Inductance (L) |
| --- | --- |
| Series-aiding | 500 mH |
| Series-opposing | 300 mH |

Find the coupling coefficient (k).

**Solution**

Using the equations for self-inductance and mutual inductance, we can write:

$$L_{series-aiding} = L_1 + L_2 + 2M$$
$$L_{series-opposing} = L_1 + L_2 - 2M$$

Substituting the given values and solving for M, we can then find k.

**Common Pitfalls**
-------------------

*   Forgetting to account for stator impedance.
*   Assuming a linear relationship between torque and slip.
*   Failing to consider the effects of mutual inductance on coupled coils.

**Quick Summary**
------------------

*   The torque-speed characteristic of an induction motor describes how its torque output changes with speed.
*   Key formulas include the slip-torque equation and the torque at maximum slip equation.
*   Problem-solving patterns involve analyzing given parameters and using relevant equations to solve for desired quantities.

Note: This note is intended as a starting point for studying the topic. Students should supplement this content with additional resources and practice problems to reinforce their understanding.