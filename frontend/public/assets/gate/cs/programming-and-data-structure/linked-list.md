# Linked List Theory Note
## Introduction

A linked list is a linear collection of data elements whose order is not given by their physical placement in memory, but rather by the order in which they were inserted. It is a dynamic data structure consisting of nodes, each pointing to the next node.

## Core Concepts

### Node Structure

A node in a linked list typically consists of two parts:

- **Data**: The actual value stored in the node.
- **Reference** or **Pointer**: A link to the next node in the sequence.

```mermaid
graph LR
Node[Data] -->|Pointer|> NextNode[Data]
```

### Types of Linked Lists

There are several types of linked lists:

- **Singly Linked List**: Each node only points to the next node.
- **Doubly Linked List**: Each node points to both the previous and next nodes.

## Key Formulas/Theorems

* None specific to linked lists, but general data structure concepts apply.

## Problem Solving Patterns

### Reversing a Linked List

To reverse a linked list in-place (using O(1) extra space), follow these steps:

1. **Initiate three pointers**:
   - `prev`: pointing to the previous node.
   - `current`: pointing to the current node (start of the list).
   - `next`: pointing to the next node.

2. **Iterate through the linked list**, updating the references as follows for each iteration:

   ```markdown
   while(current != None):
       # Store the 'next' pointer before updating it.
       next_node = current.next

       # Update the 'current' node's reference to point to 'prev'.
       current.next = prev

       # Move both 'prev' and 'current' one step forward in the list.
       prev = current
       current = next_node

   # At this stage, 'prev' will be pointing to the new first node of the reversed list.
   ```

### Reversing a Linked List (Alternate Approach)

Another approach to reverse a linked list is by using recursion:

```markdown
def reverse_list(head):
    if head == None or head.next == None:
        return head

    # Reverse the rest of the list
    new_head = reverse_list(head.next)

    # Put the current node at the end of the reversed list
    head.next.next = head
    head.next = None

    return new_head
```

## Examples with Solutions

### Example 1: Reversing a Linked List

Given a singly linked list `1 -> 2 -> 3`, reverse it.

**Solution**: Apply the iterative approach outlined above.

- **Step 1:** Initialize three pointers, with `prev = None`, `current = head` (the first node), and `next_node`.
- **Step 2-5:** Iterate through the list, updating references as shown in the iterative method.

**Output**: The reversed linked list is `3 -> 2 -> 1`.

### Example 2: Reversing a Linked List Recursively

Given a singly linked list `1 -> 2 -> 3`, reverse it using recursion.

**Solution**:

- **Base Case:** If the head or its next node is null, return the current head as there's nothing to reverse.
- **Recursive Call:** Reverse the rest of the list (from `head.next` onwards) by recursively calling `reverse_list`.
- **Reversing Step:** Update the references for the current node (`head`) and the reversed rest of the list.

**Output**: The reversed linked list is `3 -> 2 -> 1`.

## Common Pitfalls

* Not iterating through the entire list when reversing.
* Incorrectly updating or not updating the next pointer.
* Confusing doubly linked lists with singly linked lists in reversal logic.

## Quick Summary

- **Linked List Basics**:
  - Nodes have data and a reference to the next node.
  - Singly and doubly linked lists exist.
- **Reversing Linked Lists**:
  - Iterate through, updating pointers for each node (iterative approach).
  - Use recursion with base case handling and recursive calls for an alternate solution.
- **Key Concepts**: Node structure, types of linked lists, reversing techniques.