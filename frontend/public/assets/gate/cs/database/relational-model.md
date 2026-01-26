**Relational Model**
=====================

### Introduction

The relational model, introduced by Edgar F. Codd in 1970, is a widely used conceptual framework for organizing data in databases. It consists of a set of tables (relations) with rows (tuples) and columns (attributes), which are related to each other through primary keys.

### Core Concepts

#### Relations

A relation is a table with rows and columns. Each row represents a single record, while each column represents an attribute or field in the record.

**Example**
```markdown
+--------+--------+
| Name   | Age    |
+--------+--------+
| John   | 25     |
| Alice  | 30     |
+--------+--------+
```

#### Attributes

Attributes are the columns of a relation, representing individual fields or properties of each record.

**Example**
```markdown
+--------+--------+--------+
| Name   | Age    | Country|
+--------+--------+--------+
| John   | 25     | USA    |
| Alice  | 30     | UK     |
+--------+--------+--------+
```

#### Tuples

Tuples are the rows of a relation, representing individual records.

**Example**
```markdown
(John, 25, USA)
(Alice, 30, UK)
```

#### Primary Key

A primary key is a unique identifier for each record in a relation. It ensures that no two records have the same value for the primary key attribute.

**Example**
```markdown
+--------+--------+
| ID     | Name   |
+--------+--------+
| 1      | John   |
| 2      | Alice  |
+--------+--------+
```

#### Functional Dependencies

Functional dependencies are a way to describe the relationships between attributes in a relation. They specify that an attribute is determined by one or more other attributes.

**Example**
```markdown
ID → Name (every ID has exactly one name)
Name → Age (every name has exactly one age)
```

### Key Formulas/Theorems

1. **First Normal Form (1NF)**: A relation is in 1NF if and only if each cell of the table contains a single value from the domain.

**LaTeX**
\[R \text{ is in 1NF} \iff \forall c \in C, \forall t \in T, |c(t)| = 1\]

2. **Second Normal Form (2NF)**: A relation is in 2NF if and only if it is in 1NF and no non-prime attribute depends on a subset of the primary key.

**LaTeX**
\[R \text{ is in 2NF} \iff R \text{ is in 1NF} \land \forall A \in C, A \notin PK \implies A \text{ not depends on } PK\]

3. **Boyce-Codd Normal Form (BCNF)**: A relation is in BCNF if and only if it is in 2NF and every determinant is a candidate key.

**LaTeX**
\[R \text{ is in BCNF} \iff R \text{ is in 2NF} \land \forall D \in C, \forall A \in C, D \rightarrow A \implies D = PK\]

### Problem Solving Patterns

1. **Decomposition**: Given a relation and a set of functional dependencies, decompose the relation into smaller relations that are in 3NF.
2. **Reconstruction**: Given a set of small relations, reconstruct the original relation.

**Example**
```markdown
Given:

R(P, Q, S, T)
PQ → S
PS → T

Decomposition:
1. R1(P, Q, S)
2. R2(P, S, T)

Reconstruction:
R(P, Q, S, T) = R1 ∪ R2
```

### Examples with Solutions

**Example 1**
Given a relation:

| P | Q | S | T |
| --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |

Find the decomposition of this relation into smaller relations that are in 3NF.

**Solution**

```markdown
R(P, Q, S)
R(P, S, T)

Note: PQ → S, PS → T
```

### Common Pitfalls

* Failing to identify the primary key.
* Ignoring functional dependencies.
* Not normalizing the relation (e.g., not in 1NF).

### Quick Summary

* Relations are tables with rows and columns.
* Attributes represent individual fields or properties of each record.
* Tuples represent individual records.
* Primary keys ensure uniqueness of records.
* Functional dependencies describe relationships between attributes.
* Normal forms (1NF, 2NF, BCNF) are used to optimize the relation.

---

**Reference Questions**

This study note is based on the following reference questions:

* CS_2021-M_25: Relational Model - Decomposition

Please ensure that you have a good understanding of the concepts and techniques covered in this study note before attempting similar questions.