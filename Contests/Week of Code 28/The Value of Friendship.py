#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,m = input().strip().split(' ')
    n,m = [int(n),int(m)]
    total = 0
    relations = [[]]
    prev_sum = 0
    for i in range(1, n+1):
        relations.append([])
    all_independent = []
    for a1 in range(m):
        x,y = input().strip().split(' ')
        x,y = [int(x),int(y)]
        # your code goes here

        x_already_friends = len(relations[x])
        y_already_friends = len(relations[y])
        if x_already_friends == 0:
            relations[y].append(x)
            relations[x].append(y)
            for friend in relations[y]:
                if x == friend:
                    continue
                relations[friend].append(x)
                relations[x].append(friend)
            prev_sum = prev_sum + len(relations[x]) * 2
            total += prev_sum
        elif y_already_friends == 0:
            relations[y].append(x)
            relations[x].append(y)
            for friend in relations[x]:
                if y == friend:
                    continue
                relations[friend].append(y)
                relations[y].append(friend)
            prev_sum = prev_sum + len(relations[y]) * 2
            total += prev_sum
        else:
            total += prev_sum
    print(total)