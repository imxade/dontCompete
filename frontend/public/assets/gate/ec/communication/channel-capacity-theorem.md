# Channel Capacity Theorem
## Introduction
The channel capacity theorem is a fundamental concept in communication theory that provides an upper bound on the rate at which information can be reliably transmitted over a communication channel. It was first introduced by Claude Shannon in 1948 and has since become a cornerstone of modern communication systems.

## Core Concepts
A communication channel is defined as a device or medium that enables the transmission of information from a sender to a receiver. The channel capacity theorem states that the maximum rate at which information can be transmitted over a channel is given by the formula:

C = B \* log2(1 + S/N)

where:
- C is the channel capacity in bits per second
- B is the bandwidth of the channel (in Hz)
- S is the signal power
- N is the noise power

The channel capacity theorem is based on the assumption that the communication channel is a discrete memoryless channel, meaning that each symbol transmitted over the channel is independent of previous symbols.

## Key Formulas/Theorems
### Channel Capacity for Discrete Memoryless Channels
For a discrete memoryless channel with N inputs and M outputs, the channel capacity can be calculated using the formula:

C = max[P(X,Y) \* log2(P(Y|X))] over all possible input distributions P(X)

where:
- C is the channel capacity in bits per symbol
- P(X) is the probability distribution of the input symbols
- P(Y|X) is the conditional probability distribution of the output symbols given the input symbols

### Capacity of a Symmetric Channel
A symmetric channel is a channel where the transition probabilities are the same for all inputs. For a symmetric channel with N inputs, the channel capacity can be calculated using the formula:

C = 2 \* log2(1 + α)

where:
- C is the channel capacity in bits per symbol
- α is a parameter that lies in the interval [0, 1]

## Problem Solving Patterns
To solve problems related to the channel capacity theorem, we need to follow these steps:

1. Identify the type of channel and its parameters.
2. Determine whether the channel is symmetric or not.
3. Calculate the channel capacity using the relevant formula.

### Examples with Solutions

**Example 1**
Consider a discrete memoryless channel with N = 3 inputs and M = 3 outputs. The transition probabilities are given by:

P(Y|X) = { α, β, γ }

where:
- P(0|0) = α
- P(1|1) = β
- P(2|2) = γ

The channel capacity is given by:

C = max[P(X,Y) \* log2(P(Y|X))] over all possible input distributions P(X)

To solve this problem, we need to find the maximum value of the expression [P(X,Y) \* log2(P(Y|X))].

**Solution**

```python
import numpy as np

# Define the transition probabilities
alpha = 0.5
beta = 0.3
gamma = 0.2

# Calculate the channel capacity
C = 2 * np.log2(1 + alpha)
print(C)
```

This code calculates the channel capacity for a symmetric channel with N = 3 inputs.

## Common Pitfalls

* Failing to identify whether the channel is symmetric or not.
* Not using the correct formula for calculating the channel capacity.
* Not taking into account the noise power in the calculation of the channel capacity.

## Quick Summary
* The channel capacity theorem provides an upper bound on the rate at which information can be reliably transmitted over a communication channel.
* The channel capacity is given by the formula C = B \* log2(1 + S/N) for additive white Gaussian noise channels.
* For discrete memoryless channels, the channel capacity is calculated using the formula C = max[P(X,Y) \* log2(P(Y|X))] over all possible input distributions P(X).
* A symmetric channel has the same transition probabilities for all inputs, and its channel capacity can be calculated using the formula C = 2 \* log2(1 + α).