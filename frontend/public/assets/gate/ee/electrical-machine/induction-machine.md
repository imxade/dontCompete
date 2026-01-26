**Induction Machine**
=====================

### Introduction
-----------------

An induction machine is a type of electrical machine that uses electromagnetic induction to generate torque and rotate. It consists of two main parts: the stator and the rotor. The stator is the stationary part, while the rotor is the rotating part.

### Core Concepts
------------------

#### Principle of Operation

The principle of operation of an induction machine is based on Faraday's law of electromagnetic induction. When a conductor (rotor) rotates within a magnetic field (stator), an electromotive force (EMF) is induced in the conductor, causing it to rotate.

#### Synchronous Speed

The synchronous speed of an induction motor is given by:

$$n_s = \frac{120f}{p}$$

where $f$ is the frequency of the supply and $p$ is the number of poles.

### Key Formulas/Theorems
-------------------------

#### Equivalent Circuit

The equivalent circuit of an induction machine can be represented as follows:

```mermaid
graph LR
A[Stator] --> B[Rotor]
B[Rotor] --> C[Magnetizing Branch]
C[Magnetizing Branch] --> D[Core Losses]
D[Core Losses] --> E[Rotational Losses]
```

The equivalent circuit consists of the stator and rotor resistance, magnetizing branch (stator to rotor turns ratio), core losses, and rotational losses.

#### Torque Equation

The torque equation for an induction motor is given by:

$$T = \frac{P_m}{\omega}$$

where $P_m$ is the mechanical power developed and $\omega$ is the angular velocity.

### Problem Solving Patterns
---------------------------

1.  **Maximum Torque at Starting**: To have maximum torque at starting, the value of extra resistance in ohms (effective to the rotor side) to be connected in series with each phase of the rotor winding is given by:

    $$R_extra = \frac{R_s}{2} + X_m$$

    where $R_s$ is the stator resistance and $X_m$ is the magnetizing reactance.

### Examples with Solutions
---------------------------

1.  **Example 1**: Find the value of extra resistance in ohms (effective to the rotor side) to be connected in series with each phase of the rotor winding for a 3-phase star-connected slip ring induction motor.

    Given:

    *   $R_s = 2 \Omega$
    *   $X_m = 2.5 \Omega$
    *   Stator to rotor turns ratio = 3:1

    Solution:

    Using the formula, we get:

    $$R_extra = \frac{2}{2} + 2.5 = 0.26 \Omega$$

### Common Pitfalls
------------------

*   **Stator and Rotor Resistance**: Students often miss to consider the stator and rotor resistance while solving problems.
*   **Magnetizing Branch**: The magnetizing branch is often neglected, but it plays a crucial role in determining the torque.

### Quick Summary
-----------------

*   Induction machine uses electromagnetic induction to generate torque and rotate.
*   Equivalent circuit consists of stator and rotor resistance, magnetizing branch, core losses, and rotational losses.
*   Torque equation is given by $T = \frac{P_m}{\omega}$.

This comprehensive theory note covers all the necessary concepts, formulas, and problem-solving patterns required to solve questions on induction machines.