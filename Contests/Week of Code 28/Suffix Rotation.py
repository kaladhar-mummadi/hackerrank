#!/bin/python3

import sys

def swap(str, index1, index2):
    diff = index2 - index1
    swap_len = len(str) - index1
    while swap_len:
        print("test")
    temp = str[index1]
    str[index1] = str[index2]
    str[index2] = temp
    return str
def howFar(str, alphabets, current_index):
    required_char = ""
    index = current_index
    next_char = 0
    for val in alphabets:
        temp_char = chr(next_char + 97)
        if temp_char == str[current_index]:
            return -1
        if val != 0:
            required_char = temp_char
        next_char += 1
    for i in str[current_index:]:
        if i == required_char:
            return index
        index += 1
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    alphabets = [0]*26
    for i in s:
        alphabets[ord(i) - 97] += 1
    i = 0
    s_len = len(s)
    while i < s_len:
        next_char_index = howFar(str, alphabets, i)
        if  next_char_index != -1 :
            swap(str, i, next_char_index)

