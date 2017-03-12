n = int(input())
arr = []
strings = []
counts = [0]*100
for _ in range(n):
    inputData = input().split(" ")
    arr.append(int(inputData[0]))
    strings.append(inputData[1])
    counts[int(inputData[0])] += 1

for i in range(1,100):
    counts[i] += counts[i-1]

sortedArray = [""]*n
for i in range(n-1, -1, -1):
    if i >= n//2:
        sortedArray[counts[arr[i]] - 1] = strings[i]
    else:
        sortedArray[counts[arr[i]] - 1] = "-"
    counts[arr[i]] -= 1
print(" ".join(sortedArray))