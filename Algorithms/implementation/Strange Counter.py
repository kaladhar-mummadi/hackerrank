#!/bin/python3

import sys
import math

arr = []

MAX = math.pow(10,12)

t = int(input().strip())

if t <= 3:
    print(4 - t)
else:
    j = 3
    slots = 3
    while slots < t:
        j *= 2
        slots += j
    slots -= j
    print(j-(t-slots) + 1)