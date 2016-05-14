import math

testCases = int(input())

for testcase in range(testCases):
    a, b = [int(temp) for temp in input().split(' ')]
    squareRootOfa = int(math.sqrt(a))
    squareRootOfb = int(math.sqrt(b))
    result = squareRootOfb - squareRootOfa
    if (pow(squareRootOfa, 2) == a):
        result += 1
    print(result)
