**Network Theorem**
====================

### Introduction
The Network Theorem, also known as Thevenin's Theorem, is a fundamental concept in electric circuit analysis. It helps simplify complex networks by replacing them with an equivalent two-terminal network consisting of a voltage source and a series resistor.

### Core Concepts
-----------------

#### Voltage Source and Series Resistor
A voltage source is a device that maintains a constant voltage across its terminals, while a series resistor opposes the flow of current through it.

**Definition 1:** **Thevenin Equivalent Circuit**

Given a complex network with multiple sources and loads, Thevenin's Theorem states that we can replace the entire network with an equivalent two-terminal circuit consisting of:

* A voltage source $V_{TH}$ in series with a resistance $R_{TH}$
* This equivalent circuit has the same current-voltage characteristics as the original complex network

**Mathematical Representation**

Given a complex network $N$, its Thevenin equivalent circuit can be represented as:
\[ V_{TH} = \frac{V_1}{Z_1} Z_2 + V_2 \]
where:

* $V_1$ and $V_2$ are the open-circuit voltages at terminals 1 and 2
* $Z_1$ and $Z_2$ are the impedances of circuits connected to these terminals

**LaTeX Formulas**

The Thevenin equivalent voltage can be calculated using:
\[ V_{TH} = \frac{V_1}{|Z_1 + Z_2|} |Z_2| \]

### Key Formulas/Theorems
-------------------------

* **Thevenin's Theorem**: A complex network can be replaced by an equivalent two-terminal circuit consisting of a voltage source and series resistor.
* **Equivalent Circuit**: $V_{TH}$ in series with $R_{TH}$
* **Mathematical Representation**:
\[ V_{TH} = \frac{V_1}{Z_1} Z_2 + V_2 \]

### Problem Solving Patterns
---------------------------

1. **Identify the network type**: Determine if the problem involves a complex network or a simple circuit.
2. **Apply Thevenin's Theorem**: If the problem involves a complex network, apply Thevenin's Theorem to simplify it.
3. **Calculate $V_{TH}$ and $R_{TH}$**: Use the given formulas to calculate the equivalent voltage source and series resistor.

### Examples with Solutions
---------------------------

**Example 1:** Given the following circuit:

```
  +-----+     |        |
  |  V  |----->|       |
  +-----+     |        |
           |      |
           |      |
           v      v
  +-----+     +-----+
  |  R1 ||-----||R2   |
  +-----+     +-----+
```

*Find the Thevenin equivalent voltage $V_{TH}$ and series resistor $R_{TH}$.*

**Solution**

Using Thevenin's Theorem:

```r
# Define variables
V1 = 10 V
Z1 = 5 Ω
V2 = 0
Z2 = 3 Ω

# Calculate the Thevenin equivalent voltage
V_TH = (V1 / (|Z1 + Z2|)) * |Z2|

# Print result
print(V_TH)
```

The final answer is $V_{TH} = 6.67 V$

### Common Pitfalls
------------------

* **Incorrect application of Thevenin's Theorem**: Failing to identify the network type or applying the theorem incorrectly can lead to incorrect results.
* **Insufficient calculation**: Not calculating all variables required for the equivalent circuit.

### Quick Summary
----------------

| Concept | Description |
| --- | --- |
| Thevenin's Theorem | Simplifies complex networks by replacing them with an equivalent two-terminal network. |
| Equivalent Circuit | $V_{TH}$ in series with $R_{TH}$. |
| Key Formulas/Theorems | Thevenin's Theorem and its mathematical representation. |

[Back to top](#top)