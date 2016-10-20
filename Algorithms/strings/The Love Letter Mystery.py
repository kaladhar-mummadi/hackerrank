tests = int(input())

for _ in range(tests):
    str = input()
    i = 0
    j = len(str) - 1
    result = 0
    while i < j :
        if str[i] < str[j]:
            result += (ord(str[j]) - ord(str[i]))
        else:
            result += (ord(str[i]) - ord(str[j]))
        i += 1
        j -= 1
    print(result)