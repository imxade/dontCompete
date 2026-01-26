**Probability Theory**
=======================

### Introduction
-----------------

Probability theory deals with the study of chance events and their likelihood of occurrence. It provides a mathematical framework for analyzing random phenomena, making predictions, and understanding uncertainty. In this theory note, we will cover the fundamental concepts, formulas, and problem-solving strategies related to probability.

### Core Concepts
----------------

*   **Experiment**: A well-defined action or situation that yields a set of outcomes.
*   **Sample Space**: The set of all possible outcomes of an experiment.
*   **Event**: A subset of the sample space, consisting of one or more outcomes.
*   **Probability**: A measure of the likelihood of an event occurring, ranging from 0 (impossible) to 1 (certain).
*   **Independent Events**: Events where the occurrence of one does not affect the probability of the other.

### Key Formulas/Theorems
-------------------------

#### Addition Rule for Two Independent Events

\[ P(A \cup B) = P(A) + P(B) - P(A \cap B) \]

where $P(A \cup B)$ is the probability of either event A or event B occurring, and $P(A \cap B)$ is the probability of both events A and B occurring.

#### Multiplication Rule for Two Independent Events

\[ P(A \cap B) = P(A) \times P(B) \]

where $P(A \cap B)$ is the probability of both events A and B occurring, and $P(A)$ and $P(B)$ are the probabilities of individual events A and B.

#### Conditional Probability

\[ P(A|B) = \frac{P(A \cap B)}{P(B)} \]

where $P(A|B)$ is the probability of event A occurring given that event B has occurred, and $P(A \cap B)$ and $P(B)$ are the probabilities of events A and B.

### Problem Solving Patterns
---------------------------

*   **List all possible outcomes**: Identify every outcome in the sample space.
*   **Count favorable outcomes**: Count how many outcomes meet the given condition (e.g., getting an even number on a die).
*   **Apply probability formulas**: Use addition, multiplication, or conditional probability rules as needed.

### Examples with Solutions
---------------------------

**Example 1:** Two fair six-sided dice are rolled simultaneously. What is the probability that at least one die shows an even number?

*   Sample Space: $\{(i,j) | i=1,2,...,6 \text{ and } j=1,2,...,6\}$
*   Favorable Outcomes: Counting the pairs where at least one die shows an even number, we get $(18-9)$ favorable outcomes.
*   Probability: $\frac{18-9}{36} = \frac{9}{36} = \frac{1}{4}$

**Example 2:** A coin is flipped twice. What is the probability that at least one of the flips shows heads?

*   Sample Space: $\{(HH, HT, TH, TT)\}$
*   Favorable Outcomes: Counting the pairs where at least one flip shows heads, we get $(2)$ favorable outcomes.
*   Probability: $\frac{2}{4} = \frac{1}{2}$

### Common Pitfalls
-------------------

*   **Miscounting outcomes**: Make sure to list all possible outcomes and accurately count the favorable ones.
*   **Incorrect application of formulas**: Double-check which probability rule applies in each scenario.

### Quick Summary
-----------------

*   **Experiments** and **sample spaces**
*   **Events**, **probability**, and **independent events**
*   **Addition Rule for Two Independent Events**, **Multiplication Rule for Two Independent Events**, and **Conditional Probability**
*   **Problem-solving patterns**: list all possible outcomes, count favorable outcomes, and apply probability formulas

By mastering these concepts and techniques, you will be well-prepared to tackle a wide range of probability questions on the GATE CS exam.