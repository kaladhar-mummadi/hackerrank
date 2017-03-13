#!/bin/python3

import sys
def gcd(a,b):
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a
def lcmTwo(a,b):
    return ((a * b) // gcd(a,b))

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]
i = 1
lcm = a[0]
while i < n:
    lcm = lcmTwo(a[i], lcm)
    i += 1
i = 1
gcd_val = b[0]
while i < m:
    gcd_val = gcd(gcd_val, b[i])
    i += 1
count = 0
for  i in range(lcm, gcd_val+1):
    if i % lcm == 0 and gcd_val%i == 0:
        count += 1
print(count)