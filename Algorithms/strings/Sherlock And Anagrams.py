from collections import *
t = int(input())
for _ in range(t):
    str = input()
    check = defaultdict(int)
    l = len(str)

    for i in range(l):
        for j in range(i + 1, l + 1):
            sub = list(str[i:j])
            sub.sort()
            sub = "".join(sub)
            check[sub] += 1
    sum = 0
    for i in check:
        n = check[i]
        sum += ( n * (n - 1) )/ 2
    print(int(sum))