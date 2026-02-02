**Stability Analysis using Routh-Hurwitz and Nyquist Criteria**
===========================================================

**Introduction**
---------------

Stability analysis is a crucial aspect of control systems, ensuring that the system remains stable under various operating conditions. In this note, we'll delve into the concepts of stability analysis using Routh-Hurwitz (RH) and Nyquist criteria.

**Core Concepts**
-----------------

### 1. **Routh-Hurwitz Criterion**

The RH criterion is a method for determining the stability of a linear system by analyzing its characteristic equation.

*   The characteristic equation is given by: $p(s) = \det(a_{ij})$
*   For each coefficient, calculate the following sequence:
    *   $r_1$ is the sum of all elements in row 1.
    *   $r_2$ is the determinant of the matrix formed by rows 1 and 2.
    *   Continue this pattern until a repeated root is found or all roots are identified.

### 2. **Nyquist Criterion**

The Nyquist criterion is used to determine the stability of a closed-loop system using its open-loop transfer function $G(s)H(s)$.

*   Plot the Nyquist diagram of $G(s)H(s)$, which represents the gain and phase shift of the system.
*   Use the RHP and LHP poles of the system to define critical angles:
    *   $\theta_c$ is the angle at which a RHP pole intersects with the imaginary axis.
    *   $\theta_r$ is the angle from the negative real axis to the intersection point of the Nyquist plot with the negative real axis.

### 3. **Transfer Function**

The transfer function $H(s)$ describes how the system responds to input signals.

*   A stable system has all poles in the LHP.
*   The high-frequency asymptote (HFA) is the slope of the Bode magnitude plot at high frequencies.

**Key Formulas/Theorems**
-------------------------

### 1. **Routh-Hurwitz Criterion**

The RH criterion involves calculating the following:

$$
\begin{aligned}
r_1 &= \sum_{i=1}^{n} a_{11,i} \\
r_2 &= \det(a_{ij})_{i,j=1,2} \\
&\vdots \\
r_n &= \det(a_{ij})_{i,j=1,n}
\end{aligned}
$$

### 2. **Nyquist Criterion**

The Nyquist criterion involves plotting the following:

$$
\begin{aligned}
G(s)H(s) &= k \frac{s+a}{s+b} \\
\theta_c &= -\angle G(jb) + \pi \\
\theta_r &= \angle G(jc)
\end{aligned}
$$

### 3. **Transfer Function**

The transfer function involves:

$$
H(s) = \frac{k}{(1+sT_d)(1+sT_i)}
$$

**Problem Solving Patterns**
---------------------------

*   When applying the RH criterion, focus on identifying repeated roots and their corresponding coefficients.
*   For the Nyquist criterion, determine critical angles by analyzing the intersection points of the Nyquist plot with the real axis.

**Examples with Solutions**
---------------------------

### 1. **Routh-Hurwitz Criterion**

Consider the system:

$$
\begin{aligned}
p(s) &= s^3 + 2s^2 + 6s + 12 \\
r_1 &= \sum_{i=1}^{n} a_{11,i} = 1+2+6+12 = 21 \\
r_2 &= \det(a_{ij})_{i,j=1,2} = 0
\end{aligned}
$$

Solving for $r_2$, we obtain:

$$
r_2 = \frac{(a_{11,2})(a_{22,1}) - (a_{11,1})(a_{22,2})}{(a_{12,1})(a_{22,1})} = 0
$$

### 2. **Nyquist Criterion**

Consider the system:

$$
\begin{aligned}
G(s)H(s) &= \frac{k}{s+a} \\
k &= 10 \\
a &= 5
\end{aligned}
$$

Plotting $G(jb)$, we find:

$$
\angle G(jb) = -\arctan(\frac{b}{a}) = -\arctan(\frac{1}{5})
$$

At $\theta_c$, the Nyquist plot intersects with the real axis at:

$$
\begin{aligned}
\theta_c &= \theta_r \\
&= \angle G(jc) = 0 + \pi
\end{aligned}
$$

### 3. **Transfer Function**

Consider the system:

$$
H(s) = \frac{k}{(1+sT_d)(1+sT_i)}
$$

Using the Bode magnitude plot, we find that the HFA is given by:

$$
\begin{aligned}
|H(jw)| &\propto |jw| \\
\Midline{\phantom{=}}\Midline{\phantom{|}}
&\propto w^2
\end{aligned}
$$

**Common Pitfalls**
-----------------

*   Failing to identify repeated roots when applying the RH criterion.
*   Misinterpreting critical angles when using the Nyquist criterion.

**Quick Summary**
----------------

*   Routh-Hurwitz criterion: a method for determining stability by analyzing characteristic equations.
*   Nyquist criterion: used to determine stability of closed-loop systems using open-loop transfer functions.
*   Transfer function: describes system response to input signals, with a focus on high-frequency asymptotes.

Note that all questions have been explained in detail. This study note will help you master the concepts tested in GATE exam papers and related topics.

References:

1.  [Routh-Hurwitz criterion](https://en.wikipedia.org/wiki/Routh%E2%80%93Hurwitz_stability_criterion)
2.  [Nyquist criterion](https://en.wikipedia.org/wiki/Nyquist_stability_criterion)
3.  [Transfer function](https://en.wikipedia.org/wiki/Transfer_function)

**Online Resources**

1.  [GATE CS exam questions and solutions](https://gateoverflow.in/)
2.  [Wikipedia: Control theory](https://en.wikipedia.org/wiki/Control_theory)