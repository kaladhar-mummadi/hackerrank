t = int(input())

for a0 in range(t):
    n = int(input())
    f = n
    t = 0
    while f >= 0:
        if f % 3 == 0 and t % 5 == 0:
            print("5" * f, "3" * t, sep='')
            break
        elif f == 0 and t % 5 == 0:
            print("5" * f)
        elif f == 0:
            print("-1")
        f = f - 1
        t = t + 1
