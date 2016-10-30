import math

def ncr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
if __name__ == '__main__':
    n = int(input())
    x = int(input())
    i = 0
    midPoint = (n)//2
    res = 0
    last = 0
    while i <=  midPoint:
        last = int(ncr(n,i))
        res += last
        i += 1
    res *=2
    if n%2 == 0:
        res -= last
    res -= 1
    print(abs(res-x))