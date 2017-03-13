n = int(input())
arr = [int(temp) for temp in input().split(" ")]
freq = [0]*101
for i in arr:
    freq[i] += 1
minimum = n
for i in freq:
    diff = n - i
    if diff < minimum:
        minimum = diff
print(minimum)
