n, d = input().split(" ")
[n, d] = [int(n), int(d)]
arr = [int(temp) for temp in input().split(" ")]
visited = [False]*n
i = 0
total = 0
while i < n-1:
    if visited[i] == True:
        i += 1
        continue
    j = i +1
    prev = arr[i]
    count = 1
    visited[i] = True
    while j < n and (prev+d) >= arr[j]:
        if prev+d == arr[j]:
            count += 1
            prev = arr[j]
            visited[j] = True

        j += 1
    if count >= 3:
        total += ( count - 2)
    i += 1
print(total)

