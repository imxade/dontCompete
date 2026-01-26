**SQL and Set Operations**
==========================

**Introduction**
---------------

SQL (Structured Query Language) is a standard language for managing relational databases. It provides various set operations to manipulate data, including union, intersection, difference, and Cartesian product. This note covers the theoretical concepts of SQL and set operations.

**Core Concepts**
-----------------

### Relations and Tables

A relation is a table with rows and columns. Each column represents an attribute, and each row represents a tuple (a single record).

```sql
CREATE TABLE Employee (
  eid INT,
  Name VARCHAR(255)
);

CREATE TABLE Brand (
  bid INT,
  bName VARCHAR(255)
);
```

### Set Operations

Set operations in SQL perform actions on two or more sets of data.

*   **UNION**: Combines rows from multiple tables into a single table.
*   **INTERSECT**: Returns only the common rows between two tables.
*   **EXCEPT** (or **MINUS**): Returns all rows from one table except those in another table.
*   **CARTESIAN PRODUCT** (or **CROSS JOIN**): Returns a new table with each row of one table combined with each row of another table.

```sql
-- UNION
SELECT * FROM Employee UNION SELECT * FROM Brand;

-- INTERSECT
SELECT * FROM Employee INTERSECT SELECT * FROM Brand;

-- EXCEPT (MINUS)
SELECT * FROM Employee MINUS SELECT * FROM Brand;

-- CARTESIAN PRODUCT (CROSS JOIN)
SELECT * FROM Employee CROSS JOIN Brand;
```

### Set Operators

Set operators in SQL are used to perform set operations.

*   **UNION**: `UNION`
*   **INTERSECT**: `INTERSECT`
*   **EXCEPT** (or **MINUS**): `-` (minus sign)
*   **CARTESIAN PRODUCT** (or **CROSS JOIN**): `,` (comma)

```sql
-- UNION
SELECT * FROM Employee, Brand WHERE Employee.eid = Brand.bid;

-- INTERSECT
SELECT * FROM Employee, Brand WHERE Employee.eid = Brand.bid AND Employee.Name = Brand.bName;

-- EXCEPT (MINUS)
SELECT * FROM Employee, Brand WHERE Employee.eid = Brand.bid EXCEPT SELECT * FROM Own;

-- CARTESIAN PRODUCT (CROSS JOIN)
SELECT * FROM Employee, Brand;
```

**Key Formulas/Theorems**
-------------------------

None

**Problem Solving Patterns**
---------------------------

### Pattern 1: Use INTERSECT to Find Common Rows

To find the rows common between two tables, use the `INTERSECT` operator.

```sql
-- Example:
SELECT * FROM Employee INTERSECT SELECT * FROM Brand;
```

### Pattern 2: Use UNION to Combine Tables

To combine rows from multiple tables into a single table, use the `UNION` operator.

```sql
-- Example:
SELECT * FROM Employee UNION SELECT * FROM Brand;
```

**Examples with Solutions**
---------------------------

### Example 1: Find Eids Who Own All Brands

To find the eids who own all brands, use the following query:

```sql
SELECT DISTINCT eid 
FROM (Own) INTERSECT (Brand);
```

However, this will not give the correct result because it returns eids that are common between `Own` and `Brand`, not those that own all brands.

The correct answer is:

```sql
SELECT T1.eid 
FROM Own AS T1 
INTERSECT 
SELECT T2.eid 
FROM Brand AS T2;
```

### Example 2: Find Eids Who Own Only One Brand

To find the eids who own only one brand, use the following query:

```sql
SELECT DISTINCT eid 
FROM (Own) EXCEPT ((Own), (Brand));
```

However, this will not give the correct result because it returns eids that are present in either `Own` but not in both.

The correct answer is:

```sql
SELECT T1.eid 
FROM Own AS T1 
EXCEPT 
SELECT T2.eid 
FROM Brand AS T2;
```

### Example 3: Find Eids Who Do Not Own Any Brands

To find the eids who do not own any brands, use the following query:

```sql
SELECT DISTINCT eid 
FROM Employee EXCEPT ((Own));
```

**Common Pitfalls**
------------------

*   **Misunderstanding set operators**: Make sure to understand what each set operator does and how it differs from others.
*   **Incorrect usage of table aliases**: Use meaningful table aliases and make sure they are used consistently throughout the query.
*   **Ignoring row uniqueness**: Always use `DISTINCT` when necessary to avoid duplicate rows.

**Quick Summary**
-----------------

*   Set operations in SQL: UNION, INTERSECT, EXCEPT (or MINUS), CARTESIAN PRODUCT (CROSS JOIN)
*   Set operators: UNION, INTERSECT, -, ,
*   Understanding set operators and their usage is crucial for solving problems
*   Use table aliases consistently to avoid confusion

Note: This theory note covers the basics of SQL and set operations. Make sure to practice more questions to reinforce your understanding.