**Linear Programming**
=======================

**Introduction**
---------------

Linear programming (LP) is a method to achieve the best outcome in a given mathematical model for some list of requirements represented as linear relationships. It's a crucial tool in Operations Research, used to optimize various systems and processes.

**Core Concepts**
-----------------

### What is Linear Programming?

*   A linear programming problem involves maximizing or minimizing a linear objective function subject to a set of constraints, which are also expressed as linear equations.
*   The goal is to find the optimal solution that satisfies all constraints while optimizing the objective function.

### Key Components

*   **Decision Variables**: The variables that are being optimized.
*   **Objective Function**: A linear equation representing the quantity to be maximized or minimized.
*   **Constraints**: Linear inequalities or equalities that must be satisfied.

**Key Formulas/Theorems**
-------------------------

### Simplex Algorithm

The simplex algorithm is a popular method for solving LP problems. It works by moving from one feasible solution to another, improving the objective function value until an optimal solution is reached.

\begin{align*}
\max \quad & c^T x \\
s.t. \quad & Ax = b \\
& x \geq 0
\end{align*}

The simplex algorithm uses a tableau (a matrix of coefficients) to perform the optimization.

### Shadow Prices

Shadow prices are used in linear programming to measure the change in the objective function value due to a small increase in one of the resources.

If a resource is not fully utilized, its shadow price is zero. This indicates that the LP problem has found an optimal solution where the additional units of the resource do not improve the objective function value.

```latex
\text{Shadow Price} = \begin{cases}
0 & \text{if resource is not fully utilized}\\
\text{positive} & \text{if resource is underutilized and increasing it will improve the objective function value}\\
\text{negative} & \text{if resource is overutilized and decreasing it will improve the objective function value}
\end{cases}
```

**Problem Solving Patterns**
---------------------------

### Understanding Resource Utilization

To solve LP problems, it's essential to understand how resources are utilized. If a resource is not fully utilized, its shadow price is zero.

### Using Simplex Algorithm

The simplex algorithm can be used to solve large-scale LP problems efficiently. It involves creating a tableau and performing pivot operations to find the optimal solution.

**Examples with Solutions**
---------------------------

### Example 1: Minimizing Cost

A company wants to minimize its production costs by allocating resources optimally. The objective function is to minimize the total cost, subject to constraints on resource availability.

| Resource | Availability |
| --- | --- |
| Labor | 100 units |
| Material | 200 units |

The objective function is:

$$\min \quad 2x + 3y$$

Subject to constraints:

$$x + y \leq 50$$
$$2x + y \leq 75$$
$$x, y \geq 0$$

Using the simplex algorithm, we can find the optimal solution:

| x | y |
| --- | --- |
| 25 | 30 |

The minimum cost is: $$\min = 2(25) + 3(30) = 160$$

### Example 2: Maximizing Profit

A company wants to maximize its profit by allocating resources optimally. The objective function is to maximize the total profit, subject to constraints on resource availability.

| Resource | Availability |
| --- | --- |
| Labor | 100 units |
| Material | 200 units |

The objective function is:

$$\max \quad 4x + 3y$$

Subject to constraints:

$$x + y \leq 50$$
$$2x + y \leq 75$$
$$x, y \geq 0$$

Using the simplex algorithm, we can find the optimal solution:

| x | y |
| --- | --- |
| 25 | 30 |

The maximum profit is: $$\max = 4(25) + 3(30) = 220$$

**Common Pitfalls**
------------------

*   Not fully utilizing resources.
*   Overlooking constraints.

**Quick Summary**
-----------------

*   Linear programming is a method to optimize systems and processes.
*   Key components include decision variables, objective function, and constraints.
*   Shadow prices are used to measure the change in the objective function value due to small increases in resources.

By understanding these concepts and practicing with examples, you'll be well-prepared for tackling linear programming problems on the GATE CS exam.