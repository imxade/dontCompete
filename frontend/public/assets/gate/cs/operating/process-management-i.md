**Process Management I**
=========================

### Introduction

Process management is a crucial aspect of operating systems that deals with creating, scheduling, and managing processes within the system. A process is an executing instance of a program, and process management ensures that these instances are executed efficiently and safely.

### Core Concepts

*   **Processes**: An executing instance of a program.
*   **Threads**: Lightweight processes that share memory with other threads in the same process.
*   **Context Switching**: The process of switching between two or more processes or threads to execute them on the CPU.
*   **Synchronization**: Mechanisms used to coordinate access to shared resources among multiple processes or threads.

### Key Formulas/Theorems

No specific formulas are applicable for this topic. However, understanding of synchronization primitives like Semaphores, Monitors, and Locks is crucial.

### Problem Solving Patterns

When dealing with process management questions:

1.  **Understand the question**: Identify the key concepts involved (processes, threads, context switching, synchronization).
2.  **Identify synchronization points**: Determine where processes or threads interact with each other.
3.  **Analyze access patterns**: Consider how shared resources are accessed and updated by different processes or threads.

### Examples with Solutions

**Example 1**

Suppose two threads, `T1` and `T2`, update shared variables `a` and `b`. Initially, `a = b = 0`.

```markdown
// T1
a = a + 1;
b = b * 1;

// T2
a = a * 2;
b = b + 2;
```

**Solution**

The possible combinations of values for `a` and `b` after both threads finish execution are:

*   `(4, 4)`
*   `(3, 3)`

This is because the updates to `a` and `b` by each thread can occur in any order.

### Common Pitfalls

1.  **Overlooking synchronization**: Failing to consider how shared resources are accessed and updated.
2.  **Ignoring context switching**: Not accounting for the possibility of context switching between threads.
3.  **Incorrectly analyzing access patterns**: Misunderstanding how processes or threads interact with each other.

### Quick Summary

*   Processes: Executing instances of programs
*   Threads: Lightweight processes sharing memory
*   Context Switching: Switching between processes/threads on CPU
*   Synchronization: Coordinating access to shared resources among multiple processes/threads

**Note**: This summary is not a complete list of all key points, but it covers the essential concepts related to Process Management I.