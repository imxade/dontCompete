**Regular Expressions and Finite Automata Theory**
=====================================================

### Introduction
-----------------

Regular expressions (RE) are a formal language to describe patterns in strings. They are used extensively in database design, querying, and validation. Finite automata (FA) theory provides a mathematical foundation for REs, enabling the study of their properties and behavior.

### Core Concepts
------------------

#### Regular Expressions

A regular expression is a pattern string that describes a set of possible input strings.

*   **Concatenation**: `ab` matches any string consisting of `a` followed by `b`.
*   **Union**: `a | b` matches any string matched by either `a` or `b`.
*   **Kleene Star**: `a\*` matches any number (including zero) of occurrences of `a`.

#### Finite Automata

A finite automaton is a mathematical model that can be in one of a finite number of states.

*   **Deterministic Finite Automata (DFA)**: A DFA has a single initial state and a set of transition rules.
*   **Non-Deterministic Finite Automata (NFA)**: An NFA has multiple possible next states for each input symbol.

### Key Formulas/Theorems
---------------------------

#### Kleene's Theorem

The following are equivalent:

1.  A language is regular.
2.  There exists a DFA that accepts the language.
3.  There exists an RE that describes the language.

**Mathematical Representation**
```latex
L \in REG \iff \exists M = (Q, q_0, F, \Sigma, \delta) \text{ s.t. }
    L = \{ w \mid \exists q \in F, \delta(q_0, w) = q \}
```

### Problem Solving Patterns
---------------------------

1.  **Pattern Matching**: Identify the pattern described by the RE and match it against the input string.
2.  **State Transition Diagrams**: Draw state transition diagrams for DFAs or NFAs to visualize their behavior.

### Examples with Solutions
-----------------------------

#### Example: Matching Binary Numbers Divisible by 3

We need to find an RE that matches all binary numbers divisible by 3.

**Step 1:** Identify the pattern.

A number is divisible by 3 if the sum of its digits is divisible by 3. In binary, this means:

*   `0` is divisible by 3.
*   `1` followed by any number of `01`s and ending with `0` is also divisible by 3 (e.g., `10100`, `11010`, etc.).

**Step 2:** Construct the RE.

Using the pattern identified, we can construct the following RE:

```mermaid
graph LR
A[0] -->|ε|> B[1(01*0)*]
```

The resulting RE is: `(0 + 1(01*0)*)*`

### Common Pitfalls
---------------------

1.  **Overcomplicating the Pattern**: Avoid unnecessary complexity in constructing the RE.
2.  **Failing to Identify Patterns**: Regular expressions can be difficult to read; make sure you understand the pattern described.

### Quick Summary
------------------

*   Regular Expressions (RE) are a formal language for describing patterns in strings.
*   Finite Automata (FA) theory provides a mathematical foundation for REs.
*   Key concepts include concatenation, union, Kleene star, DFA, and NFA.
*   Practice problem-solving using pattern matching and state transition diagrams.

**References**

*   Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2006). Introduction to automata theory, languages, and computation. Addison-Wesley.
*   Sipser, M. (1997). Introduction to the theory of computation. PWS Publishing.

Note: The references provided are for general knowledge only; they may not be directly related to the specific questions covered in this study note.