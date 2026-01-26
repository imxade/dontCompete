**Three Phase Induction Motor**
=====================================

### Introduction
-----------------

A three-phase induction motor (TPIM) is a type of AC electrical machine that uses electromagnetic induction to produce torque. It is widely used for industrial and commercial applications due to its simplicity, reliability, and efficiency.

### Core Concepts
------------------

#### Principle of Operation
The TPIM operates on the principle of electromagnetic induction between the stator and rotor windings. When an alternating current flows through the stator winding, it produces a rotating magnetic field that induces currents in the rotor. The rotor then acts as an electromagnet, producing its own magnetic field that interacts with the stator's field to produce torque.

#### Slip
The slip (s) is defined as the ratio of the difference between the synchronous speed (Ns) and the actual speed (N) to the synchronous speed:

$$ s = \frac{N_s - N}{N_s} $$

Slip is an important parameter in induction motor design, as it affects the efficiency and power factor of the machine.

#### Equivalent Circuit
The equivalent circuit of a TPIM consists of stator resistance (Rs), stator leakage reactance (Xs'), rotor resistance (R2'), and rotor leakage reactance (X2'). The circuit can be represented by the following equation:

$$ V_s = \sqrt{(R_1 + sR_2)^2 + (X_{s'}^2 + s^2X_2'^2)} $$

where Vs is the stator voltage.

### Key Formulas/Theorems
---------------------------

#### Synchronous Speed
The synchronous speed of a TPIM can be calculated using the following formula:

$$ N_s = \frac{120f}{P} $$

where f is the frequency and P is the number of poles.

#### Slip Frequency
The slip frequency (sf) is related to the slip (s) by the following equation:

$$ sf = s \times f $$

### Problem Solving Patterns
-----------------------------

1. **Reducing Supply Voltage and Frequency**: When the supply voltage and frequency are reduced, the motor's speed decreases proportionally.
2. **Constant Torque Load**: For a constant torque load, the motor's speed is directly proportional to the slip.

### Examples with Solutions
---------------------------

**Example 1: Reducing Supply Voltage and Frequency**

Given:

* 3-phase induction motor
* Rated supply voltage = 415 V, frequency = 50 Hz, poles = 6
* Speed = 960 RPM, torque load constant

When the supply voltage and frequency are reduced by 20%, calculate the new speed.

Solution:
Using the synchronous speed formula, we can calculate the new synchronous speed:

$$ N_{s,new} = \frac{120 \times (0.8f)}{(0.8P)} $$

Since the slip is proportional to the ratio of the difference between the synchronous speeds and the actual speed, we can write:

$$ s_{new} = \frac{N_{s,new} - N}{N_{s,new}} $$

Substituting the values, we get:

$$ s_{new} = 0.8 \times s $$

Since the torque load is constant, the new speed (N') will be:

$$ N' = N_s' \times (1 - s') $$

Substituting the values, we get:

$$ N' = 760 RPM $$

**Example 2: Constant Torque Load**

Given:

* 3-phase induction motor
* Rated supply voltage = 415 V, frequency = 50 Hz, poles = 6
* Speed = 960 RPM, torque load constant

When the slip is reduced by 20%, calculate the new speed.

Solution:
Using the formula for slip frequency, we can write:

$$ sf' = s' \times f $$

Since the torque load is constant, the new speed (N') will be directly proportional to the slip frequency:

$$ N' \propto sf' $$

Substituting the values, we get:

$$ N' = 760 RPM $$

### Common Pitfalls
-------------------

1. **Incorrect Calculation of Slip**: Failing to calculate the slip correctly can lead to incorrect answers.
2. **Ignoring Stator Leakage Reactance**: Neglecting stator leakage reactance can lead to inaccuracies in equivalent circuit calculations.

### Quick Summary
-----------------

* 3-phase induction motor operates on electromagnetic induction between stator and rotor windings
* Slip is an important parameter affecting efficiency and power factor
* Equivalent circuit consists of stator resistance, stator leakage reactance, rotor resistance, and rotor leakage reactance
* Synchronous speed can be calculated using the formula Ns = 120f/P
* Slip frequency is related to slip by sf = s \times f