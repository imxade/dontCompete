**Memory Hierarchy**
======================

### Introduction
-----------------

The memory hierarchy is a conceptual representation of how computer systems organize and utilize different types of memory to store and retrieve data efficiently. The hierarchy consists of multiple levels, each with its own characteristics and access times.

### Core Concepts
-----------------

#### Cache Memory

Cache memory is a small, fast memory that acts as an intermediate layer between the main memory and the CPU. It stores frequently accessed data to reduce the time it takes for the CPU to retrieve data from the main memory.

**Types of Cache:**

*   **L1 (Level 1) Cache:** Smallest and fastest cache level, built into the CPU.
*   **L2 (Level 2) Cache:** Larger and slower than L1 cache, often located on the CPU or in a separate chip.
*   **L3 (Level 3) Cache:** Shared among multiple cores, provides a high-speed memory access.

#### Main Memory

Main memory, also known as RAM (Random Access Memory), is the primary storage for data and program instructions. It's volatile, meaning its contents are lost when power is turned off.

**Types of Main Memory:**

*   **SRAM (Static Random-Access Memory):** Fast but expensive.
*   **DRAM (Dynamic Random-Access Memory):** Slower but more affordable.

#### Virtual Memory

Virtual memory is a combination of main memory and secondary storage, such as hard drives or solid-state drives. It provides an illusion of having more physical memory than available.

### Key Formulas/Theorems
-------------------------

*   **Cache Hit Ratio (CHR) Formula:**

    $$
    CHR = \frac{Number\ of\ cache\ hits}{Total\ number\ of\ accesses}
    $$

*   **Average Memory Access Time (AMAT) Formula:**

    $$
    AMAT = (1 - P_{miss}) \times T_{hit} + P_{miss} \times (T_{hit} + T_{miss})
    $$

    Where:
    *   $P_{miss}$ is the miss penalty probability.
    *   $T_{hit}$ is the cache access time.
    *   $T_{miss}$ is the memory access time.

### Problem Solving Patterns
---------------------------

1.  **Calculate Cache Hit Ratio (CHR):**

    Use the CHR formula to calculate the ratio of cache hits to total accesses.
2.  **Determine Average Memory Access Time (AMAT):**

    Apply the AMAT formula to find the average memory access time based on the miss penalty probability, cache access time, and memory access time.

### Examples with Solutions
---------------------------

**Example 1: Calculating CHR**

Suppose a cache has a hit rate of 0.8 and a total number of accesses is 1000.

CH = (0.8) \* (1000) = 800

CHR = 800/1000 = 0.8

**Example 2: Determining AMAT**

Given:

*   Miss penalty probability, P_miss = 0.1
*   Cache access time, T_hit = 10 ns
*   Memory access time, T_miss = 50 ns

Apply the AMAT formula:

AMAT = (1 - 0.1) \* (10) + 0.1 \* (10 + 50)
= 0.9 \* (10) + 0.1 \* (60)
= 9 + 6
= 15 ns

### Common Pitfalls
------------------

*   **Mistaking CHR for AMAT:** Be careful not to confuse the cache hit ratio with the average memory access time.
*   **Overlooking Miss Penalty Probability:** Remember that the miss penalty probability affects the average memory access time.

### Quick Summary
-----------------

*   **Cache Memory:**
    *   Small, fast memory that acts as an intermediate layer between main memory and CPU.
    *   Has multiple levels (L1, L2, L3).
*   **Main Memory:**
    *   Primary storage for data and program instructions.
    *   Volatile, meaning its contents are lost when power is turned off.
*   **Virtual Memory:**
    *   Combination of main memory and secondary storage.
    *   Provides an illusion of having more physical memory than available.

**Visuals**

No Mermaid diagrams or online images were included in this response as the format does not allow for them.