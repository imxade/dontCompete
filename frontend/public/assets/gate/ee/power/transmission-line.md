**Transmission Line Theory**
==========================

**Introduction**
---------------

A transmission line is a crucial component of an electric power system, responsible for transporting electrical energy from generation sources to consumption points. In this note, we will cover the essential concepts and formulas related to transmission lines, with a focus on the GATE CS exam.

**Core Concepts**
-----------------

### 1. Lossless Transmission Line

A lossless transmission line is an ideal model of a transmission line where no energy losses occur during transmission. The line is characterized by its resistance (R), inductance (L), capacitance (C), and conductance (G).

### 2. Phasors

Phasors are complex numbers used to represent AC quantities. They are useful for analyzing sinusoidal signals.

### 3. Impedance

Impedance is a measure of the opposition to current flow in an AC circuit. It is denoted by Z and has units of ohms (Ω).

**Key Formulas/Theorems**
-------------------------

* **Ohm's Law**: $V=IZ$
* **Impedance Formula**: $Z=\sqrt{R^2+X^2}$
* **Power Flow Equation**: $P=\frac{EV}{X}$

where:

* E = voltage (V)
* I = current (A)
* R = resistance (Ω)
* X = reactance (Ω)
* P = real power (W)

**Problem Solving Patterns**
---------------------------

### 1. Distance Relay Operation

Distance relays are used to protect transmission lines from faults. The relay operates when the current exceeds a certain threshold.

Example:

Suppose we have a lossless transmission line with a reactance of 0.2 pu per phase, uniformly distributed along its length. If the generator terminal voltage is 1 pu and there is no generation at the load bus, what is the threshold pu current for operation of the distance relay for a solid three-phase-to-ground fault on the transmission line?

Solution:

The impedance seen by the distance relay is given by $Z=\sqrt{R^2+X^2}$. Since the line is lossless, R = 0. Therefore, $Z=X=0.2$ pu.

The current threshold for operation of the distance relay is given by $I_{threshold}=E/X=1/0.2=5$ A.

### 2. Power Flow Through a Transmission Line

Suppose we have two buses connected by a lossless transmission line, with bus 1 sending reactive power towards bus 2 through a line of reactance X. If the voltage at bus 2 is fixed at 1 pu and the magnitude of voltage at bus 1 is changed so that the reactive power sent from bus 1 is increased by 20%, what is the new value of the voltage magnitude at bus 1?

Solution:

The real power flow through the line is zero, since there is no generation at either bus. The reactive power flow is given by $Q=EV/X$. Therefore, if the reactive power is increased by 20%, the new reactive power flow is $Q'=1.2Q$.

Since the voltage at bus 2 is fixed at 1 pu, the reactance of the line X remains constant. Therefore, the new voltage magnitude at bus 1 can be found from $V_1'=\sqrt{E^2/X^2-4Q'}= \boxed{1.12}$ pu.

**Common Pitfalls**
-----------------

* Not considering losses in the transmission line
* Assuming a non-lossless transmission line

**Quick Summary**
-----------------

* Lossless transmission line: R = 0, Z = X
* Distance relay operation: $I_{threshold}=E/X$
* Power flow through a transmission line: $Q=EV/X$

Note: This summary is not exhaustive and is meant to be a quick reference for students.