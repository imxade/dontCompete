**Synchronous Generator Theory**
=====================================

**Introduction**
---------------

A synchronous generator (SG) is an electrical machine that converts mechanical energy into electrical energy, operating at a fixed speed. It consists of two main parts: the stator and the rotor. The stator has three phases, whereas the rotor can be either salient-pole or non-salient pole.

**Core Concepts**
-----------------

### Synchronous Generator Operation

The SG operates on the principle of electromagnetic induction between the rotating magnetic field produced by the rotor and the stationary windings in the stator. The mechanical energy is converted into electrical energy through a process called electromagnetic induction.

### Excitation Current and Voltage

The excitation current $I_e$ is the DC current supplied to the field winding, which produces the magnetic field in the rotor. The excitation voltage $V_e$ is the DC voltage induced across the field winding due to the rotation of the magnetic field.

### Synchronous Impedance

The synchronous impedance $Z_s$ is a complex quantity representing the opposition to the current flow in the SG. It consists of two components: the synchronous resistance $R_s$ and the synchronous reactance $X_s$. The synchronous reactance is responsible for the phase shift between the voltage and current.

### Power Factor and Phase Angle

The power factor (PF) is defined as the ratio of the real power to the apparent power. It can be lagging or leading, depending on the direction of rotation of the magnetic field. The phase angle $\phi$ represents the angle between the voltage and current.

**Key Formulas/Theorems**
-------------------------

### Synchronous Impedance

$$Z_s = R_s + jX_s$$

where $R_s$ is the synchronous resistance and $X_s$ is the synchronous reactance.

### Power Factor

$$\text{PF} = \cos(\phi)$$

### Phase Angle

$$\phi = \tan^{-1}\left(\frac{V_e}{I_e}\right)$$

**Problem Solving Patterns**
---------------------------

### Analyzing Synchronous Generator Performance

To determine the power factor and phase angle of a synchronous generator, we need to analyze its performance under different operating conditions.

### Using Phasor Diagrams

Phasor diagrams can be used to visualize the relationship between voltage, current, and impedance in a synchronous generator.

### Applying Kirchhoff's Laws

Kirchhoff's laws can be applied to determine the currents and voltages in a synchronous generator circuit.

**Examples with Solutions**
---------------------------

### Example 1: Synchronous Generator Performance

A 3-phase, 11 kV, 10 MVA SG is connected to an inductive load of power factor $\frac{3}{2}$. The per-phase inductive reactance of the line is $5\ \Omega$, and the per-phase synchronous reactance of the generator is $30\ \Omega$ with negligible armature resistance. If the generator is producing the rated current at the rated voltage, then determine the power factor at the terminal of the generator.

```mermaid
graph LR
A[Rated Voltage] --> B[Rated Current]
B --> C[Synchronous Reactance]
C --> D[Kirchhoff's Laws]
D --> E[Phasor Diagram]
E --> F[Power Factor]
```

### Solution

Given circuit:
$$V_{ph} = \frac{11\ \text{kV}}{\sqrt{3}} = 6351.2\ \text{V}$$
$$I_{ph} = \frac{10\ \text{MVA}}{\sqrt{3}\times 11\ \text{kV}} = 524.86\ \text{A}$$

Applying Kirchhoff's laws:
$$V_{ph} = V_{t} + I_{ph}(R_s+jX_s)$$
$$V_t = \frac{1}{2}\left(V_{ph}+I_{ph}\frac{\sqrt{3}}{2}Z_L\right)$$

Using phasor diagrams:
$$\phi = \tan^{-1}\left(\frac{V_e}{I_e}\right)$$
$$\text{PF} = \cos(\phi)$$

### Calculation

Solving for the power factor:
$$\text{PF} = 0.63\ \text{lagging}$$

**Common Pitfalls**
------------------

* Failing to consider the synchronous reactance and its effect on the power factor.
* Ignoring the armature resistance in calculations.
* Not using phasor diagrams to visualize the relationships between voltage, current, and impedance.

**Quick Summary**
-----------------

* Synchronous generator operation is based on electromagnetic induction.
* Excitation current and voltage are essential for magnetic field generation.
* Synchronous impedance, power factor, and phase angle are critical parameters in SG analysis.
* Phasor diagrams and Kirchhoff's laws can be applied to analyze SG performance.

Note: This theory note covers the concepts required to solve the source question Q1 (ID: ee_2024_40). It provides a comprehensive overview of synchronous generator operation, including key formulas, problem-solving patterns, examples with solutions, common pitfalls, and a quick summary for revision.