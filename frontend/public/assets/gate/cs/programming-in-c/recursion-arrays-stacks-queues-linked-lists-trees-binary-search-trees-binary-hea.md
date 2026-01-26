**Theory Note: Data Structures and File Input/Output**
=====================================================

**Introduction**
---------------

Data structures are essential for efficient programming, enabling us to manage and manipulate large amounts of data effectively. This note covers key concepts including recursion, arrays, stacks, queues, linked lists, trees, binary search trees, binary heaps, graph theory, and file input/output.

**Core Concepts**
-----------------

### 1. Recursion

Recursion is a programming technique where a function calls itself repeatedly until it reaches the base case, solving problems by breaking them down into smaller sub-problems of the same type.

*   A recursive function has two components: a **base case**, which stops the recursion, and a **recursive case**, which breaks down the problem.
*   Recursion can be used to solve problems that have an inherent hierarchical structure.

### 2. Arrays

Arrays are collection data structures where elements of the same data type are stored in contiguous memory locations.

*   Array indexing allows for efficient access to elements using their index as a key.
*   Common array operations include insertion, deletion, and search.

### 3. Stacks

A stack is a last-in-first-out (LIFO) data structure that supports two primary operations: **push** (add an element to the top of the stack) and **pop** (remove the top element from the stack).

*   Stack implementation can be done using arrays or linked lists.
*   Stacks are useful for parsing expressions, evaluating postfix notation, and implementing recursive algorithms.

### 4. Queues

A queue is a first-in-first-out (FIFO) data structure that supports two primary operations: **enqueue** (add an element to the end of the queue) and **dequeue** (remove the front element from the queue).

*   Queue implementation can be done using arrays or linked lists.
*   Queues are useful for job scheduling, print queues, and network protocols.

### 5. Linked Lists

A linked list is a dynamic collection data structure where elements are linked together via pointers.

*   Linked lists allow for efficient insertion and deletion of elements at any position.
*   Common operations include traversal and search.

### 6. Trees

A tree is a hierarchical data structure composed of nodes, with each node having child nodes except the root node.

*   Trees support various traversals including in-order, pre-order, and post-order.
*   Binary trees are a special type of tree where each node has at most two children.

### 7. Binary Search Trees (BSTs)

A BST is a binary tree where for every node, all elements in the left subtree are less than the current node, and all elements in the right subtree are greater than the current node.

*   BSTs support efficient search, insertion, and deletion operations with an average time complexity of O(log n).

### 8. Binary Heaps

A binary heap is a complete binary tree where for every node, either all children are smaller (min-heap) or larger (max-heap) than the current node.

*   Heaps support efficient insertion and deletion operations with an average time complexity of O(log n).
*   Common applications include priority queues and sorting algorithms.

### 9. Graph Theory

Graph theory is a branch of mathematics that deals with sets of objects called vertices connected by edges.

*   Graphs can be classified as directed or undirected, weighted or unweighted.
*   Algorithms for graph traversal include DFS (Depth-First Search) and BFS (Breadth-First Search).

### 10. File Input/Output

File input/output operations involve reading data from files and writing data to files.

*   Common file functions include `fopen()`, `fread()`, `fwrite()`, and `fclose()`.

**Key Formulas/Theorems**
-------------------------

| Formula/Theorem | Description |
| --- | --- |
| $T(n) = O(log n)$ | Time complexity of BST operations (search, insertion, deletion) |
| $T(n) = O(log h)$ | Time complexity of heap operations (insertion, deletion) |
| $T(n) = O(V + E)$ | Time complexity of graph traversal algorithms (DFS, BFS) |

**Problem Solving Patterns**
---------------------------

1.  **Recursion**: Identify the base case and recursive case.
2.  **Arrays**: Use indexing for efficient access to elements.
3.  **Stacks**: Implement using arrays or linked lists; use push and pop operations.
4.  **Queues**: Implement using arrays or linked lists; use enqueue and dequeue operations.
5.  **Linked Lists**: Focus on insertion and deletion at any position.

**Examples with Solutions**
---------------------------

### Example 1: Recursion

```c
#include <stdio.h>

int factorial(int n) {
    if (n == 0 || n == 1)
        return 1; // base case
    else
        return n * factorial(n - 1); // recursive case
}

int main() {
    printf("%d\n", factorial(5));
    return 0;
}
```

### Example 2: Arrays

```c
#include <stdio.h>

void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    print_array(arr, sizeof(arr) / sizeof(arr[0]));
    return 0;
}
```

### Example 3: Stacks

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10

typedef struct {
    int data[MAX_SIZE];
    int top;
} Stack;

void push(Stack* stack, int element) {
    if (stack->top == MAX_SIZE - 1)
        printf("Stack overflow!\n");
    else
        stack->data[++(stack->top)] = element;
}

int pop(Stack* stack) {
    if (stack->top == -1)
        printf("Stack underflow!\n");
    else
        return stack->data[--(stack->top)];
}

void main() {
    Stack stack;
    push(&stack, 5);
    push(&stack, 10);
    printf("%d\n", pop(&stack));
}
```

### Example 4: Queues

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10

typedef struct {
    int data[MAX_SIZE];
    int front, rear;
} Queue;

void enqueue(Queue* queue, int element) {
    if ((queue->rear + 1) % MAX_SIZE == queue->front)
        printf("Queue is full!\n");
    else
        queue->data[(++(queue->rear)) % MAX_SIZE] = element;
}

int dequeue(Queue* queue) {
    if (queue->front == -1 || queue->rear == queue->front - 1)
        printf("Queue is empty!\n");
    else
        return queue->data[queue->front++];
}

void main() {
    Queue queue;
    enqueue(&queue, 5);
    enqueue(&queue, 10);
    printf("%d\n", dequeue(&queue));
}
```

### Example 5: Linked Lists

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

void insert_at_head(Node** head, int element) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = element;
    new_node->next = *head;
    *head = new_node;
}

int main() {
    Node* head = NULL;
    insert_at_head(&head, 5);
    insert_at_head(&head, 10);
    printf("%d\n", head->data);
}
```

**Common Pitfalls**
------------------

1.  **Recursion**: Failing to identify the base case can lead to stack overflow.
2.  **Arrays**: Using an index out of bounds can cause undefined behavior.
3.  **Stacks**: Implementing without considering LIFO order can lead to incorrect results.
4.  **Queues**: Implementing without considering FIFO order can lead to incorrect results.

**Quick Summary**
-----------------

| Data Structure | Time Complexity | Space Complexity |
| --- | --- | --- |
| Recursion | O(log n) | O(n) |
| Arrays | O(1) | O(n) |
| Stacks | O(1) | O(n) |
| Queues | O(1) | O(n) |
| Linked Lists | O(1) | O(n) |
| Trees | O(log n) | O(n) |
| BSTs | O(log n) | O(n) |
| Binary Heaps | O(log n) | O(n) |
| Graphs | O(V + E) | O(V + E) |

Note: This note provides a comprehensive overview of data structures and file input/output operations in C.