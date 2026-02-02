**Network Analysis**
====================

### Introduction
---------------

Network analysis is a fundamental topic in Electrical Engineering that deals with the study of electrical networks, including both passive (resistors, capacitors, and inductors) and active components (sources). This theory note focuses on the basics of network analysis, covering key concepts, formulas, and problem-solving patterns.

### Core Concepts
-----------------

*   **Network Topology**: The arrangement of components within a circuit.
*   **Node**: A point where two or more branches meet in a network.
*   **Branch**: A conductor that carries current between nodes.
*   **Mesh**: A closed path in a network containing no other closed paths.

### Key Formulas/Theorems
-------------------------

$$\begin{aligned}
V &= \frac{\omega LI}{R} \\
Z &= R + jX_L - jX_C \\
I_{max} &= \frac{V_0}{\sqrt{(R^2 + (\omega L - \frac{1}{\omega C})^2)^2}} \\
f &= \frac{1}{2\pi \sqrt{LC}}
\end{aligned}$$

where $V$ is the voltage across an inductor, $\omega$ is the angular frequency, $L$ is the inductance, $R$ is the resistance, $Z$ is the impedance, $X_L$ is the inductive reactance, $X_C$ is the capacitive reactance, $I_{max}$ is the maximum current through a component, and $f$ is the resonant frequency.

### Problem Solving Patterns
-----------------------------

*   **Identify Network Topology**: Understand how components are connected.
*   **Solve for Voltage or Current**: Use Ohm's law ($V = IR$), Kirchhoff's voltage law (KVL), or Kirchhoff's current law (KCL).
*   **Calculate Impedance**: Combine resistance and reactance.

### Examples with Solutions
---------------------------

**Example 1:** Find the value of inductance $L$ for an air-core coil connected in series with a variable capacitor, given that a maximum voltage of 30 V is observed across it when excited by a 10 V sinusoidal source at 1000 rad/s.

```latex
% \documentclass{article}
\begin{aligned}
V_{max} &= 30 \\
R &= 10 \Omega \\
\omega &= 1000 \text{ rad/s} \\
C &= x \\
I_{max} &= \frac{V_0}{\sqrt{(R^2 + (\omega L - \frac{1}{\omega C})^2)^2}} = \frac{V_{max}}{\sqrt{R^2 + (\omega L - \frac{1}{\omega x})^2}}
% \end{aligned}
```

Solving for $L$:

$$\begin{aligned}
I_{max} &= \frac{30}{\sqrt{(10)^2 + (1000L - \frac{1}{1000x})^2}} \\
R &= 10
% \end{aligned}$$

Given the maximum voltage, solve for L:

**Example 2:**

### Common Pitfalls
-------------------

*   **Incorrect Application of KVL/KCL**: Verify that the chosen variables satisfy the laws.
*   **Miscalculating Impedance**: Combine resistance and reactance correctly.

### Quick Summary
------------------

*   Network topology and component connections are essential to solving network problems.
*   Use key formulas, such as Ohm's law, KVL/KCL, and impedance calculations, to solve for voltage or current.
*   Verify the application of laws and formulas carefully to avoid common pitfalls.