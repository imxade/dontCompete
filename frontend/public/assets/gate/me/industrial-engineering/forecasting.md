**Forecasting**
================

### Introduction

Forecasting is a crucial aspect of Industrial Engineering that deals with predicting future outcomes based on historical data and trends. It helps in making informed decisions for resource allocation, production planning, and demand management. In this note, we will cover the key concepts, formulas, and techniques required to solve forecasting-related problems.

### Core Concepts

#### Mean Absolute Percent Error (MAPE)

The MAPE is a measure of the average difference between forecasted and actual values as a percentage of the actual value.

$$
\text{MAPE} = \frac{\sum_{i=1}^{n} \left| \frac{D_i - F_i}{D_i} \right| \times 100}{n}
$$

where:

* $D_i$ is the actual demand for month $i$
* $F_i$ is the forecasted demand for month $i$
* $n$ is the number of months

#### Exponential Smoothing (ES)

Exponential smoothing is a method used to forecast future values based on past data. It assigns weights to each past value, with more recent values given greater weight.

$$
F_t = \alpha \times D_{t-1} + (1 - \alpha) \times F_{t-1}
$$

where:

* $F_t$ is the forecasted demand for month $t$
* $D_{t-1}$ is the actual demand for month $(t-1)$
* $\alpha$ is the smoothing factor, which controls the weight given to recent values

### Key Formulas/Theorems

#### MAPE Formula (LaTeX)

$$
\text{MAPE} = \frac{\sum_{i=1}^{n} \left| \frac{D_i - F_i}{D_i} \right| \times 100}{n}
$$

### Problem Solving Patterns

* When given a table of demands and forecasts, calculate the MAPE using the formula above.
* Identify the type of forecasting method used (e.g., ES) and apply the relevant formula.

### Examples with Solutions

**Example 1: Calculating MAPE**

| Month | Demand ($D_i$) | Forecast ($F_i$) |
| --- | --- | --- |
| April | 225 | 200 |
| May | 220 | 240 |
| June | 285 | 300 |

Solution:

* Calculate the absolute percentage error for each month:
	+ April: $\left| \frac{225 - 200}{225} \right| \times 100 = 11.1\%$
	+ May: $\left| \frac{220 - 240}{220} \right| \times 100 = 9.09\%$
	+ June: $\left| \frac{285 - 300}{285} \right| \times 100 = 5.26\%$
* Calculate the MAPE:
$$
\text{MAPE} = \frac{\sum_{i=1}^{3} \left| \frac{D_i - F_i}{D_i} \right| \times 100}{3} = \frac{11.1 + 9.09 + 5.26}{3} = 8.15\%
$$

**Example 2: Exponential Smoothing**

Suppose we have the following demands and forecasts:

| Month | Demand ($D_i$) | Forecast ($F_i$) |
| --- | --- | --- |
| Jan | 100 | 120 |
| Feb | 110 | 130 |
| Mar | 120 | 140 |

We want to forecast the demand for April using ES with $\alpha = 0.2$. Calculate the forecasted demand for April.

Solution:

* Calculate the weighted average of past demands:
$$
F_{\text{Apr}} = 0.2 \times D_{\text{Mar}} + (1 - 0.2) \times F_{\text{Mar}} = 0.2 \times 120 + 0.8 \times 140 = 128
$$

### Common Pitfalls

* When calculating MAPE, ensure to use the absolute percentage error for each month.
* When applying ES, choose an appropriate value of $\alpha$ based on the problem context.

### Quick Summary

* MAPE formula: $\text{MAPE} = \frac{\sum_{i=1}^{n} \left| \frac{D_i - F_i}{D_i} \right| \times 100}{n}$
* Exponential Smoothing (ES) formula: $F_t = \alpha \times D_{t-1} + (1 - \alpha) \times F_{t-1}$