# Combinatorial Mathematics for GATE CS: Teams and Selection
==============================================

## Introduction
-------------

Combinatorial mathematics, a fundamental aspect of discrete mathematics, deals with counting problems that involve selecting or arranging objects. In this note, we focus on forming teams and selections, specifically applying to the GATE CS exam context.

## Core Concepts
---------------

### Selection Principle

*   The selection principle states that for each element in a set, there are multiple ways it can be included in combinations.
*   Understanding this concept is crucial when dealing with problems involving team formations or selections.

### Counting Methods

*   We use counting methods to determine the number of ways an object can be selected or arranged. These include:
    *   **Multiplication Principle**: When each selection results in a unique combination, we multiply the number of choices for each step.
        ```
        n(A ∩ B) = n(A) \* n(B)
        ```
    *   **Addition Principle**: When an object can be selected from multiple sets, we add the number of choices.
        ```
        n(A ∪ B) = n(A) + n(B)
        ```

## Key Formulas/Theorems
-------------------------

### Combinations (n choose k)

*   The formula for combinations is:
    ```
    C(n, k) =  \frac{n!}{k!(n-k)!}
    ```
*   When \(k = 1\), we have permutations.

### Permutations

*   For arranging objects in a specific order, we use the permutation formula:
    ```
    P(n, k) = \frac{n!}{(n-k)!}
    ```

## Problem Solving Patterns
---------------------------

### Team Formations with Restrictions

*   When forming teams with restrictions (e.g., Q must be in each team), calculate combinations considering the restriction.
*   Use the multiplication principle when multiple events occur together.

### Example 1: Team Formation without Restriction

Suppose we want to form a team of 3 from 5 individuals. Using the combination formula:

\[ C(5, 3) = \frac{5!}{3!(5-3)!} = \frac{120}{6*2} = 10 \]

### Example 2: Team Formation with Restriction

If Q must be in each team of size exceeding one formed from P, Q, R, and S:

*   Calculate the number of teams that can be formed without considering Q first.
*   Then consider the remaining individuals to form teams with Q as a member.

### Solution for Q1 (ee_2020_8):

Given P, Q, R, S are 4 individuals. We want to find how many teams of size exceeding one can be formed with Q as a member:

*   First, calculate the total number of teams without restriction: C(4,2) = \frac{24}{2*2} = 6
*   Since we need Q in each team, consider Q already chosen and form combinations from the remaining individuals: C(3,1) = 3
*   Multiply by the number of ways to select Q as a member (since this can happen for all possible teams): 6 \times 3 = 18

However, we need teams with size exceeding one. Thus:

*   Exclude the case where no other members are selected: 1 team with just Q
*   Subtract this from our previous result: 18 - 1 = 17 (not a valid option) However, looking at the original problem statement and answer options provided for ee_2020_8, we find that teams of size greater than one would indeed include scenarios where only two individuals are chosen. Hence correcting our understanding to reflect the scenario properly.

Upon revisiting the rationale with correct interpretation:

*   We initially consider combinations from 4 individuals (excluding Q) for all team sizes:
    *   For a team of 2, C(3, 2) = \frac{6}{2} = 3 ways.
    *   For a team of 3, C(3, 3) = 1 way.
*   In each scenario, Q can be added in multiple ways since Q is always a member. Hence the initial multiplication principle approach leads us to find the correct method.

To directly compute as per question:
- Select Q and then choose one more person from three options: C(4,2) = 6, because we are considering groups of size greater than one (which means at least two people). So for each group selected by combination formula with four elements, there is a possibility that the team could be formed including the third element.