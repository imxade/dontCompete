# Scheduling Algorithm
=====================================

## Introduction
---------------

Scheduling algorithms are used to manage the execution of processes on a CPU. They aim to optimize system performance, resource utilization, and user satisfaction. In this note, we'll cover the Round Robin (RR) scheduling algorithm and its theoretical concepts.

## Core Concepts
-----------------

### Round Robin Scheduling Algorithm

The RR algorithm is a non-preemptive, FCFS-based algorithm that assigns each process a fixed time slice called the Time Quantum (TQ). The CPU switches between processes after completing the TQ of the current process. This ensures that all processes have a fair share of CPU time.

### Key Terms

*   **Time Quantum (TQ)**: The fixed time allocated to each process before the scheduler switches to another process.
*   **Context Switch**: The overhead of switching from one process to another, including updating registers and memory spaces.
*   **FCFS (First-Come-First-Served)**: A scheduling algorithm where processes are executed in the order they arrive.

## Key Formulas/Theorems
-------------------------

### Average Turnaround Time (ATT)

The average time taken by a process to complete its execution, including waiting for CPU allocation.

$$ \text{ATT} = \frac{\sum \text{(Turnaround Time of all processes)}}{\text{Number of processes}} $$

### Average Waiting Time (AWT)

The average time spent by a process in the ready queue before being allocated the CPU.

$$ \text{AWT} = \frac{\sum \text{(Waiting Time of all processes)}}{\text{Number of processes}} $$

## Problem Solving Patterns
---------------------------

*   **Context Switches**: Analyze context switches to determine possible CPU burst times.
*   **Time Quantum**: Use TQ to limit the execution time of each process.

## Examples with Solutions
-------------------------

### Example 1: RR Scheduling with TQ = 4

| Process | Arrival Time | Burst Time |
| --- | --- | --- |
| P | 0 | 3 |
| Q | 2 | 7 |
| R | 5 | 6 |
| S | 9 | 2 |

TQ = 4, Context Switches:

*   From S to Q: 1 switch
*   From R to Q: 1 switch
*   From Q to R: 2 switches

Possible CPU Burst Times:

$$ \text{CPU Burst Time} = \begin{cases} \text{Burst Time} &\quad \text{if } TQ > \text{Burst Time}\\ \text{TQ} &\quad \text{otherwise} \end{cases} $$

Applying this to each process:

| Process | CPU Burst Time |
| --- | --- |
| P | 3 (TQ = 4) |
| Q | 7 (TQ = 4) |
| R | 6 (TQ = 4) |
| S | 2 (TQ = 4) |

Note that context switches do not change the CPU burst time.

### Source Question Analysis

*   **cs_2022_43**: Analyze context switches and apply the formula for CPU burst time.

## Common Pitfalls
-----------------

*   **Ignoring Context Switches**: Failing to account for context switches can lead to incorrect conclusions.
*   **Incorrect TQ Assignment**: Misjudging the time quantum can result in suboptimal scheduling decisions.

## Quick Summary
---------------

### Key Concepts:

*   Round Robin Scheduling Algorithm (RR)
*   Time Quantum (TQ)
*   Context Switches
*   Average Turnaround Time (ATT) and Average Waiting Time (AWT)

### Formulae:

*   ATT = ∑(Turnaround Time of all processes)/Number of processes
*   AWT = ∑(Waiting Time of all processes)/Number of processes

### Key Insights:

*   Context switches affect CPU burst times.
*   TQ limits execution time for each process.

By mastering these concepts and insights, you'll be well-prepared to tackle the source question cs_2022_43 and similar scheduling algorithm problems.