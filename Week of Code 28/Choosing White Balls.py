#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
balls = input().strip()
# your code goes here
possibilities = []
#
# for ball in balls:
#     if ball == 'W':
#         arr[ball] = True
possibilities.append(balls)

res = 0
while k:

    next_possibilities_removed_white = []
    next_possibilities_removed_black = []
    removed_black = 0
    removed_white = 0

    for possibility in possibilities:
        no_of_times_possible_removed_white = 0
        no_of_times_possible_removed_black = 0
        for i in range(0, len(possibility)):
            from_left = i
            from_right = n - 1 - i
            if possibility[from_left] == "W" and from_left != from_right:
                no_of_times_possible_removed_white += 1
                next_possibilities_removed_white.append(possibility[:from_left] + possibility[from_left+1:])
            elif possibility[from_right] == "W":
                no_of_times_possible_removed_white += 1
                next_possibilities_removed_white.append(possibility[:from_right] + possibility[from_right+1:])

            if possibility[from_left] == "B" and from_left != from_right:
                no_of_times_possible_removed_black += 1
                next_possibilities_removed_black.append(possibility[:from_left] + possibility[from_left+1:])
            elif possibility[from_right] == "B":
                no_of_times_possible_removed_black += 1
                next_possibilities_removed_black.append(possibility[:from_right] + possibility[from_right+1:])

        removed_white += no_of_times_possible_removed_white/n
        removed_black += (1 - no_of_times_possible_removed_black/n)
    next_possibilities_removed_white = list(set(next_possibilities_removed_white))
    next_possibilities_removed_black = list(set(next_possibilities_removed_black))
    expected_white = (1/len(possibilities) * (removed_white))
    expected_blac = (1/len(possibilities) * (removed_black))
    if len(next_possibilities_removed_white) == 0:
        break
    if expected_white > expected_blac:
        possibilities = next_possibilities_removed_white
        res += expected_white
    elif expected_white == expected_blac:
        print("equal")
    else:
        possibilities = next_possibilities_removed_black
        res += expected_blac
    n -= 1
    k -= 1
print(format(res, ".6f"))