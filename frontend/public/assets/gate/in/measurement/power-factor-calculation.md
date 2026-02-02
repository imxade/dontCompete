**Power Factor Calculation**
==========================

### Introduction

Power factor (PF) is a measure of how effectively an AC power system uses the available voltage to produce useful work. It is defined as the ratio of true power (P) to apparent power (S). In this theory note, we will cover the calculation of power factor and its significance in electrical measurements.

### Core Concepts

#### True Power (P)

True power, also known as real power, is the actual power consumed by a load. It is measured in watts (W).

```latex
P = V_{rms} \times I_{rms} \times \cos(\phi)
```

where $V_{rms}$ is the root mean square voltage, $I_{rms}$ is the root mean square current, and $\cos(\phi)$ is the power factor angle.

#### Apparent Power (S)

Apparent power is the vector sum of true power and reactive power. It is measured in volt-amperes (VA).

```latex
S = V_{rms} \times I_{rms}
```

#### Power Factor

Power factor is defined as the ratio of true power to apparent power.

```latex
PF = \frac{P}{S} = \cos(\phi)
```

### Key Formulas/Theorems

* True power (P) can be calculated using the formula: $P = V_{rms} \times I_{rms} \times \cos(\phi)$
* Apparent power (S) can be calculated using the formula: $S = V_{rms} \times I_{rms}$
* Power factor (PF) is defined as the ratio of true power to apparent power: $PF = \frac{P}{S} = \cos(\phi)$

### Problem Solving Patterns

When solving problems involving power factor calculation, follow these steps:

1. Identify the given values: voltage, current, and power.
2. Calculate true power (P) using the formula: $P = V_{rms} \times I_{rms} \times \cos(\phi)$
3. Calculate apparent power (S) using the formula: $S = V_{rms} \times I_{rms}$
4. Calculate power factor (PF) by dividing true power by apparent power: $PF = \frac{P}{S}$

### Examples with Solutions

**Example 1**

Given:

* Voltage ($V_{rms}$): 100 V ± 1%
* Current ($I_{rms}$): 1 A ± 1%
* Power ($W$): 50 W ± 2%

Calculate the power factor.

```latex
P = V_{rms} \times I_{rms} \times \cos(\phi) = 100 \, \text{V} \times 1 \, \text{A} \times \cos(\phi)
S = V_{rms} \times I_{rms} = 100 \, \text{V} \times 1 \, \text{A}
PF = \frac{P}{S} = \cos(\phi) = \frac{50}{\sqrt{(100^2 + (1)^2)}} = 0.998
```

The power factor is approximately 0.998.

**Example 2**

Given:

* Voltage ($V_{rms}$): 200 V ± 1%
* Current ($I_{rms}$): 2 A ± 1%
* Power ($W$): 100 W ± 2%

Calculate the power factor.

```latex
P = V_{rms} \times I_{rms} \times \cos(\phi) = 200 \, \text{V} \times 2 \, \text{A} \times \cos(\phi)
S = V_{rms} \times I_{rms} = 200 \, \text{V} \times 2 \, \text{A}
PF = \frac{P}{S} = \cos(\phi) = \frac{100}{\sqrt{(200^2 + (2)^2)}} = 0.995
```

The power factor is approximately 0.995.

### Common Pitfalls

* Failing to calculate apparent power correctly.
* Not considering the percentage errors in voltage, current, and power measurements.
* Using incorrect values for true power or apparent power.

### Quick Summary

* Power factor (PF) is defined as the ratio of true power (P) to apparent power (S): $PF = \frac{P}{S}$
* True power (P) can be calculated using the formula: $P = V_{rms} \times I_{rms} \times \cos(\phi)$
* Apparent power (S) can be calculated using the formula: $S = V_{rms} \times I_{rms}$
* Percentage errors in voltage, current, and power measurements must be considered when calculating power factor.