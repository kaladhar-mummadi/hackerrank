#!/bin/python3

import sys


n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
freq = [0] * 6
for i in types:
    freq[i] += 1
maximum = -1
max_num = -1
i = 1
while i < 6:
    if maximum < freq[i]:
        maximum = freq[i]
        max_num = i
    i += 1
print(max_num)