length = int(input())
ar = [int(i) for i in input().strip().split()]
median = -1
def swap(arr, i , j):
    arr[j], arr[i] = arr[i], arr[j]

def partition(start, end) :
    global ar
    pivot = ar[end-1]
    i = start - 1
    for j in range(start,end):
        if ar[j] <= pivot:
            i += 1
            swap(ar, i, j)
    return i

def quickSort(left, right):
    global ar
    global median
    if left >= right-1 or median != -1:
        return
    pivotIndex = partition(left, right)

    quickSort(left, pivotIndex)
    if pivotIndex >= int(length/2) and median == -1:
        median = pivotIndex
        print(ar[int(length/2)])
    quickSort(pivotIndex+1, right)
quickSort(0, length)