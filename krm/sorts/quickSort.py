def swap(arr, i , j):
    arr[j], arr[i] = arr[i], arr[j]

def partition(ar, start, end) :
    pivot = ar[end-1]
    i = start - 1
    for j in range(start,end):
        if ar[j] <= pivot:
            i += 1
            swap(ar, i, j)
    print(" ".join(map(str, ar)))

    return i
def inPlace(ar, left, right):
    if left >= right-1:
        return
    pivotIndex = partition(ar, left, right)
    inPlace(ar, left, pivotIndex)

    inPlace(ar, pivotIndex+1, right)