#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
maximum = max(height)
if maximum - k <=0 :
    print(0)
else:
    print(maximum - k)