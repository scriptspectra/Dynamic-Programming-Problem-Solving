### Problem description:
# Given a target sum `targetSum` and a list of numbers `numbers`,
# determine if it is possible to generate the `targetSum` 
# by summing any combination of elements from `numbers`.
#
# * You may use an element of `numbers` as many times as needed.
# * All input numbers are non-negative integers.
# * Return True if the target sum can be made, otherwise False.
#
# ---
#
### Example:
#
# numbers = [2, 3], targetSum = 7
#
# Possible combinations:
# - 3 + 2 + 2 = 7
# - 2 + 2 + 3 = 7
#
# So the output is True
#
# numbers = [5, 3, 4, 7], targetSum = 7
# - 7 = 7 (direct)
# - 3 + 4 = 7
# Output: True
#
# numbers = [2, 4], targetSum = 7
# - No combination sums to 7
# Output: False
#
# ---
#
### Base cases:
#
# * If targetSum == 0 → return True (no numbers needed)
# * If targetSum < 0 → return False (cannot sum to negative)
#
# ---
#
### Recurrence relation:
#
# For each number in numbers:
#   - Check if targetSum - number can be summed recursively
#   - If any recursive call returns True → targetSum can be made
#
# Formula:
#   canSum(targetSum, numbers) = OR(canSum(targetSum - num, numbers) for num in numbers)
#
# ---
#
### Why this is a DP problem:
#
# * Many subproblems overlap (same targetSum occurs multiple times)
# * Using **memoization** (top-down) or **tabulation** (bottom-up) 
#   improves efficiency from exponential to polynomial time.
