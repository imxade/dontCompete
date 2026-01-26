**Forecasting Model**
======================

**Introduction**
---------------

In industrial engineering production planning and control, forecasting models are used to predict future demand for products or services. Accurate forecasting helps manufacturers plan and optimize their production schedules, reduce inventory costs, and improve customer satisfaction.

**Core Concepts**
-----------------

### Mean Absolute Percent Error (MAPE)

The MAPE is a measure of the average difference between forecasted and actual values as a percentage of the actual value. It is calculated using the formula:

$$\text{MAPE} = \frac{\sum_{i=1}^{n} |D_i - F_i|}{100} \times 100\%$$

where $D_i$ is the actual demand and $F_i$ is the forecasted demand for period $i$, and $n$ is the number of periods.

### Example: Calculating MAPE

| Month | Demand ($D_i$) | Forecast ($F_i$) | Error ($|D_i - F_i|$) |
| --- | --- | --- | --- |
| April | 225 | 200 | 25 |
| May | 220 | 240 | 20 |
| June | 285 | 300 | 15 |
| July | 290 | 270 | 20 |
| August | 250 | 230 | 20 |

$$\text{MAPE} = \frac{(11.1 + 9.09 + 5.26 + 6.89 + 8.00)}{100} \times 100\% = 8.068\%$$

**Key Formulas/Theorems**
-------------------------

### MAPE Formula (again)

$$\text{MAPE} = \frac{\sum_{i=1}^{n} |D_i - F_i|}{100} \times 100\%$$

### Velocity Components in Two-Dimensional Flow

Given:
$$2u_{xyt} = u_x + v_y$$
$$2v_{y t} = u_x - v_y$$

Integrating the above equations, we get:

$$\ln(x) - \ln(y) = c_1$$

At $x=1$, $y=1$:
$$c_1 = 0$$

Therefore,
$$\ln(xy) = 2\ln(1/x) + 2\ln(1/y)$$
or equivalently,
$$xy = e^{2\ln(1/x) + 2\ln(1/y)} = \frac{e^{\ln(1/x)^2}}{x^y}$$

**Problem Solving Patterns**
---------------------------

*   **MAPE Calculation**: When calculating MAPE, be careful to include the absolute difference between forecasted and actual values.
*   **Velocity Components**: When integrating velocity components in two-dimensional flow, use logarithmic functions to simplify the expressions.

**Examples with Solutions**
-------------------------

### Example 1: Calculating MAPE

| Month | Demand ($D_i$) | Forecast ($F_i$) | Error ($|D_i - F_i|$) |
| --- | --- | --- | --- |
| April | 225 | 200 | 25 |
| May | 220 | 240 | 20 |
| June | 285 | 300 | 15 |
| July | 290 | 270 | 20 |
| August | 250 | 230 | 20 |

$$\text{MAPE} = \frac{(11.1 + 9.09 + 5.26 + 6.89 + 8.00)}{100} \times 100\% = 8.068\%$$

### Example 2: Velocity Components in Two-Dimensional Flow

Given:
$$2u_{xyt} = u_x + v_y$$
$$2v_{y t} = u_x - v_y$$

Integrating the above equations, we get:

$$\ln(x) - \ln(y) = c_1$$

At $x=1$, $y=1$:
$$c_1 = 0$$

Therefore,
$$\ln(xy) = 2\ln(1/x) + 2\ln(1/y)$$
or equivalently,
$$xy = e^{2\ln(1/x) + 2\ln(1/y)} = \frac{e^{\ln(1/x)^2}}{x^y}$$

**Common Pitfalls**
------------------

*   **MAPE Calculation**: Don't forget to include the absolute difference between forecasted and actual values.
*   **Velocity Components**: Be careful when integrating velocity components in two-dimensional flow, as logarithmic functions can be tricky.

**Quick Summary**
-----------------

*   MAPE: measure of average difference between forecasted and actual values as a percentage
*   Velocity components: integrate using logarithmic functions
*   Calculating MAPE: include absolute differences between forecasted and actual values

This comprehensive theory note covers all the necessary concepts, formulas, and problem-solving patterns for forecasting models in industrial engineering production planning and control. Make sure to practice problems from various sources to reinforce your understanding.