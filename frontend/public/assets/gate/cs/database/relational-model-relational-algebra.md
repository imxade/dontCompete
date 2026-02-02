**Relational Model Relational Algebra**
=====================================

### Introduction

The relational model and relational algebra are fundamental concepts in database management systems, introduced by Edgar F. Codd in 1970. The relational model represents data as tables with well-defined relationships between them, while relational algebra provides a formal language for querying and manipulating these relations.

### Core Concepts

#### Relations

A relation is a table of tuples (rows) with a fixed number of columns (attributes). Each tuple has a unique combination of attribute values.

#### Attributes

Attributes are the individual columns in a relation. They can be either atomic (simple data types like integers or strings) or composite (structured data types).

#### Tuples

Tuples are the rows in a relation, consisting of a set of attribute values.

#### Operations

Relational algebra defines several operations for querying and manipulating relations:

1. **Selection** ($\sigma$): Selects tuples based on a condition.
2. **Projection**: Projects attributes from a relation.
3. **Union**: Combines two or more relations.
4. **Intersection**: Returns the common tuples between two relations.
5. **Difference**: Returns the tuples in one relation but not another.

### Key Formulas/Theorems

#### Equi-Join

Given two relations R and S with common attributes A, the equi-join of R and S is denoted as $R \bowtie S$. It returns the tuples where the values of A in both R and S match.

$$
\begin{aligned}
R &\bowtie S \\
&= \sigma_{A = B}(R \times S)
\end{aligned}
$$

### Problem Solving Patterns

1. **Identify common attributes**: In equi-join problems, find the shared attributes between the two relations.
2. **Apply selection conditions**: Use $\sigma$ to filter tuples based on specific conditions.
3. **Project relevant attributes**: Select only necessary columns for the final result.

### Examples with Solutions

**Example 1: Equi-Join**

Given:

| A | B |
| --- | --- |
| 10 | 20 |
| 30 | 40 |

| C | D |
| --- | --- |
| 10 | 90 |
| 30 | 45 |

Find the equi-join of R and S on attribute A.

**Solution**

$$
\begin{aligned}
R \bowtie S &= \sigma_{A = C}(R \times S) \\
&= \begin{array}{c|c|c|}
A & B & C & D \\
10 & 20 & 10 & 90 \\
30 & 40 & 30 & 45
\end{array}
\end{aligned}
$$

**Example 2: Selection**

Given:

| A | B |
| --- | --- |
| 10 | 20 |
| 30 | 40 |

Find the tuples where B > 30.

**Solution**

$$
\begin{aligned}
R &= \sigma_{B > 30}(R) \\
&= \begin{array}{c|c|}
A & B \\
30 & 40
\end{array}
\end{aligned}
$$

### Common Pitfalls

1. **Misinterpreting join types**: Ensure you understand the difference between equi-join, natural join, and cross-product.
2. **Omitting crucial conditions**: Always consider selection conditions when solving problems.

### Quick Summary

* Relations: tables of tuples with fixed attributes
* Attributes: individual columns in a relation
* Tuples: rows in a relation
* Operations:
	+ Selection ($\sigma$)
	+ Projection
	+ Union
	+ Intersection
	+ Difference
* Key formulas/theorems:
	+ Equi-join

This comprehensive theory note covers the essential concepts of relational model and relational algebra, including relations, attributes, tuples, operations, and key formulas. It also includes problem-solving patterns, examples with solutions, and common pitfalls to watch out for.

---

**Additional Resources**

* Codd, E. F. (1970). A Relational Model of Data for Large Shared Data Banks.
* Date, C. J. (2004). An Introduction to Database Systems.