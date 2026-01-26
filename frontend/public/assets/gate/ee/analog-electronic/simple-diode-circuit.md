**Simple Diode Circuit**
=======================

### Introduction

A simple diode circuit consists of a single diode connected to a power source, often with resistors or other components. Ideal diodes are assumed to have zero resistance when conducting and infinite resistance when not conducting.

### Core Concepts

* **Diode**: A two-terminal device that conducts current in one direction but blocks it in the opposite direction.
* **Ideal Diode**: A hypothetical diode with zero resistance (0 Ω) and infinite resistance (∞ Ω).
* **Nodal Analysis**: A method used to solve electrical circuits by applying Kirchhoff's Current Law (KCL) at each node.

### Key Formulas/Theorems

$$
I = \frac{V}{R}
$$

where $I$ is the current through a resistor, $V$ is the voltage across it, and $R$ is its resistance.

**KCL**

At any node in an electrical circuit, the sum of currents entering the node equals the sum of currents leaving the node:

$$
\sum_{i} I_i = 0
$$

where $I_i$ represents the current through each component connected to the node.

### Problem Solving Patterns

* **Assume both diodes are ON**: Solve for the voltage and current in the circuit as if both diodes were conducting.
* **Apply nodal analysis**: Use KCL at a strategic node to solve for the desired quantities.

### Examples with Solutions

**Q1: Given Circuit**

```mermaid
graph LR
A[10V] -->|1kΩ|> B(V_x)
B --> C[(D_1) (D_2)]
C -->|1kΩ|> D[3.13V]
```

**Solution**: 

Apply nodal analysis at node $x$:

$$
\begin{aligned}
\frac{x}{1k} - \frac{x}{1k} + \frac{3.13}{1k} &= 0 \\
x - x + 3.13 & = 0 \\
3.13 & = 0 \\
x & = \frac{10-3.13}{2}
\end{aligned}
$$

Simplifying, we get $x = 3.44V$. 

Since both diodes are assumed to be ON, the current through each diode is:

$$
I_1 = I_2 = \frac{x}{1k} = \frac{3.44}{1k}
$$

Therefore, $I = 3.44 mA$.

### Common Pitfalls

* **Ignoring ideal diode assumptions**: Be cautious when assuming an ideal diode is conducting or not.
* **Misapplying KCL**: Double-check your calculations for nodal analysis.

### Quick Summary

* Ideal diodes have zero resistance and infinite resistance
* Apply nodal analysis using KCL at strategic nodes
* Assume both diodes are ON to solve for voltage and current
* Use $I = \frac{V}{R}$ to calculate currents