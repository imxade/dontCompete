# Unit Processes and Operations: Water and Wastewater Quality and Treatment
## Introduction
Water and wastewater treatment involve various unit processes to remove contaminants, pollutants, and pathogens. This note focuses on the theoretical concepts, formulas, and insights required for the GATE CS exam.

## Core Concepts
The quality of water is determined by its physical, chemical, and biological properties. Key factors include:

* **pH**: Measure of acidity or alkalinity (0-14 pH scale)
* **Dissolved Oxygen (DO)**: Essential for aquatic life (mg/L)
* **Biochemical Oxygen Demand (BOD)**: Measure of organic pollution (mg/L)
* **Chemical Oxygen Demand (COD)**: Measure of chemical pollution (mg/L)

## Key Formulas/Theorems
LaTeX formulas are used throughout this note. Basic math notation:

```latex
\begin{align*}
pH = -\log_{10}[H^+]
\end{align*}
```

### pH Calculation

Given an amount of HCl added to distilled water, we calculate the pH using:

```latex
\begin{align*}
pH &= -\log_{10}\left[\frac{n \cdot M}{V}\right]\\
    &=-\log_{10}\left[\frac{(35.67 \text{ mg}) \cdot (M_{\text{HCl}})}{(1 \text{ L})}\right]
\end{align*}
```

where $n$ is the number of moles, $M$ is molarity, and $V$ is volume.

## Problem Solving Patterns

### Example Q1:
Q: Question 2
An amount of 35.67 mg HCl is added to distilled water and the total solution volume is made to one litre.
The atomic weights of H and Cl are 1 and 35.5, respectively. Neglecting the dissociation of water, the pH 
of the solution, is
(A) 2.50 
(B) 3.50 
(C) 2.01 
(D) 3.01

### Solution
Given:
* 35.67 mg HCl added to 1 L distilled water.
* Atomic weights: H (1), Cl (35.5).

First, calculate the number of moles:

```latex
\begin{align*}
n_{\text{HCl}} &= \frac{\text{mass HCl}}{\text{molar mass HCl}}\\
             & = \frac{(35.67 \times 10^{-3} \text{ g})}{(1 + 35.5) \text{ g/mol}} \\
             &\approx 9.96 \times 10^{-4} \text{ mol}
\end{align*}
```

Calculate the molarity:

```latex
\begin{align*}
M_{\text{HCl}} &= \frac{n_{\text{HCl}}}{V}\\
             & = \frac{(9.96 \times 10^{-4} \text{ mol})}{(1 \text{ L})} \\
             &\approx 9.96 \times 10^{-4} \text{ M}
\end{align*}
```

Calculate the pH using:

```latex
\begin{align*}
pH &= -\log_{10}\left[\frac{n \cdot M}{V}\right]\\
    &=-\log_{10}\left[\frac{(9.96 \times 10^{-4} \text{ mol}) \cdot (1)}{(1 \text{ L})}\right] \\
    &\approx -\log_{10}(9.96 \times 10^{-4})\\
    &\approx 3.01
\end{align*}
```

Therefore, the correct answer is (D) 3.01.

## Common Pitfalls

* Forgetting to convert units.
* Not accounting for dissociation of water (negligible in this case).
* Incorrect application of pH calculation formula.

## Quick Summary

* Water quality parameters: pH, DO, BOD, COD
* pH calculation using $pH = -\log_{10}[H^+]$
* Key concepts and formulas applied to Q1