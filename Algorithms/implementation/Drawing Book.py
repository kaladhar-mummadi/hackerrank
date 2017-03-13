#!/bin/python3

import sys


n = int(input().strip())
p = int(input().strip())
from_front = p // 2
total = n // 2
from_back = total - from_front
if from_front < from_back:
    print(from_front)
else:
    print(from_back)