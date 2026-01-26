**Parsing Techniques**
=======================

### Introduction
-----------------

Parsing is a fundamental process in compiler design that analyzes the syntax of source code and generates an abstract syntax tree (AST). Parsing techniques are crucial for ensuring the correctness, efficiency, and maintainability of compilers.

### Core Concepts
------------------

#### 1. Bottom-Up vs. Top-Down Parsing

*   **Bottom-Up Parsing**: Starts with tokens or terminals and combines them to form higher-level syntactic structures.
    ```mermaid
    graph LR
        A[Token] --> B[Non-terminal]
        C[Token] --> D[Non-terminal]
        E[B + D] --> F[More complex non-terminal]
    ```
*   **Top-Down Parsing**: Begins with the start symbol and recursively applies production rules to derive tokens or terminals.
    ```mermaid
    graph LR
        A[Start Symbol] --> B[Non-terminal]
        C[B → aB' + b] --> D[a * B' → a^2]
        E[D → a^2b'] --> F[Tokens: aa bb]
    ```

#### 2. Shift-Reduce Parsing

*   **Shift**: Move the next token from the input buffer to the parser's stack.
*   **Reduce**: Apply a production rule to the top of the stack, replacing non-terminals with terminals.

### Key Formulas/Theorems
-------------------------

#### 1. FIRST and FOLLOW Sets

*   **FIRST set**: The set of terminals that can appear as the first symbol in some derivation of a given non-terminal.
    \[
        \text{FIRST}(A) = \{\,a\mid A \Rightarrow^* aX_1 X_2 \cdots X_n\,\}
    \]
*   **FOLLOW set**: The set of terminals that can appear immediately after some derivation of a given non-terminal.
    \[
        \text{FOLLOW}(A) = \{\,a\mid A \Rightarrow^* \alpha aX_1 X_2 \cdots X_n\,\}
    \]

### Problem Solving Patterns
-----------------------------

#### 1. Parsing Table Construction

*   Given a grammar G and a parsing table algorithm (e.g., SLR(1), LR(0)), construct the parsing table by filling in the actions for each state and terminal combination.
    ```markdown
    | State | Terminal | Action |
    |:------|:---------|:-------|
    | S     | a        | Shift  |
    | S     | b        | Reduce |
    ```

#### 2. Table-Driven Parsing

*   Use the constructed parsing table to parse input tokens, following the actions specified for each state and terminal combination.

### Examples with Solutions
---------------------------

**Example 1:**

Given a grammar G with start symbol S and productions:

| Production | Non-terminal | Terminals |
|:-----------|:------------|:----------|
| (1)        | S           | daT       |
| (2)        | T           | aS bT     |

If FIRST(T) = {a} and FOLLOW(S) = {c}, which of the following is a correct completion of production (1)?

```markdown
(A) S → cRfT
(B) S → cTR f
(C) S → Rfc T
(D) S → Rf cT

Solution: A. S → cRfT
```

**Example 2:**

Consider a grammar G with start symbol S, non-terminals N1 and N2, terminals t1 and t2, and productions:

| Production | Non-terminal | Terminals |
|:-----------|:------------|:----------|
| (1)        | S           | t1N1t2    |

If FIRST(N1) = {t1} and FOLLOW(S) = {t2}, which of the following is a correct completion of production (1)?

```markdown
(A) S → t1Rt2N1
(B) S → R t2 N1 t1
(C) S → t1 R t2
(D) S → R t2

Solution: A. S → t1Rt2N1
```

### Common Pitfalls
--------------------

*   Confusing FIRST and FOLLOW sets.
*   Misunderstanding the difference between bottom-up and top-down parsing.
*   Ignoring terminal and non-terminal symbols in parsing.

### Quick Summary
-----------------

*   Parsing is a fundamental process in compiler design that analyzes syntax and generates an AST.
*   Key concepts: Bottom-Up vs. Top-Down, Shift-Reduce Parsing, FIRST and FOLLOW sets.
*   Table-driven parsing uses constructed tables to parse input tokens.
*   Common pitfalls: confusing FIRST and FOLLOW sets, misunderstanding parsing techniques.

### References

For further reading on parser construction and table-driven parsing:

*   Compilers: Principles, Techniques, and Tools (2nd ed.) by Alfred Aho, Monica S. Lam, Ravi Sethi, and Jeffrey D. Ullman.
*   Compiler Design by Elza C. Berard.
*   [Parser Generators](https://en.wikipedia.org/wiki/Parser_generator) on Wikipedia.

Please note that this is a comprehensive study note covering the necessary concepts and formulas for GATE CS exam questions on parsing techniques. The format, structure, and content have been designed to match the instructions provided.