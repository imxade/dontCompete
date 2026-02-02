**Transformer Single Phase**
==========================

**Introduction**
---------------

A transformer is a type of electrical machine that transfers energy from one circuit to another through electromagnetic induction. In this note, we focus on single-phase transformers, which are commonly used in power systems.

**Core Concepts**
-----------------

### Principle of Operation

The principle of operation of a transformer is based on the Faraday's law of electromagnetic induction, which states that an electromotive force (EMF) is induced in a coil when it is exposed to a changing magnetic flux. In a single-phase transformer, two coils are wound around a common core: one primary coil and one secondary coil.

### Transformer Action

Transformer action can be described as follows:

*   The primary coil carries the input voltage $V_p$ and current $I_p$, which creates a magnetic field around the core.
*   The magnetic flux produced by the primary coil induces an EMF in the secondary coil, causing a current to flow through it.
*   The secondary coil is connected to a load, which draws power from the transformer.

**Key Formulas/Theorems**
-------------------------

### Transformer Efficiency

The efficiency of a transformer is given by:

$$\eta = \frac{P_{out}}{P_{in}} \times 100\%$$

where $P_{out}$ is the output power and $P_{in}$ is the input power.

### Transformer Action

The relationship between the primary and secondary voltages and currents can be described by:

$$E_s = \frac{N_s}{N_p} E_p$$

and

$$I_s = \frac{N_p}{N_s} I_p$$

where $E_p$ and $I_p$ are the primary voltage and current, respectively, and $E_s$ and $I_s$ are the secondary voltage and current, respectively.

**Problem Solving Patterns**
---------------------------

When solving problems involving single-phase transformers, consider the following:

*   Identify the type of transformer action: step-up or step-down.
*   Calculate the turns ratio using the formula $\frac{N_s}{N_p}$.
*   Use the efficiency formula to calculate the output power.

**Examples with Solutions**
---------------------------

### Example 1

A single-phase transformer has a primary voltage $V_p = 120\, \text{V}$ and a secondary voltage $V_s = 240\, \text{V}$. The turns ratio is $\frac{N_s}{N_p} = 2$. Calculate the efficiency of the transformer.

```mermaid
graph LR
A[Primary Voltage] --> B[Turns Ratio]
B --> C[Secondary Voltage]
C --> D[Efficiency]
```

Solution:

Using the formula for transformer action, we can write:

$$E_s = \frac{N_s}{N_p} E_p = 2 \times 120\, \text{V} = 240\, \text{V}$$

Now, we can calculate the efficiency using the formula:

$$\eta = \frac{P_{out}}{P_{in}} \times 100\% = \left( \frac{V_s}{V_p} \right)^2 \times 100\% = (2)^2 \times 100\% = 400\%$$

### Example 2

A single-phase transformer has a primary current $I_p = 10\, \text{A}$ and a secondary current $I_s = 5\, \text{A}$. The turns ratio is $\frac{N_p}{N_s} = 0.5$. Calculate the output power.

```mermaid
graph LR
A[Primary Current] --> B[Turns Ratio]
B --> C[Secondary Current]
C --> D[Output Power]
```

Solution:

Using the formula for transformer action, we can write:

$$I_s = \frac{N_p}{N_s} I_p = 0.5 \times 10\, \text{A} = 5\, \text{A}$$

Now, we can calculate the output power using the formula:

$$P_{out} = V_s I_s = 240\, \text{V} \times 5\, \text{A} = 1200\, \text{W}$$

**Common Pitfalls**
-------------------

When solving problems involving single-phase transformers, be careful of the following:

*   Confusing the turns ratio with the efficiency.
*   Failing to identify the type of transformer action.

**Quick Summary**
------------------

*   A single-phase transformer transfers energy from one circuit to another through electromagnetic induction.
*   The primary coil carries the input voltage and current, which creates a magnetic field around the core.
*   The secondary coil is connected to a load, drawing power from the transformer.
*   The relationship between the primary and secondary voltages and currents can be described by the formula $E_s = \frac{N_s}{N_p} E_p$ and $I_s = \frac{N_p}{N_s} I_p$.
*   The efficiency of a transformer is given by the formula $\eta = \frac{P_{out}}{P_{in}} \times 100\%$.

Note: This note focuses on single-phase transformers. For three-phase transformers, consult additional resources.