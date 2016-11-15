"""
https://www.hackerrank.com/challenges/bon-appetit
"""
def calcDiff(arr, k):
    res = 0
    for val in arr:
        res += val
    res -= arr[k]
    if (res//2) == sum:
        print("Bon Appetit")
    else:
        temp = res//2
        print(abs(temp - sum))
if __name__ == '__main__':
    n,k = input().split(' ')
    n,k = [int(n), int(k)]
    arr = [int(temp) for temp in input().split(' ')]
    sum = int(input())
    calcDiff(arr, k)