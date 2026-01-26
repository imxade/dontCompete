**Fick's Law of Mass Transfer**
=============================

### Introduction

Fick's law describes the rate at which a substance diffuses through a medium, driven by a concentration gradient. This fundamental principle underlies many mass transfer processes, including gas-liquid and liquid-liquid extraction.

### Core Concepts

#### Diffusion Coefficient

The diffusion coefficient (D) is a measure of how easily a substance can move through a medium. It depends on the physical properties of the substance and the medium, such as temperature, pressure, and molecular weight.

LaTeX:
\[ D = \frac{k}{C} \]

where k is a constant and C is the concentration of the substance.

#### Concentration Gradient

The concentration gradient (dC/dx) is the change in concentration with respect to distance. It drives the diffusion process, as molecules tend to move from areas of high concentration to areas of low concentration.

LaTeX:
\[ \frac{dC}{dx} = -\frac{k}{D} \]

where k is a constant and D is the diffusion coefficient.

### Key Formulas/Theorems

**Fick's Law**

LaTeX:
\[ J = -D \frac{dC}{dx} \]

where J is the flux of the substance, D is the diffusion coefficient, and dC/dx is the concentration gradient.

#### Mass Transfer Coefficient

The mass transfer coefficient (k) relates the rate of mass transfer to the driving force (concentration difference).

LaTeX:
\[ k = \frac{D}{\Delta x} \]

where Δx is the thickness of the boundary layer.

### Problem Solving Patterns

1. **Identify the diffusion process**: Determine whether it's a gas-liquid, liquid-liquid, or solid-gas process.
2. **Determine the driving force**: Identify the concentration gradient or pressure difference that drives the mass transfer process.
3. **Apply Fick's Law**: Use the formula J = -D dC/dx to relate the flux of the substance to the diffusion coefficient and concentration gradient.

### Examples with Solutions

**Example 1:**

A gas flows over a liquid film, causing the solute to diffuse into the liquid. The concentration of the solute in the gas is 0.5 mol/m³, and the concentration in the liquid is 0.2 mol/m³. If the diffusion coefficient is 10⁻⁵ m²/s, what is the rate of mass transfer?

LaTeX:
\[ J = -D \frac{dC}{dx} = -(10^{-5}) \frac{(0.5-0.2)}{1} = 3 \times 10^{-6} \, \text{mol/m²s} \]

**Example 2:**

A liquid flows through a packed tower, stripping a solute from the gas phase. The Henry's law constant is 10⁻³ Pa/m³. If the mole fraction of the solute in the gas phase is 0.1, what is the rate of mass transfer?

LaTeX:
\[ J = y m P \]

where y is the mole fraction of the solute in the gas phase, m is Henry's law constant, and P is the pressure.

### Common Pitfalls

* Failing to identify the diffusion process
* Ignoring the concentration gradient or driving force
* Using incorrect units for the diffusion coefficient or mass transfer coefficient

### Quick Summary

* **Diffusion Coefficient**: Measure of how easily a substance can move through a medium.
* **Concentration Gradient**: Change in concentration with respect to distance, drives diffusion process.
* **Fick's Law**: Relates flux of substance to diffusion coefficient and concentration gradient.
* **Mass Transfer Coefficient**: Relates rate of mass transfer to driving force (concentration difference).

**Mermaid Diagram:**
```mermaid
graph LR
A[Diffusion Process] --> B[Concentration Gradient]
B --> C[Fick's Law]
C --> D[Mass Transfer Coefficient]
D --> E[Rate of Mass Transfer]
