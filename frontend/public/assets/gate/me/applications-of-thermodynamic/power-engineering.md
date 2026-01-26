# Applications of Thermodynamics - Power Engineering
## Introduction
Thermodynamic principles are crucial in understanding the behavior and efficiency of various power plants, including steam power plants, gas turbines, and internal combustion engines. This topic focuses on applying thermodynamic concepts to analyze and optimize these systems.

## Core Concepts
### 1. First Law of Thermodynamics (Energy Conservation)
\[ \Delta U = Q - W \]
where $\Delta U$ is the change in internal energy, $Q$ is the heat added, and $W$ is the work done on or by the system.

### 2. Second Law of Thermodynamics
It introduces the concept of entropy, which quantifies the disorder or randomness of a system. For an isolated system, the total entropy always increases over time.

### 3. Ideal Rankine Cycle
A fundamental cycle in steam power plants, consisting of:
- Isentropic compression (Pump)
- Constant pressure heat addition (Boiler)
- Isentropic expansion through high-pressure turbine (HPT) and low-pressure turbine (LPT)
- Constant pressure heat rejection (Condenser)

### 4. Reheat Rankine Cycle
An improvement over the ideal Rankine cycle, where the steam is reheated to a higher temperature before entering the LPT.

## Key Formulas/Theorems

### Efficiency of an Ideal Rankine Cycle
\[ \eta_{R} = 1 - \frac{1}{\eta_{t}} \]
where $\eta_R$ is the efficiency of the Rankine cycle and $\eta_t$ is the efficiency of the turbine.

### Efficiency of a Reheat Rankine Cycle
\[ \eta_{RH} = \eta_{R} + (W_{LPT} - W_{HPT})/Q \]

## Problem Solving Patterns

1. **Identify System Boundaries**: Clearly define the system being analyzed.
2. **Apply Thermodynamic Laws**: Use the first and second laws of thermodynamics as necessary to solve problems.
3. **Calculate Work and Heat Transfer**: Ensure accurate calculations for work done by or on the system, including the work output from turbines and pumps.

## Examples with Solutions

### Example 1: Efficiency of an Ideal Rankine Cycle
Given:
- $\eta_t = 0.8$
- $Q = 1000 \text{ kJ/kg}$
Find the efficiency of the ideal Rankine cycle.
\[ \eta_{R} = 1 - \frac{1}{\eta_{t}} = 1 - \frac{1}{0.8} = 0.25 \]
\[ \eta_{R}(\%) = 25\% \]

### Example 2: Quality of Steam at the Exit of a Low-Pressure Turbine
Given:
- $W_{LPT} = 1500 \text{ kJ/kg}$
- $W_{HPT} = 750 \text{ kJ/kg}$
- $\eta_{t} = 0.8$
Find the quality of steam at the exit of the low-pressure turbine.
First, calculate the thermal efficiency:
\[ \eta_{R} = 1 - \frac{1}{\eta_{t}} = 0.25 \]
Then, find the net heat supplied to the cycle:
\[ Q = W_{LPT} + W_{HPT} \]
Using the second law for an ideal reheat Rankine cycle:
\[ \eta_{R} = \frac{Q - W_p}{Q} \]
Given $W_p = 20 \text{ kJ/kg}$, we can find $Q$ and solve for the quality of steam.

## Common Pitfalls

- **Incorrect System Boundaries**: Failing to clearly define the system being analyzed.
- **Misapplication of Thermodynamic Laws**: Incorrect use of the first or second laws of thermodynamics.

## Quick Summary
### Key Concepts:

- First law of thermodynamics (energy conservation)
- Second law of thermodynamics (entropy increase over time)
- Ideal and reheat Rankine cycles
- Efficiency formulas for these cycles

### Important Formulas:
\[ \Delta U = Q - W \]
\[ \eta_{R} = 1 - \frac{1}{\eta_{t}} \]
\[ \eta_{RH} = \eta_{R} + (W_{LPT} - W_{HPT})/Q \]

### Problem Solving Tips:
- Clearly define system boundaries.
- Accurately calculate work and heat transfer.