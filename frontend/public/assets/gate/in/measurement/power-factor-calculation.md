**Power Factor Calculation**
==========================

**Introduction**
---------------

The power factor (PF) is a measure of how effectively an AC electrical circuit or system converts input current into useful work. It's defined as the ratio of real power to apparent power and plays a crucial role in electrical engineering, particularly in power systems and measurement.

**Core Concepts**
-----------------

### Real Power vs. Apparent Power

Real power (P) is the actual power used by the load, while apparent power (S) is the vector sum of the real and reactive powers. The power factor is the ratio of these two quantities:

$$PF = \frac{P}{S} = cos(\phi)$$

where $\phi$ is the power angle between the voltage and current.

### Power Triangle

The power triangle is a graphical representation of the relationship between real power, apparent power, and reactive power. It's an essential tool for understanding power factor calculations:

```mermaid
graph LR
    P[Real Power] -->|cos(φ)|> S[Apparent Power]
    S ---|sin(φ)|--> Q[Reactive Power]
```

### Power Factor Calculation

The maximum power factor is achieved when the load is purely resistive, i.e., $\phi = 0^\circ$. In this case, $PF_{max} = cos(0^\circ) = 1$.

**Key Formulas/Theorems**
-------------------------

*   Real power: $P = VIcos(\phi)$
*   Apparent power: $S = VI$
*   Power factor: $PF = \frac{P}{S} = cos(\phi)$

**Problem Solving Patterns**
---------------------------

1.  Identify the type of load (resistive, inductive, or capacitive) and its impact on the power factor.
2.  Determine the apparent power (S) using the voltage and current values.
3.  Calculate the real power (P) using the power factor formula.
4.  Use the power triangle to visualize the relationship between real, apparent, and reactive powers.

**Examples with Solutions**
---------------------------

### Example 1: Maximum Power Factor

Given:
*   Voltage (V): 300 V
*   Current (I): 5 A
*   Wattmeter reading: 300 W

Objective: Find the maximum power factor.

Solution:

$$PF_{max} = \frac{P}{S} = cos(0^\circ) = 1$$

However, we need to find the value of $\phi$ for a wattmeter reading of 300 W. Using the formula $P = VIcos(\phi)$, we can rewrite it as:

$$300 = 300 \times 5 \times cos(\phi)$$

Solving for $\phi$, we get:

$$cos(\phi) = \frac{1}{0.2} \approx 5$$

Since the value is greater than 1, it's incorrect to assume a maximum power factor of $PF_{max}$. The correct approach involves finding the actual value of $\phi$.

### Example 2: Power Factor Calculation

Given:
*   Voltage (V): 300 V
*   Current (I): 5 A
*   Wattmeter reading: 300 W

Objective: Find the power factor.

Solution:

First, let's find the apparent power (S):

$$S = VI = 300 \times 5 = 1500 VA$$

Next, calculate the real power (P) using the wattmeter reading:

$$P = 300 W$$

Now, use the formula $PF = \frac{P}{S}$ to find the power factor:

$$PF = \frac{300}{1500} = 0.2$$

**Common Pitfalls**
-------------------

*   Assuming a maximum power factor of 1 when the load is not purely resistive.
*   Failing to account for the actual value of $\phi$ in calculations.

**Quick Summary**
------------------

*   Power factor (PF) is the ratio of real power (P) to apparent power (S).
*   Real power: $P = VIcos(\phi)$
*   Apparent power: $S = VI$
*   Power factor: $PF = \frac{P}{S} = cos(\phi)$
*   Maximum power factor is achieved when $\phi = 0^\circ$.