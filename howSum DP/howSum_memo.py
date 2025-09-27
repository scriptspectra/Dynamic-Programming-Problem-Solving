def howSumMemo(numbers, targetSum, memo=None):
    if targetSum in memo: return memo[targetSum]

    # base cases
    if targetSum == 0: return []
    if targetSum < 0: return None

    for number in numbers:
        remainder = targetSum - number
        result = howSumMemo(numbers, remainder)
        if result is not None:
            memo[remainder] = result + [number]
            return 