# dynamic programming 
# 1. memoization
# 2. tabulation

def fib_memo(n, memo):
    if n in memo:
        return memo[n]
    else:
        if n <= 1:
            memo[n] = n
            return n
        else:
            memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
            return memo[n]
        
memo = {}

print(fib_memo(50, memo))  # Output: 12586269025