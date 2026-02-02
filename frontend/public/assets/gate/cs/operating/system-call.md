**System Call**
================

### Introduction
---------------

A system call is an interface between a program and the operating system (OS) that allows the program to request services from the OS. System calls are used to perform tasks such as process creation, file I/O, network communication, and more.

### Core Concepts
-----------------

In a Unix/Linux environment, system calls are invoked by the C library functions listed below:

*   `sleep`: Suspends the execution of a program for a specified amount of time.
*   `exit`: Terminates the current process.
*   `fork`: Creates a new process that is an exact copy of the calling process.
*   `exec`: Replaces the contents of the memory space of a process with a new program.

When a system call is invoked, the following sequence occurs:

1.  The C library function calls the system call interface (e.g., `syscall` on Linux).
2.  The system call interface invokes the corresponding kernel routine.
3.  The kernel routine performs the requested action and returns control to the system call interface.
4.  The system call interface returns control to the C library function, which then returns to the program.

### Key Formulas/Theorems
---------------------------

None specific to this topic.

### Problem Solving Patterns
-----------------------------

1.  **Identify System Calls**: Recognize which C library functions invoke system calls.
2.  **Understand Kernel Routines**: Be aware of the kernel routines corresponding to each system call.

### Examples with Solutions
---------------------------

Q: Which of the following standard C library functions will always invoke a system call when executed from a single-threaded process in a UNIX/LINUX Operating system?

A:
```mermaid
graph LR
    Program-->|Invoke| C Library Function (e.g., sleep)
    C Library Function -->|Invoke System Call Interface| System Call Interface
    System Call Interface -->|Invoke Kernel Routine| Kernel Routine
```

### Common Pitfalls
-------------------

1.  **Confusing library functions with system calls**: Be aware of the distinction between C library functions and system calls.
2.  **Not considering kernel routines**: Remember that system calls are implemented as kernel routines.

### Quick Summary
------------------

*   System call: interface between program and OS.
*   System call invocation sequence:
    *   C library function calls system call interface
    *   System call interface invokes kernel routine
    *   Kernel routine performs action, returns control to system call interface
    *   System call interface returns control to C library function
*   Recognize which C library functions invoke system calls (e.g., `sleep`, `exit`).

Note: This content is subject to modification or expansion as needed.