**Operating Condition: Power**
==========================

**Introduction**
---------------

The operating condition of a power system refers to its state under various loading conditions. In this context, we'll focus on minimizing losses in a power network.

**Core Concepts**
----------------

*   **Power Loss**: The total loss in the system is given by the sum of the squared currents through each branch multiplied by their respective resistances.
*   **Impedance**: Impedance ($z$) is a complex quantity with real and imaginary parts, represented as $z = r + jx$, where $r > 0$ and $x > 0$. The magnitude of impedance can be calculated using $|z| = \sqrt{r^2 + x^2}$.

**Key Formulas/Theorems**
-------------------------

*   **Power Loss Formula**: Given the current drawn from each load bus ($I_pu$) and the per-unit impedance ($z$) of each branch, the total power loss is calculated as:
    $$
    P_L = \sum_{i=1}^{n} |I_i|^2 r_i
    $$
*   **Minimum Loss Condition**: To minimize losses, we need to reduce the current flowing through branches with higher resistances.

**Problem Solving Patterns**
---------------------------

*   Identify the branches contributing most to power loss.
*   Determine which branch can be opened without compromising network stability.
*   Calculate the new current distribution after removing a branch.

**Examples with Solutions**
-------------------------

### Example 1

Suppose we have a system with three branches, and their impedances are given as $z_1 = (0.5 + j1)$, $z_2 = (0.8 + j0.6)$, and $z_3 = (1 + j0.9)$. The current drawn from each load bus is equal to $I_{pu}$.

*   Calculate the power loss in the system.
    \begin{align*}
    P_L &= |I_1|^2 r_1 + |I_2|^2 r_2 + |I_3|^2 r_3\\
    &=(0.9)^2(0.5) + (0.8)^2(0.8) + (0.7)^2(1) \\
    &= 0.405 + 0.512 + 0.49 = 1.407 \text{ p.u.}
    \end{align*}

### Example 2

Given the impedance and currents for branches $b_{12}$, $b_{23}$, and $b_{34}$ as follows:

| Branch | Impedance ($z$) | Current ($I$) |
| --- | --- | --- |
| $b_{12}$ | (0.6 + j1.2) | 0.8 pu |
| $b_{23}$ | (0.5 + j0.7) | 0.9 pu |
| $b_{34}$ | (0.4 + j0.8) | 1.1 pu |

*   Identify the branch that should be opened to minimize losses.

## Solution

To determine which branch should be opened, we need to calculate the power loss for each possible combination and select the one with minimum loss.

For this example, let's assume opening $b_{12}$ results in a new current distribution given by:

| Branch | Current ($I$) |
| --- | --- |
| $b_{12}$ | 0 pu |
| $b_{23}$ | 1.2 pu |
| $b_{34}$ | 1.4 pu |

Now, we can recalculate the power loss as follows:

\begin{align*}
P_L &= (1.2)^2(0.5) + (1.4)^2(0.8) + (1.3)^2(1) \\
&= 0.72 + 1.92 + 1.69 = 4.33 \text{ p.u.}
\end{align*}

Similarly, opening $b_{23}$ results in a new current distribution:

| Branch | Current ($I$) |
| --- | --- |
| $b_{12}$ | 0.8 pu |
| $b_{23}$ | 0 pu |
| $b_{34}$ | 1.4 pu |

Recalculating the power loss gives us:

\begin{align*}
P_L &= (0.8)^2(0.6) + (1.4)^2(0.5) + (1.3)^2(1) \\
&= 0.48 + 1.96 + 1.69 = 4.13 \text{ p.u.}
\end{align*}

Finally, opening $b_{34}$ results in a new current distribution:

| Branch | Current ($I$) |
| --- | --- |
| $b_{12}$ | 0.8 pu |
| $b_{23}$ | 1.2 pu |
| $b_{34}$ | 0 pu |

Recalculating the power loss gives us:

\begin{align*}
P_L &= (0.8)^2(0.6) + (1.2)^2(0.5) + (1.4)^2(1) \\
&= 0.48 + 0.72 + 1.96 = 3 \text{ p.u.}
\end{align*}

Comparing the power losses for each scenario, we find that opening $b_{34}$ results in the minimum loss of 3 p.u.

**Common Pitfalls**
-------------------

*   Students often neglect to consider the current distribution after removing a branch.
*   Failing to accurately calculate the power loss using the correct formula can lead to incorrect conclusions.

**Quick Summary**
-----------------

*   Minimizing losses involves reducing the current through branches with higher resistances.
*   Identify the most contributing branches and determine which one to open without compromising network stability.
*   Calculate the new current distribution after removing a branch and recalculate the power loss.