**Combinational Circuit**
========================

### Introduction
A combinational circuit is a type of digital logic circuit that produces its output based on the current input values. It does not have any memory, meaning it does not store any information from previous inputs.

### Core Concepts
#### Gates and their Functions
Combinational circuits are built using basic gates:

| Gate | Function |
| --- | --- |
| AND ( conjunction ) | `A ∧ B` = 1 if both A and B are 1 |
| OR ( disjunction ) | `A ∨ B` = 1 if either A or B is 1 |
| NOT ( negation ) | ¬A = 0 if A is 1, 1 if A is 0 |

#### Multiplexers
Multiplexers (MUX) are essential components in combinational circuits. They select one of multiple inputs based on a control signal.

### Key Formulas/Theorems

No specific formulas or theorems apply to this topic. However, understanding Boolean algebra laws is crucial:

| Law | Description |
| --- | --- |
| Commutative law | `A ∧ B = B ∧ A` |
| Associative law | `(A ∧ B) ∧ C = A ∧ (B ∧ C)` |
| Distributive law | `A ∨ (B ∧ C) = (A ∨ B) ∧ (A ∨ C)` |

### Problem Solving Patterns
**Step 1: Identify the circuit type and function.**
In this case, we have a digital logic circuit with three 2-to-1 multiplexers.

**Step 2: Understand input values and their impact on outputs.**

For example, given:
`X_1 = 1, X_2 = 1, X_3 = 0, X_4 = 0`
we can analyze the behavior of each MUX:

| MUX | Control Signals (A, B) |
| --- | --- |
| `1` | (C,D), (E,F) |
| `2` | (G,H), (I,J) |
| `3` | (K,L), (M,N) |

### Examples with Solutions

**Q1:** Given a 2-to-1 multiplexer with inputs `A`, `B`, and select line `S`. If `S = 0`, then output is `A`. If `S = 1`, then output is `B`.

```mermaid
graph LR
    A[Input] -->|S=0|> X[A]
    B[Input] -->|S=1|> Y[B]
```

**Solution:**

When `S = 0`, the output is `A`. When `S = 1`, the output is `B`.

### Common Pitfalls

* Not understanding the function of each gate or component.
* Misinterpreting input values and their impact on outputs.

### Quick Summary
* Combinational circuits produce outputs based on current inputs.
* Gates (AND, OR, NOT) and multiplexers are essential components.
* Boolean algebra laws apply to combinational circuit analysis.

**This Theory Note is a starting point for your studies. It's crucial to practice solving problems and understanding the concepts through multiple examples and scenarios.**