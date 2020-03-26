def shellSort(arr):
    k = len(arr)/2
    while(k >= 1):
        for current in range(k, len(arr)):
            temp = arr[current]
            walk = current - k
            while( walk >= 0 and temp < arr[walk]):
                arr[walk + k] = arr[walk]
                walk = walk - k
            arr[walk + k] = temp
        k = k /2
arr = [45,67,23,21,24,7,2,6,4,90]
shellSort(arr)
print arr


