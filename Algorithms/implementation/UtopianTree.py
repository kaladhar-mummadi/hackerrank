t = int(input())

for a0 in range(t):
    n = int(input())
    result = 1
    for i in range(n):
        if (i + 1) % 2 == 0:
            result += 1
        else:
            result *= 2
    print(result)
