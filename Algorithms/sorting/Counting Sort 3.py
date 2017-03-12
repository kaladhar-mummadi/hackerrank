n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input().split(" ")[0]))
counts = [0]*100
for i in arr:
    counts[i]+=1
prev_sum = 0
for i in range(1,100):
    counts[i] += counts[i-1]
print(" ".join(map(str, counts)))