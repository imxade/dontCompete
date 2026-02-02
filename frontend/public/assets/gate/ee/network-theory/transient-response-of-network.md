**Transient Response of Network**
=====================================

**Introduction**
---------------

The transient response of a network refers to its behavior over time after a change occurs, such as closing a switch or changing an input signal. Understanding this concept is crucial for analyzing and designing electronic circuits.

**Core Concepts**
-----------------

### Time Constant (τ)

The time constant (τ) of a circuit determines how quickly it responds to changes in its inputs. It's defined as the ratio of the total resistance (Rt) to the total reactance (Xt).

LaTeX
```tex
\tau = \frac{R_t}{X_t}
```

### Thevenin Equivalent Circuit

The Thevenin equivalent circuit is a simplified representation of a network, showing only its internal impedance and an ideal voltage source.

Mermaid diagram:
```mermaid
graph LR
A[Network] -->|Th(ε)|> B[Thevenin Equivalent]
```

**Key Formulas/Theorems**
-------------------------

### R-L Network

For an R-L network, the time constant (τ) is given by:

LaTeX
```tex
\tau = \frac{L}{R}
```
where L is the inductance and R is the resistance.

### Inductor Time Constant

The time constant for an inductor (τL) is related to its value (eqL):

LaTeX
```tex
\tau_L = \frac{L}{eq_L} = \frac{5H}{5Ω}
```

**Problem Solving Patterns**
---------------------------

1. **Identify the type of circuit**: Determine whether it's an R-L, R-C, or L-C network.
2. **Calculate the time constant (τ)**: Use the relevant formula(s) to find the time constant.
3. **Analyze the transient response**: Understand how the circuit behaves over time after a change occurs.

**Examples with Solutions**
---------------------------

### Example 1

Given:
A circuit with an inductor (L = 5H), a resistor (R = 10Ω), and a capacitor (C) is connected to a voltage source. The switch S is initially open, and then closed at time t=0.

Solution:

* Calculate the time constant (τ):
```latex
\tau = \frac{L}{R} = \frac{5H}{10Ω} = 0.5s
```
* Analyze the transient response:
The capacitor will charge up over time, and the current through the inductor will decay exponentially.

### Example 2

Given:
A circuit with an R-L network has a resistance (R) of 15Ω and an inductance (L) of 1H. The switch S is initially open and then closed at time t=0.

Solution:

* Calculate the time constant (τ):
```latex
\tau = \frac{L}{eq_L} = \frac{1H}{5Ω}
```
* Analyze the transient response:
The current through the inductor will decay exponentially over time, and the voltage across the resistor will increase linearly.

**Common Pitfalls**
-------------------

1. **Incorrect unit conversions**: Be careful when converting units from one quantity to another.
2. **Misunderstanding circuit behavior**: Pay attention to how different components interact with each other during transient response analysis.

**Quick Summary**
------------------

* Time constant (τ) is a measure of a circuit's response time
* Thevenin equivalent circuit simplifies network analysis
* R-L, R-C, and L-C networks have distinct time constants and behaviors

This comprehensive theory note covers the core concepts, formulas, and problem-solving patterns for transient response analysis in network theory.