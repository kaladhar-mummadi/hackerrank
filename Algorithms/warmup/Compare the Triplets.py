a = [int(temp) for temp in input().split(" ")]
b = [int(temp) for temp in input().split(" ")]


aSum =0
bSum = 0
i = 0
while i < 3:
    if a[i] > b[i]:
        aSum += 1
    elif a[i] < b[i]:
        bSum += 1
    i += 1
print(aSum, bSum)