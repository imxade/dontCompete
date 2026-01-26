**Logic Gates**
===============

**Introduction**
---------------

Logic gates are fundamental electronic devices used to perform logical operations on binary inputs. They play a crucial role in digital electronics, computer systems, and communication networks. This note provides an in-depth explanation of logic gates, focusing on the concepts tested in previous years' GATE exams.

**Core Concepts**
-----------------

### Types of Logic Gates

1. **AND Gate**: Produces output 1 only if all inputs are 1.
2. **OR Gate**: Produces output 1 if any input is 1.
3. **NOT Gate**: Inverts the input (i.e., 0 becomes 1 and vice versa).

### CMOS Implementation of Logic Gates

CMOS (Complementary Metal-Oxide-Semiconductor) logic gates use a combination of NMOS (n-channel MOSFETs) and PMOS (p-channel MOSFETs) to implement logical operations. In the context of NOT gates, CMOS implementation is used.

### Key Formulas/Theorems

* Entropy of a discrete random variable $X$ taking $K$ possible distinct real values:
\[ H(X) = -\sum_{i=1}^{k} P(x_i) \log_2 P(x_i) \]
where $P(x_i)$ is the probability of each value.

**Problem Solving Patterns**
---------------------------

### Analyzing CMOS NOT Gates

When analyzing CMOS NOT gates, consider the following:

* The NMOS transistor will be in the linear regime for a logical high input.
* The noise margin (NM) of the CMOS logic gate depends on both the sizing of transistors and the mobility of electrons.

**Examples with Solutions**
-------------------------

### Example 1: CMOS NOT Gate

Consider a CMOS NOT gate with NMOS transistor $M_n$ and PMOS transistor $M_p$. The input is logical high (1).

```mermaid
graph LR
    A[Logical High] --> B[M_n: Linear Regime]
```

* What is the state of the NMOS transistor?
Answer: In the linear regime.

### Example 2: Noise Margin

Suppose we have a CMOS NOT gate with equal-sized transistors. The noise margin (NM) for both logical high and low inputs is the same.

```mermaid
graph LR
    A[Logical High] --> B[NM = NM_L]
```

* Is it true that the mobility of electrons never influences the switching speed of the NOT gate?
Answer: No, mobility of electrons does influence the switching speed.

**Common Pitfalls**
------------------

1. **Misunderstanding CMOS Implementation**: Be aware of how CMOS logic gates work, especially in the context of NOT gates.
2. **Ignoring NM and Mobility**: Remember that noise margin and electron mobility are crucial factors affecting the behavior of CMOS logic gates.

**Quick Summary**
-----------------

* Logic gates are fundamental electronic devices performing logical operations on binary inputs.
* CMOS implementation uses a combination of NMOS and PMOS transistors to implement logical operations.
* Noise margin (NM) depends on transistor sizing and electron mobility.
* NM for both logical high and low inputs is the same in equal-sized transistors.

Note: This note covers the essential concepts related to logic gates, CMOS implementation, and noise margin. Review these topics thoroughly to improve your understanding and prepare for future GATE exams.