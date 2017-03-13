#!/bin/python3

import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()
temp_arr = []
length = 0
for i in word:
    temp_arr.append(h[ord(i) - ord('a')])
    length += 1
max_hieght = max(temp_arr)
print(max_hieght * length)
