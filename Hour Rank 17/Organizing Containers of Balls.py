#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    M = []
    row_sum = []
    col_sum = []
    for M_i in range(n):
       M_t = [int(M_temp) for M_temp in input().strip().split(' ')]
       M.append(M_t)
       row_sum.append(sum(M_t))
    for i in range(n):
        s = 0
        for j in range(n):
            s += M[j][i]
        col_sum.append(s)
    row_sum = sorted(row_sum)
    col_sum = sorted(col_sum)
    i = 0
    for i in range(n):
        if row_sum[i] != col_sum[i]:
            break
    if i == n-1:
        print("Possible")
    else:
        print("Impossible")

    # your code goes here
