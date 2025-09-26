def gridTraveler(rows, cols):
    if rows == 0 or cols == 0: return 0
    if rows == 1 and cols == 1: return 1

    return gridTraveler(rows-1, cols) + gridTraveler(rows, cols-1)

print(gridTraveler(2, 3))
print(gridTraveler(3, 2))