#!/bin/python3

import sys


N = int(input().strip())
arr = [int(B_temp) for B_temp in input().strip().split(' ')]
no_of_odds = 0
bread_loves = 0
prev_odd_index = -1
for i in range(N):
    number = arr[i]
    if number%2 != 0:
        no_of_odds += 1
        if prev_odd_index != -1:
            bread_loves += (i-prev_odd_index)
        if i > 0 and arr[i-1]%2 != 0 and prev_odd_index != -1:
            prev_odd_index = -1
        else:
            prev_odd_index = i
if no_of_odds%2 != 0:
    print("NO")
else:
    print((bread_loves)*2)