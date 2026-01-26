**Fatigue Strength and S-N Diagram**
=====================================

**Introduction**
---------------

Fatigue strength is a critical consideration in machine design, particularly for components subject to cyclic loading. The S-N diagram, also known as the Wöhler curve, is a widely used tool for predicting fatigue life under various loading conditions.

**Core Concepts**
-----------------

### Fatigue Strength

Fatigue strength refers to the maximum stress a material can withstand without failing due to repeated loading and unloading cycles. It is typically measured in terms of the number of cycles (N) required to cause failure.

### S-N Diagram

The S-N diagram is a plot of stress (S) against the number of cycles (N) to failure. The diagram consists of two regions:

*   **Low-cycle fatigue**: High stresses at low cycle numbers, where plastic deformation occurs.
*   **High-cycle fatigue**: Low stresses at high cycle numbers, where cyclic hardening and softening occur.

**Key Formulas/Theorems**
-------------------------

The S-N diagram can be described by the following equation:

`S_N = S_0 (N/N_f)^m`

where:

*   `S_N` is the fatigue strength
*   `S_0` is a material constant
*   `N` is the number of cycles to failure
*   `N_f` is the number of cycles at which the material fails under static loading
*   `m` is a material constant

**Problem Solving Patterns**
---------------------------

When solving fatigue strength and S-N diagram problems, follow these steps:

1.  **Identify the material properties**: Determine the material's constants (`S_0`, `N_f`, and `m`) using relevant data or reference tables.
2.  **Determine the loading conditions**: Calculate the stress (`S`) applied to the component under cyclic loading.
3.  **Plot the S-N diagram**: Use the given equation to plot the S-N curve for the specific material and loading conditions.

**Examples with Solutions**
---------------------------

### Example 1

A circular mild steel (MS) shaft is subjected to a cyclic loading of `σ = 100 MPa` at `N = 10^6 cycles`. Determine the fatigue strength using the given equation:

```latex
S_N = S_0 (N/N_f)^m
```

Assuming `S_0 = 500 MPa`, `N_f = 10^5 cycles`, and `m = 3`, calculate the fatigue strength.

### Solution

Substitute the values into the equation:

`S_N = 500 (10^6 / 10^5)^3`
`S_N ≈ 500 × 100^3`
`S_N ≈ 5,000 MPa`

The fatigue strength of the MS shaft is approximately `5,000 MPa`.

**Common Pitfalls**
------------------

When solving fatigue strength and S-N diagram problems:

*   **Oversimplify the material properties**: Avoid assuming arbitrary values for material constants.
*   **Ignore loading conditions**: Remember that cyclic loading affects fatigue life significantly.

**Quick Summary**
-----------------

*   Fatigue strength is a measure of a material's ability to withstand repeated loading and unloading cycles.
*   The S-N diagram plots stress against the number of cycles to failure.
*   Use the equation `S_N = S_0 (N/N_f)^m` to calculate fatigue strength.

**References**

*   [1] Wöhler, A. (1867). "Über die Festigkeit von Eisen bei wiederholten Beanspruchung." Zeitschrift für Bauwesen, 17, 583-627.
*   [2] Manson, S. S. (1966). "Fatigue Analysis and Design of Mechanical Components." McGraw-Hill.

**Images**

None