**Hydrology**
================

**Introduction**
---------------

Hydrology is the study of water in all its forms and cycles, playing a crucial role in water resources engineering. Understanding hydrological principles is essential for designing efficient irrigation systems, flood control measures, and predicting water availability.

**Core Concepts**
-----------------

### Water Balance Equation

The water balance equation represents the relationship between precipitation (P), evapotranspiration (ET), runoff (R), and change in storage (ΔS) over a specific period:

$$
\begin{aligned}
P &= ET + R + \Delta S \\
\end{aligned}
$$

### Direct Runoff Hydrograph

A direct runoff hydrograph is the graphical representation of the rate at which water flows into a channel or river. The shape and characteristics of the hydrograph depend on various factors, including rainfall intensity, duration, and catchment properties.

### Rainfall-Runoff Relationship

The rainfall-runoff relationship describes how rainfall excess is converted into direct runoff. This process involves infiltration, interflow, and groundwater recharge.

**Key Formulas/Theorems**
-------------------------

*   The maximum available water in the root zone (AWC) can be calculated using:
    $$
    \begin{aligned}
    AWC &= 0.2 \times D \\
    \end{aligned}
    $$
    where D is the maximum root zone depth.

*   Irrigation requirement can be determined using:
    $$
    \begin{aligned}
    I &= \frac{\text{Crop water demand}}{\text{Irrigation efficiency}} \\
    \end{aligned}
    $$

**Problem Solving Patterns**
---------------------------

### Interval Between Irrigation (Q1)

*   Calculate the maximum available water in the root zone using the given maximum root zone depth.
*   Determine the irrigation requirement by dividing crop water demand by irrigation efficiency.
*   Use the formula for interval between irrigation:
    $$
    \begin{aligned}
    t &= \frac{\text{AWC}}{I} \\
    \end{aligned}
    $$

### Direct Runoff Hydrograph (Q2)

*   Calculate rainfall excess using the unit hydrograph method.
*   Determine the time base of the direct runoff hydrograph.
*   Use the formula for calculating rainfall excess:
    $$
    \begin{aligned}
    R_e &= P - ET \\
    \end{aligned}
    $$

### Rainfall-Runoff Relationship (Q3)

*   Calculate the φ-index using the given rainfall and direct runoff values.

**Examples with Solutions**
---------------------------

### Interval Between Irrigation

Suppose crop water demand is 10 mm/day, irrigation efficiency is 70%, and maximum root zone depth is 80 mm. We want to find the interval between irrigation.

First, calculate AWC:
$$
\begin{aligned}
AWC &= 0.2 \times D \\
&= 0.2 \times 80 \\
&= 16 \text{mm} \\
\end{aligned}
$$

Next, determine irrigation requirement:
$$
\begin{aligned}
I &= \frac{\text{Crop water demand}}{\text{Irrigation efficiency}} \\
&= \frac{10}{0.7} \\
&\approx 14.28 \text{mm/day} \\
\end{aligned}
$$

Finally, calculate interval between irrigation:
$$
\begin{aligned}
t &= \frac{\text{AWC}}{I} \\
&\approx \frac{16}{14.28} \\
&\approx 1.12 \text{days} \\
\end{aligned}
$$

### Direct Runoff Hydrograph

Suppose the time base of the direct runoff hydrograph is 90 hours, peak flow occurs at 20 hours from the start of the storm, and area of catchment is 300 km^2.

First, calculate rainfall excess using unit hydrograph method:
$$
\begin{aligned}
R_e &= P - ET \\
&= \text{(Given rainfall)} - \text{(Evapotranspiration)} \\
&= 5.4 \text{cm} \\
\end{aligned}
$$

Next, determine the φ-index:
$$
\begin{aligned}
\phi &= \frac{\text{Rainfall excess}}{\text{Time base}} \\
&\approx \frac{5.4}{90} \\
&\approx 0.06 \text{cm/hour} \\
\end{aligned}
$$

### Rainfall-Runoff Relationship

Suppose rainfall intensity is 10 mm/hr, direct runoff is 1.6 cm, and we want to find the φ-index.

First, calculate rainfall excess:
$$
\begin{aligned}
R_e &= P - ET \\
&= \text{(Given rainfall)} - \text{(Evapotranspiration)} \\
&= \text{(Rainfall intensity) $\times$ (Duration)} \\
&= 10 \times 2.0 \\
&= 20 \text{mm} \\
\end{aligned}
$$

Next, calculate φ-index:
$$
\begin{aligned}
\phi &= \frac{\text{Direct runoff}}{\text{(Rainfall excess) $\times$ (Duration)}} \\
&\approx \frac{1.6}{(20) \times 2.0} \\
&\approx 4.00 \text{mm/hour} \\
\end{aligned}
$$

**Common Pitfalls**
------------------

*   Forgetting to account for irrigation efficiency in calculations.
*   Incorrectly applying formulas or units.

**Quick Summary**
-----------------

*   Water balance equation: P = ET + R + ΔS
*   Direct runoff hydrograph: graph of rate at which water flows into a channel or river.
*   Rainfall-runoff relationship: describes how rainfall excess is converted into direct runoff.
*   Irrigation requirement: (Crop water demand) / (Irrigation efficiency)
*   Interval between irrigation: AWC / I
*   φ-index: (Rainfall excess) / (Duration)

Note to self:

This theory note covers the essential concepts and formulas required for hydrology. To ensure high-quality, exam-focused study material, revise and update this content as needed based on recent exams and student feedback.

For visual aids, consider adding Mermaid diagrams or online images that accurately represent hydrological principles and processes.