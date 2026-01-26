# Transformer
================

## Introduction
---------------

A transformer is a static electrical device that transfers electrical energy from one circuit to another through electromagnetic induction. It consists of two or more coils (windings) on a common magnetic core, allowing for efficient transfer of power between circuits.

## Core Concepts
-----------------

### Electromagnetic Induction

Electromagnetic induction occurs when a changing magnetic field induces an electromotive force (EMF) in a nearby conductor. This is the fundamental principle behind transformer operation.

### Faraday's Law of Induction

Faraday's law states that the EMF induced in a coil is proportional to the rate of change of the magnetic flux through the coil:

$$\epsilon = -N \frac{d\Phi_B}{dt}$$

where $\epsilon$ is the induced EMF, $N$ is the number of turns in the coil, and $\Phi_B$ is the magnetic flux.

### Mutual Inductance

Mutual inductance occurs when a changing current in one coil induces an EMF in another nearby coil. This is used to transfer energy between the primary and secondary windings in a transformer.

## Key Formulas/Theorems
-------------------------

### Transformer Efficiency

The efficiency of a transformer is given by:

$$\eta = \frac{P_{out}}{P_{in}} = 1 - \frac{P_{loss}}{P_{in}}$$

where $P_{out}$ is the output power, $P_{in}$ is the input power, and $P_{loss}$ are the losses in the transformer.

### Transformer Action Ratio

The action ratio (or turns ratio) of a transformer is given by:

$$\frac{N_s}{N_p} = \sqrt{\frac{V_s}{V_p}}$$

where $N_s$ and $N_p$ are the number of turns in the secondary and primary windings, respectively.

## Problem Solving Patterns
---------------------------

### Voltage Polarities

In a single-phase two-winding transformer:

*   The primary voltage $V_p$ is applied to the primary winding.
*   The induced primary voltage $E_p$ is equal in magnitude but opposite in polarity to $V_p$.
*   The open-circuit secondary voltage $V_s$ is zero if there is no load on the secondary.
*   The induced secondary voltage $E_s$ is proportional to the number of turns in the secondary winding.

## Examples with Solutions
---------------------------

### Example 1: Transformer Efficiency

A transformer has an input power of 100 W and an output power of 90 W. What is its efficiency?

Solution:
$$\eta = \frac{P_{out}}{P_{in}} = \frac{90}{100} = 0.9$$

### Example 2: Transformer Action Ratio

A transformer has a primary voltage of 120 V and a secondary voltage of 240 V. What is the action ratio?

Solution:
$$\frac{N_s}{N_p} = \sqrt{\frac{V_s}{V_p}} = \sqrt{\frac{240}{120}} = 1.414$$

## Common Pitfalls
------------------

*   Forgetting to consider the polarity of voltages in transformer problems.
*   Failing to account for losses in transformer efficiency calculations.

## Quick Summary
---------------

*   Transformers transfer energy between circuits through electromagnetic induction.
*   Faraday's law and mutual inductance are key principles behind transformer operation.
*   Efficiency and action ratio formulas must be applied correctly.
*   Voltage polarities must be considered when solving transformer problems.