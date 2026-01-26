**Per Unit System Calculation for Power Systems**
=====================================================

**Introduction**
---------------

The per unit system (p.u.) is a method used to simplify power system calculations by normalizing quantities such as voltages, currents, impedances, and powers. This approach enables engineers to analyze complex systems more easily and accurately.

**Core Concepts**
-----------------

*   **Per Unit Basis**: Normalization of quantities using base values, which are typically the nominal ratings of a system.
*   **Slack Bus**: A bus in a power system where voltage is not allowed to change during analysis. It serves as a reference point for voltage magnitude and angle.

**Key Formulas/Theorems**
-------------------------

### Per Unit Impedance

Given:

| Symbol | Description |
| --- | --- |
| Zbase | Base impedance |
| Zn | Nominal impedance |

Per unit impedance (Zp.u.) formula:
$$
\begin{aligned}
Z_{p.u.} &= \frac{Z_n}{Z_{base}} \\
&= \frac{n^2}{n_1^2} \cdot Z_n
\end{aligned}
$$

where:

| Symbol | Description |
| --- | --- |
| n   | Ratio of nominal power to base power |
| n1  | Ratio of nominal voltage to base voltage |

### Per Unit Current

Given:

*   Nominal current (In)
*   Base current (Ibase)

Per unit current (Ip.u.) formula:
$$
\begin{aligned}
I_{p.u.} &= \frac{I_n}{I_{base}} \\
&= \frac{n^2}{n_1^2} \cdot I_n
\end{aligned}
$$

### Per Unit Voltage

Given:

*   Nominal voltage (Vn)
*   Base voltage (Vbase)

Per unit voltage (Vp.u.) formula:
$$
\begin{aligned}
V_{p.u.} &= \frac{V_n}{V_{base}} \\
&= \frac{n^2}{n_1^2} \cdot V_n
\end{aligned}
$$

**Problem Solving Patterns**
-----------------------------

### Single-Line Diagram Analysis

*   Identify the type of fault (line-to-line, line-to-ground, etc.).
*   Determine the sequence diagram and relevant impedances.
*   Apply per unit system calculations to simplify analysis.

**Examples with Solutions**
---------------------------

### Example 1: Line-to-Line Fault

Given:

| Symbol | Description |
| --- | --- |
| E1 | Voltage at Bus 1 |
| Z1 | Impedance from Bus 1 to Bus 2 |

Per unit voltage at Bus 1 (Vp.u.) for a line-to-line fault:
$$
\begin{aligned}
V_{p.u.} &= \frac{E_1}{Z_1} \\
&= \frac{n^2}{n_1^2} \cdot E_1 \cdot Z_n^{-1}
\end{aligned}
$$

### Example 2: Fault Current Calculation

Given:

| Symbol | Description |
| --- | --- |
| Ia | Current at Bus A |
| Za | Impedance from Bus A to Ground |

Per unit current (Ip.u.) for a fault:
$$
\begin{aligned}
I_{p.u.} &= \frac{I_a}{Z_a} \\
&= \frac{n^2}{n_1^2} \cdot I_n \cdot Z_n^{-1}
\end{aligned}
$$

**Common Pitfalls**
-------------------

*   Incorrect application of per unit system formulas.
*   Failure to identify relevant sequence diagrams and impedances.

**Quick Summary**
------------------

*   Normalization using base values for power systems analysis
*   Per unit impedance, current, and voltage formulas
*   Single-line diagram analysis for fault calculations

This comprehensive theory note on the per unit system calculation covers all theoretical concepts required to solve problems similar to source question Q1 (ID: ee_2023_60). The provided examples and formulas serve as a starting point for students to develop their skills in power system analysis using the per unit system.