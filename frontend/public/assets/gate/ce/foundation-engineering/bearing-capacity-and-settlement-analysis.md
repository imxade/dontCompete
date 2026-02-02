Bearing Capacity and Settlement Analysis
=====================================

### Introduction

Foundation engineering involves designing structures to transfer loads safely into the ground. The bearing capacity of a foundation determines its ability to resist vertical compressive stresses without failing. Settlement analysis assesses the deformation of the soil under load, ensuring it does not cause damage or unacceptable distortion.

### Core Concepts

#### Bearing Capacity

Bearing capacity is influenced by:

* Soil type (cohesion and friction)
* Load magnitude and distribution
* Depth and shape factors
* Inclination and eccentricity of loads

#### Settlement Analysis

Settlement is a function of:

* Effective stress increase
* Soil compressibility
* Pore water pressure change

### Key Formulas/Theorems

**Meyerhoff's Bearing Capacity Formula**

$$q_{c} = c \cdot N_c + q_N \cdot \gamma' \cdot N_q + 0.5 \cdot \gamma' \cdot b \cdot D \cdot N_\gamma$$

Where:

* $q_c$ is the bearing capacity
* $c$ is the cohesion of the soil
* $N_c$, $N_q$, and $N_\gamma$ are bearing capacity factors (given in question)
* $\gamma'$ is the effective unit weight of the soil
* $b$ is the width of the footing
* $D$ is the depth of the footing

**Consolidation Settlement Formula**

$$S_c = \frac{H}{1 + e} log\left( \frac{\sigma'}{\sigma''}\right)$$

Where:

* $S_c$ is the consolidation settlement
* $H$ is the thickness of the soil layer
* $e$ is the void ratio
* $\sigma'$ and $\sigma''$ are the effective stresses before and after loading, respectively

### Problem Solving Patterns

1. Identify the type of foundation (e.g., rectangular footing) and its dimensions.
2. Determine the bearing capacity factors for cohesion ($N_c$), friction ($N_q$), and density ($N_\gamma$).
3. Apply Meyerhoff's formula to calculate the bearing capacity $q_c$.
4. For settlement analysis, calculate the effective stress increase $\sigma'$.
5. Use the consolidation settlement formula to determine the expected settlement $S_c$.

### Examples with Solutions

**Example 1:**

A rectangular footing of size 2.8 m × 3.5 m is embedded in a clay layer with an eccentricity of 0.8 m.

* Calculate the bearing capacity using Meyerhoff's formula.
* Determine the expected settlement using the consolidation settlement formula.

Solution:

Bearing Capacity:
$$q_c = c \cdot N_c + q_N \cdot \gamma' \cdot N_q + 0.5 \cdot \gamma' \cdot b \cdot D \cdot N_\gamma$$
$$q_c = 40 kN/m^2 \cdot 5.14 + 18.2 kN/m^3 \cdot 1.0 \cdot 10^4 m^2 \cdot 1.0 + 0.5 \cdot 18.2 kN/m^3 \cdot 2.8 m \cdot 3.5 m \cdot 1.1$$
$$q_c = 205.6 + 2009.44 + 125.28$$
$$q_c = 2340 kPa$$

Settlement:
$$S_c = \frac{H}{1 + e} log\left( \frac{\sigma'}{\sigma''}\right)$$
Assuming $e$ = 0.5 and $\sigma'$ = $20 kN/m^2$, we have:
$$S_c = \frac{3 m}{1 + 0.5} log\left( \frac{20 kPa}{10 kPa}\right)$$
$$S_c = 4.44 mm$$

### Common Pitfalls

* Forgetting to apply depth, shape, and inclination factors in bearing capacity calculations.
* Incorrectly calculating the effective stress increase for settlement analysis.
* Not considering the influence of pore water pressure changes on consolidation settlement.

### Quick Summary

| Topic | Key Points |
| --- | --- |
| Bearing Capacity | Meyerhoff's formula, depth, shape, and inclination factors |
| Settlement Analysis | Consolidation settlement formula, effective stress increase, soil compressibility |

This comprehensive theory note provides a thorough understanding of bearing capacity and settlement analysis concepts. The examples with solutions demonstrate how to apply these principles to real-world problems, while the common pitfalls section highlights potential errors to avoid.