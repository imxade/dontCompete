**Economic Load Dispatch (ELD)**
=====================================

### Introduction
Economic Load Dispatch (ELD) is a method used to determine the optimal allocation of power generation among available units while minimizing the total cost. It's a crucial aspect of power system operation, ensuring efficient use of resources.

### Core Concepts
#### Power System Network Representation
A power system network can be represented as a graph with nodes (buses) and edges (lines). Each node represents a bus where power is generated or consumed, while each edge represents the transmission line connecting two buses.

#### Economic Dispatch Problem Formulation
Given:

* A set of generating units with their respective cost functions (`C_i(x)`), where `x` is the output power of unit `i`
* A load demand curve (`P_D`)
* The objective: minimize total generation cost while meeting load demand

### Key Formulas/Theorems
The economic dispatch problem can be formulated as:

$$ \min_{x} \sum_{i=1}^N C_i(x) $$

subject to:

* Load balance constraint: $\sum_{i=1}^N x_i = P_D$
* Non-negativity constraints: $x_i \geq 0$ for all `i`

### Problem Solving Patterns
#### Sequential Convex Programming (SCP)
SCP is a method used to solve the economic dispatch problem. It involves:

1. Formulating the Lagrangian function:
```latex
L(x, \lambda) = \sum_{i=1}^N C_i(x) - \lambda (\sum_{i=1}^N x_i - P_D)
```
2. Finding the Karush-Kuhn-Tucker (KKT) conditions:

| Variable | Condition |
| --- | --- |
| $x_i$ | $\frac{\partial L}{\partial x_i} = C_i'(x_i) + \lambda = 0$ |
| $\lambda$ | $\sum_{i=1}^N x_i - P_D = 0$ |

### Examples with Solutions
**Example 1**

Given:

* Two generating units: Unit 1 has a cost function $C_1(x) = 2x + 3$, while Unit 2 has a cost function $C_2(x) = x^2$
* Load demand curve: $P_D = 10$

Find the optimal output power of each unit using SCP.

**Solution**

1. Formulate the Lagrangian function:
```latex
L(x, \lambda) = (2x + 3) + (\lambda_1)(x - 5) + (\lambda_2)(x - 10)
```
2. Find the KKT conditions:

| Variable | Condition |
| --- | --- |
| $x$ | $\frac{\partial L}{\partial x} = 2 + \lambda_1 + \lambda_2 = 0$ |
| $\lambda_1$ | $x - 5 = 0$ |
| $\lambda_2$ | $x - 10 = 0$ |

Solving the KKT conditions yields: `x = 7.5`

### Common Pitfalls

* Failing to account for non-convexities in the cost functions
* Ignoring the load balance constraint

### Quick Summary
* Economic Load Dispatch (ELD) is a method used to determine the optimal allocation of power generation among available units while minimizing the total cost.
* The economic dispatch problem can be formulated as a nonlinear programming problem with equality and inequality constraints.
* Sequential Convex Programming (SCP) is a widely used method for solving the economic dispatch problem.