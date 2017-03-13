#!/bin/python3

import sys
import math
def dist(x1, y1, x2, y2):
    return math.sqrt(math.pow(abs(x1-x2),2) + math.pow(abs(y1-y2),2))
w,h = input().strip().split(' ')
w,h = [int(w),int(h)]
circleX,circleY,r = input().strip().split(' ')
circleX,circleY,r = [int(circleX),int(circleY),int(r)]
x1,y1,x3,y3 = input().strip().split(' ')
x1,y1,x3,y3 = [int(x1),int(y1),int(x3),int(y3)]
# your code goes here
pixels = [["." for i in range(w)] for j in range(h)]

#circle
top_left_circle_X = circleX - r
top_left_circle_Y = circleY - r
bottom_right_circle_X = circleX + r
bottom_right_circle_Y = circleY + r

for i in range(top_left_circle_X, bottom_right_circle_X+1):
    for j in range(top_left_circle_Y, bottom_right_circle_Y+1):
        if i < 0 or j < 0 or i >= w or j >= h:
            continue
        if dist(i,j,circleX, circleY) <= r:
            pixels[j][i] = "#"


#square
midp_x = (x1+x3)/2
midp_y = (y1+y3)/2
result = ""
for i in range(h):
    result += "".join(map(str,pixels[i])) + "\n"
print(result)