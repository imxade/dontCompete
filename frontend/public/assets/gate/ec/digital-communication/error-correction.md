**Error Correction**
=====================

### Introduction
-----------------

Error correction is a critical component of digital communication systems. It ensures that data transmitted over noisy channels can be recovered with a high degree of accuracy. In this note, we will focus on error correction using Hamming codes.

### Core Concepts
------------------

#### Memoryless Binary Symmetric Channel (BSC)

A memoryless BSC is a channel where each bit is transmitted independently and identically distributed (i.i.d). The probability of transmitting a 0 or 1 is equal, and the probability of receiving an incorrect bit is given by $\epsilon$.

### Key Formulas/Theorems
-------------------------

#### Hamming Code

A $(n,k)$ Hamming code encodes $k$ message bits into $n$ codeword bits using the following generator matrix:

$$G = \begin{bmatrix} 1 & 0 & 0 & \cdots & 0 \\ 0 & 1 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 1 \\ g_1 & g_2 & g_3 & \cdots & g_k \end{bmatrix}$$

where $g_i$ are the parity check bits.

#### Minimum Hamming Distance Decoding

Minimum Hamming distance decoding is a method of decoding codewords where the receiver compares the received codeword with all possible codewords and selects the one with the minimum Hamming distance.

### Problem Solving Patterns
---------------------------

1. **Calculate Codeword Probability**: Given $\epsilon$, calculate the probability that a transmitted codeword is decoded correctly using minimum Hamming distance decoding.
2. **Determine Error Correction Capability**: Determine the number of bit errors an $(n,k)$ Hamming code can correct.

### Examples with Solutions
---------------------------

**Q1: ec_2022_62**

Consider communication over a memoryless binary symmetric channel using a (7, 4) Hamming code. Each transmitted bit is received correctly with probability $1 - \epsilon$, and flipped with probability $\epsilon$. For each codeword transmission, the receiver performs minimum Hamming distance decoding, and correctly decodes the message bits if and only if the channel introduces at most one bit error.

For $0.1 = \epsilon$, the probability that a transmitted codeword is decoded correctly is _________ (round off to two decimal places).

**Solution**

Given that the bits are transmitted using $(7, 4)$ Hamming code

$\Rightarrow$ Total number of bits $n = 7$

Given that the transmitted bit are received correctly with probability $1 - \epsilon$.

So, probability of receiving an incorrect bit is $\epsilon = 0.1$.

The probability that a codeword is decoded correctly using minimum Hamming distance decoding is given by:

$$P(\text{correct}) = (1 - \epsilon)^n \sum_{i=0}^{\lfloor\frac{n-1}{2}\rfloor} {n \choose i} \epsilon^i$$

where $\lfloor x \rfloor$ denotes the greatest integer less than or equal to $x$.

Substituting $n = 7$, $\epsilon = 0.1$, we get:

$$P(\text{correct}) = (1 - 0.1)^7 \left( {7 \choose 0} (0.1)^0 + {7 \choose 1} (0.1)^1 + {7 \choose 2} (0.1)^2 \right)$$

Simplifying, we get:

$$P(\text{correct}) = 0.850$$

### Common Pitfalls
--------------------

*   Failing to calculate the probability of receiving an incorrect bit correctly.
*   Not using the correct formula for minimum Hamming distance decoding.

### Quick Summary
---------------

*   Error correction is a critical component of digital communication systems.
*   Minimum Hamming distance decoding is a method of decoding codewords.
*   The probability that a transmitted codeword is decoded correctly can be calculated using the formula:
    $$P(\text{correct}) = (1 - \epsilon)^n \sum_{i=0}^{\lfloor\frac{n-1}{2}\rfloor} {n \choose i} \epsilon^i$$