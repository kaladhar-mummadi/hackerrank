length = int(input())
ar = [int(i) for i in input().strip().split()]
ar2 = ar[:]
quicksortSwaps = 0
insertionSwaps = 0
def swap(arr, i , j):
    global quicksortSwaps
    quicksortSwaps += 1
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
def insertionSort():
    global ar2
    global insertionSwaps
    i = 1
    while i < length:
        element = ar2[i]
        j = i - 1
        while j >= 0:
            if ar2[j] > element:
                insertionSwaps += 1
                ar2[j + 1] = ar2[j]
                ar2[j] = element
            j -= 1
        i += 1

def quickSort(left, right):
    global ar
    if left >= right-1:
        return
    pivotIndex = partition(left, right)
    quickSort(left, pivotIndex)

    quickSort(pivotIndex+1, right)
quickSort(0, length)
insertionSort()
print(insertionSwaps-quicksortSwaps)