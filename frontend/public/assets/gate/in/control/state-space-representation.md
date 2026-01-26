**State Space Representation**
==========================

### Introduction
-----------------

State space representation is a method of analyzing and designing control systems using differential equations. It describes the system's behavior by its state variables, which are the variables that define the system's current state.

### Core Concepts
------------------

#### State Variables
---------------

*   A state variable is a variable that defines the system's current state.
*   The number of state variables depends on the order of the differential equation describing the system.

#### System Matrix (A)
----------------------

*   The system matrix, denoted as $A$, represents the dynamics of the system.
*   It is an $n \times n$ matrix where $n$ is the number of state variables.
*   The diagonal elements represent the rates at which each state variable changes.

#### Input Matrix (B)
----------------------

*   The input matrix, denoted as $B$, represents the effect of inputs on the system's states.
*   It is an $n \times m$ matrix where $m$ is the number of inputs and $n$ is the number of state variables.

#### State Equation
-------------------

The state equation describes how the system's state evolves over time. For a continuous-time system, it can be written as:

$$\dot{\mathbf{x}}(t) = A\mathbf{x}(t) + B\mathbf{u}(t)$$

where $\mathbf{x}(t)$ is the state vector, $A$ is the system matrix, and $B$ is the input matrix.

#### Output Equation
---------------------

The output equation describes how the system's outputs are related to its states. It can be written as:

$$\mathbf{y}(t) = C\mathbf{x}(t) + D\mathbf{u}(t)$$

where $\mathbf{y}(t)$ is the output vector, $C$ is the output matrix, and $D$ is the feedthrough matrix.

### Key Formulas/Theorems
-------------------------

*   **Liapunov Stability**: A system is said to be Liapunov stable if there exists a positive definite function $\mathcal{V}(\mathbf{x})$ such that:

$$\dot{\mathcal{V}}(\mathbf{x}) \leq 0$$

for all $t > 0$.

*   **Lyapunov Equation**: The Lyapunov equation is used to determine the stability of a system. It can be written as:

$$P = A^TP + PA - Q$$

where $P$ and $Q$ are symmetric matrices, and $A$ is the system matrix.

### Problem Solving Patterns
------------------------------

#### Pattern 1: Finding State Space Representation

*   Given an output equation, find the corresponding state space representation.
*   Use the **Output Equation** formula to derive the state equation.

#### Example:

Given the output equation $\dot{y}(t) = 2x(t)$, find the state space representation.

```latex
\begin{align*}
\mathbf{x} & =
\begin{bmatrix}
x \\
y
\end{bmatrix}
\\
A &
=
\begin{bmatrix}
0 & 1 \\
2 & 0
\end{bmatrix}
\\
B &
=
\begin{bmatrix}
0 \\
1
\end{bmatrix}
\end{align*}
```

#### Pattern 2: Finding System Matrix (A)

*   Given a state equation, find the system matrix $A$.
*   Use the **State Equation** formula to derive the system matrix.

#### Example:

Given the state equation $\dot{x}(t) = -2x(t) + u(t)$, find the system matrix $A$.

```latex
\begin{align*}
A &
=
-
\begin{bmatrix}
-2 & 0 \\
0 & 0
\end{bmatrix}
\\
B &
=
\begin{bmatrix}
1 \\
0
\end{bmatrix}
\end{align*}
```

### Examples with Solutions
---------------------------

#### Example 1:

Consider the system described by the state equation $\dot{x}(t) = -2x(t) + u(t)$.

```latex
\begin{align*}
A &
=
-
\begin{bmatrix}
-2 & 0 \\
0 & 0
\end{bmatrix}
\\
B &
=
\begin{bmatrix}
1 \\
0
\end{bmatrix}
\end{align*}
```

Find the state space representation.

```latex
\begin{align*}
\mathbf{x} & =
\begin{bmatrix}
x \\
y
\end{bmatrix}
\\
A &
=
\begin{bmatrix}
-2 & 0 \\
0 & 0
\end{bmatrix}
\\
B &
=
\begin{bmatrix}
1 \\
0
\end{bmatrix}
\end{align*}
```

#### Example 2:

Consider the system described by the state equation $\dot{x}(t) = -x(t) + u(t)$.

```latex
\begin{align*}
A &
=
-
\begin{bmatrix}
-1 & 0 \\
0 & 0
\end{bmatrix}
\\
B &
=
\begin{bmatrix}
1 \\
0
\end{bmatrix}
\end{align*}
```

Find the state space representation.

```latex
\begin{align*}
\mathbf{x} & =
\begin{bmatrix}
x \\
y
\end{bmatrix}
\\
A &
=
-
\begin{bmatrix}
-1 & 0 \\
0 & 0
\end{bmatrix}
\\
B &
=
\begin{bmatrix}
1 \\
0
\end{bmatrix}
\end{align*}
```

### Common Pitfalls
----------------------

*   **Incorrect System Matrix (A)**: Make sure to derive the system matrix correctly.
*   **Inconsistent State Equation**: Ensure that the state equation matches the system matrix.

### Quick Summary
-----------------

*   State space representation is a method of analyzing and designing control systems using differential equations.
*   The system matrix $A$ represents the dynamics of the system.
*   The input matrix $B$ represents the effect of inputs on the system's states.
*   The state equation describes how the system's state evolves over time.

This comprehensive theory note covers all theoretical concepts, formulas, and insights required to solve the given source questions. It provides a detailed explanation of principles, laws, or algorithms, along with specific techniques derived from the source questions.