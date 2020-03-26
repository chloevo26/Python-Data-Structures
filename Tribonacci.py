def tribonacci(n):
    if n == 0:
        return n
    elif n == 1 or n == 2:
        return 1
    else:
        return tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)


#print(tribonacci(25))


def trib(n):
    cache = {}
    if n == 0:
        cache[n] = 0
        return n
    elif n == 1 or n == 2:
        cache[n] = 1
        return 1
    else:
        if n in cache:
            return cache[n]
        else:
            result = trib(n - 3) + trib(n - 2) + trib(n - 1)
            cache[n] = result
            return result

print(trib(27))

def trib_iter(n):
    a,b,c = 0,1,1
    for i in range(2,n):
        a,b,c = b,c,a+b+c
    return c

print(trib_iter(4))