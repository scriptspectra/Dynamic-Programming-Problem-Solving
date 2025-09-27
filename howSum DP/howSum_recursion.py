def howSumRecursion(numbers, targetSum):
    if targetSum == 0: return []
    if targetSum < 0: return None

    for number in numbers:
        remainder = targetSum - number
        result = howSumRecursion(numbers, remainder)
        if result is not None:
            return result + [number]       

print(howSumRecursion([2,3,4,7], 7))