#!/bin/python3

import sys
import math
import operator

#
# min,max = input().strip().split(' ')
# min,max = [int(min),int(max)]
arr = {}
for i in range(1,1000):
    fractional_value =  ((i*3) + 1) / i
    arr[i] = abs(fractional_value - math.pi)
arr = sorted(arr.items(), key = operator.itemgetter(1))

for (key,value) in arr:
    print(key,  value)