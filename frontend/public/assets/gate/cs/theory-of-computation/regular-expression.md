# Regular Expressions
=====================================

## Introduction
---------------

Regular expressions are a pattern-matching language used to describe search patterns in strings. They are commonly used in text processing, data validation, and string manipulation. In this note, we will cover the theoretical concepts of regular expressions and their application in solving problems related to the Theory of Computation.

## Core Concepts
-----------------

*   **Regular Expression**: A pattern-matching language that describes a search pattern in strings.
*   **Alphabet**: The set of characters used in the regular expression. It can be any finite set of symbols, such as {a, b, c}.
*   **String**: A sequence of characters from the alphabet.
*   **Language**: A set of strings.

## Key Formulas/Theorems
-------------------------

The following are key concepts related to regular expressions:

$$
\begin{align*}
L(S) &amp;= \{\sigma \in S^* \mid \sigma \text{ matches the pattern } p\}\\
p|q &amp;\equiv L(p) \cup L(q)\\
p \cdot q &amp;\equiv L(p) \circ L(q)\\
p^* &amp;= \{\epsilon\} \cup (L(p))^+\\
p^+ &amp;= L(p)^+
\end{align*}
$$

## Problem Solving Patterns
---------------------------

When solving problems related to regular expressions, the following patterns can be useful:

### Pattern 1: Matching a String of Characters

*   Use `a*b` or `b*a` to match any string of characters.
*   Use `(ab)*` to match any string consisting of `ab`s.

Example:

Given the language represented by the regular expression $(ab)^*$, find the number of strings in the language that have length 3.

Solution:
```mermaid
graph LR;
    A[Start] --> B[Length 3]
    C[(ab)^*] --> D[Match (ab) three times]
    E[Match (ab) three times] --> F[Count 4!/(3!*1!) = 4]
```

### Pattern 2: Counting Strings of a Certain Length

*   Use the formula `n!/((k-1)! * k)` to count strings of length `n` consisting of `k` blocks.
*   Use the formula `n!/((n-k)! * k)` to count strings of length `n` with exactly `k` matches.

Example:

Given the language represented by the regular expression `(ab)*(ba)*`, find the number of strings in the language that have length 4 and consist of two blocks.

Solution:
```mermaid
graph LR;
    A[Start] --> B[Length 4]
    C[(ab)*(ba)*] --> D[Match (ab) or (ba) twice]
    E[Match (ab) or (ba) twice] --> F[Count 4!/((2!*2!)) = 6]
```

## Examples with Solutions
---------------------------

### Example 1

Given the language represented by the regular expression `b(ab)^*`, find the number of strings in the language that have length 3.

Solution:

```mermaid
graph LR;
    A[Start] --> B[Length 3]
    C[b(ab)^*] --> D[Match (ab) twice and b once]
    E[Match (ab) twice and b once] --> F[Count 3!/((2!*1!)) = 3]
```

### Example 2

Given the language represented by the regular expression `(a|b)(ab)^*`, find the number of strings in the language that have length 4.

Solution:

```mermaid
graph LR;
    A[Start] --> B[Length 4]
    C[(a|b)(ab)^*] --> D[Match (a|b) and (ab) twice]
    E[Match (a|b) and (ab) twice] --> F[Count 2 * 3!/((2!*1!)) = 6]
```

## Common Pitfalls
-------------------

When solving problems related to regular expressions, the following are common pitfalls:

*   Not using the correct formulas for counting strings of a certain length.
*   Not considering all possible cases when matching strings.

## Quick Summary
-----------------

*   Regular expressions describe search patterns in strings.
*   The alphabet is the set of characters used in the regular expression.
*   Strings are sequences of characters from the alphabet.
*   Languages are sets of strings.
*   Key formulas and theorems related to regular expressions include:
    *   $L(S) = \{\sigma \in S^* \mid \sigma \text{ matches the pattern } p\}$
    *   $p|q \equiv L(p) \cup L(q)$
    *   $p \cdot q \equiv L(p) \circ L(q)$
    *   $p^* = \{\epsilon\} \cup (L(p))^+$
    *   $p^+ = L(p)^+$

By following these concepts, formulas, and patterns, you should be able to solve problems related to regular expressions and the Theory of Computation.