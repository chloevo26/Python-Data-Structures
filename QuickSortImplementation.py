def quick_sort(arr):
    quick_sort_help(arr, 0, len(arr)-1)


def quick_sort_help(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first, last)
        quick_sort_help(arr, first, splitpoint-1)
        quick_sort_help(arr, splitpoint+1, last)


def partition(arr, first, last):
    pivotvalue = arr[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        # increment the leftmark until we locate the value that greater than the pivot value
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark += 1
        # decrement the rightmark until we locate the value that less than the pivot value
        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp
    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark

arr = [2,3,5,1,4,7,6,8]
quick_sort(arr)
print arr
