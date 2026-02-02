**Rectifier Uncontrolled**
=========================

**Introduction**
---------------

A rectifier uncontrolled is a type of power electronic circuit used to convert AC (Alternating Current) voltage to DC (Direct Current) voltage. It is called "uncontrolled" because it does not have any control mechanism to regulate the output voltage or current.

**Core Concepts**
-----------------

A rectifier uncontrolled consists of four diodes connected in a bridge configuration, as shown:

```mermaid
graph LR
    A[Diode 1] -->|D1|> B[Diode 2]
    C[Diode 3] -->|D3|> D[Diode 4]
    E[GND]
```

The diodes are connected in such a way that during the positive half-cycle of the AC voltage, D1 and D3 conduct, while during the negative half-cycle, D2 and D4 conduct.

**Key Formulas/Theorems**
-------------------------

*   The output DC voltage ($V_{DC}$) is given by:
    $$V_{DC} = \frac{V_m}{\pi}$$
    where $V_m$ is the peak value of the AC voltage.
*   The average output current ($I_{DC}$) is given by:
    $$I_{DC} = \frac{I_m}{2}$$
    where $I_m$ is the maximum value of the AC current.

**Problem Solving Patterns**
----------------------------

To solve problems related to rectifier uncontrolled, you need to follow these steps:

1.  Identify the type of rectifier and its configuration (half-wave or full-wave).
2.  Determine the peak value ($V_m$) and maximum value ($I_m$) of the AC voltage/current.
3.  Calculate the output DC voltage ($V_{DC}$) using the formula above.
4.  Calculate the average output current ($I_{DC}$) using the formula above.

**Examples with Solutions**
---------------------------

### Example 1

A rectifier uncontrolled circuit has an input AC voltage of $240\, V$ at $50\, Hz$. What is the output DC voltage?

```markdown
## Step 1: Calculate the peak value ($V_m$) of the AC voltage.
$V_m = \sqrt{2} \times V_{rms} = \sqrt{2} \times 240\, V$

## Step 2: Calculate the output DC voltage ($V_{DC}$).
$V_{DC} = \frac{V_m}{\pi} = \frac{\sqrt{2} \times 240\, V}{\pi}$
```

The final answer is $\boxed{108.26}\, V$.

### Example 2

A rectifier uncontrolled circuit has an input AC current of $10\, A$. What is the average output current?

```markdown
## Step 1: Calculate the maximum value ($I_m$) of the AC current.
$I_m = \sqrt{2} \times I_{rms} = \sqrt{2} \times 10\, A$

## Step 2: Calculate the average output current ($I_{DC}$).
$I_{DC} = \frac{I_m}{2} = \frac{\sqrt{2} \times 10\, A}{2}$
```

The final answer is $\boxed{7.07}\, A$.

**Common Pitfalls**
------------------

*   Forgetting to calculate the peak value ($V_m$) or maximum value ($I_m$) of the AC voltage/current.
*   Not using the correct formula for calculating the output DC voltage ($V_{DC}$).
*   Not checking the units of the answer.

**Quick Summary**
-----------------

*   Rectifier uncontrolled is a type of power electronic circuit used to convert AC voltage to DC voltage.
*   The output DC voltage is given by $V_{DC} = \frac{V_m}{\pi}$, where $V_m$ is the peak value of the AC voltage.
*   The average output current is given by $I_{DC} = \frac{I_m}{2}$, where $I_m$ is the maximum value of the AC current.