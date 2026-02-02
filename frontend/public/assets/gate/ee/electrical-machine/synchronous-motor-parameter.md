**Synchronous Motor Parameters**
=====================================

**Introduction**
---------------

A synchronous motor is a type of AC electrical machine that operates at a fixed speed, synchronized with the frequency of the supply current. It consists of two main parts: the stator and the rotor. The stator is the stationary part that carries the windings, while the rotor is the rotating part that carries the magnetic field.

**Core Concepts**
----------------

### Synchronous Reactance

The synchronous reactance ($X_s$) is a critical parameter in synchronous motor design. It represents the opposition to the flow of current in the stator windings due to the magnetic field established by the rotor. The synchronous reactance is given by:

$$X_s = \frac{E}{I}$$

where $E$ is the induced emf (electromotive force) in the stator windings and $I$ is the current flowing through them.

### Armature Resistance

In a synchronous motor, the armature resistance ($R_a$) is typically negligible due to the high conductivity of the rotor material. However, it can be significant in certain cases, such as when the rotor is made of a lower-conductivity material or when there are significant losses in the rotor.

### Power Factor

The power factor (PF) is a measure of how effectively the motor uses the supply current to produce mechanical output. It is given by:

$$PF = \cos(\theta)$$

where $\theta$ is the phase angle between the voltage and current.

**Key Formulas/Theorems**
-------------------------

* **Synchronous Motor Equation**: The torque developed by a synchronous motor is given by:
  $$T = \frac{E \cdot I}{\omega}$$
* **Power Developed**: The power developed by a synchronous motor is given by:
  $P = T \cdot \omega$
* **Efficiency**: The efficiency of a synchronous motor is given by:
  $$\eta = \frac{P_{out}}{P_{in}}$$

**Problem Solving Patterns**
---------------------------

### Step-by-Step Approach

To solve problems involving synchronous motors, follow these steps:

1. Calculate the induced emf ($E$) using the synchronous reactance and current.
2. Calculate the power developed by the motor using the torque and angular velocity.
3. Calculate the efficiency of the motor using the power output and input.

**Examples with Solutions**
---------------------------

### Example 1

A star-connected 3-phase, 400 V, 50 kVA, 50 Hz synchronous motor has a synchronous reactance of 1 ohm per phase. The shaft load on the motor is 10 kW while the power factor is 0.8 leading. The loss in the motor is 2 kW.

**Solution**

* Calculate the induced emf ($E$):
  $$E = X_s \cdot I$$
  Since $X_s = 1\Omega$, we need to find $I$. We can use the power factor and load to calculate it:
  $$P_{out} = P_{in} - P_L$$
  $$P_{in} = V \cdot I \cos(\theta)$$
  Substituting values, we get:
  $$E = X_s \cdot I = 1 \cdot \frac{V}{X_s} \cos(\theta)$$
* Calculate the power developed by the motor:
  $P_{out} = T \cdot \omega$
  We can use the torque and angular velocity to calculate it.
* Calculate the efficiency of the motor:
  $$\eta = \frac{P_{out}}{P_{in}}$$

### Example 2

A synchronous motor has a synchronous reactance of 2 ohms per phase. The induced emf is 200 V per phase, and the current flowing through it is 100 A per phase.

**Solution**

* Calculate the power developed by the motor:
  $$P = T \cdot \omega$$
  We can use the torque and angular velocity to calculate it.
* Calculate the efficiency of the motor:
  $$\eta = \frac{P_{out}}{P_{in}}$$

**Common Pitfalls**
-------------------

### Neglecting Armature Resistance

When neglecting armature resistance, ensure that the current flowing through the stator windings is correctly calculated.

### Incorrect Calculation of Power Developed

Ensure that the power developed by the motor is correctly calculated using the torque and angular velocity.

### Inaccurate Efficiency Calculations

Ensure that the efficiency of the motor is accurately calculated using the power output and input.

**Quick Summary**
-----------------

* Synchronous reactance ($X_s$) represents opposition to current flow in stator windings.
* Armature resistance ($R_a$) can be significant in certain cases.
* Power factor (PF) measures how effectively motor uses supply current.
* Torque developed by synchronous motor is given by $T = \frac{E \cdot I}{\omega}$.
* Power developed by synchronous motor is given by $P = T \cdot \omega$.
* Efficiency of synchronous motor is given by $\eta = \frac{P_{out}}{P_{in}}$.