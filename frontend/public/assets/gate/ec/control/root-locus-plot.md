**Root Locus Plot**
====================

### Introduction

The Root Locus plot is a graphical representation of the roots of a transfer function as a parameter (usually gain) varies. It's a fundamental tool for control system analysis and design, helping engineers understand how the system responds to different inputs.

### Core Concepts

#### Definition

Given a characteristic equation:

$$\Delta(s) = 1 + K \frac{\prod_{i=1}^n (s-s_i)}{s^{n-m}\prod_{j=1}^m (s-s_j)} = 0$$

where $K$ is the gain, $s_i$ and $s_j$ are poles and zeros of the system, respectively. The Root Locus plot shows the loci of the roots $s_i$ as $K$ varies from 0 to $\infty$.

#### Key Features

*   **Asymptotes**: Lines on the plot indicating the direction of movement for the roots as gain increases.
*   **Centroid**: Average position of the asymptotes, representing the dominant behavior of the system.
*   **Breakaway/Break-in points**: Specific values of $K$ where the number of roots changes, affecting stability.

### Key Formulas/Theorems

1.  **Asymptote angles**:

$$\theta_i = \frac{(2i-1)180^\circ}{n-m} \text{ for } i=1,2,...,n-m$$

    where $n$ is the number of poles and $m$ is the number of zeros.

2.  **Centroid**:

$$s_c = \frac{\sum_{j=1}^m s_j}{n-m}$$

3.  **Breakaway/Break-in condition**:

For a system with $n$ poles and $m$ zeros, the breakaway/break-in point occurs when:

$$\frac{d\Delta(s)}{ds} = 0 \text{ at } K = K_b$$

### Problem Solving Patterns

1.  **Identify the number of poles and zeros**:
    Determine $n$ and $m$ from the characteristic equation to calculate asymptote angles and centroid.
2.  **Find the breakaway/break-in point(s)**:
    Apply the condition that $\frac{d\Delta(s)}{ds} = 0$ at $K = K_b$ to identify specific values of $K$ where stability changes.

### Examples with Solutions

1.  Solve for the Root Locus plot of:

$$\Delta(s) = (s+2)(s+3)^2 + K \frac{(s-4)}{s^2} = 0$$

    *   Asymptote angles: $\theta_1 = 180^\circ$, $\theta_2 = 360^\circ$
    *   Centroid: $s_c = -\frac{5}{3}$
    *   Breakaway point at $K=4$

2.  Identify the transfer function resulting in the given Root Locus plot:

$$G(s) = \frac{(s+1)}{(s^2 + 6s + 36)(s+72)}$$

    *   Compare the given asymptote angles and centroid with the calculated values.

### Common Pitfalls

*   Forgetting to consider complex conjugate poles/zeros
*   Misidentifying the number of poles and zeros
*   Failing to apply the breakaway/break-in condition correctly

### Quick Summary

| Concept | Key Points |
| --- | --- |
| Root Locus plot | Graphical representation of roots vs gain; indicates stability and behavior |
| Asymptotes | Lines indicating direction of root movement as gain increases |
| Centroid | Dominant behavior of the system; average position of asymptotes |
| Breakaway/Break-in points | Specific values of gain where number of roots changes |

**Note**: The above quick summary covers key concepts but might not be comprehensive. This theory note aims to provide a high-yield, exam-focused resource for students preparing for GATE CS.