def pair_sum(arr, k):
    counter = 0;
    dict = {}
    result = set()
    for i,val in enumerate(arr):
        n = k - val
        if n not in dict:
            dict[val] = i
        else:
            result.add((val,n))
    return len(result)

print(pair_sum([1,3,2,2],4))
print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
print(pair_sum([1,2,3,1],3))