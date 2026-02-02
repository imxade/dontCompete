**Operating Systems: Process Scheduling**
=====================================

**Introduction**
---------------

Process scheduling is a critical aspect of operating systems that manages the execution of processes on a single computer or within a network. The goal is to allocate system resources effectively, ensuring each process receives its turn to execute while minimizing delays.

**Core Concepts**
-----------------

### Process States

A process can be in one of four states:

1. **New**: Created but not yet started
2. **Ready**: Waiting for CPU allocation
3. **Running**: Currently executing on the CPU
4. **Waiting (Blocked)**: Suspended until an event occurs, such as I/O completion

### Scheduling Algorithms

These algorithms determine which process to execute next:

1. **FCFS (First-Come-First-Served)**: Processes are executed in order of arrival.
2. **SJF (Shortest Job First)**: The shortest process is executed first.
3. **SRTF (Shortest Remaining Time First)**: The process with the shortest remaining execution time is executed next.
4. **Priority Scheduling**: High-priority processes are executed before lower-priority ones.

### Process Synchronization

Coordinating access to shared resources ensures data consistency:

1. **Mutual Exclusion**: Only one process can access a resource at a time.
2. **Semaphore**: A variable controlling access to shared resources.
3. **Monitors**: High-level synchronization construct using semaphores.

**Key Formulas/Theorems**
-------------------------

### Little's Law

Average number of processes in the system (L) is related to average arrival rate (λ) and average service time (T):

$$L = \lambda T$$

### M/M/1 Queueing Model

Mean response time (R) for a single-server queue:

$$R = \frac{\rho}{2(1-\rho)}$$

where ρ is the utilization factor.

**Problem Solving Patterns**
---------------------------

When solving process scheduling problems, consider:

1. **Process States**: Ensure you understand each state's implications.
2. **Scheduling Algorithms**: Choose the correct algorithm based on given constraints (e.g., FCFS for shortest remaining time).
3. **Process Synchronization**: Use semaphores or monitors to coordinate access to shared resources.

**Examples with Solutions**
---------------------------

### Example 1

Suppose we have three processes (P1, P2, P3) and two CPU-bound tasks A and B:

| Process | Task | Arrival Time |
| --- | --- | --- |
| P1     | A   | 0          |
| P2     | B   | 2          |
| P3     | A   | 4          |

If we use FCFS scheduling, the order of execution will be:

P1 (A), P2 (B), P3 (A)

### Solution

This example demonstrates how to apply FCFS scheduling.

**Common Pitfalls**
-------------------

Be cautious when dealing with:

1. **Starvation**: When a process is denied access to resources for an extended period.
2. **Deadlocks**: A situation where processes are blocked indefinitely due to mutual resource holding.

**Quick Summary**
-----------------

* Process states: New, Ready, Running, Waiting
* Scheduling algorithms: FCFS, SJF, SRTF, Priority Scheduling
* Process synchronization: Mutual Exclusion, Semaphore, Monitor
* Key formulas/theorems: Little's Law, M/M/1 Queueing Model

By mastering these concepts and techniques, you'll be well-prepared to tackle process scheduling questions in the GATE CS exam.