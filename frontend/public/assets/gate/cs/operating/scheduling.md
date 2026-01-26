**Scheduling Theory Note**
==========================

### Introduction
-----------------

Scheduling is a crucial aspect of Operating Systems that deals with allocating system resources, such as CPU time and I/O devices, to processes or threads. In this note, we will focus on two popular scheduling algorithms: Preemptive Shortest Remaining Time First (SRTF) and Non-Preemptive Shortest Job First (NP-SJF).

### Core Concepts
-----------------

*   **Process**: A program in execution, including its data and control information.
*   **Thread**: A lightweight process that shares the same memory space as other threads within a process.
*   **Scheduling Algorithm**: A set of rules or policies used to determine which process or thread should execute next.
*   **Preemption**: The act of suspending a running process or thread and replacing it with another one.

### Key Formulas/Theorems
-------------------------

The average waiting time (WT) for SRTF can be calculated using the formula:

$$ WT_{SRTF} = \frac{1}{n} \sum_{i=1}^{n} \left( WT_i + TAT_i - BT_i \right) $$

where n is the number of processes, WT_i is the waiting time for process i, TAT_i is the turn-around time for process i, and BT_i is the burst time (execution time) for process i.

The average waiting time (WT) for NP-SJF can be calculated using the formula:

$$ WT_{NP-SJF} = \frac{1}{n} \sum_{i=1}^{n} \left( WT_i + TAT_i - BT_i \right) $$

### Problem Solving Patterns
-----------------------------

To solve SRTF and NP-SJF problems, follow these steps:

1.  Calculate the burst time (BT) for each process.
2.  Sort the processes in ascending order of their burst times.
3.  Apply the scheduling algorithm to determine the next process to execute.
4.  Calculate the waiting time (WT) and turn-around time (TAT) for each process.

### Examples with Solutions
---------------------------

**Example 1: SRTF**

| Process | Arrival Time (AT) | Burst Time (BT) |
| --- | --- | --- |
| A     | 0             | 10            |
| B     | 2             | 6             |
| C     | 4             | 3             |
| D     | 6             | 7             |

Solution:

1.  Calculate the burst time (BT) for each process.
2.  Sort the processes in ascending order of their burst times.

        A: AT = 0, BT = 10
        B: AT = 2, BT = 6
        C: AT = 4, BT = 3
        D: AT = 6, BT = 7

    Sort by BT:

        C: AT = 4, BT = 3
        B: AT = 2, BT = 6
        A: AT = 0, BT = 10
        D: AT = 6, BT = 7

3.  Apply SRTF to determine the next process to execute.

    T1: C (AT = 4, BT = 3)
    T2: B (AT = 2, BT = 6)

    Calculate WT and TAT:

        C: WT = 0, TAT = 7
        B: WT = 3, TAT = 11

**Example 2: NP-SJF**

| Process | Arrival Time (AT) | Burst Time (BT) |
| --- | --- | --- |
| A     | 0             | 10            |
| B     | 2             | 6             |
| C     | 4             | 3             |
| D     | 6             | 7             |

Solution:

1.  Calculate the burst time (BT) for each process.
2.  Sort the processes in ascending order of their burst times.

        A: AT = 0, BT = 10
        B: AT = 2, BT = 6
        C: AT = 4, BT = 3
        D: AT = 6, BT = 7

    Sort by BT:

        C: AT = 4, BT = 3
        B: AT = 2, BT = 6
        A: AT = 0, BT = 10
        D: AT = 6, BT = 7

3.  Apply NP-SJF to determine the next process to execute.

    T1: C (AT = 4, BT = 3)
    T2: B (AT = 2, BT = 6)

    Calculate WT and TAT:

        C: WT = 0, TAT = 7
        B: WT = 5, TAT = 11

### Common Pitfalls
-------------------

*   Failing to calculate the burst time (BT) for each process.
*   Not sorting processes in ascending order of their burst times.
*   Confusing SRTF with NP-SJF.

### Quick Summary
-----------------

| Algorithm      | Key Characteristics |
| ---            | ---                  |
| SRTF           | Preemptive, shortest  |
|                | remaining time first  |
| NP-SJF         | Non-preemptive,       |
|                | shortest job first    |

To solve SRTF and NP-SJF problems:

1.  Calculate the burst time (BT) for each process.
2.  Sort the processes in ascending order of their burst times.
3.  Apply the scheduling algorithm to determine the next process to execute.

**Additional Resources**

For further learning, explore these resources:

*   [Operating System by William Stallings](https://www.amazon.com/Operating-Systems-William-Stallings/dp/0073523402/)
*   [Process Scheduling in Operating Systems by GeeksforGeeks](https://www.geeksforgeeks.org/process-scheduling-in-operating-systems/)