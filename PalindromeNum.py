def palindrome(n):
    if n < 0 or (n %10 == 0 and n!= 0):
        return False
    else:
        revNum = 0
        while(n > revNum):
            revNum = revNum * 10 + n%10
            n /= 10
    return n == revNum or n == revNum/10


print(palindrome(12321))




