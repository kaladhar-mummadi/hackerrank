length = int(input())
arr = [int(temp) for temp in input().split(" ")]
i = 0
while i < length:
    element = arr[i]
    j = i - 1
    while j >= 0:
        if arr[j] > element:
            arr[j + 1] = arr[j]
            print(" ".join(str(temp) for temp in arr))
            arr[j] = element
        j -= 1
    i += 1
print(" ".join(str(temp) for temp in arr))