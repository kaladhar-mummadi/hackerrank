n = int(input())
arr = [int(i) for i in input().split(" ")]
counts = [0]*100
for i in arr:
    counts[i]+=1
for i in range(0,100):
    if counts[i] > 0:
        print(" ".join(map(str, [i]*counts[i])), end= " ")
