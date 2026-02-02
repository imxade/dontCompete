**Relational Data Model**
=========================

### Introduction

The relational data model is a widely used approach to organizing and storing data in a database. It was first introduced by Edgar F. Codd in 1970 as a way to manage complex, large-scale datasets. The relational model views data as tables with rows (tuples) and columns (attributes), allowing for efficient querying and manipulation of the data.

### Core Concepts

#### Relations

A relation is a set of tuples, where each tuple represents a single record or row in the table. Each attribute of the relation corresponds to a column in the table.

**Definition:** A relation R is defined as a set of n-ary relations (R1, R2, ..., Rn) where:

* R = {r1, r2, ..., rm} for some m
* Each ri is an instance of R

#### Attributes and Domains

Attributes are the columns in a table, while domains represent the data type of each attribute. For example, an attribute "Name" might have a domain of strings.

**Definition:** An attribute A with a domain D is denoted as A:D.

#### Keys

Keys are used to identify unique records within a relation. There are two types of keys:

* **Primary Key (PK):** Uniquely identifies each tuple in the relation.
* **Foreign Key (FK):** References the primary key of another relation.

#### Relations with Foreign Keys

A foreign key is an attribute in one relation that references the primary key of another relation. This establishes a relationship between the two relations.

```mermaid
graph LR
  R1[Relation 1] -->|PK|> R2[Relation 2]
```

### Key Formulas/Theorems

* **First Normal Form (1NF):** A relation is in 1NF if each attribute contains only atomic values.
* **Second Normal Form (2NF):** A relation is in 2NF if it is in 1NF and no non-key attribute depends on only a part of the primary key.

### Problem Solving Patterns

When solving questions related to the relational data model, consider the following patterns:

* **Key identification:** Identify primary keys and foreign keys in each relation.
* **Normal forms:** Check if relations are in normal form (1NF, 2NF) as required by the problem statement.
* **Relationships:** Analyze relationships between relations using foreign keys.

### Examples with Solutions

**Example 1:**

Suppose we have two relations:

| Relation 1 | Relation 2 |
| --- | --- |
| OrderID (PK) | CustomerID (PK), Name, Address |
| ProductID (FK) |  |

Which of the following statements is true?

* S1: A relation cannot have more than one foreign key.
* S2: A foreign key in a relation scheme R cannot be used to refer to the tuples of R.

The correct answer is D) Both S1 and S2 are false.

**Solution:**

Relation 1 has two foreign keys: OrderID (FK) references the primary key of Relation 2, while ProductID (FK) references another table not shown. Therefore, statement S1 is false. Statement S2 is also false because a foreign key can be used to refer to tuples in the same relation.

### Common Pitfalls

* **Misidentification of keys:** Ensure you identify primary and foreign keys correctly.
* **Confusion between normal forms:** Understand the difference between 1NF, 2NF, and higher normal forms.
* **Ignoring relationships:** Analyze relationships between relations carefully when solving problems.

### Quick Summary

* Relational data model: tables with rows (tuples) and columns (attributes)
* Relations: sets of tuples
* Attributes and domains: columns and data types
* Keys: primary key (uniquely identifies each tuple), foreign key (references another relation's primary key)
* Normal forms: 1NF (atomic values in attributes), 2NF (no non-key attribute depends on only part of primary key)

Note: This summary is a concise review of the main concepts covered in this theory note. It is not intended to be exhaustive, but rather a quick reference for students to revisit key points.