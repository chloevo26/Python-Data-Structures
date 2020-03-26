def insertionSort(arr):
    for current in range(1, len(arr)):
        temp = arr[current]
        walk = current - 1
        while(walk >= 0 and temp < arr[walk]):
            arr[walk + 1] = arr[walk]
            walk = walk - 1
        arr[walk + 1] = temp
arr = [4,6,2,7,1,9,11]
insertionSort(arr)
print arr