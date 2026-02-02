Concurrency and Synchronization
=============================

Introduction
------------

In concurrent systems, multiple processes or threads share resources and execute simultaneously. However, this can lead to unexpected behavior if not properly synchronized. This topic covers the fundamental concepts of concurrency and synchronization.

Core Concepts
---------------

### Semaphores

A semaphore is a variable that controls access to shared resources by multiple threads. It acts as a gatekeeper, ensuring only one thread can access the resource at a time.

*   **Binary Semaphore**: A binary semaphore has two states: 0 or 1.
*   **Counting Semaphore**: A counting semaphore has a count value, indicating how many threads can access the resource simultaneously.

```mermaid
graph LR
    A[Thread] --> B[Wait(Semaphore)]
    C[Thread] --> D[Wait(Semaphore)]
    E[Resource] --> F[Access]
```

### Synchronization

Synchronization is the process of coordinating access to shared resources among multiple threads. It ensures that only one thread can access a resource at a time, preventing conflicts and ensuring data integrity.

*   **Mutual Exclusion**: Ensures only one thread can access a resource at a time.
*   **Starvation-Free Scheduling**: Ensures all threads have a fair chance to access the resource.

Key Formulas/Theorems
----------------------

### Critical Section Problem

The critical section problem states that when multiple threads share resources, each thread has a critical section where it needs exclusive access to the resource. The challenge is to design an algorithm that ensures mutual exclusion while minimizing overhead.

*   **Peterson's Algorithm**: A solution to the critical section problem using two variables: `turn` and `flag`.

```latex
\begin{algorithm}
  \caption{Peterson's Algorithm}
  \label{alg:petersons}
  \begin{algorithmic}
    \STATE $turn = 0$
    \FOR {each process $P_i$}
      \IF {$i$ has exclusive access to the resource}
        \STATE $\text{enter critical section}$
        \STATE $\text{do work}$
        \STATE $\text{exit critical section}$
      \ENDIF
    \ENDFOR
  \end{algorithmic}
\end{algorithm}
```

Problem Solving Patterns
-------------------------

### Analyzing Synchronization Algorithms

To analyze synchronization algorithms, follow these steps:

1.  **Identify Shared Resources**: Determine which resources are shared among threads.
2.  **Determine Access Requirements**: Identify the critical sections where each thread needs exclusive access to the resource.
3.  **Evaluate Algorithm Effectiveness**: Assess whether the algorithm ensures mutual exclusion and minimizes overhead.

Examples with Solutions
-----------------------

### Example: Peterson's Algorithm

Suppose we have two threads, `T1` and `T2`, sharing a semaphore `s`. Both threads need exclusive access to the resource during their critical sections.

```python
import threading

s = threading.Semaphore(1)  # binary semaphore initialized to 1

def T1():
    s.acquire()  # wait for semaphore
    print("T1 has exclusive access")
    # do work
    s.release()  # signal semaphore

def T2():
    s.acquire()  # wait for semaphore
    print("T2 has exclusive access")
    # do work
    s.release()  # signal semaphore

t1 = threading.Thread(target=T1)
t2 = threading.Thread(target=T2)

t1.start()
t2.start()

t1.join()
t2.join()
```

Common Pitfalls
-----------------

*   **Deadlocks**: Avoid creating situations where two or more threads are blocked indefinitely, each waiting for the other to release a resource.
*   **Starvation**: Ensure all threads have a fair chance to access shared resources.

Quick Summary
--------------

*   **Semaphores**: Variables controlling access to shared resources among multiple threads.
*   **Synchronization**: Coordinating access to shared resources among multiple threads.
*   **Peterson's Algorithm**: A solution to the critical section problem using two variables: `turn` and `flag`.
*   **Deadlocks** and **Starvation**: Avoid situations where threads are blocked indefinitely or have an unfair chance to access shared resources.