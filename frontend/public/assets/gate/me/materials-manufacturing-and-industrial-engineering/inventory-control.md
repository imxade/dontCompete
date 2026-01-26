**Inventory Control**
=====================

**Introduction**
---------------

Inventory control refers to the management of inventory levels within a production system to meet customer demand while minimizing costs. It involves predicting and responding to changes in demand, managing stock levels, and optimizing the flow of goods through the supply chain.

**Core Concepts**
-----------------

### Types of Inventory

There are three types of inventory:

*   **Raw Materials**: Unprocessed materials used as inputs for production.
*   **Work-in-Process (WIP) materials**: Partially processed products that are still in progress.
*   **Finished Goods**: Fully processed and completed products ready for sale.

### Inventory Control Strategies

Inventory control strategies aim to balance demand with supply while minimizing costs. Common strategies include:

*   **Just-In-Time (JIT)**: Producing and delivering products just in time to meet customer demand, reducing inventory levels.
*   **Economic Order Quantity (EOQ)**: Determining the optimal order quantity based on production costs and holding costs.

**Key Formulas/Theorems**
-------------------------

### Economic Order Quantity (EOQ)

The EOQ formula is given by:

$$\text{EOQ} = \sqrt{\frac{2DC}{H}}$$

where:
*   $D$ is the demand rate
*   $C$ is the ordering cost per order
*   $H$ is the holding cost per unit per time period

### Lead Time and Safety Stock

Lead time is the time between placing an order and receiving the goods. Safety stock is additional inventory held to mitigate supply chain disruptions.

$$\text{Safety Stock} = z \sigma \sqrt{\text{Lead Time}}$$

where:
*   $z$ is a standard deviation factor
*   $\sigma$ is the standard deviation of demand
*   Lead Time is the average time between placing an order and receiving the goods

**Problem Solving Patterns**
---------------------------

When solving inventory control problems, consider the following:

1.  **Understand the problem context**: Identify the key factors influencing inventory levels.
2.  **Determine the inventory type**: Raw materials, WIP, or finished goods?
3.  **Apply relevant formulas and strategies**: EOQ, JIT, etc.

**Examples with Solutions**
---------------------------

### Example 1: Calculating EOQ

Given:

*   Demand rate $D = 100$ units per day
*   Ordering cost per order $C = \$10$
*   Holding cost per unit per time period $H = \$5$

Calculate the EOQ.

$$\text{EOQ} = \sqrt{\frac{2(100)(\$10)}{\$5}} = 40.8$$

### Example 2: Calculating Safety Stock

Given:

*   Standard deviation of demand $\sigma = 15$
*   Lead Time $= 7$ days
*   Desired service level (z) $= 1.65$

Calculate the safety stock.

$$\text{Safety Stock} = 1.65 \times 15 \sqrt{7} = 131.4$$

**Common Pitfalls**
-----------------

When working with inventory control, be aware of:

*   **Insufficient data**: Ensure accurate and reliable demand forecasts.
*   **Incorrect formulas**: Verify calculations for EOQ, safety stock, etc.

**Quick Summary**
----------------

Inventory control strategies aim to balance demand with supply while minimizing costs. Key concepts include types of inventory (raw materials, WIP, finished goods), economic order quantity (EOQ) formula, lead time and safety stock calculations.