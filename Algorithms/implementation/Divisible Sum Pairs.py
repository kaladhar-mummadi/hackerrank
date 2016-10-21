"""
https://www.hackerrank.com/challenges/divisible-sum-pairs
"""
def sum(arr, n, k):
    i = 0
    res = 0
    while i < n:
        j = i + 1
        while j<n:
            if (arr[i]+arr[j]) % k == 0 :
                res += 1
            j += 1
        i += 1
    return res
if __name__ == '__main__':
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    print(sum(a, n, k))