#!/bin/python3

import sys

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

if (x1 > x2 and v1 < v2) or (x1 < x2 and v1 > v2):
    ahead = abs(x1 - x2)
    each_step_near = abs(v1 - v2)
    if (ahead % each_step_near) == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
