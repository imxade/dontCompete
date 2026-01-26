**Network Theory - Basic of Network**
=====================================

### Introduction
---------------

Network theory is a fundamental branch of electrical engineering that deals with the analysis and design of electrical networks. This section covers the basic concepts of network theory, including nodes, branches, and power flow.

### Core Concepts
-----------------

#### Nodes and Branches

A **node** is a point in a network where two or more elements are joined. A **branch** is a single element (or) component in a circuit.

*   In an electrical network, the junction of branches at a common point is called a Node.
*   A Junction is a point where three circuit paths meet.

#### Types of Nodes

There are different types of nodes in a network:

*   **Principle node**: The junction of three or more elements. Example:
    ```
    +---------------+
    |  R1  |       |
    +-------+       |
            |       |
            v       v
    +---------------+---------------+
    |         |       |         |
    |  R2  |       |  R3  |
    +-------+       +-------+
    ```
*   **Non-principle node**: A node with only two elements connected to it.

#### Number of Nodes and Branches

The number of nodes in a network can be found using the following formula:

$$\text{Number of nodes} = \text{Number of branches} - \text{Number of junctions} + 1$$

### Key Formulas/Theorems
-------------------------

*   **KCL (Kirchhoff's Current Law)**: The sum of currents entering a node is equal to the sum of currents leaving a node.
    $$\sum I_{in} = \sum I_{out}$$
*   **KVL (Kirchhoff's Voltage Law)**: The sum of voltages around a loop is zero.
    $$\sum V_{loop} = 0$$

### Problem Solving Patterns
---------------------------

When solving network problems, follow these steps:

1.  Draw the circuit diagram and identify the nodes and branches.
2.  Apply KCL or KVL to the nodes or loops in the circuit.
3.  Use Ohm's law to find currents and voltages.

### Examples with Solutions
---------------------------

#### Example 1: Nodal Analysis

Given circuit:

```
+---------------+
|  R1  |       |
+-------+       |
        |       |
        v       v
+---------------+---------------+
|         |       |         |
|  R2  |       |  R3  |
+-------+       +-------+
```

Find the current $I$ flowing through resistor $R_1$.

Solution:

*   Apply KCL to node A:
    $$\sum I_{in} = \sum I_{out}$$
    $$I + I_2 = I_3$$
*   Use Ohm's law to find the currents:
    $$I_2 = \frac{V}{R_2}$$
    $$I_3 = \frac{V}{R_3}$$
*   Substitute the expressions for $I_2$ and $I_3$ into the KCL equation:
    $$I + \frac{V}{R_2} = \frac{V}{R_3}$$

#### Example 2: Finding Power Delivered by a Source

Given circuit:

```
+---------------+
|  R1  |       |
+-------+       |
        |       |
        v       v
+---------------+---------------+
|         |       |         |
|  R2  |       |  R3  |
+-------+       +-------+
10 V
```

Find the power delivered by the 10 V source.

Solution:

*   Apply KVL to loop ABCD:
    $$\sum V_{loop} = 0$$
    $$V - I_1R_1 - I_2R_2 = 0$$
*   Use Ohm's law to find the currents:
    $$I_1 = \frac{V}{R_1}$$
    $$I_2 = \frac{V}{R_2}$$
*   Substitute the expressions for $I_1$ and $I_2$ into the KVL equation:
    $$V - \frac{V}{R_1}R_1 - \frac{V}{R_2}R_2 = 0$$

### Common Pitfalls
-------------------

*   Be careful when applying KCL and KVL to ensure that you are using the correct equations.
*   Use Ohm's law correctly to find currents and voltages.

### Quick Summary
-----------------

*   A node is a point in a network where two or more elements are joined.
*   A branch is a single element (or) component in a circuit.
*   KCL states that the sum of currents entering a node is equal to the sum of currents leaving a node.
*   KVL states that the sum of voltages around a loop is zero.

### References
---------------

*   [1] Network Theory by S.S. Bhattacharyya, New Age International Publishers.
*   [2] Electric Circuits by James W Nilsson and Susan A Riedel, Addison-Wesley.

This study note covers the basic concepts of network theory, including nodes, branches, power flow, and Kirchhoff's laws. It also includes examples with solutions to illustrate how to apply these concepts to solve problems.