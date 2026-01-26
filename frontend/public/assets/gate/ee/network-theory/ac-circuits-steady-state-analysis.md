**AC Circuits Steady State Analysis**
=====================================

### Introduction
-----------------

In this section, we will delve into the world of AC circuits and analyze them in steady state. This involves understanding the behavior of AC circuits when they have reached a stable condition.

### Core Concepts
-----------------

*   **Phasors**: Phasors are complex numbers that represent AC waveforms. They are used to simplify the analysis of AC circuits.
*   **Impedance**: Impedance is the total opposition to the flow of an alternating current in a circuit, including resistance and reactance.

### Key Formulas/Theorems
---------------------------

The key formulas for steady state analysis are:

$$Z = R + jX$$

where $Z$ is impedance, $R$ is resistance, and $X$ is reactance.

$$V = I \cdot Z$$

where $V$ is voltage, $I$ is current, and $Z$ is impedance.

### Problem Solving Patterns
---------------------------

When solving AC circuit problems in steady state:

1.  Identify the components of the circuit.
2.  Determine the type of circuit (series, parallel, or combination).
3.  Apply Ohm's law for circuits to find voltages and currents.
4.  Use Kirchhoff's laws as necessary.

### Examples with Solutions
---------------------------

**Example 1**

A series RC circuit has a resistance of 10 $\Omega$ and capacitance of 0.5 F. The voltage across the resistor is given by:

$$V_R = I \cdot R$$

where $I$ is the current through the circuit.

The impedance of the circuit can be calculated using:

$$Z = R + jX_c = R + \frac{1}{j\omega C}$$

Simplifying, we get:

$$Z = 10 + \frac{1}{0.5 \cdot j2\pi f}$$

Substituting this into Ohm's law, we can solve for the current $I$.

**Solution**

The solution is as follows:


```latex
I = \frac{V_{in}}{\left|Z\right|}
```

where $V_{in}$ is the input voltage.


For the given circuit with a 10 V source:

$$I = \frac{10}{\sqrt{100 + (1/0.5j2\pi f)^2}}$$


```latex
% Simplifying for clarity:
I = \frac{10}{\sqrt{\frac{(100(2\pi f)^2 + 4)}{(2\pi f)^2}}} \\
% Substituting the values and performing calculations:
% Simplified Expression for I in terms of frequency (f)
% I \approx 9.98 
```

The magnitude of the voltage across the resistor is then:

$$V_R = I \cdot R \approx 99.8 V$$

**Example 2**

A circuit consists of a 3 $\Omega$ and a 6 $\Omega$ resistor in parallel, with a 10 F capacitor connected across them. The AC source has an amplitude of 10 V.


```mermaid
graph LR
    A[3 Ω] -->|I|> B[Capacitor]
    C[6 Ω] -->|I|> D[Capacitor]
```

**Solution**

First, we calculate the total impedance:

$$Z = \frac{1}{\frac{1}{3} + \frac{1}{6}} = 2$$


The magnitude of the current is:


```latex
% Calculate I from Z and V:
I = \frac{V}{|Z|}
```

$V=10$, $Z=2$, so we have $I = \frac{10}{2}$, which gives us $5$ amps.


Now, we can find the magnitude of the voltage across each resistor using Ohm's law:


```latex
% Apply V = I * Z to calculate VR for both resistors:
VR_3Ω = 3A * 3Ω
VR_6Ω = 6A * 6Ω 
```

Hence, $VR_3\Omega$ is $9V$, and $VR_6\Omega$ is $36V$.