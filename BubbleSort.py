def bubbleSort(arr):
    n = len(arr)

    # traverse through all array elements
    for i in range(n):
        # last i elements are already in place
        for j in range(n-i-1):
            # traverse the array from 0 to n-i-1
            # swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [64,34,25,12,22,11,90]
bubbleSort(arr)
print(arr)
