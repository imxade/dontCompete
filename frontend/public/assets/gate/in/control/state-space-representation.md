**State Space Representation**
==========================

**Introduction**
---------------

In control systems, state space representation is a method of describing a system using its internal states and their relationships. It's a powerful tool for analyzing and designing complex systems. The state space model is represented by the following equations:

$$
\begin{aligned}
\dot{x}(t) &= Ax(t) + Bu(t) \\
y(t) &= Cx(t) + Du(t)
\end{aligned}
$$

where $x(t)$ is the state vector, $u(t)$ is the input, $A$ is the system matrix, $B$ is the input matrix, $C$ is the output matrix, and $D$ is the feedthrough matrix.

**Core Concepts**
-----------------

### State Space Representation

The state space representation describes a system using its internal states and their relationships. The state vector $x(t)$ represents the current state of the system, while the input $u(t)$ is used to modify this state.

### System Matrix A

The system matrix $A$ represents the dynamics of the system. It's an $n \times n$ matrix where $n$ is the number of states in the system. The entries in the matrix describe how each state interacts with others and how they evolve over time.

### Input Matrix B

The input matrix $B$ represents the influence of the input on the system. It's an $n \times m$ matrix, where $m$ is the number of inputs to the system. Each column of the matrix corresponds to a different input.

**Key Formulas/Theorems**
-------------------------

### Transfer Function from State Space Representation

Given a state space representation with matrices $A$, $B$, $C$, and $D$, the transfer function can be derived using the following formula:

$$
\begin{aligned}
H(s) &= C(sI - A)^{-1}B + D \\
&= \frac{CB(s)}{s^nb_0 + s^{n-1}b_{n-1} + \cdots + b_n}
\end{aligned}
$$

where $n$ is the number of states in the system, and $I$ is the identity matrix.

**Problem Solving Patterns**
---------------------------

### Finding Poles in State Space Representation

To find poles in a state space representation, we need to solve for the eigenvalues of the system matrix $A$. The eigenvalues are given by the solutions to the characteristic equation:

$$
|sI - A| = 0
$$

where $I$ is the identity matrix.

### Example: Finding Poles at the Origin

Given a state space representation with matrix $A$, we want to find a value of $A$ such that one of its poles is at the origin. This means that one of the eigenvalues of $A$ must be zero.

For example, let's consider the system matrix:

$$
\begin{aligned}
A &= \begin{bmatrix}
0 & 1 \\
-1 & -2
\end{bmatrix}
\end{aligned}
$$

The characteristic equation for this matrix is:

$$
|sI - A| = s^2 + 2s + 1 = 0
$$

Solving for $s$, we get:

$$
\begin{aligned}
s &= -1 \pm j
\end{aligned}
$$

Therefore, the poles of this system are at $-1 \pm j$. Since none of these poles are at the origin, we need to modify the matrix $A$ to achieve a pole at the origin.

One possible solution is:

$$
\begin{aligned}
A &= \begin{bmatrix}
0 & 1 \\
-2 & -3
\end{bmatrix}
\end{aligned}
$$

The characteristic equation for this modified matrix is:

$$
|sI - A| = s^2 + 3s + 2 = (s+2)(s+1) = 0
$$

Solving for $s$, we get:

$$
\begin{aligned}
s &= -1, \quad -2
\end{aligned}
$$

Therefore, the poles of this system are at $-1$ and $-2$. Since one of these poles is at the origin, we have successfully modified the matrix $A$ to achieve a pole at the origin.

**Common Pitfalls**
------------------

* Failing to check for pole-zero cancellations in state space representation.
* Assuming that a system with all non-negative eigenvalues has no poles.
* Misunderstanding the difference between controllability and observability Gramian matrices.

**Quick Summary**
-----------------

* State space representation describes a system using its internal states and their relationships.
* System matrix $A$ represents the dynamics of the system, while input matrix $B$ represents the influence of inputs on the system.
* Transfer function can be derived from state space representation using the formula:
  $$
  \begin{aligned}
  H(s) &= C(sI - A)^{-1}B + D
  \end{aligned}
  $$
* To find poles in a state space representation, we need to solve for the eigenvalues of the system matrix $A$.
* Poles at the origin can be achieved by modifying the system matrix $A$.