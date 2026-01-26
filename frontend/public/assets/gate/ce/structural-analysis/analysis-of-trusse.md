**Analysis of Trusses**
======================

**Introduction**
---------------

A truss is a structure composed of straight members connected at joints to form triangles, which are the strongest shapes in engineering. The analysis of trusses involves determining the internal forces (tensions or compressions) and reactions (forces exerted by supports) on each member.

**Core Concepts**
----------------

### Assumptions

* Truss members are prismatic and linearly elastic.
* All members have identical axial rigidity.
* Joints are idealized as pin joints, allowing for rotation but no translation.

### Principles

1. **Virtual Work Method**: This method involves applying virtual displacements to the system and equating the work done by internal forces and external loads to zero.
2. **Method of Joints**: This method involves analyzing each joint in turn to find the internal forces on its members.
3. **Method of Sections**: This method involves cutting the truss into a number of sections, usually along the line of action of a force or reaction.

### Key Formulas/Theorems

* The equilibrium equations for a joint are given by:
\[ \sum F_x = 0, \quad \sum F_y = 0, \quad \sum M_A = 0 \]
* The internal forces on a member are related to the external loads and reactions by:
\[ F_i = \frac{F_{ext}}{\cos(\theta)} \]

```latex
\begin{equation}
\text{Equilibrium equations for a joint:} \\
\sum F_x = 0, \quad \sum F_y = 0, \quad \sum M_A = 0
\end{equation}

\begin{equation}
\text{Internal forces on a member:} \\
F_i = \frac{F_{ext}}{\cos(\theta)}
\end{equation}
```

**Problem Solving Patterns**
---------------------------

1. **Draw the truss**: Visualize the problem and draw the truss with all its members and joints.
2. **Identify the type of support**: Determine whether the supports are pin or roller, as this affects the equilibrium equations.
3. **Apply the method of joints or sections**: Choose either method to analyze the internal forces on each member.

**Examples with Solutions**
---------------------------

### Example 1: Method of Joints

```markdown
Given:
* Truss with 13 joints and 22 members
* Pin supports at A and L, roller support at K
* Loads at H (10kN vertically downward) and B (10kN horizontally rightward)

Find the reaction at pin support L.

Solution:

1. Draw the truss and identify the type of support.
2. Apply the method of joints to joint L.
3. Write down the equilibrium equations for joint L:
\[ \sum F_x = 0, \quad \sum F_y = 0, \quad \sum M_A = 0 \]
4. Solve for the reaction at pin support L.

```latex
\begin{equation}
R_L = \frac{F_H}{2} + \frac{F_B}{2} = 5kN + 5kN = 10kN
\end{equation}

### Example 2: Method of Sections

```markdown
Given:
* Truss with 13 joints and 22 members
* Pin supports at A and L, roller support at K
* Loads at H (10kN vertically downward) and B (10kN horizontally rightward)

Find the internal forces on member KL.

Solution:

1. Draw the truss and identify the type of support.
2. Apply the method of sections by cutting the truss along line KL.
3. Write down the equilibrium equations for section KL:
\[ \sum F_x = 0, \quad \sum F_y = 0, \quad \sum M_A = 0 \]
4. Solve for the internal forces on member KL.

```latex
\begin{equation}
F_{KL} = \frac{F_H}{2} + \frac{F_B}{2} = 5kN + 5kN = 10kN
\end{equation}

**Common Pitfalls**
------------------

* Failing to identify the type of support.
* Not applying the correct method (joints or sections).
* Not writing down the equilibrium equations.

**Quick Summary**
-----------------

* Truss is a structure composed of straight members connected at joints to form triangles.
* Analysis involves determining internal forces and reactions on each member.
* Key concepts: Virtual Work Method, Method of Joints, and Method of Sections.
* Equilibrium equations for a joint:
\[ \sum F_x = 0, \quad \sum F_y = 0, \quad \sum M_A = 0 \]
* Internal forces on a member related to external loads and reactions by:
\[ F_i = \frac{F_{ext}}{\cos(\theta)} \]

Note: The provided examples are simplified and not actual questions from the source. They serve as illustrations of how to apply the concepts to solve problems.