length = int(input())
ar = [int(i) for i in input().strip().split()]
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
    print(" ".join(map(str, ar)))

    return i

def quickSort(left, right):
    global ar
    if left >= right-1:
        return
    pivotIndex = partition(left, right)
    quickSort(left, pivotIndex)

    quickSort(pivotIndex+1, right)
quickSort(0, length)