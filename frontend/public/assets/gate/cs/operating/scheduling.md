**Scheduling**
================

### Introduction

Scheduling is a crucial component of Operating Systems that manages the allocation of system resources, particularly CPU time, to processes or threads. A scheduler decides which process should run next on the CPU, ensuring efficient and fair utilization of system resources.

### Core Concepts

#### Types of Schedulers

1. **Non-Preemptive Scheduler**: Once a process is allocated the CPU, it runs until completion without interruptions.
2. **Preemptive Scheduler**: The operating system can interrupt a running process to allocate the CPU to another process.

#### Scheduling Algorithms

1. **First-Come-First-Served (FCFS)**: Processes are executed in the order they arrive.
2. **Shortest Job First (SJF)**: The process with the shortest burst time is executed next.
3. **Priority Scheduling**: Processes are assigned priorities, and the highest-priority process runs first.

### Key Formulas/Theorems

* Average waiting time (WT) in a non-preemptive scheduler can be calculated using the following formula:

$$\text{Average WT} = \frac{\sum(\text{Burst Time})}{n}$$

where $n$ is the number of processes and $\text{Burst Time}$ is the CPU burst time for each process.

* For a SJF scheduler, the average waiting time can be calculated using:

$$\text{Average WT}_{SJF} = \frac{\sum(\text{Burst Time})^2}{2n\bar{x}}$$

where $\bar{x}$ is the average burst time of all processes.

### Problem Solving Patterns

1. **Calculate Average Waiting Time**: Use the formula to calculate the average waiting time for a given set of processes.
2. **Determine Scheduling Algorithm**: Identify the type of scheduler (non-preemptive or preemptive) and apply the corresponding algorithm.
3. **Analyze Gantt Charts**: Understand how to read and analyze Gantt charts, which represent the schedule of processes over time.

### Examples with Solutions

**Example 1: Non-Preemptive Scheduler**

Three processes arrive at time zero with CPU bursts time of 16, 20, and 10 milliseconds. Calculate the average waiting time for this set of processes.

```python
# Given data
processes = [16, 20, 10]
n = len(processes)

# Calculate average waiting time using the formula
average_wt = sum(processes) / n

print(f"The average waiting time is {int(average_wt)} milliseconds.")
```

**Example Solution:**

The output will be:

`The average waiting time is 12 milliseconds.`

### Common Pitfalls

1. **Forgetting to round the result**: Always remember to round the result to the nearest integer as required.
2. **Incorrectly applying formulas**: Double-check the formulas and ensure they match the problem requirements.

### Quick Summary

* Scheduling is a crucial component of Operating Systems that manages CPU time allocation.
* Non-preemptive schedulers run processes until completion without interruptions.
* Average waiting time can be calculated using the formula: $\frac{\sum(\text{Burst Time})}{n}$.
* SJF schedulers use the formula: $\frac{\sum(\text{Burst Time})^2}{2n\bar{x}}$ to calculate average waiting time.

### Visuals

```mermaid
graph LR
A[Start] --> B[Process A]
C[Burst Time = 16ms] --> D[Wait for Process A to finish]
E[Process B arrives with Burst Time = 20ms] --> F[Run Process B after Process A finishes]
G[Process C arrives with Burst Time = 10ms] --> H[Run Process C after Process B finishes]
