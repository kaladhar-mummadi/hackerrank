if __name__ == '__main__':
    n,m = input().split(' ')
    n,m = [int(n), int(m)]
    arr = [int(temp) for temp in input().split(' ')]
    arr.sort()
    maxDiff = 0
    i = 0
    firstDiff = abs(arr[0]- 0)
    while i < m - 1:
        diff = abs(arr[i] - arr[i + 1])
        if maxDiff < diff:
            maxDiff = diff
        i += 1
    lastDiff = abs(arr[-1] - n + 1)
    midDiff = maxDiff // 2
    if n == m:
        print(0)
    else:
        print(max([firstDiff, midDiff, lastDiff]))