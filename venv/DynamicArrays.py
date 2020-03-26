import sys

n = 50
data = []
for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)

    print('Length: {0:3d}; Size in bytes: {1:4d} '.format(a,b))
    data.append(n)

# what python does is it set the number of bytes larger than what is needs to hold the current elements in the list
# there is an underlying change in memory when you insert more and more elements until you need a memory usage jump
