def gridtraveler_Rec(n, m):
    """calculates number of paths we can travel from start to end"""
    if n == 1 and m == 1 : return 1
    if n == 0 or m == 0 : return 0

    # we can move only to right or down from the current position
    # gridtraveler_Rec(n-1, m) --- moving down
    # gridtraveler_Rec(n, m-1) --- moving right
    return gridtraveler_Rec(n-1, m) + gridtraveler_Rec(n, m-1)

print(gridtraveler_Rec(2,3))