**Distillation of Binary Mixtures**
=====================================

### Introduction
----------------

Binary mixture distillation involves separating two components, A and B, from a mixture based on their boiling points. The batch still is a widely used apparatus for this process. Understanding the principles behind binary mixture distillation is crucial in chemical engineering.

### Core Concepts
-----------------

#### Relative Volatility
--------------------

Relative volatility ($\alpha$) is a dimensionless quantity that represents the ratio of partial pressures of two components at their respective boiling points.

$\alpha = \frac{P_A}{P_B}$

where $P_A$ and $P_B$ are the partial pressures of components A and B, respectively.

#### Fenske-Underwood-Gilliland (FUG) Method
---------------------------------------------

The FUG method is used to calculate the number of theoretical plates required for separation. However, this topic will focus on a simpler approach using the Rayleigh equation.

### Key Formulas/Theorems
-------------------------

#### Rayleigh Equation
----------------------

$y_x = \frac{F}{F - W} (1 - y_{x+1})^{n-1}$

where:
* $y_x$: mole fraction of A in vapor at plate x
* $F$: feed rate
* $W$: withdrawal rate
* $y_{x+1}$: mole fraction of A in vapor at plate x + 1
* $n$: number of plates

#### Modified Rayleigh Equation for Batch Distillation
--------------------------------------------------------

$y_x = \frac{F}{F - W} (1 - y_{F})^{\alpha^{(W/F)}-1}$

where:
* $y_x$: mole fraction of A in vapor at plate x
* $F$: feed rate
* $W$: withdrawal rate
* $y_F$: initial mole fraction of A in feed

### Problem Solving Patterns
-----------------------------

To solve problems related to binary mixture distillation using the Rayleigh equation, follow these steps:

1.  Determine the initial and final compositions.
2.  Calculate the relative volatility ($\alpha$).
3.  Apply the modified Rayleigh equation to find the final composition.

### Examples with Solutions
---------------------------

**Example 1:**

Given:
*   Initial charge = 1 kmol
*   A in feed (initial) = 0.1 kmol
*   A in still (final) = 0.01 kmol
*   Relative volatility ($\alpha$) = 4.5

Find the mole fraction of B remaining in the vessel.

**Solution:**

Apply the modified Rayleigh equation:

$$y_x = \frac{F}{F - W} (1 - y_{F})^{\alpha^{(W/F)}-1}$$

where $y_F = 0.1$, $\alpha = 4.5$, and the final amount of A is 0.01 kmol.

$y_x = \frac{1}{1 - 0.01} (1 - 0.1)^{(4.5^{(0.01/1)}-1)}$

Simplifying, we get:

$y_x = 0.982$

### Common Pitfalls
-------------------

*   Failing to apply the correct formula based on the given conditions.
*   Incorrectly calculating the relative volatility or initial and final compositions.

### Quick Summary
-----------------

*   Relative volatility ($\alpha$) is a key concept in binary mixture distillation.
*   The modified Rayleigh equation can be used for batch distillation calculations.
*   Always verify the units and correctly apply the formulas.

Note: This theory note focuses on providing a high-yield, exam-focused study material. Practice problems and additional examples are recommended to reinforce understanding.