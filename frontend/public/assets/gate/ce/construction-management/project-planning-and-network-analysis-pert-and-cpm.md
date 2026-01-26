**Project Planning and Network Analysis (PERT & CPM)**

### Introduction

Project planning involves scheduling activities to achieve specific goals within a project framework. Network analysis, specifically PERT (Program Evaluation and Review Technique) and CPM (Critical Path Method), are essential tools in this context. These methods help in determining the critical path of a project, estimating durations, and calculating floats.

### Core Concepts

**1. Critical Path:**
The critical path is the sequence of activities that determines the minimum duration required to complete a project. It's the longest path through the network diagram.

**2. Activity On Node (AON) vs. Activity On Arrow (AOA):**
AON: Each activity is represented by a node, and arrows indicate dependencies.
AOA: Arrows represent activities, while nodes denote events or milestones.

### Key Formulas/Theorems

#### PERT Calculations

*   **Expected Duration (Te)**:
    $$
    T_e = \frac{\sum (O_i + 4M_i + I_i)}{6}
    $$

    Where:
    -   Oi = Optimistic time
    -   Mi = Most likely time
    -   Ii = Pessimistic time

*   **Variance:**
    $$
    V_t = \frac{\sum (I_i - M_i)^2 + (\frac{1}{6})(\sum (O_i - 4M_i + I_i)^2)}{36}
    $$

#### CPM Calculations

*   **Early Start (ES)**:
    $$
    E_S = E_S \text{ of Predecessor Activity} + L_{\text{Predecessor}}
    $$

*   **Late Finish (LF)**:
    $$
    L_F = L_F \text{ of Successor Activity} - D_{\text{Successor}}
    $$

### Problem Solving Patterns

1.  **Identify the Critical Path:** Determine the longest path through the network diagram, which indicates the minimum duration required to complete the project.
2.  **Calculate Floats:** Compute early start, late finish, and total floats for each activity to understand its scheduling flexibility.

### Examples with Solutions

**Example:**

Suppose we have a project with two activities, A and B, where:

| Activity | Optimistic (Oi) | Most Likely (Mi) | Pessimistic (Ii) |
| --- | --- | --- | --- |
| A    | 3               | 5                | 7              |
| B    | 4               | 6                | 8              |

**PERT Calculations:**

*   Expected Duration of Activity A:
    $$
    T_e(A) = \frac{(3 + 4 \times 5 + 7)}{6} = \frac{38}{6}
    $$

### Common Pitfalls

1.  **Misunderstanding the Critical Path:** Ensure you identify the longest path through the network, which determines the project's minimum duration.
2.  **Incorrect Float Calculations:** Double-check your early start, late finish, and total floats calculations to avoid incorrect conclusions.

### Quick Summary

| Concept | Brief Description |
| --- | --- |
| PERT & CPM | Project planning methods for scheduling activities and estimating durations. |
| Critical Path | Longest path through the network diagram, determining project minimum duration. |
| Activity On Node (AON) vs. AOA | Representing activities in a network diagram. |

### References

*   [1]: "Project Management: The Managerial Process" by Erik W. Larson and Clifford Gray
*   [2]: "Construction Planning, Equipment, and Methods" by James G. Fairiss