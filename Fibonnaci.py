def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

print(fib_rec(10))


n = 10
cache = [None] * (n+1)

def fib_dyn(n):
    if n == 0 or n == 1:
        return n
    if cache[n] != None:
        return cache[n]
    result = fib_dyn(n-1) + fib_dyn(n-2)
    cache[n] = result
    return result

print(fib_dyn(10))

def fib_iter(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

print(fib_iter(10))