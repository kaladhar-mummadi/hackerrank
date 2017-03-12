n = int(input())
arr1 = [int(i) for i in input().split(" ")]
m = int(input())
arr2 = [int(i) for i in input().split(" ")]
counts1 = [0]*101
counts2 = [0]*101
minimum1 = min(arr1)
for i in arr1:
    counts1[i-minimum1] += 1

for i in arr2:
    counts2[i-minimum1] += 1

result = set()
for i in range(0,101):
    if counts1[i] != counts2[i]:
        result.add(i)
result = sorted(result)
result = [minimum1+i for i in result]
print(" ".join(map(str,result)))