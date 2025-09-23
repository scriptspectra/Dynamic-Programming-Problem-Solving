### Problem description:
# Imagine you are standing in the top-left corner of an `m × n` grid.
# You want to travel to the bottom-right corner.
#
# * You can only move **down** or **right** at each step.
# * The question is: How many unique ways are there to travel across the grid?
#
# ---
#
### Example:
#
# For a `2 × 3` grid (2 rows, 3 columns):
#
# Start → □ → □
#   ↓       ↓
#   □ → □ → End
#
# There are 3 unique paths:
# 1. Right → Right → Down
# 2. Right → Down → Right
# 3. Down → Right → Right
#
# ---
#
### Base cases:
#
# 1. If either dimension is 0 (`0 × n` or `m × 0`), there are 0 ways (no grid).
# 2. If it’s a `1 × 1` grid, there is exactly 1 way (you’re already at the destination).
#
# ---
#
### Recurrence relation:
#
# To reach a cell `(m, n)`, you must come either:
# * From the top `(m-1, n)`
# * Or from the left `(m, n-1)`
#
# Formula:
#   gridTraveler(m, n) = gridTraveler(m-1, n) + gridTraveler(m, n-1)
#
# ---
#
### Why this is a DP problem:
#
# * The subproblems overlap a lot (same (m, n) values get recomputed).
# * With memoization (top-down) or tabulation (bottom-up), the solution is efficient.
#
# Examples:
# * gridTraveler(2, 3) = 3
# * gridTraveler(3, 3) = 6
# * gridTraveler(18, 18) = huge number, but DP makes it feasible.