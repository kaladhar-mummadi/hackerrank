#!/bin/python3

import sys


n = int(input().strip())
vertical = True
horizontal = True
x1,y1 = input().strip().split(' ')
x1, y1 = [int(x1),int(y1)]
for a0 in range(n - 1):
    x,y = input().strip().split(' ')
    x,y = [int(x),int(y)]
    vertical = True if vertical and x == x1 else False
    horizontal = True if horizontal and y == y1 else False

if vertical or horizontal:
    print("YES")
else:
    print("NO")