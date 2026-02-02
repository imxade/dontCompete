# Air Pollution: Environmental Engineering Theory Note
==============================================

## Introduction

Air pollution is a significant environmental issue that affects both human health and ecosystems worldwide. Understanding the principles of air pollution is crucial for assessing compliance with emissions standards, mitigating its effects, and protecting public health.

## Core Concepts

### Atmospheric Dispersion of Pollutants

Pollutants released into the atmosphere can be dispersed through various mechanisms:

* **Advection**: horizontal movement due to winds
* **Diffusion**: random movement due to molecular interactions
* **Dispersion**: large-scale mixing due to wind shear and turbulence

### Emissions Standards

Emissions standards regulate the amount of pollutants released by industrial sources. These standards are typically expressed in terms of concentration (mg/Nm3) or mass flow rate.

## Key Formulas/Theorems

LaTeX:
```latex
\text{Stoichiometric Air Requirement} = \frac{\text{Fuel Mass Flow Rate}}{\text{Air Mass Flow Rate}}
```
### Stoichiometric Air Requirement

The stoichiometric air requirement is calculated using the mass balance equation:

$$\text{Fuel Mass Flow Rate} = \text{Oxygen Mass Flow Rate} + \text{Nitrogen Mass Flow Rate} + \text{Other Inerts Mass Flow Rate}$$

## Problem Solving Patterns

### Assessing Compliance with Emissions Standards

To assess compliance, the measured concentration of pollutants must be corrected to account for deviations from standard conditions (e.g., oxygen content).

### Calculating Stoichiometric Air Requirement

When given the composition of fuel and combustion products, calculate the stoichiometric air requirement using the mass balance equation.

## Examples with Solutions

### Example 1: Assessing Compliance with Emissions Standards

Given:
* Measured HCl concentration = 42 mg/Nm3
* Measured O2 concentration = 13%
* Emission standard for HCl (11% O2) = 50 \* 10^3 mg/Nm3

Solution:

$$\text{Corrected HCl emission} = \frac{\text{Meas. HCl}}{\text{Meas. O2}} \times 0.11$$
$$= \frac{42}{13} \times 50,000 = 25,000 \text{ mg/Nm3} > 50,000 \text{ mg/Nm3}$$

No compliance.

### Example 2: Calculating Stoichiometric Air Requirement

Given:
* Fuel composition: C = 35%, O2 = 26%, H2 = 10%, S = 6%, N2 = 3%
* Burning rate = 1000 tonnes/d
* Atomic weights: H = 1, C = 12, N = 14, O = 16, S = 32

Solution:

First, calculate the mass balance equation for each element:

$$\text{C: } 35 \times 10^3 = \frac{2}{22.4} \times \text{Air Mass Flow Rate}$$
$$= \frac{1}{0.21} \times \text{Oxygen Mass Flow Rate} + ...$$

Using the mass balance equation, calculate the stoichiometric air requirement:

$$\text{Stoichiometric Air Requirement} = \frac{\text{Fuel Mass Flow Rate}}{\text{Air Mass Flow Rate}}$$
$$= \frac{1000}{6965} \approx 1.43 \times 10^3 \text{ tonnes/d}$$

## Common Pitfalls

* Failing to account for deviations from standard conditions when assessing compliance with emissions standards.
* Incorrectly calculating the stoichiometric air requirement.

## Quick Summary
### Key Concepts:

* Atmospheric dispersion of pollutants
* Emissions standards
* Stoichiometric air requirement

### Formulas/Theorems:

* Stoichiometric Air Requirement formula
* Mass balance equation for each element