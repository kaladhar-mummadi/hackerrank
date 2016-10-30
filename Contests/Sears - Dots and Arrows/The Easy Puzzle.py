def gcd(a,b):
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a
def lcm(small, large):
    if small > large :
        temp = large
        large = small
        small = temp
    elif small == large:
        return small
    largeMultiple = large
    while largeMultiple % small != 0:
        largeMultiple += large
    return  largeMultiple

def lcmTwo(a,b):
    return ((a * b) // gcd(a,b))
T = int(input())
for _ in range(T):
    N, K = input().split(' ')
    N, K = [int(N), int(K)]
    arr = [int(temp) for temp in input().split(' ')]
    i = 2
    if len(arr) > 1:
        totlalLcm = lcmTwo(arr[0], arr[1])
        while i < len(arr):
            lcmTwo(totlalLcm, arr[i])
            i += 1
    else:
        totlalLcm = arr[0]
    if totlalLcm % K == 0:
        print("YES")
    else:
        print("NO")

