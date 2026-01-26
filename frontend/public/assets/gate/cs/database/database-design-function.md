**Database Design Function**
==========================

### Introduction
-----------------

First normal form (1NF) is a fundamental concept in database design, introduced by Edgar F. Codd in his 1970 paper "A Relational Model of Data for Large Shared Data Banks". A relation R is said to be in 1NF if each cell in the table contains atomic values, meaning no repeating groups or multi-valued attributes.

### Core Concepts
-----------------

#### Atomicity and Repeating Groups

In a relation R, each column must contain atomic values. This means that there should not be any:

* **Repeating groups**: A group of values that repeat for a single entity.
* **Multi-valued attributes**: Attributes that can hold multiple values.

Example:
Suppose we have an employee table with columns `id`, `name`, and `contact_info`. If the `contact_info` column contains multiple phone numbers, email addresses, or other contact information for each employee, it violates 1NF.

#### Candidate Keys

A candidate key is a minimal set of attributes that uniquely identifies a tuple in a relation. In other words, if we remove one attribute from a candidate key, it should no longer be able to identify the tuple.

In a table with multiple candidate keys, all the attributes together form the primary key.

### Key Formulas/Theorems
-------------------------

None

### Problem Solving Patterns
-----------------------------

1.  **Identify repeating groups or multi-valued attributes**: Look for columns that contain multiple values or groups of values.
2.  **Check for atomicity**: Ensure each cell in the table contains only one value.
3.  **Verify candidate keys**: Confirm that there are no duplicate keys and that all tuples can be uniquely identified.

### Examples with Solutions
---------------------------

**Example 1:** An employee table with multiple phone numbers for each employee:

| id | name | contact_info |
| --- | --- | --- |
| 1  | John | (123) 456-7890, (987) 654-3210 |
| 2  | Jane | (555) 123-4567 |

**Solution:** This table is not in 1NF because the `contact_info` column contains repeating groups.

**Example 2:** A student table with multiple courses enrolled:

| id | name | course_enrolled |
| --- | --- | --- |
| 1  | Alice | Math, Science, English |
| 2  | Bob   | History, Geography |

**Solution:** This table is not in 1NF because the `course_enrolled` column contains repeating groups.

### Common Pitfalls
-------------------

*   Missing or ignoring atomicity.
*   Confusing candidate keys with primary keys.
*   Assuming that all tables must have a single primary key.

### Quick Summary
-----------------

*   Relations in 1NF have atomic values (no repeating groups or multi-valued attributes).
*   Candidate keys are minimal sets of attributes that uniquely identify tuples.
*   No formulas or theorems apply directly to this topic.