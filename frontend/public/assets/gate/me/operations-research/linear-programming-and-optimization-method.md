**Linear Programming and Optimization Method**
=============================================

### Introduction
---------------

Linear programming is a method to achieve the best outcome (such as maximum profit or minimum cost) in a given mathematical model for some list of requirements represented as linear relationships. The goal is to find the optimal solution that maximizes or minimizes a linear function subject to a set of constraints.

### Core Concepts
-----------------

#### Linear Programming Problem

A linear programming problem can be defined by:

* **Decision variables**: $x_1, x_2, ..., x_n$ representing the resources or quantities to be determined.
* **Objective function** (also known as **cost function**): a linear combination of decision variables $f(x) = c_1x_1 + c_2x_2 + ... + c_nx_n$, where $c_i$ are coefficients representing the importance of each variable in the objective function.
* **Constraints**: a set of linear inequalities or equalities involving decision variables and constants.

#### Optimality Conditions

For a linear programming problem to have an optimal solution, it must satisfy the following conditions:

1.  **Primal feasibility**: The solution must satisfy all the constraints.
2.  **Dual feasibility**: The dual variables (shadow prices) must be non-negative for constraints that are satisfied as equalities.
3.  **Complementary slackness**: If a constraint is not fully utilized, its corresponding shadow price should be zero.

### Key Formulas/Theorems
-------------------------

$$\begin{aligned}
& \text{Primal problem: } & & \\ 
& \min_{x} & & c^T x \\
& s.t. & & Ax = b \\
& & & x \geq 0

\\[-10pt]
& \text{Dual problem: } & & \\ 
& \max_{y} & & y^T b \\
& s.t. & & A^Ty \leq c
\end{aligned}$$

where $A$ is the constraint matrix, $b$ is the right-hand side vector of constraints, and $c$ is the coefficient vector of the objective function.

### Problem Solving Patterns
---------------------------

1.  **Graphical Method**: For problems with two variables, plot the feasible region on a coordinate plane and find the optimal solution graphically.
2.  **Simplex Algorithm**: A systematic procedure for solving linear programming problems by iteratively improving an initial basic feasible solution.
3.  **Duality Theorem**: Establishes that for any primal problem, there exists a dual problem with complementary solutions.

### Examples with Solutions
---------------------------

**Example 1:** Find the maximum value of $x + y$ subject to the constraints:

$$\begin{aligned}
& x + y \leq 4 \\
& x - y \geq 2 \\
& x, y \geq 0

\end{aligned}$$

The dual problem is:

$$\begin{aligned}
& \max_{y_1, y_2} & & y_1(4) + y_2(2)
\\[-10pt]
& s.t. & & y_1 - y_2 \leq 1 \\
& & & y_1 + y_2 \leq 1
\end{aligned}$$

Solving the dual problem gives $y_1 = 0$ and $y_2 = 1$. Therefore, the optimal solution is $(x,y) = (3,1)$.

**Example 2:** Find the minimum value of $-x + y$ subject to:

$$\begin{aligned}
& x - y \geq -2 \\
& x + y \leq 5 \\
& x - y \leq -1
\end{aligned}$$

The solution can be obtained by using the Simplex Algorithm.

### Common Pitfalls
--------------------

*   Failing to check for complementary slackness when determining optimality conditions.
*   Not considering all possible combinations of decision variables and constraints.
*   Misinterpreting the objective function or constraints.

### Quick Summary
-----------------

*   Linear programming is a method for solving optimization problems with linear relationships between decision variables and constraints.
*   The goal is to find the optimal solution that maximizes or minimizes a linear function subject to a set of constraints.
*   Optimality conditions include primal feasibility, dual feasibility, and complementary slackness.
*   Key formulas and theorems include the primal and dual problems, as well as duality theorem.

---

I hope this comprehensive Theory Note on Linear Programming and Optimization Method helps you prepare for your GATE CS exam!