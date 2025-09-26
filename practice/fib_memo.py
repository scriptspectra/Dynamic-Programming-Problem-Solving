from time import time

def fib_memo(n, memo={}):
    """returns nth fibonacci number through memoization technique"""
    if n in memo: return memo[n]

    if n == 0 or n == 1: return n

    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

print("Fib - Memoization")

# 20th fibonacci number
start_time_1 = time()
print(fib_memo(20))
end_time_1 = time()
print(f"time taken: {end_time_1-start_time_1}")

# 40th fibonacci number
start_time_2 = time()
print(fib_memo(40))
end_time_2 = time()
print(f"time taken: {end_time_2-start_time_2}")