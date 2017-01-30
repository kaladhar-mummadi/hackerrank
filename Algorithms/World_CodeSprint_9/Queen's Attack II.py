def positionToBeRemoved(rQ, cQ, rO, cO, n):
    res = 0
    r_diff = abs(rQ-rO)
    c_diff = abs(cQ-cO)
    if rO == rQ:
         if cO > cQ:
             res = n - cO + 1
         elif cO < cQ:
             res = cO
    elif cO == cQ:
        if rO > rQ:
            res = n - rO + 1
        elif rO < rQ:
            res = rO
    elif rO > rQ and (r_diff == c_diff):
        if cO > cQ:
             res = min(n - cO + 1, n - rO + 1)
        elif cO < cQ:
             res = min(cO, n - rO + 1)
    elif rO < rQ and (r_diff == c_diff):
        if cO > cQ:
             res = min(n - cO + 1, rO)
        elif cO < cQ:
             res = min(cO, rO)
    return res
def pointNearToQueen(rQ, cQ, rO, cO, n, arr):
    r_diff = abs(rQ-rO)
    c_diff = abs(cQ-cO)
    if rO == rQ:
         if cO > cQ:
             if cO < arr[0]['c'] or arr[0]['c'] == -1:
                 arr[0]['c'] = cO
                 arr[0]['r'] = rO
         elif cO < cQ:
             if cO > arr[4]['c'] or arr[4]['c'] == -1:
                 arr[4]['c'] = cO
                 arr[4]['r'] = rO
    elif cO == cQ:
        if rO > rQ:
            if rO < arr[6]['r'] or arr[6]['c'] == -1:
                arr[6]['r'] = rO
                arr[6]['c'] = cO
        elif rO < rQ:
            if rO > arr[2]['r'] or arr[2]['c'] == -1:
                arr[2]['r'] = rO
                arr[2]['c'] = cO
    elif rO > rQ and (r_diff == c_diff):
        if cO > cQ:
            if rO < arr[7]['r'] or arr[7]['c'] == -1:
                arr[7]['r'] = rO
                arr[7]['c'] = cO
        elif cO < cQ:
            if rO < arr[5]['r'] or arr[5]['c'] == -1:
                arr[5]['r'] = rO
                arr[5]['c'] = cO
    elif rO < rQ and (r_diff == c_diff):
        if cO > cQ:
            if rO > arr[1]['r'] or arr[1]['c'] == -1:
                arr[1]['c'] = cO
                arr[1]['r'] = rO
        elif cO < cQ:
             if rO > arr[3]['r'] or arr[3]['c'] == -1:
                arr[3]['c'] = cO
                arr[3]['r'] = rO
    return arr
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]
columns_right = n-cQueen
columns_left = cQueen-1
rows_up = n-rQueen
rows_down = rQueen-1
diagnol_top_right = min(columns_right, rows_up)
diagnol_bottom_right = min(columns_right, rows_down)
diagnol_bottom_left = min(rows_down, columns_left)
diagnol_top_left = min(columns_left, rows_up)
total_possibilities = columns_right+columns_left+rows_down+rows_up+diagnol_top_left+diagnol_top_right+diagnol_bottom_right+diagnol_bottom_left
#arr = [{'r': rQueen,'c': n}, {'r': 1,'c': n}, {'r': 1,'c':cQueen}, {'r': 1, 'c': 1}, {'r':rQueen, 'c': 1}, {'r': n,'c': 1}, {'r': n, 'c': cQueen}, {'r':n, 'c':n}]
arr = [{'r':-1, 'c': -1} for i in range(8)]
for a0 in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    arr = pointNearToQueen(rQueen, cQueen, rObstacle, cObstacle, n, arr)
if k > 0:
    for p in arr:
        if p['r'] != -1:
            total_possibilities -= positionToBeRemoved(rQueen, cQueen, p['r'], p['c'], n)
print(total_possibilities)
