**State Variable Model and Solution of State Equation**
=====================================================

### Introduction
---------------

The state variable model is a mathematical representation of a system's behavior, focusing on its internal states. It is an essential tool in control systems for analyzing and designing feedback controllers.

### Core Concepts
-----------------

#### What are State Variables?
---------------------------

State variables are the minimum number of variables required to describe the behavior of a system completely and uniquely. They can be physical quantities like position, velocity, or current.

#### The State Equation
----------------------

The state equation is a differential equation that describes how the state variables change over time.

**Mathematical Representation**
```latex
\dot{x} = f(x,u,t)
```
where $\dot{x}$ is the derivative of the state variable $x$ with respect to time, $u$ is the input to the system, and $t$ is time.

#### Types of State Equations
-----------------------------

There are two types of state equations:

1.  **State-derivative equation**: This type of equation relates the derivatives of state variables to other variables in the system.
2.  **State-variable equation**: This type of equation relates one or more state variables to each other.

### Key Formulas/Theorems
-------------------------

#### The State Transition Matrix
--------------------------------

The state transition matrix is a matrix that describes how the state variables change over time.

**Mathematical Representation**
```latex
\phi(t) = e^{\int_{0}^{t} A(s)ds}
```
where $A(s)$ is the system matrix, and $\phi(t)$ is the state transition matrix.

### Problem Solving Patterns
---------------------------

#### Identifying State Variables
------------------------------

When analyzing a system, identify the minimum number of variables required to describe its behavior completely and uniquely. These variables are the state variables.

#### Formulating the State Equation
-----------------------------------

Once the state variables are identified, formulate the state equation by relating the derivatives of these variables to other variables in the system.

### Examples with Solutions
---------------------------

**Example 1:**
A circuit consists of an inductor ($L=0.5H$), a resistor ($R_1=2\Omega$ and $R_2=4\Omega$), and a capacitor ($C=0.25F$). The state variables are the current through the inductor ($i_L$) and the voltage across the capacitor ($v_C$).

The state equation for this system is:

$\begin{bmatrix} \dot{i}_L \\ \dot{v}_C \end{bmatrix} = \begin{bmatrix} -\frac{1}{0.5} & 0 \\ 0 & -4 \end{bmatrix}\begin{bmatrix} i_L \\ v_C \end{bmatrix} + \begin{bmatrix} 2 \\ 4 \end{bmatrix}u$

**Solution:**

To solve this equation, we need to find the state transition matrix and multiply it by the initial conditions.

### Common Pitfalls
-------------------

*   Failing to identify the minimum number of state variables.
*   Formulating an incorrect state equation.

### Quick Summary
------------------

*   State variable model is a mathematical representation of a system's behavior.
*   The state equation describes how the state variables change over time.
*   Identify state variables by determining the minimum number required to describe the system completely and uniquely.
*   Formulate the state equation using the derivatives of these variables.

### References
--------------

*   Control Systems, Ogata, K.