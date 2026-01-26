# psm stability
## Introduction
Power System Stability (PSM) refers to the ability of a power system to withstand disturbances, such as faults or changes in load, without losing its equilibrium. The stability of a power system is crucial for maintaining reliable and efficient operation.

## Core Concepts
### Power Angle Curve
The power angle curve describes the relationship between the power output of a generator and its load angle ($\delta$). Mathematically, it can be represented as:
\[ P(\delta) = \frac{E^2}{X} \sin(\delta) \]
where $P(\delta)$ is the power output at load angle $\delta$, $E$ is the voltage behind the generator, and $X$ is the reactance of the transmission line.

### Critical Fault Clearing Angle
The critical fault clearing angle ($\delta_c$) is the minimum load angle required for a fault to be cleared by opening a line. This angle determines the maximum allowable power output during a fault.

## Key Formulas/Theorems

\[ P_{max} = \frac{E^2}{X} \]
\[ P(\delta) = \frac{P_{max}}{\sin(\delta_c)} \sin(\delta) \]

## Problem Solving Patterns
### Fault Clearance
When a fault occurs on a line, the power output of the generator decreases. The critical fault clearing angle determines when the fault can be cleared by opening the line.

## Examples with Solutions

**Q1:**
Given that the mechanical input power is $0.5 P_{max}$ and the power output during the fault is $\frac{P_{max}}{2} \sin(\delta)$, determine the accelerating area on the power angle curve.
### Solution
First, we need to find the maximum load angle ($\delta_{max}$) when the fault occurs:
\[ 0.5 P_{max} = \frac{E^2}{X} \sin(\delta_{max}) \]
Solving for $\delta_{max}$ gives us:
\[ \delta_{max} = \sin^{-1}\left( \frac{0.5 E^2}{P_{max} X} \right) \]
Next, we need to find the load angle ($\delta_f$) when the fault is cleared:
\[ P(\delta_f) = 0.5 P_{max} \]
Substituting $P(\delta_f)$ into the power angle equation gives us:
\[ \frac{E^2}{X} \sin(\delta_f) = 0.5 P_{max} \]
Solving for $\delta_f$ gives us:
\[ \delta_f = \sin^{-1}\left( \frac{P_{max}}{2 E^2/X} \right) \]
The accelerating area on the power angle curve is given by:
\[ A = \int_{\delta_c}^{\delta_{max}} P(\delta) d\delta - \int_{0}^{\delta_f} P(\delta) d\delta \]
Substituting $P(\delta)$ and evaluating the integrals gives us:
\[ A = \frac{E^2}{X} \left[ -\cos(\delta_{max}) + \cos(\delta_c) + \cos(\delta_f) \right] \]

## Common Pitfalls

* Failing to account for the critical fault clearing angle ($\delta_c$)
* Incorrectly calculating the maximum load angle ($\delta_{max}$) during the fault
* Not considering the effect of the fault on the power output and load angle

## Quick Summary

* Power System Stability (PSM) refers to the ability of a power system to withstand disturbances without losing equilibrium.
* The critical fault clearing angle determines when a fault can be cleared by opening a line.
* The accelerating area on the power angle curve is given by integrating $P(\delta)$ between $\delta_c$ and $\delta_{max}$.

Please note that this is just an initial draft. You may need to modify it based on your specific requirements or any additional information you have about the topic.