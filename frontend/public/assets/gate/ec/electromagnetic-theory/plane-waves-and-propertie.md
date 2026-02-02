# Plane Waves and Properties
==========================

## Introduction
---------------

Plane waves are a fundamental concept in electromagnetic theory, describing waves that propagate through space with minimal distortion. They play a crucial role in understanding various phenomena, from radio wave propagation to optical communication systems.

## Core Concepts
-----------------

### Electromagnetic Spectrum

The electromagnetic spectrum consists of various types of waves, including:

*   Radio waves (long wavelength, low frequency)
*   Microwaves (medium wavelength, medium frequency)
*   Infrared waves (short wavelength, high frequency)
*   Visible light (very short wavelength, very high frequency)
*   Ultraviolet waves (even shorter wavelength, even higher frequency)

### Plane Waves

Plane waves are a special case of electromagnetic waves where the electric and magnetic field components are perpendicular to each other and the direction of propagation.

### Phase Velocity

Phase velocity is the speed at which the phase of a wave propagates through a medium. It can be calculated using the formula:

$$v_p = \frac{\omega}{k}$$

where $\omega$ is the angular frequency and $k$ is the wavenumber.

### Group Velocity

Group velocity is the speed at which the energy of a wave propagates through a medium. It can be calculated using the formula:

$$v_g = \frac{d\omega}{dk}$$

## Key Formulas/Theorems
-------------------------

*   **Wave Impedance**: The ratio of the electric field to the magnetic field in a plane wave.

    $$Z = \sqrt{\frac{\mu_0}{\epsilon_0}}$$

*   **Speed of Light**: The speed at which electromagnetic waves propagate through a vacuum.

    $$c = \frac{1}{\sqrt{\mu_0 \epsilon_0}}$$

## Problem Solving Patterns
---------------------------

### Identifying Dominant Mode

To identify the dominant mode in a waveguide, we need to find the cut-off frequency for each mode and compare it with the operating frequency.

*   If the operating frequency is greater than the cut-off frequency, the mode is not excited.
*   If the operating frequency is equal to the cut-off frequency, the mode is excited, but only at the cut-off frequency.
*   If the operating frequency is less than the cut-off frequency, the mode is not excited.

### Calculating Phase Velocity

To calculate the phase velocity of a plane wave, we need to use the formula:

$$v_p = \frac{\omega}{k}$$

## Examples with Solutions
---------------------------

### Example 1: Calculating Cut-off Frequency

A rectangular waveguide has dimensions $a = 8$ cm and $b = 4$ cm. The operating frequency is 3.4 GHz. Find the cut-off frequency for the dominant mode.

```python
import math

# Given values
a = 8e-2  # meters
b = 4e-2  # meters
f = 3.4e9  # Hz

# Calculate cut-off frequency
fc = (1 / (2 * math.sqrt(2))) * (f * math.sqrt(a**2 + b**2))
print("Cut-off frequency: ", fc, "Hz")
```

### Example 2: Calculating Phase Velocity

A plane wave has an angular frequency of $\omega = 2\pi \times 10^9$ rad/s and a wavenumber of $k = 2\pi / \lambda$. Find the phase velocity.

```python
import math

# Given values
omega = 2 * math.pi * 1e9  # rad/s
k = 2 * math.pi / 3e-8  # rad/m

# Calculate phase velocity
vp = omega / k
print("Phase velocity: ", vp, "m/s")
```

## Common Pitfalls
------------------

*   Failing to identify the dominant mode in a waveguide.
*   Calculating phase velocity using the wrong formula.

## Quick Summary
---------------

*   Plane waves are electromagnetic waves with minimal distortion.
*   Phase velocity is the speed at which the phase of a wave propagates through a medium.
*   Group velocity is the speed at which energy propagates through a medium.
*   Wave impedance is the ratio of electric to magnetic field in a plane wave.

### References

[1] "Electromagnetic Theory" by David K. Cheng

[2] "Wave Propagation and Antennas" by John D. Kraus