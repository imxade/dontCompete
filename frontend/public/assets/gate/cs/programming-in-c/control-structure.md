**Control Structure**
=====================

### Introduction

A control structure in programming determines the order of execution of program statements. It decides how a program should behave under different circumstances. Control structures are used to control the flow of a program's execution, allowing for more complex and dynamic behavior.

### Core Concepts

#### Conditional Statements (if-else)

Conditional statements allow a program to make decisions based on certain conditions. The general syntax is:
```c
if (condition) {
    // code to execute if condition is true
} else {
    // code to execute if condition is false
}
```
Example:
```c
int x = 5;
if (x > 10) {
    printf("x is greater than 10");
} else {
    printf("x is less than or equal to 10");
}
```
#### Loops (while, for)

Loops allow a program to execute a block of code repeatedly. The general syntax is:
```c
while (condition) {
    // code to execute while condition is true
}

for (initialization; condition; increment/decrement) {
    // code to execute in each iteration
}
```
Example:
```c
int i = 0;
while (i < 5) {
    printf("%d\n", i);
    i++;
}

for (int i = 0; i < 5; i++) {
    printf("%d\n", i);
}
```
#### Switch Statements

Switch statements allow a program to execute different blocks of code based on the value of an expression. The general syntax is:
```c
switch (expression) {
    case value1:
        // code to execute if expression equals value1
        break;
    case value2:
        // code to execute if expression equals value2
        break;
    default:
        // code to execute if none of the above cases match
}
```
Example:
```c
int x = 5;
switch (x) {
    case 1:
        printf("x is 1");
        break;
    case 2:
        printf("x is 2");
        break;
    default:
        printf("x is something else");
}
```
### Key Formulas/Theorems

N/A

### Problem Solving Patterns

1. **Identify the control structure**: Determine which type of control structure (if-else, while, for, switch) is being used in the problem.
2. **Understand the condition**: Analyze the condition under which the control structure will execute a particular block of code.
3. **Break down the logic**: Break down the problem into smaller sub-problems and identify the control structures required to solve each one.

### Examples with Solutions

**Q1:**

Consider the following C program:
```c
#include <stdio.h>

int main() {
    int a = 6;
    int b = 0;

    while (a < 10) {
        a = a / 12 + 1;
        a += b;
    }

    printf("%d", a);
    return 0;
}
```
What is the output of this program?

Solution:
The program gets stuck in an infinite loop because `a` is never decremented inside the while loop. Therefore, the condition `a < 10` will always be true.

**Q2:**

Consider the following C function definition:
```c
int f(int x, int y) {
    for (int i = 0; i < y; i++) {
        x *= x + y;
    }

    return x;
}
```
What is the return value of this function when called with inputs `20` and `10`?

Solution:
When called with inputs `20` and `10`, the function will execute the for loop 10 times. In each iteration, `x` is multiplied by `x + y`. Therefore, after 10 iterations, `x` will be equal to `(20^2)^10 = (400)^10`.

### Common Pitfalls

1. **Infinite loops**: Make sure that the condition in a while or for loop will eventually become false.
2. **Incorrect conditions**: Double-check that the conditions in if-else statements are correct.
3. **Missing breaks**: In switch statements, make sure to include a break statement after each case.

### Quick Summary

* Conditional statements (if-else) allow programs to make decisions based on certain conditions.
* Loops (while, for) allow programs to execute blocks of code repeatedly.
* Switch statements allow programs to execute different blocks of code based on the value of an expression.
* Infinite loops can occur when a condition is never false.

### Mermaid Diagrams

N/A