**Recurrence Relations**
========================

**Introduction**
---------------

A recurrence relation is a mathematical equation that defines a sequence recursively, where each term of the sequence is defined as a function of previous terms. Recurrence relations are used to model various phenomena in mathematics, computer science, and other fields.

**Core Concepts**
-----------------

### 1. Recursive Definition

A recurrence relation is defined by a recursive formula:

$$a_n = f(a_{n-1}, a_{n-2}, \ldots, a_0)$$

where $f$ is a function that depends on previous terms of the sequence.

### 2. Initial Conditions

The initial conditions specify the first few terms of the sequence, which are used to start the recursive process.

**Key Formulas/Theorems**
-------------------------

*   **Linear Recurrence Relation**: A linear recurrence relation has the form:

$$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \ldots + c_k a_0$$

where $c_i$ are constants.

*   **Non-Homogeneous Recurrence Relation**: A non-homogeneous recurrence relation has the form:

$$a_n = f(a_{n-1}, a_{n-2}, \ldots, a_0) + g(n)$$

where $f$ is a function of previous terms and $g$ is a function of the index $n$.

**Problem Solving Patterns**
---------------------------

### 1. Analyzing the Recurrence Relation

To solve a recurrence relation, analyze its structure to identify patterns or methods that can be applied.

### 2. Using Substitution Method

The substitution method involves substituting the solution of a simpler recurrence relation into the given recurrence relation.

### 3. Using Generating Functions

Generating functions are used to transform a recurrence relation into an algebraic equation, which can then be solved.

**Examples with Solutions**
---------------------------

### Example 1: Lucas Sequence

The Lucas sequence is defined by the recurrence relation:

$$L_n = L_{n-1} + L_{n-2}, \text{ for } n \geq 3$$

with initial conditions $L_1 = 1$ and $L_2 = 3$. Find the closed-form solution.

Solution:
The characteristic equation of this recurrence relation is:

$$x^2 - x - 1 = 0$$

Solving this equation yields the roots $x = \frac{1 + \sqrt{5}}{2}$ and $x = \frac{1 - \sqrt{5}}{2}$. Therefore, the closed-form solution of the Lucas sequence is:

$$L_n = A\left(\frac{1 + \sqrt{5}}{2}\right)^n + B\left(\frac{1 - \sqrt{5}}{2}\right)^n$$

where $A$ and $B$ are constants that can be determined from the initial conditions.

### Example 2: Non-Homogeneous Recurrence Relation

Consider the recurrence relation:

$$f_n = f_{n-1} + f_{n-2}, \text{ for } n \geq 3$$

with initial conditions $f_1 = 1$ and $f_2 = 2$. Find the closed-form solution.

Solution:
Using the substitution method, let:

$$g_n = f_n - a n^2$$

where $a$ is a constant to be determined. Then, we have:

$$g_{n-1} + g_{n-2} = (f_{n-1} - a(n-1)^2) + (f_{n-2} - a(n-2)^2) = f_n - an^2 = g_n$$

Therefore, the recurrence relation for $g_n$ is:

$$g_n = g_{n-1} + g_{n-2}, \text{ for } n \geq 3$$

with initial conditions $g_1 = f_1 - a(1)^2 = 1 - a$ and $g_2 = f_2 - a(2)^2 = 2 - 4a$. The closed-form solution of the recurrence relation for $g_n$ is:

$$g_n = A\left(\frac{1 + \sqrt{5}}{2}\right)^n + B\left(\frac{1 - \sqrt{5}}{2}\right)^n$$

where $A$ and $B$ are constants that can be determined from the initial conditions. The closed-form solution of the original recurrence relation is then given by:

$$f_n = a n^2 + g_n$$

**Common Pitfalls**
------------------

*   Forgetting to set up the correct initial conditions
*   Not identifying the type of recurrence relation (linear, non-homogeneous)
*   Not using generating functions or substitution method when necessary

**Quick Summary**
-----------------

*   Recursive definition: $a_n = f(a_{n-1}, a_{n-2}, \ldots, a_0)$
*   Linear recurrence relation: $a_n = c_1 a_{n-1} + c_2 a_{n-2} + \ldots + c_k a_0$
*   Non-homogeneous recurrence relation: $a_n = f(a_{n-1}, a_{n-2}, \ldots, a_0) + g(n)$
*   Substitution method and generating functions are used to solve recurrence relations.