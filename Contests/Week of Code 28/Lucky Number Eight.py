#!/bin/python3

import sys

MOD = 1000000007
n = int(input().strip())
number = input().strip()
# your code goes here
single = {}
index = 0
result = 0
for i in number:
    if int(i) % 2 == 0:
        if i in single:
            single[i].append(index)
        else:
            single[i] = [index]
    index += 1
double = {}
index = 0
for i in number:
    for key, value in single.items():
        double_digit = i + key
        if int(double_digit) % 4 == 0:
            # for internal in value:
            # if index >= value.index(index):
            #     continue
            if double_digit in double:
                if index in double[double_digit]:
                    total = double[double_digit][index]
                else:
                    total = 0
                double[double_digit][index] = total + (len(value) - value.index(index) - 1)
            else:
                double[double_digit] = {index: len(value) - value.index(index) - 1}
    index += 1

triple = {}

index = 0
for i in number:
    for key, value in double.items():
        triple_digit = i + key
        if int(triple_digit) % 8 == 0:
            for key, internal in value.items():
                if index >= key:
                    continue
                if triple_digit in triple:
                    if index in triple[triple_digit]:
                        total = triple[triple_digit][index]
                    else:
                        total = 0
                    triple[triple_digit][index] = total + internal
                else:
                    triple[triple_digit] = {index: internal}

    index += 1


def fastFact(base, power):
    temp = base
    ret = 1
    while (power):
        if power & 1:
            ret = (ret * temp) % MOD
        temp = (temp * temp) % MOD
        power >>= 1
    return ret


def differentIndexSum(arr):
    n = len(arr)
    return (n * (n + 1)) // 2


for key, items in single.items():
    if int(key) % 8 == 0:
        result = (result + len(items)) % MOD
for key, items in double.items():
    if int(key) % 8 == 0:
        result = (result + sum(list(items.values()))) % MOD
for key, value in triple.items():
    for index,comb in value.items():
        if comb == 0:
            continue
        temp = (comb * fastFact(2, index)) % MOD
        #result = (result + fastFact(2, int(index))) % MOD
        #result = (result * comb) % MOD
        result = (result + temp) % MOD
print(result)
