**Finite Automata**
================

### Introduction
---------------

A finite automaton (FA) is a mathematical model used to recognize patterns in strings of symbols. It consists of a set of states, transitions between these states based on input symbols, and an accepting state that indicates whether the input string belongs to a language or not.

### Core Concepts
-----------------

#### States
-----

*   A state in an FA represents a specific condition or situation.
*   An FA can have multiple states, each with its own set of properties.
*   The number of states determines the complexity of the FA.

#### Transitions
------------

*   A transition is a change from one state to another based on input symbols.
*   Each state has an associated set of possible transitions, which are defined by the transition function.
*   The transition function maps each state and input symbol to the next state.

#### Accepting States
-------------------

*   An accepting state indicates that the input string belongs to a language.
*   If the FA ends up in an accepting state after processing the entire input string, it accepts the string.
*   Multiple states can be designated as accepting states.

### Key Formulas/Theorems
-------------------------

$$ \delta(q, a) = p $$

Transition function: $\delta$ maps each state $q$, input symbol $a$, to the next state $p$.

### Problem Solving Patterns
-----------------------------

1.  **Deterministic Finite Automata (DFA)**:
    *   A DFA is an FA that has exactly one transition from each state for each possible input symbol.
2.  **Non-Deterministic Finite Automata (NFA)**:
    *   An NFA can have multiple transitions from a single state for the same input symbol.
3.  **Minimalization**:
    *   The process of converting an FA to its minimal equivalent form, which has fewer states while maintaining the same language recognition.

### Examples with Solutions
---------------------------

1.  **DFA Example**
    ```mermaid
    graph LR;
        A[Start] -->|0|> B[State 2]
        B -->|1|> C[State 3]
        C -->|0|> D[Accepting State]
    ```
    This DFA recognizes the language $\{ w \mid w = 01^n, n \geq 0\}$.

2.  **NFA Example**
    ```mermaid
    graph LR;
        A[Start] -->|0|> B[State 2]
        A -->|1|> C[State 3]
        B -->|0|> D[Accepting State]
    ```
    This NFA recognizes the language $\{ w \mid w = 01^n, n \geq 0\}$.

### Common Pitfalls
----------------------

*   Confusing between DFA and NFA.
*   Not considering all possible transitions.
*   Failing to minimize the FA.

### Quick Summary
-----------------

*   Finite Automata (FAs) recognize patterns in strings of symbols.
*   States, transitions, and accepting states are key components of an FA.
*   Deterministic and non-deterministic FAs have different properties.
*   Minimalization is essential for optimizing FAs.

Note: This theory note aims to cover the concepts and formulas required to solve questions like the one provided. It will be updated as more questions are analyzed, ensuring that every concept tested in the source questions is explained.