**Number Representations and Computer Arithmetic: Fixed and Floating Point**
===========================================================

### Introduction

In digital logic, number representations and computer arithmetic play a crucial role in processing information. The ability to accurately represent numbers and perform arithmetic operations is essential for efficient computation. This note covers the fundamental concepts of fixed-point and floating-point number representations, including cyclic redundancy check (CRC) based error detecting schemes.

### Core Concepts

#### Fixed-Point Numbers

Fixed-point numbers are a type of binary number representation where each bit has a specific weight or significance. The most significant bit (MSB) represents the sign, and subsequent bits represent increasing powers of two.

#### Floating-Point Numbers

Floating-point numbers use a radix point to separate the integer part from the fractional part. They consist of three main components:

1. **Sign bit**: Indicates the sign of the number.
2. **Exponent**: Represents the power of two that should be multiplied with the mantissa (fractional part).
3. **Mantissa** (or Fraction): The actual value represented by the floating-point number.

#### Cyclic Redundancy Check (CRC)

The CRC is a polynomial-based error-detecting scheme used to ensure data integrity during transmission or storage. It generates a checksum based on the message bits and appends it as check bits at the end of the message.

### Key Formulas/Theorems

$$
\text{CRC}_{n+1} = \text{CRC}_n + (x^n) \cdot m_{n-1}
$$

where $\text{CRC}$ is the CRC value, $m$ is the message bit, and $x$ is the generator polynomial.

### Problem Solving Patterns

#### Pattern 1: CRC Calculation

Given a message `1100` and a generator polynomial `1011`, calculate the check bits using the CRC scheme:

1. Initialize $\text{CRC} = 0000$.
2. Calculate $\text{CRC}_{n+1}$ for each bit in the message:
	* For `m_3`: $\text{CRC}_4 = \text{CRC}_3 + (x^3) \cdot m_3 = 1010$
	* For `m_2`: $\text{CRC}_5 = \text{CRC}_4 + (x^4) \cdot m_2 = 1101$
	* For `m_1`: $\text{CRC}_6 = \text{CRC}_5 + (x^5) \cdot m_1 = 1010$
3. The check bits are the last three bits of $\text{CRC}$.

#### Pattern 2: Floating-Point Operations

Given a floating-point number `(-7.5)_10` in binary format, perform addition with another floating-point number `(4.25)_10`.

### Examples with Solutions

**Example 1:** Calculate the check bits for message `1100` using generator polynomial `1011`

Using Pattern 1:

* $\text{CRC}_3 = \text{CRC}_2 + (x^2) \cdot m_2 = 1010$
* $\text{CRC}_4 = \text{CRC}_3 + (x^3) \cdot m_3 = 1101$
* The check bits are `100`.

**Example 2:** Perform floating-point addition for `-7.5` and `4.25`

Using Pattern 2:

* Convert decimal numbers to binary: $(-7.5)_10$ becomes `(11110101)_2` (ignoring the sign) and `(01000100)_2`.
* Perform addition, taking care of rounding errors:
	+ Exponents: add `3 + 4 = 7`
	+ Mantissas: add `1101000 + 0001000 = 1110000`
	+ Combine results: `(-1.25)_10`

### Common Pitfalls

* When performing CRC calculations, ensure the generator polynomial is applied correctly.
* In floating-point operations, be aware of rounding errors and handle them accordingly.

### Quick Summary

* Fixed-point numbers use binary representation with each bit having a specific weight.
* Floating-point numbers use radix point to separate integer part from fractional part.
* Cyclic Redundancy Check (CRC) generates checksum based on message bits using polynomial-based error-detecting scheme.
* Patterns 1 and 2 provide techniques for CRC calculation and floating-point operations, respectively.

**Note:** This is a comprehensive theory note, but it may not cover all possible scenarios. Practice problems and additional resources are recommended to reinforce understanding.