#!/bin/python3

import sys


Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    arr = [0]*26
    atleast_one_underscore = False
    out_of_order = False
    for i in b:
        if i != "_":
            arr[ord(i)-65] += 1
        else:
            atleast_one_underscore = True

    #
    if atleast_one_underscore == False:
        i = ord(b[0])-65
        arr[i] = -1
        for k in b[1:]:
            if (ord(k)-65) == i or arr[(ord(k)-65)] != -1:
                arr[(ord(k)-65)] = -1
                i = ord(k)-65
            elif arr[(ord(k)-65)] == -1:
                print("NO")
                break

        else:
            if n != 1:
                print("YES")
            else:
                print("NO")
    else:
        pairs_available = True
        for i in arr:
            if i == 1:
                pairs_available = False
                break
        if pairs_available and atleast_one_underscore:
            print("YES")
        else:
            print("NO")