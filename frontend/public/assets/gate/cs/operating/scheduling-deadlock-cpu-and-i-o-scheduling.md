# Scheduling Deadlock CPU and I/O Scheduling
=====================================

## Introduction
---------------

Scheduling algorithms are a crucial part of operating systems, determining how tasks or processes are executed on a computer's processor. Two key concepts in this area are deadlock prevention and I/O scheduling.

### Deadlocks

A deadlock is a situation where two or more processes are unable to continue executing because each process is waiting for the other to release resources. This can lead to system crashes, data loss, and decreased productivity.

## Core Concepts
-----------------

### Preemptive Shortest Remaining Time First (SRTF)

In SRTF, the processor selects the task with the shortest remaining time. If a new task arrives with a shorter burst time than the current task, the processor preempts the current task to execute the new one.

*   **Advantages:**
    *   Effective for systems with varying task durations
    *   Minimizes waiting times and maximizes system utilization
*   **Disadvantages:**
    *   Requires continuous monitoring of task durations
    *   Can lead to increased context switching overhead

### Non-Preemptive Shortest Job First (NP-SJF)

In NP-SJF, the processor executes tasks in order of their arrival. If a new task arrives with a shorter burst time than the current task, it is not preempted but continues executing.

*   **Advantages:**
    *   Simple to implement
    *   Minimizes context switching overhead
*   **Disadvantages:**
    *   Inefficient for systems with varying task durations
    *   Can lead to increased waiting times

## Key Formulas/Theorems
-------------------------

### Average Waiting Time (AWT)

\[ AWT = \frac{\sum\limits_{i=1}^{n} WT_i}{n} \]

where \( WT_i \) is the waiting time for task \( i \), and \( n \) is the total number of tasks.

### Average Turnaround Time (ATT)

\[ ATT = \frac{\sum\limits_{i=1}^{n} TAT_i}{n} \]

where \( TAT_i \) is the turnaround time for task \( i \).

## Problem Solving Patterns
---------------------------

When solving scheduling problems, follow these steps:

1.  Understand the system configuration (number of processors, tasks, and resources).
2.  Identify the type of scheduler used (SRTF or NP-SJF).
3.  Calculate the waiting time for each task.
4.  Calculate the turnaround time for each task.
5.  Use formulas to find AWT and ATT.

## Examples with Solutions
-------------------------

### Example 1: SRTF CPU Scheduling

Consider a system with four tasks:

| Task | Arrival Time | Burst Time |
| --- | --- | --- |
| P1   | 0           | 10         |
| P2   | 2           | 6          |
| P3   | 4           | 3          |
| P4   | 6           | 7          |

Using SRTF, the processor executes tasks in order of their remaining burst time.

| Task | Remaining Burst Time | Waiting Time | Turnaround Time |
| --- | --- | --- | --- |
| P1   | 10                   | 0            | 26             |
| P2   | 6                    | 11           | 19             |
| P3   | 3                    | 13           | 7              |
| P4   | 7                    | 20           | 26             |

AWT = (0 + 11 + 6 + 13) / 4 = 7.5
ATT = (26 + 19 + 7 + 26) / 4 = 16

### Example 2: NP-SJF CPU Scheduling

Consider the same system as in Example 1.

Using NP-SJF, the processor executes tasks in order of their arrival.

| Task | Remaining Burst Time | Waiting Time | Turnaround Time |
| --- | --- | --- | --- |
| P1   | 10                   | 0            | 26             |
| P2   | 6                    | 17           | 19             |
| P3   | 3                    | 9            | 13             |
| P4   | 7                    | 20           | 26             |

AWT = (0 + 17 + 6 + 13) / 4 = 8.5
ATT = (26 + 19 + 13 + 26) / 4 = 18

## Common Pitfalls
-------------------

When solving scheduling problems, avoid these common pitfalls:

*   Failing to identify the type of scheduler used.
*   Incorrectly calculating waiting times and turnaround times.
*   Forgetting to use formulas to find AWT and ATT.

## Quick Summary
-----------------

Scheduling algorithms are crucial in operating systems. Deadlocks can lead to system crashes, data loss, and decreased productivity. SRTF and NP-SJF are two key concepts in this area:

| Algorithm | Advantages | Disadvantages |
| --- | --- | --- |
| SRTF    | Effective for varying task durations, minimizes waiting times | Requires continuous monitoring of task durations, can lead to increased context switching overhead |
| NP-SJF  | Simple to implement, minimizes context switching overhead | Inefficient for systems with varying task durations, can lead to increased waiting times |

Use formulas to find AWT and ATT:

\[ AWT = \frac{\sum\limits_{i=1}^{n} WT_i}{n} \]

\[ ATT = \frac{\sum\limits_{i=1}^{n} TAT_i}{n} \]