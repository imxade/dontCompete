**Single Phase Transformer**
==========================

### Introduction
-----------------

A single-phase transformer is a type of electrical transformer that transfers electrical energy between two circuits through electromagnetic induction, but for only one phase. This note will cover the core concepts, key formulas, and problem-solving patterns required to tackle questions related to single-phase transformers.

### Core Concepts
------------------

#### Transformer Basics

A transformer consists of two coils: a primary coil (P) connected to the source circuit, and a secondary coil (S) connected to the load circuit. The transformer transfers energy from the primary coil to the secondary coil through electromagnetic induction.

*   Energy transfer occurs due to changes in magnetic flux between the coils.
*   The direction of energy flow is determined by the polarity of the coils.

#### Transformer Types

Based on the application and configuration, transformers can be classified into several types:

*   **Step-up transformer**: Increases voltage from primary to secondary.
*   **Step-down transformer**: Decreases voltage from primary to secondary.
*   **Isolation transformer**: Transfers energy while providing electrical isolation between primary and secondary circuits.

### Key Formulas/Theorems
-------------------------

#### Transformer Ratings

The ratings of a single-phase transformer are defined as follows:

*   **Apparent power** (S): $VA = V_P \times I_P = V_S \times I_S$
*   **Active power** (P): $P = \frac{V_P}{\sqrt{3}} \times I_P$ or $P = V_S \times I_S$

#### Transformer Efficiency

The efficiency of a transformer is given by:

$$\eta = \frac{P_{out}}{P_{in}} = 1 - \frac{P_{losses}}{P_{in}}$$

where $P_{losses}$ includes copper losses and iron losses.

### Problem Solving Patterns
-----------------------------

*   **OC (Open Circuit) Characteristics**: Measure the no-load voltage at various excitation levels.
    *   Plot a graph with excitation current on the x-axis and no-load voltage on the y-axis.
*   **SC (Short Circuit) Characteristics**: Measure the short-circuit current at different excitation levels.
    *   Plot a graph with excitation current on the x-axis and short-circuit current on the y-axis.

### Examples with Solutions
---------------------------

**Example 1: Calculating Transformer Rating**

A single-phase transformer has a primary voltage of 220 V and secondary voltage of 110 V. The rated power is 10 kW. Calculate the transformation ratio (a) and the turns ratio (n).

```latex
\text{Transformation Ratio} = \frac{V_S}{V_P} = \frac{110}{220} = 0.5

\text{Turns Ratio} = n = \sqrt{\frac{S}{P}} = \sqrt{\frac{10,000}{10,000}} = 1
```

**Example 2: Calculating Transformer Efficiency**

A single-phase transformer has a copper loss of 100 W and an iron loss of 200 W. Calculate the efficiency at full load.

```latex
\text{Efficiency} = \eta = 1 - \frac{P_{losses}}{P_{in}} = 1 - \frac{300}{10,000} = 0.97 or 97%
```

### Common Pitfalls
-------------------

*   Failing to account for iron losses in calculations.
*   Assuming the transformation ratio equals the turns ratio.
*   Not considering the direction of energy flow.

### Quick Summary
------------------

*   Single-phase transformers transfer energy between two circuits through electromagnetic induction.
*   Key formulas include transformer ratings, efficiency, and OC/SC characteristics.
*   Problem-solving patterns involve analyzing graphs and calculations.

Note: This note is focused on single-phase transformers. For questions related to three-phase transformers or other electrical machine topics, please refer to the relevant notes.