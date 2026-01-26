**Theory of Computation: Regular Expressions and Finite Automata, Context-Free Grammars and Pushdown Automata**
===========================================================

### Introduction
--------------------------------------------------------

Regular expressions (regex) are a powerful tool for describing patterns in strings. Finite automata (FA) are used to recognize regular languages. Context-free grammars (CFGs) and pushdown automata (PDA) are essential for understanding the theory of computation, particularly with regards to context-free languages.

### Core Concepts
------------------

#### Regular Expressions

Regular expressions are a pattern specification language that describes strings. Regex patterns consist of:

1. **Literal characters**: Represented by themselves.
2. **Character classes**:
	* `.` (dot) matches any character.
	* `[abc]` matches any character within the brackets.
3. **Quantifiers**:
	* `*` (star) matches zero or more occurrences.
	* `+` (plus) matches one or more occurrences.
	* `?` (question mark) matches zero or one occurrence.
4. **Special sequences**:
	* `|` (pipe) specifies an alternative pattern.
	* `( )` (parentheses) groups a pattern and allows repetition.

#### Finite Automata

Finite automata are used to recognize regular languages. A FA consists of:

1. **States**: Represented by `q0`, `q1`, etc.
2. **Transitions**: Represented by `δ(q, σ) = p`, where `q` is the current state, `σ` is the input symbol, and `p` is the next state.
3. **Start state**: Typically `q0`.
4. **Accept states**: States that accept the input string.

#### Context-Free Grammars

Context-free grammars are used to describe context-free languages. A CFG consists of:

1. **Non-terminals**: Represented by uppercase letters (e.g., `S`, `A`).
2. **Terminals**: Represented by lowercase letters or strings.
3. **Productions**: Rules for replacing non-terminals with combinations of terminals and non-terminals.

#### Pushdown Automata

Pushdown automata are used to recognize context-free languages. A PDA consists of:

1. **States**: Similar to FA states.
2. **Stack**: Allows the PDA to keep track of parentheses or other nesting structures.
3. **Transitions**: Specify how to manipulate the stack.

### Key Formulas/Theorems
-------------------------

* **Regular Expression Equivalence**: A language is regular if and only if it can be described by a regex.
* **FA and Regex Relationship**: Every FA corresponds to a unique regex, and vice versa.
* **CFG and PDA Relationship**: Every CFG corresponds to a unique PDA, and vice versa.

```latex
\begin{equation}
L(G) = \bigcup_{\sigma} L(G, \sigma)
\end{equation}
```

### Problem Solving Patterns
-----------------------------

1. **Regex Pattern Matching**: Identify the regex pattern and use it to match strings.
2. **FA Design**: Design a FA that accepts a given language.
3. **CFG Derivation**: Use CFG productions to derive a string from a non-terminal.

### Examples with Solutions
---------------------------

**Example 1:** Given the regex `a*b`, find all strings accepted by this pattern.

```mermaid
graph LR
    A[Input: ''] --> B[a]
    B --> C[b]
    C --> D[*] -- Zero or more a's -->
```

The string `''` is accepted because it matches the regex pattern `a*b`.

**Example 2:** Design a FA that accepts the language `{ww^R | w ∈ {0,1}*}`.

| State | Input | Next State |
| --- | --- | --- |
| q0 | 0 | q0 |
| q0 | 1 | q1 |

The FA has two states: `q0` and `q1`. The start state is `q0`, and the accept state is `q1`.

### Common Pitfalls
------------------

1. **Regex Overlap**: Be careful when using overlapping regex patterns.
2. **FA State Explosion**: Avoid designing FAs with too many states.
3. **CFG Non-termination**: Ensure CFGs are context-free.

### Quick Summary
---------------

* Regular expressions describe regular languages.
* Finite automata recognize regular languages.
* Context-free grammars and pushdown automata recognize context-free languages.
* Key formulas and theorems relate regex, FA, CFG, and PDA.

This comprehensive theory note covers all the concepts tested in the source questions. It includes core concepts, key formulas/theorems, problem-solving patterns, examples with solutions, and common pitfalls.