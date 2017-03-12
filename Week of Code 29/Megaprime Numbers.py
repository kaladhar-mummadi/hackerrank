#!/bin/python3

import sys
import math

first, last = input().strip().split(' ')
first, last = [int(first), int(last)]
one_digits = [2, 3, 5, 7]
primes = [2, 3, 5, 7]
digits = 0

digit_len = len(str(last))
def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False

    return True
prev_arr = set([2,3,5,7])
prev_index = 0
for i in range(2, digit_len + 1):
    temp_arr = []
    all_numbers = []
    last_index = prev_index
    for j in prev_arr:
        for k in one_digits:
            suffix_add = j * 10 + k
            prefix_add = k * int(math.pow(10, i - 1)) + j
            if (suffix_add in temp_arr) == False and isPrime(suffix_add):
                temp_arr.append(suffix_add)
            if (prefix_add in temp_arr) == False and isPrime(prefix_add):
                temp_arr.append(prefix_add)
            all_numbers.append(suffix_add)
            all_numbers.append(prefix_add)
    prev_arr = set(all_numbers)
    primes += temp_arr
res = 0
primes = sorted(primes)
for i in primes:
    if i >= first and i <= last:
        res += 1
print(res)