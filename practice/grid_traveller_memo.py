def gridTravellerMemo(rows, cols, memo={}):
    key = f"{rows},{cols}"

    if key in memo: return memo[key]

    if rows == 0 or cols == 0: 
        memo[key] = 0
    elif rows == 1 and cols == 1: 
        memo[key] = 1
    else:
        memo[key] = gridTravellerMemo(rows-1, cols, memo) + gridTravellerMemo(rows, cols-1, memo)

    return memo[key]

print(gridTravellerMemo(2, 3))
print(gridTravellerMemo(18, 18))