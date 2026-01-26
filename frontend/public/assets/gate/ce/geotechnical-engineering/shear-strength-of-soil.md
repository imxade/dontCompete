**Shear Strength of Soil**
=========================

### Introduction
The shear strength of soil is a critical parameter in geotechnical engineering, particularly for design and analysis of various structures such as foundations, tunnels, and slopes. The shear strength of soil depends on several factors including the effective stress, friction angle, and cohesion.

### Core Concepts
The shear strength of soil can be determined using various methods, including:

* **Triaxial Compression Test**: This test is widely used to determine the shear strength of soil. In this test, a cylindrical sample of soil is subjected to a confining pressure (σ3) and then sheared along its axis until failure occurs.
* **Drained Triaxial Test**: In this type of test, the soil sample is allowed to drain freely during the shearing process. This helps to eliminate the effects of pore water pressure on the shear strength of the soil.
* **Consolidated Undrained (CU) Triaxial Test**: In this type of test, the soil sample is consolidated under a confining pressure for a specified period before being subjected to shearing.

### Key Formulas/Theorems

The shear strength of soil can be calculated using the following formulas:

* **Mohr-Coulomb Failure Criterion**:

$$\tau = c' + \sigma_n \tan \phi'$$

where $\tau$ is the shear stress, $c'$ is the effective cohesion, $\sigma_n$ is the normal stress, and $\phi'$ is the effective friction angle.

* **Effective Stress Law**:

$$p' = p - u$$

where $p'$ is the effective confining pressure, $p$ is the total confining pressure, and $u$ is the pore water pressure.

* **Skempton's Pore Pressure Parameter (B)**:

$$B = \frac{Δu}{σ_3}$$

where $Δu$ is the change in pore water pressure and $σ_3$ is the effective confining pressure.

### Problem Solving Patterns
When solving problems related to shear strength of soil, follow these steps:

1. Determine the type of test (drained or consolidated undrained) and the conditions under which it was conducted.
2. Identify the relevant parameters (effective cohesion, friction angle, pore water pressure, etc.) that affect the shear strength of the soil.
3. Apply the appropriate formulas and theorems to calculate the shear strength of the soil.

### Examples with Solutions

**Example 1**

A consolidated undrained triaxial test was conducted on a saturated clay sample. The confining pressure was 200 kPa, and the pore water pressure at failure was recorded as 50 kPa. Calculate the Skempton's pore pressure parameter (B) for the soil sample.

```latex
Δu = 50 - 0 = 50 \text{ kPa}
σ_3 = 200 \text{ kPa}
B = \frac{Δu}{σ_3} = \frac{50}{200} = 0.25
```

**Example 2**

A drained triaxial test was conducted on a saturated sand sample. The confining pressure was 300 kN/m², and the axial stress at failure was recorded as 2100 kN/m². Calculate the angle of shearing plane (in degrees) with respect to horizontal.

```latex
τ = \frac{2}{3} \sigma_1' = \frac{2}{3} \times 2100 = 1400 \text{ kPa}
\phi' = \arctan \left( \frac{\tau - c'}{\sigma_n} \right) = \arctan \left( \frac{1400}{300} \right)
= 58.19^\circ
```

### Common Pitfalls

* Students often forget to consider the effects of pore water pressure on the shear strength of soil.
* Inconsistent units and dimensions can lead to errors in calculations.

### Quick Summary
Key concepts:

* Triaxial compression test, drained triaxial test, and consolidated undrained (CU) triaxial test
* Mohr-Coulomb failure criterion, effective stress law, and Skempton's pore pressure parameter (B)
* Formulas for calculating shear strength of soil

```mermaid
graph LR
  A[Shear Strength of Soil] --> B[Triaxial Compression Test]
  C[Drained Triaxial Test] --> D[Coefficients of Friction Angle and Cohesion]
  E[Consolidated Undrained (CU) Triaxial Test] --> F[Pore Water Pressure Effects]
