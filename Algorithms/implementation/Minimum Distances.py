n = int(input())
A = [int(temp) for temp in input().split(" ")]
indexes = {}
index = 0
for i in A:
    if i in indexes:
        indexes[i][-1] = index - indexes[i][-1]
        indexes[i].append(index)
    else:
        indexes[i] = [index]
    index += 1
res = -1
for i in indexes:
    value = indexes[i]
    if len(value) > 1:
        minimum = min(value)
        if res == -1 or res > minimum:
            res = minimum
print(res)