**Transient Behavior or Initial Condition**
=====================================

**Introduction**
---------------

In network theory, transient behavior refers to the change in system response over time when an external disturbance is introduced. This concept is crucial for understanding how circuits behave under various conditions. The initial condition plays a significant role in determining the circuit's response.

**Core Concepts**
-----------------

When dealing with transient behavior, we need to consider two primary aspects:

1.  **Initial Condition**: This refers to the state of the circuit before any external disturbance is introduced.
2.  **Time Constant**: This represents the time it takes for a system to reach 63.2% of its final value.

**Key Formulas/Theorems**
-------------------------

*   For an inductor-capacitor (LC) circuit, the natural response can be described by:

$$\frac{d^2Q}{dt^2} + \omega_0^2 Q = 0$$

where $Q$ is the charge on the capacitor and $\omega_0$ is the resonant frequency.

*   For an inductor-capacitor-resistor (LCR) circuit, the natural response can be described by:

$$\frac{d^2V}{dt^2} + \frac{1}{RC}\frac{dV}{dt} + \omega_0^2 V = 0$$

where $V$ is the voltage across the capacitor and $\omega_0$ is the resonant frequency.

**Problem Solving Patterns**
---------------------------

When solving problems related to transient behavior, consider the following patterns:

*   Analyze the initial condition of the circuit.
*   Identify any external disturbances introduced into the system.
*   Apply the relevant formulas or theorems to describe the natural response of the circuit.

**Examples with Solutions**
-------------------------

### Example 1: LC Circuit

An LC circuit is formed by connecting a capacitor and an inductor in series. The initial voltage across the capacitor is $V_0 = 10\, \text{V}$, and the inductance is $L = 0.5\, \text{H}$. At time $t = 0$, the switch is closed.

*   (a) Determine the current through the circuit at $t = 1$ s.
*   (b) Determine the voltage across the capacitor at $t = 2$ s.

### Solution

(a) The current through the inductor can be described by:

$$I(t) = \frac{V_0}{\omega L}\sin(\omega t)$$

where $\omega = \sqrt{\frac{1}{LC}}$. Substituting the given values, we get:

$$I(1) = \frac{10}{\sqrt{\frac{1}{0.5 \times 10^{-6}}} \cdot 0.5} \sin(\sqrt{\frac{1}{0.5 \times 10^{-6}}} \cdot 1) = 20\, \text{A}$$

(b) The voltage across the capacitor can be described by:

$$V_c(t) = V_0 e^{-\omega t}$$

Substituting the given values, we get:

$$V_c(2) = 10 e^{-\sqrt{\frac{1}{0.5 \times 10^{-6}}} \cdot 2} = 3.74\, \text{V}$$

### Example 2: LCR Circuit

An LCR circuit is formed by connecting a capacitor, an inductor, and a resistor in series. The initial voltage across the capacitor is $V_0 = 30\, \text{V}$, the inductance is $L = 10\, \text{H}$, and the resistance is $R = 4\, \Omega$. At time $t = 0$, the switch is closed.

*   (a) Determine the current through the circuit at $t = 1$ s.
*   (b) Determine the voltage across the capacitor at $t = 2$ s.

### Solution

(a) The current through the inductor can be described by:

$$I(t) = \frac{V_0}{R} e^{-\frac{R}{L} t}$$

Substituting the given values, we get:

$$I(1) = \frac{30}{4} e^{-\frac{4}{10}} = 7.5 e^{-0.4} = 6.46\, \text{A}$$

(b) The voltage across the capacitor can be described by:

$$V_c(t) = V_0 (1 - e^{-\frac{R}{L} t})$$

Substituting the given values, we get:

$$V_c(2) = 30 (1 - e^{-0.4 \cdot 2}) = 21.63\, \text{V}$$

**Common Pitfalls**
-------------------

*   Failing to consider the initial condition of the circuit.
*   Not applying the relevant formulas or theorems.

**Quick Summary**
-----------------

Transient behavior or initial condition is a critical concept in network theory that describes how circuits behave under various conditions. Key concepts include:

*   Initial Condition: The state of the circuit before any external disturbance is introduced.
*   Time Constant: The time it takes for a system to reach 63.2% of its final value.

Key formulas and theorems include:

*   Natural response of an LC circuit
*   Natural response of an LCR circuit

Problem solving patterns involve analyzing the initial condition, identifying external disturbances, and applying relevant formulas or theorems.