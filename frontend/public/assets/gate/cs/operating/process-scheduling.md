**Process Scheduling**
=======================

### Introduction
-----------------

Process scheduling is a fundamental concept in Operating Systems that deals with allocating CPU time to processes or threads for execution. The goal of process scheduling is to optimize system performance, throughput, and fairness among competing processes.

### Core Concepts
-----------------

#### Process States
A process can be in one of the following states:

*   **New**: Created but not started yet.
*   **Ready**: Waiting to be executed by the CPU.
*   **Running**: Currently being executed by the CPU.
*   **Waiting**: Waiting for I/O completion or other resources.
*   **Zombie**: Finished, but parent process hasn't acknowledged termination.

#### Scheduling Algorithms
There are several scheduling algorithms:

*   **First-Come-First-Served (FCFS)**: Processes are executed in the order they arrive.
*   **Shortest Job First (SJF)**: Shortest process is executed first.
*   **Priority Scheduling**: Processes with higher priority execute first.
*   **Round Robin (RR)**: Each process executes for a fixed time quantum.

### Key Formulas/Theorems
-------------------------

#### Round Robin Formula
The average waiting time (`W`) and response time (`R`) can be calculated using the following formulas:

$$
\begin{aligned}
W &= \frac{T_q + T_{idle}}{2} \\
R &= W
\end{aligned}
$$

where `T_q` is the time quantum, and `T_idle` is the idle time.

#### Context Switching Time
The context switching time (`CST`) can be estimated using:

$$ CST = \frac{\text{number of context switches}}{\text{total execution time}}
$$

### Problem Solving Patterns
---------------------------

*   **Analyze Arrival Times**: Understand the order in which processes arrive and how it affects scheduling decisions.
*   **Context Switching**: Identify opportunities for reducing context switching times to optimize performance.
*   **Time Quantum Management**: Optimize time quantum allocation to minimize waiting times.

### Examples with Solutions
-------------------------

#### Example 1: Round Robin Scheduling

Suppose we have three processes `P`, `Q`, and `R` arriving at time 0. We allocate a time quantum of 2 units for each process using Round Robin scheduling. What is the average waiting time?

```
| Process | Arrival Time | Burst Time | Waiting Time |
| --- | --- | --- | --- |
| P     | 0           | 5         | 4             |
| Q     | 3           | 3         | 2             |
| R     | 6           | 1         | 1             |

Average waiting time: (10 + 8) / 3 = 18 / 3 = 6
```

#### Example 2: Context Switching

Suppose we have two processes `P` and `Q` with burst times of 5 and 3 units, respectively. If the context switching time is 1 unit, what is the total execution time?

```
Total execution time = P's burst + Q's burst + 2 \* CST
= 5 + 3 + 2 \* 1
= 9
```

### Common Pitfalls
-------------------

*   **Ignoring Context Switching**: Failing to account for context switching times can lead to underestimation of total execution time.
*   **Incorrect Time Quantum Allocation**: Misallocating time quantum can result in suboptimal performance.

### Quick Summary
------------------

*   Process scheduling aims to optimize system performance, throughput, and fairness.
*   Round Robin and Priority Scheduling are common algorithms used for process allocation.
*   Context switching times should be accounted for to estimate total execution time accurately.