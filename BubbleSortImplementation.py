def bubble_sort(arr):
    # go backward except for the very last element
    for n in range(len(arr)-1,0, -1):
        print 'This is the n: ', n
        for k in range(n):
            print 'This is the k index check: ',k
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp

arr = [5,3,7,4]
bubble_sort(arr)
print(arr)
