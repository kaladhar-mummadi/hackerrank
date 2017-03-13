#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    first_dist = abs(x-z)
    second_dist = abs(y-z)
    if first_dist == second_dist:
        print("Mouse C")
    elif first_dist < second_dist:
        print("Cat A")
    else:
        print("Cat B")