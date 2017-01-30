#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    arr = []
    all_values = [False] * (n +1)
    for i in range(1, n+1):
        if i <= k and k+i <= n :
            arr.append(k+i)
            all_values[k+i] = True
        elif i-k >= 0:
            arr.append(i-k)
            all_values[i-k] = True
    no_repeated = True
    for i in range(1,n+1):
        if not all_values[i]:
            no_repeated = False
    if no_repeated:
        print(" ".join(str(x) for x  in arr))
    else:
        print("-1")