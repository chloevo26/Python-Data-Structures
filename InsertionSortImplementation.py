def insertion_sort(arr):
    for i in range(1, len(arr)):
        currentValue = arr[i]
        position = i
        while position > 0 and arr[position-1] > currentValue:
            arr[position] = arr[position-1]
            position = position -1

        arr[position] = currentValue

arr = [4,6,2,7,1,9,11]
insertion_sort(arr)
print arr