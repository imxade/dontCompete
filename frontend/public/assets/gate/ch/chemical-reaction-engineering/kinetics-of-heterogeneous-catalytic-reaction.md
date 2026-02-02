**Kinetics of Heterogeneous Catalytic Reaction**
=====================================================

**Introduction**
---------------

Heterogeneous catalytic reactions involve the interaction between a catalyst and reactants in a separate phase. These reactions are commonly encountered in chemical engineering applications, where they often control the rate of a process. This note focuses on the kinetics of heterogeneous catalytic reactions, particularly those involving porous spherical catalysts.

**Core Concepts**
----------------

### Diffusion-Limited Reactions

In heterogeneous catalytic reactions, mass transport can limit the reaction rate. For intraphase diffusion-controlled reactions, the rate is determined by the diffusion of reactants through the pores of the catalyst.

### Heterogeneous Catalytic Reaction Mechanism

The reaction mechanism involves three steps:

1.  Diffusion of reactant A into the pore.
2.  Adsorption of A onto the surface.
3.  Reaction between adsorbed species to form product B.

**Key Formulas/Theorems**
-------------------------

### **Formula for Observed Rate**

For a first-order heterogeneous reaction with intraphase diffusion control, the observed rate is given by:

$$r_{obs} = \frac{D_eC_A}{\epsilon r_p}\left(\frac{\delta C_{A,i}}{1+\frac{\delta}{r_p}+\frac{k_dC_{B,i}}{k_rC_{A,i}}}\right)$$

where:

*   $D_e$: Effective diffusion coefficient
*   $C_A$: Bulk concentration of A
*   $\epsilon$: Catalyst porosity
*   $r_p$: Particle radius
*   $\delta$: Thickness of the boundary layer
*   $k_d$: Desorption rate constant
*   $k_r$: Reaction rate constant

### **Formula for Thiele Modulus**

The Thiele modulus ($\phi$) characterizes the ratio of reaction rate to diffusion rate:

$$\phi = \frac{r_p}{3}\sqrt{\frac{k_rC_{A,i}}{D_eC_B}}$$

**Problem Solving Patterns**
---------------------------

When solving problems involving heterogeneous catalytic reactions, follow these steps:

1.  Identify the type of reaction and control mechanism.
2.  Determine the relevant rate constants and kinetic parameters.
3.  Use the observed rate formula to relate concentration and reaction rate.
4.  Apply the Thiele modulus to understand the effect of catalyst size on reaction rate.

**Examples with Solutions**
-------------------------

### **Example 1: Observed Rate Calculation**

Suppose we have a first-order heterogeneous reaction with intraphase diffusion control:

$$A \rightarrow B$$

Given:

*   $D_e = 10^{-5} m^2/s$
*   $\epsilon = 0.4$
*   $r_p = 1.5 \times 10^{-3} m$
*   $C_A = 0.3 mol/L$
*   $k_d = 0.01 s^{-1}$
*   $k_r = 0.05 L/mol/s$

Calculate the observed rate ($r_{obs}$) at a bulk concentration of A.

**Step 1**: Calculate the Thiele modulus:

$$\phi = \frac{1.5 \times 10^{-3}}{3}\sqrt{\frac{0.05 \times 0.3}{10^{-5} \times 0.2}}$$

$$\phi ≈ 0.23$$

**Step 2**: Use the observed rate formula:

$$r_{obs} = \frac{D_eC_A}{\epsilon r_p}\left(\frac{\delta C_{A,i}}{1+\frac{\delta}{r_p}+\frac{k_dC_B}{k_rC_A}}\right)$$

Assuming $\delta = 10^{-4}$ and $C_B ≈ 0$ (since product B is formed in the reaction), we have:

$$r_{obs} ≈ \frac{10^{-5} \times 0.3}{0.4 \times 1.5 \times 10^{-3}}\left(\frac{10^{-4} \times 0.3}{1+10^{-4}/(1.5 \times 10^{-3})}\right)$$

$$r_{obs} ≈ 8.33 \times 10^{-6} mol/m^2/s$$

### **Example 2: Comparison of Catalyst Particles**

Suppose we have two catalyst particles with radii $r_1 = 3 mm$ and $r_2 = 6 mm$. Given a bulk concentration of A ($C_A = 0.1 mol/L$) and observed rates for $r_1$ ($r_{obs,1} = 0.2 mol/sL$) and $r_2$ ($r_{obs,2}$ to be calculated).

Calculate the observed rate ($r_{obs,2}$) for catalyst particle $r_2$.

**Step 1**: Calculate the Thiele modulus for $r_2$:

$$\phi = \frac{6 \times 10^{-3}}{3}\sqrt{\frac{0.05 \times 0.1}{10^{-5} \times 0.2}}$$

$$\phi ≈ 0.46$$

**Step 2**: Use the observed rate formula:

$$r_{obs,2} = \frac{D_eC_A}{\epsilon r_2}\left(\frac{\delta C_{A,i}}{1+\frac{\delta}{r_2}+\frac{k_dC_B}{k_rC_A}}\right)$$

Assuming the same values as before and using the calculated Thiele modulus, we have:

$$r_{obs,2} ≈ \frac{10^{-5} \times 0.1}{0.4 \times 6 \times 10^{-3}}\left(\frac{10^{-4} \times 0.1}{1+10^{-4}/(6 \times 10^{-3})}\right)$$

$$r_{obs,2} ≈ 0.033 mol/sL$$

**Common Pitfalls**
-------------------

When solving problems involving heterogeneous catalytic reactions, be careful to:

*   Identify the type of reaction and control mechanism correctly.
*   Use the correct rate constants and kinetic parameters for the given conditions.
*   Apply the observed rate formula and Thiele modulus appropriately.

**Quick Summary**
-----------------

*   Heterogeneous catalytic reactions involve the interaction between a catalyst and reactants in separate phases.
*   Diffusion-limited reactions can control the reaction rate, particularly intraphase diffusion control.
*   The observed rate is determined by the diffusion of reactants through the pores of the catalyst.
*   The Thiele modulus characterizes the ratio of reaction rate to diffusion rate.

This comprehensive theory note covers all theoretical concepts, formulas, and insights required to solve questions on kinetics of heterogeneous catalytic reactions. By following this guide, you will be well-prepared for exams like GATE CS.