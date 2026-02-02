**Centre of Mass**
================

**Introduction**
---------------

The centre of mass (COM) is a fundamental concept in engineering mechanics, describing the point where the entire mass of an object can be considered to be concentrated for the purpose of analyzing its motion. This theory note will cover the core concepts, formulas, and problem-solving patterns required to tackle questions related to centre of mass.

**Core Concepts**
-----------------

### Definition

The centre of mass (COM) is a point in an object where the entire weight of the object can be considered to act. It is the point that moves as if all the mass of the object were concentrated at that point.

### Laws

* The law of conservation of momentum states that the total momentum of a closed system remains constant over time.
* The centre of mass moves in accordance with Newton's second law, where the force acting on an object is equal to its mass times its acceleration.

**Key Formulas/Theorems**
-------------------------

$$\mathbf{r}_{\text{COM}} = \frac{\sum m_i \mathbf{r}_i}{\sum m_i}$$

where:

* $\mathbf{r}_{\text{COM}}$ is the position vector of the COM
* $m_i$ is the mass of each object
* $\mathbf{r}_i$ is the position vector of each object relative to a reference point

**Problem Solving Patterns**
---------------------------

### Q1: Centre of Mass with External Forces

When an external force acts on an object, its COM will move in accordance with Newton's second law. The force acting on the COM can be calculated using the following formula:

$$\mathbf{F}_{\text{COM}} = \sum \mathbf{F}_i$$

where $\mathbf{F}_i$ is each external force acting on the object.

**Examples with Solutions**
---------------------------

### Example 1: Centre of Mass in a Rigid Body

A rigid body has a mass distribution as shown:

| Object | Mass (kg) | Position Vector |
| --- | --- | --- |
| A    | 2        | $\mathbf{r}_A = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$ |
| B    | 3        | $\mathbf{r}_B = \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}$ |

Find the COM of the rigid body.

Solution:

$$\mathbf{r}_{\text{COM}} = \frac{(2\mathbf{r}_A + 3\mathbf{r}_B)}{5}$$

$$= \frac{1}{5} \begin{pmatrix} 10 \\ 3 \\ 0 \end{pmatrix}$$

### Example 2: Centre of Mass with External Forces

A beam is subjected to a concentrated force as shown:

| Force | Magnitude (N) | Position Vector |
| --- | --- | --- |
| F    | 100         | $\mathbf{r}_F = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$ |

Find the COM of the beam and the force acting on it.

Solution:

$$\mathbf{r}_{\text{COM}} = \frac{\mathbf{r}_F}{2} = \begin{pmatrix} 0.5 \\ 0 \\ 0 \end{pmatrix}$$

$$\mathbf{F}_{\text{COM}} = F = \begin{pmatrix} 100 \\ 0 \\ 0 \end{pmatrix}$$

**Common Pitfalls**
------------------

* Forgetting to include all external forces when calculating the COM.
* Assuming the COM is at the geometric centre of an object.

**Quick Summary**
-----------------

* Centre of mass (COM) is a point where entire weight of an object can be considered to act.
* Laws: conservation of momentum, Newton's second law.
* Key formulas: $\mathbf{r}_{\text{COM}} = \frac{\sum m_i \mathbf{r}_i}{\sum m_i}$ and $\mathbf{F}_{\text{COM}} = \sum \mathbf{F}_i$.

Note: This theory note covers the core concepts and formulas required to tackle questions related to centre of mass. The examples provided demonstrate how to apply these concepts in different scenarios.