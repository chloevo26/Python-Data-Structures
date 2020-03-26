def selectionSort(arr):
    # traverse through the array
    for i in range(len(arr)):
        # set the first element in the unsorted array as minimum
        min_idx = i
        # traverse through the unsorted array, find min
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # swap the found minimum with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [64, 25, 12, 22, 11]
selectionSort(arr)
print arr