**Stack Theory Note**
======================

### Introduction
---------------

A stack is a fundamental data structure used to store and retrieve elements in a Last-In-First-Out (LIFO) order. It follows the principle of pushing elements onto the top of the stack and popping them from the same position.

### Core Concepts
-----------------

*   **Stack Operations**:
    *   `push(element)`: adds an element to the top of the stack.
    *   `pop()`: removes the top element from the stack and returns its value.
    *   `peek()`: returns the value of the top element without removing it.

### Key Formulas/Theorems
-------------------------

No specific formulas or theorems apply directly to stacks. However, understanding the time complexity of stack operations is crucial:

*   **Time Complexity**:
    *   `push(element)`: O(1)
    *   `pop()`: O(1)

### Problem Solving Patterns
-----------------------------

When dealing with stack-related problems, focus on the following patterns:

1.  **Simulation**: Understand the sequence of operations and simulate the behavior of a stack.
2.  **Visualization**: Draw diagrams to visualize the stack's structure and how elements are pushed and popped.

### Examples with Solutions
---------------------------

**Example 1:** Consider the sequence of operations `push(54); push(52); pop(); push(55); push(62); s = pop();`

1.  Push 54 onto the stack.
    ```
          +-------+
          |       |
          +-------+
           ^
           |
    ```
2.  Push 52 onto the stack.
    ```
          +-------+   +-------+
          |       |   |       |
          +-------+   +-------+
           ^            ^
           |            |
    ```
3.  Pop an element from the stack (54).
    ```
          +-------+
          |       |
          +-------+
           ^
           |
    ```
4.  Push 55 onto the stack.
    ```
          +-------+   +-------+
          |       |   |       |
          +-------+   +-------+
           ^            ^
           |            |
    ```
5.  Push 62 onto the stack.
    ```
          +-------+   +-------+   +-------+
          |       |   |       |   |       |
          +-------+   +-------+   +-------+
           ^            ^            ^
           |            |            |
    ```
6.  Pop an element from the stack (62).
    `s = 62`

**Example 2:** Consider the sequence of operations `enqueue(21); enqueue (24); dequeue(); enqueue(28); enqueue(32): q = dequeue();`

Note that this example is related to queues, not stacks.

1.  Enqueue 21 onto the queue.
    ```
          +--------+
          |        |
          +--------+ 
           ^
           |
    ```
2.  Enqueue 24 onto the queue.
    ```
          +--------+   +--------+
          |        |   |        |
          +--------+   +--------+ 
           ^            ^
           |            |
    ```
3.  Dequeue an element from the queue (21).
    ```
          +--------+   +--------+
          |        |   |       |
          +--------+   +--------+ 
           ^            ^
           |            |
    ```
4.  Enqueue 28 onto the queue.
    ```
          +--------+   +--------+   +--------+
          |        |   |       |   |        |
          +--------+   +--------+   +--------+ 
           ^            ^            ^
           |            |            |
    ```
5.  Enqueue 32 onto the queue.
    ```
          +--------+   +--------+   +--------+   +--------+
          |        |   |       |   |        |   |        |
          +--------+   +--------+   +--------+   +--------+ 
           ^            ^            ^            ^
           |            |            |            |
    ```
6.  Dequeue an element from the queue (24).
    `q = 24`

### Common Pitfalls
-------------------

*   Confusing LIFO and FIFO order.
*   Not considering the initial empty stack or queue.

### Quick Summary
-----------------

*   A stack follows the LIFO principle.
*   Key operations: push, pop, peek.
*   Time complexity of push and pop: O(1).
*   Simulation and visualization are essential problem-solving strategies.