**Inductor and Capacitor Q Factor**
=====================================

### Introduction
The Q factor of an inductor or capacitor is a measure of its quality, specifically its ability to store energy. In this note, we'll cover the theoretical concepts, formulas, and insights required to solve questions related to the Q factors of inductors and capacitors.

### Core Concepts
#### Inductor Q Factor

The Q factor of an inductor is defined as the ratio of its inductive reactance to its resistance:

$$Q_{L} = \frac{\omega L}{R}$$

where $ω$ is the angular frequency, $L$ is the inductance, and $R$ is the resistance.

#### Capacitor Q Factor

The Q factor of a capacitor is defined as the ratio of its capacitive reactance to its resistance:

$$Q_{C} = \frac{\omega C}{G}$$

where $\omega$ is the angular frequency, $C$ is the capacitance, and $G$ is the conductance.

### Key Formulas/Theorems
When an inductor and a capacitor are connected in series, their Q factors can be combined using the following formula:

$$Q_{\text{total}} = \frac{1}{\frac{1}{Q_{L}} + \frac{1}{Q_{C}}}$$

This formula allows us to calculate the overall Q factor of the circuit.

### Problem Solving Patterns
When solving questions related to inductor and capacitor Q factors, follow these steps:

1. Identify the individual Q factors of the inductor and capacitor.
2. Apply the formula for combining the Q factors to find the overall Q factor.
3. Round off the result to the nearest integer (if required).

### Examples with Solutions

**Example 1**

An inductor has a Q factor of 60, and a capacitor has a Q factor of 240. Find the overall Q factor of the circuit.

```mermaid
graph LR
A[Q_L = 60] --> B[Q_C = 240]
B --> C[Q_total = 1 / (1/60 + 1/240)]
C --> D{Final Answer}
```

Solution:

$Q_{\text{total}} = \frac{1}{\frac{1}{60} + \frac{1}{240}}$

$= \frac{1}{\frac{4}{240} + \frac{1}{240}}$

$= \frac{1}{\frac{5}{240}}$

$= 48$

**Example 2**

A circuit has an inductor with a Q factor of 120 and a capacitor with a Q factor of 360. What is the overall Q factor?

Solution:

Using the formula, we get:

$Q_{\text{total}} = \frac{1}{\frac{1}{120} + \frac{1}{360}}$

$= \frac{1}{\frac{3}{360} + \frac{1}{360}}$

$= \frac{1}{\frac{4}{360}}$

$= 90$

### Common Pitfalls

* Students often forget to round off the result to the nearest integer (if required).
* When combining Q factors, they may incorrectly add or subtract the reciprocals instead of using the correct formula.

### Quick Summary
* The Q factor of an inductor is given by $Q_{L} = \frac{\omega L}{R}$.
* The Q factor of a capacitor is given by $Q_{C} = \frac{\omega C}{G}$.
* The overall Q factor of a circuit with an inductor and a capacitor in series is given by $Q_{\text{total}} = \frac{1}{\frac{1}{Q_{L}} + \frac{1}{Q_{C}}}$.

I hope this comprehensive theory note helps you tackle questions related to inductor and capacitor Q factors!