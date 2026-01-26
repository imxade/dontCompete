**Project Scheduling**
=======================

**Introduction**
---------------

Project scheduling is a crucial aspect of production planning and control, aiming to optimize resource allocation and minimize project duration. This topic involves analyzing activities, their dependencies, and time estimates to determine the critical path, which dictates the minimum possible completion time.

**Core Concepts**
-----------------

### Activity-on-Arc (AOA) Network

In AOA networks, each activity is represented by an arc between nodes. The network consists of:

*   **Nodes**: Represent activities or events
*   **Arcs**: Connect nodes and represent dependencies between activities

### Critical Path Method (CPM)

CPM determines the critical path in a project schedule, which is the sequence of activities with zero slack time. The critical path dictates the minimum possible completion time.

**Key Formulas/Theorems**
-------------------------

$$\text{Early Start} (ES_i) = \max\left(0, \sum_{j=1}^{i-1} ES_j + L_j - D_i\right)$$

$$\text{Late Finish} (LF_i) = \min\left(F_i, \sum_{j=i+1}^n LF_j + D_i + P_i\right)$$

where:

*   $ES_i$ is the early start time for activity $i$
*   $L_j$ is the latest finish time for predecessor $j$
*   $D_i$ is the duration of activity $i$
*   $F_i$ is the finish time for activity $i$
*   $P_i$ is the processing time for activity $i$

**Problem Solving Patterns**
---------------------------

### Identifying Critical Activities

To determine critical activities, calculate the slack time for each activity using:

$$\text{Slack Time} = ES - LF$$

If the slack time is zero, the activity is critical.

### Applying the Critical Path Method

1.  Determine the early start and late finish times for each activity.
2.  Calculate the slack time for each activity.
3.  Identify critical activities with zero slack time.
4.  Analyze the critical path to determine the minimum possible completion time.

**Examples with Solutions**
---------------------------

### Example 1: Determining Critical Activities

Suppose we have a project schedule with three activities:

| Activity | Duration (h) | Predecessors |
| --- | --- | --- |
| A | 2 | - |
| B | 3 | A |
| C | 2 | A |

Calculate the slack time for each activity.

1.  Determine the early start and late finish times for each activity.
    *   $ES_A = \max(0, 0 + 0 - 2) = 0$
    *   $LF_B = \min(F_B, 2 + D_B) = \min(5, 5 + 3) = 8$
    *   $ES_C = \max(0, ES_A) = \max(0, 0) = 0$
2.  Calculate the slack time for each activity.
    *   $Slack A = ES_A - LF_A = 0 - 2 = -2$ (not applicable)
    *   $Slack B = ES_B - LF_B = 3 - 8 = -5$ (not applicable)
    *   $Slack C = ES_C - LF_C = 0 - (ES_C + D_C) = 0 - (0 + 2) = -2$
3.  Identify critical activities with zero slack time.
    *   Activity A is not critical since its slack time is -2.
    *   Activity B is not critical since its slack time is -5.
    *   Activity C has a slack time of -2, but its predecessors (A) are not critical.

### Example 2: Applying the Critical Path Method

Suppose we have a project schedule with five activities:

| Activity | Duration (h) | Predecessors |
| --- | --- | --- |
| A | 2 | - |
| B | 3 | A |
| C | 2 | A |
| D | 4 | B, E |
| E | 5 | F |

Determine the critical path and minimum possible completion time.

1.  Determine the early start and late finish times for each activity.
    *   $ES_A = \max(0, 0 + 0 - 2) = 0$
    *   $LF_B = \min(F_B, 5 + D_B) = \min(7, 8) = 7$
    *   $ES_C = \max(0, ES_A) = \max(0, 0) = 0$
2.  Calculate the slack time for each activity.
    *   $Slack A = ES_A - LF_A = 0 - 2 = -2$ (not applicable)
    *   $Slack B = ES_B - LF_B = 3 - 7 = -4$ (not applicable)
    *   $Slack C = ES_C - LF_C = 0 - (ES_C + D_C) = 0 - (0 + 2) = -2$
3.  Identify critical activities with zero slack time.
    *   Activity A is not critical since its slack time is -2.
    *   Activity B is not critical since its slack time is -4.
    *   Activity C has a slack time of -2, but its predecessors (A) are not critical.

The critical path is A -> B -> D with a minimum possible completion time of 11 hours.

**Common Pitfalls**
-------------------

*   Failing to calculate slack times correctly
*   Misidentifying critical activities
*   Ignoring predecessor relationships

**Quick Summary**
-----------------

### Key Concepts:

*   Activity-on-Arc (AOA) network
*   Critical Path Method (CPM)
*   Early Start and Late Finish times
*   Slack Time calculation
*   Identifying critical activities

### Formulas/Theorems:

*   $\text{Early Start} (ES_i) = \max\left(0, \sum_{j=1}^{i-1} ES_j + L_j - D_i\right)$
*   $\text{Late Finish} (LF_i) = \min\left(F_i, \sum_{j=i+1}^n LF_j + D_i + P_i\right)$

### Problem Solving Patterns:

*   Identifying critical activities using slack time calculation
*   Applying the Critical Path Method to determine minimum possible completion time