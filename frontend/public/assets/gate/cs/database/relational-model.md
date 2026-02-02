# Relational Model
=====================

## Introduction
---------------

The relational model, introduced by Edgar Codd, is a widely used data modeling approach for database management systems. It represents data as tables with rows and columns, where each column has a unique name (attribute) and each row represents a single record or tuple.

## Core Concepts
-----------------

### Relations

A relation is a set of tuples (rows), where each tuple has a fixed number of attributes (columns). Each attribute has a unique name, and the order of attributes does not matter. For example:

| empId | name   | gender | salary |
|-------|--------|--------|--------|
| 1     | John   | Male   | 5000   |
| 2     | Jane   | Female | 6000   |

### Keys

A key is an attribute or a set of attributes that uniquely identifies each tuple in the relation. There are two types of keys:

* **Primary Key (PK)**: A single attribute or a set of attributes that uniquely identifies each tuple.
* **Foreign Key (FK)**: An attribute or a set of attributes that references the primary key of another relation.

### Functional Dependencies

A functional dependency is a relationship between two sets of attributes in a relation, where one set determines the other. For example:

P → QR means that if P is known, then QR can be determined uniquely.

## Key Formulas/Theorems
-------------------------

* **Armstrong's Axioms**:
	+ If P → QR and Q → R, then P → R (transitivity)
	+ If P → QR and R → S, then P → QS (composition)
	+ If P → QR and Q ⊆ S, then P → SR (augmentation)

## Problem Solving Patterns
---------------------------

### SQL Query Analysis

When analyzing a SQL query, follow these steps:

1. **Identify the relations**: Determine which tables are involved in the query.
2. **Determine the keys**: Identify the primary and foreign keys used in the query.
3. **Analyze the conditions**: Break down the WHERE clause into individual conditions and analyze each one.

### Functional Dependencies

When analyzing functional dependencies, follow these steps:

1. **Identify the determining attributes**: Determine which attributes determine the other set of attributes.
2. **Apply Armstrong's Axioms**: Use the axioms to infer new functional dependencies.

## Examples with Solutions
---------------------------

**Example 1: SQL Query Analysis**

Consider the following query:
```sql
SELECT deptId, COUNT(*)
FROM emp
WHERE gender = "female" AND salary > (SELECT AVG(salary) FROM emp)
GROUP BY deptId;
```
To solve this query:

1. **Identify the relations**: The relation is `emp`.
2. **Determine the keys**: The primary key is `empId`, and there are no foreign keys.
3. **Analyze the conditions**:
	* `gender = "female"` filters tuples where `gender` equals "female".
	* `salary > (SELECT AVG(salary) FROM emp)` filters tuples where `salary` exceeds the average salary of all employees.

The query will return the number of female employees in each department whose salary is greater than the company-wide average salary.

**Example 2: Functional Dependencies**

Consider the following functional dependencies:
```markdown
P → QR
T → R
```
To solve this problem:

1. **Identify the determining attributes**: `P` determines `QR`, and `T` determines `R`.
2. **Apply Armstrong's Axioms**:
	+ By transitivity, P → R.

## Common Pitfalls
-----------------

* **Failing to identify keys**: Make sure to identify primary and foreign keys correctly.
* **Misunderstanding functional dependencies**: Pay attention to the determining attributes and apply Armstrong's Axioms correctly.
* **Incorrect SQL query analysis**: Break down complex queries into individual conditions and analyze each one carefully.

## Quick Summary
---------------

* Relations are sets of tuples with fixed attributes (columns).
* Keys uniquely identify tuples in a relation.
* Functional dependencies describe relationships between attributes in a relation.
* Apply Armstrong's Axioms to infer new functional dependencies.

Note: This is not an exhaustive summary, but rather a starting point for further study and exploration.