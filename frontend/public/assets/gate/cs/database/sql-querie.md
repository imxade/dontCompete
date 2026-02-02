**SQL Query Theory Note**
==========================

**Introduction**
---------------

SQL (Structured Query Language) is a fundamental language for managing and manipulating data in relational databases. This note covers essential concepts, formulas, and problem-solving patterns required to tackle SQL query questions on the GATE CS exam.

**Core Concepts**
-----------------

* **Relational Model**: A database model that organizes data into tables with well-defined relationships between them.
* **SQL Syntax**: The language used to interact with relational databases, consisting of commands like `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.
* **Set Theory**: SQL queries often involve set operations like union, intersection, and difference.

**Key Formulas/Theorems**
------------------------

### 1. Relational Algebra

Relational algebra is a formal language for manipulating relational databases using operators like:

* $\pi$ (project): Selects attributes from a relation.
* $\sigma$ (select): Filters tuples based on conditions.
* $\cup$ (union): Combines two relations into one.
* $\cap$ (intersection): Returns common tuples between two relations.
* $\setminus$ (difference): Subtracts one relation from another.

**Problem Solving Patterns**
---------------------------

### 1. Using Relational Algebra

*   When asked to return a set of eids who own all brands, use the division operator $/$:
    ```
(
(Own) /
(Brand))
eid
```

    This pattern is based on the source question Q1 (cs_2022_55).

### 2. Handling Self-Joins

*   When comparing tuples from the same relation, use a self-join or a correlated subquery.

**Examples with Solutions**
---------------------------

### Example 1: Return the eids of employees who own all brands

Suppose we have three tables:

| Employee (eid, Name) |
| --- | --- |
| eid = 1, John        |
| eid = 2, Jane        |

| Brand (bid, bName)   |
| --- | --- |
| bid = 1, Apple       |
| bid = 2, Samsung     |

| Own (eid, bid)      |
| --- | --- |
| eid = 1, bid = 1    |
| eid = 1, bid = 2    |
| eid = 2, bid = 3    |

Using relational algebra:

```sql
(
(Own) /
(Brand))
eid
```

This query returns the eids who own all brands.

### Example 2: Return the names of employees who own only Apple

Suppose we have three tables:

| Employee (eid, Name) |
| --- | --- |
| eid = 1, John        |
| eid = 2, Jane        |

| Brand (bid, bName)   |
| --- | --- |
| bid = 1, Apple       |
| bid = 2, Samsung     |

| Own (eid, bid)      |
| --- | --- |
| eid = 1, bid = 1    |
| eid = 1, bid = 2    |
| eid = 3, bid = 3    |

Using relational algebra:

```sql
(
(Own) /
(Own))
eid
```

This query returns the names of employees who own only Apple.

**Common Pitfalls**
------------------

*   Failing to use the correct operator (e.g., union instead of intersection).
*   Neglecting to handle self-joins or correlated subqueries.
*   Forgetting to specify all relevant attributes in the SELECT clause.

**Quick Summary**
---------------

*   Relational algebra operators: $\pi$, $\sigma$, $\cup$, $\cap$, $\setminus$
*   Division operator $/$ for returning a set of eids who own all brands
*   Handling self-joins and correlated subqueries
*   Use the correct operator and specify all relevant attributes in the SELECT clause