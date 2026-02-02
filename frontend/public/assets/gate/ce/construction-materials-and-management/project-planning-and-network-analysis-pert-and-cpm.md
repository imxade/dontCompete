**Project Planning and Network Analysis - PERT and CPM**
===========================================================

### Introduction
-----------------

Project planning is a critical aspect of construction management, involving the organization, coordination, and allocation of resources to achieve project objectives. Network analysis techniques, such as Program Evaluation and Review Technique (PERT) and Critical Path Method (CPM), are essential tools for efficient project planning.

**Core Concepts**
----------------

### What is PERT?
-----------------

Program Evaluation and Review Technique (PERT) is a network analysis technique used to estimate the time required to complete a project. It was developed by the US Navy in the late 1950s and early 1960s.

#### Key Components:

* **Network Diagram**: A graphical representation of the project activities and their relationships.
* **Activity List**: A list of all activities required to complete the project, along with their estimated durations.
* **Event List**: A list of events that mark the beginning or end of each activity.

### What is CPM?
-----------------

Critical Path Method (CPM) is a network analysis technique used to identify the critical path in a project and determine the minimum time required to complete it. It was developed by Morgan R. Walker et al. at DuPont in 1958.

#### Key Components:

* **Network Diagram**: A graphical representation of the project activities and their relationships.
* **Activity List**: A list of all activities required to complete the project, along with their estimated durations.
* **Critical Path**: The longest path through the network diagram that determines the minimum time required to complete the project.

### Key Formulas/Theorems
---------------------------

#### PERT:

*   **Expected Time (ET)**: $E(T) = \frac{\sum T_{i}}{n}$
*   **Standard Deviation (SD)**: $\sigma = \sqrt{\frac{\sum T_i^2}{n} - E(T)^2}$

#### CPM:

*   **Critical Path**: The path with the longest total duration through the network diagram.
*   **Earliest Finish Time (EF)**: $E(F) = L + S$
*   **Latest Start Time (LS)**: $L(S) = F - S$

### Problem Solving Patterns
---------------------------

#### Crashing in PERT:

When crashing an activity, its duration is reduced, and the overall project time may decrease. However, this can increase costs due to resource utilization.

*   To determine whether crashing is beneficial, compare the cost of crashing with the indirect cost of the project.
*   Use the formula: $C_{crashed} = C + (C_{indirect} \times T_{crashed})$

#### Critical Path Analysis in CPM:

To identify the critical path and minimize project time, analyze the network diagram.

*   Identify the critical activities with zero slack.
*   Determine the earliest finish time for each activity and calculate the latest start time.
*   Compare the EF and LS to identify potential bottlenecks.

### Examples with Solutions
---------------------------

**Example 1:**

A project consists of two activities, A and B. Activity A takes 5 days to complete, while activity B takes 3 days. The total project duration is 8 days. If the indirect cost of the project is Rs. 500 per day, is it economically advisable to crash activity B by 1 day?

**Solution:**

*   Calculate the expected time for activity B: $E(T_B) = \frac{3}{1} = 3$ days
*   Calculate the standard deviation for activity B: $\sigma = \sqrt{\frac{9}{1} - 3^2} = \sqrt{6}$
*   Determine the cost of crashing activity B by 1 day: $C_{crashed} = C + (C_{indirect} \times T_{crashed})$
*   Compare the cost of crashing with the indirect cost of the project.

**Example 2:**

A construction project has three activities, A, B, and C. The network diagram is as follows:

```
       +---------------+
       |         A     |
       +---------------+
              |
              |
              v
       +---------------+
       |      B      |
       +---------------+
              |
              |
              v
       +---------------+
       |         C     |
       +---------------+
```

The earliest finish times for each activity are:

*   Activity A: 5 days
*   Activity B: 3 days
*   Activity C: 2 days

Determine the critical path and calculate the minimum project duration.

**Solution:**

*   Identify the critical activities with zero slack.
*   Determine the earliest finish time for each activity.
*   Calculate the latest start time for each activity.
*   Compare the EF and LS to identify potential bottlenecks.

### Common Pitfalls
-------------------

1.  **Inadequate Resource Allocation**: Insufficient resources can lead to delays, increased costs, or even project abandonment.
2.  **Incorrect Network Diagram Representation**: An inaccurate network diagram can result in incorrect critical path identification, leading to suboptimal resource allocation and scheduling decisions.
3.  **Ignoring Indirect Costs**: Failing to consider indirect costs, such as opportunity costs, can lead to poor investment decisions and decreased profitability.

### Quick Summary
------------------

*   PERT: A network analysis technique for estimating project duration.
*   CPM: A network analysis technique for identifying the critical path and minimizing project time.
*   Critical Path Method (CPM):
    *   Identify the longest path through the network diagram.
    *   Calculate the earliest finish time and latest start time for each activity.
*   Key Formulas:
    *   Expected Time (ET): $E(T) = \frac{\sum T_i}{n}$
    *   Standard Deviation (SD): $\sigma = \sqrt{\frac{\sum T_i^2}{n} - E(T)^2}$