**Sinusoidal Steady State Analysis**
=====================================

**Introduction**
---------------

Sinusoidal steady state analysis is a technique used to analyze electrical circuits containing sinusoidal sources and impedances. It involves breaking down the circuit into its fundamental frequency components and analyzing each component separately.

**Core Concepts**
-----------------

* **Phasors**: Phasors are complex numbers that represent AC signals. They have both magnitude and phase angle.
* **Impedance**: Impedance is a measure of how much a circuit opposes the flow of current. It is measured in ohms (Ω) and can be either resistive or reactive.
* **Reactance**: Reactance is the opposition to the change in current due to an inductor or capacitor. It is measured in ohms (Ω).
* **Admittance**: Admittance is the reciprocal of impedance.

**Key Formulas/Theorems**
-------------------------

* **Phasor Addition**: $\mathbf{A} + \mathbf{B} = (\mathbf{A_x} + \mathbf{B_x}) + j(\mathbf{A_y} + \mathbf{B_y})$
* **Impedance Division**: $\frac{\mathbf{V}}{\mathbf{I}} = \frac{1}{\mathbf{Y}} = \mathbf{Z}$
* **Admittance Formula**: $\mathbf{Y} = \frac{1}{\mathbf{Z}}$

**Problem Solving Patterns**
---------------------------

### Identifying Components

When analyzing a circuit, identify the components that are relevant to the problem. In this case, we have:

* A sinusoidal source with an amplitude of 1 V and frequency ω.
* An impedance Z.

We need to find the current flowing through the circuit.

**Step 1**: Convert the voltage source to phasor form.

```mermaid
graph LR;
    V[t] -->|V_max|> V0[phasor]
```

**Step 2**: Find the admittance of the impedance Z.

*   If Z is a resistor, then Y = $\frac{1}{Z}$.
*   If Z is an inductor or capacitor, then Y = $j\omega C$ or $\frac{1}{j\omega L}$ respectively.

**Step 3**: Use the admittance formula to find the current I.

$I = \mathbf{V} \cdot \mathbf{Y}$

### Example with Solution

Consider the circuit shown below:

![circuit](https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Sinusoidal_steady_state_analysis_circuit.svg/400px-Sinusoidal_steady_state_analysis_circuit.svg.png)

Find the current flowing through the circuit.

**Solution**

*   Convert the voltage source to phasor form: $V = 1 \angle 0^\circ$
*   Find the admittance of the impedance Z:

    $Y = \frac{1}{Z} = \frac{1}{j\omega L} = -j\frac{1}{\omega L}$

*   Use the admittance formula to find the current I:

    $I = V \cdot Y = (1 \angle 0^\circ) (-j\frac{1}{\omega L}) = j \frac{1}{\omega L} \angle -90^\circ$

**Common Pitfalls**
-------------------

*   Not converting the voltage source to phasor form.
*   Forgetting to find the admittance of the impedance Z.
*   Using the wrong formula for admittance.

**Quick Summary**
---------------

*   Convert the voltage source to phasor form.
*   Find the admittance of the impedance Z.
*   Use the admittance formula to find the current I.