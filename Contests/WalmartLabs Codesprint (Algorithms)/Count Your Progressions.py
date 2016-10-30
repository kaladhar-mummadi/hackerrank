import math

def ncr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
mod = 1000000009
def getModForPwer(n, times):
    global mod
    i = 1
    res = n
    while i < times:
        res *= n
        res %= mod
        i += 1
    return res
n = int(input())
arr = [0] * 101
for _ in range(n):
    temp = int(input())
    arr[temp] += 1
res = 0
i = 1

while i < 101:
    if arr[i] == 0:
        i += 1
        continue
    res += getModForPwer(2, arr[i])
    res -= 1
    res %= mod
    i += 1
i = 1
mulRes = 1
while i<101:
    j = i
    sum = 0
    numberOfelement = 0
    while j < 101:
        if sum !=0 and arr[j] == 0:
            break
        if arr[j] !=0 :
            numberOfelement += 1
        sum += arr[j]
        j += i
    if sum !=0 and numberOfelement > 1:
        k = 0
        k = 2
        while k <= numberOfelement:
            res += int(ncr(sum, k))
            res %= mod
            k +=1
        # res += getModForPwer(2, sum)
        # res -= sum
        # res -= 1
    i += 1
total = res+mulRes + 1
print(res)