t = int(input())

for testcase in range(t):
    n = int(input())
    temp = n
    result = 0
    while (int(temp) != 0):
        digit = temp % 10
        if (digit != 0 and n % digit == 0):
            result += 1
        temp = int(temp / 10)
    print(result)
