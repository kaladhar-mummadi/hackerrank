MOD = 1000000007
def pow(a, b):
    x = 1
    y = a
    while b > 0:
        if b%2 == 1:
            x = x*y
            if x > MOD:
                x %= MOD
        y = y*y
        if y > MOD:
            y %= MOD
        b //= 2
    return x
def inverseEuler(n):
    return pow(n, MOD-2)
def c(n,r):
    f = [1]*(n+1)
    i = 2
    while i <= n:
        f[i] = (f[i-1]*i) % MOD
        i += 1
    return (f[n]*(inverseEuler(f[r]) * inverseEuler(f[n-r])) % MOD) % MOD

p = int(input())

for _ in range(p):
    m, n = input().split(' ')
    m, n = [int(m), int(n)]
    combs = c(m, n)
    combs = (combs * n) % MOD
    res = combs - (n - 1)
    print(res)