#https://www.hackerrank.com/challenges/sock-merchant
def pairs(n, arr):
    vals = [0]*100
    i = 0
    while i < n:
        vals[arr[i] - 1] += 1
        i += 1
    i = 0
    res = 0
    while i < 100:
        q = vals[i] // 2
        res += q

        i += 1
    return res


if __name__ == '__main__':
    n = int(input())
    arr = [int(temp) for temp in input().split(' ')]
    print(pairs(n, arr))