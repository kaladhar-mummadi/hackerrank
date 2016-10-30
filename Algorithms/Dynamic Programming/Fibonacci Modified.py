t1,t2, n = [int(temp) for temp in input().split(' ')]
arr = [t1,t2]
i = 2
while i < n:
    arr.append((arr[i - 1]* arr[i-1]) + arr[i-2])
    i +=1
print(arr[n-1])