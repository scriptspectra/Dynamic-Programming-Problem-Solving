def canSumMemoization(numbers, targetSum, memo={}):
    if targetSum in memo: return memo[targetSum]

    if targetSum == 0: return True
    if targetSum < 0: return False

    for number in numbers:
        if canSumMemoization(numbers, targetSum-number):
            memo[targetSum] = True
            return True
        
    memo[targetSum] = False
    return False
        
print(canSumMemoization([2,3,4,7], 7))
print(canSumMemoization([7,14], 300))