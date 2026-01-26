**General Reasoning: Aptitude Theory Note**
=============================================

**Introduction**
---------------

Aptitude questions in GATE CS exams test your logical reasoning and problem-solving skills. This note will cover the essential concepts, formulas, and techniques required to tackle aptitude-related problems.

**Core Concepts**
-----------------

### 1. Logical Reasoning

Logical reasoning involves using rules, patterns, and structures to deduce conclusions from given information. Familiarize yourself with basic logical operators:

* Conjunction (∧): p ∧ q (p and q)
* Disjunction (∨): p ∨ q (p or q)
* Negation (¬): ¬p (not p)

### 2. Conditional Statements

Conditional statements have the form "if-then" or "only if." They can be written as:

p → q (if p, then q)
q ← p (only if q, then p)

**Key Formulas/Theorems**
-------------------------

* **De Morgan's Laws**: ¬(p ∧ q) = ¬p ∨ ¬q; ¬(p ∨ q) = ¬p ∧ ¬q
* **Law of Non-Contradiction**: p ∧ ¬p = ⊥ (false)
* **Modus Ponens**: if p → q and p, then q

**Problem Solving Patterns**
---------------------------

### 1. Using the Given Statements

Carefully analyze each statement to understand its implications.

### 2. Identifying Logical Consequences

Apply logical operators and rules to deduce new statements from given ones.

**Examples with Solutions**
---------------------------

**Q1:** Either P marries Q or X marries Y.

* Analysis: If P marries Q, then the other option (X marries Y) is false.
* Solution: The correct negation is neither of these two options, making option A the correct answer.

```mermaid
graph LR
A[Either P marries Q] --> B[X marries Y]
```

**Q2:** Consider two rectangular sheets M and N with dimensions 6 × 4 cm each.

* Folding operation (i): M folded into half by joining short edges.
* Folding operation (ii): N folded into half by joining long edges.
* Analysis: After three iterations, M will have a final perimeter of 8 cm, while N will have a final perimeter of 13 cm.
* Solution: The ratio of perimeters is 13:7.

**Q3:** Evaluate the expression λ(p,q) for (p,q) = (3/2, 2/3).

```mermaid
graph LR
A[(3/2,2/3)] --> B[λ(p,q)]
```

* Analysis: The given function λ(p,q) has two cases. If p ≥ q, then λ(p,q) = -pq + p^2. Otherwise, λ(p,q) = pq.
* Solution: Since (p,q) = (3/2, 2/3), we have p < q. Therefore, λ(p,q) = pq.

**Common Pitfalls**
-----------------

1. **Missing implicit assumptions**: Make sure you understand the conditions and constraints of each problem.
2. **Overlooking negations**: Double-check if a statement is being negated or not.
3. **Failing to apply logical rules**: Remember De Morgan's laws, Law of Non-Contradiction, and Modus Ponens.

**Quick Summary**
-----------------

* Familiarize yourself with basic logical operators (conjunction, disjunction, negation).
* Understand conditional statements and their implications.
* Practice applying logical rules (De Morgan's laws, Law of Non-Contradiction, Modus Ponens).
* Carefully analyze each statement to identify logical consequences.

This comprehensive note covers the essential concepts, formulas, and techniques required for aptitude-related problems in GATE CS exams. Remember to practice regularly and focus on developing your problem-solving skills.