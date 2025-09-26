def canSumRecursion(numbers, targetSum):
    if targetSum == 0: return True
    if targetSum < 0: return False

    for number in numbers:
        if canSumRecursion(numbers, targetSum-number):
            return True
    
print(canSumRecursion([2,3,4,7], 7))