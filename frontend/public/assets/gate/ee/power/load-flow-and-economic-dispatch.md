**Load Flow and Economic Dispatch**
=====================================

**Introduction**
---------------

Load flow and economic dispatch are crucial components of power system analysis, aimed at determining the most economical way to supply a given load while respecting the physical constraints of the power grid. In this note, we will cover the theoretical concepts and formulas required for solving GATE-style questions on these topics.

**Core Concepts**
-----------------

### Load Flow

Load flow analysis involves calculating the current flowing through each branch of the power network under steady-state conditions. It is essential to determine the voltage magnitude and phase angle at each bus in the system.

The load flow problem can be formulated as a set of nonlinear equations:

$$P_V = V_i \sum_{j=1}^{n} V_j |Y_{ij}| \cos(\theta_{ij} - \delta_i + \delta_j)$$

$$Q_V = V_i \sum_{j=1}^{n} V_j |Y_{ij}| \sin(\theta_{ij} - \delta_i + \delta_j)$$

where:

* $P_V$ and $Q_V$ are the active and reactive power injections at bus $i$
* $V_i$ and $\delta_i$ are the voltage magnitude and phase angle at bus $i$, respectively
* $Y_{ij}$ is the admittance between buses $i$ and $j$
* $\theta_{ij}$ is the phase angle of $Y_{ij}$
* $n$ is the number of buses in the system

### Economic Dispatch

Economic dispatch involves allocating the total load among generators such that the total cost of generation is minimized while meeting the load demand. The economic dispatch problem can be formulated as a set of nonlinear equations:

$$\min \sum_{i=1}^{n} F_i(P_i)$$

subject to:

* $P_D = \sum_{i=1}^{n} P_i$
* $P_i \geq 0$, for all $i$

where:

* $F_i(P_i)$ is the cost function of generator $i$ as a function of its output
* $P_D$ is the total load demand
* $P_i$ is the output of generator $i$

### Incremental Cost

The incremental cost of each generator is given by the derivative of its cost function with respect to its output:

$$\lambda_i = \frac{dF_i(P_i)}{dP_i}$$

**Key Formulas/Theorems**
-------------------------

* **Load Flow**: The load flow problem can be formulated as a set of nonlinear equations, as described above.
* **Economic Dispatch**: The economic dispatch problem can be formulated as a set of nonlinear equations, as described above.
* **Incremental Cost**: The incremental cost of each generator is given by the derivative of its cost function with respect to its output.

**Problem Solving Patterns**
---------------------------

### Ignoring Network Losses

When ignoring network losses, we assume that all generators supply their power directly to the load without any transmission losses. In this case, the economic dispatch problem simplifies to:

$$\min \sum_{i=1}^{n} F_i(P_i)$$

subject to:

* $P_D = \sum_{i=1}^{n} P_i$
* $P_i \geq 0$, for all $i$

### Using Incremental Cost

To solve the economic dispatch problem, we can use the incremental cost of each generator as a Lagrange multiplier. The optimal solution is given by:

$$P_i^* = arg\min_{P_i} F_i(P_i)$$

subject to:

* $\lambda_i = \frac{dF_i(P_i)}{dP_i}$

**Examples with Solutions**
---------------------------

### Example 1: Economic Dispatch

Suppose we have two generators with cost functions $F_1(P_1) = 0.05P_1^2 + 10$ and $F_2(P_2) = 0.03P_2^2 + 5$. The total load demand is 260 MW, and we ignore network losses.

Using the incremental cost method, we can find the optimal output of each generator:

$$\lambda_1 = \frac{dF_1(P_1)}{dP_1} = 0.1P_1 + 10$$

$$\lambda_2 = \frac{dF_2(P_2)}{dP_2} = 0.06P_2 + 5$$

Equating the incremental costs, we get:

$$0.1P_1 + 10 = 0.06P_2 + 5$$

Substituting $P_D = 260$ MW and solving for $P_1$ and $P_2$, we get:

$$P_1^* = 160 \text{ MW}$$
$$P_2^* = 100 \text{ MW}$$

### Example 2: Load Flow

Suppose we have a simple power system with two buses, each with an active power injection of $P_V = 100$ MW. The admittance between the two buses is $Y_{12} = 1 + j5$, and the phase angle of $Y_{12}$ is $\theta_{12} = \pi/2$. We want to find the voltage magnitude and phase angle at each bus.

Using the load flow equations, we can write:

$$P_V = V_1 |Y_{12}| \cos(\theta_{12} - \delta_1 + \delta_2)$$

Solving for $V_1$ and $\delta_1$, we get:

$$V_1^* = 120.71 \text{ kV}$$
$$\delta_1^* = 35.26^\circ$$

**Common Pitfalls**
------------------

### Ignoring Network Losses

When ignoring network losses, it is essential to ensure that the generators supply their power directly to the load without any transmission losses.

### Using Incremental Cost

When using incremental cost as a Lagrange multiplier, it is crucial to ensure that the optimal solution satisfies the constraints of the economic dispatch problem.

**Quick Summary**
-----------------

* Load flow analysis involves calculating the current flowing through each branch of the power network under steady-state conditions.
* Economic dispatch involves allocating the total load among generators such that the total cost of generation is minimized while meeting the load demand.
* The incremental cost of each generator is given by the derivative of its cost function with respect to its output.

This concludes our comprehensive theory note on load flow and economic dispatch. By mastering these concepts, you will be well-prepared to tackle GATE-style questions on these topics.