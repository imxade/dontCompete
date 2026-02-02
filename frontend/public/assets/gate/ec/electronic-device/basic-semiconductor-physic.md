**Basic Semiconductor Physics**
=====================================

**Introduction**
---------------

Semiconductors are materials with electrical conductivity between that of a conductor and an insulator. Their unique properties make them crucial for electronic devices, including transistors, diodes, and solar cells.

**Core Concepts**
-----------------

### 1. Fermi Energy Level

The Fermi energy level (EF) is the energy level at which the probability of finding an electron is 50%. In a semiconductor, EF lies between the conduction band (CB) and valence band (VB).

### 2. Degenerate and Non-Degenerate Semiconductors

*   A **degenerate** semiconductor has EF in the CB, indicating many electrons have been excited into the CB.
*   A **non-degenerate** semiconductor has EF in the VB, with few electrons excited into the CB.

### 3. Intrinsic Semiconductors

Intrinsic semiconductors are pure materials without impurities. Their electrical conductivity is due to thermal excitation of electrons from the VB to the CB.

**Key Formulas/Theorems**
-------------------------

*   $E_F = E_C - kT \ln (n/V)$ for non-degenerate n-type semiconductors
*   $E_F = E_V + kT \ln (p/N)$ for non-degenerate p-type semiconductors

### 4. Intrinsic Carrier Concentration

$n_i = 2\left(\frac{2\pi k T}{h^2}\right)^{\frac{3}{2}}(m_n^*m_p^*)^{\frac{3}{4}} e^{-E_g/2kT}$

where $n_i$ is the intrinsic carrier concentration, $k$ is Boltzmann's constant, $T$ is temperature in Kelvin, $h$ is Planck's constant, and $m_n^*$ and $m_p^*$ are the effective masses of electrons and holes.

**Problem Solving Patterns**
---------------------------

*   When determining whether a semiconductor is degenerate or non-degenerate, consider the position of EF relative to CB and VB.
*   To solve questions about intrinsic semiconductors at 0 K, recall that all energy states in the VB are filled with electrons and all energy states in the CB are empty.

**Examples with Solutions**
-------------------------

### Example 1: Degenerate Semiconductor

In a semiconductor, if EF lies in the conduction band, then:

*   The material is **degenerate n-type**, as explained earlier.
*   Use this understanding to solve question ec\_2023\_16.

### Example 2: Intrinsic Carrier Concentration

Suppose an intrinsic semiconductor has the following parameters:
*   Temperature $T = 300\ K$
*   Bandgap energy $E_g = 1.12\ eV$
*   Effective masses of electrons and holes $m_n^* = 0.22 \times m_0$, $m_p^* = 0.54 \times m_0$

Use the intrinsic carrier concentration formula to calculate $n_i$.

### Example Solution

```python
import math

# Given parameters
T = 300  # Temperature in Kelvin
E_g = 1.12e-19  # Bandgap energy in Joules
m_n_star = 0.22 * 9.11e-31  # Effective mass of electrons in kg
m_p_star = 0.54 * 9.11e-31  # Effective mass of holes in kg

# Intrinsic carrier concentration formula
n_i = (2 * math.pi * 1.38e-23 * T / (6.626e-34**2))**(3/2) * \
      (m_n_star * m_p_star)**(3/4) * math.exp(-E_g / (2 * 1.38e-23 * T))

print(n_i)
```

**Common Pitfalls**
------------------

*   Confusing degenerate and non-degenerate semiconductors.
*   Misinterpreting the intrinsic carrier concentration formula.

**Quick Summary**
-----------------

### Key Points

*   Fermi energy level lies between CB and VB in semiconductors.
*   Degenerate semiconductors have EF in the CB, while non-degenerate semiconductors have EF in the VB.
*   Intrinsic semiconductors are pure materials with electrical conductivity due to thermal excitation of electrons.

### Formulae

*   $E_F = E_C - kT \ln (n/V)$ for non-degenerate n-type semiconductors
*   $E_F = E_V + kT \ln (p/N)$ for non-degenerate p-type semiconductors
*   $n_i = 2\left(\frac{2\pi k T}{h^2}\right)^{\frac{3}{2}}(m_n^*m_p^*)^{\frac{3}{4}} e^{-E_g/2kT}$