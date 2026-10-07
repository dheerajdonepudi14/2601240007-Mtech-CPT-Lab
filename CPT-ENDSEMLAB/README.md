# 0/1 Knapsack Dynamic Programming

## Problem Statement

A cloud service provider has a limited amount of computing resources. Each application requires a specific amount of resources and generates a certain revenue. Each application can either be deployed completely or not deployed.

Implement the 0/1 Knapsack Dynamic Programming algorithm to maximize revenue within the available resource capacity.

The program must display:
- Maximum revenue
- Selected applications
- DP table
- Time complexity
- Space complexity

## Concept Identification

**Algorithm:** 0/1 Knapsack

**Technique:** Dynamic Programming

**Problem Type:** Optimization Problem

The algorithm considers every application and makes two choices:
1. Select the application.
2. Do not select the application.

The choice that gives the higher revenue is stored in the DP table.

## Example

| Application | Resource Required | Revenue |
|---|---:|---:|
| App A | 2 | 40 |
| App B | 3 | 50 |
| App C | 4 | 70 |
| App D | 5 | 80 |

Available resource capacity: **7**

One optimal solution is App B and App C.

Total resources = 3 + 4 = **7**

Total revenue = 50 + 70 = **120**

## Procedure

1. Store the resource requirement and revenue of every application.
2. Read the available resource capacity.
3. Create a DP table with rows for applications and columns for resource capacities.
4. Process every application and every possible capacity.
5. If the application cannot fit, copy the previous value.
6. If it can fit, calculate the revenue for selecting and not selecting it.
7. Store the larger value in the DP table.
8. The bottom-right cell contains the maximum revenue.
9. Backtrack through the table to find the selected applications.
10. Display the result and complexity.

## Implementation

The complete executable implementation is provided in `Program_2.py`.

## Input

- Applications: App A, App B, App C, App D
- Resources: 2, 3, 4, 5
- Revenue: 40, 50, 70, 80
- Capacity: 7

## Output

```text
============================================================
0/1 KNAPSACK - CLOUD RESOURCE ALLOCATION
============================================================

Available Resource Capacity: 7

Maximum Revenue: 120

Selected Applications:
- App B (Resource = 3, Revenue = 50)
- App C (Resource = 4, Revenue = 70)

Total Resources Used: 7
Total Revenue: 120
```

## DP Table

| Application / Capacity | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| None | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| App A | 0 | 0 | 40 | 40 | 40 | 40 | 40 | 40 |
| App B | 0 | 0 | 40 | 50 | 50 | 90 | 90 | 90 |
| App C | 0 | 0 | 40 | 50 | 70 | 90 | 110 | 120 |
| App D | 0 | 0 | 40 | 50 | 70 | 90 | 110 | 120 |

The bottom-right value, `dp[4][7]`, is **120**, the maximum revenue.

## Complexity Analysis

### Time Complexity

The DP table has `n x C` states, where `n` is the number of applications and `C` is the available capacity.

**Time Complexity: O(n x C)**

### Space Complexity

The complete DP table stores approximately `(n + 1) x (C + 1)` values.

**Space Complexity: O(n x C)**

## Conclusion

The 0/1 Knapsack Dynamic Programming algorithm finds the maximum possible revenue without exceeding the available cloud resource capacity.

For the sample input, the maximum revenue is **120**.

Each application is selected at most once.

## Execution

Run the program using:

```bash
python Program_2.py
```

No external Python packages are required.
