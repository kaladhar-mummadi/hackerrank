#!/bin/python3

import sys
import math

n = int(input().strip())
len_arr = [0] * 1000000
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   dig_len = len(unsorted_t) - 1
   if len_arr[dig_len] == 0 :
       len_arr[dig_len] = [unsorted_t]
   else:
       len_arr[dig_len].append(unsorted_t)
   unsorted.append(unsorted_t)
sort_arr = []
for elements in len_arr:
    if elements !=0:
        sort_arr += sorted(elements)
print("\n".join(sort_arr))
