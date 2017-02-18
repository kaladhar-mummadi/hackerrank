length = int(input())
arr = [int(temp) for temp in input().split(" ")]
i = 1
while i < length:
    element = arr[i]
    j = i - 1
    while j >= 0:
        if arr[j] > element:
            arr[j + 1] = arr[j]
            arr[j] = element
        j -= 1
    print(" ".join(str(temp) for temp in arr))
    i += 1