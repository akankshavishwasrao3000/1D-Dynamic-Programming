# 1D-Dynamic-Programming
Step-by-step 1D Dynamic Programming practice in Python, covering Fibonacci, Climbing Stairs, Frog Jump, Maximum Sum of Non-Adjacent Elements, and Minimum Cost Climbing Stairs.
# 1D Dynamic Programming

This folder contains my step-by-step practice of **1D Dynamic Programming (DP)** problems in Python.

The problems focus on understanding how a solution can be built from previously calculated states and stored in a one-dimensional `dp` array.

## Problems Covered

| # | Problem                              | Main Concept                |
| - | ------------------------------------ | --------------------------- |
| 1 | Fibonacci Number                     | Basic DP                    |
| 2 | Climbing Stairs                      | DP with previous two states |
| 3 | Frog Jump                            | Minimum cost DP             |
| 4 | Maximum Sum of Non-Adjacent Elements | Take / Skip DP              |
| 5 | Minimum Cost Climbing Stairs         | Minimum cost DP             |

## Learning Approach

For each problem, I am practicing:

* Understanding the problem
* Identifying the DP state
* Creating the `dp` array
* Handling base cases
* Building the solution step by step
* Checking edge cases
* Understanding time and space complexity

## Example DP Pattern

A common 1D DP approach is:

```python
dp = [0] * n

# Base cases
dp[0] = ...

# Build the answer
for i in range(1, n):
    dp[i] = ...
```

The exact transition depends on the problem.

## Goal

The goal of this folder is to build a strong foundation in **1D Dynamic Programming** through simple problems before moving to more complex DP patterns.
