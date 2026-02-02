**Shear Strength of Soil**
=========================

### Introduction
The shear strength of soil is a critical parameter in geotechnical engineering, affecting the stability and safety of structures built on or within soil. The shear strength is determined by the ability of the soil to resist shear stresses, which are forces that cause the soil particles to slide past each other.

### Core Concepts

#### **Triaxial Test**
The triaxial test is a laboratory procedure used to determine the shear strength of soil. It involves applying confining pressure (σ3) and axial stress (σ1) to a cylindrical specimen, while measuring the resulting vertical strain and pore water pressure.

**Principle:** The Mohr-Coulomb failure criterion states that the shear strength of the soil is related to the normal stress and the angle of internal friction. For a drained triaxial test, the relationship can be expressed as:

$$\tau = c' + \sigma_n \tan \phi'$$

where τ is the shear stress, c' is the effective cohesion, σn is the normal stress, and φ' is the effective angle of internal friction.

#### **Pore Water Pressure**
During a triaxial test, pore water pressure (u) develops within the soil specimen due to the applied stresses. Skempton's pore pressure parameter (B) is defined as:

$$B = \frac{\Delta u}{\sigma_v}$$

where Δu is the change in pore water pressure and σv is the change in effective vertical stress.

### Key Formulas/Theorems

* Mohr-Coulomb failure criterion: τ = c' + σn tan φ'
* Skempton's pore pressure parameter (B): B = Δu / σv
* Effective cohesion (c'): related to the angle of internal friction and normal stress: c' = σn tan φ'

### Problem Solving Patterns

* **Drained Triaxial Test:** Use the Mohr-Coulomb failure criterion to determine the shear strength.
* **Consolidated Undrained (CU) Triaxial Test:** Calculate Skempton's pore pressure parameter (B) using the change in pore water pressure and effective vertical stress.

### Examples with Solutions

**Example 1: Drained Triaxial Test**

A drained triaxial test is conducted on a saturated sand specimen. The axial stress reaches a value of 2100 kN/m² from an initial confining pressure of 2300 kN/m². Determine the angle of shearing plane (in degrees) with respect to horizontal.

**Solution:**

* Normal stress (σn) = (2100 + 2300)/2 = 2200 kN/m²
* Angle of internal friction (φ') = arctan(c'/σn)
Assuming c' = 0 (sand), φ' ≈ 30°

**Example 2: Consolidated Undrained (CU) Triaxial Test**

A CU triaxial test is conducted on a soil sample. The cell pressure is increased from 20 kPa to 30 kPa, resulting in a pore water pressure of 1 kPa. At failure, the axial stress is 50 kPa, and the pore water pressure at failure is 21 kPa. Determine Skempton's pore pressure parameter (B).

**Solution:**

* Change in pore water pressure (Δu) = 21 - 1 = 20 kPa
* Effective vertical stress (σv) = (30 + 10)/2 = 20 kPa
* B ≈ Δu / σv = 20/20 = 1

### Common Pitfalls

* Forgetting to account for pore water pressure in CU triaxial tests.
* Misinterpreting the relationship between normal stress and effective cohesion.

### Quick Summary

* Triaxial test: determines shear strength of soil under different stresses.
* Drained triaxial test: uses Mohr-Coulomb failure criterion to determine shear strength.
* Consolidated undrained (CU) triaxial test: calculates Skempton's pore pressure parameter (B).
* Pore water pressure affects the shear strength of soil in CU triaxial tests.