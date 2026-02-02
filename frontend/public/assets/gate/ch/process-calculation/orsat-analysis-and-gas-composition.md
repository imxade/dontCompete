**Orsat Analysis and Gas Composition**
=====================================

**Introduction**
---------------

Orsat analysis is a laboratory technique used to determine the composition of a gas mixture. It involves measuring the volume or pressure of each component in the mixture, allowing for the calculation of their respective mole fractions. This note will cover the principles of Orsat analysis and its application to determining gas composition.

**Core Concepts**
-----------------

### Principle of Orsat Analysis

Orsat analysis is based on the principle that each component in a gas mixture occupies a specific volume or pressure at equilibrium. By measuring the volume or pressure of each component, we can calculate their mole fractions using the ideal gas law:

$PV = nRT$

where $P$ is pressure, $V$ is volume, $n$ is the number of moles, $R$ is the gas constant, and $T$ is temperature in Kelvin.

### Humidity Measurement

Humidity measurement involves determining the mole fraction of water vapor in a gas mixture. This can be done using various techniques, including cooling the gas to condense the water vapor or measuring the change in pressure due to the presence of water vapor.

**Key Formulas/Theorems**
-------------------------

### Ideal Gas Law

$PV = nRT$

### Mole Fraction Calculation

Mole fraction is calculated as:

$\chi_i = \frac{n_i}{n_{total}}$

where $\chi_i$ is the mole fraction of component $i$, $n_i$ is the number of moles of component $i$, and $n_{total}$ is the total number of moles in the mixture.

**Problem Solving Patterns**
---------------------------

### Step 1: Calculate Total Number of Moles

Calculate the total number of moles in the gas mixture by summing the mole fractions of each component:

$n_{total} = \sum n_i$

### Step 2: Determine Humidity Measurement

Determine the mole fraction of water vapor in the gas mixture using the humidity measurement.

**Examples with Solutions**
---------------------------

### Example 1

A stack gas has a composition of 65 mol% $N_2$, 15 mol% CO, 10 mol% CO$_2$, and 10 mol% O$_2$. The humidity measurement reveals that the mole fraction of H$_2$O is 0.07. Calculate the mole fraction of N$_2$ on a wet basis.

Let's assume we have 100 moles of stack gas:

$n_{N_2} = 65$
$n_{CO} = 15$
$n_{CO_2} = 10$
$n_{O_2} = 10$

Total number of moles (dry):
$n_{total,dry} = n_{N_2} + n_{CO} + n_{CO_2} + n_{O_2} = 100$

Mole fraction of N$_2$ on a dry basis:
$\chi_{N_2,dry} = \frac{n_{N_2}}{n_{total,dry}} = \frac{65}{100} = 0.65$

Let $x$ be the number of moles of H$_2$O:

$n_{H_2O} = x$
$n_{total,wet} = n_{total,dry} + n_{H_2O} = 100 + x$

Mole fraction of N$_2$ on a wet basis:
$\chi_{N_2,wet} = \frac{n_{N_2}}{n_{total,wet}} = \frac{65}{100+x}$

Given the humidity measurement, we can set up an equation to solve for $x$:

$\frac{x}{100+x} = 0.07$
$x = \frac{7}{1-0.07} = 7.5268$

Now we can calculate the mole fraction of N$_2$ on a wet basis:

$\chi_{N_2,wet} = \frac{65}{100+7.5268} = \frac{65}{107.5268} = 0.6036 \approx 0.60$ (rounded to two decimal places)

### Example 2

A gas mixture has the following composition: 50 mol% CH$_4$, 20 mol% CO, and 30 mol% H$_2$. The humidity measurement reveals that the mole fraction of H$_2$O is 0.03. Calculate the mole fraction of CO on a wet basis.

Let's assume we have 100 moles of gas mixture:

$n_{CH_4} = 50$
$n_{CO} = 20$
$n_{H_2} = 30$

Total number of moles (dry):
$n_{total,dry} = n_{CH_4} + n_{CO} + n_{H_2} = 100$

Mole fraction of CO on a dry basis:
$\chi_{CO,dry} = \frac{n_{CO}}{n_{total,dry}} = \frac{20}{100} = 0.2$

Let $x$ be the number of moles of H$_2$O:

$n_{H_2O} = x$
$n_{total,wet} = n_{total,dry} + n_{H_2O} = 100+x$

Mole fraction of CO on a wet basis:
$\chi_{CO,wet} = \frac{n_{CO}}{n_{total,wet}} = \frac{20}{100+x}$

Given the humidity measurement, we can set up an equation to solve for $x$:

$\frac{x}{100+x} = 0.03$
$x = \frac{3}{1-0.03} = 3.0303$

Now we can calculate the mole fraction of CO on a wet basis:

$\chi_{CO,wet} = \frac{20}{100+3.0303} = \frac{20}{103.0303} = 0.1944 \approx 0.19$ (rounded to two decimal places)

**Common Pitfalls**
------------------

*   Forgetting to account for the humidity measurement in calculations.
*   Not using the correct formula for calculating mole fraction on a wet basis.
*   Rounding errors when solving for $x$.

**Quick Summary**
-----------------

| Concept | Formula/Equation |
| --- | --- |
| Ideal Gas Law | $PV = nRT$ |
| Mole Fraction Calculation | $\chi_i = \frac{n_i}{n_{total}}$ |
| Humidity Measurement | $\frac{x}{100+x} = 0.07$ |

This comprehensive theory note covers the principles of Orsat analysis, gas composition, and problem-solving patterns for the given topic. It includes step-by-step examples, key formulas, and common pitfalls to help students master this subject.