length = int(input())
arr = [int(i) for i in input().split(" ")]
arr = sorted(arr)
diffs = []
minimum_diff = -1
for i in range(0, length-1):
    diffs.append(arr[i+1] - arr[i])
    if minimum_diff > diffs[i] or minimum_diff == -1:
        minimum_diff = diffs[i]
i = 0
pairs = []
for diff in diffs:
    if minimum_diff == diff:
        pairs.append(arr[i])
        pairs.append(arr[i+1])
    i += 1
print(" ".join(map(str, pairs)))