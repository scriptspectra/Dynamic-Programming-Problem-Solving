def fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_arr = [0, 1]
        for i in range(n-2):
            fib_arr.append(fib_arr[i]+fib_arr[i+1])
        return fib_arr
    
def fib_recursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
    
def dib1(n):
    print(n)
    if n < 1:
        return
    else:
        dib1(n-1)

def dib2(n):
    print(n)
    if n <= 0:
        return
    else:
        dib2(n-2)

# print(fib(8))
# print(f"8th fib: {fib_recursive(8)}")

print("Dib 1 executing...")
print(dib1(6))

print("Dib 2 executing...")
print(dib2(6))