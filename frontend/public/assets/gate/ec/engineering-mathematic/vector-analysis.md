**Vector Analysis**
====================

**Introduction**
---------------

Vector analysis is a branch of mathematics that deals with the study of vectors, which are mathematical objects used to describe quantities with both magnitude and direction. It plays a crucial role in physics, engineering, and computer science. In this theory note, we will cover the essential concepts, formulas, and problem-solving patterns required for tackling vector analysis questions on the GATE CS exam.

**Core Concepts**
-----------------

### Vectors

*   A vector is represented by an arrow with both magnitude (length) and direction.
*   Two vectors are equal if they have the same magnitude and direction.

### Vector Addition

*   The sum of two vectors is obtained by placing them head-to-tail, resulting in a new vector whose tail coincides with the tail of the first vector and whose head coincides with the head of the second vector.
*   The magnitude of the resultant vector can be calculated using the Pythagorean theorem.

### Scalar Multiplication

*   A scalar is a real number that represents a quantity without direction.
*   When a vector is multiplied by a scalar, its magnitude changes by a factor equal to the absolute value of the scalar, and its direction remains unchanged if the scalar is positive or changes sign if the scalar is negative.

**Key Formulas/Theorems**
-------------------------

### Vector Magnitude

*   The magnitude (or norm) of a vector $\mathbf{a}$ is denoted by $|\mathbf{a}|$ and calculated as: $|\mathbf{a}| = \sqrt{x^2 + y^2}.$
*   For any two vectors $\mathbf{a}$ and $\mathbf{b},$: $|\mathbf{a} + \mathbf{b}|^2 = |\mathbf{a}|^2 + |\mathbf{b}|^2 + 2|\mathbf{a}||\mathbf{b}|\cos(\theta).$
*   For any vector $\mathbf{a},$: $|\lambda \mathbf{a}| = |\lambda| |\mathbf{a}|.$

### Vector Dot Product

*   The dot product of two vectors $\mathbf{a}$ and $\mathbf{b}$ is denoted by $\mathbf{a} \cdot \mathbf{b}$ and calculated as: $\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \cos(\theta).$
*   For any two vectors $\mathbf{a}$ and $\mathbf{b},$: $\mathbf{a} \cdot (\mathbf{b} + \mathbf{c}) = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \cdot \mathbf{c}.$

### Vector Cross Product

*   The cross product of two vectors $\mathbf{a}$ and $\mathbf{b}$ is denoted by $\mathbf{a} \times \mathbf{b}$ and calculated as: $|\mathbf{a}| |\mathbf{b}| \sin(\theta) \hat{\mathbf{n}},$ where $\hat{\mathbf{n}}$ is a unit vector perpendicular to both $\mathbf{a}$ and $\mathbf{b}.$

**Problem Solving Patterns**
---------------------------

### Pattern 1: Finding the Magnitude of a Resultant Vector

*   Identify the magnitudes of the individual vectors.
*   Use the Pythagorean theorem or the formula for the magnitude of a resultant vector to find its magnitude.

### Pattern 2: Finding the Dot Product of Two Vectors

*   Calculate the magnitudes and angle between the two vectors.
*   Use the formula for the dot product to find the result.

**Examples with Solutions**
---------------------------

### Example 1:

Find the magnitude of the resultant vector when two vectors $\mathbf{a}$ and $\mathbf{b}$ are added head-to-tail, given that $|\mathbf{a}| = 3$ and $|\mathbf{b}| = 4.$

Solution:
Using the Pythagorean theorem, we find that $|\mathbf{a} + \mathbf{b}|^2 = (3)^2 + (4)^2 = 25.$ Therefore, $|\mathbf{a} + \mathbf{b}| = \sqrt{25} = 5.$

### Example 2:

Find the dot product of two vectors $\mathbf{a}$ and $\mathbf{b},$ given that $|\mathbf{a}| = 3,$ $|\mathbf{b}| = 4,$ and $\theta = 60^\circ.$

Solution:
Using the formula for the dot product, we find that $\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \cos(\theta) = (3)(4)\cos(60^\circ) = 6.$

**Common Pitfalls**
------------------

*   Failing to calculate the correct magnitude or dot product.
*   Not using the correct formula for vector addition, scalar multiplication, or the dot/cross product.

**Quick Summary**
-----------------

*   Vectors have both magnitude and direction.
*   The sum of two vectors is obtained by placing them head-to-tail.
*   Scalar multiplication changes a vector's magnitude but not its direction.
*   Vector magnitude can be calculated using the Pythagorean theorem.
*   The dot product of two vectors is given by $|\mathbf{a}| |\mathbf{b}| \cos(\theta).$
*   The cross product of two vectors is given by $|\mathbf{a}| |\mathbf{b}| \sin(\theta) \hat{\mathbf{n}}.$