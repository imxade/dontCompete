# Radiation Pattern Theory Note
=====================================

## Introduction
---------------

Radiation pattern refers to the distribution of radiated power or electric field strength in space as a function of direction. It's an essential concept in electromagnetic theory, particularly when dealing with antennas and wave propagation.

## Core Concepts
-----------------

### 1. Directive Gain (Directivity)

Directive gain is a measure of the concentration of radiated power in a specific direction. It's defined as the ratio of the maximum power radiated per unit solid angle to the average power radiated per unit solid angle over all directions.

\[ D = \frac{4\pi}{\Omega} \]

where \( D \) is the directive gain and \( \Omega \) is the beam solid angle.

### 2. Electric Field in Free Space

The electric field strength in free space at a distance \( r \) from an antenna can be calculated using the formula:

\[ E = \frac{E_0}{r} e^{-j\beta r} \]

where $E$ is the electric field, $E_0$ is the maximum value of the electric field (at $r=0$), $\beta$ is the phase constant ($=\omega/c$, where $\omega$ is the angular frequency and $c$ is the speed of light).

### 3. Radiation Pattern

The radiation pattern is a graph that shows how the radiated power or electric field strength varies with direction.

## Key Formulas/Theorems
------------------------

\[ P_r = \frac{\lambda^2}{4\pi} |E|^2 A_e \]

where $P_r$ is the radiated power, $\lambda$ is the wavelength, $|E|$ is the magnitude of the electric field, and $A_e$ is the effective aperture.

## Problem Solving Patterns
---------------------------

1.  To find the amplitude of the electric field in free space at a distance $r$ from an antenna, we can use the formula:

    \[ E = \frac{E_0}{r} e^{-j\beta r} \]

2.  Given the directive gain and radiated power, we can calculate the beam solid angle using the formula:

    \[ D = \frac{4\pi}{\Omega} \]
3.  To find the maximum value of the electric field $E_0$, we need to know the radiated power, directional gain, and distance from the antenna.

## Examples with Solutions
---------------------------

### Example 1: Amplitude of Electric Field

An antenna has a directive gain of 6 dB and is radiating a total power of 16 kW. Find the amplitude of electric field in free space at a distance of 8 km from the antenna in the direction of 6 dB gain.

\[ D = 10 \log_{10} (P_r) - 20\log_{10} (\theta_{3dB}) \]
where $\theta_{3dB}$ is the half-power beamwidth.

Given:
- $D = 6$ dB
- $P_r = 16$ kW

\[ P_r = 10^{\frac{6}{10}} \times 16\]

The electric field can be found using:

\[ E = \sqrt{\frac{\eta}{\rho} \cdot \frac{4\pi}{D}} \sqrt{P_r} e^{-j\beta r} \]
where $\eta$ is the intrinsic impedance of free space, and $\rho$ is the distance from the antenna.

\[ E = \sqrt{\frac{120 \pi}{6 \times 16}} \cdot \sqrt{16000}\]

Simplifying,

\[ E \approx 0.2443\text{ V/m} \]

### Example 2: Beam Solid Angle

Given an antenna with a directive gain of 6 dB and radiating power of 16 kW, find the beam solid angle.

First, we find the maximum value of the electric field $E_0$:

\[ P_r = E_0^2 \cdot A_e \]

We can rearrange this to solve for $E_0$:

\[ E_0 = \sqrt{\frac{P_r}{A_e}} \]

Since we don't have $A_e$, we'll use the formula involving directive gain and radiated power instead.

## Common Pitfalls
-----------------

-   Not converting dB values to actual numbers when performing calculations.
-   Forgetting that radiation patterns are usually given as a function of the angle relative to the antenna's axis.
-   Assuming a linear relationship between electric field strength and distance without considering the effect of wavelength or phase constant.

## Quick Summary
---------------

-   **Radiation Pattern**: Describes how radiated power or electric field strength varies with direction.
-   **Directive Gain (Directivity)**: Concentration of radiated power in specific directions, defined as $\frac{4\pi}{\Omega}$.
-   **Electric Field in Free Space**: $E = \frac{E_0}{r} e^{-j\beta r}$.
-   **Radiation Pattern Formula**: $P_r = \frac{\lambda^2}{4\pi} |E|^2 A_e$.

This comprehensive theory note covers all key concepts related to radiation pattern, ensuring that students are well-prepared for the GATE CS exam.