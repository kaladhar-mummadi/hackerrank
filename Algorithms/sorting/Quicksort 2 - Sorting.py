length = int(input())
ar = [int(i) for i in input().strip().split()]

def partition(start, end) :
    left = []
    right = []
    global ar
    pivot = ar[start]
    for j in range(start,end):
        if ar[j] < pivot:
            left.append(ar[j])
        elif ar[j]> pivot:
            right.append(ar[j])

    temp = left + [pivot]+right
    j = 0
    for i in range(start,end):
        ar[i] = temp[j]
        j += 1
    return start + len(left)


def quickSort(left, right):
    global ar
    if left >= right:
        return
    pivotIndex = partition(left, right)
    quickSort(left, pivotIndex)

    quickSort(pivotIndex+1, right)
    if right -left >= 2:
        print(" ".join(map(str, ar[left:right])))
quickSort(0, length)