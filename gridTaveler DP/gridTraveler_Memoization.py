def gridTravelerMemo(n, m, memo={}):
    # memo key
    key = f"{n},{m}"

    if key in memo: return memo[key]

    if n == 1 and m == 1: return 1
    if n == 0 or m == 0: return 0

    memo[key] = gridTravelerMemo(n-1, m, memo) + gridTravelerMemo(n, m-1, memo)
    return memo[key]

print(gridTravelerMemo(2,3))
print(gridTravelerMemo(18,18))