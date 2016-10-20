n = int(input())
gemStoneMap = {}
result = 0
for i in range(ord('a'), ord('z') + 1):
    gemStoneMap[chr(i)] = 0

for _ in range(n):
    composition = input()
    compositionSet = set()
    for i in range(len(composition)):
        compositionSet.add(composition[i])
    for j in compositionSet:
        gemStoneMap[j] += 1
        if gemStoneMap[j] == n:
            result += 1
print(result)