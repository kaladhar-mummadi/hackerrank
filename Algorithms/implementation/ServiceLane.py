n, t = [int(a_temp) for a_temp in input().strip().split(' ')]
widthArr = [int(a_temp) for a_temp in input().strip().split(' ')]

for a0 in range(t):
    i, j = [int(a_temp) for a_temp in input().strip().split(' ')]
    print(min(widthArr[i:j + 1]))
