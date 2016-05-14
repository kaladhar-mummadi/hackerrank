t = int(input())

for a0 in range(t):
    numberOfStones = int(input())
    a = int(input())
    b = int(input())
    tempArray = [a, b]
    tempArray.sort()
    a, b = tempArray
    result = []
    i = 0
    while i < numberOfStones:
        value = str(a * (numberOfStones - 1 - i) + b * i)
        if len(result) == 0:
            result.append(value)
        elif value != result[-1]:
            result.append(value)
        i += 1
    print(" ".join(result))
