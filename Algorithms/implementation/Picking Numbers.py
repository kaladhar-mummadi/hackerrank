n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
arr = [0]*101
for i in a:
    arr[i] += 1
maximum = 0
i = 1
while i < n:
    temp = arr[i] + arr[i-1]
    if temp > maximum:
        maximum = temp
    i += 1
print(maximum)