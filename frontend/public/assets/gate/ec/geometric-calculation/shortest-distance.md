**Shortest Distance**
======================

### Introduction
The shortest distance between two parallel lines or planes is a fundamental concept in geometry, often used in various fields like engineering and computer science. This topic is crucial for solving problems related to distances, projections, and intersections.

### Core Concepts
The shortest distance between two parallel lines can be found using the formula:

$$d = \frac{|b_1 - b_2|}{\sqrt{a_1^2 + 1}}$$

where $(a_1, b_1)$ and $(a_2, b_2)$ are the slopes of the two lines.

For two parallel planes, we can use a similar approach. If we know the normal vectors to each plane, we can find the distance between them using:

$$d = \frac{|(\mathbf{n}_1 \times \mathbf{n}_2) \cdot (\mathbf{p} - \mathbf{q})|}{||\mathbf{n}_1 \times \mathbf{n}_2||}$$

where $\mathbf{n}_1$ and $\mathbf{n}_2$ are the normal vectors to each plane, and $\mathbf{p}$ and $\mathbf{q}$ are points on each plane.

### Key Formulas/Theorems
$$d = \frac{|b_1 - b_2|}{\sqrt{a_1^2 + 1}}$$

### Problem Solving Patterns
When solving problems involving shortest distances, follow these steps:

1. Identify the type of problem (parallel lines or planes).
2. Determine the necessary information (slopes, normal vectors, points).
3. Apply the relevant formula.

For example, in Q1 (ec_2022_3), we are given a trapezium with parallel sides PQ and SR. We need to find the shortest distance between them.

### Examples with Solutions
**Q1:**
A trapezium has vertices marked as P, Q, R, and S (in that order anticlockwise). The side PQ is parallel to side SR. Further, it is given that, PQ = 11 cm, QR = 4 cm, RS = 6 cm and SP = 3 cm.
What is shortest distance between PQ and SR (in cm)?

## Step 1: Identify the type of problem
We are dealing with a trapezium, which involves parallel lines.

## Step 2: Determine the necessary information
We know the lengths of the sides PQ, QR, RS, and SP.

## Step 3: Apply the relevant formula
To find the shortest distance between two parallel lines, we can use the formula:

$$d = \frac{|b_1 - b_2|}{\sqrt{a_1^2 + 1}}$$

However, this formula is for slopes. We need to convert the given lengths into a format suitable for the formula.

## Step 4: Convert the given lengths
Let's consider PQ as our base and QR as our height (since they are parallel).

## Step 5: Calculate the distance
We can now calculate the shortest distance using:

$$d = \frac{|11 - 3|}{\sqrt{1^2 + (\frac{4}{\Delta})^2}}$$

where $\Delta$ is the length of the shorter side (QR). Since QR = 4 cm, we can plug this value in.

## Step 6: Simplify and calculate
After simplifying, we get:

$$d = \frac{|11 - 3|}{\sqrt{1 + (\frac{4}{4})^2}}$$

$$d = \frac{8}{\sqrt{1 + 1}}$$

$$d = \frac{8}{\sqrt{2}}$$

$$d = \frac{8\sqrt{2}}{\sqrt{2}\cdot\sqrt{2}}$$

$$d = \frac{8\sqrt{2}}{2}$$

$$d = 4\sqrt{2}$$

## Step 7: Convert the answer to a numerical value
We can approximate $4\sqrt{2}$ as:

$$d ≈ 5.66$$

However, we need to choose from the given options.

### Common Pitfalls
- Forgetting to convert lengths into suitable formats for formulas.
- Misapplying formulas for parallel lines/planes.
- Not considering the type of problem (lines or planes).

### Quick Summary
* Shortest distance between two parallel lines: $d = \frac{|b_1 - b_2|}{\sqrt{a_1^2 + 1}}$
* Shortest distance between two parallel planes: $d = \frac{|(\mathbf{n}_1 \times \mathbf{n}_2) \cdot (\mathbf{p} - \mathbf{q})|}{||\mathbf{n}_1 \times \mathbf{n}_2||}$
* Use the relevant formula based on the type of problem.
* Convert lengths into suitable formats for formulas.

Note: The above theory note is tailored to address the specific question and context provided. As an expert GATE CS exam tutor, this comprehensive study note aims to cover all theoretical concepts, formulas, and insights required to solve the given questions and similar future questions.