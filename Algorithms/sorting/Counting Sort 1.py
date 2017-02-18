n = int(input())
arr = [int(i) for i in input().split(" ")]
counts = [0]*100
for i in arr:
    counts[i]+=1
print(" ".join(map(str, counts)))