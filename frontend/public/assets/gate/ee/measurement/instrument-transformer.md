**Instrument Transformers**
==========================

**Introduction**
---------------

Instrument transformers are crucial components in electrical measurement systems. They enable the measurement of high voltage and current levels without directly exposing measuring instruments to these hazardous conditions. This note covers the essential concepts, formulas, and insights required for the GATE CS exam.

**Core Concepts**
----------------

### Types of Instrument Transformers

There are two primary types of instrument transformers:

1.  **Current Transformer (CT)**: Used to measure high currents in a circuit.
2.  **Potential Transformer (PT)**: Used to measure high voltages in a circuit.

**Key Formulas/Theorems**
-------------------------

LaTeX is not directly supported in Markdown, but we can use mathematical notation:

-   The ratio of the secondary current to the primary current in a CT is given by:

$$\frac{I_2}{I_1} = \frac{N_2}{N_1}$$

where $I_2$ and $I_1$ are the secondary and primary currents, respectively, and $N_2$ and $N_1$ are the number of turns in the secondary and primary coils.

-   The ratio of the secondary voltage to the primary voltage in a PT is given by:

$$\frac{V_2}{V_1} = \frac{N_2}{N_1}$$

where $V_2$ and $V_1$ are the secondary and primary voltages, respectively.

**Problem Solving Patterns**
---------------------------

### Pattern 1: Matching Features with Instrument Transformers

Given a list of features for instrument transformers, match each feature with its corresponding transformer type (CT or PT).

-   Identify the key characteristics of each transformer type:
    -   CT: Primary current is the line current, secondary burden affects primary current
    -   PT: Open-circuited secondary is not desirable, primary is connected in parallel to the grid
-   Use the following steps to solve:
    1.  Identify the correct features for each transformer type.
    2.  Match each feature with its corresponding transformer type.

### Pattern 2: Applying Formulas

Use the formulas provided earlier to solve problems involving instrument transformers.

**Examples with Solutions**
---------------------------

### Example 1:

A CT has a primary current of 10 A and secondary current of 5 A. If the number of turns in the primary coil is 100, find the number of turns in the secondary coil.

```latex
\frac{I_2}{I_1} = \frac{N_2}{N_1}
\Rightarrow N_2 = N_1 \times \frac{I_2}{I_1}
= 100 \times \frac{5}{10}
= 50
```

### Example 2:

A PT has a primary voltage of 400 V and secondary voltage of 20 V. If the number of turns in the primary coil is 500, find the number of turns in the secondary coil.

```latex
\frac{V_2}{V_1} = \frac{N_2}{N_1}
\Rightarrow N_2 = N_1 \times \frac{V_2}{V_1}
= 500 \times \frac{20}{400}
= 25
```

**Common Pitfalls**
-------------------

-   Confusing the formulas for CT and PT.
-   Not considering the direction of current flow in the secondary coil.

**Quick Summary**
-----------------

*   Instrument transformers (CT and PT) are used to measure high currents and voltages.
*   Use the following formulas:
    *   $\frac{I_2}{I_1} = \frac{N_2}{N_1}$ for CT
    *   $\frac{V_2}{V_1} = \frac{N_2}{N_1}$ for PT
*   Match features with transformer types:
    *   Primary current is the line current: CT
    *   Open-circuited secondary is not desirable: PT
    *   Primary is connected in parallel to the grid: PT