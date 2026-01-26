# AC Circuits and Power - Measurement Theory Note
## Introduction
AC circuits are a fundamental aspect of electrical engineering, and understanding their behavior is crucial for designing and analyzing power systems. In this note, we will focus on the measurement of AC circuits, specifically reactive power.

## Core Concepts
### True Power vs Reactive Power
True power (P) represents the actual power consumed by a circuit, while reactive power (Q) represents the power that flows back and forth between the source and the load due to the inductive or capacitive nature of the circuit. In an AC circuit, true power is given by $P = VI \cos{\phi}$, where V is the root mean square (rms) voltage, I is the rms current, and $\phi$ is the phase angle between V and I.

### Phase Angle
The phase angle ($\phi$) between V and I is a measure of the circuit's power factor. A pure resistive load has a phase angle of 0°, while a pure inductive or capacitive load has an infinite phase angle. The power factor (PF) is given by $\cos{\phi}$.

## Key Formulas/Theorems
* True Power: $P = VI \cos{\phi}$
* Reactive Power: $Q = V I \sin{\phi}$
* Power Factor: $PF = \cos{\phi}$
* Phase Angle: $\tan{\phi} = \frac{V_{L}}{I_{L}}$ for a purely inductive or capacitive load

## Problem Solving Patterns
To solve problems involving AC circuits and measurement, follow these steps:

1. Calculate the true power (P) using the formula $P = VI \cos{\phi}$.
2. If given the reactive power (Q), use it to find the phase angle ($\phi$) with the equation $\tan{\phi} = \frac{Q}{P}$.
3. Use the phase angle to find the power factor (PF) using $\cos{\phi}$.

## Examples with Solutions

### Example 1:
A household fan consumes 60 W and draws a current of 0.3125 A (rms) when connected to a 230 V (rms) AC, 50 Hz single-phase mains. Find the reactive power drawn by the fan in VAR.

```latex
\begin{aligned}
P &= VI \cos{\phi} \\
&= 60 W
\end{aligned}

\begin{aligned}
I_{rms} &= 0.3125 A
\\
V_{rms} &= 230 V
\\
\cos{\phi} &= \frac{P}{VI} = \frac{60}{230 \times 0.3125} = 0.835 \\
\tan{\phi} &= \sqrt{\left(\frac{1}{\cos^2{\phi}} - 1\right)} = \sqrt{\left(\frac{1}{(0.835)^2} - 1\right)} = 1.034
\\
Q &= V I \sin{\phi} \\
&= 230 \times 0.3125 \times \tan^{-1}(1.034) \\
&= 39.53 VAR
\end{aligned}
```

## Common Pitfalls

* Confusing true power (P) with reactive power (Q).
* Not considering the phase angle ($\phi$) when calculating reactive power.
* Misapplying the formulas for AC circuits.

## Quick Summary

| Concept | Formula |
| --- | --- |
| True Power | $P = VI \cos{\phi}$ |
| Reactive Power | $Q = V I \sin{\phi}$ |
| Phase Angle | $\tan{\phi} = \frac{V_{L}}{I_{L}}$ for a purely inductive or capacitive load |
| Power Factor | $PF = \cos{\phi}$ |

Note: This note covers the concepts and formulas required to solve GATE 2021, Q5. It is essential to practice solving similar problems to reinforce understanding.